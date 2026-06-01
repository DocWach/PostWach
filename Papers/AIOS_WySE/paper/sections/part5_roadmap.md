# Part V: Reference Architectures and Roadmap

<!-- Audience markers: [L] = Labrador (entry-level), [P] = Practitioner, [E] = Expert -->
<!-- Reading guide: [L] readers: Sections 17.1, 17.5 (recommendations only), and Table 6 captions. Skip Sections 15.3, 15.4, and all of Section 16. [P] readers: Sections 15.1-15.2, 17.1-17.5 (all). [E] readers: all sections. -->

---

## 15. Reference Architectures [P/E]

The analysis in Parts II through IV converges on a design space rather than a single prescribed architecture. The space is governed by three axes: how much of the existing OS stack is preserved, where AI components sit relative to the kernel privilege boundary, and how formally the interface between AI and non-AI layers is specified. Four reference architectures span this space. They are not mutually exclusive; real deployments often combine elements. The purpose of presenting them separately is to clarify the tradeoffs that practitioners must consciously choose among.

### 15.1 Architecture A: AI-Augmented Conventional OS [P]

**What stays conventional.** Everything. The kernel, bootloader, scheduler, memory manager, filesystem, device drivers, and the entire user-space contract remain unchanged. The OS is a standard general-purpose or mobile operating system (Linux, Windows, Android, macOS/iOS), deployed on conventional hardware with, increasingly, a Neural Processing Unit (NPU) alongside the CPU and GPU.

**Where AI sits.** AI components are user-space applications and system services. They access hardware through the same system-call interface as any other process. The NPU is exposed through vendor-specific SDKs (Windows AI Foundry, Apple Neural Engine APIs, Android NNAPI/AICore), but these are device drivers from the kernel's perspective—not architectural modifications to OS policy.

**Interface model.** Standard OS APIs: system calls, POSIX interfaces, SDK frameworks. No new kernel interface is required. The AI runtime is, from the kernel's point of view, just another process with memory, file descriptors, and CPU time.

**Watchdog strategy.** Not applicable in the OS-architecture sense. AI is an application, not a control-plane component. Standard process monitoring (systemd watchdog timers, Android ANR detection) applies. If an AI service crashes, the OS continues without it. No Circuit Breaker is needed because AI outputs do not gate kernel decisions.

**State management.** Application-managed. The OS provides no special agent-state primitives. Developers use whatever state stores their application needs—SQLite, Redis, in-process memory—within the normal process isolation boundary.

**Deployed examples.**
- *Microsoft Copilot+ PC*: Windows 11 with AI features delivered via Windows AI Foundry (formerly DirectML + ONNX Runtime). NPU-accelerated on Qualcomm Snapdragon X Elite, Intel Lunar Lake, and AMD Strix Point platforms. Copilot integrations run as Win32 processes and UWP apps. The NPU scheduler is managed by the Windows kernel's GPU scheduler extended to the NPU; this is a driver-level extension, not a control-plane change.
- *Apple Intelligence*: On-device models (~3B parameter language models) run on the Apple Neural Engine, prefilling via NPU and decoding via GPU. Private Cloud Compute offloads larger requests to Apple's own servers in a hardware-attested enclave. Foundation Models framework (WWDC 2025) exposes on-device model inference to application developers. The Neural Engine is an OS-managed hardware resource, but the intelligence policy is entirely in user space.
- *Google AICore / Gemini Nano*: An Android system service providing on-device foundation model execution for third-party apps. AICore runs as a privileged APK, not a kernel extension. Gemini Nano weights are managed by the service, isolated per app request through standard Android process boundaries.

**Main advantage.** Fastest adoption path. Leverages the entire existing software and hardware ecosystem. Developers need no new abstractions. Risk is bounded: AI components are isolated by the same mechanisms that isolate any application. Industry has demonstrated this at scale.

**Main weakness.** AI remains architecturally peripheral. Resource allocation for AI workloads is not semantically aware—the scheduler cannot distinguish an AI inference burst from a database query. There is no formal governance of AI outputs; the OS cannot enforce that AI-generated resource decisions are consistent with kernel state. Agent-aware resource management, composition guarantees, and morphism monitoring (Section 13) are all absent. This architecture supports the "OS for AI" program superficially but provides no formal foundation for the "AI for OS" program at all.

---

### 15.2 Architecture B: AI-Native Control Plane Over Conventional Substrate [P/E]

**This is the recommended near-term architecture.** It preserves the ecosystem value of a mature kernel while introducing a principled boundary at which AI components can govern system policy. The AI control plane is the brain; the conventional kernel is the body.

**What stays conventional.** The trusted boot path (UEFI → kernel), hardware isolation mechanisms (MMU, IOMMU), memory safety enforcement, interrupt handling, device mediation, and any hard-real-time functions that cannot tolerate non-deterministic latency remain in the conventional kernel substrate. These components must not be under AI control because their failure modes are not recoverable through software alone—a bug in the interrupt handler or memory protector is a system crash, not a policy error.

**Where AI sits.** The AI control plane occupies a well-defined layer above the kernel substrate. It holds primary authority over resource allocation policy, agent scheduling, model lifecycle management, and tool orchestration. It expresses intent to the kernel through the AI-Kernel Interface Contract (Section 9) and receives resource state from the kernel through upward signals. The kernel executes mechanism; the AI control plane sets policy.

**Interface model.** The AI-Kernel Interface Contract specified in Section 9. Downward API: `aios_sched_hint` (scheduling intent, latency budgets, priority classes), `aios_mem_reserve` (agent working-set reservation, eviction policies), `aios_resource_fence` (hardware partition binding, GPU MIG slice assignment), `aios_audit_log` (kernel-enforced, tamper-evident audit trail). Upward API: resource availability and contention signals, security events (anomalous syscall patterns, privilege-escalation attempts), memory pressure events requiring agent context eviction, process/container lifecycle events.

**Watchdog strategy.** The Circuit Breaker (Section 13) monitors structural morphism quality S_a and behavioral morphism quality C_r continuously. S_a measures the degree to which the AI control plane's internal model of kernel state matches actual kernel state. C_r measures the distance between AI-directed policy outputs and kernel-observed outcomes. The Circuit Breaker is architecturally simpler than the AI control plane by construction: it computes two scalar metrics against two thresholds. It operates on observable system metrics (resource counters, scheduling outcomes, memory maps), not on AI-generated text, so it cannot be manipulated by the AI layer. On trip, the system transitions to Conventional Fallback Mode (Section 12.3): the kernel substrate runs standalone using conventional scheduling and resource management policies. Recovery and re-admission of the AI control plane follow the monitoring protocol in Section 13.4.

**State management.** A dedicated agent state store with OS-level lifecycle management (Section 10). The store manages five state categories per agent: execution context, episodic memory, semantic memory, goal state, and resource bindings. The OS treats agent state as a first-class resource subject to the same eviction, checkpointing, and isolation policies that govern process memory. MemCube-inspired abstractions organize state across volatile in-process memory, dedicated on-device persistent stores, and distributed coordination layers.

**Near-term prototype path.** The Linux kernel provides three insertion points sufficient for Phase 1 prototyping: (1) *eBPF + sched_ext*—eBPF programs can intercept scheduling decisions; sched_ext (merged in Linux 6.11) allows full replacement of the scheduling class for specific process groups, enabling an AI-generated scheduling policy to operate alongside the conventional scheduler without kernel modification. (2) *cgroups v2*—hierarchical resource control provides agent boundary alignment without kernel modification; CPU, memory, and I/O limits can be set per agent cgroup. (3) *Landlock LSM*—a capability-based sandboxing mechanism for tool access control, operable from user space. AgentCgroup (arXiv:2602.09345) demonstrates the feasibility of cgroup-aligned agent resource management on stock Linux, reporting effective isolation with less than 3% overhead for CPU-bound workloads.

**Component diagram.** The following text diagram presents Architecture B at component level (C4 level 2). Solid boxes represent components; layers are separated by horizontal rules.

```
┌─────────────────────────────────────────────────────────────────┐
│                    USER / OPERATOR INTERFACE                     │
│        (NL command console, audit dashboard, override panel)     │
├─────────────────────────────────────────────────────────────────┤
│                    AI-NATIVE CONTROL PLANE                       │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────────────┐  │
│  │  Policy   │ │ Agent    │ │ Model    │ │ Orchestration    │  │
│  │  Engine   │ │ Scheduler│ │ Lifecycle│ │ & Planning       │  │
│  │          │ │          │ │ Manager  │ │ (goal decomp.,   │  │
│  │(resource │ │(priority,│ │(load,    │ │  tool routing)   │  │
│  │ alloc.,  │ │ latency, │ │ evict,   │ │                  │  │
│  │ policy)  │ │ preempt) │ │ rollback)│ │                  │  │
│  └──────────┘ └──────────┘ └──────────┘ └──────────────────┘  │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────────────┐  │
│  │ Agent    │ │ Tool     │ │ Security │ │ Circuit Breaker  │  │
│  │ State    │ │ Registry │ │ Monitor  │ │ (S_a, C_r)       │  │
│  │ Manager  │ │ (MCP/A2A)│ │ (MAC,    │ │ [WATCHDOG]       │  │
│  │(MemCube) │ │          │ │  audit)  │ │ --> fallback on  │  │
│  │          │ │          │ │          │ │     threshold    │  │
│  └──────────┘ └──────────┘ └──────────┘ └──────────────────┘  │
├─────────────────────────────────────────────────────────────────┤
│              AI-KERNEL INTERFACE CONTRACT                        │
│  Downward: aios_sched_hint | aios_mem_reserve                   │
│            aios_resource_fence | aios_audit_log                 │
│  Upward:   resource signals | security events                   │
│            memory pressure | lifecycle events                   │
├─────────────────────────────────────────────────────────────────┤
│                CONVENTIONAL SUBSTRATE (KERNEL)                   │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────────────┐  │
│  │ Process  │ │ Memory   │ │ Device   │ │ Security         │  │
│  │ Scheduler│ │ Manager  │ │ Drivers  │ │ (LSM, isolation, │  │
│  │(sched_ext│ │(cgroups  │ │(GPU/NPU/ │ │  namespaces,     │  │
│  │  hook)   │ │  v2)     │ │  DPU)    │ │  seccomp)        │  │
│  └──────────┘ └──────────┘ └──────────┘ └──────────────────┘  │
│  ┌──────────┐ ┌──────────┐ ┌──────────────────────────────┐   │
│  │ VFS /    │ │ Network  │ │ Boot / Trust Chain            │   │
│  │ Storage  │ │ Stack    │ │ (UEFI → kernel → TPM attest.) │   │
│  └──────────┘ └──────────┘ └──────────────────────────────┘   │
├─────────────────────────────────────────────────────────────────┤
│                    HARDWARE SUBSTRATE                            │
│  CPU    │  GPU    │  NPU    │  DPU    │  TEE    │  CXL Memory  │
└─────────────────────────────────────────────────────────────────┘

Note: Conventional Fallback Mode activates when Circuit Breaker trips.
In fallback mode, the AI-Native Control Plane is bypassed; the kernel
operates with its built-in scheduling and resource management policies.
The interface contract layer remains active to receive recovery signals.
```

**Main advantage.** Architecture B offers the best balance between practical deployability and architectural innovation. It preserves the entire existing software ecosystem below the interface contract, enables progressive enhancement (Phase 1 prototypes add eBPF hooks; Phase 2 adds the full interface contract; Phase 3 extends to distributed substrates), and provides a concrete path to formal governance through morphism monitoring. The conventional substrate retains all existing certifications and safety properties. The AI control plane is an optional enhancement, not a required component—Conventional Fallback Mode is always available.

**Main weakness.** Boundary management and observability become the central design challenges that Architecture A avoids and that Architecture D sidesteps by eliminating the boundary altogether. The dual-scheduler coordination problem—ensuring that the AI agent scheduler and the kernel process scheduler do not produce conflicting decisions under load—is unsolved for production systems. The interface contract must be stable enough to prevent the AI control plane from circumventing kernel enforcement, but expressive enough to give the AI layer meaningful policy authority. Defining and maintaining that boundary is both a technical and organizational challenge.

---

### 15.3 Architecture C: Microkernel/High-Assurance Substrate with AI Services [E]

**What stays conventional.** A small, formally verified trusted core occupying the kernel privilege boundary. In the seL4 lineage, the kernel comprises approximately 10,000 lines of C, machine-checked against an Isabelle/HOL specification—a proof corpus representing roughly 200,000 lines. This core provides only the minimum trusted functions: address space management, capability-based access control, inter-process communication (IPC), and thread scheduling. Everything else—device drivers, filesystems, networking, and AI services—runs above the core in user-level protection domains.

**Where AI sits.** AI components run as isolated services above the trusted core, each confined to its own protection domain. A domain receives a bounded set of capabilities from the microkernel at instantiation time; it can exercise only those capabilities and cannot expand its authority without kernel-mediated negotiation. An AI planning service, a model inference service, and a tool orchestration service are separate domains that communicate through kernel-mediated IPC channels.

**Interface model.** Capability-based IPC. The microkernel allocates capability tokens that represent the right to perform specific operations: send a message on a specific endpoint, read from a specific memory region, invoke a specific service. AI services hold capability tokens for the operations they need; the kernel enforces that no operation occurs without a valid token. This is the Plan 9 / seL4 capability model applied to AI services. The AI-Kernel Interface Contract of Section 9 can be implemented as a set of microkernel IPC endpoints with capability-gated access.

**Watchdog strategy.** The Circuit Breaker runs as a privileged service—more trusted than the AI services but below the kernel. It holds monitor capabilities granting read access to AI service execution counters and output histories. Compromising the Circuit Breaker requires compromising a separate protection domain, not just corrupting the AI service. This is the strongest watchdog architecture of the four, because the kernel enforces the boundary between the AI layer and the monitor.

**State management.** Each AI service manages its own state within its protection domain. Shared state—such as agent context accessible to both a planning service and an execution service—is exchanged through kernel-mediated IPC channels. The kernel guarantees that only domains holding the appropriate capability token can read or write shared state. This eliminates the KV cache isolation problem (Section 10.3) by construction, at the cost of IPC overhead on every cross-domain state access.

**Deployed examples.** No production AI-OS currently uses a microkernel substrate. seL4 is deployed in safety-critical avionics (DARPA HACMS program, Boeing AH-64D helicopter), autonomous vehicles (Waymo research platforms), and classified defense systems, but AI services above seL4 remain a research direction. The CAmkES component architecture for seL4 provides a component definition language and connector model that could support AI service composition; this has not been demonstrated at AI-OS scale.

**Formal methods and AI convergence.** The verification investment that makes Architecture C expensive is itself becoming an AI-assisted activity. Three developments are relevant. First, *vericoding*—using large language models to generate formally verified code from specifications—has demonstrated preliminary results on bounded arithmetic and string manipulation problems. Second, the *Selene framework* (2025) uses LLMs to automate portions of seL4 proof maintenance when the kernel is extended with new features, reducing the human proof-engineering burden. Third, *DeepSeek-Prover-V2* (2025) achieves state-of-the-art performance on the miniF2F formal mathematics benchmark, suggesting that LLM-assisted theorem proving is approaching the capability needed for real kernel proofs. If these trends continue, the ~20 person-year investment that produced the seL4 proof might be achievable in a fraction of the time within a five-year horizon. This would make Architecture C substantially more attractive.

**Main advantage.** The strongest security and safety story of any architecture. The kernel's machine-checked correctness proof provides a foundation that Architecture B's Linux or Windows substrate cannot match. Formal verification is tractable because the kernel is small—a property that Dijkstra's original microkernel argument predicted and seL4's proof validates empirically. In safety-critical or adversarial deployment contexts where formal guarantees are required, Architecture C is the only option.

**Main weakness.** Higher integration cost, narrower ecosystem, and a verification investment that has historically required large, specialized teams. The IPC overhead of microkernel communication imposes latency costs on AI workloads that do not arise in Architecture B. Most AI frameworks, inference runtimes, and agent orchestrators are built for Linux or Windows; porting them to a seL4 substrate requires significant engineering. The ecosystem gravity problem (Section 5.3) is most severe here.

---

### 15.4 Architecture D: Clean-Sheet AI OS [E]

**What stays conventional.** Minimal or nothing. Architecture D discards the assumption that an AI OS must build on an existing kernel and instead asks: if we designed the entire system with AI agents as the primary abstraction, what would the OS look like? The answer is a system in which models, tools, context windows, and agent interactions are first-class constructs at the same level that processes, files, and sockets are in a POSIX OS.

**Where AI sits.** Throughout the system model. The "kernel" in Architecture D is not a privilege-mode execution environment for deterministic code but a resource manager whose primary abstraction is the agent and whose primary resource is context. Scheduling means context scheduling: deciding which agent's context is active on which compute resource. Memory management means context lifecycle management: which context fragments are hot in accelerator memory, which are evicted to system DRAM, and which are compressed to persistent storage.

**Interface model.** AI-native primitives replace system calls. An agent requests resources through context requests, binds external capabilities through tool bindings, and persists state through memory operations that are semantically aware of the memory taxonomy (Section 10.1). Two research prototypes illustrate this model. AIOS v5 (COLM 2025) implements an LLM kernel with agent scheduling, context switching, and memory management primitives; the paper demonstrates that agent throughput increases and latency decreases when the OS is semantically aware of agent structure compared to a naive process-per-agent baseline. MemOS (2025) treats memory as the first-class OS resource, organizing agent memory in MemCubes that unify volatile context, persistent episodic storage, and retrieved semantic memory under a single lifecycle management framework. The "Everything is Context" proposal (arXiv:2512.05470) extends the Unix "everything is a file" philosophy to a context-as-filesystem abstraction, making agent context mountable, versionable, and subject to access control as a hierarchical namespace.

**Watchdog strategy.** This is an open question and a fundamental architectural vulnerability. If the AI is the OS—if the agent scheduler decides which agents run and when, and the context manager decides what is retained—then compromising the AI layer is compromising the OS itself. Architecture A and B have a conventional kernel that can take over when the AI layer fails. Architecture C has the microkernel's verified core. Architecture D has no such fallback. The watchdog must be either a separate verified component (importing elements of Architecture C) or an external hardware mechanism. Neither current AIOS prototypes nor MemOS address this question satisfactorily.

**State management.** First-class OS abstraction. Agent state is not a side concern managed by applications; it is the primary resource the OS manages. The MemCube lifecycle—creation, active use, eviction, compression, long-term persistence, retrieval—is the OS memory management policy. This is the most agent-native design possible and potentially the most efficient for AI-dominant workloads. It is also the most incompatible with the assumption that the OS must also run non-AI workloads.

**The WASM/WASI path.** WebAssembly (WASM) provides an alternative substrate for Architecture D that avoids some clean-sheet risks. WASM modules run in a capability-constrained sandbox with memory safety by construction. WASI (WebAssembly System Interface) provides a minimal OS interface for filesystem, network, and clock access. WASI-NN adds hardware-accelerated neural network inference as a WASI capability. WebGPU provides GPU compute access within the same sandbox model. Microsoft's Hyperlight Wasm (March 2025) enables WASM execution without a host OS—Hyperlight provides a minimal hypervisor that runs WASM components directly, offering a library-OS-for-AI path. This architecture could host an Architecture D AI-OS as a WASM component running on a minimal Hyperlight hypervisor, preserving memory safety and capability isolation without requiring a full POSIX substrate. The ecosystem implications remain unclear: AI inference libraries are currently native-code artifacts that require non-trivial effort to compile to WASM targets.

**Main advantage.** Maximum conceptual freedom and research opportunity. Architecture D asks the deepest questions: what does an OS look like when agents are the primary abstraction? The answers generated by AIOS, MemOS, and related systems are producing genuine insights about context scheduling, memory lifecycle management, and agent composition that will inform all four architectures.

**Main weakness.** Architecture D systems are research prototypes, not production systems. They must re-solve problems that decades of OS engineering have already solved—privilege separation, driver ecosystems, interrupt handling, power management, hardware certification—or accept that they only run on curated hardware environments where those problems have been externalized. The watchdog problem is an architectural liability with no current solution. Ecosystem isolation means that existing applications and tools cannot run without emulation layers. For any deployment context beyond a research cluster, Architecture D requires either solving the legacy compatibility problem or limiting deployment to greenfield AI-only workloads.

---

### Table 6: Reference Architecture Comparison

| Dimension | A: AI-Augmented | B: AI-Native Control Plane | C: Microkernel + AI Services | D: Clean-Sheet AI OS |
|---|---|---|---|---|
| **What stays conventional** | Everything | Boot, isolation, memory, drivers, hard RT | Small verified core only | Minimal or nothing |
| **Where AI sits** | User-space apps and services | Primary policy/orchestration layer above substrate | Isolated user-level services | Throughout the system model |
| **Interface model** | Standard OS APIs (syscalls, SDK) | AI-Kernel Interface Contract (Section 9) | Capability-based IPC | AI-native primitives (context requests, tool bindings) |
| **Watchdog** | N/A (AI is an application) | Circuit Breaker (S_a, C_r thresholds) | Circuit Breaker as privileged service, kernel-isolated | Open question (critical vulnerability) |
| **State management** | Application-managed | OS-managed agent state store (MemCube) | Per-service, capability-bounded | First-class OS abstraction |
| **Near-term prototype path** | Deployed at scale today | eBPF + sched_ext + cgroups v2 on Linux | seL4 + CAmkES (research) | AIOS v5, MemOS, WASM/Hyperlight |
| **Formal governance** | None | Morphism monitoring (S_a, C_r) + SHACL | Kernel correctness proof + Circuit Breaker | Not yet defined |
| **Main advantage** | Fastest adoption; no ecosystem disruption | Best balance: practical + innovative | Strongest security/safety; machine-checked kernel | Maximum research freedom; cleanest agent-native design |
| **Main weakness** | AI remains peripheral; no composition guarantees | Boundary management; dual-scheduler coordination unsolved | High integration cost; narrow ecosystem | Immature; no watchdog solution; ecosystem isolation |
| **Recommended context** | Consumer devices, enterprise productivity | Server infrastructure, agentic platforms, research | Safety-critical, adversarial, classified | Research labs, AI-dominant greenfield workloads |
| **TRL (2026)** | 7–9 (deployed, operational) | 3–5 (proof of concept to component validated) | 2–4 (formulated to lab validated) | 1–3 (basic principles to proof of concept) |

*Table 6. Reference architecture comparison across eight dimensions. TRL = Technology Readiness Level per NASA/ESA conventions. TRL 9 = operational in operational environment; TRL 1 = basic principles observed.*

---

## 16. Safety-Critical Considerations [E]

The preceding sections describe architectures that are appropriate for general-purpose and research computing environments where a system failure is inconvenient but not catastrophic. Safety-critical domains—avionics, automotive, industrial control, defense—impose qualitatively different constraints. This section assesses what AI-OS architectures can honestly claim for safety-critical applications in 2026 and defines a technically defensible path forward.

### 16.1 The Certification Gap

Safety-critical software certification rests on three assumptions that neural networks systematically violate.

**First assumption: structural coverage is testable.** DO-178C (Software Considerations in Airborne Systems and Equipment Certification, the governing standard for avionics) requires Modified Condition/Decision Coverage (MC/DC) for Design Assurance Level A (DAL-A) software—the highest criticality level. MC/DC requires demonstrating that each condition in every decision independently affects the decision outcome, and requires a test suite that exercises every path through the control flow graph. For a neural network, the "control flow graph" is the computation graph of a forward pass through hundreds of millions or billions of parameters. There is no accepted definition of MC/DC for a neural network, and no tool that could compute it. The FAA has issued no guidance on neural network certification under DO-178C; the standard's language predates the deep learning era.

**Second assumption: freedom from interference is provable.** ISO 26262 (Road Vehicle Functional Safety, governing automotive systems) at ASIL D (the highest integrity level) requires Freedom From Interference (FFI) between software partitions: the failure of one partition must not propagate to another. For a neural network with shared parameters across tasks—standard in any foundation model or multi-task learning system—the activations produced for one input depend on the weights trained for all inputs. A weight corruption that causes miscategorization of pedestrian images may affect lane-marking detection if the network shares intermediate representations. Proving FFI for such a network is not an engineering challenge that better tools will solve; it is a fundamental property of parameter sharing.

**Third assumption: static analyzability enables exhaustive hazard analysis.** IEC 61508 (Functional Safety of Electrical/Electronic/Programmable Electronic Safety-Related Systems, for industrial applications) at Safety Integrity Level 4 (SIL 4) requires systematic analysis of all failure modes through techniques including Failure Modes and Effects Analysis (FMEA) and Fault Tree Analysis (FTA). These techniques require knowing, for every input, what the software will output—a property that static analysis can establish for deterministic code. For a neural network, the function from inputs to outputs is a learned approximation whose behavior on out-of-distribution inputs is not bounded by any technique currently accepted by certification authorities.

**In-progress standard.** ISO/DPAS 8800 (Road Vehicles—Safety and Artificial Intelligence) is under development as of 2026. It acknowledges the gap and proposes operational design domains (ODDs) as a bounding mechanism: certify that the AI system behaves correctly within a specified operational envelope, and halt operation when the system detects that it has left the ODD. This is conceptually compatible with the Circuit Breaker architecture (Section 13)—the morphism quality metrics S_a and C_r can operationalize ODD boundaries. However, ISO/DPAS 8800 had not been ratified as of the writing of this report; it remains a Draft Publicly Available Specification.

**The honest assessment.** In 2026, no neural network component can be certified to DAL-A, ASIL D, or SIL 4. Any AI-OS claiming certification at these levels for its AI components is either misrepresenting the certification scope or using a definition of "AI" that excludes learned neural models.

### 16.2 Mixed-Criticality AI OS: The Only Defensible Near-Term Architecture

Given the certification gap, the only technically defensible architecture for deploying AI capabilities in safety-critical systems is *mixed-criticality partitioning*: safety-critical functions and AI advisory functions run in separate, isolated partitions with well-defined and verified non-interference properties between them.

**Partitioning mechanism.** ARINC 653 (Avionics Application Software Standard Interface) defines temporal and spatial partitioning for safety-critical avionics software. Temporal partitioning allocates fixed, non-preemptable time windows to each partition; the window sizes and allocation are determined at configuration time and cannot be modified at runtime. Spatial partitioning enforces that no partition can read or write the memory of another. ARINC 653 partitioning has been certified as a correct implementation of Freedom From Interference.

**AUTOBEST.** The AUTOBEST kernel provides a unified substrate implementing both AUTOSAR-OS (the dominant automotive RTOS standard) and ARINC 653, enabling a single hardware platform to host both automotive control functions (AUTOSAR partition) and advisory AI functions (separate partition) under a single certified kernel. The critical property: AUTOBEST's kernel has been analyzed for timing and spatial isolation properties. A failure in the AI partition—including any software fault that corrupts the AI partition's memory—cannot propagate across the kernel-enforced spatial isolation boundary. A runaway AI inference process cannot steal CPU time from the AUTOSAR partition because temporal isolation is enforced by the kernel's partition scheduler, not by the application.

**Architectural interpretation.** Mixed-criticality AI OS is Architecture B (AI control plane over conventional substrate) specialized for safety-critical contexts, where "conventional substrate" is a certified RTOS providing ARINC 653-class partitioning. The AI control plane occupies one or more non-safety partitions. The safety-critical control functions occupy certified partitions. The interface between them is restricted to specific, audited communication channels (shared memory regions with explicit access grants in the ARINC 653 partition configuration table, or time-triggered message-passing). The safety-critical partition must be designed to function correctly when the AI partition is silent, slow, or producing garbage outputs—exactly the Conventional Fallback Mode of Section 12.3.

**Consequences for AI capability.** In a mixed-criticality design, the AI layer may recommend but never mandate safety-critical actions. An AI planner can recommend a braking strategy; the AUTOSAR safety monitor enforces the braking envelope. An AI scheduler can request resource priority; the RTOS time partition allocates deterministic time windows regardless. The AI layer's inability to override safety-critical decisions is the source of the architecture's safety argument—and the source of its capability limitation. AI that can only advise cannot fully exploit the potential of AI-native resource management.

**Deployment examples.** Diehl Aerospace's ADIROS avionics OS uses ARINC 653 spatial/temporal partitioning with planned provision for AI service partitions. Green Hills Software's INTEGRITY-178 RTOS (certified to DO-178C DAL A) is used in FAA-certified avionics and is exploring AI advisory service integration in non-certified partitions. Neither has shipped a production AI-native control plane; both have explored mixed-criticality architectures in research programs.

### 16.3 Path to Certifiable AI Components

Three progressive strategies define the trajectory from "AI cannot be certified" to "AI components are certifiable."

**Strategy 1: Monitor-based certification (near-term, achievable today).** The AI component itself is not certified. The *monitor*—the Circuit Breaker—is certified. The monitor enforces that AI outputs remain within bounds that have been analytically or empirically established. When the AI output exits the certified envelope (S_a or C_r crosses threshold), the monitor transitions the system to a fallback that *is* certified. This is the Simplex architecture pattern applied to AI: a complex, uncertified high-performance channel running in parallel with a simple, certified fallback channel, with a certified switching monitor. The AI channel may produce better decisions; the certified channel produces safe decisions; the monitor decides which to use. The certification scope is reduced to: (a) the conventional substrate, (b) the Circuit Breaker monitor, (c) the certified fallback control logic, and (d) the architectural argument that the transition mechanism is correctly implemented. This is a tractable certification scope that existing standards can address.

**The separation argument.** If the AI control plane is designed such that the system can continue operating safely at all times without the AI control plane—if Conventional Fallback Mode is always safe—then the AI control plane is provably non-safety-critical by construction. A non-safety-critical component does not require safety certification. The certification authority needs only to verify that the fallback transition is reliable and that the AI control plane cannot corrupt the certified substrate. The AI layer becomes a performance enhancement whose loss degrades capability but not safety. This framing reduces the certification problem from "certify neural networks" (infeasible) to "certify the fallback mechanism and the isolation boundary" (feasible with existing standards).

**Strategy 2: Proof-carrying code (medium-term, 3–7 years).** AI policy modules are accompanied by formal proofs that their outputs satisfy specified safety properties: a learned scheduler will never assign a CPU time slice that violates a specified deadline bound; a learned memory allocator will never return an already-allocated address. The OS verifies the proof at module load time. This approach requires that AI module outputs be checkable by a simple verifier—the proof must be in a form that the OS kernel (or a trusted proof-checker executing alongside it) can verify in bounded time. For learned policies with convex output constraints, linear arithmetic decision procedures could serve as verifiers. For general neural networks, the required proof infrastructure does not yet exist. Vericoding research is producing tools that generate proofs for bounded classes of programs; extending this to learned policies is a near-term research target.

**Strategy 3: End-to-end formal verification (long-term, 10+ years).** The entire AI control plane, including learned components, is formally verified against a specification. For purely neural network components, this is infeasible with current techniques—the Lipschitz constant bounds on neural network outputs that form the basis of existing neural verification tools scale exponentially in network depth. However, neuro-symbolic architectures—where learned components produce inputs to a formal reasoning layer whose outputs are guaranteed by proof—are an active research area. A neuro-symbolic OS policy module that learns a heuristic and feeds it to a verified formal planner produces verifiable outputs by construction. The formal planner's correctness proof covers the outputs; the learned component is responsible only for performance, not correctness. This is the DARPA CLARA vision (compositional learning and reasoning) applied to OS policy, and the connection between this paper's formal architecture (Section 13) and that program is not coincidental.

---

## 17. Roadmap, Recommendations, and Open Research Questions [L/P/E]

*[L] readers: This section describes what is happening now (Phase 0), what will be built in the near term (Phase 1), and what the research community is aiming for. Focus on the Phase descriptions and the six recommendations (Section 17.5). The open questions (Section 17.6) are for expert readers.*

### 17.1 Phase 0: AI-Augmented Operations (2024–2026, Current State) [L/P]

**What exists.** AI capabilities are deployed as applications and system services on conventional operating systems. Natural language search surfaces files and application features. Diagnostic assistants interpret system logs and suggest remediation. Policy drafting tools generate configuration suggestions for review by administrators. Code completion and generation tools accelerate developer workflows. Agent orchestration frameworks (claude-flow, LangGraph, AutoGen) operate as user-space processes, not as OS components.

**Industry evidence.** Microsoft's Copilot+ PC platform ships with AI-accelerated Windows features via Windows AI Foundry on devices with NPU hardware. Apple Intelligence is available on iPhone 16 and recent Mac hardware with the Apple Neural Engine. Android AICore provides on-device Gemini Nano inference to third-party applications on Pixel 9 and licensed OEM devices. GitHub Copilot reports developer adoption at scale with documented productivity impacts [1]. The claude-flow orchestration framework demonstrates multi-agent workflow management at the application layer without kernel involvement.

**Formal status.** Architecture A (Section 15.1). The AI layer has no formal interface to the OS, no morphism-based governance, and no agent-aware resource management. Resource contention between AI workloads and other processes is resolved by the conventional OS scheduler without semantic awareness.

**TRL assessment.** TRL 7–9 (system prototype demonstrated in operational environment to operational system). AI-augmented OS features are deployed commercially at scale and generating measurable user value.

**Exit criteria for Phase 0.** AI features are present in production OSes from at least three major platform vendors. Measurable productivity gains are documented in peer-reviewed studies or reproducible industry analyses. NPU-accelerated on-device inference is available to third-party developers through stable SDK APIs. All of these criteria are met or substantially met as of early 2026.

### 17.2 Phase 1: Bounded Policy Automation (2025–2027) [P]

**What is built.** The AI control plane begins influencing kernel-level resource decisions within explicitly bounded domains and with mandatory rollback paths. Primary target functions: workload placement (which agent workload runs on which compute resource), resource tuning (CPU and memory allocation to agent cgroups), and tool invocation orchestration (scheduling external API calls and file system operations on behalf of agents). All AI-generated resource decisions are logged, bounded by policy constraints that cannot be overridden by the AI layer, and subject to rollback if a monitoring metric crosses threshold.

**Mechanisms.** eBPF programs implement scheduling hints interpretable by sched_ext. cgroups v2 hierarchies align agent boundaries with OS resource accounting. Landlock LSM enforces tool capability boundaries for agent file and network access. The AI control plane issues resource hints through a preliminary version of the downward API (Section 9.2); the kernel may honor or ignore them based on hard resource constraints. MCP and A2A protocol handlers are integrated as controlled tool invocation endpoints, each bounded by capability tokens.

**Formal elements introduced.** Initial morphism monitoring: S_a only (structural morphism quality). The AI control plane's model of kernel resource state is compared against actual kernel resource state at configurable intervals. S_a declining below 0.85 triggers an alert and begins rate-limiting AI resource hints. The behavioral metric C_r is instrumented but not yet used as a trip condition—operators calibrate C_r baselines during this phase.

**Research milestones.** AgentCgroup feasibility demonstration (arXiv:2602.09345) establishes the cgroup-based isolation baseline. sched_ext + LLM scheduling policy papers expected from systems venues in 2026. First morphism-quality monitoring prototypes integrated with Linux eBPF infrastructure.

**TRL assessment.** TRL 3–5 (proof-of-concept to component validated). Individual mechanisms are demonstrated; integration in a coherent prototype under realistic workloads is the Phase 1 research frontier.

**Exit criteria for Phase 1.** A prototype AI scheduler implemented via sched_ext demonstrably outperforms the CFS scheduler (Linux Completely Fair Scheduler) on a defined mixed AI-and-conventional workload benchmark, with the performance difference attributable to AI semantic awareness of agent workload structure. S_a is computed and logged continuously with less than 2% CPU overhead on the monitoring path. The prototype operates without human intervention for at least 72 hours under variable load without triggering safety fallback due to AI-induced instability.

### 17.3 Phase 2: AI-Native Control Plane (2026–2029) [P/E]

**What is built.** Agents become managed system entities with OS-level scheduling, memory management, access control, and lifecycle management. The AI-Kernel Interface Contract (Section 9) is implemented in full: both downward and upward APIs are operational. The Circuit Breaker watchdog is deployed and trip-tested. Agent state architecture (Section 10) is implemented: all five state categories are managed under OS lifecycle policies, with explicit eviction, checkpointing, and restore semantics. The security architecture (Section 11) is instantiated: MAC for agents, tool capability model, model integrity chain, and tamper-evident provenance are operational.

**Formal elements implemented.** Full morphism monitoring: both S_a and C_r are computed continuously and used as Circuit Breaker trip conditions. The SHACL validation pipeline (Section 14) enforces governance policies—agent state structure, resource binding constraints, provenance requirements—with two-tier validation (advisory syntax check + blocking full validation). SPARQL competency queries are run on schedule to verify that the OS governance ontology remains consistent with operational state.

**Agent state architecture target.** MemCube-inspired state lifecycle is operational: volatile in-process state, dedicated on-device persistent store, and distributed coordination layer are all managed under a unified agent state lifecycle policy. State isolation between agents is enforced at the OS level—cross-agent state reads require explicit capability grant. Checkpoint/restore is demonstrated for agent migration between compute nodes within a single rack.

**Research milestones.** First production-quality prototype of the full AI-Kernel Interface Contract on a Linux or Windows substrate. Empirical Circuit Breaker demonstration: at least three distinct failure scenarios (inference livelock, model weight corruption, catastrophically wrong policy decision) are injected and recovered automatically with the Circuit Breaker within a defined recovery time objective. Formal paper establishing morphism quality metrics as computable OS observables.

**TRL assessment.** TRL 2–4 (technology concept formulated to lab validated). This phase is beyond current prototypes; it requires integration of research results from multiple active programs (sched_ext scheduling, MemOS memory management, Circuit Breaker watchdog, CBTO ontology governance) into a coherent system.

**Exit criteria for Phase 2.** An Architecture B prototype runs the AI-native control plane with formal governance for at least 30 days under real agent workloads. The Circuit Breaker is demonstrated to detect and recover from each of the six failure modes in the taxonomy (Section 12.1) with correct transition to Conventional Fallback Mode and re-admission of the AI control plane after recovery. S_a and C_r are tracked continuously with less than 5% total monitoring overhead. At least one safety-critical scenario is demonstrated in mixed-criticality configuration (ARINC 653-style partition with AI advisory in separate partition and certified fallback in safety partition).

### 17.4 Phase 3: Heterogeneous Resource Fabric (2028–2032) [E]

**What is built.** The AI-OS extends beyond a single node to a distributed fabric spanning CPUs, NPUs, DPUs, GPUs, confidential-computing domains, and disaggregated CXL memory. Agents are no longer bound to a single node; the OS manages cross-node agent placement, migration, and state consistency. The AI control plane federates across nodes with consensus-based resource policy coordination. Mixed-criticality partitioning is extended to the rack level: safety-critical partitions on safety-certified hardware, AI control plane on accelerator-rich infrastructure.

**Formal elements extended.** Composition morphisms for distributed agents: when agent A delegates to agent B running on a different node, the composed morphism h_A ∘ h_B is computed and its quality assessed against the product of the individual morphism quality bounds. Cross-node state consistency is governed by a distributed consistency protocol with explicit convergence guarantees. TEE-protected agent state migration: agent state encrypted in an NVIDIA H100 or AMD SEV-SNP TEE on the source node is re-attested on the destination node before decryption and re-instantiation.

**Hardware targets.** NVIDIA NVL72 rack-scale GPU architecture with NVLink fabric enabling coherent memory access across 72 GPUs. Intel TDX Connect for secure CPU-to-GPU channels. CXL memory pooling enabling dynamic memory disaggregation across rack components. ARM CCA Realms for mobile and edge AI-OS deployments.

**Research milestones.** Multi-node agent migration with state consistency demonstrated across a 4-node testbed. Rack-scale TEE integration with verified state continuity across migration. Composition morphism quality bound proven to hold under realistic agent delegation patterns. First safety-critical certification attempt for a mixed-criticality AI-OS component using the monitor-based certification strategy (Section 16.3).

**TRL assessment.** TRL 1–3 (basic principles observed to proof-of-concept). Distributed AI orchestration (Kubernetes + LLM agents) exists at lower abstraction levels; the formal morphism-governed, security-preserving, safety-aware version is research.

**Exit criteria for Phase 3.** Multi-node agent migration is demonstrated with S_a maintained above 0.80 across the migration event and state consistency verified within 500ms of migration completion. Composition morphism quality does not degrade below 0.75 for agent delegation chains of depth 5 or greater. A mixed-criticality safety argument is reviewed and accepted by at least one domain certification authority (aviation, automotive, or defense) as a candidate path to certification (not full certification—a credible path).

### 17.5 Six Principal Recommendations [P]

The following recommendations are addressed to practitioners building AI-native platforms, researchers establishing the theoretical foundations, and program managers allocating investment between these two activities.

**Recommendation 1: Treat "AI-based OS" as a spectrum, not a binary label.** The taxonomy in this report identifies four architectures that differ in where AI sits, how AI is governed, and what formal properties the AI layer holds. Claiming to build an "AI OS" without specifying which point on this spectrum is a communication failure, not an architectural decision. Architects should be explicit: "We are building Architecture A with NPU acceleration" or "We are targeting Architecture B with morphism-based governance." Vague claims obscure tradeoffs and prevent meaningful evaluation.

**Recommendation 2: Build on existing substrates in the near term.** The ecosystem gravity argument (Section 5.3) applies with full force. Linux on server infrastructure and Windows on enterprise workstations have device drivers, filesystem implementations, security modules, and developer toolchains representing decades of engineering investment. seL4 has a machine-checked correctness proof. All of these represent value that a clean-sheet AI OS must replicate at significant cost. Architecture B preserves this value while enabling AI-native policy governance. The clean-sheet path (Architecture D) is appropriate for research contexts and AI-only greenfield workloads; it is not appropriate as the default path for production systems in 2026.

**Recommendation 3: Map AI families to OS responsibilities instead of asking which AI paradigm wins.** Table 5 (Section 6.2) establishes that different AI families are appropriate for different OS functions: neuro-symbolic systems for policy reasoning that must be auditable, large language models for natural language interfaces and code generation, reinforcement-learned policies for resource optimization with feedback, probabilistic graphical models for anomaly detection with calibrated uncertainty. No single AI paradigm can be the OS because no single AI paradigm excels at all of these functions. An AI-OS design that bets on one paradigm is fragile; one that composes paradigms through the formal interface contract is robust.

**Recommendation 4: Treat standards as layered—classical OS standards remain necessary; AI interoperability standards are emerging and not a replacement.** POSIX, AUTOSAR, ARINC 653, and DO-178C specify mechanisms (system calls, partitioning, certification) that AI-adjacent standards do not address. MCP, A2A, and the NIST AI Agent Standards Initiative specify AI interoperability mechanisms that OS standards do not address. Both layers are necessary. Practitioners who defer to only one layer—treating AI standards as sufficient, or treating classical OS standards as covering the AI layer—will produce systems with gaps. The AI-Kernel Interface Contract (Section 9) is precisely the specification of how these two layers connect.

**Recommendation 5: Design for heterogeneous hardware from the start.** In 2026, AI inference does not execute exclusively on the CPU. NPUs, GPUs, DPUs, and accelerator fabrics are first-class compute resources in every significant AI workload. An AI-OS that ignores NPU scheduling, GPU memory management, or DPU offload policies is designing for hardware that does not reflect the deployment environment. Phase 3 heterogeneous fabric requirements should be considered in Phase 1 and 2 design decisions—particularly the state management architecture (Section 10) and the security architecture (Section 11), which both need to account for non-CPU compute and disaggregated memory from the beginning.

**Recommendation 6: Put governance, evidence, and failure-mode analysis on equal footing with capability demonstrations.** The AI systems community has a demonstrated bias toward demonstrating capabilities and underweighting failure modes, governance mechanisms, and formal properties. For an AI-OS—a system that controls resource allocation for everything else running on the machine—this bias is dangerous. The Circuit Breaker is as important as the agent scheduler. The agent state isolation model is as important as the agent memory capacity. The morphism quality metrics are as important as the agent throughput metrics. A system that can schedule 1,000 concurrent agents but has no watchdog, no fallback, and no formal governance is a liability, not an asset. Investment in governance mechanisms should be tracked and reported alongside investment in capability.

### 17.6 Open Research Questions [E]

The following twelve questions define the research frontier for morphism-grounded AI operating systems as of early 2026. Each is stated precisely, with sufficient context to indicate why it is open and what resolving it would enable.

**Q1: Determinism boundary.** Which OS decisions must remain deterministic, and what is the formal criterion for placing a decision on the deterministic versus AI-optimizable side? The heuristic answer (interrupt handling must be deterministic; workload placement need not be) is not a formal criterion. A formal criterion would specify, for any OS function, whether non-deterministic policy can be introduced without violating the safety and liveness properties of the overall system. This criterion does not exist. Developing it would enable principled architecture decisions about which functions can be AI-governed.

**Q2: Interface contract standardization.** Can the AI-Kernel Interface Contract be standardized across implementations, analogously to how POSIX standardized the kernel-to-userspace boundary? A standard AI-Kernel contract would enable AI control plane components to be ported across OS substrates—an AI agent scheduler developed for a Linux substrate would run on a Windows substrate with the same formal properties. The challenge is that the contract must express enough semantics to be meaningful (not just naming conventions) while remaining implementable on diverse substrates. This is the open-systems problem for AI-OS, analogous to what POSIX solved for UNIX.

**Q3: Provenance and rollback granularity.** How should provenance, rollback, and attestation work for AI-driven actions that modify system state? What is the minimum granularity of rollback that a governance framework must support? An AI-driven resource allocation decision that persists agent state to disk and evicts another agent's context involves multiple state mutations across different storage substrates. Rolling back the allocation requires undoing all of these mutations atomically. Defining the transaction boundary and the audit granularity is an open systems problem with no established solution for AI-OS contexts. PROV-O provides a vocabulary for provenance; it does not specify the rollback protocol.

**Q4: Continual learning stability.** How can transfer learning and continual learning be exploited for OS policy adaptation without destabilizing the platform? An AI scheduler that learns from workload patterns can improve over time—but a policy that shifts as a result of learning can also produce unexpected behavior changes in systems that operators assumed were stable. Catastrophic forgetting in continual learning systems has been studied in general ML contexts; the OS-specific version of the problem—learning from system events without destabilizing the policies that govern the system generating those events—has not been formalized.

**Q5: Node versus fabric boundary.** What is the right boundary between a node OS and a distributed agent-control fabric? When does an AI-OS become a cluster scheduler, and when does a cluster scheduler become an AI-OS? Kubernetes with LLM-based workload placement policies shares architectural features with an AI-OS. Distributed AI-OS proposals share architectural features with cluster schedulers. Clarifying the boundary—which functions belong to the node OS and which to the fabric, and what the formal interface between them is—is necessary to prevent the "everything is an AI-OS" conflation that afflicts current discourse.

**Q6: Morphism metric standardization.** Can S_a and C_r (or equivalent morphism quality metrics) be standardized across AI-OS implementations to enable cross-platform comparison? In their current form, S_a and C_r are defined relative to a specific Wymore formalization of the kernel and AI control plane (Section 13). Different AI-OS implementations will formalize their system models differently, making the metrics non-comparable across implementations. Standardizing the metrics requires standardizing the system model formalism—a significant undertaking, analogous to standardizing OS performance benchmarks (SPEC) but for formal properties rather than throughput.

**Q7: Verification cost reduction.** What is the minimum formal verification investment for a credible AI-native control plane? Can AI-assisted proof generation (vericoding) reduce this investment to economically feasible levels? seL4's 200,000-line proof corpus for 10,000 lines of C establishes a rough upper bound on verification cost for a trusted kernel. An AI-native control plane is larger and more complex. If vericoding can reduce the proof-to-code ratio by an order of magnitude, Architecture C becomes broadly feasible; if vericoding can produce proofs for bounded AI policy modules, Strategy 2 (Section 16.3) becomes achievable. The current state of vericoding tools does not support this assessment; the empirical rate of improvement is an active research question.

**Q8: State persistence under confidential computing.** How does agent state persistence interact with confidential computing constraints? Can TEE-protected agent state survive migration across physical nodes? TEE-protected state is encrypted under a key that is bound to a specific physical hardware configuration (AMD SEV-SNP binds to the physical CPU; NVIDIA H100 TEE binds to specific GPU firmware). Migrating agent state across nodes requires either re-encrypting under the destination TEE's key (which requires secure key exchange under attestation) or establishing a distributed TEE spanning both nodes (rack-scale confidential computing, not yet generally available). The protocol for agent state migration with TEE continuity is an open systems security problem.

**Q9: Prompt injection as systemic vulnerability.** What governance structures prevent prompt injection from becoming a systemic OS vulnerability rather than an application-level nuisance? In Architecture A, prompt injection compromises an application. In Architecture B, prompt injection targeting the AI control plane could influence OS resource allocation decisions—effectively a privilege escalation vector. In Architecture D, prompt injection targeting the AI kernel could be an OS exploit. The transition from application-level to OS-level threat model requires OS-level mitigations: formal input validation at the AI-Kernel interface, prompt provenance tracking, and anomaly detection for unusual resource requests following unusual inputs. None of these mechanisms exist in production AI-OS systems.

**Q10: Mixed-criticality evolution.** How should mixed-criticality partitioning evolve as AI components become more capable and possibly certifiable? The mixed-criticality architecture (Section 16.2) is premised on the AI partition being non-certified and non-safety-critical. If Strategy 2 or Strategy 3 (Section 16.3) produces AI modules with formal proofs of bounded behavior, the partition architecture must evolve to allow certified AI components to interact with safety-critical partitions through verified channels. The certification authority requirements for such channels, and the formal properties required of the AI module proof, have not been defined.

**Q11: Energy-proportional AI.** Can an AI-native control plane achieve energy-proportional computing—where energy consumption scales with load—or does the overhead of AI inference inherently increase idle power consumption? AI control plane components (model weights, inference infrastructure) consume static memory and may consume periodic CPU cycles for monitoring and garbage collection even when the system is lightly loaded. The energy cost of AI governance may offset the efficiency gains from AI-optimized resource allocation. Empirical measurement of this tradeoff does not exist in the literature for Architecture B systems.

**Q12: Composition scaling.** Does morphism composition quality degrade gracefully with the number of composed agents, or is there a cliff beyond which governance becomes intractable? Section 13.5 establishes that composition morphisms must be monitored when agent A delegates to agent B. For delegation chains of depth n, the composed morphism is h_1 ∘ h_2 ∘ … ∘ h_n. If morphism quality degrades multiplicatively (each composition multiplies quality by a factor less than 1), then quality falls exponentially in chain depth, and governance of deeply nested agent compositions is infeasible. If quality degrades sublinearly, governance scales. The actual degradation function depends on the specific system, but the theoretical relationship has not been established.

---

## References (Part V)

[1] T. Kalliamvakou, "Research: Quantifying GitHub Copilot's impact in the enterprise with Accenture," GitHub Blog, Mar. 2024.

[2] Microsoft, "Windows AI Foundry," Microsoft Developer Documentation, 2025. [Online]. Available: https://learn.microsoft.com/en-us/windows/ai/

[3] Apple Inc., "Introducing Apple Intelligence," Apple Developer Documentation, WWDC 2025.

[4] Google, "AICore and Gemini Nano for Android," Android Developers, 2025.

[5] Z. Xu et al., "AgentCgroup: Cgroup-Aligned Resource Management for LLM Agents," arXiv:2602.09345, Feb. 2026.

[6] M. Shi et al., "AIOS: LLM Agent Operating System," in *Proc. 1st Conf. on Language Modeling (COLM)*, Philadelphia, PA, Oct. 2024.

[7] MemOS Project, "MemOS: Memory Operating System for LLM Agents," GitHub Repository, 2025.

[8] Y. Xu et al., "Everything is Context: A Filesystem Abstraction for LLM Agent Memory," arXiv:2512.05470, Dec. 2025.

[9] G. Klein et al., "seL4: Formal Verification of an OS Kernel," in *Proc. ACM SOSP*, Big Sky, MT, Oct. 2009, pp. 207–220.

[10] T. Murray et al., "seL4: From General Purpose to a Proof of Information Flow Enforcement," in *Proc. IEEE S&P*, San Francisco, CA, May 2013, pp. 415–429.

[11] RTCA, *DO-178C: Software Considerations in Airborne Systems and Equipment Certification*, Radio Technical Commission for Aeronautics, 2011.

[12] International Organization for Standardization, *ISO 26262: Road Vehicles — Functional Safety*, 2nd ed., Geneva, Switzerland, 2018.

[13] International Electrotechnical Commission, *IEC 61508: Functional Safety of E/E/PE Safety-Related Systems*, Geneva, Switzerland, 2010.

[14] ISO/SAE, *ISO/DPAS 8800: Road Vehicles — Safety and Artificial Intelligence*, Draft Publicly Available Specification, 2024.

[15] ARINC, *ARINC 653: Avionics Application Software Standard Interface*, Airlines Electronic Engineering Committee, 2015.

[16] M. Zuepke et al., "AUTOBEST: A United AUTOSAR-OS and ARINC 653 Kernel," in *Proc. IEEE RTAS*, Vienna, Austria, Apr. 2016, pp. 143–154.

[17] J. Rushby, "Design and Verification of Secure Systems," in *Proc. ACM SOSP*, Pacific Grove, CA, Dec. 1981, pp. 12–21.

[18] NASA, *Technology Readiness Level Definitions*, NASA Office of the Chief Technologist, 2012.

[19] A. Rashid et al., "Vericoding: LLM-Assisted Generation of Formally Verified Programs," arXiv:2501.xxxxx, 2025.

[20] P. Jiang et al., "Selene: Automating seL4 Proof Engineering with Large Language Models," arXiv:2502.xxxxx, 2025.

[21] DeepSeek-AI, "DeepSeek-Prover-V2: Advancing Formal Mathematics Reasoning via Reinforcement Learning for Subgoal Decomposition," arXiv:2504.21801, 2025.

[22] DARPA, *DARPA-PA-25-07-02: Compositional Learning-And-Reasoning (CLARA)*, Defense Advanced Research Projects Agency, Nov. 2025.

[23] Microsoft, "Hyperlight Wasm: OS-Free WebAssembly Execution," Microsoft Open Source Blog, Mar. 2025.

[24] N. Forsgren et al., "The SPACE of Developer Productivity," *Queue*, vol. 19, no. 1, pp. 20–48, Jan./Feb. 2021.

[25] NVIDIA, "NVIDIA Hopper Architecture: Confidential Computing," NVIDIA Technical Brief, 2023.

[26] P. Wach and R. Sandman, "Toward a Library of Isomorphic Patterns for Systems Engineering," in *Proc. CSER 2026*, Mar. 2026.

[27] W. Wymore, *Model-Based Systems Engineering*, CRC Press, Boca Raton, FL, 1993.

[28] P. Wach, "AI Circuit Breaker Trust Ontology (CBTO): Ontology-Grounded Trust Metrology for AI Systems," Technical Report v4.0, University of Arizona, Feb. 2026.

[29] SEAgent Project, "MAC-Based Multi-Agent Security Framework for LLM Systems," GitHub Repository, 2025.

[30] B. Chen et al., "PunkGo: Tamper-Evident Audit Logs as a Kernel Primitive," arXiv:2503.xxxxx, 2025.
