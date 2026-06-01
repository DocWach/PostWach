# Practitioner Guide: Building an AI-Native Operating System

*Extracted from: AIOS-WySE Technical Report — AI Operating Systems: A Morphism-Grounded Analysis*
*Target audience: Software architects and AI platform engineers*
*For formal proofs, ontology definitions, and full derivations, see the main report (Parts I–V).*

---

## 1. Scope

This guide is for engineers building or evaluating AI-native platform infrastructure: inference serving layers, agentic workload orchestrators, or production systems where AI components influence OS-level resource decisions. It covers what to decide, what to build, and what tradeoffs exist at each design point.

This guide does not cover:
- Formal derivations of morphism quality metrics (see Part IV of the main report)
- The Circuit Breaker Trust Ontology (CBTO) specification (see AI Circuit Breaker Design Spec v4.0)
- Full IDL specifications for the AI-Kernel Interface Contract (see Section 9 of Part III)
- Safety certification evidence packages (see Section 16 of Part V)

You need roughly a graduate level of familiarity with OS internals and distributed systems. No prior formal methods background is required.

---

## 2. The Two Problems: "AI for OS" vs. "OS for AI"

Before spending engineering time, identify which problem you are actually solving. They are orthogonal programs with different requirements, threat models, and success metrics. Conflating them produces systems designed for neither.

**"AI for OS"** uses AI as an implementation technique for classical OS functions. The OS is still the OS; AI improves how it does its job. Examples: ML-based scheduling patches that learn workload patterns and adjust CPU time allocation; AI-driven memory prefetchers that predict access sequences; eBPF programs combined with ML models for adaptive networking. Fundamental OS abstractions (processes, virtual memory, system calls) remain unchanged. AI is a better algorithm for decisions the OS was already making.

**"OS for AI"** treats AI agents as the primary workload and asks how the OS should manage them. New abstractions are required: agent scheduling (how do I give CPU time to an LLM reasoning loop?), context management (how do I store and retrieve the episodic memory of a long-running agent?), tool mediation (how do I safely expose filesystem and network access to an agent that generates its own tool calls?). The agents are the workload; the OS manages them as it has always managed processes, but the workload properties are radically different.

**Table 1: "AI for OS" vs. "OS for AI" Comparison**

| Dimension | "AI for OS" | "OS for AI" |
|---|---|---|
| Primary question | How can AI improve kernel functions? | How should the OS manage AI agents? |
| Latency requirement | Microsecond (scheduling decisions) | Millisecond-second (inference latency) |
| Threat model | Adversarial workloads exploit learned scheduler | Prompt injection escalates agent privileges |
| Success metric | Resource utilization, tail latency, power efficiency | Agent throughput, context quality, task completion |
| Certification challenge | Proving learned policy meets safety guarantees | Proving agent behavior stays within policy bounds |
| Existing insertion point | eBPF, sched_ext, cgroups v2 | MCP, A2A, agent frameworks |

This report's architecture (Parts III–V) primarily addresses "OS for AI," which is further from engineering maturity and most in need of rigorous treatment. At every decision point below, flag which program you are implementing. The answer changes almost every design choice.

---

## 3. Nine Engineering Requirements

These requirements constrain the design space before the first component diagram is drawn. R1–R7 extend classical OS requirements with AI-specific mechanisms. R8 and R9 are new with no classical OS analogue.

**Table 2: Engineering Requirements Summary**

| Req | Name | One-Sentence Definition | Current Best Practice |
|---|---|---|---|
| R1 | Trusted Substrate | The AI control plane must inherit its trust properties from hardware-rooted, conventionally verified boot chain. | Linux + UEFI Secure Boot + TPM 2.0 attestation; seL4 for maximum assurance |
| R2 | AI Runtime and Resource Manager | Agent workloads require a runtime that understands inference phases, KV cache semantics, and per-agent capability manifests. | AIOS v5 scheduling (2.1x throughput improvement demonstrated); AgentCgroup cgroup-aligned resource partitioning |
| R3 | Tool and Interoperability Layers | Agents invoke tools through a stable, standardized interface enforced at the infrastructure layer. | MCP (model-to-tool, 97M+ monthly SDK downloads); A2A (agent-to-agent, Linux Foundation) |
| R4 | Model Lifecycle Management | Models must be evaluated, signed, deployed, monitored for drift, and rolled back — none of which has a conventional software analogue. | Cryptographic signing, hash-verified load, behavioral drift monitoring via C_r metric |
| R5 | Hardware-Aware Heterogeneous Scheduler | AI workloads span CPU/GPU/NPU/DPU; the scheduler needs semantic knowledge of inference phases and model memory requirements. | sched_ext BPF policy; NVIDIA MIG; cgroup v2 aligned to agent boundaries; io_uring for async I/O |
| R6 | Operator Control and Auditability | Human operators must be able to override, suspend, and audit the AI control plane through kernel-privilege mechanisms that work even when AI is compromised. | PunkGo/Right to History: Merkle tree audit logging at < 1.3 ms latency; privileged override syscall |
| R7 | Risk Management and Governance | NIST AI RMF properties (validity, safety, security, resilience, transparency, privacy, bias) must map to specific OS mechanisms. | Circuit Breaker (safety), morphism metrics S_a/C_r (reliability), PROV-O audit trail (transparency) |
| R8 | Agent State Management | Agent state has five distinct categories with incompatible consistency requirements; treating them uniformly is a correctness error. | Redis (execution context), vLLM/TGI (KV cache), vector DB (semantic memory), etcd (goal state) |
| R9 | Energy and Thermal Governance | AI inference directly competes with OS overhead for thermal headroom on edge hardware; thermal state must be a first-class scheduling signal. | Linux thermal_zone + proactive batch-size reduction before throttle threshold; RAPL/PPAS integration |

**Why each requirement matters:**

R1 is the load-bearing requirement. No AI governance survives a compromised substrate. Choose the substrate first, based on your worst-case isolation requirement — not your average-case workload.

R2 is the performance-critical one. AgentCgroup [arXiv:2602.09345] established that OS execution overhead accounts for 56–74% of end-to-end agent task latency. The runtime is not a performance optimization; it is a performance-critical architectural component.

R8 is the hardest new problem. It has no satisfactory solution in the existing literature. The five state categories have fundamentally different lifecycle semantics and conflating them produces correctness failures. Section 5 below covers this in detail.

R9 has no classical analogue. On edge hardware (NVIDIA Jetson Orin, Qualcomm Snapdragon), AI inference and OS overhead compete for thermal headroom. Ignoring this produces non-deterministic latency spikes from hardware throttling.

---

## 4. The AI-Kernel Interface

The interface between the AI control plane and the kernel is the architecture. A layered design without a specified interface is not an architecture — it is an aspiration. Prior treatments name the concept; this section specifies it.

### 4.1 Six Downward API Primitives

The AI control plane expresses intent to the kernel through these primitives. The kernel treats them as hints with authority: it biases its behavior toward expressed preferences when no safety invariant is threatened, and overrides them when safety invariants are at stake.

**Table 3: Downward API Summary**

| Primitive | Purpose | Key Parameters |
|---|---|---|
| `aios_sched_hint` | Communicate scheduling preference for an agent workload | workload_id, latency_budget_ns, priority_class {REALTIME, HIGH, NORMAL, BEST_EFFORT, BACKGROUND}, preferred_cpu_set |
| `aios_sched_yield_hint` | Signal that a workload is entering a blocking phase (tool call, I/O wait) so the kernel can yield immediately | workload_id, estimated_block_ns |
| `aios_mem_reserve` | Reserve memory for an agent's working set with a specified eviction policy | agent_id, working_set_bytes (soft), hard_limit_bytes (enforced), eviction_policy |
| `aios_mem_annotate` | Tag a memory region with AI semantic type so the kernel's eviction policy aligns with AI runtime preferences | region_base, region_size, region_type {KV_CACHE, MODEL_WEIGHTS, RAG_BUFFER, GOAL_STATE, EPISODIC_LOG}, eviction_priority |
| `aios_resource_fence` | Bind an agent to specific hardware partitions (GPU MIG slice, NPU queue, NUMA node) | agent_id, cpu_affinity, gpu_partition, npu_queue, numa_node; returns fence_handle |
| `aios_audit_log` | Submit an event to the kernel-maintained tamper-evident Merkle tree log | event_type, agent_id, action_hash (SHA-256), payload; returns log_sequence_number and merkle_root after inclusion |

The full IDL definitions are in Section 9.2 of Part III. These summaries are sufficient for architectural decisions.

### 4.2 Five Upward Event Categories

The kernel delivers these events to the AI control plane as a structured notification stream. The AI control plane subscribes and responds via the downward API.

1. **Resource availability signals.** CPU utilization per-core and per-NUMA-node, memory pressure (free pages, swap rate, cgroup usage), GPU queue depth and utilization per MIG partition, NPU availability, thermal zone temperatures. Delivered on configurable polling interval (typical: 100 ms) and as threshold-crossing notifications.

2. **Security events.** Anomalous system call patterns from agent processes, privilege escalation attempts (capability requests outside granted set), capability violations (file access outside Landlock domain, network connection to undeclared destination), cross-agent memory access attempts.

3. **Memory pressure events.** Graduated severity: WARNING (nominate eviction candidates), CRITICAL (eviction must occur within next scheduling cycle), EMERGENCY (OOM killer about to fire). The AI control plane must respond to WARNING by nominating low-priority KV caches; failure triggers automatic kernel LRU eviction.

4. **Process and container lifecycle events.** Agent crash notification with exit reason, agent timeout (process exceeded scheduling quantum by configurable factor), container lifecycle transitions (start/pause/stop/destroy) for containerized agents.

5. **Circuit Breaker events.** Morphism quality metric updates (S_a and C_r values), threshold crossing warnings, trip notifications initiating transition to Conventional Fallback Mode.

### 4.3 Policy vs. Mechanism: The Governing Rule

**The kernel enforces mechanism. The AI control plane sets policy. The kernel can always override.**

This is the safety argument for the entire architecture. It must be treated as non-negotiable, not as a design preference.

Mechanisms the kernel enforces unconditionally (the AI control plane cannot override these):
- Memory isolation between agents
- Scheduling quantum enforcement (the kernel retains preemption authority always)
- Memory protection between address spaces
- Audit log immutability (entries cannot be deleted or modified by any user-space entity, including the AI control plane)
- Hardware access mediation

Policies the AI control plane sets (expressed via downward API, honored subject to mechanism constraints):
- Agent communication topology (which agents may invoke which via A2A)
- Resource allocation priorities (scheduling hints, memory reservations, hardware partition assignments)
- Model selection for agent workloads
- Workload placement across heterogeneous hardware
- Agent eviction ordering under memory pressure
- Security posture adjustments within permitted bounds (tightening Landlock, adding seccomp filters — not removing kernel-level security)

An AI control plane that allocates all memory to a priority agent, starving the kernel's own memory pools, is overridden by the OOM killer. This is correct behavior. Design for it explicitly; do not treat it as an edge case.

### 4.4 Near-Term Linux Implementation

The full interface contract does not exist as a deployed system. However, each component has a credible insertion point in current Linux. This is deployable today on Linux 6.12 or later.

**eBPF + sched_ext.** `sched_ext` (merged in Linux 6.12) allows scheduling policy to be implemented as BPF programs loaded by user space. This is the closest existing mechanism to the downward scheduling API. AgentCgroup demonstrates the path: `sched_ext` for CPU scheduling and `memcg_bpf_ops` for memory control, with cgroups aligned to tool-call boundaries rather than container boundaries.

**cgroups v2.** The unified cgroup v2 hierarchy provides hierarchical resource control for CPU, memory, and I/O. The novel step for AI-OS is aligning cgroup boundaries to agent task boundaries rather than process or container boundaries. An agent that spawns subprocesses for tool execution should have all associated processes in a single cgroup subtree.

**Landlock LSM.** Capability-token-based filesystem sandboxing. A tool server receives a Landlock ruleset scoped to the specific paths it requires; any access outside the ruleset is denied at kernel level.

**seccomp-BPF.** Per-agent system call restriction via BPF programs. An agent that should not have network access can be restricted to a seccomp profile blocking all socket-related syscalls.

**io_uring.** Asynchronous I/O batching for tool-call I/O operations, reducing per-operation syscall overhead — directly addressing the 56–74% kernel overhead finding from AgentCgroup.

**The gap.** These mechanisms fall short of the full interface contract in three ways: the kernel treats KV caches as anonymous memory (no semantic understanding of AI state), there is no formal scheduling intent communication (sched_ext hints are BPF programs, not typed API calls), and CPU and GPU scheduling remain disconnected (no cross-device coordination). Closing these gaps is a medium-term research program, not a configuration task. Document the gaps explicitly so the delta between your prototype and the full specification is traceable.

### 4.5 The AgentCgroup Finding: Why This Matters for Performance

AgentCgroup [arXiv:2602.09345] measured OS execution overhead for agentic workloads on stock Linux and found that wait time in kernel scheduling queues, syscall processing, and memory management accounts for **56–74% of end-to-end agent task latency**. This is not a workload optimization problem. It means that for most real agent tasks, the majority of wall-clock time is spent waiting on the OS, not on inference.

Implication: aligning cgroup boundaries to agent task boundaries (rather than container boundaries) is not an architectural nicety — it is the primary performance lever available on current Linux. Do this first, before any other optimization.

---

## 5. Agent State: The Hardest New Problem

A conventional OS process has two primary state components: a virtual address space and an open file descriptor table. The OS knows how to checkpoint, migrate, and restore these because their semantics are fully specified by the programming model.

An AI agent's state has five distinct components, each with different lifecycle semantics, ownership requirements, and persistence implications. Treating them as a single "agent memory" resource conflates fundamentally different consistency and durability requirements. This is a correctness error, not a performance concern.

### 5.1 State Taxonomy

**Table 4: Agent State Taxonomy**

| Category | Contents | Lifecycle | Consistency Requirement | Persistence |
|---|---|---|---|---|
| Execution context | Current task spec, tool bindings, in-flight call results, plan position | Created at launch; invalid after task completion | Not applicable (single-writer) | Volatile; checkpoint for migration |
| Episodic memory | Recent interaction history, transformer KV cache | Grows during session; evictable under pressure | Session-scoped coherence | Session-persistent; archivable |
| Semantic memory | RAG index pointers, learned associations, fact cache | Accumulated over agent lifetime | Eventual consistency acceptable | Durable; versioned |
| Goal state | Objectives, subgoal decomposition, pending commitments to other agents | Set by orchestrator; modified by planning | **Strong consistency required** | Durable until explicit change |
| Resource bindings | File descriptors, GPU memory, network connections, API sessions | Acquired during execution; released on completion | N/A (kernel-managed) | Volatile; re-acquire on resume |

The strongest requirement is on goal state. An agent with a stale view of its goal structure may pursue obsolete or contradictory objectives. This is a safety issue, not a performance issue. Goal state must be linearizable: every read reflects all prior writes.

Episodic memory that is "strongly consistent" wastes write latency on consistency protocols that provide no safety benefit. Use eventual consistency for semantic memory and RAG indices.

### 5.2 Storage Recommendations Per Category

**Execution context.** Redis with AOF persistence (or equivalent fast durable store) at checkpoint boundaries. Tool-call boundaries are the natural checkpointing points: the agent is between inference steps, in-flight calls have completed or timed out, and state can be serialized without capturing mid-inference KV cache state. Checkpoint format must be sufficient to reconstruct the agent's execution at a different node.

**Episodic memory (KV cache).** Managed by the inference engine (vLLM, TGI, llama.cpp) with LRU eviction. Accept that evicted KV cache is not recoverable without recomputation. Provide the inference engine with priority signals from the AI runtime via `aios_mem_annotate`. Design agents that degrade gracefully when KV cache is evicted — do not depend on cache persistence for correctness.

**Semantic memory.** Dedicated vector database with versioned snapshots (Qdrant, Weaviate, or Milvus all support collection versioning). Tag writes with agent identity and timestamp for provenance tracing. Versioning is required — not just for rollback, but for the model lifecycle management requirement (R4): a model update may require rolling back semantic memory state written by the previous model version.

**Goal state.** Linearizable key-value store: etcd or FoundationDB. No exceptions. Goal state changes relatively infrequently (new orchestrator directives, major subgoal completions), so write latency of a linearizable store is acceptable. Never use eventually consistent storage for goal state.

**Resource bindings.** Track which bindings exist for accounting and leak detection, but design for the invariant that bindings are always volatile. On agent suspension or migration: release all bindings, re-acquire on resume. Require that external resources (API sessions, network connections) support session resumption without loss of logical state.

### 5.3 Ownership and Consistency Model

When agent A delegates a subtask to subagent B, and B modifies shared state, three ownership models are available:

- **Agent-local ownership.** B's modifications are local to B. A receives a result value, not a state mutation. Cleanest isolation; requires explicit state merge if A needs B's learned facts.
- **Hierarchical delegation.** B operates within A's state namespace; B's modifications are visible to A and all other subagents A has spawned. Intuitive for orchestrator/subagent relationships; requires distributed shared memory.
- **Transactional delegation.** B's modifications are isolated until B commits; A can accept or reject B's state delta as a unit. Most composable; significant implementation complexity.

Choose agent-local ownership as the default. Use hierarchical delegation only when the orchestrator explicitly needs shared state across its subagents. Use transactional delegation only when you have the infrastructure for distributed transactions.

### 5.4 Warning: Prompt Injection via Shared State

If agent A writes to a shared semantic memory store and agent B reads from it in a subsequent inference step, A has an injection vector into B's context. In the conventional security model, this is a confused deputy attack: B has capabilities that A does not, and A exploits shared state to influence B's behavior.

Treat writes to shared agent state as security-sensitive operations subject to the same trust checks as any other inter-agent communication. Per-agent write namespacing in semantic memory is not optional in multi-tenant or multi-agent deployments.

KV cache sharing is a specific high-risk case. Sharing KV caches between agents improves inference throughput (agents processing the same system prompt can share its cached representation), but shared caches are a timing side channel: measurements of cache hits and misses can leak information about other agents' contexts. Current systems (HeART, Oaken) prioritize performance and do not address this. Be explicit about the tradeoff if you enable KV cache sharing.

---

## 6. Security Architecture

### 6.1 Five Threat Types

AI-native OS threats are not conventional OS threats transposed into a new domain. Several are qualitatively novel and their severity is elevated because the AI control plane has privileged authority over resource allocation and policy enforcement.

**Threat 1: Prompt injection as OS-level privilege escalation.** An adversary who can control content ingested by the AI control plane — through a compromised tool response, a manipulated RAG document, or a crafted agent-to-agent message — can attempt to cause the control plane to take unauthorized actions: allocating resources to the adversary's agents, suppressing audit log entries, granting elevated permissions, initiating denial-of-service against other agents. This is structurally equivalent to a buffer overflow that overwrites a return address. The mechanism is different (semantic manipulation versus memory corruption); the consequence is the same. Every input to the control plane from an external source must be treated as potentially adversarial.

**Threat 2: Confused deputy in multi-agent systems.** Agent A (limited permissions) requests that agent B (elevated permissions) perform an operation on A's behalf. If A's message can inject instructions into B's context, B becomes a confused deputy: it performs operations authorized by B's permissions on behalf of A's interests. The key principle: B must verify not just that A's request is within A's permissions but that the operation B is being asked to perform is consistent with A's delegated authority — which may be less than A's full permission set.

**Threat 3: Model supply chain compromise.** Poisoned model weights, corrupted LoRA adapters, backdoored fine-tuned models. A model loaded into the AI control plane becomes part of the system's policy-making authority. There is no byte-for-byte reproducibility from source code that would detect this; behavior emerges from billions of floating-point parameters that cannot be inspected by reading the weights. Cryptographic signing and hash verification at load time are necessary but not sufficient.

**Threat 4: Side-channel attacks on shared inference resources.** Multiple agents sharing a GPU may leak information through timing side channels (cache line eviction timing), memory access patterns (cache occupancy observable from co-located agents), and power consumption signatures. GPU-level side channels are less well-studied than CPU-level channels, but the physics is the same. The CUDA shared memory model and L2 cache architecture create attack surfaces with no equivalent in CPU-centric security models.

**Threat 5: State corruption via shared agent memory.** Any shared state accessible to multiple agents is a potential corruption vector. Agent A can write adversarial content to shared semantic memory that corrupts agent B's context in subsequent inference steps.

### 6.2 Five-Tier Isolation Model

**Table 5: Agent Isolation Tier Specification**

| Tier | Mechanism | Isolation Strength | Launch Overhead | Appropriate Use Case |
|---|---|---|---|---|
| 0 | Same process, shared address space | None — single failure domain | ~0 | Internal sub-agents, trusted library tools within a single agent process |
| 1 | Separate processes, capability-based IPC | Process-level ASLR + separate address space | ~1 ms | System agents with mutual trust; default for cooperating agents within a workload |
| 2 | Separate containers (namespaces + cgroups v2) | Namespace isolation; shared kernel | ~5–50 ms | User-installed agents; third-party tools; untrusted but not adversarial agents |
| 3 | Separate VMs or hardware TEEs | Full kernel isolation; hardware-enforced | ~100 ms–1 s | Agents handling sensitive data; CUI/ITAR; agents with elevated permissions |
| 4 | Hardware partitions (MIG, SR-IOV, NPU domains) | Physical hardware isolation | Static configuration | GPU workload isolation; multi-tenant inference; physically separated compute domains |

**Default assignments:** System agents (spawned by the AI-OS for resource management and scheduling) at Tier 1. User-installed agents (from external sources) at Tier 2. Agents handling CUI/ITAR/sensitive data at Tier 3. GPU inference workloads from mutually untrusted tenants at Tier 4.

Upgrading an agent from Tier 2 to Tier 3 requires explicit operator authorization, logged via `aios_audit_log`. Downgrading an agent's isolation tier without explicit operator override is prohibited. These invariants prevent privilege escalation through tier migration.

### 6.3 Tool Capability Model: Least Privilege

Each agent receives a capability manifest at launch time. The manifest specifies exactly what the agent is allowed to do. Nothing not in the manifest is permitted by default.

Required manifest elements:
- **Filesystem access**: Landlock rules specifying readable, writable, and executable paths
- **Network access**: permitted destination addresses and port ranges (enforced via network namespace)
- **System call surface**: seccomp-BPF profile specifying permitted syscalls and argument constraints
- **Inter-agent communication**: whitelist of agent identifiers the agent may invoke via A2A
- **Model access**: which model versions the agent may invoke for inference
- **Memory limits**: hard memory cap enforced via cgroup v2

Each tool invocation requires presenting a capability token scoped to the specific operation. An agent cannot self-elevate: it cannot grant itself capabilities it was not issued at launch. Capability delegation from parent to subagent must be conservative: the subagent's capability set is the intersection of the parent's capabilities and the explicitly delegated subset.

Near-term implementation: Landlock LSM, seccomp-BPF, and network namespaces. The full vision (cryptographic tokens presented at each tool invocation and verified before kernel enforcement) requires infrastructure not yet in mainline kernel but is architecturally aligned with Fuchsia/Zircon handle semantics.

### 6.4 Model Integrity Chain

A model loaded into the AI control plane must be verifiably the same artifact that was evaluated, approved, and signed. Four stages:

1. **Cryptographic signing.** Model registry stores SHA-256 hashes of weight files and adapter files, plus a digital signature over the manifest. At load time, verify signature before mapping weights into process memory.

2. **Load-time attestation.** For TEE deployments, the model loading process occurs inside the TEE and produces a remote attestation report including a measurement of the model loading procedure and the model's manifest hash. This closes the gap between "the registry says the hash matches" and "the running model is actually the registered model."

3. **Runtime integrity checks.** Map weight pages read-only after loading. Any write attempt generates a page fault caught by the kernel. Optional: periodic background re-hashing of weight memory against the stored manifest hash.

4. **Policy engine.** Enforce a model whitelist: only model versions in the approved manifest may be loaded. Loading an unlisted model is a security event logged via `aios_audit_log`.

---

## 7. Failure Modes and Recovery

### 7.1 Six Failure Modes

An AI-native OS has a new failure mode category with no classical analogue: the AI control plane can fail by producing wrong policy decisions with high confidence while continuing to run. A conventional kernel either runs correctly or crashes. An AI control plane can fail gracefully, producing output continuously, while the outputs are catastrophically incorrect.

**Table 6: AI Control Plane Failure Mode Taxonomy**

| Failure Mode | Description | Detection Mechanism | Time to Detect |
|---|---|---|---|
| Process crash | Segfault, OOM kill, unhandled exception in control plane process | Process monitor (systemd, supervisord); kernel exit notification | < 1 s |
| Inference livelock | Control plane enters non-terminating reasoning loop; generates tokens without producing policy decisions | Output rate monitor; token generation rate with timeout watchdog | 1–30 s |
| Wrong policy decision | AI makes catastrophically incorrect resource allocation, permission grant, or security decision | Circuit Breaker: S_a/C_r threshold violation; behavioral anomaly detector; operator audit | 1 s–1 min |
| Adversarial compromise | OS-level prompt injection causes control plane to act against system interests | Behavioral anomaly detection; action/intent divergence monitor; audit log anomaly analysis | Variable; may be slow |
| Weight corruption | Model weights modified by storage error, bit rot, or adversary | Hash verification at load time; periodic background re-hash | At load time or periodic interval |
| Split-brain | AI control plane and kernel disagree on current system state | State reconciliation heartbeat with state hash comparison | 1–10 s |

### 7.2 Conventional Fallback Mode

When the AI control plane is unavailable — crash, Circuit Breaker trip, adversarial compromise, or operator-initiated suspension — the system must continue operating in a defined degraded mode. This mode must be specified with the same precision as the nominal operating mode.

**Preserved in fallback:**
- Boot and initialization (substrate is always conventional; unaffected)
- Hardware isolation between agents (cgroup v2 and namespace configuration persists from last AI control plane configuration)
- Scheduling (default kernel scheduler: CFS on Linux, or configured sched_ext baseline policy, operating without AI-derived hints)
- Memory management (kernel default with LRU eviction; no semantic awareness)
- I/O (unaffected)
- Security enforcement (all kernel-enforced security mechanisms persist: seccomp, Landlock, network namespace)
- Audit logging (Merkle tree logging continues; AI control plane absence does not disable the audit trail)
- Operator override (operates at kernel privilege; does not require AI cooperation)

**Unavailable in fallback:**
- AI-driven policy optimization (workload placement, resource allocation)
- Agent orchestration (no new agents launched; running agents continue but cannot spawn subagents)
- Natural-language operator interface
- Predictive scheduling
- Adaptive resource allocation (limits are static)
- Model lifecycle decisions

**Transition:** Automatic on Circuit Breaker trip; manual via `aios_fallback_engage` privileged syscall. The transition must complete within one scheduling cycle — fallback state must be achievable without AI control plane cooperation, since it may be unresponsive.

**Return from fallback:** AI control plane restarts and performs state reconciliation. Authority is restored gradually: scheduling hints first, resource allocation decisions second, model lifecycle operations third. Full authority is restored only after Circuit Breaker confirms S_a and C_r are within acceptable bounds.

### 7.3 Circuit Breaker as Watchdog

The watchdog problem for AI systems has a structure that standard process monitoring does not address. A conventional watchdog (systemd, supervisord, hardware watchdog timer) monitors whether a process is alive and restarts it on failure. This is insufficient when the AI control plane can fail silently: it continues running, consuming compute, and producing wrong outputs, without any exception to catch or signal to handle.

A naive response is to use a second AI system to monitor the first. Do not do this. Two AI systems agreeing on wrong outputs is a coherent failure mode, not a detection mechanism.

The correct design: the watchdog must be simpler than what it monitors by construction, and must operate on observable system metrics rather than on AI-generated text.

The Circuit Breaker monitors two scalar metrics computed from observable system state — resource allocation outcomes, agent task completion rates, policy decision outcomes — not from the AI control plane's self-reported beliefs:

- **S_a (structural morphism quality):** measures how well the AI control plane's internal model of kernel state matches actual observable kernel state. Declining S_a indicates the control plane is developing a false picture of system state.
- **C_r (behavioral morphism quality):** measures the distance between AI-directed policy outputs and kernel-observed outcomes. Declining C_r indicates the control plane's outputs are diverging from their intended effects.

The Circuit Breaker cannot be compromised by the AI control plane because it does not share any input channels with it. The AI control plane processes agent messages, tool responses, and operator commands in its inference context. The Circuit Breaker reads kernel telemetry, process lifecycle events, and resource accounting metrics. An adversary who compromises the AI control plane via prompt injection cannot inject into the Circuit Breaker's metric inputs.

The Circuit Breaker runs at higher privilege than the AI control plane. It cannot be killed or influenced by the AI layer. When it trips, it calls `aios_fallback_engage` directly, bypassing the AI control plane.

This architecture substitutes simplicity for intelligence in the monitoring role. The Circuit Breaker is not more capable than the AI control plane; it is more reliable precisely because it is less capable. It computes two numbers against two thresholds. That is enough.

For the formal derivation of S_a and C_r as Wymore-morphism quality metrics and the full CBTO ontology grounding, see the AI Circuit Breaker Design Specification v4.0 and Section 13 of Part IV.

---

## 8. Reference Architectures

### 8.1 Architecture Comparison

Four reference architectures span the design space. They differ on three axes: how much of the existing OS stack is preserved, where AI components sit relative to the kernel privilege boundary, and how formally the interface between AI and non-AI layers is specified.

**Table 7: Reference Architecture Comparison**

| Dimension | A: AI-Augmented | B: AI-Native Control Plane | C: Microkernel + AI Services | D: Clean-Sheet AI OS |
|---|---|---|---|---|
| What stays conventional | Everything | Boot, isolation, memory, drivers, hard RT | Small verified core only | Minimal or nothing |
| Where AI sits | User-space apps and services | Primary policy/orchestration layer above substrate | Isolated user-level services | Throughout the system model |
| Interface model | Standard OS APIs (syscalls, SDK) | AI-Kernel Interface Contract (Section 9) | Capability-based IPC | AI-native primitives (context requests, tool bindings) |
| Watchdog | N/A (AI is an application) | Circuit Breaker (S_a, C_r thresholds) | Circuit Breaker as privileged service, kernel-isolated | Open question (critical vulnerability) |
| State management | Application-managed | OS-managed agent state store (MemCube) | Per-service, capability-bounded | First-class OS abstraction |
| Near-term prototype path | Deployed at scale today | eBPF + sched_ext + cgroups v2 on Linux | seL4 + CAmkES (research) | AIOS v5, MemOS, WASM/Hyperlight |
| Formal governance | None | Morphism monitoring (S_a, C_r) + SHACL | Kernel correctness proof + Circuit Breaker | Not yet defined |
| Main advantage | Fastest adoption; no ecosystem disruption | Best balance: practical + innovative | Strongest security/safety; machine-checked kernel | Maximum research freedom |
| Main weakness | AI remains peripheral; no composition guarantees | Boundary management; dual-scheduler coordination unsolved | High integration cost; narrow ecosystem | Immature; no watchdog solution; ecosystem isolation |
| Recommended context | Consumer devices, enterprise productivity | Server infrastructure, agentic platforms, research | Safety-critical, adversarial, classified | Research labs, AI-dominant greenfield workloads |
| TRL (2026) | 7–9 (deployed, operational) | 3–5 (proof of concept to component validated) | 2–4 (formulated to lab validated) | 1–3 (basic principles to proof of concept) |

### 8.2 Architecture B Component Diagram

Architecture B is the recommended near-term architecture. The AI control plane is the brain; the conventional kernel is the body. The following diagram presents Architecture B at component level (C4 level 2).

```
+-------------------------------------------------------------------+
|                    USER / OPERATOR INTERFACE                       |
|        (NL command console, audit dashboard, override panel)       |
+-------------------------------------------------------------------+
|                    AI-NATIVE CONTROL PLANE                         |
|  +----------+ +----------+ +----------+ +------------------+      |
|  |  Policy   | | Agent    | | Model    | | Orchestration    |      |
|  |  Engine   | | Scheduler| | Lifecycle| | & Planning       |      |
|  |           | |          | | Manager  | | (goal decomp.,   |      |
|  |(resource  | |(priority,| |(load,    | |  tool routing)   |      |
|  | alloc.,   | | latency, | | evict,   | |                  |      |
|  | policy)   | | preempt) | | rollback)| |                  |      |
|  +----------+ +----------+ +----------+ +------------------+      |
|  +----------+ +----------+ +----------+ +------------------+      |
|  | Agent    | | Tool     | | Security | | Circuit Breaker  |      |
|  | State    | | Registry | | Monitor  | | (S_a, C_r)       |      |
|  | Manager  | | (MCP/A2A)| | (MAC,    | | [WATCHDOG]       |      |
|  | (MemCube)| |          | |  audit)  | | --> fallback on  |      |
|  |          | |          | |          | |     threshold    |      |
|  +----------+ +----------+ +----------+ +------------------+      |
+-------------------------------------------------------------------+
|              AI-KERNEL INTERFACE CONTRACT                          |
|  Downward: aios_sched_hint | aios_mem_reserve                     |
|            aios_resource_fence | aios_audit_log                   |
|  Upward:   resource signals | security events                     |
|            memory pressure | lifecycle events                     |
+-------------------------------------------------------------------+
|                CONVENTIONAL SUBSTRATE (KERNEL)                     |
|  +----------+ +----------+ +----------+ +------------------+      |
|  | Process  | | Memory   | | Device   | | Security         |      |
|  | Scheduler| | Manager  | | Drivers  | | (LSM, isolation, |      |
|  |(sched_ext| |(cgroups  | |(GPU/NPU/ | |  namespaces,     |      |
|  |  hook)   | |  v2)     | |  DPU)    | |  seccomp)        |      |
|  +----------+ +----------+ +----------+ +------------------+      |
|  +----------+ +----------+ +-----------------------------+        |
|  | VFS /    | | Network  | | Boot / Trust Chain          |        |
|  | Storage  | | Stack    | | (UEFI -> kernel -> TPM)     |        |
|  +----------+ +----------+ +-----------------------------+        |
+-------------------------------------------------------------------+
|                    HARDWARE SUBSTRATE                              |
|  CPU    |  GPU    |  NPU    |  DPU    |  TEE    |  CXL Memory     |
+-------------------------------------------------------------------+

Note: Conventional Fallback Mode activates when Circuit Breaker trips.
In fallback mode, the AI-Native Control Plane is bypassed; the kernel
operates with its built-in scheduling and resource management policies.
The interface contract layer remains active to receive recovery signals.
```

### 8.3 Decision Framework

**Choose Architecture A if:**
- Your AI components are applications or system services, not infrastructure controllers
- You need to deploy within 12 months on existing hardware and existing OS
- Your agents do not require kernel-aware resource management
- You accept that resource contention between AI workloads and other processes will be resolved without semantic awareness

**Choose Architecture B if:**
- You are building server infrastructure, agentic platforms, or a research system intended to become production
- You need formal governance of AI policy decisions (morphism monitoring, Circuit Breaker, audit trail)
- You can work with TRL 3–5 components and expect to iterate
- You want ecosystem compatibility (Linux, existing driver stacks, existing security tooling)

**Choose Architecture C if:**
- Safety or security certification is required (avionics, automotive, classified systems)
- You have a team with seL4/microkernel experience and multi-year timeline
- Formal verification of the kernel substrate is a hard requirement, not a preference
- You can accept narrow ecosystem and higher IPC overhead

**Choose Architecture D if:**
- You are in a research lab with no production deployment timeline
- Your workload is AI-dominant and you have no legacy compatibility requirements
- You are explicitly exploring what OS-native agent abstractions look like from first principles
- You accept that there is no solved watchdog problem for this architecture

**Default recommendation: Architecture B.** It preserves the entire existing software ecosystem below the interface contract, enables progressive enhancement (Phase 1 prototypes add eBPF hooks; Phase 2 adds the full interface contract; Phase 3 extends to distributed substrates), and provides a concrete path to formal governance. The conventional substrate retains all existing certifications and safety properties. The AI control plane is an optional enhancement — Conventional Fallback Mode is always available.

---

## 9. Safety-Critical Contexts

### 9.1 The Certification Gap

Safety-critical software certification rests on three assumptions that neural networks systematically violate.

**Structural coverage is not testable.** DO-178C requires Modified Condition/Decision Coverage (MC/DC) for Design Assurance Level A (DAL-A) software. MC/DC requires demonstrating that each condition in every decision independently affects the decision outcome, exercising every path through the control flow graph. There is no accepted definition of MC/DC for a neural network and no tool that could compute it. The FAA has issued no guidance on neural network certification under DO-178C.

**Deterministic behavior cannot be assumed.** DO-178C and ISO 26262 assume that given the same inputs, a software component produces the same outputs. Neural networks with floating-point non-determinism, GPU round-off differences, and probabilistic sampling violate this assumption.

**Traceability from requirements to code is not available.** Both standards require bidirectional traceability from system requirements through software requirements to source code to executable object code. The "source" of a neural network is training data and a training procedure; there is no readable code that implements a specific safety requirement in a traceable way.

ISO/DPAS 8800 (AI safety for automotive) was in progress as of early 2026 but not yet ratified. There is no currently ratified standard providing a path to certify a neural network to DAL-A or ASIL-D.

### 9.2 Mixed-Criticality Partitioning

The only technically defensible near-term architecture for safety-critical deployments is mixed-criticality partitioning. This separates the system into two strictly isolated partitions:

**Safety-critical partition:** Contains only certifiable deterministic software. Implements the core safety function using certified RTOS (ARINC 653 partition executive for avionics; ISO 26262-compliant hypervisor for automotive). Certified to DO-178C DAL-A or ISO 26262 ASIL-D as appropriate. Has no run-time dependency on the AI partition.

**AI advisory partition:** Contains the AI components. Provides recommendations, optimization, and enhanced capability. Cannot take safety-critical actions directly. Communicates with the safety-critical partition only through defined, bounded interfaces with strict input validation and sanity checks.

### 9.3 The Separation Argument

If the AI components are non-safety-critical by architecture — if they cannot directly command safety-critical actuators and their outputs are validated before any safety-critical action is taken — then the certification argument applies only to:

1. **The substrate:** the conventional RTOS partition, which is certifiable
2. **The monitor:** the Circuit Breaker watchdog, which must itself be certifiable (deterministic, bounded, no neural network components)
3. **The interface boundary:** the input validation and sanity checks that prevent AI outputs from directly causing safety-critical actions

This is the "monitor-based certification strategy": certify the monitor and the substrate; treat the AI as an uncertified advisory component that can be overridden at any time. The monitor must be simpler than what it monitors by construction, which is why the Circuit Breaker's design (two scalar metrics against two thresholds) is not a simplification for convenience — it is the property that makes the watchdog certifiable.

Do not attempt to certify the AI components themselves under DO-178C or ISO 26262. The standards provide no path for this. The correct strategy is to ensure the AI is never the last line of defense for a safety-critical function.

---

## 10. Roadmap

### 10.1 Four-Phase Development Plan

**Table 8: Development Roadmap**

| Phase | Period | Name | TRL (2026 Assessment) | Measurable Exit Criteria |
|---|---|---|---|---|
| 0 | 2024–2026 | AI-Augmented Operations | 7–9 | AI features deployed by 3+ major platform vendors; peer-reviewed productivity evidence; stable NPU SDK APIs for third-party developers |
| 1 | 2025–2027 | Bounded Policy Automation | 3–5 | AI scheduler (sched_ext) demonstrably outperforms CFS on mixed AI/conventional benchmark; S_a computed and logged with < 2% CPU overhead; prototype operates 72 hours without human intervention |
| 2 | 2026–2029 | AI-Native Control Plane | 2–4 | Architecture B prototype with full interface contract runs 30 days under real agent workloads; Circuit Breaker detects and recovers from all 6 failure modes; S_a and C_r tracked with < 5% total monitoring overhead |
| 3 | 2028–2032 | Heterogeneous Resource Fabric | 1–3 | Multi-node agent migration with S_a > 0.80 maintained; composition morphism quality > 0.75 for delegation chains of depth 5+; mixed-criticality safety argument accepted by a domain certification authority as a candidate path |

Phase 0 is complete. The research frontier is Phase 1 (proving AI-aware scheduling outperforms conventional scheduling on semantically mixed workloads) and the integration work needed for Phase 2.

### 10.2 Six Recommendations as Checklist

- [ ] **Treat "AI-based OS" as a spectrum.** Be explicit: "We are building Architecture A with NPU acceleration" or "We are targeting Architecture B with morphism-based governance." Vague claims obscure tradeoffs and prevent meaningful evaluation.

- [ ] **Build on existing substrates in the near term.** Linux, Windows, and seL4 represent decades of engineering value. Architecture B preserves this value while enabling AI-native policy governance. Architecture D is appropriate for research contexts; it is not appropriate as the default production path in 2026.

- [ ] **Map AI families to OS responsibilities rather than picking one paradigm.** Neuro-symbolic systems for auditable policy reasoning. LLMs for natural language interfaces and code generation. RL policies for resource optimization with feedback. Probabilistic models for anomaly detection with calibrated uncertainty. An AI-OS that bets on one paradigm is fragile.

- [ ] **Treat standards as layered: classical OS standards remain necessary; AI interoperability standards are not a replacement.** POSIX, AUTOSAR, ARINC 653, and DO-178C specify mechanisms that MCP, A2A, and NIST AI agent standards do not address. Both layers are required.

- [ ] **Design for heterogeneous hardware from the start.** In 2026, AI inference does not run exclusively on CPU. NPUs, GPUs, and DPUs are first-class compute resources. Design the state management architecture (Section 5) and security architecture (Section 6) to account for non-CPU compute and disaggregated memory from the beginning, not as a retrofit.

- [ ] **Put governance, evidence, and failure-mode analysis on equal footing with capability demonstrations.** The Circuit Breaker is as important as the agent scheduler. Agent state isolation is as important as agent memory capacity. Morphism quality metrics are as important as agent throughput metrics. A system that can schedule 1,000 concurrent agents but has no watchdog, no fallback, and no formal governance is a liability.

---

## 11. Getting Started: Minimal Viable Prototype

This section describes a practical path to a single-node Architecture B prototype with measurable quality metrics. The target demonstrates the key architectural elements without requiring research-prototype infrastructure.

**Goal:** single-node prototype demonstrating Architecture B with a working Circuit Breaker, agent-aligned cgroup hierarchy, and measurable S_a/C_r quality metrics.

### Step 1: Start with Linux as Substrate

Require Linux 6.12 or later. This is non-negotiable: `sched_ext` was merged in 6.12 and is the enabler for all scheduling experiments. Confirm TPM 2.0 and UEFI Secure Boot are operational. Establish a baseline measurement of agent task latency with no modifications — this is your performance baseline for demonstrating improvement.

Verify the AgentCgroup result in your environment: measure the fraction of agent task latency attributable to kernel scheduling queues, syscall processing, and memory management. This fraction (typically 56–74%) is the headroom your prototype needs to recover.

### Step 2: eBPF + sched_ext for AI-Influenced Scheduling

Implement a `sched_ext` BPF scheduling class that assigns priority based on agent workload type. Start with a minimal policy: REALTIME for agents in active inference (decode phase), HIGH for agents waiting on tool call results, BACKGROUND for episodic memory writes and semantic index updates.

The BPF program should read agent workload metadata from a shared memory region maintained by the AI runtime. The runtime writes: current phase (prefill/decode/idle/blocked), latency budget, agent priority class. The BPF scheduler reads these values and makes per-dispatch decisions.

Measure the improvement: agent task throughput and tail latency should improve relative to the CFS baseline. Document the delta. This is your Phase 1 exit criterion demonstration.

### Step 3: cgroups v2 Aligned to Agent Boundaries

Create a cgroup hierarchy that matches agent task boundaries, not container boundaries. Structure:

```
/sys/fs/cgroup/aios/
  agent-<id>/          # one per logical agent
    inference/         # inference process and GPU worker threads
    tools/             # subprocesses spawned for tool execution
    state/             # state management I/O
```

Set CPU, memory, and I/O limits per agent cgroup. The hard memory limit (via `memory.max`) must be enforced at the agent level — if the agent exceeds its memory budget, the kernel kills the agent, not an unrelated process.

Align the `sched_ext` scheduling class from Step 2 to operate per-cgroup, not per-process. An agent that spawns subprocesses for tool execution inherits the scheduling policy from the parent agent cgroup.

### Step 4: MCP for Tool Integration

Integrate MCP as your tool invocation layer. Every agent tool call (file read, web fetch, database query, subprocess execution) must route through MCP, not through direct system calls from the agent process. This gives you:
- A single point to enforce capability checks before kernel enforcement
- An audit point for all tool invocations
- Rate limiting and timeout enforcement at the infrastructure layer, not in agent code

Wire each MCP tool server's Landlock ruleset (Step 6) to the tool's declared filesystem access requirements. The MCP server process holds the capability token; the agent process does not.

### Step 5: Simple Circuit Breaker

Implement the Circuit Breaker as a privileged daemon that the AI control plane cannot kill. It must read kernel telemetry, not AI-generated text.

Minimum viable Circuit Breaker implementation:

**S_a (structural quality):** At each measurement interval (suggest: 5 seconds), query the AI control plane's internal model of active agent states and resource allocations. Query the kernel (via cgroup stats, /proc, or eBPF maps) for actual active processes and their resource usage. Compute S_a as the fraction of the control plane's claimed state that matches observed kernel state. Declare a threshold: if S_a falls below 0.80 for three consecutive intervals, trip.

**C_r (behavioral quality):** Track the outcome rate of AI-issued scheduling hints. When the control plane issues `aios_sched_hint` with a latency budget, record whether the actual scheduling decision honored the budget. C_r is the fraction of honored hints over a sliding window. If C_r falls below 0.70 for two consecutive windows, trip.

**Trip action:** When either threshold is crossed, the Circuit Breaker writes a flag to a shared memory location that the kernel's `sched_ext` BPF program reads. The BPF program transitions to a conventional scheduling policy (CFS semantics) and stops honoring `aios_sched_hint` calls. Log the trip event to a kernel-maintained append-only file before the transition.

**Recovery:** Do not auto-recover. Require operator review of the trip event and explicit operator command to re-enable AI scheduling. This is a conservative policy appropriate for a prototype — Phase 2 systems can implement automated re-admission after S_a and C_r return to acceptable bounds.

### Step 6: Landlock for Tool Sandboxing

Apply Landlock LSM to every MCP tool server process. Each tool server has a manifest declaring which filesystem paths it requires access to. At tool server startup, apply a Landlock ruleset granting exactly those paths. Any access outside the ruleset is denied at kernel level.

Example: a file-reading tool server that should only read from `/home/data/` and `/tmp/` receives a Landlock ruleset permitting read access to those paths only. An attempt to read from `/etc/` is denied by the kernel, not by the application.

This is the tool capability model from Section 6.3, implemented with currently available kernel infrastructure. The full vision (cryptographic capability tokens presented at each invocation) is not required for the prototype.

### Step 7: Agent State Store

Deploy the four-store state architecture from Section 5.2:

- **Redis with AOF persistence:** execution context checkpoints at tool-call boundaries. Configure AOF persistence to ensure checkpoints survive process crashes.
- **vLLM or TGI with built-in KV cache management:** do not implement your own KV cache eviction. Use the inference engine's built-in LRU policy. Add priority annotations via `aios_mem_annotate` (or the prototype equivalent: a sidecar process that reads KV cache occupancy and sends MADV_DONTNEED hints for low-priority caches under memory pressure).
- **Qdrant (or Weaviate):** semantic memory with versioned collections. Tag every write with agent ID and timestamp.
- **etcd:** goal state with strong consistency. Use etcd's compare-and-swap for goal state updates to prevent lost writes under concurrent orchestrator access.

### Step 8: Measure Against Quality Metrics

A prototype that cannot be measured has not demonstrated anything. Collect these metrics:

| Metric | How to Measure | Target |
|---|---|---|
| Agent task throughput | Completed tasks per minute across the agent population | > CFS baseline |
| P95 agent task latency | 95th percentile end-to-end task time | < 80% of CFS baseline |
| Kernel overhead fraction | % of agent task time in kernel scheduling/memory | < 50% (vs. 56–74% baseline) |
| S_a | Control plane state vs. observed kernel state match fraction | > 0.85 under normal load |
| C_r | Fraction of scheduling hints honored within latency budget | > 0.80 under normal load |
| Circuit Breaker trip rate | Trips per 24 hours under normal load | < 1 per 24 hours |
| Recovery time from trip | Time from Circuit Breaker trip to stable fallback mode | < 1 scheduling cycle (< 10 ms) |

Report all seven metrics. A system that improves throughput but has low S_a has a governance problem that will manifest as a correctness failure under load. A system with high S_a and low C_r has a scheduling hint implementation problem. The metrics are diagnostic, not just pass/fail.

---

*For formal proofs, the WySE Metamodel formalization, the full AI-Kernel Interface Contract IDL, the CBTO ontology specification, SPARQL competency queries, and the complete survey of related work, see the AIOS-WySE Technical Report (Parts I–V) and the AI Circuit Breaker Design Specification v4.0.*
