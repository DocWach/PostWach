# Part I: Foundations — What Exists Today

---

## 1. Introduction and Scope

### 1.1 What People Mean When They Say "AI Operating System" [L]

The phrase "AI operating system" has spread rapidly through the technology press, investment community, and research literature, accumulating meanings as it travels. Smartphones are marketed as platforms for AI operating systems. Cloud orchestration services are branded as intelligent operating layers. Agent frameworks call themselves the operating systems of the agentic era. The phrase is now so loaded that, without clarification, it communicates almost nothing.

This is a metaphor problem, and it deserves a serious answer.

The simplest way to ground the discussion is to start with what an operating system actually is, and then ask where, precisely, artificial intelligence enters the picture. Consider a skyscraper. A modern high-rise has a building management system — software that was installed when the building was constructed, runs around the clock, and provides services that tenants use without needing to know anything about the underlying engineering: electricity delivered to every outlet, water maintained at pressure, elevators dispatched on demand, access control at every door, HVAC adjusted zone by zone. Tenants write their own work without worrying about whether the power grid can handle their computers. The building management system mediates between the raw infrastructure and the activity that happens inside.

An operating system does exactly this for computing hardware. It starts first, stays in control, and provides services — process scheduling, memory allocation, file storage, network access, security enforcement — that applications consume without touching the hardware directly. The system call is the door through which every application enters the building, and the kernel is the building management office that decides whether to grant access.

When people say "AI operating system," they are typically describing one of three fundamentally different ideas:

**Type A** is adding smart thermostats and automated lighting to an existing building: intelligence is layered into individual services while the building management system itself remains unchanged. Apple Intelligence and the Google Gemini Nano integration in Android are current examples. The kernel is untouched; AI runs as a privileged system service.

**Type B** is replacing the building management system with an AI-driven one while keeping the building structure intact. The walls, floors, and elevators are the same, but the control logic — scheduling, resource allocation, access policy — is now governed by an AI-native layer sitting above a conventional OS kernel. This is the most credible engineering path for the next five years.

**Type C** is designing an entirely new building in which the AI is the structure: agents are first-class entities equivalent to processes, context is a managed resource equivalent to memory, and the kernel's job is defined around the needs of AI workloads rather than adapted to them. Research systems such as AIOS [1] and MemOS [2] explore this frontier.

These three types are not interchangeable, and conflating them produces confusion about what has been built, what remains theoretical, and what the research community should actually be working on. Section 7 returns to them with precise definitions and industry evidence. For now, the important point is that all three are coherent engineering concepts — they simply differ in where they situate intelligence relative to the trusted substrate.

---

### 1.2 The Two Orthogonal Research Programs [P/E]

The most important structural distinction in the AI-OS literature is one that most survey papers fail to draw clearly: the difference between **"AI for OS"** and **"OS for AI."** These are orthogonal research programs. Conflating them produces category errors in requirements, metrics, and threat models.

**"AI for OS"** treats AI as an implementation technique for classical OS functions. The operating system is still the operating system; AI improves how it does its job. Concrete examples include: ML-based scheduling patches for the Linux kernel that learn workload patterns and adjust CPU time allocation [3]; AI-driven memory prefetchers that predict access sequences to reduce cache miss rates [4]; and eBPF programs combined with machine learning models for adaptive networking, where the kernel's data plane is tuned by a learning agent operating in user space [5]. In all of these cases, the fundamental OS abstractions — processes, virtual memory, system calls — remain unchanged. AI is a better algorithm for decisions that the OS was already making.

**"OS for AI"** treats AI agents as the primary workload and asks how the OS should manage them. Rather than improving the kernel's internal mechanisms, this program adds new abstractions: agent scheduling (how do I give CPU time to an LLM reasoning loop?), context management (how do I store and retrieve the episodic memory of a long-running agent?), tool mediation (how do I safely expose filesystem and network access to an agent that generates its own tool calls?). Systems such as AIOS v5 (Mei et al., COLM 2025) [1], MemOS [2], and the claude-flow orchestration framework [6] are representative. The agents are the workload; the OS manages them as it has always managed processes — but the workload properties are radically different.

These programs have different latency requirements, different success metrics, and different threat models. Mixing them in a single paper without labeling which is being addressed produces claims that are simultaneously true and irrelevant to the reader's actual problem. Table 1 makes the comparison explicit.

**Table 1: "AI for OS" vs. "OS for AI" — Side-by-Side Comparison**

| Dimension | "AI for OS" | "OS for AI" |
|---|---|---|
| Primary question | How can AI improve kernel functions? | How should the OS manage AI agents? |
| Latency requirement | Microsecond (scheduling decisions) | Millisecond-second (inference latency) |
| Threat model | Adversarial workloads exploit learned scheduler | Prompt injection escalates agent privileges |
| Success metric | Resource utilization, tail latency, power efficiency | Agent throughput, context quality, task completion |
| Certification challenge | Proving learned policy meets safety guarantees | Proving agent behavior stays within policy bounds |
| Existing insertion point | eBPF, sched_ext, cgroups v2 | MCP, A2A, agent frameworks |

This report covers both programs. At every point where the discussion shifts from one to the other, the text flags the transition explicitly. The formal architecture developed in Parts III and IV — the interface contract, the agent state model, the Circuit Breaker watchdog — primarily addresses the "OS for AI" program, which is further from engineering maturity and most in need of rigorous treatment.

---

### 1.3 Scope and Method

This report synthesizes the current state of both research programs, constructs a defensible engineering architecture for the near- and medium-term, and provides formal foundations that distinguish this work from descriptive surveys.

**Sources** draw from four categories: primary systems research published on arXiv and in ACM/IEEE venues between 2023 and early 2026; industry documentation from Microsoft, Google, Apple, NVIDIA, and Intel; standards bodies including POSIX, AUTOSAR, ARINC, NIST, and the Linux Foundation; and formal methods literature spanning the Wymore five-tuple formalism, OWL 2 DL ontology design, and SHACL constraint specification. Where the literature is sparse or absent — particularly on agent state management and the formal interface contract — this report synthesizes a position from first principles and labels it as such.

**Audience layering** is explicit throughout. Section and subsection headings carry audience markers: [L] for content accessible to any technically literate reader, [P] for content directed at practitioners building AI-native platforms, and [E] for content that assumes familiarity with operating systems internals, formal methods, or AI systems research. A reader with a labrador retriever's patience for jargon can read the [L] sections and the callout boxes and get the substance. A systems architect can add the [P] sections. A researcher can read everything.

---

### 1.4 What This Report Adds Beyond Existing Surveys

Several useful surveys of AI-OS concepts have appeared in the 2024-2026 period [7, 8]. This report contributes four things that existing surveys do not provide.

**First**, a formal interface contract using Wymore five-tuple morphisms. The idea that an AI control plane must have a specified contract with the kernel it governs is widely stated and never designed. Section 9 specifies that contract in terms of downward APIs (from AI control plane to kernel), upward APIs (from kernel to AI control plane), and the policy-mechanism boundary that determines which side owns each decision. Sections 13-14 then ground the contract in morphism theory, enabling measurable quality metrics for the interface at runtime.

**Second**, a runtime governance mechanism. The Circuit Breaker watchdog (Section 13) monitors two orthogonal morphism quality metrics — structural quality S_a and behavioral quality C_r — and trips to a deterministic conventional fallback when either metric degrades beyond a defined threshold. This is novel: prior work either ignores the failure case or handles it with the vague phrase "safe fallbacks." The watchdog is simpler than what it monitors by construction, which is the key property that makes it trustworthy.

**Third**, a complete agent state architecture. Section 10 provides the first systematic treatment of agent state as an OS resource management problem: a taxonomy of state categories (execution context, episodic memory, semantic memory, goal state, resource bindings), storage substrate options for each, ownership and isolation semantics, and consistency model requirements. This is, in the authors' assessment, the hardest new OS problem introduced by AI agents, and it receives correspondingly serious treatment.

**Fourth**, empirical grounding from the 2025-2026 literature explosion. The past eighteen months have produced a cluster of concrete systems — AgentCgroup [9], MemOS [2], PunkGo [10], SEAgent [11], AIOS v5 [1] — that provide design evidence rather than conceptual arguments. This report integrates those results systematically rather than treating them as isolated demonstrations.

---

## 2. What Is an Operating System?

### 2.1 The Beginner Definition [L]

An operating system is the software that runs a computer underneath everything else. It starts first, before any application, and it stays in control of the hardware for as long as the machine is on. Its job is to let other software use the machine without each piece of software having to solve, independently, the problems of sharing the processor, managing memory, talking to storage devices, or enforcing that one program cannot read or destroy another program's data.

The National Institute of Standards and Technology describes an OS as "a master control application" and "software that manages hardware and software resources while providing common services to programs" [12]. The OSTEP textbook — the standard reference for operating systems education — frames the OS mission around three concepts [13]: **virtualization** (transforming raw hardware into useful abstractions, so that each program sees what looks like a private processor and private memory even though it shares both with many others), **concurrency** (arbitrating overlapping work so that multiple activities proceed simultaneously without corrupting each other), and **persistence** (ensuring that data survives beyond the lifetime of any individual program or the power cycle of the machine).

Returning to the skyscraper analogy: the operating system is the building management system that was installed when the building was constructed. It runs continuously, invisible to most tenants, providing electricity, water, elevator access, and climate control as services that tenants use without knowing how the infrastructure delivers them. A tenant writing a report does not manage voltage regulators. A developer writing an application does not manage CPU registers. The OS absorbs that complexity and offers a cleaner, safer interface in its place.

---

### 2.2 The Systems-Level Definition [P]

At the level of systems engineering, an OS is defined not just by what it does but by where it sits and when it takes control. The modern boot sequence illustrates the architecture precisely. The UEFI firmware initializes hardware and provides boot services; the OS loader calls `ExitBootServices()`, at which point the firmware relinquishes control and the kernel assumes it [14]. From that moment, the kernel is the most privileged software on the machine. Everything else — drivers, system services, applications — executes with less privilege and accesses hardware only by asking the kernel.

The system call is the fundamental boundary. The Linux man-pages define it as "the fundamental interface between an application and the Linux kernel" [15]: a controlled entry point through which user-space code requests kernel services. The kernel validates the request, performs the privileged operation, and returns a result. The calling program never touches the hardware directly.

**Table 2: Classical OS Responsibilities**

| Core OS Responsibility | Plain-Language Meaning | Canonical Mechanisms |
|---|---|---|
| Boot and control transfer | Take over from firmware and establish a trusted execution baseline | Loader, boot services handoff, kernel entry point |
| Execution management | Run multiple programs safely and productively | Processes, threads, context switches, system calls |
| Resource management | Share finite resources such as CPU time and memory | Schedulers, virtual memory, page allocation, reclaim |
| Persistence and I/O | Store data durably and mediate device access | VFS, filesystems, drivers, block and network stacks |
| Protection and policy | Prevent one activity from breaking or stealing from another | Privilege rings, access control lists, encryption, isolation |

These five responsibilities are not independent. Resource management and protection are deeply intertwined: a memory allocator that allows one process to read another's pages has failed at both. The boot and control transfer responsibility establishes the trust anchor that makes all subsequent protection claims meaningful. A system that provides persistence but lacks protection may be a useful tool but is not a trustworthy OS.

---

### 2.3 The Boundary Test [E]

Not every piece of infrastructure software is an operating system. Kubernetes, container runtimes, browser engines, and agent orchestration frameworks all perform OS-like functions — scheduling, resource management, isolation, namespace management — without satisfying the full definition. The distinction matters for this report because the term "AI operating system" is routinely applied to systems that are OS-adjacent without meeting the OS definition, and the engineering consequences of that gap are significant.

A system is closest to a classical operating system when it satisfies three tests simultaneously:

1. **Trusted boot path.** It is on the trusted path from firmware initialization to runtime. It takes control through a documented, verifiable mechanism (e.g., `ExitBootServices()` or an equivalent trusted boot handoff) and is in the trusted computing base for subsequent software.

2. **Hardware mediation.** It mediates access to hardware or virtualized hardware. Applications cannot bypass it to reach the instruction set, memory bus, or device registers. This is what makes the OS the single source of truth for resource state.

3. **Stable privileged interfaces.** It exposes privileged services to applications through stable interfaces that applications depend on. The system call API, the ABI for executable formats, the device model — these are contracts that OS users build upon and that the OS is obligated to maintain.

If a system fails any of these tests, it occupies a different engineering category. Kubernetes manages container scheduling and resource limits, but it does not own the boot path and does not mediate hardware — it delegates to the host OS for both. A browser runtime provides sandboxed execution and persistent storage, but it runs above a conventional OS and cannot enforce protection without the OS's cooperation. Agent orchestration frameworks are further still from the OS definition: they manage agent lifecycles and routing logic, but they have no privileged access to hardware and no trusted position in the boot chain.

This does not make those systems unimportant. It does mean that their security and resource management guarantees are derived from, rather than equivalent to, OS-level guarantees. An agent framework that claims OS-level isolation without kernel backing is making a claim it cannot keep.

As a formal definition candidate, an OS can be described as a triple (H, K, I) where:
- H is a hardware abstraction layer providing a uniform interface to physical or virtualized hardware resources;
- K is a kernel — trusted code executing with elevated privilege, in the trusted computing base, reachable through a verified boot path;
- I is an interface contract to user space specifying the system call API, ABI, executable format expectations, and device model.

A system that provides (H, K, I) in its full form is an OS. A system that provides only I — an interface without privileged hardware mediation — is middleware. A system that provides only H — hardware abstraction without user-space contracts — is firmware or a hypervisor. The distinction is not pedantic; it determines what security guarantees can be derived from the system and what must be imported from elsewhere.

---

## 3. OS Taxonomy: Categories, Architecture, and Standards

### 3.1 By Purpose [P]

Operating systems are not a homogeneous category. They differ by workload domain, certification requirements, real-time constraints, and security posture. Understanding this taxonomy is essential for AI-OS design because the right architecture depends entirely on where in this space the target system sits.

**General-purpose operating systems** — Linux, Windows, macOS — are designed for heterogeneous workloads on commodity hardware. They conform to POSIX.1-2024 [16] and the Single UNIX Specification, providing a stable interface layer that application software can depend on across hardware generations. Their schedulers and memory managers are tuned for throughput and interactivity rather than worst-case latency. For AI-OS purposes, general-purpose OS kernels are the most common substrate for "OS for AI" research, and Linux in particular is the dominant platform for AI infrastructure.

**Mobile operating systems** — Android, iOS — run on ARM SoCs with integrated NPUs, power-managed displays, sensor arrays, and cellular radios. Their ABI regimes are tightly controlled (Android's Bionic libc, iOS's Darwin/XNU with sandboxed app model), and application sandboxing is more aggressive than in desktop general-purpose OSes. Both platforms have deployed Type A AI-OS features: on-device inference for camera scene recognition, voice processing, and now foundation model integration (Apple Intelligence, Google Gemini Nano via AICore).

**Embedded and real-time operating systems** — FreeRTOS, Zephyr, VxWorks — target constrained hardware with deterministic latency requirements. They provide task scheduling with bounded worst-case execution time, interrupt latency guarantees, and minimal memory footprint. AI on embedded platforms is a rapidly growing area (TinyML, edge inference), but the AI-OS architecture question in this space is dominated by the "AI for OS" program: can AI improve power management, thermal control, or sensor fusion in real-time without violating timing guarantees?

**Safety-critical operating systems** — avionics partition executives, automotive HPCS kernels — operate under formal certification requirements. ARINC 653 [17] specifies temporal and spatial partitioning for avionics; AUTOSAR Adaptive [18] provides a POSIX-compatible platform for automotive high-performance computing. These systems must demonstrate freedom from interference: a failure in one partition must not propagate to another. This is the category where AI-OS integration faces the hardest certification challenges, discussed in Section 16.

**Microkernel and high-assurance operating systems** — MINIX 3, seL4 — trade compatibility and performance for verifiability. The seL4 microkernel [19] carries a machine-checked formal proof of functional correctness relative to its specification, absence of undefined behavior, and enforced capability-based access control. It took approximately 20 person-years to produce for roughly 10,000 lines of C. For AI-OS purposes, a verified microkernel substrate provides the strongest possible trust anchor — but the integration cost is correspondingly high.

**Unikernels** — Unikraft [20], MirageOS [21] — represent a distinct architectural philosophy: a single application is compiled together with exactly the OS components it needs into a single kernel image that boots in a virtual machine. There is no multi-tenancy, no shell, no user-space / kernel-space separation in the classical sense. The result is minimal attack surface, fast cold starts (10-50 ms for Unikraft), and high VM density (10,000-100,000 VMs per server in cloud deployments). Unikraft raised $6 million in October 2025 specifically targeting AI cloud workloads [22], a signal that the unikernel model is being evaluated for disaggregated AI inference. For AI-OS purposes, unikernels are a compelling substrate for stateless agent execution: each agent invocation is a fresh VM, isolation is total, and cold start latency is acceptable for tasks measured in seconds rather than microseconds.

**Capability-based operating systems** — Fuchsia/Zircon [23] — implement a zero-default-privilege model in which processes begin with no capabilities and must receive explicit grants to access resources. Every handle is a capability token; there is no ambient authority from username or group membership. Fuchsia shipped its stable F27 release in July 2025, deployed on Google Nest devices, marking the first production deployment of a capability-based OS at consumer scale. For AI-OS purposes, the Zircon object model maps naturally to agent tool invocation: an agent that wants to write a file must hold a capability for that file, not merely run as a user with write permission.

**Distributed control planes** — Kubernetes [24], cloud orchestration layers — perform OS-like functions (scheduling, resource management, namespace isolation, service discovery) across clusters of machines. They do not satisfy the OS triple (H, K, I): they have no trusted boot path and no direct hardware mediation. They are OS-adjacent systems that manage a fleet of OS instances rather than hardware directly. For AI-OS purposes, they are the current deployment substrate for most production multi-agent systems and a critical integration point for "OS for AI" architectures.

**Table 3: OS Taxonomy by Purpose**

| Category | Representative Systems | Standards | Key Constraint | AI-OS Relevance |
|---|---|---|---|---|
| General-purpose | Linux, Windows, macOS | POSIX.1-2024, SUS | Broad compatibility | Primary research substrate |
| Mobile | Android, iOS | Bionic ABI, Darwin | Power, sandboxing | Type A deployments live here |
| Embedded/RTOS | FreeRTOS, Zephyr, VxWorks | Vendor/project-specific | Deterministic latency | AI-for-OS in power/thermal |
| Safety-critical | ARINC 653 executives, AUTOSAR Adaptive | DO-178C, ISO 26262 | Certification | Hardest certification challenge |
| Microkernel/high-assurance | seL4, MINIX 3 | Project-specific, proof ecosystems | Verification cost | Strongest trust anchor |
| Unikernel | Unikraft, MirageOS | Project-specific | No multi-tenancy | Stateless agent execution |
| Capability-based | Fuchsia/Zircon | Project-specific | Integration cost | Maps to agent tool model |
| Distributed control plane | Kubernetes, cloud orchestration | Container OCI | No boot path ownership | Current multi-agent substrate |

---

### 3.2 By Kernel Architecture [E]

The kernel architecture determines how OS responsibilities are allocated between privileged and unprivileged code, and the tradeoffs between performance, security, and verifiability.

**Monolithic kernels** — Linux, BSD — place all OS services (scheduler, memory manager, filesystem, device drivers, network stack) in a single address space executing at kernel privilege. This maximizes performance through direct function calls between subsystems and minimizes context switching overhead. The cost is that a bug anywhere in the kernel can compromise the entire system. Linux's security record reflects this: a vulnerability in a device driver is a kernel vulnerability. For AI-OS purposes, Linux's monolithic architecture is a liability for the trust model but an asset for performance and ecosystem access.

**Microkernels** — seL4, MINIX 3 — run only the minimal required services at kernel privilege (inter-process communication, scheduling, memory management) and push everything else into isolated user-space servers. A compromised file server cannot corrupt the network stack; a failed device driver can be restarted without rebooting. seL4's formal proof of functional correctness is only possible because the kernel is small enough to be verified — a monolithic kernel of comparable capability would be orders of magnitude larger than any current verification technology can handle. For AI-OS purposes, a microkernel substrate enables stronger isolation between the AI control plane and the trusted kernel core, at the cost of IPC overhead and integration difficulty.

**Hybrid kernels** — Windows NT kernel, macOS XNU — blend monolithic and microkernel designs pragmatically. XNU combines a Mach microkernel core with BSD kernel extensions in the same address space, sacrificing strict isolation for compatibility and performance. Windows NT's executive runs device drivers in kernel mode while keeping the hardware abstraction layer (HAL) as a distinct component. Both approaches reflect the lesson that pure microkernel designs have historically struggled to compete with monolithic kernels on performance at scale.

**Unikernels** make a different tradeoff: they collapse the user-space / kernel-space boundary entirely for the case of a single application. The application and its OS libraries compile into a single address space that boots as a virtual machine under a hypervisor. The hypervisor provides the isolation that the kernel would otherwise provide. The result is a minimal attack surface and fast cold starts, but no multi-tenancy within a single VM instance.

**The library OS and exokernel lineage** — Exokernel [25], Drawbridge [26] — pursued the idea that the kernel should expose hardware resources as directly as possible and let application-level libraries implement OS abstractions. WebAssembly System Interface (WASI) [27] and runtime environments built on it (Hyperlight Wasm, Wassette) are a contemporary descendant of this lineage: WASM provides a portable, sandboxed execution environment in which OS interfaces are defined by the WASI specification rather than by a local kernel. For AI-OS purposes, WASM/WASI is a plausible substrate for portable agent execution: a WASM-compiled agent can run on any conforming runtime, with capability-controlled access to OS interfaces.

**The Fuchsia/Zircon object model** — Google's Fuchsia OS uses the Zircon microkernel with a capability-based object model as its foundational security architecture. Every kernel resource is an object, and every handle to an object is a capability token specifying what operations the holder may perform. Processes start with no capabilities; they receive handles through explicit grants from a parent or through the component framework's capability routing. This zero-default-privilege architecture maps naturally to the principle of least authority for AI agents: an agent receives exactly the capabilities it needs for its task and no more.

---

### 3.3 By Standards Regime [E]

Standards define the interface contracts that users depend on and that OS vendors are obligated to maintain. Understanding the standards landscape is essential for AI-OS design because new standards define where novel interfaces will be stabilized, and the absence of standards identifies where the research community has work to do.

**Classical OS standards** include POSIX.1-2024 [16] (process management, filesystem, signals, sockets, threads), the Single UNIX Specification (SUS), AUTOSAR Adaptive Platform [18] (POSIX-based platform for automotive HPC), and ARINC 653 [17] (temporal and spatial partitioning for avionics). These standards provide the stable interface contracts that make decades of application software portable across hardware generations. Any AI-OS design that discards POSIX compatibility discards the application software ecosystem that depends on it.

**Safety certification standards** — DO-178C [28] for avionics software, ISO 26262 [29] for automotive functional safety, IEC 61508 [30] for industrial safety systems — are not interface standards but process and evidence standards. They specify how software must be developed, analyzed, and tested to achieve a given safety integrity level (SIL) or development assurance level (DAL). Neural networks violate the structural coverage criteria (Modified Condition/Decision Coverage, MC/DC) that these standards mandate for high-assurance software, and there is currently no published method to certify a learned model to DO-178C DAL A or ISO 26262 ASIL D. ISO/DPAS 8800 [31], addressing AI safety for automotive, was in progress as of early 2026 but not yet ratified.

**Emerging AI-adjacent standards** define the interfaces through which AI agents interact with tools and with each other — the layer at which "OS for AI" architectures must plug in:

- The **Model Context Protocol (MCP)** [32], released by Anthropic in November 2024 and reaching its 2025 specification with over 97 million monthly SDK downloads, defines a standardized JSON-RPC 2.0 interface between AI models and external tools, data sources, and services. MCP is the closest thing the AI agent ecosystem currently has to a system call interface: it specifies how an agent requests a file read, a web fetch, or a database query, and how the provider responds.

- The **Agent2Agent Protocol (A2A)** [33], contributed to the Linux Foundation in June 2025, defines how autonomous agents discover each other, negotiate capabilities, and exchange task delegation. A2A addresses agent-to-agent communication, the layer above tool invocation.

- The **NIST AI Agent Standards Initiative**, launched in February 2026 [34], published a Request for Information on agent security and began coordinating with standards bodies on agent identity, capability assertion, and audit logging requirements.

The critical gap in this landscape is the absence of a POSIX equivalent for AI-OS interfaces. There is no standard that specifies: how an agent registers with an OS-level scheduler, what resource hints it may express, how its context is managed under memory pressure, or what audit records the OS must maintain of its actions. This gap is not merely inconvenient; it means that current "OS for AI" systems are building on interfaces that have no interoperability guarantees. Closing this gap is one of the open research questions that this report identifies in Section 17.

---

## 4. Hardware Substrate and Platform Evolution

### 4.1 The Hardware Spectrum [P]

AI workloads do not execute on a single type of hardware. They span a spectrum from milliwatt microcontrollers running TinyML inference to rack-scale supercomputers running multi-billion-parameter foundation models. An AI-OS architecture that assumes a particular hardware form factor will fail to generalize. Table 4 captures the relevant spectrum.

**Table 4: Hardware Spectrum for AI-OS Deployment**

| Platform Class | Representative Hardware | AI Capability | Memory | Key OS Constraint |
|---|---|---|---|---|
| MCU / tiny embedded | STM32, ESP32, RP2040 | TinyML, < 1M parameters | KB-scale RAM | No MMU, bare-metal or RTOS only |
| Mobile / edge SoC | Apple A18 Pro, Qualcomm Snapdragon X Elite, MediaTek Dimensity 9400 | On-device LLM (1-7B parameters) | 8-32 GB LPDDR | Power budget, thermal, NPU scheduling |
| Desktop / laptop | Intel Core Ultra 200, AMD Ryzen AI 300 | Local inference, coding assistants | 32-128 GB DDR5 | NPU + iGPU coordination, memory bandwidth |
| Server / cloud | NVIDIA H100 SXM5, AMD MI300X, Intel Gaudi 3 | Foundation model training/inference | 80-192 GB HBM per GPU | Multi-GPU coordination, NVLink/InfiniBand |
| Accelerator-rich / disaggregated | NVIDIA GB200 NVL72, CXL memory pooling, DPU-augmented | Rack-scale LLM serving | TB-scale disaggregated | Placement, locality, attestation, thermal |

The important engineering observation is that the same AI application may need to execute across multiple rows of this table simultaneously — a multi-agent pipeline might run orchestration logic on a server, invoke specialized agents on edge devices, and store retrieved context in a disaggregated memory pool. The OS that manages this pipeline cannot be designed for any single row; it must reason about placement, data locality, and failure semantics across the full stack.

---

### 4.2 The Heterogeneity Inflection [E]

The hardware landscape has undergone a qualitative shift in the 2024-2026 period that changes the OS design problem significantly. Three developments are driving the inflection.

**Neural Processing Units at scale.** Microsoft's Copilot+ PC certification program mandates 40 TOPS (Tera Operations Per Second) of NPU capacity in Phase 1 devices (2024) and 80-100 TOPS in Phase 2 (2025-2026) [35]. Apple Silicon integrates a dedicated Neural Engine that the OS explicitly manages as a hardware resource, scheduling neural network inference tasks to the Neural Engine rather than the CPU or GPU. These NPUs are not general-purpose processors; they execute matrix operations and convolutions efficiently but cannot run arbitrary code. The OS must maintain a new kind of resource abstraction: not a CPU core with a scheduler, but an accelerator with a model loader, a workload queue, and power management hooks.

**Data Processing Units.** NVIDIA BlueField DPUs [36] offload networking, storage I/O, and security processing from the CPU to a dedicated ARM-based processor with programmable data path hardware. The DPU executes software-defined networking pipelines, NVMe-oF storage operations, and TLS encryption without consuming CPU cycles. For AI-OS purposes, DPUs represent a programmable infrastructure layer that can enforce resource accounting, network policy, and storage access control at line rate — capabilities that complement an AI control plane managing agent traffic at a higher level of abstraction.

**CXL 2.0 memory pooling.** The Compute Express Link standard at version 2.0 [37] enables memory disaggregation: physical memory devices can be attached to a CXL switch fabric and dynamically allocated to multiple hosts. A host OS can expand its effective memory capacity by requesting memory from the pool, or release it when demand falls. For AI agents with large context windows and episodic memory stores, CXL disaggregation is significant: the working set of a long-running agent may exceed local DRAM capacity but fit comfortably in a pool that can be leased on demand. The OS must manage CXL-attached memory with attention to latency (CXL adds ~100ns of access latency relative to local DDR) and to the ownership semantics of memory that may be reclaimed.

**Confidential computing hardware.** The past three years have seen rapid maturation of hardware-enforced confidential computing, driven by multi-party AI training, regulated inference, and zero-trust infrastructure requirements:

- **AMD SEV-SNP** (Secure Encrypted Virtualization-Secure Nested Paging) [38] encrypts the memory of virtual machines and provides hardware-rooted attestation that verifiable reports of the VM's configuration can be generated and verified by remote parties. An AI model loaded into a SEV-SNP protected VM cannot be read by the hypervisor or host OS.

- **Intel TDX** (Trust Domain Extensions) [39] provides equivalent hardware-enforced VM isolation using a CPU-integrated Trust Domain Manager. TDX VMs (Trust Domains) operate with encrypted memory that is inaccessible to the host software stack, and they can generate signed attestation reports for remote verification.

- **ARM Confidential Compute Architecture (CCA)** [40] introduces a fourth privilege level (Realm) in addition to the existing Secure/Non-Secure/Hypervisor levels. Realm VMs run in hardware-isolated memory protected from both the Normal World OS and the Secure World firmware.

- **NVIDIA H100 GPU TEE** [41] is the first GPU-resident trusted execution environment at production scale. The H100 introduces a hardware root of trust for the GPU, encrypts GPU memory, and can generate attestation reports for AI model inference workloads. The overhead for typical LLM inference is reported at less than 5% — an acceptable cost for regulated or multi-party deployments.

- **Intel TDX Connect** [42] enables secure communication channels between a CPU Trust Domain and an NVIDIA H100 GPU TEE, so that data passed between CPU-resident orchestration logic and GPU-resident inference does not traverse an unprotected bus.

- **NVIDIA Vera Rubin NVL72** [43], announced at GTC 2025, extends the TEE concept to rack scale: the trusted execution environment spans an entire AI compute rack of 72 GPUs interconnected by NVLink 6, with the hardware root of trust covering the full rack-scale compute fabric. This represents the frontier of confidential AI computing: workloads that require the isolation guarantees of a TEE but the compute capacity of a full rack.

The implication for OS design is direct: the hardware substrate for AI workloads now includes cryptographically isolated execution environments at multiple granularities — VM, GPU, and rack. An OS that does not reason about attestation, about which workloads run in which isolation tier, and about the performance characteristics of crossing those isolation boundaries cannot manage a modern confidential AI compute environment.

---

### 4.3 What This Means for AI-OS Design [E]

The heterogeneity inflection produces a design requirement that classical OS theory does not directly address: **intelligence will execute across CPUs, NPUs, GPUs, DPUs, and secure enclaves, not "on the CPU."** A scheduler that models workload as a sequence of CPU time slices misses the fundamental structure of AI inference, which may involve CPU-resident orchestration logic, NPU-resident quantized models, GPU-resident large-model inference, and DPU-resident network policy enforcement, all executing concurrently on a single AI task.

The OS must therefore maintain policies for:

- **Placement**: which computational stage of an AI pipeline executes on which hardware type, given current load, latency requirements, and power budget.
- **Data locality**: where is the model weight, the context window, and the retrieved knowledge — and how much does it cost to move each to the execution unit?
- **Attestation**: which execution environments have been verified to be running known software, and which workloads require attestation before executing in proximity?
- **Fallback**: if the NPU is unavailable (thermal throttling, hardware fault), what does the AI pipeline do — fall back to CPU inference, degrade gracefully, or fail the task?

**Energy and thermal management** deserves emphasis as a first-class OS concern, not an afterthought. On modern mobile and embedded SoCs, the AI inference workload and the OS management overhead compete for the same power budget and contribute to the same thermal envelope. An NPU inference burst may drive junction temperature above the throttling threshold, reducing CPU frequency and degrading OS responsiveness. Without thermal-aware scheduling — where the OS models the thermal consequences of scheduling decisions across the CPU, NPU, and GPU simultaneously — thermal throttling is unpredictable and its impact on AI workload latency is opaque. This is not a performance optimization; it is a correctness concern for AI-OS designs deployed in thermally constrained environments.

> **Key insight for all audiences:** The fundamental hardware assumption of classical OS design — that there is a CPU with some memory — is no longer adequate for AI workloads. A modern AI compute environment is a heterogeneous, partially disaggregated, policy-rich fabric of processing elements with different capabilities, isolation properties, and power characteristics. The OS that manages this fabric needs abstractions that classical OS theory has not yet provided.

---

## 5. How to Create an Operating System

### 5.1 The Engineering Pipeline [P]

Creating an operating system is one of the hardest sustained engineering challenges in software. The following sequence describes the canonical pipeline, from initial scope to production deployment. Each step is demanding in isolation; the combination is the reason that successful new OS efforts are measured in decades, not years.

**Scope definition** comes first: what is the target hardware, who are the users, what are the performance and security requirements, and what compatibility constraints must be respected? A decision made here — to target a single processor family, to maintain POSIX compatibility, to certify to a safety standard — constrains every subsequent step. Scope creep during OS development is catastrophically expensive.

**Architecture selection** follows: monolithic kernel, microkernel, hybrid, unikernel, or capability-based? This choice determines the trust model, the performance profile, the verification approach, and the developer experience for the next decade. Microkernel architectures offer stronger isolation and verifiability; monolithic architectures offer better performance and easier driver integration. There is no right answer independent of requirements.

**Boot implementation** is the first concrete engineering challenge. The OS must initialize at the power-on reset, establish a trusted execution environment before loading the kernel, and hand off from firmware in a verifiable state. Boot code is the most security-critical software in the system — a boot-path vulnerability compromises every security guarantee that follows. Modern boot chains (UEFI Secure Boot, ARM Trusted Firmware, RISC-V Trusted Execution) have made this somewhat more tractable, but boot implementation remains a specialized engineering discipline.

**Kernel core implementation** provides the foundational services: interrupt handling, privilege separation, timer management, context switching, and memory initialization. This is the software that, if it fails, fails immediately and visibly. Kernel panics, memory corruption from early allocation bugs, and interrupt masking errors are the characteristic failures of this phase.

**Resource managers** build on the kernel core: a scheduler (deciding which thread runs on which CPU at each moment), a memory manager (managing virtual address spaces, page allocation, TLB coherence, swap), and a filesystem (organizing persistent storage, managing the VFS layer, handling concurrent access). Each of these is a deep engineering discipline in its own right; the Linux scheduler, for example, has been under continuous active development for over thirty years.

**Device support** is, in practice, one of the largest engineering investments in any OS effort. Hardware devices — storage controllers, network adapters, display controllers, input devices, cryptographic accelerators — each require a driver: software that understands the device's register interface, interrupt behavior, DMA constraints, and power management requirements. An OS with thirty drivers is a research prototype. An OS with thirty thousand drivers is a product. The distance between those two numbers is measured in engineer-years.

**User-space contract** defines what applications can depend on: the system call API, the C runtime library interface, the executable format (ELF, COFF, Mach-O), the dynamic linker, the shell, and the language runtime assumptions. Once established, this contract is extremely difficult to change; applications are built to it and their binaries encode it. The POSIX standard exists precisely because OS vendors recognized that a stable user-space contract is a public good that benefits the entire ecosystem.

**Development discipline** is the operational side of OS engineering: kernel instrumentation and tracing (ftrace, perf, DTrace), debugging (KGDB, kernel address sanitizers), performance measurement and regression testing, security vulnerability management, upgrade mechanisms, and the organizational processes that sustain quality in a large, multi-contributor codebase over years. Linux's development discipline, embodied in maintainer trees, Tested-By chains, and the linux-next integration tree, is as important to its success as any technical feature.

**Ecosystem building** is the final and often decisive factor. An OS without a compiler toolchain, a package manager, documentation, a tutorial ecosystem, and a developer community cannot reach production adoption regardless of its technical merits. The history of technically superior OSes that failed for ecosystem reasons — Multics, Plan 9, various research microkernels — illustrates this principle repeatedly.

---

### 5.2 The Minimum Viable Kernel [E]

If the full OS engineering pipeline is too ambitious for an initial effort, what is the minimum necessary for a kernel to be functional? The xv6 teaching OS [44], used in MIT's operating systems course, provides a useful baseline: approximately 10,000 lines of C that implement the core of a Unix-like kernel sufficient for student experimentation.

The minimum viable kernel requires, in order:

**First**, privilege separation: the CPU must have at least two execution levels (privileged and unprivileged), and the kernel must execute in the privileged level with user code executing in the unprivileged level. On x86-64, this is ring 0 (kernel) and ring 3 (user). On ARM, this is EL1 (kernel) and EL0 (user). Without privilege separation, there is no kernel — there is only software running in a flat address space.

**Second**, trap and interrupt handling: when a user-space program executes a system call instruction (SYSCALL on x86-64, SVC on ARM), the CPU must save the user-space register state, switch to the kernel stack, and transfer control to a defined kernel entry point. Similarly, hardware interrupts — from timers, network cards, storage controllers — must be dispatched to registered handlers in kernel space. These mechanisms are the foundation of everything else.

**Third**, timer support: without a hardware timer firing periodic interrupts, the kernel cannot preempt a running process. A timer interrupt every 10ms (or at whatever the configured tick frequency) gives the scheduler the opportunity to switch from one thread to another. Without this, a single uncooperative process can prevent all others from running.

**Fourth**, context switching: the ability to save the complete architectural state of one execution context (all registers, including the program counter and stack pointer) and restore the state of another. This is the mechanism by which the illusion of parallelism is created on a single CPU.

**Fifth**, memory initialization: the kernel must initialize the page allocator, set up page tables for its own virtual address space, and establish a memory map that tracks which physical memory ranges are available, reserved for devices, or in use by the kernel itself.

With these five primitives in place, a kernel can boot and do exactly one thing: run. Adding a scheduler turns it into a system that can run multiple things. Adding a memory manager turns it into a system that can run them without interfering with each other. Adding a filesystem turns it into a system that can persist their work. Each of these additions is a substantial engineering effort.

The seL4 and MINIX 3 projects demonstrate alternative design philosophies: MINIX 3 recovers from driver failures by restarting driver servers without rebooting, demonstrating that fault isolation is possible at a modest performance cost; seL4 demonstrates that formal correctness verification is possible at a substantial development cost. Both are valuable existence proofs for an AI-OS designer: seL4 in particular shows that a verified microkernel is feasible as a substrate, even if the verification investment is high.

---

### 5.3 The Ecosystem Burden [P/E]

The engineering pipeline described in Section 5.1 produces a kernel. It does not produce a production OS. The gap between a working kernel and a production OS is the ecosystem burden, and it is larger than most "new OS" proposals acknowledge.

**Drivers** are the most immediate constraint. Every piece of hardware that the OS must support requires a driver. A research kernel running on a QEMU virtual machine needs perhaps five drivers. A laptop deployment needs drivers for the display controller, trackpad, keyboard, wireless NIC, Bluetooth, audio codec, camera, fingerprint reader, accelerometer, ambient light sensor, NVMe controller, and USB hub. Each of these is a unique engineering effort. The Linux driver tree contains approximately 70% of the kernel's total source code — a data point that illustrates where most OS engineering effort actually goes.

**Toolchains and development environments** must either be ported to the new OS or cross-compiled from a host. Without a working C compiler, a debugger, a linker, and a package format, application development on the new OS is infeasible. Without a package manager, deploying software is a manual process that does not scale.

**The verification cost** deserves explicit quantification. The seL4 functional correctness proof [19] took approximately 20 person-years to develop for a kernel of roughly 10,000 lines of C. The proof covers the C implementation against a Haskell reference specification, and the binary against the C source (via a separate translation validation). This is the gold standard for OS verification — and it was feasible only because seL4 is tiny by the standards of a production kernel. A monolithic kernel like Linux, with over 30 million lines of code, is not verifiable by any current technique. This is not a deficiency of current verification tools; it is a reflection of the fundamental tradeoff between feature richness and verifiability.

> **Callout: The Real Reason New OS Efforts Fail**
>
> Most failed "new OS" efforts do not fail because the high-level concept was incoherent. The concept is often sound. They fail because boot, drivers, memory safety, compatibility, observability, and ecosystem gravity are brutally hard — and the cumulative engineering investment required to reach production quality is consistently underestimated by several orders of magnitude. This is one reason the most credible AI-based OS paths reuse an existing kernel or verified substrate rather than discarding it. Building on Linux (with eBPF, sched_ext, and cgroups v2 as AI-OS insertion points) or on seL4 (as a verified microkernel substrate) is not a concession; it is a rational engineering decision.

The ecosystem gravity problem is a final, often decisive constraint. Applications, developers, tooling, documentation, and deployment experience accumulate around existing OS platforms over decades. A new OS that requires porting an application ecosystem starts at a severe disadvantage. The practical implication for AI-OS design is that architectures that preserve compatibility with the existing Linux or POSIX ecosystem — Type A and Type B in the taxonomy of Section 1 — have a dramatically lower adoption barrier than clean-sheet designs.

In systems engineering terms, creating an OS is not a single act of coding. It is the staged construction of a trusted, resource-governing substrate together with interfaces, tooling, assurance evidence, and an ecosystem strategy — each stage dependent on the previous, each requiring sustained engineering investment and organizational commitment. Any proposal for an "AI operating system" that does not engage seriously with this reality is not an engineering proposal; it is a vision statement.

---

*Part II continues with Section 6: AI Taxonomy Relevant to an AI-Based OS.*

---

## References (Part I)

[1] M. Mei et al., "AIOS: LLM Agent Operating System," in *Proceedings of COLM 2025*, 2025. [arXiv:2403.16971]

[2] Memory-OS Research Group, "MemOS: A Memory Operating System for LLM Agents," arXiv preprint, 2025. [arXiv:2502.12345, illustrative — verify actual ID before publication]

[3] H. Zhu et al., "Decima: Learning Task Scheduling with Graph Neural Networks," in *Proc. ACM SIGCOMM*, 2019. [Representative "AI for OS" scheduling work]

[4] M. Hashemi et al., "Learning Memory Access Patterns," in *Proc. ICML*, 2018.

[5] T. Høiland-Jørgensen et al., "The eXpress Data Path: Fast Programmable Packet Processing in the Operating System Kernel," in *Proc. ACM CoNEXT*, 2018. [eBPF/XDP as "AI for OS" insertion point]

[6] R. uvnet, "claude-flow: Agentic Orchestration for Claude," GitHub, 2025. https://github.com/ruvnet/claude-flow

[7] [Survey reference 1 — verify before publication]

[8] [Survey reference 2 — verify before publication]

[9] [AgentCgroup — verify arXiv ID and authors before publication]

[10] [PunkGo / Right to History — verify arXiv ID before publication]

[11] [SEAgent — verify arXiv ID before publication]

[12] National Institute of Standards and Technology, *NIST IR 7316: Assessment of Access Control Systems*, 2006. [NIST OS definition — verify exact citation]

[13] R. Arpaci-Dusseau and A. Arpaci-Dusseau, *Operating Systems: Three Easy Pieces*, v1.10, Arpaci-Dusseau Books, 2023. https://ostep.org

[14] Unified EFI Forum, *UEFI Specification Version 2.10*, 2023. https://uefi.org/specifications

[15] M. Kerrisk et al., *Linux man-pages*, syscall(2), https://man7.org/linux/man-pages/man2/syscall.2.html

[16] The Open Group, *The Open Group Base Specifications Issue 8 (POSIX.1-2024)*, 2024. https://pubs.opengroup.org/onlinepubs/9799919799/

[17] Airlines Electronic Engineering Committee, *ARINC 653: Avionics Application Software Standard Interface*, Aeronautical Radio Inc., 2010.

[18] AUTOSAR, *AUTOSAR Adaptive Platform Specification*, R22-11, 2022. https://www.autosar.org

[19] G. Klein et al., "seL4: Formal Verification of an OS Kernel," in *Proc. ACM SOSP*, 2009. DOI: 10.1145/1629575.1629596

[20] F. Huici et al., "Unikraft: Fast, Specialized Unikernels the Easy Way," in *Proc. EuroSys*, 2021. DOI: 10.1145/3447786.3456248

[21] A. Madhavapeddy et al., "Unikernels: Library Operating Systems for the Cloud," in *Proc. ASPLOS*, 2013.

[22] Unikraft, "Unikraft Raises $6M to Accelerate Specialized Cloud Runtimes," Press Release, October 2025. [Verify URL before publication]

[23] Google, "Fuchsia OS Documentation," https://fuchsia.dev [Verify F27 release date]

[24] Linux Foundation, *Kubernetes Documentation*, https://kubernetes.io

[25] D. Engler et al., "Exokernel: An Operating System Architecture for Application-Level Resource Management," in *Proc. ACM SOSP*, 1995.

[26] J. Porter et al., "Rethinking the Library OS from the Top Down," in *Proc. ASPLOS*, 2011.

[27] Bytecode Alliance, *WASI: WebAssembly System Interface*, https://wasi.dev

[28] RTCA Inc., *DO-178C: Software Considerations in Airborne Systems and Equipment Certification*, 2011.

[29] International Organization for Standardization, *ISO 26262: Road Vehicles — Functional Safety*, 2018.

[30] International Electrotechnical Commission, *IEC 61508: Functional Safety of E/E/PE Safety-related Systems*, 2010.

[31] International Organization for Standardization, *ISO/DPAS 8800: Road Vehicles — Safety and Artificial Intelligence*, Draft, 2024.

[32] Anthropic, *Model Context Protocol Specification*, 2025. https://modelcontextprotocol.io/specification

[33] Linux Foundation, *Agent2Agent Protocol (A2A) Specification*, 2025. https://a2aprotocol.ai

[34] National Institute of Standards and Technology, "AI Agent Standards Initiative: Request for Information," February 2026. [Verify citation]

[35] Microsoft, "Copilot+ PC: Technical Specifications and Requirements," 2024. https://aka.ms/CopilotPCRequirements [Verify URL]

[36] NVIDIA, *BlueField-3 DPU Technical Overview*, 2023. https://www.nvidia.com/en-us/networking/products/data-processing-unit/

[37] Compute Express Link Consortium, *CXL 2.0 Specification*, 2020. https://www.computeexpresslink.org

[38] AMD, *SEV-SNP: Strengthening VM Isolation with Integrity Protection and More*, White Paper, 2020.

[39] Intel, *Intel Trust Domain Extensions (Intel TDX) Architecture Specification*, 2023.

[40] ARM Ltd., *Arm Confidential Compute Architecture (Arm CCA): System Architecture*, 2021.

[41] NVIDIA, *H100 GPU Trusted Execution Environment: Technical Overview*, 2023.

[42] Intel, *Intel TDX Connect: Enabling Secure CPU-to-GPU Communication*, Technical Brief, 2024.

[43] NVIDIA, *Vera Rubin NVL72 Architecture Overview*, GTC 2025. [Verify citation]

[44] R. Cox, F. Kaashoek, and R. Morris, *xv6: A Simple, Unix-Like Teaching Operating System*, MIT, 2023. https://pdos.csail.mit.edu/6.S081/2023/xv6/book-riscv-rev3.pdf
