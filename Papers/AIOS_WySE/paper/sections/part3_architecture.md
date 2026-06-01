# Part III: The Architecture (What Must Be Built)

> **Reading Guide:** Part III is written primarily for **[E] Expert** readers — systems architects,
> kernel engineers, and AI infrastructure researchers with familiarity with operating systems
> internals and formal methods. Callout boxes marked **[P] Practitioner** surface design-relevant
> conclusions for engineers who may skip the formal derivations. All section-local reference numbers
> are of the form [III-N] and will be renumbered globally in the combined draft.

---

## 8. Engineering Requirements

The architecture of an AI operating system is not a blank canvas. A set of obligations — some
inherited from classical OS theory, some novel to AI — constrains the design space before the first
component diagram is drawn. This section enumerates nine requirements with enough mechanical
specificity that an implementer can make concrete design decisions from them, not merely recognize
them as desiderata.

The first seven requirements retain the structure of prior surveys [III-1] but are expanded here
with specific mechanisms. Requirements eight and nine are introduced for the first time in this
report and reflect problems that have no classical OS analogue.

### 8.1 R1: Trusted Substrate

An AI-native OS must begin with a hardware root of trust and maintain that trust boundary through
the entire boot sequence into runtime operation. The AI control plane — however sophisticated —
inherits the trust properties of the substrate on which it runs. If the substrate is compromised,
no amount of AI governance recovers security.

The trusted substrate encompasses four responsibilities: **secure boot**, **hardware-enforced
isolation between execution domains**, **interrupt and exception handling**, and **device access
mediation**. Each must remain under the authority of conventional, auditable, and ideally
formally-verified software — not the AI control plane itself.

Concretely: the boot sequence must extend from a hardware root of trust (TPM 2.0 or equivalent
attestation anchor) through firmware (UEFI with Secure Boot) through the bootloader (GRUB or
equivalents) to kernel initialization. This chain produces a measurement log that can be
verified remotely. The AI control plane must not be able to modify boot configuration or inject
code below the point at which it is itself loaded.

The substrate may be instantiated as a conventional monolithic kernel (Linux, Windows NT), a
real-time operating system (VxWorks, Zephyr), a hypervisor (KVM, Xen), or a formally-verified
microkernel (seL4 [III-2]). The choice depends on the deployment tier: data center workloads can
tolerate the performance profile of Linux KVM; safety-critical embedded deployments (avionics,
automotive) require a certifiable substrate. The requirement is that *something* owns the
boot-to-runtime trust boundary and that something is not the AI control plane.

The seL4 microkernel is the only production OS kernel with a complete formal verification proof
(~20 person-years of effort for approximately 10,000 lines of C [III-3]). This is the correct
substrate for the highest-assurance deployments but imposes a severe integration cost. For
near-term deployments, Linux with Secure Boot, measured boot, and a TPM-anchored attestation
chain is the credible path.

> **[P] Practitioner Note — Substrate Selection Decision Tree**
> Choose substrate based on worst-case isolation requirement, not average-case AI workload:
> - Consumer device / enterprise desktop: Linux or Windows with Secure Boot + TPM 2.0
> - Cloud tenant isolation: KVM or Xen hypervisor as substrate; AI control plane in guest
> - Embedded AI with safety requirements: RTOS partition (ARINC 653 or ISO 26262 domain) for
>   safety-critical functions; AI advisory services in a separate unprivileged partition
> - Maximum assurance (classified, safety-critical): seL4 or equivalent, accepting high
>   verification cost

### 8.2 R2: AI Runtime and Resource Manager

Agent-based workloads expose resource management demands that are qualitatively different from
conventional processes. A web server's resource consumption is predictable; an LLM agent's is
not. The agent's token generation rate, memory footprint, and tool-call frequency depend on the
input content, the model's internal reasoning trajectory, and the number of parallel subagents
spawned — none of which is statically knowable.

The AI runtime and resource manager is responsible for four functions:

**Scheduling.** Which agent executes when, and on which hardware. Unlike CPU scheduling, where
the scheduler dispatches threads of nanosecond-to-millisecond granularity, AI scheduling must
account for inference phase (prefill is memory-bandwidth-bound; decode is compute-bound [III-4]),
model loading latency (a 70B-parameter model at bf16 precision occupies approximately 140 GB of
memory, requiring non-trivial load time), and tool-call boundaries (logical points at which an
agent yields while waiting for an external response).

The AIOS system demonstrated at COLM 2025 [III-5] quantified the value of dedicated agent
scheduling: a 2.1x improvement in agent execution throughput compared to baseline execution
without a specialized scheduler. AgentCgroup [III-6] established an equally important result from
the opposite direction: OS execution overhead — wait time in kernel scheduling queues, syscall
processing, memory management — accounts for 56 to 74 percent of end-to-end agent task latency.
The runtime layer is not a performance optimization; it is a performance-critical component.

**Context management.** KV cache management is the central resource allocation problem for
transformer-based agents. The KV cache for a single 128K-token context at bf16 precision in a
7B model can exceed 4 GB per layer; for a 70B model, it is proportionally larger. Multiple
concurrent agents create cache pressure that the kernel's conventional memory manager has no
semantic basis to resolve: it cannot distinguish a KV cache from heap memory. The AI runtime
must make eviction decisions informed by agent priority, expected token generation remaining, and
the cost of recomputing versus evicting.

**Memory management.** The AI runtime manages working set reservation — ensuring each agent has
sufficient memory for its current context without starving other agents or the kernel itself.
This includes integration with cgroup v2 memory controllers for hard limits and integration with
the system memory manager for pressure signaling.

**Access control.** Agents must not access models, tools, or data stores they are not authorized
to use. The runtime enforces a per-agent capability manifest checked at execution time, not
relying solely on OS-level process permissions (which are coarse-grained relative to the agent
permission model).

### 8.3 R3: Tool and Interoperability Layers

An AI-native OS must provide a stable, standardized interface through which agents invoke
external capabilities — tools, data sources, other agents, and external services. This interface
layer is the AI-OS analogue of the POSIX system call table: it defines what the layer above can
request from the layer below.

Two protocol families currently compete for this role. **MCP (Model Context Protocol)** [III-7],
introduced by Anthropic and now standardized with the November 2025 specification update, governs
model-to-tool connections. The current specification includes: asynchronous task execution (an
agent can initiate a long-running tool call and continue executing), parallel tool invocations,
server-initiated sampling (a tool server can request additional model inference), and structured
progress notification. The 97M+ monthly SDK downloads as of early 2026 indicate adoption at a
scale that makes it difficult to ignore in an interoperability strategy.

**A2A (Agent-to-Agent protocol)** [III-8], contributed to the Linux Foundation in June 2025,
governs agent-to-agent communication: task delegation, status reporting, and capability
advertisement between independently deployed agents. A2A addresses the multi-agent coordination
layer that MCP does not reach.

The NIST AI Agent Standards Initiative [III-9], announced in February 2026, represents emerging
federal standardization pressure toward a coherent interface taxonomy. For government deployments
— particularly the NNSA and DARPA contexts relevant to this work — NIST-alignment is not
optional; it is a procurement and compliance requirement.

The architectural implication: the AI-OS must treat MCP and A2A as infrastructure, not as
application-layer concerns. Agent tool invocation security, rate limiting, audit logging, and
capability checking must be enforced at the interoperability layer, not left to individual agent
implementations.

### 8.4 R4: Model Lifecycle Management

AI models are not static binaries. A trained model may be fine-tuned, adapted with LoRA
adapters, quantized for deployment, updated based on user feedback, or rolled back after a
behavioral regression. None of this has a direct analogue in conventional OS software management,
where a kernel module is compiled, signed, and loaded — and its behavior is fixed.

Model lifecycle management encompasses six concerns:

**Evaluation.** A model version must pass behavioral evaluation before promotion to production.
This requires benchmark harnesses, regression test suites, and — for safety-critical deployments
— formal behavioral specifications against which the model can be checked.

**Provenance.** The lineage of a model must be trackable: from training data, through training
run, through fine-tuning stages, to deployment. This is the supply chain security problem applied
to neural network weights.

**Rollback.** When a model update produces degraded behavior, the system must revert to a
previous version. Unlike a software rollback, model rollback may require state migration: agent
contexts built against the old model's behavior may be incompatible with the rolled-back version.

**Monitoring.** Deployed models drift over time as input distributions shift. The system must
measure output consistency against expected behavioral envelopes (this maps directly to the
behavioral morphism quality metric C_r defined in Section 13.3).

**Adaptation.** Transfer learning and continual learning allow models to adapt to deployment
context. But adaptation without governance is a destabilization risk: a model that updates itself
based on agent interactions can develop unexpected behaviors. The lifecycle manager must bound
the rate and scope of in-deployment adaptation.

**Drift control.** Structural drift (S_a degradation, defined in Section 13.2) occurs when the
model's internal state representation diverges from the system's expected state space. Behavioral
drift (C_r degradation) occurs when model outputs diverge from expected behavioral envelopes.
Both must be monitored continuously, not just at deployment time.

### 8.5 R5: Hardware-Aware Heterogeneous Scheduler

The compute substrate of a modern AI-capable system is not a homogeneous pool of CPU cores. It
is a heterogeneous fabric comprising CPUs, GPUs, neural processing units (NPUs), data processing
units (DPUs), and — in server-class deployments — CXL-attached disaggregated memory. Scheduling
AI workloads across this fabric requires semantic knowledge that conventional schedulers lack.

Agent.xpu [III-10] addresses the scheduling problem for agentic workloads across CPU/NPU/iGPU
configurations using a two-tier asynchronous scheduling architecture. The outer tier routes agent
workloads to the appropriate hardware domain; the inner tier uses hardware-specific coroutine
mechanisms to maximize utilization within each domain. This is the right structural approach, but
several hard problems remain unsolved:

**Latency guarantees.** Inference latency is phase-dependent: prefill (processing the input
prompt) is memory-bandwidth-bound and scales with input length; decode (generating each output
token) is compute-bound and scales with model size and batch configuration. Providing latency
guarantees across both phases simultaneously, against a heterogeneous hardware background, has
no satisfactory solution in the current literature.

**Preemption semantics.** CPU preemption is fine-grained (microsecond context switches).
GPU preemption is coarse-grained: current CUDA scheduling does not support preemption within a
kernel launch; preemption requires completing the current SM-level kernel or implementing
software-level preemption at significantly higher overhead. NPU preemption is vendor-dependent
and typically not available at all on edge NPUs. This asymmetry means that a scheduler that
preempts an agent mid-inference on a GPU incurs substantially different overhead than preempting
a CPU thread.

**Memory pressure from model loading.** A 70B model at bf16 precision requires approximately
140 GB of GPU memory. Loading and unloading models in response to workload changes takes seconds
to minutes depending on memory bandwidth — time scales that are incompatible with interactive
scheduling. The KV cache compounds this: for long-context workloads, KV cache allocation can
exceed model weight memory. The scheduler must reason about memory as a first-class scheduling
constraint, not as a secondary resource.

**Dual-scheduler conflict.** The AI runtime scheduler and the kernel scheduler operate at
different semantic levels. When the AI scheduler decides that agent A should execute on GPU-0
but the kernel scheduler has not yet dispatched the associated process to a CPU core with PCIe
affinity to GPU-0, resource locality is lost. Resolving dual-scheduler conflicts requires the
downward API described in Section 9.2: the AI scheduler communicates scheduling intent to the
kernel, which adapts its decisions accordingly.

> **[P] Practitioner Note — Near-Term Scheduler Architecture**
> For prototype deployments on Linux, the practical path is:
> - `sched_ext` for AI-aware CPU scheduling policy (BPF-based, production-ready as of Linux 6.12)
> - NVIDIA MIG or AMD MI300X partition schemes for GPU isolation
> - cgroup v2 unified hierarchy aligned to agent task boundaries (not container boundaries)
> - `io_uring` for batched async I/O from agent tool calls
> This combination covers the near-term case without requiring kernel modifications.

### 8.6 R6: Operator Control and Auditability

An AI-native OS must provide mechanisms for human operators to observe, override, and audit the
behavior of the AI control plane. This is not a soft requirement or a compliance checkbox. In
a system where AI makes resource allocation, scheduling, and security policy decisions, the
absence of auditable human override is an argument-ending safety failure.

**Override.** The operator must be able to: suspend the AI control plane and revert to
conventional fallback mode (Section 12.3); override specific AI policy decisions with manual
directives; and terminate individual agents without requiring the AI control plane's cooperation.
The override mechanism must operate at kernel privilege, not through the AI control plane's own
API — it must work even when the AI control plane is compromised or unresponsive.

**Audit trails.** PunkGo / Right to History [III-11] demonstrates that tamper-evident audit
logging can be implemented as a kernel primitive with sub-1.3 millisecond action latency using
RFC 6962 Merkle tree structures. The Merkle tree approach provides logarithmic-size inclusion
proofs: an auditor can verify that a specific action was (or was not) recorded without replaying
the entire log. This is the correct implementation model for AI-OS audit trails.

**Transparency.** The operator must be able to query the current state of the AI control plane:
which agents are active, which resources are allocated, what the current policy configuration is,
and what the current morphism quality metrics (S_a, C_r) are. This requires a structured
observation interface, not just log inspection.

### 8.7 R7: Risk Management and Governance

The NIST AI Risk Management Framework [III-12] defines eight dimensions of AI trustworthiness:
validity, reliability, safety, security, resilience, transparency, explainability, privacy, and
bias management. These are the correct categories. They are not, however, a design specification.
An OS architect cannot derive a system call API from "manage bias." The NIST AI RMF is a risk
framework, not an OS specification — it identifies what must be addressed without specifying
how it must be addressed at the OS level.

For an AI-native OS, each NIST dimension maps to specific OS-level mechanisms:

- **Validity and reliability** → model lifecycle management (R4) and behavioral monitoring (S_a,
  C_r)
- **Safety** → Circuit Breaker watchdog (Section 13.4), conventional fallback mode (Section 12.3)
- **Security** → threat model and isolation tiers (Section 11)
- **Resilience** → failure taxonomy and recovery (Section 12)
- **Transparency and explainability** → tamper-evident provenance, PROV-O audit trail (Section
  11.5)
- **Privacy** → confidential computing substrate (Section 11.6), agent isolation (Section 11.2)
- **Bias management** → model evaluation pipeline (R4), behavioral drift monitoring

The architectural design principle is: NIST AI RMF sets the *required* properties; the AI-OS
architecture specifies the *mechanisms* that realize those properties. Governance frameworks that
remain at the property level without specifying mechanisms are incomplete as design inputs.

### 8.8 R8 [NEW]: Agent State Management

This is the hardest novel OS problem introduced by AI-native computing. It has no satisfactory
solution in the existing literature, and its difficulty is structural, not incidental.

A conventional OS process has two primary state components: a virtual address space and an open
file descriptor table. The OS knows how to checkpoint, migrate, and restore these components
because their semantics are fully specified by the programming model. A process's state at any
moment is exactly its register file and memory contents.

An AI agent's state has five distinct components, each with different lifecycle semantics,
ownership requirements, and persistence implications:

1. **Execution context.** The agent's current task specification, active tool bindings, in-flight
   function call results awaiting integration, and the current position in a multi-step plan.
   This state is volatile: it is created at agent launch and is meaningless after task completion.
   It must be checkpointed for agent migration but need not persist across sessions.

2. **Episodic memory.** The agent's recent interaction history and the transformer KV cache that
   encodes it. This state grows during a session and is subject to eviction under memory pressure.
   It must persist within a session for coherent behavior; across sessions, it may be archived or
   discarded depending on application requirements.

3. **Semantic memory.** Facts retrieved from RAG indices, learned associations accumulated over
   the agent's operational lifetime, and pointer structures into external knowledge bases. This
   state must be durable and versioned: it represents the agent's accumulated knowledge and losing
   it represents a capability regression.

4. **Goal state.** The agent's current objectives, subgoal decomposition structure, pending
   commitments to other agents, and delegated tasks in progress. This state must be durable and
   strongly consistent: an agent whose goal state is lost mid-execution may take contradictory or
   dangerous actions when it resumes.

5. **Resource bindings.** Open file descriptors, GPU memory allocations, live network connections,
   API session tokens, and any other kernel-managed or externally-managed resources the agent
   holds. This state is volatile in the sense that most bindings cannot be serialized and
   migrated — they must be released on suspension and re-acquired on resume.

None of these five components maps cleanly to the Unix process model. A process has file
descriptors and memory; an agent has all that plus mutable cognitive state that is opaque to the
kernel. The kernel cannot make intelligent eviction decisions over a KV cache because it does not
know what a KV cache *is* — it sees anonymous heap memory.

This is the fundamental design tension: the state components that matter most for agent behavior
are exactly the ones the kernel is least equipped to manage. Resolving this tension requires
either enriching the kernel's semantic understanding of agent state (invasive, violating the
separation of mechanism and policy) or providing a user-space state management service with
a well-defined kernel interface for eviction signaling and priority hints (architecturally
cleaner, but requiring coordination between user space and kernel that does not currently exist).

Section 10 develops the full agent state architecture, including storage substrates, ownership
semantics, and consistency requirements for each category.

> **[P] Practitioner Note — Near-Term State Management**
> While the full agent state architecture is under-specified in the literature, the near-term
> pragmatic approach is:
> - Execution context: serialized to JSON on a fast local store (Redis with persistence) at
>   checkpoint boundaries (tool-call boundaries are natural checkpoint points)
> - KV cache: managed by the inference engine (vLLM, TGI) with LRU eviction; accept that evicted
>   cache is not recoverable without recomputation
> - Semantic memory: dedicated vector database (Qdrant, Weaviate) with versioned snapshots
> - Goal state: durable key-value store with linearizable consistency (etcd, FoundationDB)
> - Resource bindings: released and re-acquired; do not attempt serialization

### 8.9 R9 [NEW]: Energy and Thermal Governance

Modern AI-capable systems-on-chip — the Apple M4, Qualcomm Snapdragon X Elite, and NVIDIA
Jetson Orin represent the current generation — have complex thermal and power envelopes in which
AI inference directly competes with OS overhead for thermal headroom. Without thermal-aware
scheduling, power management becomes reactive: the hardware throttles unexpectedly, inference
latency spikes, and the system behaves non-deterministically from the application's perspective.

The problem is particularly acute in edge deployments. A Jetson Orin module in its standard
thermal profile will throttle GPU clock speeds when die temperature exceeds 75°C. An AI agent
performing intensive inference may sustain die temperatures near this threshold; background OS
operations — interrupt processing, memory management, network I/O — add thermal load that can
push the SoC over the threshold and trigger throttling at precisely the moment where the agent
requires consistent inference latency.

Thermal governance requires the AI-OS scheduler to treat thermal state as a first-class scheduling
signal, not as an out-of-band hardware event. Concretely:

- The scheduler must receive continuous thermal zone readings from the SoC thermal management
  interface (Linux `thermal_zone` sysfs or equivalent)
- When thermal state approaches the throttle threshold, the scheduler must proactively reduce
  inference intensity — by reducing batch size, deferring non-critical agent tasks, or migrating
  workloads to cooler compute domains — before hardware throttling occurs
- Power capping constraints (RAPL on Intel, PPAS on Apple Silicon, JTOP on Jetson) must be
  integrated into the scheduling budget, not treated as exceptional conditions
- For battery-powered edge devices, inference scheduling must cooperate with power management
  policies (ACPI, platform PM drivers) to avoid draining battery in ways that compromise OS
  responsiveness

This requirement has no direct analogue in conventional OS scheduling theory, where CPU and memory
are the primary scheduling resources and thermal state is managed transparently by hardware. The
intersection of high-intensity AI inference with OS resource management forces thermal state into
explicit scheduling consideration.

---

## 9. The AI-Kernel Interface Contract

### 9.1 Why the Interface Is the Architecture

Layered software systems stand or fall on the quality of the interfaces between their layers.
The TCP/IP protocol suite works because the interface between IP and TCP is precisely specified;
IP does not need to know what TCP is doing, and TCP does not need to know how IP routes packets.
POSIX works because the interface between kernel and application is defined with enough precision
that application software can be written without knowledge of kernel implementation.

The recommended architecture for an AI-native OS — a Type B system in the taxonomy of Section
7 — places an AI-native control plane above a conventional substrate. This is a layered claim:
the AI control plane provides policy; the substrate provides mechanism; the interface between
them governs their interaction. But a layered architecture without a specified interface is not
an architecture — it is an aspiration. Prior treatments of this problem [III-1, III-13] have
named the control plane concept without specifying the API. This section specifies it.

The interface contract must answer four questions:

1. What does the AI control plane tell the kernel? (downward API)
2. What does the kernel tell the AI control plane? (upward API)
3. Where does the policy/mechanism boundary fall?
4. What happens when the two layers disagree?

A fifth question — what happens when the AI control plane fails? — is answered in the failure
taxonomy of Section 12.

### 9.2 Downward API: AI Control Plane to Kernel

The downward API carries scheduling intent, resource reservation requests, hardware binding
directives, and audit log entries from the AI control plane to the kernel. The kernel treats
these as *hints with authority*: the kernel retains final discretion over safety-critical
decisions (preventing OOM, enforcing memory isolation, maintaining scheduler fairness invariants)
but biases its behavior toward the AI control plane's expressed preferences when no safety
invariant is at stake.

The following defines candidate primitives in a pseudo-IDL notation. These are illustrative
design candidates, not a finalized specification.

```idl
// ============================================================
// AIOS Downward API — AI Control Plane to Kernel
// Candidate Primitives v0.1 (illustrative)
// ============================================================

// --- Scheduling Intent ---

// Communicate scheduling preference for a workload unit.
// The kernel MAY honor this hint; it MUST honor it if no safety
// invariant is violated.
//
// workload_id:      Opaque identifier for the agent/inference job
// latency_budget_ns: Maximum tolerable scheduling delay in nanoseconds
// priority_class:   One of {REALTIME, HIGH, NORMAL, BEST_EFFORT, BACKGROUND}
// preferred_cpu_set: CPU affinity mask (0 = no preference)
//
// Returns: AIOS_OK | AIOS_HINT_REJECTED | AIOS_PARTIAL (partial satisfaction)
status_t aios_sched_hint(
    workload_id_t  workload_id,
    uint64_t       latency_budget_ns,
    priority_class_t priority_class,
    cpu_set_t      preferred_cpu_set
);

// Notify kernel that a workload is entering a blocking phase
// (e.g., waiting for tool call result, network I/O).
// Allows kernel to yield the CPU immediately rather than spinning
// for the next scheduling quantum.
//
// estimated_block_ns: Expected blocking duration; 0 = unknown
status_t aios_sched_yield_hint(
    workload_id_t  workload_id,
    uint64_t       estimated_block_ns
);

// --- Memory Reservation ---

// Reserve memory for an agent's working set with a specified
// eviction policy. The kernel guarantees this allocation will
// not be evicted unless the hard_limit is reached.
//
// agent_id:         Unique agent identifier
// working_set_bytes: Soft reservation (kernel best-effort)
// hard_limit_bytes:  Hard cap (kernel enforced; agent killed if exceeded)
// eviction_policy:  One of {EVICT_LRU, EVICT_CHECKPOINT_FIRST,
//                           EVICT_REJECT_NEW, EVICT_KILL_LOWEST}
//
// Returns: reservation_handle (opaque; used in subsequent calls)
//          or AIOS_ENOMEM if hard_limit cannot be satisfied
reservation_handle_t aios_mem_reserve(
    agent_id_t       agent_id,
    size_t           working_set_bytes,
    size_t           hard_limit_bytes,
    eviction_policy_t eviction_policy
);

// Release a memory reservation. Agent signals it no longer needs
// the reserved working set (e.g., task complete, agent suspended).
status_t aios_mem_release(
    reservation_handle_t handle
);

// Notify the kernel that a specific memory region contains
// AI-semantic content (KV cache, model weights, RAG buffer)
// and should be treated as a unit for eviction accounting.
// This allows the kernel's eviction policy to align with the
// AI runtime's eviction preferences.
//
// region_type: One of {KV_CACHE, MODEL_WEIGHTS, RAG_BUFFER,
//                      GOAL_STATE, EPISODIC_LOG}
// priority:    Eviction priority (lower = evict first)
status_t aios_mem_annotate(
    void*            region_base,
    size_t           region_size,
    mem_region_type_t region_type,
    uint32_t         eviction_priority
);

// --- Hardware Partition Binding ---

// Bind an agent to specific hardware partitions.
// The kernel enforces this binding for the duration of the fence.
// An agent executing outside its fenced partition is a policy violation.
//
// gpu_partition:   GPU Memory Instance Group (MIG) slice or -1 for no constraint
// npu_queue:       NPU dispatch queue identifier or -1 for no constraint
// numa_node:       NUMA node affinity or -1 for no constraint
//
// Returns: fence_handle (used to release binding)
fence_handle_t aios_resource_fence(
    agent_id_t  agent_id,
    cpu_set_t   cpu_affinity,
    int32_t     gpu_partition,
    int32_t     npu_queue,
    int32_t     numa_node
);

// Release a resource fence (agent task complete or migrating).
status_t aios_resource_fence_release(
    fence_handle_t handle
);

// --- Kernel-Enforced Immutable Audit ---

// Submit an audit event to the kernel-maintained tamper-evident
// log. The kernel appends the event to the Merkle tree log structure
// and returns the log sequence number and the Merkle root after
// inclusion. This call executes in kernel context and cannot be
// suppressed or forged by user-space code.
//
// event_type:   Enumerated event classification
//               (AGENT_LAUNCH, TOOL_INVOCATION, POLICY_DECISION,
//                MODEL_LOAD, RESOURCE_ALLOCATION, SECURITY_EVENT,
//                OPERATOR_OVERRIDE, CIRCUIT_BREAKER_TRIP)
// agent_id:     Agent responsible for the event (may be null for system events)
// action_hash:  SHA-256 hash of the action record (caller computes)
// payload_len:  Length of optional structured payload (0-4096 bytes)
// payload:      Optional structured payload (caller-allocated, kernel-copied)
//
// Returns: log_sequence_number (monotonically increasing)
//          merkle_root (current root after inclusion)
struct aios_audit_result {
    uint64_t log_sequence_number;
    uint8_t  merkle_root[32];       // SHA-256
};

aios_audit_result aios_audit_log(
    event_type_t  event_type,
    agent_id_t    agent_id,
    uint8_t       action_hash[32],
    size_t        payload_len,
    const void*   payload
);

// --- Thermal and Power Governance ---

// Declare an inference workload's power budget claim.
// The scheduler uses this to coordinate thermal load across
// simultaneous inference jobs.
//
// power_budget_mw: Maximum sustained power consumption (milliwatts)
// duration_hint_ms: Expected duration of inference job (0 = unknown)
status_t aios_power_budget_claim(
    workload_id_t workload_id,
    uint32_t      power_budget_mw,
    uint32_t      duration_hint_ms
);
```

### 9.3 Upward API: Kernel to AI Control Plane

The upward API carries resource availability signals, security events, memory pressure
notifications, and lifecycle events from the kernel to the AI control plane. The AI control
plane is a subscriber to this event stream; it receives notifications and responds with policy
decisions expressed via the downward API.

The upward API is a structured event notification interface. The following categories of events
must be delivered:

**Resource availability signals.** Continuous telemetry on hardware resource state: CPU
utilization per-core and per-NUMA-node, memory pressure (free pages, swap rate, cgroup memory
usage relative to limits), GPU queue depth and utilization per MIG partition, NPU availability,
network interface queue depth, and thermal zone temperatures per hardware domain. These signals
are delivered on a configurable polling interval (typical: 100ms) and as threshold-crossing
notifications when values exceed defined bounds.

**Security events.** Anomalous system call patterns from agent processes (delivered via eBPF
hook or seccomp notification), privilege escalation attempts (capability requests outside the
agent's granted capability set), capability violations (file access outside Landlock-granted
domain, network connection to undeclared destination), and cross-agent memory access attempts
(write to a memory region annotated as belonging to a different agent).

**Memory pressure events.** Notification that the system is approaching OOM conditions, with
severity graduated as: WARNING (eviction candidates should be nominated), CRITICAL (eviction
must occur within the next scheduling cycle), and EMERGENCY (OOM killer is about to fire). The
AI control plane must respond to WARNING by nominating low-priority KV caches for eviction;
failing to respond within a deadline triggers automatic eviction ordered by the kernel's default
policy.

**Process and container lifecycle events.** Agent process crash notification with exit reason
(signal, OOM kill, resource limit exceeded), agent timeout notification (process exceeded its
allocated scheduling quantum by a configurable factor), container lifecycle transitions (start,
pause, stop, destroy) for containerized agents.

**Circuit Breaker events.** Delivered from the Circuit Breaker monitor (Section 13.4) to the
AI control plane: morphism quality metric updates (S_a and C_r values), threshold crossing
warnings, and trip notifications that indicate the Circuit Breaker has initiated transition to
conventional fallback mode.

### 9.4 Policy vs. Mechanism Boundary

The classical OS design principle — the kernel enforces mechanism; policy lives above the kernel —
applies directly to the AI-OS interface contract, with an important extension.

**Kernel-enforced mechanisms (immutable from the AI control plane's perspective):**
- Memory isolation between agents (cannot be overridden by the AI control plane)
- Scheduling quantum enforcement (an agent cannot hold a CPU core indefinitely; the kernel
  always retains preemption authority)
- Memory protection between address spaces (the AI control plane cannot grant one agent access to
  another agent's virtual address space)
- Audit log immutability (entries appended via `aios_audit_log` cannot be deleted or modified
  by any user-space entity, including the AI control plane)
- Hardware access mediation (an agent cannot access hardware directly; all hardware access is
  mediated by kernel drivers)

**AI control plane policies (expressed via downward API, honored subject to mechanism constraints):**
- Agent communication topology (which agents may invoke which other agents via A2A)
- Resource allocation priorities (scheduling hints, memory reservations, hardware partition
  assignments)
- Model selection for agent workloads (which model version handles which agent class)
- Workload placement across heterogeneous hardware (CPU vs. GPU vs. NPU decisions)
- Agent eviction ordering under memory pressure (which agents are suspended first)
- Security posture adjustments within permitted bounds (tightening Landlock restrictions,
  adding seccomp filters — but not removing kernel-level security mechanisms)

The critical design decision: the kernel can *always* override AI control plane policy decisions
when safety invariants are threatened. An AI control plane that allocates all memory to a
priority agent, starving the kernel's own memory pools, is overridden by the OOM killer. An AI
control plane that attempts to remove an audit log entry is denied. The AI control plane is
*advisory with authority* — its preferences are honored by default, but it is not sovereign.

This asymmetry is the safety argument for the Type B architecture. The conventional substrate
is always available to override AI policy decisions that would violate system safety invariants.

### 9.5 Existing Linux Insertion Points

The full interface contract described above does not exist as a deployed system. However, each
component has a credible insertion point in the current Linux kernel and user-space ecosystem.

**eBPF + sched_ext.** The `sched_ext` framework, merged into Linux 6.12, allows scheduling
policy to be implemented as BPF programs loaded by user space. This is the closest existing
mechanism to the AI control plane's downward scheduling API. AgentCgroup [III-6] already
demonstrates this path: the system uses `sched_ext` for CPU scheduling and `memcg_bpf_ops` for
memory control, with hierarchical cgroups aligned to tool-call boundaries rather than container
boundaries. The result is an agent-semantic resource partition visible to both the kernel and
the AI runtime. This is deployable today on Linux 6.12 or later.

**cgroups v2.** The unified cgroup v2 hierarchy provides hierarchical resource control for CPU
time, memory, and I/O bandwidth. The novel step for AI-OS is aligning cgroup boundaries to
*agent task boundaries* rather than process or container boundaries. An agent that spawns
subprocesses for tool execution should have all associated processes within a single cgroup
subtree; this allows resource accounting and limit enforcement at the agent level, not just the
process level.

**Landlock LSM.** Landlock [III-14] provides filesystem sandboxing based on capability tokens:
a process can only access filesystem paths that are explicitly granted in its Landlock ruleset.
This is the near-term mechanism for the tool capability model (Section 11.3). A tool server
receives a Landlock ruleset scoped to the specific filesystem paths it requires; any access
outside that ruleset is denied at kernel level without involving the AI control plane.

**seccomp-BPF.** System call filtering via BPF programs provides per-agent system call
restriction. An agent that should not have network access can be restricted to a seccomp profile
that blocks all socket-related syscalls. This is coarse-grained relative to the full capability
model, but it is available now and imposes negligible overhead.

**io_uring.** The io_uring interface provides asynchronous I/O submission and completion without
per-operation system call overhead. For agents that issue large numbers of tool-call I/O
operations, batching via io_uring reduces context-switch overhead — directly addressing the
56-74% kernel overhead figure from AgentCgroup [III-6].

**The gap.** These mechanisms are sufficient for near-term prototyping but collectively fall
short of the full interface contract in three ways: they lack agent-aware semantic understanding
of AI state (the kernel treats KV caches as anonymous memory), they do not provide formal
scheduling intent communication (sched_ext hints are BPF programs, not typed API calls), and
they have no cross-device scheduling coordination (CPU and GPU scheduling remain disconnected).
Closing these gaps is a medium-term research and engineering program, not a configuration task.

> **[P] Practitioner Note — What You Can Build Today**
> A near-term AIOS prototype on Linux 6.12+ can implement:
> - Agent-aligned cgroup v2 hierarchy (process grouping by agent, not by container)
> - sched_ext BPF scheduling policy (communicates priority and latency preference to kernel)
> - Landlock-based tool sandboxing (per-tool filesystem capability set)
> - seccomp-BPF per-agent syscall restriction profiles
> - eBPF-based audit trail with user-space Merkle tree accumulation
> This is a meaningful approximation of the full contract. Document the gaps explicitly so
> that the delta between prototype and full specification is traceable.

---

## 10. Agent State Architecture

### 10.1 The State Taxonomy

The five categories of agent state introduced in Section 8.8 have different storage, ownership,
and lifecycle requirements that must be independently designed. Treating them as a single
"agent memory" resource — as current frameworks tend to do — conflates fundamentally different
consistency and durability requirements.

**Table 1: Agent State Taxonomy**

| Category | Contents | Lifecycle | Consistency | Persistence |
|---|---|---|---|---|
| Execution context | Current task spec, tool bindings, in-flight call results, plan position | Created at launch; invalid after task completion | Not applicable (single-writer) | Volatile; checkpoint for migration |
| Episodic memory | Recent interaction history, transformer KV cache | Grows during session; evictable under pressure | Session-scoped coherence | Session-persistent; archivable |
| Semantic memory | RAG index pointers, learned associations, fact cache | Accumulated over agent lifetime | Eventual consistency acceptable | Durable; versioned |
| Goal state | Objectives, subgoal decomposition, pending commitments | Set by orchestrator; modified by planning | Strong consistency required | Durable until explicit change |
| Resource bindings | File descriptors, GPU memory, network connections, API sessions | Acquired during execution; released on completion | N/A (kernel-managed) | Volatile; re-acquire on resume |

This taxonomy has architectural consequences. Systems that collapse all five categories into a
single storage tier — a single Redis instance or a single vector database — make state management
simple at the cost of correctness. Goal state that is "eventually consistent" is a logical
error: an agent with a stale view of its goal structure may take actions inconsistent with its
actual objectives. Episodic memory that is "strongly consistent" wastes write latency on
consistency protocols that provide no safety benefit.

### 10.2 Storage Substrates Per Category

**Execution context** maps to in-process volatile memory for the live execution path, with
serialization to a fast durable store (Redis with AOF persistence, or equivalent) at checkpoint
boundaries. Tool-call boundaries are the natural checkpointing points: the agent is between
inference steps, its in-flight calls have completed or timed out, and its state can be
serialized without capturing mid-inference KV cache state. The checkpoint format must be
sufficient to reconstruct the agent's execution at a different node — this requires serializing
not just data but also the identity of active tool bindings.

**Episodic memory** presents the hardest storage design problem because the KV cache — the
most important component of episodic memory — is opaque to user-space storage systems. The
KV cache exists inside the inference engine (vLLM, TGI, llama.cpp) and cannot be extracted
and re-injected without coupling to the inference engine's internal representation. Current
research addresses KV cache sharing and migration: HeART [III-15] targets efficient KV cache
reuse across requests; Oaken [III-16] addresses KV cache memory management under pressure. Both
are active research problems with partial production deployments. The practical near-term answer
is: accept that KV cache is managed by the inference engine, provide the engine with priority
signals from the AI runtime (via the `aios_mem_annotate` primitive), and design agents that
can gracefully degrade when KV cache is evicted.

**Semantic memory** maps to a vector database with versioned snapshots. The versioning
requirement distinguishes this from a simple RAG index: the AI-OS must be able to roll back
to a previous semantic memory state if a model update or behavioral regression requires it.
Qdrant, Weaviate, and Milvus all support collection versioning; the AI-OS must enforce that
writes to semantic memory are tagged with agent identity and timestamp for provenance tracing.

**Goal state** requires a linearly consistent key-value store with durability guarantees:
etcd or FoundationDB are the appropriate substrates. The key requirement is linearizability
(reads reflect all prior writes; there is no possibility of reading a stale goal state that
could cause the agent to pursue an obsolete objective). Given that goal state changes relatively
infrequently — typically only when the orchestrator issues new directives or the agent completes
a major subgoal — the write latency of a linearizable store is acceptable.

**Resource bindings** are managed by the kernel and external services; they cannot be
meaningfully serialized. The AI-OS must track which bindings exist (for accounting and leak
detection) but must design for the invariant that bindings are volatile: on agent suspension
or migration, all bindings are released, and on resume, they are re-acquired. This "release and
re-acquire" semantic requires that external resources (API sessions, network connections) support
session resumption without loss of logical state.

### 10.3 Ownership and Isolation

The ownership question for agent state is unexpectedly complex in multi-agent systems.
When agent A delegates a subtask to subagent B, and B modifies semantic memory or goal state
during that subtask, who owns the modification? Three positions are possible:

**Agent-local ownership.** Each agent owns its own state; B's modifications are local to B.
When B returns control to A, A receives a result value, not a state mutation. This is the
cleanest model from an isolation perspective but requires explicit state merge if A needs B's
learned facts.

**Hierarchical delegation.** B operates within A's state namespace; B's modifications are
visible to A and any other subagents A has spawned. This matches the intuitive model for
orchestrator/subagent relationships but requires a distributed shared memory abstraction that
is correct under concurrency.

**Transactional delegation.** B's modifications are isolated until B commits; A can accept or
reject B's state delta as a unit. This is the most composable model but requires
transactional semantics across agent state stores — a significant implementation complexity.

The prompt injection risk in shared state cannot be overstated. If agent A writes to a shared
semantic memory store and agent B reads from it in a subsequent inference step, A has an
injection vector into B's context. In the conventional security model, this is a confused
deputy attack [III-17]: B has capabilities that A does not, and A exploits shared state to
influence B's behavior. The AI-OS must treat writes to shared agent state as security-sensitive
operations subject to the same trust checks as any other inter-agent communication.

KV cache isolation is an open research problem at production scale. The fundamental difficulty
is that sharing KV caches between agents improves inference throughput (agents processing the
same system prompt can share its cached representation), but shared caches are a side channel:
timing measurements of cache hits and misses can leak information about other agents' contexts.
HeART and Oaken both prioritize performance; neither addresses the security implications of
shared KV state.

### 10.4 Consistency Model

The consistency requirements for each state category can be stated precisely:

**Strong consistency required.** Goal state and security policies must be strongly consistent
across all replicas and all agents that can read them. An agent that reads a stale goal state
may take contradictory actions; an agent that reads a stale security policy may violate its
access constraints. The linearizability requirement for these categories is non-negotiable.

**Audit logs** must be append-only and immutable: no record once written can be modified or
deleted. The Merkle tree structure (Section 11.5) provides tamper evidence; the kernel primitive
`aios_audit_log` ensures that no user-space code path can bypass the log. These two properties
together constitute tamper-evident provenance.

**Eventual consistency acceptable.** Semantic memory and RAG indices tolerate eventual
consistency: if two agents briefly see different versions of a knowledge base, no safety
invariant is violated (though application correctness may be affected). The write latency
reduction from eventual consistency is significant for high-frequency knowledge updates.

**Discardable on failure.** Execution context can be discarded and re-created from task
specification; the cost is re-running the agent from its last checkpoint, not a correctness
failure. Resource bindings are always volatile; their loss triggers the re-acquisition protocol,
not a failure state.

**Checkpoint and restore semantics** for agent migration across nodes require that execution
context and episodic memory (excluding KV cache) be serializable to a portable format. The
migration protocol is: (1) agent reaches a tool-call boundary, (2) checkpoint is taken
(serialized execution context + episodic log without KV cache), (3) agent is suspended on
source node, (4) checkpoint is transferred, (5) agent resumes on destination node, (6) KV
cache is reconstructed by replaying the episodic log against the inference engine. Step 6 is
expensive (proportional to history length) and motivates developing portable KV cache formats.

### 10.5 Relation to MemOS

The MemOS project [III-18, III-19] proposes the MemCube abstraction as a unifying container for
heterogeneous AI memory tiers. MemOS defines three memory types: **parametric** (model weights),
**activation** (KV cache and intermediate activations), and **plaintext** (retrieved text,
conversation history). MemCubes can be tracked across tiers, fused across memory types, and
migrated between storage backends — addressing the lifecycle management problem for the LLM
case.

The alignment between MemOS and the state taxonomy of Section 10.1 is partial. MemOS captures
episodic memory (activation = KV cache) and execution context (plaintext = retrieved context),
and it explicitly manages parametric memory (model weights). It does not model goal state or
resource bindings, which are not memory management concerns in the MemOS framing. This is
consistent with MemOS's focus on LLM memory as distinct from agent operating system concerns.

The architectural synthesis is: MemOS's MemCube abstraction is the correct implementation model
for the episodic memory and semantic memory tiers in the AI-OS state architecture. The AI-OS
should expose a MemCube-compatible interface at the episodic and semantic memory layers to
enable interoperability with MemOS-aware inference engines. Goal state and resource bindings
remain outside the MemOS scope and require separate management as described above.

### 10.6 The "Everything Is Context" Alternative

Xu et al. [III-20] propose an architectural alternative inspired by Unix's "everything is a
file" principle: in an AI-OS, everything is context. Under this model, all artifacts that an
agent interacts with — input prompts, retrieved documents, tool outputs, memory contents, logs —
are represented as context artifacts accessible through a unified filesystem-like interface.
Context artifacts can be mounted, organized in directories, given metadata, and subjected to
access control rules using the same mechanisms the OS already applies to files.

The elegance of this approach is that it requires no new kernel abstractions: the existing
filesystem namespace, permissions model, and I/O interfaces become the agent state management
system. An agent's goal state is a file; its episodic memory is a directory; its semantic
memory is a mounted filesystem. Provenance is file metadata; access control is file permissions.

The tension is that this uniformity imposes a single abstraction on fundamentally different
state categories. Goal state requires linearizable consistency; the POSIX filesystem does not
guarantee this (local filesystems provide durability; distributed filesystems provide varying
consistency guarantees). KV cache state is not meaningfully representable as a sequence of
bytes in a file; its structure is defined by the inference engine's internal representation.
Resource bindings are kernel objects, not data — treating them as files requires the Plan 9
convention of representing kernel objects as filesystem entries, which is architecturally
consistent but requires either Plan 9 or a significant VFS extension.

The "everything is context" model is most compelling as a developer-facing abstraction layer:
a way to make agent state inspectable, portable, and governable using familiar tools. It is
less compelling as a performance-critical storage substrate where the semantic differences
between state categories must be honored for correctness. The AI-OS architecture should expose
a context-filesystem view at the operator and tooling layer while using semantically appropriate
substrates underneath.

---

## 11. Security Architecture

### 11.1 Threat Model for an AI-Native OS

The security threats specific to an AI-native OS are not merely conventional OS threats
transposed into a new domain. Several are qualitatively novel, and their severity is elevated
because the AI control plane has privileged authority over resource allocation and policy
enforcement. A prompt injection attack against a web application is an application-layer nuisance;
the same attack against an AI control plane with kernel-level scheduling authority is a
privilege escalation vector.

**Threat 1: Prompt injection as OS-level privilege escalation.** An adversary who can control
content ingested by the AI control plane — through a compromised tool response, a manipulated
RAG document, or a crafted agent-to-agent message — can attempt to cause the control plane to
take unauthorized actions: allocating resources to the adversary's agents, suppressing audit
log entries, granting elevated permissions, or initiating denial-of-service against other
agents. This is the OS security threat equivalent of a buffer overflow that overwrites a return
address to redirect execution. The mechanism is different (semantic manipulation versus memory
corruption), but the consequence is the same: an attacker gains capabilities they were not
granted.

The defense-in-depth response must treat the AI control plane's input channels with the same
suspicion that a kernel treats untrusted system call arguments. Every input to the control plane
from an external source (tool responses, inter-agent messages, user-provided content) must be
treated as potentially adversarial.

**Threat 2: Confused deputy in multi-agent systems.** Agent A, with limited permissions,
requests that agent B, with elevated permissions, perform an operation on A's behalf. If B's
reasoning is influenced by A's message — particularly if A can inject instructions into B's
context — B becomes a confused deputy: it performs operations authorized by B's permissions on
behalf of A's interests [III-17]. SEAgent [III-21] formalizes this threat model and proposes a
mandatory access control framework for agent-to-agent interactions. The key principle: agent B
must verify not just that A's *request* is within A's permissions but that the operation B is
being asked to perform is consistent with A's *delegated authority* — which may be less than A's
full permission set.

**Threat 3: Model supply chain compromise.** Poisoned model weights, corrupted LoRA adapters,
and backdoored fine-tuned models represent a supply chain attack on the AI-OS trusted computing
base. A model loaded into the AI control plane becomes part of the system's policy-making
authority. An adversary who can influence a model's weights — during training, fine-tuning, or
at the model repository — can embed backdoors that cause the control plane to take specific
malicious actions when triggered by attacker-chosen input patterns. This threat has no direct
analogue in conventional software security because conventional executables are byte-for-byte
reproducible from source code; a neural network's "behavior" emerges from billions of floating
point parameters in ways that cannot be inspected by reading the weights.

**Threat 4: Side-channel attacks on shared inference resources.** Multiple agents sharing a
GPU may leak information through timing side channels (cache line eviction timing), memory
access patterns (observable from a co-located agent via cache occupancy), and power consumption
signatures. GPU-level side channels are less well-studied than CPU-level channels, but the
fundamental physics is the same: shared hardware resources create information leakage paths.
The CUDA shared memory model and L2 cache architecture create attack surfaces that are not
present in CPU-centric security models.

**Threat 5: State corruption via shared agent memory.** Any shared state accessible to
multiple agents is a potential corruption vector. If agent A writes to a shared semantic memory
store and agent B reads from it, A can attempt to corrupt B's context by writing adversarial
content. If the semantic memory store does not enforce per-agent write namespacing, A can
overwrite B's stored facts, causing B to reason from false premises in subsequent interactions.

### 11.2 Agent Isolation Tiers

The isolation requirement for a pair of agents depends on their mutual trust relationship and
the sensitivity of the resources they handle. A tiered isolation model provides appropriate
protection proportional to threat without imposing maximum-isolation overhead on all agent
interactions.

**Table 2: Agent Isolation Tier Specification**

| Tier | Mechanism | Isolation Strength | Launch Overhead | Appropriate Use Case |
|---|---|---|---|---|
| 0 | Same process, shared address space | None — single failure domain | ~0 | Internal sub-agents, trusted library tools within a single agent process |
| 1 | Separate processes, capability-based IPC | Process-level ASLR + separate address space | ~1 ms | System agents with mutual trust; default for cooperating agents within a workload |
| 2 | Separate containers (namespaces + cgroups v2) | Namespace isolation; shared kernel | ~5–50 ms | User-installed agents; third-party tools; untrusted but not adversarial agents |
| 3 | Separate VMs or hardware TEEs | Full kernel isolation; hardware-enforced | ~100 ms–1 s | Agents handling sensitive data; confidential compute workloads; agents with elevated permissions |
| 4 | Hardware partitions (MIG, SR-IOV, NPU domains) | Physical hardware isolation | Static configuration | GPU workload isolation; multi-tenant inference; physically separated compute domains |

The default policy: system agents (spawned by the AI-OS itself for resource management and
scheduling functions) operate at Tier 1. User-installed agents (installed by operators or users
from external sources) operate at Tier 2. Agents authorized to process sensitive data — data
classified under ITAR, CUI, or equivalent classifications — operate at Tier 3. GPU inference
workloads from mutually untrusted tenants operate at Tier 4.

Upgrading an agent from Tier 2 to Tier 3 requires an explicit operator authorization step, logged
via `aios_audit_log`. Downgrading an agent's isolation tier is prohibited without explicit
operator override. These invariants prevent privilege escalation through tier migration.

> **[P] Practitioner Note — Tier Selection for Common Cases**
> - LLM inference serving internal users: Tier 2 (container isolation)
> - Third-party plugin execution: Tier 2 minimum, Tier 3 if plugin accesses sensitive data
> - RAG over classified documents: Tier 3 (TEE) with attestation
> - Multi-tenant GPU inference: Tier 4 (MIG) per tenant
> - Agent that orchestrates other agents: Tier 1, but its subagents are at their own tiers

### 11.3 Tool Capability Model

Agents invoke tools through the MCP and A2A interfaces; tools access filesystems, external
networks, and third-party APIs. The central security requirement is that no agent possesses
ambient authority — an agent should only be able to access the specific resources needed for
its current task, not any resource it could theoretically reach given its process credentials.

The capability model assigns each agent a capability manifest at launch time. The manifest
specifies:

- Filesystem access: a set of Landlock rules specifying which paths are readable, writable,
  or executable
- Network access: permitted destination addresses and port ranges (enforced via network
  namespace configuration)
- System call surface: a seccomp-BPF profile specifying which syscalls are permitted and
  with which argument constraints
- Inter-agent communication: a whitelist of agent identifiers the agent may invoke via A2A
- Model access: which model versions the agent may invoke for inference
- Memory limits: hard memory cap (enforced via cgroup v2)

Each tool invocation requires presenting a capability token scoped to the specific operation.
The token is issued by the AI control plane at agent launch and cannot be self-elevated: an
agent cannot grant itself a capability it was not issued at launch. Capability delegation — where
a parent agent delegates a subset of its capabilities to a subagent — must be conservative:
the subagent's capability set is an intersection of the parent's capabilities and the explicitly
delegated subset.

The near-term implementation uses Landlock LSM, seccomp-BPF, and network namespaces for
enforcement. The full vision — where capabilities are cryptographic tokens presented at each
tool invocation and verified by the AI control plane before the kernel enforces the operation —
requires infrastructure not yet available in the mainline kernel but is architecturally aligned
with the seL4 capability model [III-2] and Fuchsia/Zircon handle semantics.

### 11.4 Model Integrity Chain

A model loaded into the AI control plane must be verifiably authentic — the same artifact that
was evaluated, approved, and signed by a trusted authority. The model integrity chain has four
stages:

**Cryptographic signing.** The AI-OS model registry stores a public key infrastructure separate
from the model storage backend. Each approved model version has a manifest containing: the
SHA-256 hash of the weight file(s), the SHA-256 hash of any associated adapter files (LoRA
weights, GGUF quantization artifacts), the model identifier and version, and a digital signature
over the manifest created by the signing authority. At load time, the AI runtime verifies the
signature before mapping any model weights into process memory.

**Load-time attestation.** For deployments using hardware TEEs, the model loading process
occurs inside the TEE; the TEE produces a remote attestation report that includes a measurement
of the model loading procedure and the model's manifest hash. A relying party can verify that
the correct model was loaded inside an authentic TEE with a specified security configuration.
This closes the gap between "the model registry says the hash matches" and "the model running
in production is actually the model from the registry."

**Runtime integrity checks.** Periodic re-verification of loaded model weights using kernel
memory protection: the weight pages are mapped read-only after loading; any attempt to write
to weight memory generates a page fault caught by the kernel. Optionally, periodic background
hashing of weight memory against the stored manifest hash provides additional assurance at the
cost of memory bandwidth.

**Policy engine.** The AI control plane enforces a model whitelist: only model versions listed
in the approved manifest may be loaded. The whitelist is versioned and signed; loading a model
not in the current whitelist is a security event logged via `aios_audit_log`. Version pinning
ensures that a deployment cannot silently drift to a newer or older model version without an
explicit update operation.

### 11.5 Tamper-Evident Provenance

The audit trail for an AI-native OS must satisfy a stronger requirement than conventional log
files: it must be impossible for the AI control plane or any agent to suppress, alter, or forge
audit records. A conventional syslog that the AI control plane can write to does not satisfy
this requirement — the AI control plane could potentially log false records or suppress true ones.

PunkGo / Right to History [III-11] demonstrates that tamper-evident logging can be implemented
as a kernel primitive with acceptable performance overhead: sub-1.3 millisecond action latency
using RFC 6962 Merkle tree structures. The Merkle tree approach works as follows: each audit
event is hashed; the hash becomes a leaf in an append-only Merkle tree maintained by the
kernel; the root hash after each insertion is returned to the caller. Any attempt to alter a
logged event would require recomputing the entire suffix of the Merkle tree and matching a
different root hash — detectable by any party holding a copy of a prior root.

The `aios_audit_log` primitive (Section 9.2) implements this pattern: each call returns the
log sequence number and the Merkle root after inclusion. Auditors periodically record the
current root; any later root that is inconsistent with the previous root and the intervening
events indicates log tampering.

PROV-O [III-22] integration adds queryable provenance on top of tamper-evident logging. While
the Merkle tree guarantees that a sequence of events was recorded in order and has not been
modified, PROV-O's entity-activity-agent model allows an auditor to query causal relationships:
"which model version produced this policy decision?", "which agent initiated this resource
allocation?", "what chain of tool calls led to this outcome?" This is the query interface for
regulatory compliance and forensic analysis — necessary for EU AI Act audit obligations
applicable to high-risk AI systems [III-23].

The CBTO ontology (from the AI Circuit Breaker design specification v4.0 [III-24]) provides
the PROV-O extension schema for AI-OS provenance. The CBTO TBox includes `cb:PolicyDecision`,
`cb:MorphismQualityMeasurement`, and `cb:AgentInvocation` as PROV-O Activity subclasses,
enabling structured provenance queries over the audit trail.

### 11.6 Confidential Computing Substrate

For deployments where agents handle sensitive data — classified information, ITAR-controlled
designs, personal health records, or proprietary financial models — the conventional isolation
model is insufficient. A hypervisor can be compromised; container isolation provides no
protection against a malicious co-tenant with physical access; network isolation cannot prevent
a compromised host OS from reading agent memory. Confidential computing addresses this by
extending hardware isolation into the memory subsystem.

**GPU TEE.** NVIDIA H100 and Blackwell architecture GPUs support a confidential computing
mode where GPU memory is encrypted and isolated from the host CPU and hypervisor. The measured
overhead for LLM inference within an NVIDIA GPU TEE is less than 5 percent relative to
non-confidential execution [III-25]. For inference workloads handling sensitive data, this
overhead is acceptable given the protection provided.

**Intel TDX Connect.** Intel Trust Domain Extensions Connect closes a gap in GPU TEE
deployments: the communication channel between a CPU trust domain and a GPU TEE. Without TDX
Connect, data passed from a CPU-side TEE to a GPU TEE crosses a potentially observable bus;
TDX Connect provides an authenticated, encrypted channel for CPU-to-GPU data transfers,
completing the confidential computing boundary around the inference workload.

**Omega System.** The Omega system [III-26] addresses a different gap: multiple agents
within a single CVM (AMD SEV-SNP protected virtual machine) sharing a single GPU TEE.
Without nested isolation, one compromised agent within the CVM can potentially read another
agent's GPU memory. Omega's Compute Protected Region mechanism provides intra-CVM isolation
at the GPU level — enabling multi-agent deployments within a single confidential VM without
requiring separate TEE instances per agent.

**Rack-scale confidential computing.** NVIDIA Vera Rubin NVL72 extends the TEE boundary to
encompass an entire AI compute rack: 72 GPUs connected via NVLink, with a rack-level attestation
capability that allows a remote verifier to confirm that the entire compute rack is operating
with authentic, unmodified firmware and that the AI workload is executing within the hardware-
enforced confidential boundary. This is the architectural endgame for maximum-assurance AI
deployments: the TEE is not a process or a VM but a physical rack.

The AI-OS architecture must treat the confidential computing boundary as a design-time decision,
not a deployment-time configuration choice. The isolation tier model of Section 11.2 maps
directly to confidential computing choices: Tier 3 corresponds to single-VM TEE (AMD SEV-SNP
or Intel TDX); Tier 4 corresponds to hardware-partitioned GPU TEE (NVIDIA MIG in confidential
mode). The AI control plane must be aware of which agents are executing within TEE boundaries
and must not route sensitive data to agents executing outside their required isolation tier.

---

## 12. Failure Taxonomy and Recovery

### 12.1 AI Control Plane Failure Modes

An AI-native OS has a new failure mode category that does not appear in conventional OS failure
analysis: the AI control plane can fail not just by crashing but by producing *wrong* policy
decisions with high confidence. A conventional OS kernel either runs correctly or crashes;
its failure modes are detectable because they produce exceptions, kernel panics, or watchdog
timeouts. An AI control plane can fail gracefully, continuing to produce output, while the
outputs are catastrophically incorrect — misallocating resources, granting elevated permissions
to unauthorized agents, suppressing security events.

This failure mode requires detection mechanisms beyond the process monitoring paradigm.

**Table 3: AI Control Plane Failure Mode Taxonomy**

| Failure Mode | Description | Detection Mechanism | Time to Detect |
|---|---|---|---|
| Process crash | Segfault, OOM kill, unhandled exception in the control plane process | Process monitor (systemd, supervisord); kernel exit notification | < 1 s |
| Inference livelock | Control plane enters a non-terminating reasoning loop; generates tokens continuously without producing policy decisions | Output rate monitor; token generation rate with timeout watchdog | 1–30 s |
| Wrong policy decision | AI makes a catastrophically incorrect resource allocation, permission grant, or security decision | Circuit Breaker: S_a/C_r threshold violation; behavioral anomaly detector; operator audit | 1 s–1 min |
| Adversarial compromise | OS-level prompt injection causes control plane to act against system interests | Behavioral anomaly detection; action/intent divergence monitor (Section 13); `aios_audit_log` anomaly analysis | Variable; may be slow |
| Weight corruption | Model weights modified by storage error, bit rot, or adversary | Integrity check (hash verification at load time); periodic background re-hash | At load time; or at periodic check interval |
| Split-brain | AI control plane and kernel disagree on current system state (e.g., control plane believes an agent is running; kernel has killed it) | State reconciliation heartbeat with state hash comparison | 1–10 s |

### 12.2 Containment and Recovery Per Failure Mode

**Process crash.** Containment: the kernel ensures that the AI control plane's crash does not
propagate to user agent workloads — agents continue executing under their last configured
resource allocations and scheduling policy. Recovery: the process monitor restarts the AI
control plane; on restart, the control plane queries the kernel for current system state (active
processes, cgroup configuration, resource allocations) and reconciles its internal model with
observed state. Time-to-recovery: typically 1–30 seconds depending on model load time.
Conventional substrate: continues operating with the last-known-good policy configuration.

**Inference livelock.** Containment: the watchdog process (Section 12.4) detects the livelock
via a timeout on the control plane's output rate and issues a SIGKILL. The AI control plane is
not given the opportunity to handle the signal because the livelock may prevent normal signal
handling. Recovery: same as process crash. Prevention: the AI control plane should not be
implemented as a single monolithic inference process; policy decisions should be decomposed
into small, bounded inference steps with per-step timeouts.

**Wrong policy decision.** Containment: the Circuit Breaker (Section 13.4) monitors behavioral
morphism quality metrics and trips when they fall below threshold. On trip, the Circuit Breaker
transitions the system to conventional fallback mode without waiting for the AI control plane
to agree. The AI control plane's incorrect policy decision is overridden at the kernel level.
Recovery: the AI control plane is suspended; an operator reviews the decision audit trail
(via PROV-O query); root cause is identified (adversarial input, model drift, or software
defect); the control plane is restarted after the root cause is addressed.

**Adversarial compromise.** Containment: the most dangerous failure mode because it may produce
a sequence of wrong policy decisions each of which individually appears plausible but collectively
constitute an attack. The Circuit Breaker's S_a metric measures whether the control plane's
model of system state is drifting from observable reality — this provides a detection signal
even when individual decisions are not obviously wrong. AgentSight [III-27] demonstrates a
monitoring pattern that tracks AI action/intent divergence: if the AI control plane reports
intending action X but the kernel observes action Y from the associated process, divergence
is flagged. Recovery: the same as wrong policy decision, but with the additional step of
conducting a security forensic analysis of all control plane outputs since the estimated
compromise time.

**Weight corruption.** Containment: if detected at load time (hash mismatch against the manifest),
the corrupted model is not loaded and the previous approved model version is used. If detected
at runtime (periodic re-hash), the AI control plane is immediately suspended and transitioned
to fallback mode. Recovery: the corrupted model file is quarantined; the model registry rolls
back to the previous version; integrity of the rollback target is verified before loading.

**Split-brain.** Containment: the split-brain condition itself must be detected before it causes
divergent actions. A reconciliation heartbeat — the AI control plane periodically submits a
hash of its internal system state model to the kernel; the kernel compares against observed state —
identifies divergence. On detection, the control plane suspends policy decisions and performs
a full state resync. Recovery: the control plane queries the kernel's authoritative state,
discards its internal model, and rebuilds from kernel-observed ground truth. Duration: typically
seconds; designed to complete within the Circuit Breaker's detection window.

### 12.3 Degraded Mode Specification: Conventional Fallback

When the AI control plane is unavailable — whether due to a crash, a Circuit Breaker trip, an
adversarial compromise, or an operator-initiated suspension — the system must continue operating
in a defined degraded mode. This mode is named **Conventional Fallback Mode** and must be
specified with the same precision as the nominal operating mode.

**Capabilities preserved in Conventional Fallback Mode:**
- Boot and initialization (unaffected; substrate is always conventional)
- Hardware isolation between agents and between agents and kernel (cgroup v2 and namespace
  configuration persists from the last AI control plane configuration)
- Scheduling (default kernel scheduler — CFS on Linux, or the configured sched_ext baseline
  policy — operates without AI-derived scheduling hints)
- Memory management (kernel's default memory manager operates without AI priority annotations;
  eviction is handled by LRU policy without semantic awareness)
- I/O (unaffected)
- Security enforcement (all kernel-enforced security mechanisms persist: seccomp profiles,
  Landlock restrictions, network namespace isolation)
- Audit logging (kernel-level Merkle tree logging continues; the AI control plane's absence
  does not disable the audit trail)
- Operator override (the override mechanism operates at kernel privilege and does not depend
  on the AI control plane being available)

**Capabilities unavailable in Conventional Fallback Mode:**
- AI-driven policy optimization (workload placement, resource allocation optimization)
- Agent orchestration (no new agents can be launched; running agents continue but cannot spawn
  subagents through the AI control plane)
- Natural-language operator interface (the AI control plane handles NL interaction; it is
  unavailable)
- Predictive scheduling (scheduling degrades to reactive, non-predictive)
- Adaptive resource allocation (resource limits are static in fallback mode)
- Model lifecycle decisions (no model updates, rollbacks, or evaluations)

**Guarantees during Conventional Fallback Mode:**
- All safety invariants maintained: no agent can exceed its configured resource limits, access
  resources outside its Landlock domain, or communicate with unauthorized agents
- Performance degrades to conventional levels: throughput and latency match what the underlying
  kernel achieves without AI optimization (still functional, not failed)
- Audit trail continues uninterrupted

**Transition into fallback mode:** Automatic on Circuit Breaker trip (Section 13.4); manual
via operator command `aios_fallback_engage` (a privileged syscall that suspends the AI control
plane and transitions to fallback configuration). The transition must complete within one
scheduling cycle — the fallback state must be achievable without cooperation from the AI control
plane, since it may be unresponsive or compromised.

**Return from fallback mode:** The AI control plane restarts and performs state reconciliation
(Section 12.2 process crash recovery). It gradually resumes policy authority: scheduling hints
are reintroduced first; resource allocation decisions second; model lifecycle operations third.
Full authority is restored only after the Circuit Breaker confirms that S_a and C_r are within
acceptable bounds.

### 12.4 The Watchdog Problem

The watchdog problem for AI systems has a structure that standard process monitoring does not
address. A conventional watchdog (systemd, supervisord, hardware watchdog timer) monitors
whether a process is alive and restarts it on failure. This is sufficient when failure is
detectable — when the faulty process crashes or hangs.

An AI control plane can fail silently: it continues running, consuming compute, and producing
outputs, while the outputs are wrong. A process monitor will not detect this failure; there is
no exception to catch, no signal to handle, no exit code to observe. The watchdog problem for
an AI-native OS is: *how do you monitor a system whose failure mode is producing confidently
wrong outputs?*

A naive response is to use a second AI system to monitor the first. But this introduces infinite
regress: who monitors the monitor? If the primary AI control plane can produce wrong outputs,
so can the monitoring AI. Two AI systems agreeing with each other's wrong outputs is a coherent
failure mode, not a detection mechanism.

The resolution — used in the AI Circuit Breaker framework [III-24] and adapted here — is that
the watchdog must be *simpler than the system it monitors by construction*, and it must operate
on *observable system metrics rather than on AI-generated text*. The Circuit Breaker (Section
13.4) monitors two scalar metrics: structural morphism quality (S_a) and behavioral morphism
quality (C_r). These are computed from observable system state — resource allocation outcomes,
agent task completion rates, policy decision outcomes — not from the AI control plane's
self-reported beliefs.

Critically, the Circuit Breaker cannot be compromised by the AI control plane because it does
not share any input channels with the AI control plane. The AI control plane processes agent
messages, tool responses, and operator commands in its inference context. The Circuit Breaker
reads kernel telemetry, process lifecycle events, and resource accounting metrics. These are
separate data flows: an adversary who compromises the AI control plane via prompt injection
cannot inject into the Circuit Breaker's metric inputs.

The Circuit Breaker runs at higher privilege than the AI control plane — it is a kernel module
or a privileged daemon that the AI control plane cannot kill or influence. When it trips, it
calls `aios_fallback_engage` directly, bypassing the AI control plane entirely.

This architecture satisfies the watchdog problem by substituting *simplicity* for *intelligence*
in the monitoring role. The Circuit Breaker is not more capable than the AI control plane; it
is more reliable precisely because it is less capable. It has no reasoning loop that can
livelock; it has no context that can be injected into; it has no model weights that can be
poisoned. It computes two numbers against two thresholds. That is enough.

---

## References for Part III

The following references are cited in Part III. Reference numbers will be harmonized across all
parts in the combined draft.

[III-1] Ge, T., et al. "AIOS: LLM Agent Operating System." *Proceedings of the 2025 Conference
on Language Modeling (COLM)*, 2025.

[III-2] Klein, G., et al. "seL4: Formal Verification of an OS Kernel." *Proceedings of the ACM
SIGOPS 22nd Symposium on Operating Systems Principles (SOSP)*, 2009, pp. 207–220.

[III-3] Klein, G., et al. "Comprehensive Formal Verification of an OS Microkernel." *ACM
Transactions on Computer Systems (TOCS)*, 32(1), 2014.

[III-4] Kwon, W., et al. "Efficient Memory Management for Large Language Model Serving with
PagedAttention." *Proceedings of the ACM SIGOPS 29th Symposium on Operating Systems Principles
(SOSP)*, 2023, pp. 611–626.

[III-5] Ge, T., et al. "AIOS v5: Resource-Efficient and Concurrent LLM Agent Scheduling."
*COLM*, 2025.

[III-6] AgentCgroup: Hierarchical Resource Management for Agentic Workloads on Linux.
arXiv:2602.09345, 2025.

[III-7] Anthropic. "Model Context Protocol Specification." MCP Specification v2025.11.05.
https://spec.modelcontextprotocol.io/, 2025.

[III-8] Google. "Agent-to-Agent Protocol (A2A)." Linux Foundation, June 2025.
https://a2aprotocol.ai/

[III-9] NIST. "NIST AI Agent Standards Initiative." National Institute of Standards and
Technology, February 2026.

[III-10] Agent.xpu: Hardware-Aware Scheduling for Agentic Workloads Across Heterogeneous SoCs.
arXiv:2506.24045, 2025.

[III-11] PunkGo / Right to History: Tamper-Evident Audit Logging as a Kernel Primitive.
arXiv:2602.20214, 2026.

[III-12] NIST. "Artificial Intelligence Risk Management Framework (AI RMF 1.0)." NIST AI
100-1. National Institute of Standards and Technology, January 2023.

[III-13] Mei, K., et al. "AIOS: LLM Agent Operating System." arXiv:2403.16971, 2024.

[III-14] Salaün, M. "Landlock: Unprivileged access control." Linux kernel documentation,
available at: https://docs.kernel.org/security/landlock.html

[III-15] HeART: Hierarchical and Efficient Attention KV Cache Reuse for Transformer Inference.
Active research, 2025–2026.

[III-16] Oaken: Efficient KV Cache Management Under Memory Pressure for LLM Serving.
Active research, 2025–2026.

[III-17] Hardy, N. "The Confused Deputy (or why capabilities might have been invented)."
*ACM SIGOPS Operating Systems Review*, 22(4), 1988, pp. 36–38.

[III-18] MemOS: A Memory Operating System for LLM Agents. arXiv:2505.22101, 2025.

[III-19] MemOS: MemCube Abstraction and Heterogeneous Memory Management.
arXiv:2507.03724, 2025.

[III-20] Xu, Z., et al. "Everything Is Context: A Unified Filesystem Abstraction for AI Agent
State." arXiv:2512.05470, 2025.

[III-21] SEAgent: Mandatory Access Control for Multi-Agent AI Systems.
arXiv:2601.11893, 2026.

[III-22] Moreau, L., et al. "PROV-O: The PROV Ontology." W3C Recommendation, April 2013.
https://www.w3.org/TR/prov-o/

[III-23] European Parliament. "Regulation (EU) 2024/1689 (AI Act)." Official Journal of the
European Union, July 2024.

[III-24] Wach, P. "AI Circuit Breaker Design Specification v4.0: Ontology-Grounded Trust
Metrology." Technical Report, University of Arizona, February 2026.

[III-25] NVIDIA. "NVIDIA Confidential Computing: Protecting Data in Use with GPU TEE."
NVIDIA Technical Brief TB-10298-001, 2023.

[III-26] Omega: Nested Isolation for Multi-Tenant Agentic Workloads within Confidential VMs.
arXiv:2512.05951, 2025.

[III-27] AgentSight: Behavioral Monitoring and Action/Intent Divergence Detection for AI Agents.
Research prototype, 2025–2026.
