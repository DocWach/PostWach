# Toward a Morphism-Grounded AI Operating System: Architecture, Formal Foundations, and Research Roadmap

**Patrick F. Wach**  
University of Arizona, Systems and Industrial Engineering  
Tucson, AZ, USA

*March 2026*

---

## Abstract

The phrase "AI operating system" has proliferated across product marketing, investment decks, and
research papers, acquiring incompatible meanings as it travels. Smartphones, cloud orchestrators,
agent frameworks, and research kernels have all been labeled AI operating systems, rendering the
term nearly useless as a technical designator. This report provides a rigorous answer to a
deceptively simple question: what would a well-engineered AI operating system actually be?

The analysis begins from first principles. An operating system is software that starts first,
maintains hardware control, and provides resource management services -- scheduling, memory,
persistence, protection -- through a stable privileged interface that applications consume
without touching hardware directly. Any candidate AI operating system must satisfy these criteria
or explain precisely why it does not. The report formalizes this as a three-part boundary test
and applies it to five candidate systems.

Two orthogonal research programs have independently produced work labeled as "AI OS": the "AI for
OS" program, which replaces or augments kernel functions with AI-derived components, and the "OS
for AI" program, which extends OS resource management to treat AI agents as first-class managed
entities. Conflating these programs produces architectures that are underspecified in both
directions. The report separates them, maps current systems to each, and analyzes what each
requires.

The central technical contribution is a formal interface contract for an AI operating system.
Using Wymore's system-theoretic formalism, the interface between an AI control plane and its
underlying kernel substrate is defined as a morphism h: Z_ai -> Z_k between two five-tuple
system models. The quality of this morphism is continuously measurable via two orthogonal scalar
metrics: a structural metric S_a that captures how accurately the AI control plane's model of
kernel state reflects reality, and a behavioral metric C_r that captures how closely AI policy
decisions produce their intended outcomes. These two axes are provably orthogonal and together
necessary and sufficient for morphism quality characterization.

The Circuit Breaker watchdog is grounded in this formalism: it monitors S_a and C_r against
configurable thresholds and, on violation, transitions the system to a conventional fallback
mode. Because the Circuit Breaker evaluates only two scalar metrics -- it does not interpret
AI-generated text or reason about agent goals -- it is simpler than the control plane it
monitors by construction, and can be independently verified.

Agent state management emerges as the hardest novel OS problem: agents require coordinated
management of execution context, episodic memory, semantic memory, goal state, and resource
bindings, with ownership, consistency, and persistence semantics that have no direct classical
OS analogue. Four reference architectures are evaluated against nine engineering requirements.
Architecture B -- an AI-native control plane over an unmodified conventional kernel substrate --
is recommended for near-term deployment, because it preserves decades of investment in kernel
correctness and ecosystem while enabling formal AI governance via the morphism interface contract
and Circuit Breaker watchdog. The report concludes with a four-phase roadmap anchored to
Technology Readiness Levels and fifteen precisely stated open research questions that define the
boundary of what is currently known.

---

## Reading Guide

This report is written for three audiences simultaneously. Each section is labeled with one or
more of the following markers:

**[L] -- Labrador retriever level.** A labrador retriever is a friendly, intelligent animal that
cannot read technical papers. Sections marked [L] use plain language, everyday analogies, and no
equations. A non-technical reader -- a program manager, a policy analyst, a curious student --
can read every [L] section and come away with an accurate understanding of what this report is
about, why it matters, and what its recommendations are. No prior knowledge of operating systems
or AI is assumed.

**[P] -- Practitioner level.** A practitioner is a working software architect, systems engineer,
or AI platform engineer who has built or deployed production systems. Sections marked [P] use
technical vocabulary freely, include tables and design patterns, and are written for someone who
needs to make implementation decisions. Some [P] sections contain equations or pseudocode, but
these are always explained in adjacent text.

**[E] -- Expert level.** An expert is a systems researcher, kernel engineer, or formal methods
specialist with deep knowledge of operating systems internals, AI systems, or both. Sections
marked [E] contain formal definitions, derivations, detailed comparative analysis, and references
to primary research literature. Expert readers should focus on Section 2.3 (boundary test),
Sections 6.2 and 7.2 (AI taxonomy and mapping), Sections 9-14 (architecture and formal
foundations), and all appendices.

**Recommended reading paths:**

- *Labrador reader:* Sections 1.1, 2.1, 7.1, 7.3, 17.1-17.4, and the summary boxes throughout.
  You do not need to read anything else to understand what this report recommends and why.
- *Practitioner with limited time:* Sections 1, 2.1-2.2, 7, 8-9 (overview paragraphs), 11.2
  (isolation tiers), 12.3 (degraded mode), 15, and 17. These sections contain the design
  decisions, architectural recommendations, and roadmap without requiring engagement with the
  formal theory.
- *Expert reviewer:* Part IV (Sections 13-14) for the formal foundations. Section 15 and
  Table 6 for the architectural comparison that depends on them. Section 17.5 for the open
  research questions that define the boundary of what is known. Appendix A for the boundary
  test applied to five example systems.

**A note on reference numbering.** Each part uses its own local reference numbering (e.g.,
[III-1] in Part III, [IV-1] in Part IV). References from all parts are unified in Appendix F
with globally consistent numbers. Where a reference appears with a part-local number in the
body text, the Appendix F entry maps to the same work. The note "Reference numbers are
per-section; see Appendix F for unified numbering" applies throughout.

---

## Table of Contents

**Front Matter**
- Abstract
- Reading Guide
- Table of Contents

**Part I: Foundations -- What Exists Today**
- 1. Introduction and Scope [L/P/E]
  - 1.1 What People Mean When They Say "AI Operating System" [L]
  - 1.2 The Two Orthogonal Research Programs [P/E]
  - 1.3 Scope and Method
  - 1.4 What This Report Adds Beyond Existing Surveys
- 2. What Is an Operating System? [L/P/E]
  - 2.1 The Beginner Definition [L]
  - 2.2 The Systems-Level Definition [P]
  - 2.3 The Boundary Test [E]
- 3. OS Taxonomy: Categories, Architecture, Standards [P/E]
  - 3.1 By Purpose [P]
  - 3.2 By Kernel Architecture [E]
  - 3.3 By Standards Regime [E]
- 4. Hardware Substrate and Platform Evolution [P/E]
  - 4.1 The Hardware Spectrum [P]
  - 4.2 The Heterogeneity Inflection [E]
  - 4.3 What This Means for AI-OS Design [E]
- 5. How to Create an Operating System [P/E]
  - 5.1 The Engineering Pipeline [P]
  - 5.2 The Minimum Viable Kernel [E]
  - 5.3 The Ecosystem Burden [P/E]

**Part II: The AI Dimension**
- 6. AI Taxonomy Relevant to an AI-Based OS [P/E]
  - 6.1 A Five-Layer Framework [P]
  - 6.2 Comparative Fit to OS Responsibilities [E]
- 7. What Counts as an AI-Based OS? [L/P/E]
  - 7.1 Three Meanings, Precisely Defined [L/P]
  - 7.2 The "OS for AI" vs. "AI for OS" Mapping [E]
  - 7.3 Industry Evidence: What Has Shipped [P]

**Part III: The Architecture -- What Must Be Built**
- 8. Engineering Requirements [P/E]
  - 8.1 R1: Trusted Substrate
  - 8.2 R2: AI Runtime and Resource Manager
  - 8.3 R3: Tool and Interoperability Layers
  - 8.4 R4: Model Lifecycle Management
  - 8.5 R5: Hardware-Aware Heterogeneous Scheduler
  - 8.6 R6: Operator Control and Auditability
  - 8.7 R7: Risk Management and Governance
  - 8.8 R8: Agent State Management
  - 8.9 R9: Energy and Thermal Governance
- 9. The AI-Kernel Interface Contract [E]
  - 9.1 Why the Interface Is the Architecture
  - 9.2 Downward API: AI Control Plane to Kernel
  - 9.3 Upward API: Kernel to AI Control Plane
  - 9.4 Policy vs. Mechanism Boundary
  - 9.5 Existing Insertion Points [P/E]
- 10. Agent State Architecture [E]
  - 10.1 The State Taxonomy
  - 10.2 Storage Substrates per Category
  - 10.3 Ownership and Isolation
  - 10.4 Consistency Model
  - 10.5 Relation to MemOS
  - 10.6 The "Everything Is Context" Alternative
- 11. Security Architecture [E]
  - 11.1 Threat Model for an AI-Native OS
  - 11.2 Agent Isolation Tiers
  - 11.3 Tool Capability Model
  - 11.4 Model Integrity Chain
  - 11.5 Tamper-Evident Provenance
  - 11.6 Confidential Computing Substrate
- 12. Failure Taxonomy and Recovery [E]
  - 12.1 AI Control Plane Failure Modes
  - 12.2 Detection, Containment, Recovery
  - 12.3 Degraded Mode Specification
  - 12.4 The Watchdog Problem

**Part IV: Formal Foundations**
- 13. Morphism-Grounded Interface Specification [E]
  - 13.1 The Wymore Formalism for System Interfaces
  - 13.2 Structural Morphism Quality (S_a)
  - 13.3 Behavioral Morphism Quality (C_r)
  - 13.4 The Circuit Breaker as Watchdog
  - 13.5 Composition Correctness via Morphism Composition
  - 13.6 Connection to DARPA CLARA
- 14. Ontological Grounding [E]
  - 14.1 CBTO as the OS Governance Ontology
  - 14.2 SHACL Validation Pipeline for AI-OS Governance
  - 14.3 Relation to the Portfolio Ontology

**Part V: Reference Architectures and Roadmap**
- 15. Reference Architectures [P/E]
  - 15.1 Architecture A: AI-Augmented Conventional OS [P]
  - 15.2 Architecture B: AI-Native Control Plane (Recommended) [P/E]
  - 15.3 Architecture C: Microkernel/High-Assurance Substrate [E]
  - 15.4 Architecture D: Clean-Sheet AI OS [P/E]
  - 15.5 Comparative Assessment
- 16. Safety-Critical Considerations [E]
  - 16.1 The Certification Gap
  - 16.2 Mixed-Criticality AI OS
  - 16.3 Path to Certifiable AI Components
- 17. Roadmap and Open Questions [L/P/E]
  - 17.1 Phase 0: AI-Augmented Operations (2024-2026)
  - 17.2 Phase 1: Bounded Policy Automation (2025-2027)
  - 17.3 Phase 2: AI-Native Control Plane (2026-2029)
  - 17.4 Phase 3: Heterogeneous Resource Fabric (2028-2032)
  - 17.5 Open Research Questions

**Back Matter**
- Appendix A: Boundary Test Applied to Five Systems
- Appendix B: Glossary of Key Terms
- Appendix C: Comparison Table -- AIOS vs. MemOS vs. PunkGo vs. claude-flow
- Appendix D: Note on AI-Kernel Interface Primitives
- Appendix E: Note on CBTO Extension
- Appendix F: Unified Reference List

---

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

**Microkernel and high-assurance operating systems** — MINIX 3, seL4 — trade compatibility and performance for verifiability. The seL4 microkernel [19] carries a machine-checked formal proof of functional correctness relative to its specification, absence of undefined behavior, and enforced capability-based access control. It took approximately 20 person-years to produce for 8,700 lines of C (plus 600 lines of assembler). For AI-OS purposes, a verified microkernel substrate provides the strongest possible trust anchor — but the integration cost is correspondingly high.

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

- **NVIDIA H100 GPU TEE** [41] is the first GPU-resident trusted execution environment at production scale. The H100 introduces a hardware root of trust for the GPU, encrypts GPU memory, and can generate attestation reports for AI model inference workloads. The overhead for typical LLM inference queries is below 7% — an acceptable cost for regulated or multi-party deployments.

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

**The verification cost** deserves explicit quantification. The seL4 functional correctness proof [19] took approximately 20 person-years to develop for a kernel of 8,700 lines of C (plus 600 lines of assembler). The proof covers the C implementation against a Haskell reference specification, and the binary against the C source (via a separate translation validation). This is the gold standard for OS verification — and it was feasible only because seL4 is tiny by the standards of a production kernel. A monolithic kernel like Linux, with over 30 million lines of code, is not verifiable by any current technique. This is not a deficiency of current verification tools; it is a reflection of the fundamental tradeoff between feature richness and verifiability.

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


---

# Part II: The AI Dimension

## Section 6: AI Taxonomy Relevant to an AI-Based OS [P/E]

The phrase "AI operating system" brings with it an implicit assumption that AI is a single thing — a capability that can be plugged into an OS like a new device driver. This assumption is wrong in a way that matters architecturally. AI is a broad family of techniques with radically different properties, failure modes, and resource demands. Choosing the wrong AI family for an OS role does not merely produce a suboptimal result; it can produce a system that is simultaneously overconfident, opaque, and brittle — exactly the wrong combination for infrastructure software.

This section constructs a layered taxonomy of AI techniques organized around their relevance to OS-like functions. The goal is not to survey the AI literature comprehensively — that literature now runs to hundreds of thousands of papers — but to give architects a structured map for asking: *which AI technique is suited to which OS responsibility, and at what cost?*

---

### 6.1 A Five-Layer Framework [P]

The taxonomy organizes AI techniques into five layers, ordered roughly from the most explicit and interpretable to the most opaque and embodied. Within each layer, the discussion proceeds from plain-language description to technical depth, then maps each technique to concrete OS relevance.

**Table 4: Five-Layer AI Taxonomy for OS-Relevant Analysis**

| Layer | Label | Included Techniques | Primary OS Relevance |
|-------|-------|--------------------|--------------------|
| 1 | Knowledge and Reasoning | Expert systems, probabilistic graphical models, causal AI, neuro-symbolic AI | Policy checking, diagnosis, interpretable decision support, uncertainty handling |
| 2 | Learning and Adaptation | Classical ML, deep learning, reinforcement learning, continual learning, transfer learning | Adaptive control, workload prediction, specialization, optimization over time |
| 3 | Foundation-Model Substrate | LLMs, code models, multimodal foundation models | Natural-language interfaces, code and policy assistance, broad capability bootstrapping |
| 4 | Decision and Autonomy | Planning, single-agent AI, multi-agent systems, agent swarms | Tool orchestration, task decomposition, distributed execution, negotiation |
| 5 | Embodiment and World Models | World models, embodied AI | Cyber-physical integration, robotics, digital twin management, tightly coupled operational autonomy |

---

#### Layer 1: Knowledge and Reasoning

At its simplest, a knowledge-and-reasoning system represents what is known about a domain — facts, rules, relationships — and uses that representation to draw conclusions. This is the oldest form of AI, predating machine learning by decades, and it remains uniquely well-suited to contexts where the reasoning must be visible and auditable.

**Expert systems** encode knowledge as explicit rules in a knowledge base and use a forward or backward chaining inference engine to derive conclusions from those rules [1, 2]. The classic framing — `IF condition THEN action` — maps directly to policy enforcement: a configuration management policy is an expert system rule; a compliance check is a backward-chaining query against a regulatory knowledge base. The core strengths are transparency (every decision traces to a rule), predictability (the same inputs always produce the same outputs), and domain precision (rules can encode regulatory language almost verbatim). The core weakness is brittleness: expert systems depend on human experts to encode every relevant fact, they struggle with open-ended perception, and they cannot adapt when the world changes without manual rule revision.

**Probabilistic graphical models (PGMs)** — Bayesian networks, Markov random fields, dynamic Bayesian networks — represent uncertain knowledge as a graph where nodes are variables and edges encode conditional dependencies [3]. Where expert systems assume the world is knowable with certainty, PGMs acknowledge partial observability and noisy evidence. For an OS this matters in diagnostic contexts: a system anomaly might stem from any of a dozen interacting causes, and PGMs can maintain a probability distribution over hypotheses rather than committing to a single answer. PGM inference scales poorly with graph complexity and requires careful modeling of dependencies, but for structured diagnostic problems with well-understood causal structure, they offer uncertainty quantification that expert systems cannot match.

**Causal AI** extends probabilistic reasoning to the distinction between correlation and intervention — the ability to answer not just "what is associated with what" but "what would happen if I changed X?" [4]. Causal methods support counterfactual reasoning ("if I had allocated more memory to that agent, would the latency spike have occurred?") and root-cause analysis that goes beyond correlation. In OS terms, causal AI is the natural tool for incident post-mortems and for reasoning about the effects of policy changes before deploying them.

**Neuro-symbolic AI** combines statistical learning — typically a neural network — with explicit symbolic structure [5]. The motivation is to capture the best of both worlds: neural components handle perception and pattern recognition at scale, while symbolic components enforce constraints, support compositional reasoning, and provide explanations. For an OS, neuro-symbolic approaches are attractive for tasks that require both contextual understanding and rule-constrained behavior — for example, a tool-invocation policy that must learn from usage patterns but must never violate explicit security constraints. The current liability is immaturity: neuro-symbolic integration remains an active research area with few production-grade frameworks, and integration with existing system infrastructure is non-trivial.

---

#### Layer 2: Learning and Adaptation

Where Layer 1 techniques reason from knowledge explicitly provided, Layer 2 techniques acquire knowledge from data. This shift unlocks the ability to generalize, adapt, and improve over time — but at the cost of interpretability, stability guarantees, and predictable failure modes.

**Classical machine learning** — linear models, decision trees, gradient boosting, support vector machines — produces models that are relatively compact, computationally cheap at inference time, and often interpretable. For OS applications such as workload classification, anomaly detection, and performance prediction, classical ML remains competitive with deep learning while imposing far lower runtime overhead and offering better-understood generalization bounds.

**Deep learning** — multi-layer neural networks, convolutional architectures, transformers — delivers state-of-the-art performance on perception, sequence modeling, and high-dimensional pattern recognition. Its OS relevance lies primarily in recognizing complex patterns in logs, traces, and telemetry that resist hand-crafted feature engineering. Deep learning models are large, computationally intensive, and opaque; deploying them on the critical OS management path demands careful isolation and fallback planning.

**Reinforcement learning (RL)** is the AI family most naturally aligned with OS control problems [6]. An RL agent observes system state (CPU utilization, queue depths, memory pressure), takes actions (schedule process A, migrate workload B, throttle agent C), receives a reward signal (latency, throughput, energy consumption), and learns a policy that maximizes cumulative reward over time. The mapping from OS scheduling and resource management to the RL state-action-reward framework is almost exact in principle. In practice, RL in production systems faces three serious challenges: reward misspecification (optimizing the measured metric rather than the intended objective), instability during exploration (the agent may try harmful actions while learning), and sample inefficiency (learning a good policy may require millions of transitions, which is expensive or impossible on a production system). Offline RL and constrained RL variants address some of these challenges, but caution and conservative initialization remain essential.

**Continual learning** — also called lifelong learning — addresses the problem of adapting a model to new data without catastrophic forgetting of previously learned knowledge [7]. This is directly relevant to long-lived OS intelligence: a scheduler that learns a good policy for one workload mix must not forget it when the workload changes seasonally, and a policy engine that learns new compliance rules must not erase its understanding of existing ones. Continual learning remains an active research problem; the best current techniques (elastic weight consolidation, progressive neural networks, replay-based methods) all involve tradeoffs between plasticity and stability.

**Transfer learning** — adapting a model trained on one domain for use in another — is relevant to OS deployment scenarios where training data is scarce [8]. A general workload predictor trained on cloud telemetry can be fine-tuned on a specific organization's usage patterns; a policy model trained in simulation can be adapted to a production environment with limited safe exploration. Transfer learning reduces the data requirement for specialization, which is important for OS intelligence that must be useful from the first deployment.

---

#### Layer 3: Foundation-Model Substrate

Foundation models are large neural networks trained on broad, diverse datasets — typically via self-supervised learning — that acquire general-purpose representations reusable across many downstream tasks [9]. Large language models (LLMs), code models, and multimodal models all belong to this category. A critical clarification: LLMs are a subset of foundation models, not a synonym. The broader category includes models that process images, audio, structured data, and combinations thereof; LLMs are specifically foundation models trained predominantly on text.

**For an OS**, the foundation-model substrate is relevant primarily as an interface and assistance layer rather than a core control mechanism. Natural-language user interfaces, code generation for configuration and automation, policy drafting, documentation synthesis, and multimodal interaction all benefit from foundation model capabilities. The ability to issue an instruction in plain English — "allocate 40% of NPU capacity to the rendering workload until the deadline at 5 PM" — and have the system interpret and execute it correctly requires the kind of broad linguistic competence that only foundation models currently provide.

The liabilities are substantial and architectural. Foundation models hallucinate — they generate plausible-sounding but incorrect outputs — at rates that remain poorly characterized for safety-critical contexts [9]. They are susceptible to prompt injection, where adversarial content in the environment causes the model to execute instructions it should not [10]. They are expensive to run and expensive to update; a model that fits in the OS management layer today may require hardware upgrades to run after the next version release. Their outputs are nondeterministic, which makes testing and verification fundamentally harder than for conventional software. And their context windows, while growing, impose limits on the amount of system state a foundation model can reason about simultaneously.

The architectural implication is clear: foundation models should be used where their broad capabilities provide clear value — interaction, assistance, search, drafting — and should not be placed on the latency-critical or safety-critical OS control path. Section 9 will specify where the boundary should fall.

---

#### Layer 4: Decision and Autonomy

Layer 4 techniques are concerned with constructing and executing plans — sequences of actions that achieve goals under constraints, possibly across multiple interacting agents.

**Planning systems** generate action sequences from goal specifications, precondition-effect models of available actions, and constraints [11]. Classical planning (STRIPS, PDDL) produces deterministic, verifiable plans when the domain model is accurate. Modern neuro-symbolic planners and LLM-augmented planning systems handle more open-ended goal specifications at the cost of weaker guarantees. For an OS, planning is relevant to workflow orchestration, task decomposition, and constrained resource allocation — any scenario where the system must reason about a multi-step action sequence before committing to the first action.

**Single-agent AI** encapsulates the pattern of a single AI system using tools, maintaining state, and pursuing goals within a bounded scope [11]. The governance and ownership model is simple: one agent, one responsibility, one boundary. Single-agent systems are appropriate for personalized assistance, local automation, and contained tool use. They do not scale to complex multi-system coordination.

**Multi-agent systems** decompose complex tasks across multiple specialized agents that coordinate through defined communication protocols [12]. The coordination mechanisms — message passing, negotiation, shared memory, auction-based allocation — mirror distributed systems patterns, and the OS-level challenges are analogous: agent discovery, resource contention resolution, failure isolation, and consistency across distributed state. "Agentic swarms" — large numbers of relatively simple agents organized for parallelism — are a specific organizational pattern within multi-agent systems, not a scientifically distinct family. The gains from multi-agent decomposition (specialization, parallelism, fault isolation) come with corresponding costs: coordination overhead, emergent failure modes that neither individual agent can anticipate, and debugging difficulty that increases combinatorially with agent count.

---

#### Layer 5: Embodiment and World Models

**World models** are internal learned representations of environment dynamics — models that the AI system uses to simulate how the world will respond to actions, enabling planning and decision-making without requiring direct experimentation [13]. In OS contexts, world models are most relevant for cyber-physical systems where the OS controls or monitors physical processes: an AI OS for a manufacturing robot needs an internal model of how the robot's actions affect its physical environment; a digital-twin-backed control system uses a world model to predict process behavior before intervening.

**Embodied AI** — AI systems that learn through physical interaction with an environment — is central to robotics and autonomous systems and optional for conventional computing operating systems. An OS for an autonomous vehicle or a space system may require embodied AI components; an OS for a data center or a workstation does not. The engineering burden — large training datasets collected from physical interaction, tight integration with sensor and actuator systems, real-time control loops — is substantial.

Layer 5 is included in this taxonomy for completeness and for architectures targeting cyber-physical or robotic operating environments. It is marked out-of-scope for office productivity and enterprise computing OS designs, though it becomes directly relevant for the NNSA mission contexts that involve physical plant monitoring and autonomous system management.

---

### 6.2 Comparative Fit to OS Responsibilities [E]

Having characterized each AI family, we can now map them systematically to classical OS responsibilities. This mapping is the analytic core of the taxonomy — the question a designer must answer before committing to an AI-for-OS architecture.

**Table 5: AI Family Fit to OS Responsibilities**

| AI Family | Best-Fit OS Roles | Strengths | Primary Liabilities |
|-----------|-------------------|-----------|---------------------|
| Expert systems | Policy enforcement, compliance checking, configuration validation, explainable troubleshooting | Explicit rules, full traceability, predictable behavior, auditability | Brittle knowledge acquisition; weak at open-ended perception; cannot self-update |
| Probabilistic + causal reasoning | Anomaly diagnosis, fault isolation, root-cause analysis, uncertainty-aware resource estimation | Uncertainty quantification, counterfactual reasoning, structured hypothesis maintenance | Modeling complexity; sensitive to domain assumptions; data quality requirements |
| Neuro-symbolic AI | Rule-constrained automation, explainable policy enforcement, mixed-mode reasoning workflows | Combines statistical learning with explicit structure; explanation + compositionality | Immature tooling; difficult integration patterns; limited production-grade frameworks |
| Reinforcement learning | Adaptive scheduling, power/performance tuning, queue management, placement optimization | Sequential decision optimization under measured objectives | Reward misspecification; instability during exploration; sample inefficiency; safety risks |
| Foundation models / LLMs | Natural-language interface, code and policy drafting, multimodal user support, general assistance, log summarization | Wide capability coverage; flexible zero-shot and few-shot adaptation; multimodal | Hallucination; prompt injection exposure; cost; context sprawl; nondeterminism; verification difficulty |
| Planning systems | Task decomposition, multi-step workflow orchestration, constrained action sequencing, dependency resolution | Goal-directed structure; explicit search; verifiable plan preconditions | Sensitive to domain modeling quality; search complexity grows with plan depth; open-world brittleness |
| Single-agent AI | Tool use, local automation, personalized assistance, contained task execution | Simple governance; clear ownership boundaries; straightforward to monitor and audit | Limited specialization; does not scale to complex multi-system coordination |
| Multi-agent systems and swarms | Complex task decomposition, coordination across services or hardware tiers, distributed workload management | Role specialization; parallelization; fault isolation when properly designed | Coordination overhead; emergent failure modes; debugging difficulty; state consistency challenges |
| World-model / embodied AI | Cyber-physical OS, robotic control, digital twin management, autonomous systems | Forward simulation; decision support in dynamic physical environments | High data and integration burden; less relevant for conventional computing |

The table reveals two structural patterns that have direct architectural implications.

First, no single AI family covers more than a fraction of the OS responsibility surface. Policy enforcement favors expert systems; diagnosis favors probabilistic reasoning; interaction favors foundation models; resource optimization favors RL; complex task execution favors multi-agent systems. An architecture that commits to a single AI paradigm — most commonly, an architecture that equates "AI OS" with "LLM OS" — will either leave most OS responsibilities to conventional code (rendering the "AI" label misleading) or will attempt to use foundation models for roles they are poorly suited to (rendering the architecture fragile).

Second, the liabilities of the AI families are not uniformly distributed. Foundation models are most problematic where determinism and verifiability are required — exactly the properties the OS control path demands. Expert systems and probabilistic reasoning are most problematic where open-ended adaptation and perceptual breadth are required — exactly what interaction layers need. A credible AI-based OS architecture will therefore be layered and compositional, assigning each AI family to the OS role where its strengths dominate its liabilities.

> **Key Architectural Insight**: No single AI family should be expected to "be the OS." A credible AI-based OS will almost certainly be a composite: symbolic or neuro-symbolic reasoning for policy enforcement, probabilistic and causal methods for diagnosis, reinforcement learning or predictive control for adaptation, foundation models for interaction and general assistance, and multi-agent patterns for decomposition and tool use. The central design challenge is not choosing the AI family but specifying the interfaces between families and between the composite AI layer and the conventional substrate below it.

#### Concrete Insertion Mechanisms

Beyond the abstract mapping, two concrete engineering mechanisms deserve specific attention because they represent deployed or near-deployed paths to "AI for OS" functionality rather than hypothetical future capabilities.

**eBPF and sched_ext** constitute the Linux-native path to AI-influenced kernel behavior. Extended Berkeley Packet Filter (eBPF) allows verified programs to be loaded into the kernel and attached to specific hooks — network processing, system call tracing, performance counters, and, as of Linux 6.11, the CPU scheduler through the `sched_ext` interface [14]. The `sched_ext` framework, developed jointly by Meta and Google and merged into the Linux mainline in June 2024, allows complete replacement of the CPU scheduling policy with an eBPF program without recompiling the kernel. Projects such as SchedCP combine LLM-generated scheduling strategies with `sched_ext` to produce an adaptive scheduler: the LLM reasons semantically about workload characteristics, generates an eBPF scheduling program, and loads it at runtime — achieving up to 1.79x faster build times and 2.11x P99 latency reduction in reported benchmarks [15]. AgentSight and GPTtrace use eBPF to provide zero-instrumentation observability into LLM agent behavior at the kernel level [16]. These are not research prototypes in the traditional sense; `sched_ext` is mainline Linux, eBPF is deployed in production at Google, Meta, and Cloudflare, and the AI-augmented scheduling work is actively productizing. For architectures that must interoperate with existing Linux infrastructure, eBPF + `sched_ext` is the most mature available path.

**WASM and WASI** constitute a complementary insertion point from the runtime direction. WebAssembly (WASM) was originally designed for portable, safe execution of code in web browsers, but its memory-safe, capability-based execution model makes it attractive as a portable AI runtime layer outside the browser [17]. The WebAssembly System Interface (WASI) defines a capability-based interface for WASM modules to access system resources, providing deny-by-default sandboxing: a WASM tool has no filesystem access, no network access, and no environment access unless explicitly granted through a WASI capability. Microsoft's Wassette project (released August 2025) implements this model for AI agent tools: agents can fetch WASM components from OCI registries and execute them in isolated sandboxes with strict resource limits, providing a sandboxing model for tool use that is lighter than containers and more principled than process isolation alone [18]. WASI-NN extends the interface to hardware-accelerated neural network inference, turning AI inference into a cross-platform capability rather than a hardware-specific deployment problem [19]. Hyperlight (Microsoft Research) takes this further, executing WASM modules without a traditional OS at all — an extreme unikernel pattern relevant for the lowest-latency, highest-isolation agent tool deployments.

These two mechanisms — eBPF + `sched_ext` at the kernel boundary, WASM + WASI at the runtime boundary — are not just illustrative of a paradigm. They are the concrete engineering tools available today for building prototype AI-native control planes on existing substrates, and any near-term architecture (Type B as defined in Section 7) should treat them as the primary implementation path.

---

## Section 7: What Counts as an AI-Based OS? [L/P/E]

The question "is this an AI operating system?" is more than taxonomic. It determines what claims can be made about the system's properties, what architectural decisions are load-bearing, and whether the marketing language reflects something real or is a rebranding exercise. This section provides three precise definitions, grounded in the OS boundary test established in Section 2.3, and then evaluates current industry products against them.

---

### 7.1 Three Meanings, Precisely Defined [L/P]

#### Type A: AI-Augmented Conventional OS

In plain language: a normal operating system with AI services running on top of it or integrated as system services. The kernel, device drivers, scheduler, memory manager, and filesystem remain conventional code. AI handles interaction, diagnostics, search, policy suggestion, and workload optimization — all services layered above the hardware-mediated compute substrate that the kernel manages.

Analogy for the entry-level reader: imagine a building with traditional structure — concrete, steel, elevators, plumbing — but with smart thermostats, voice assistants, and an AI building manager who can answer questions, schedule maintenance, and suggest energy optimizations. The building's structure does not change. The intelligence lives above it, communicating with occupants and adjusting settings, but cannot redesign the walls.

Type A is the category that encompasses most of what is currently marketed as "AI operating systems." The OS provides process isolation, hardware mediation, and the security boundary. AI services run as privileged system processes or as managed services above the kernel, with the same trust level as other system software. The kernel may be unmodified; the AI capabilities are additions, not replacements.

Type A does not mean superficial. Apple Intelligence (discussed in Section 7.3) is Type A, and it involves deep hardware co-design, a custom Neural Engine, sophisticated on-device/cloud routing, and a new developer API surface (Foundation Models framework). It is a serious engineering achievement. But the boot path, kernel, scheduler, and memory manager of iOS and macOS remain conventional. The AI is powerful and deeply integrated into the product experience; it is not the kernel.

**Formally**: Type A satisfies the OS boundary test (trusted boot path, hardware mediation, stable privileged interfaces) through conventional means. AI components satisfy none of the three boundary-test conditions on their own; they depend entirely on the conventional kernel for isolation and hardware mediation.

#### Type B: AI-Native Control Plane over Conventional Substrate

In plain language: the conventional kernel handles the minimum required trust functions — booting, isolation, memory safety, interrupt handling, device mediation — and AI becomes the primary locus of policy, orchestration, and work decomposition above it. The kernel continues to provide the trust foundation; the AI layer sits above it as the intelligence layer and drives most of the decisions that a traditional OS kernel might have made deterministically.

Analogy: replacing the building management system — the system that schedules HVAC, controls access, monitors power consumption, routes maintenance requests — with an AI-driven one, while keeping the building's structure (concrete, steel, elevators) intact. The building looks the same from outside. Inside, the intelligence that governs its operation has changed fundamentally. The walls cannot reconfigure themselves, but everything that happens within and between the walls is now orchestrated by AI.

Type B is the recommended near-term architecture for production AI-native systems. It does not require a new kernel, does not abandon decades of investment in Linux or Windows NT, and does not face the ecosystem incompatibility that a clean-sheet OS must overcome. It does require a carefully specified interface between the AI control plane and the conventional substrate — the central design problem addressed in Section 9.

**Formally**: Type B satisfies the OS boundary test through conventional means (kernel), but the *policy* layer — which decisions are made and how — is primarily AI-governed. The kernel enforces mechanism (scheduling quanta, memory protection, device arbitration); the AI control plane sets policy (which agents communicate, how resources are allocated among workloads, what actions are taken in response to system events). Section 9 specifies what this distinction requires concretely.

#### Type C: Clean-Sheet AI OS

In plain language: a system designed from first principles around AI primitives, where models, tools, and agents are first-class system entities rather than processes managed by a conventional kernel. Many classical OS services — scheduling, memory management, storage access — are reconceived around AI-native abstractions. Low-level hardware management is either replaced by new mechanisms or delegated to a minimal substrate retained for safety.

Analogy: designing an entirely new kind of building where the AI IS the structure — not a manager operating within a fixed building, but a system in which the walls, floors, and rooms adapt dynamically to need. Maximum conceptual freedom; most research-intensive; least mature; weakest ecosystem.

Type C is the research frontier. AIOS v5 and MemOS (discussed in Section 7.3) are the leading exemplars. Both demonstrate that agent-specific kernel abstractions improve performance and governance, but both continue to run atop conventional Linux infrastructure — they are Type C in their conceptual framing and their internal abstractions, while retaining a Type A or B conventional substrate for hardware management.

**Formally**: Type C attempts to satisfy the OS boundary test through AI-native means, at least for the AI-workload portion of the system. In current implementations, this attempt is partial; the hardware boundary is still managed by conventional software, and the "AI OS" label applies to the agent management layer rather than the full system stack.

> **Important Definitional Consequence**: Many products that will be marketed as "AI operating systems" in the near and medium term will be Type A or B — AI-native control planes layered over Linux, Windows, an RTOS, or a microkernel substrate. This is not a defect; it is a feature. The credible engineering path builds intelligence on proven foundations rather than replacing them. The appropriate test is not "does this have a new kernel?" but "where does intelligence sit in the architecture, and what does it control?"

---

### 7.2 The "OS for AI" vs. "AI for OS" Mapping [E]

Section 1.2 identified two orthogonal research programs that the phrase "AI operating system" conflates. The three types defined above map onto those programs in specific ways that have practical implications for system designers.

**Table 6: Type–Program Mapping**

| Type | Serves "AI for OS"? | Serves "OS for AI"? | Primary Gap | Industry Exemplar |
|------|---------------------|---------------------|-------------|-------------------|
| A: AI-augmented | Yes — AI improves specific OS functions (scheduling, anomaly detection, interaction) | Partially — AI services run as applications, not as managed first-class OS entities with OS-level lifecycle governance | AI agents lack formal OS-managed lifecycle; no scheduling or isolation guarantees beyond process-level | Copilot+ PC (current), Apple Intelligence |
| B: AI-native control plane | Yes — AI drives scheduling, resource allocation, policy enforcement across the compute substrate | Yes — agents become managed entities with OS-level lifecycle, scheduling, and access control managed by the AI control plane | Interface contract between AI control plane and kernel substrate must be formally specified (see Section 9) | Copilot+ PC (trajectory), claude-flow over Linux |
| C: Clean-sheet AI OS | Partially — kernel functions may use AI internally, but primary focus is agent management | Yes — primary purpose is to manage AI agents as first-class workloads; pioneering agent-native abstractions | Hardware mediation still delegated to conventional substrate; ecosystem and verification immature | AIOS v5, MemOS |

Several architectural consequences follow from this mapping.

First, Type A systems that aspire to serve "OS for AI" — to manage AI agents as first-class entities — face a fundamental gap: agents in a Type A system are processes or services; they have process-level scheduling and memory management, not agent-level lifecycle governance. This is not merely a missing feature; it is an architectural mismatch that cannot be resolved by adding another system service. The step from Type A to Type B is therefore not incremental; it requires defining what "agent lifecycle" means at the OS level and implementing a control plane that enforces it.

Second, Type B requires the interface specification that Section 9 provides. Without a specified downward API (AI control plane to kernel) and upward API (kernel to AI control plane), "AI-native control plane" is a metaphor. The interface is the architecture.

Third, Type C and the "OS for AI" program share a common challenge: defining what it means for an agent to be a first-class OS entity. This is harder than it appears. Classical OS first-class entities — processes, threads, files, sockets — have clear semantics: creation, lifecycle, resource accounting, isolation, termination. Agents have goal state, episodic memory, semantic memory, resource bindings, and delegation relationships. The agent state architecture (Section 10) is the missing formalism that would make Type C systems as well-specified as their Type B counterparts.

---

### 7.3 Industry Evidence: What Has Shipped [P]

The following five cases ground the taxonomy in real deployments. For each, the discussion identifies which type the system represents, the key architectural choices it makes, and what those choices reveal about the design space.

#### Microsoft Windows AI Foundry / Copilot+ PC (Type A → B Transition)

Windows AI Foundry — announced at Microsoft Build 2025 as a renaming of the Windows Copilot Runtime — is Microsoft's unified AI development stack for Windows, providing a lifecycle from model selection and optimization through fine-tuning and on-device deployment [20]. The platform aligns Windows AI tooling with Azure AI Foundry, establishing a consistent model management model across edge and cloud.

The architectural trajectory is a deliberate transition from Type A toward Type B. The current Copilot+ PC experience — AI features layered above a conventional Windows 11 kernel — is clearly Type A: the kernel, scheduler, and hardware mediation are unchanged; AI capabilities are system services or applications. The CorePC modular architecture, which decomposes Windows into independently updatable components with the kernel in a read-only partition, prepares the substrate for more aggressive AI integration [21]. The "Bromine" (26H1) kernel update goes further: reports indicate that this update moves Copilot and autonomous agent logic closer to kernel integration, with the stated intent of ending the "AI-on-top" era in favor of AI embedded at the kernel level [22].

The hardware mandate enforces a concrete floor: Copilot+ certification requires a Neural Processing Unit (NPU) capable of at least 40 TOPS, with next-generation requirements rising to 80-100 TOPS. This mandate transforms AI from a software feature into a hardware contract — the beginning of an AI-hardware co-design discipline analogous to what x86 privilege rings did for memory protection.

**Architectural lesson**: The world's largest OS vendor is evolving incrementally from Type A to Type B — not through a clean-sheet rewrite, but through modular decomposition, a hardware mandate, and kernel integration of the control plane. The incremental path is deliberate: it preserves ecosystem compatibility while advancing the architecture. This is the most credible near-term trajectory for production OS evolution.

#### Apple Intelligence (Type A with Deep Hardware Integration)

Apple Intelligence is the umbrella AI capability for iOS 18+, iPadOS 18+, and macOS Sequoia and beyond. The on-device component is a ~3 billion parameter multimodal foundation model optimized for Apple silicon through architectural innovations including KV-cache sharing and 2-bit quantization-aware training [23]. The model runs on the Neural Engine — a co-processor integrated into Apple's A-series and M-series SoCs that is managed by the OS, not directly accessible to application developers.

The Foundation Models framework (WWDC 2025) extends the OS service model to AI: Apple exposes a developer API through which third-party applications access the same on-device foundation model that powers Apple Intelligence [24]. This is a significant architectural move — it treats the on-device AI model as a managed OS resource, analogous to how iOS manages location services or camera access: capability-gated, privacy-controlled, metered, and shared across applications without each application managing its own model.

The routing architecture further illustrates the OS service model. The OS classifies tasks and routes them to on-device inference (privacy-first, available without network connectivity) or to Private Cloud Compute (power-first, for tasks exceeding on-device model capacity), with the routing decision made at the OS level rather than the application level [25]. Applications do not decide where their AI workloads run; the OS does, based on policy that the user can inspect and configure.

**Architectural lesson**: Apple treats the AI model as part of the SoC's OS-managed compute substrate — like a GPU or Neural Engine, not like an application. The Foundation Models framework IS an OS service interface for AI inference. The routing architecture IS an OS resource management policy. This is Type A in the classical sense (no new kernel) but it demonstrates the design moves that characterize Type B: AI capability managed as a first-class system resource with defined policies, isolation, and governance.

#### Google Android AICore / Gemini Nano (Type A with System Service Model)

AICore is a system service built into Android that manages on-device foundation model execution [26]. It provides shared access to a Gemini Nano model across applications — avoiding redundant model downloads, managing hardware-accelerated inference, and maintaining user privacy through isolation and non-persistence of inference inputs and outputs.

The ML Kit GenAI APIs provide the developer interface: high-level use-case APIs (summarization, proofreading, image description) and a low-level Prompt API for flexible interaction [27]. Both are backed by AICore's shared model management. Applications do not instantiate their own model; they call an OS service that manages the model on their behalf.

AICore's privacy architecture reflects the Private Compute Core principles: AICore is isolated from most other system packages; each inference request is isolated; no input or output is persisted after the request completes [26]. This is capability-based AI resource management implemented as a conventional Android system service — no new kernel mechanisms, but a principled OS service architecture for shared AI inference.

**Architectural lesson**: AICore demonstrates that a system service model for AI inference — shared, hardware-accelerated, capability-controlled, privacy-preserving — is deployable on existing OS infrastructure without kernel modifications. It provides a template for how a Type A system can responsibly manage AI capabilities: treat the foundation model as an OS resource, not as an application library. The model is managed; access is mediated; the lifecycle is OS-controlled.

#### AIOS v5 (Type C — Agent-Native Kernel Abstractions)

AIOS — "LLM Agent Operating System" from the AGI Research group at Rutgers University — is the most complete implementation of a Type C architecture in the published literature [28]. The AIOS kernel provides scheduling, context management, memory management, storage management, and access control for runtime LLM agents. It presents agent-specific abstractions — agent context, agent memory, agent scheduling queues — rather than repurposing conventional OS process abstractions for agent workloads.

The AIOS v5 paper (accepted at COLM 2025) reports experimental results demonstrating that agent-specific kernel abstractions improve performance: using the AIOS scheduler rather than direct LLM API calls achieves up to 2.1x throughput improvement with Reflexion-based agents on Llama-3.1-8b, with the system supporting up to 250 concurrent agents by default [28]. The AIOS-Agent SDK and Cerebrum repository provide developer-facing interfaces.

A critical architectural note: AIOS runs atop conventional Linux, not on bare metal. It is a Type C system in its conceptual framing — agents are first-class entities, the "kernel" provides agent-native abstractions — but it delegates hardware management to Linux. This is architecturally honest and practically inevitable: building a new hardware-level OS to demonstrate agent scheduling principles would be a decade-scale undertaking. AIOS demonstrates that the agent abstraction layer is worth building, even if the substrate under it remains conventional.

**Architectural lesson**: Agent-specific kernel abstractions — scheduling, context management, memory governance — measurably improve performance and provide a principled governance layer for AI workloads. This is the strongest empirical evidence to date that "OS for AI" is a real engineering problem with real solutions, not merely an analogy. The AIOS architecture demonstrates what first-class agent management looks like; the open question is how to integrate it with a conventional hardware substrate without losing the trust properties the conventional kernel provides.

#### MemOS (Type C Variant — Memory-Centric)

MemOS takes a different angle on the clean-sheet AI OS problem: rather than focusing on scheduling and process management, it focuses on memory as the primary scarce resource that AI systems fail to manage well [29]. Current LLMs, MemOS argues, have three fundamentally different kinds of memory — parametric (weights), activation (KV cache and runtime state), and plaintext (retrieved facts, RAG content) — but no unified management system that governs them consistently. Applications handle each type ad hoc, with no lifecycle management, no priority-based eviction policy, no consistency guarantees, and no cross-task persistence.

MemOS introduces the **MemCube** as the unifying abstraction: a standardized memory unit that encapsulates both semantic payload and structured metadata, enabling uniform scheduling, access control, and lifecycle governance across all three memory types. MemCubes can be tracked, fused, promoted (from plaintext to parametric, for example), and migrated across memory tiers under unified policy. The reported improvement over OpenAI's global memory on the LoCoMo temporal reasoning benchmark is 159% — a substantial claim that should be independently replicated, but which is directionally consistent with the thesis that unified memory management produces better outcomes than ad hoc per-type handling [29, 30].

**Architectural lesson**: Memory governance may be the central OS design problem for AI workloads — more fundamental than scheduling, because AI systems' performance is dominated by the quality and availability of their memory content, not primarily by compute scheduling. MemOS's MemCube abstraction provides a template for what "agent state as first-class OS resource" could look like in practice. Section 10 will extend this analysis into a full agent state architecture that encompasses MemOS's memory taxonomy and the additional state dimensions (goal state, resource bindings, execution context) that MemOS does not address.

---

#### Synthesis: What the Evidence Establishes

Five observations emerge from examining these five systems together.

**First**, every production system is Type A or, at most, transitioning to Type B. No shipping production OS has made agents first-class entities at the kernel level. The commercial trajectory is clear — Microsoft's Bromine roadmap, Apple's Foundation Models framework, Google's AICore service model all move toward deeper AI integration — but the destination has not been reached.

**Second**, the "system service" pattern is converging as the near-term standard. Apple Intelligence, Android AICore, and Windows AI Foundry all treat the AI model as a managed system resource accessed through a privileged API, not as a library bundled by each application. This is the right architectural move for Type A systems aspiring to Type B: it provides shared resource management, consistent policy enforcement, and OS-mediated access control without requiring a new kernel.

**Third**, the research systems (AIOS, MemOS) demonstrate that agent-specific abstractions produce measurable improvements. This is not merely a conceptual argument; it is an empirical one. The 2.1x throughput improvement in AIOS and the 159% memory benchmark improvement in MemOS provide concrete evidence that the "OS for AI" program addresses real problems with real engineering solutions.

**Fourth**, none of the five systems has specified a formal interface contract between the AI control layer and the conventional substrate. This gap is significant: without a specified interface, the boundary between AI policy and kernel mechanism is informal, underdocumented, and potentially unsafe. Section 9 addresses this gap directly.

**Fifth**, security is the weakest dimension across all five systems. Prompt injection, model supply chain integrity, capability model for AI tool use, and tamper-evident provenance are either absent or superficially addressed in every case. Section 11 develops the security architecture that these systems require but have not yet implemented.

---

*Part III: The Architecture (Sections 8–12) continues in* `part3_architecture.md`.

---

## References (Part II — Sequential, to be unified in Appendix F)

[1] R. Davis, H. Shrobe, and P. Szolovits, "What is a Knowledge Representation?" *AI Magazine*, vol. 14, no. 1, pp. 17–33, 1993.

[2] S. J. Russell and P. Norvig, *Artificial Intelligence: A Modern Approach*, 4th ed. Pearson, 2020.

[3] D. Koller and N. Friedman, *Probabilistic Graphical Models: Principles and Techniques*. MIT Press, 2009.

[4] J. Kaddour, A. Lynch, Q. Liu, M. J. Kusner, and R. Silva, "Causal Machine Learning: A Survey and Open Problems," arXiv:2206.15475, Jun. 2022.

[5] M. M. Hedblom, O. Kutz, B. Guizzardi, and G. Guizzardi, "Towards a Taxonomy of Neuro-Symbolic Approaches," arXiv:2305.08876, May 2023.

[6] R. S. Sutton and A. G. Barto, *Reinforcement Learning: An Introduction*, 2nd ed. MIT Press, 2018.

[7] L. Wang, X. Zhang, H. Su, and J. Zhu, "A Comprehensive Survey of Continual Learning: Theory, Method and Application," arXiv:2302.00487, Feb. 2023.

[8] S. J. Pan and Q. Yang, "A Survey on Transfer Learning," *IEEE Transactions on Knowledge and Data Engineering*, vol. 22, no. 10, pp. 1345–1359, Oct. 2010.

[9] R. Bommasani et al., "On the Opportunities and Risks of Foundation Models," arXiv:2108.07258, Aug. 2021.

[10] K. Greshake, S. Abdelnabi, S. Mishra, C. Endres, T. Holz, and M. Fritz, "Not What You've Signed Up For: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection," in *Proc. ACM Workshop on Artificial Intelligence and Security*, 2023.

[11] Z. Chen, W. Liu, Y. Li, Z. Xiao, and Z. Xu, "A Survey on Planning with Large Language Models," arXiv:2412.05528, Dec. 2024.

[12] Z. Chen, Y. Liu, W. Li, and Z. Xu, "A Survey on Multi-Agent Systems with Foundation Models," arXiv:2412.17481, Dec. 2024.

[13] R. Yang, H. Ma, C. Fang, X. Zhang, H. Wang, and B. Li, "World Models for Autonomous Systems," arXiv:2510.16732, Oct. 2025.

[14] Linux Kernel Development Community, "sched_ext: BPF-Extensible Scheduler Class," Linux Kernel 6.11 release notes, Sept. 2024.

[15] eunomia.dev, "SchedCP: Automatically Optimize Linux Scheduler with MCP Server," 2025. [Online]. Available: https://eunomia.dev/GPTtrace/schedcp/

[16] eunomia.dev, "AgentSight: Zero-Instrument LLM and AI Agent Observability in eBPF," 2025. [Online]. Available: https://eunomia.dev/GPTtrace/

[17] WebAssembly Community Group, "WebAssembly Specification," W3C, 2022. [Online]. Available: https://webassembly.github.io/spec/

[18] Microsoft Open Source Blog, "Introducing Wassette: WebAssembly-Based Tools for AI Agents," Aug. 2025. [Online]. Available: https://opensource.microsoft.com/blog/2025/08/06/introducing-wassette-webassembly-based-tools-for-ai-agents

[19] WebAssembly/WASI, "WASI-NN: Neural Network Proposal for WASI," GitHub, 2024. [Online]. Available: https://github.com/WebAssembly/wasi-nn

[20] Microsoft Windows Developer Blog, "Advancing Windows for AI Development: New Platform Capabilities and Tools Introduced at Build 2025," May 2025. [Online]. Available: https://blogs.windows.com/windowsdeveloper/2025/05/19/advancing-windows-for-ai-development-new-platform-capabilities-and-tools-introduced-at-build-2025/

[21] Windows News AI, "Windows 12 CorePC: Modular OS, On-Device AI, and the Future of Windows," 2025. [Online]. Available: https://windowsnews.ai/article/windows-12-corepc-modular-os-on-device-ai-and-the-future-of-windows.403981

[22] Financial Content / Token Ring, "Windows Reborn: Microsoft Moves Copilot into the Kernel, Launching the Era of the AI-Native OS," Jan. 2026. [Online]. Available: https://markets.financialcontent.com/wral/article/tokenring-2026-1-1-windows-reborn-microsoft-moves-copilot-into-the-kernel-launching-the-era-of-the-ai-native-os

[23] Apple Machine Learning Research, "Apple Intelligence Foundation Language Models Tech Report 2025," 2025. [Online]. Available: https://machinelearning.apple.com/research/apple-foundation-models-tech-report-2025

[24] Apple Machine Learning Research, "Updates to Apple's On-Device and Server Foundation Language Models," 2025. [Online]. Available: https://machinelearning.apple.com/research/apple-foundation-models-2025-updates

[25] Apple Machine Learning Research, "Introducing Apple's On-Device and Server Foundation Models," 2024. [Online]. Available: https://machinelearning.apple.com/research/introducing-apple-foundation-models

[26] Google Developers, "Gemini Nano: AI System Service for Android," Android Developers Documentation, 2025. [Online]. Available: https://developer.android.com/ai/gemini-nano

[27] Google Developers, "Overview of the ML Kit GenAI APIs," Google for Developers, 2025. [Online]. Available: https://developers.google.com/ml-kit/genai

[28] Z. Mei, Y. Ding, S. Cheng, X. Liao, and Z. Xu, "AIOS: LLM Agent Operating System," *Conference on Language Modeling (COLM)*, 2025. arXiv:2403.16971.

[29] MemOS Team, "MemOS: An Operating System for Memory-Augmented Generation (MAG) in Large Language Models," arXiv:2505.22101, May 2025.

[30] MemTensor Team, "MemOS: AI Memory OS for LLM and Agent Systems," arXiv:2507.03724, Jul. 2025.


---

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
(~20 person-years of effort for 8,700 lines of C (plus 600 lines of assembler) [III-3]). This is the correct
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
RFC 6962 Merkle tree structures. The Merkle tree approach provides compact inclusion (448-byte proofs at 10,000 log entries)
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
overhead for LLM inference within an NVIDIA GPU TEE is below 7 percent for typical queries relative to
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


---

# Part IV: Formal Foundations

## The Differentiator

The architecture described in Parts II and III — an AI control plane atop a conventional kernel substrate, with a watchdog mechanism, agent state model, and security isolation tiers — risks reduction to an elaborate metaphor without a formal foundation. Any sufficiently sophisticated orchestration framework layered over containers and Kubernetes can be described in similar terms. What distinguishes AIOS-WySE from an architecture document is the following claim, which this Part argues is both precise and testable: the interface between the AI control plane and the kernel substrate is a morphism, the quality of that morphism is continuously measurable at runtime via two orthogonal scalar metrics, and the safety of the entire system can be enforced by a monitor whose correctness is independently verifiable because it evaluates only those two scalars against configurable thresholds.

This formalism is not decorative. It is load-bearing in four ways. It defines the interface contract (the morphism h, Section 13.1). It specifies what correctness means at runtime (morphism quality, Sections 13.2-13.3). It grounds the safety mechanism in something simpler than and independent of the AI control plane it monitors (the Circuit Breaker, Section 13.4). And it extends naturally to composed multi-agent systems in a way that is algebraically consistent (composition morphisms, Section 13.5). Without this structure, the architecture reduces to: run LLMs in containers under Kubernetes. This Part makes the case that it need not.

---

## Section 13: Morphism-Grounded Interface Specification

### 13.1 The Wymore Formalism for System Interfaces

The formal substrate for the interface contract is Wymore's model-based systems engineering formalism [1], extended in the WySE Metamodel [2] and operationalized in the author's concurrent work on isomorphic patterns in systems engineering [3]. The formalism provides a mathematically precise definition of a system as an input-output structure with explicit state, transition, and readout components.

**Definition 1 (Wymore System).** A *system* is a tuple

    Z = (X, Y, S, T, Omega, delta, lambda)

where:

- X is the *input set* — the set of all admissible input values
- Y is the *output set* — the set of all observable output values
- S is the *state set* — all distinguishable internal configurations of the system
- T is the *time base* — either the reals (continuous time) or the integers (discrete time)
- Omega is the set of *admissible input segments*, where each omega: T -> X is a function defining how inputs vary over time
- delta: S x Omega -> S is the *state transition function*, mapping an initial state and an input segment to the successor state
- lambda: S -> Y is the *readout function*, mapping each state to an observable output

This formalism is deliberately general. It does not prescribe implementation technology, programming language, or deployment substrate. A conventional Unix kernel, an LLM-based control plane, and a hardware interrupt controller are all systems in the sense of Definition 1. The formalism's value lies precisely in this generality: it provides a vocabulary for specifying what it means for two systems to be compatible, and for measuring how faithfully one system represents another.

**Remark 1.** The Wymore tuple used in CBTO [4] and in the isomorphism library [3] employs a five-tuple notation Z = (S, I, O, N, R) that suppresses the time base T and input segment set Omega for compactness. The seven-tuple of Definition 1 is the complete form. Throughout this Part, both notations are used interchangeably, with context making clear which components are in scope.

**Definition 2 (Kernel System).** The conventional kernel substrate is modeled as

    Z_k = (X_k, Y_k, S_k, T, Omega_k, delta_k, lambda_k)

where the components are interpreted as follows:

- X_k is the *kernel input set*, comprising: system calls from user-space processes, hardware interrupt signals, timer expiration events, I/O completion notifications, and memory management unit fault signals
- Y_k is the *kernel output set*, comprising: scheduling decisions (which process runs next, for how long), memory allocation results (virtual address ranges, physical frame assignments), I/O operation results (bytes transferred, error codes), security verdict signals (syscall allowed, capability granted or denied), and process lifecycle events (fork results, exit statuses, signal deliveries)
- S_k is the *kernel state set*, comprising: the process table (PID, state, priority, resource limits), page tables and physical frame allocator state, file descriptor tables per process, device driver state registers, scheduler run queues (for each scheduling class and CPU), cgroup hierarchy with per-node resource counters, and security label assignments (SELinux contexts, Landlock capability sets)
- delta_k is the kernel's *state transition function* — for a conventional kernel, this function is deterministic: given an initial state and a system call, the successor state is determined (modulo hardware non-determinism in interrupt timing, which can be modeled as part of the input segment)
- lambda_k is the kernel's *readout function*, mapping each kernel state to the set of observable outputs presented to user-space processes and hardware peripherals

**Remark 2.** The determinism of delta_k is architecturally significant. It is what allows the kernel substrate to serve as a trusted reference in the morphism framework. A non-deterministic kernel transition function would prevent the state mapping h_S from being verified, because the same AI control plane decision could produce different kernel behaviors on successive executions.

**Definition 3 (AI Control Plane System).** The AI-native control plane is modeled as

    Z_ai = (X_ai, Y_ai, S_ai, T, Omega_ai, delta_ai, lambda_ai)

where:

- X_ai is the *control plane input set*, comprising: agent requests (task submissions, resource requests, tool invocations), resource availability and contention signals from the kernel upward API, operator commands and policy updates, tool execution results returned through MCP or A2A interfaces, model inference outputs (completions, structured responses, chain-of-thought traces), and security alerts from anomaly detection subsystems
- Y_ai is the *control plane output set*, comprising: policy decisions (scheduling hints, resource allocation verdicts, access control decisions, agent priority adjustments), orchestration commands to agent runtimes (launch, pause, checkpoint, terminate), resource hints to the kernel downward API (memory reservation requests, scheduling class assignments, CPU affinity hints), and audit log entries (immutable records of policy decisions and their rationale)
- S_ai is the *control plane state set*, comprising: the agent registry (enrolled agent identifiers, types, trust classes, isolation tier assignments), per-agent state models (execution context, episodic memory, semantic memory indices, goal decompositions, resource bindings — see Section 10), the model inventory (loaded model weights, version attestations, performance histories), the active policy rule base (current scheduling policies, access control rules, resource limits), and the performance history store (historical morphism quality measurements for trend analysis)
- delta_ai is the control plane's *state transition function* — critically, this function is **nondeterministic** due to foundation model inference. For a given control plane state and input, the successor state is a distribution over states, not a single state. This is the fundamental architectural asymmetry between Z_k and Z_ai.
- lambda_ai is the control plane's *readout function*, mapping control plane states to the policy decisions and commands that constitute its observable output

**Remark 3.** The nondeterminism of delta_ai is not a bug; it is the source of the AI control plane's adaptability. However, it precludes the use of delta_ai in formal verification at the level of individual transitions. This constraint directly motivates the morphism quality framework of Sections 13.2-13.3: rather than verifying individual transitions, the framework monitors the aggregate quality of the control plane's model of the kernel over time.

**Definition 4 (Interface Morphism).** The *interface* between the AI control plane and the kernel substrate is a morphism

    h: Z_ai -> Z_k

defined by three component maps:

- h_X: X_ai -> X_k — the *downward API*: maps AI control plane policy decisions and commands to kernel inputs (the set of structured kernel primitives the control plane may invoke, as specified in Section 9.2)
- h_Y: Y_k -> Y_ai — the *upward API*: maps kernel output signals to control plane inputs (the structured event stream the kernel presents to the control plane, as specified in Section 9.3)
- h_S: S_ai -> S_k — the *state correspondence map*: maps each element of the AI control plane's internal state to the corresponding element of the kernel state it represents

The morphism h is the **interface specification**. It is the formal object that must be designed (Section 9), implemented (as the concrete API defined in Section 9.2-9.3 and Appendix D), verified (in the sense that h_X and h_Y are well-typed and h_S is sound at system initialization), and monitored at runtime (in the sense that the quality of h_S is tracked continuously, as formalized in Section 13.2).

**Remark 4.** The morphism h is not required to be an isomorphism — perfect bijective correspondence between Z_ai and Z_k would require the AI control plane to maintain an exact replica of every kernel state variable, which is both impractical and unnecessary. What is required is that h be a faithful-enough homomorphism that the AI control plane's policy decisions, when translated through h_X, reliably produce the intended kernel behaviors. Formalizing "faithful enough" is the purpose of the morphism quality metrics S_a and C_r.

### 13.2 Structural Morphism Quality (S_a)

The structural quality metric captures the fidelity of the AI control plane's model of kernel state — specifically, how accurately h_S maps control plane state representations to the kernel states they are intended to represent.

**Definition 5 (Degree of Homomorphism).** Following [3], the *degree of homomorphism* of a component map h_S: S_ai -> S_k is:

    sigma(h_S) = (1 / |S_k|) * sum_{j=1}^{|S_k|} [ 1 / |h_S^{-1}(s_j)| ]

where h_S^{-1}(s_j) denotes the preimage of kernel state element s_j under h_S — that is, the set of control plane state elements that h_S maps to s_j.

**Definition 6 (Structural Morphism Quality).** The *structural morphism quality* of the interface morphism h is:

    S_a = sigma(h_S)

When h_S is a bijection (one-to-one and onto), each preimage has cardinality 1, and sigma = 1. When h_S is many-to-one (the AI control plane conflates distinct kernel states), preimage cardinalities exceed 1, and sigma < 1. The metric is bounded: sigma in (0, 1].

**Operational interpretation for AI-OS.** The structural quality metric has a direct runtime interpretation:

- S_a = 1.0: The AI control plane's state model perfectly tracks the kernel's actual state. Every kernel state distinction that matters for policy decisions is represented in the control plane's model. (Unachievable in practice due to unavoidable measurement latency and abstraction.)
- S_a in [0.9, 1.0): The control plane tracks kernel state accurately. Minor staleness or abstraction is within engineering tolerance. Normal operating range.
- S_a in [0.7, 0.9): The control plane's model is moderately stale or abstracted. Policy decisions based on this state are less reliable. Warning threshold (Caution state in the Circuit Breaker).
- S_a < 0.7 (configurable threshold theta_S): The control plane is operating on a significantly stale or incorrect model of kernel state. Policy decisions may be actively harmful — scheduling decisions based on stale resource data may overcommit resources, and access control decisions based on stale security labels may misclassify agent capabilities. Trip threshold.

**Drift detection.** S_a declining monotonically over successive measurement windows is the signature of drift: the kernel's actual state is evolving (due to workload changes, new agent activity, hardware events) faster than the AI control plane's model can track. Drift is distinct from episodic degradation (sudden drop due to a specific event) and is addressed with different recovery procedures (re-synchronization of the state model versus fallback and restart).

**Measurability.** S_a is computable at runtime via the following procedure: at interval tau (configurable; default 100ms for rapid response or 1s for low-overhead operation), sample a subset of kernel state variables (from the process table, memory allocator, cgroup counters, and scheduler queues); query the AI control plane's internal state model for its representation of those same variables; compute sigma(h_S) over the sampled state elements. The computational complexity of this procedure is O(|sample|) per monitoring cycle, where |sample| is the number of kernel state elements sampled.

**Extension to non-state components.** The degree of homomorphism can be computed independently for h_X (input mapping cardinality) and the implied h_Y mapping. A composite structural quality metric that averages sigma across all three component maps provides a more complete characterization but requires richer instrumentation. The single-axis formulation (h_S only) is the minimum tractable measurement for the AI-OS runtime context.

### 13.3 Behavioral Morphism Quality (C_r)

The behavioral quality metric captures whether the AI control plane's policy decisions, when executed through h_X, produce the outcomes the control plane predicted. It measures the gap between expected and observed system behavior rather than the gap between state representations.

**Definition 7 (Output Distance).** The *output distance* between the control plane's predicted kernel behavior and the kernel's actual behavior is:

    D = max_{t in T_window} || y_predicted(t) - y_actual(t) ||

where T_window is the current monitoring window, y_predicted(t) in Y_k is the output the AI control plane predicted the kernel would produce at time t given the policy decisions issued, and y_actual(t) in Y_k is the output the kernel actually produced. The norm is the L-infinity norm over the relevant output dimensions (scheduling latency, memory allocation success rate, I/O throughput, security verdict distribution).

**Definition 8 (Behavioral Morphism Quality).** The *behavioral morphism quality* of the interface morphism h is:

    C_r = 1 - D / D_max

where D_max is a domain-specific normalization constant (the maximum tolerable output distance, set at system configuration time). C_r in [0, 1], with C_r = 1 corresponding to perfect prediction accuracy (D = 0) and C_r = 0 corresponding to maximally wrong predictions (D = D_max).

**Operational interpretation for AI-OS.** The behavioral quality metric has the following interpretation:

- C_r = 1.0: Every AI policy decision produces exactly the predicted kernel behavior. Unachievable in practice due to inherent kernel nondeterminism in interrupt timing and hardware variability.
- C_r in [0.9, 1.0): AI policy decisions are effective with minor deviations. Normal operating range.
- C_r in [0.8, 0.9): AI policy decisions are producing measurable deviations from predicted outcomes. The control plane's model of kernel dynamics is degrading. Warning threshold (Caution state).
- C_r < 0.8 (configurable threshold theta_C): AI decisions are consistently producing unexpected kernel outcomes. This may indicate that the workload's characteristics have shifted beyond the control plane's training distribution, that the kernel's behavior has changed (e.g., due to a kernel update or hardware configuration change), or that the control plane's model of system dynamics is fundamentally incorrect for the current operating context. Trip threshold.

**The orthogonality of S_a and C_r.** The two metrics are analytically independent, as established in [3]. This orthogonality has operational consequences:

1. High S_a, low C_r: The AI control plane has an accurate, up-to-date model of the kernel's current state, but its predictions about the effect of its policy decisions are wrong. This indicates a dynamics model failure — the control plane understands where the system is but not where it will go in response to its commands. Likely cause: workload characteristics or hardware performance have shifted outside the distribution used to train the dynamics model.

2. Low S_a, high C_r: The AI control plane's model of kernel state is coarse or stale, but despite this, its policy decisions are producing correct outcomes. This is a benign case: the control plane is "getting the right answer for the wrong reason." However, it is a warning that the control plane's policy effectiveness is fragile — a small environmental change could simultaneously collapse C_r.

3. Both declining: The control plane is losing fidelity on both axes simultaneously. This is the most serious case and typically indicates either a rapid environmental change (new workload pattern, hardware fault) or a systematic failure in the monitoring and update pipeline.

4. Neither declining: Normal operation. The morphism h is maintaining adequate quality.

**Remark 5.** The normalization D / D_max in Definition 8 converts the scale-dependent output distance D into a scale-independent quality score. This is important for two reasons: it allows C_r and S_a to be compared directly (both are dimensionless, in [0,1]), and it allows the composite trust score K_trust = f(S_a, C_r) to be computed without arbitrary weighting of incommensurable quantities.

### 13.4 The Circuit Breaker as Watchdog

Section 12.4 formulated the watchdog problem: a monitor for an AI control plane cannot itself be AI-based without creating infinite regress, but a purely conventional timer-based watchdog cannot detect the substantive failures (wrong policy decisions, stale state models) that are most dangerous in an AI-OS context. The Circuit Breaker resolves this by monitoring precisely the morphism quality metrics (S_a, C_r) that characterize these substantive failures, using a monitoring mechanism simple enough for independent formal verification.

**Definition 9 (Circuit Breaker).** The *Circuit Breaker* is a runtime monitor M defined by a state machine with state set {CLOSED, OPEN, HALF-OPEN}, operating on the two real-valued inputs (S_a(t), C_r(t)) and the configurable parameters (theta_S, theta_C, T_cooldown, T_validation), where:

- theta_S in (0, 1) is the structural quality trip threshold
- theta_C in (0, 1) is the behavioral quality trip threshold
- T_cooldown > 0 is the minimum time the breaker remains OPEN before attempting recovery
- T_validation > 0 is the time the breaker must observe stable metrics in HALF-OPEN before transitioning to CLOSED

The state transitions of M are:

    CLOSED -> OPEN if (S_a(t) < theta_S) OR (C_r(t) < theta_C)
    OPEN -> HALF-OPEN after T_cooldown has elapsed
    HALF-OPEN -> CLOSED if (S_a(t) >= theta_S) AND (C_r(t) >= theta_C) for duration T_validation
    HALF-OPEN -> OPEN if (S_a(t) < theta_S) OR (C_r(t) < theta_C)

When M enters OPEN, the AI control plane is disabled and the system transitions to Conventional Fallback Mode (Section 12.3). When M is HALF-OPEN, the AI control plane processes a limited workload under enhanced monitoring. When M is CLOSED, the AI control plane operates normally.

**Why the Circuit Breaker resolves the infinite regress.** The regress arises when an AI monitor monitors an AI control plane, because the monitor itself may fail in AI-specific ways (wrong predictions, stale models, hallucinated assessments). The Circuit Breaker avoids this by construction:

1. It evaluates two scalar metrics against numeric thresholds. No foundation model inference, no LLM calls, no semantic reasoning. The transition function of M is a finite-state machine with two real-valued guard conditions and one time-delay guard. Its correctness can be established by inspection and verified by model checking.

2. It observes system metrics — kernel state samples and measured output distances — that are independent of the AI control plane's self-reported state. The control plane cannot misrepresent S_a or C_r by manipulating its own outputs, because those metrics are computed from kernel-observable ground truth.

3. It executes at higher privilege than the AI control plane. The Circuit Breaker is a kernel module or hypervisor component, not a user-space process that the AI control plane could schedule, throttle, or terminate.

4. Its failure modes are a strict subset of conventional software failure modes: process crash, memory corruption, timer failure. Each of these failure modes is handled by well-understood mechanisms (watchdog timer, memory protection, hardware timer redundancy) that have been in production use for decades.

**SHACL trip conditions.** The Circuit Breaker's trip thresholds are expressed as SHACL constraints in the CBTO, enabling configuration validation and governance audit [4]. The following shape enforces that any active CircuitBreaker instance has valid threshold parameters and that the current morphism quality is above the warning floor:

```turtle
@prefix sh: <http://www.w3.org/ns/shacl#> .
@prefix cb: <http://circuitbreaker.ontology/trust#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

cb:CircuitBreakerShape a sh:NodeShape ;
    sh:targetClass cb:CircuitBreaker ;
    sh:property [
        sh:path cb:structuralTripThreshold ;
        sh:minInclusive "0.5"^^xsd:decimal ;
        sh:maxInclusive "0.95"^^xsd:decimal ;
        sh:datatype xsd:decimal ;
        sh:severity sh:Violation ;
        sh:message "Structural trip threshold theta_S must be in [0.5, 0.95]." ;
    ] ;
    sh:property [
        sh:path cb:behavioralTripThreshold ;
        sh:minInclusive "0.5"^^xsd:decimal ;
        sh:maxInclusive "0.95"^^xsd:decimal ;
        sh:datatype xsd:decimal ;
        sh:severity sh:Violation ;
        sh:message "Behavioral trip threshold theta_C must be in [0.5, 0.95]." ;
    ] ;
    sh:property [
        sh:path cb:currentBreakerState ;
        sh:in ( cb:Normal cb:Caution cb:Restrict cb:Halt cb:Lockdown ) ;
        sh:severity sh:Violation ;
        sh:message "Circuit Breaker state must be a member of the defined state enumeration." ;
    ] .

cb:MorphismQualityAssertionShape a sh:NodeShape ;
    sh:targetClass cb:MorphismMapping ;
    sh:property [
        sh:path ( cb:hasStructuralQuality cb:sigmaValue ) ;
        sh:minInclusive "0.0"^^xsd:decimal ;
        sh:maxInclusive "1.0"^^xsd:decimal ;
        sh:datatype xsd:decimal ;
        sh:severity sh:Violation ;
        sh:message "Structural quality sigma must be in [0.0, 1.0]." ;
    ] ;
    sh:property [
        sh:path ( cb:hasBehavioralQuality cb:outputDistance ) ;
        sh:minInclusive "0.0"^^xsd:decimal ;
        sh:datatype xsd:decimal ;
        sh:severity sh:Violation ;
        sh:message "Output distance D must be non-negative." ;
    ] ;
    sh:property [
        sh:path ( cb:hasStructuralQuality cb:sigmaValue ) ;
        sh:minInclusive "0.7"^^xsd:decimal ;
        sh:severity sh:Warning ;
        sh:message "Structural quality sigma below warning threshold 0.7 — monitor for drift." ;
    ] .
```

**The graduated response model.** The CBTO's cb:BreakerState enumeration [4] extends the three-state machine of Definition 9 to a five-state graduated response: Normal, Caution, Restrict, Halt, Lockdown. This extension maps S_a and C_r to intermediate response levels before a full trip, enabling proportional response:

- Normal: (S_a >= 0.9) AND (C_r >= 0.9). No restrictions on AI control plane operation.
- Caution: (S_a in [0.8, 0.9)) OR (C_r in [0.8, 0.9)). AI control plane continues operating; enhanced monitoring frequency; operator notification issued.
- Restrict: (S_a in [0.7, 0.8)) OR (C_r in [0.7, 0.8)). AI control plane continues operating for existing workloads; new high-risk policy decisions require operator confirmation.
- Halt: (S_a < 0.7) OR (C_r < 0.7). AI control plane disabled; system enters Conventional Fallback Mode.
- Lockdown: Halt condition persisted for more than T_lockdown without successful recovery. All AI control plane activity disabled; requires manual operator clearance and full state re-synchronization before resumption.

The specific threshold values (0.7, 0.8, 0.9) are defaults. System operators configure thresholds appropriate to their deployment context (safety-critical systems will use tighter thresholds; research deployments may use looser ones). SHACL constraints validate that operator-configured thresholds fall within engineering-approved ranges.

### 13.5 Composition Correctness via Morphism Composition

The single-agent morphism framework of Sections 13.1-13.4 applies when one AI control plane interacts with one kernel substrate. The multi-agent case requires composing morphisms.

**The composition problem.** When agent A delegates a subtask to agent B, both agents interact with the same kernel substrate. Agent A's morphism h_A: Z_A -> Z_k expresses A's interface with the kernel. Agent B's morphism h_B: Z_B -> Z_k expresses B's interface. The composed system (A operating through B) must maintain adequate morphism quality with the shared substrate, but the composition of A's and B's state models, decision pipelines, and output functions introduces additional error that is not captured by monitoring h_A or h_B in isolation.

**Definition 10 (Agent Composition Morphism).** Let Z_A and Z_B be Wymore systems for agents A and B respectively, both mapped to the same kernel system Z_k. The *composed system* (A, B) is a Wymore system Z_AB with:

- State set S_AB = S_A x S_B (the product of the individual agent state sets, augmented with shared state that both agents can read and write)
- Input set X_AB = X_A union X_B minus X_shared, where X_shared are inputs consumed internally in the delegation protocol
- Output set Y_AB: the outputs of the composition (A's terminal outputs, since B's outputs are consumed as inputs to A)
- Transition function delta_AB derived from the composition of delta_A and delta_B through the delegation protocol

The *composition morphism* is h_AB: Z_AB -> Z_k.

**Definition 11 (Composition Correctness Criterion).** The composed morphism h_AB satisfies the *composition correctness criterion* if:

    S_a(h_AB) >= min(S_a(h_A), S_a(h_B)) - epsilon_c
    C_r(h_AB) >= min(C_r(h_A), C_r(h_B)) - epsilon_c

where epsilon_c in [0, 0.1] is a configurable *composition tolerance* — the permissible degradation in morphism quality introduced by the act of composition itself.

**Theorem 1 (Morphism Quality Bound under Composition).** If h_A and h_B are homomorphisms from Z_A and Z_B to Z_k respectively, and the shared state S_AB is accessed under a protocol that preserves consistency (no concurrent writes without a linearizable lock), then the composition morphism h_AB satisfies:

    sigma(h_AB) <= min(sigma(h_A), sigma(h_B))

That is, the structural quality of the composition cannot exceed the structural quality of the weaker component morphism. The bound is tight: composition can only add mapping imprecision, never remove it.

*Proof sketch.* The state mapping h_{AB,S}: S_AB -> S_k factors through the individual state mappings h_{A,S}: S_A -> S_k and h_{B,S}: S_B -> S_k. Any kernel state element s_k that is in the preimage of h_{A,S} at cardinality c_A and in the preimage of h_{B,S} at cardinality c_B has preimage cardinality at least max(c_A, c_B) under h_{AB,S} (since S_AB = S_A x S_B, the product state space can conflate at least as many distinct kernel states as either component). The degree of homomorphism sigma(h_AB) therefore satisfies sigma(h_AB) <= min(sigma(h_A), sigma(h_B)). Consistency of shared state access (no concurrent write conflicts) ensures the bound is not further degraded by race conditions. []

**Remark 6.** Theorem 1 establishes a chain of morphism quality degradation: composition can never improve morphism fidelity and may worsen it. This has a direct operational implication: deep agent delegation chains (A delegates to B, B delegates to C, C delegates to D) are subject to progressive morphism quality degradation, placing a practical engineering limit on the depth of delegation in a morphism-governed system. This limit is enforced by the composition correctness criterion (Definition 11): the OS governance layer rejects delegation requests that would produce a composed morphism below the threshold.

**Violation responses.** When the composition correctness criterion is violated — that is, when the measured quality of the composed morphism falls below the individual component qualities minus the tolerance — the following responses are available in increasing order of severity:

1. *Re-synchronization*: force both agents to refresh their state models from the kernel (re-compute h_A and h_B), then re-attempt the composition. Appropriate when the violation is transient (due to a brief period of high kernel activity or measurement noise).

2. *Rollback*: undo the effects of the delegated subtask, return the system to the state before delegation was initiated, and issue an operator notification. Appropriate when re-synchronization fails or the violation exceeds a configurable magnitude.

3. *Decomposition*: restructure the delegated task so that A and B interact with non-overlapping regions of the kernel state, then monitor h_A and h_B independently. Appropriate when the shared state in S_AB is the source of composition degradation.

4. *Escalation*: present the task to a human operator for direct execution. Appropriate when the delegated task is safety-critical and no automated recovery is viable.

**Category-theoretic structure.** The composition framework has a natural categorical interpretation. Let C_k be the category whose objects are Wymore system models and whose morphisms are the homomorphisms h: Z_i -> Z_k for various i. Morphism composition in this category is associative (delegation chains compose correctly) and the identity morphism exists (the kernel's own identity map). The composition correctness criterion (Definition 11) is then a quality-preserving functor condition: it requires that any endofunctor on C_k induced by agent delegation preserve morphism quality within epsilon_c. This categorical structure is noted here as a foundation for future work; it is not operationally required for the AI-OS implementation but provides the theoretical basis for extending the framework to distributed multi-kernel deployments.

**Connection to DARPA CLARA.** The DARPA CLARA program requires "Compositional Learning-And-Reasoning with verifiable quality bounds" [5]. The morphism composition framework of this section is precisely this: compositional in the sense that Definition 10 defines the composed system formally; learning-and-reasoning in the sense that the component agents Z_A and Z_B may employ any AI method (LLM, RL, symbolic reasoning, neural-symbolic hybrid); verifiable in the sense that the composition correctness criterion (Definition 11) is testable at runtime via the same morphism quality measurement infrastructure used for single-agent monitoring; and with quality bounds in the sense that Theorem 1 establishes a monotone degradation guarantee.

The CLARA program's specific metric requirements map as follows:

- *Verifiability without performance loss*: S_a and C_r are computed in O(|sample|) per monitoring cycle, adding negligible latency relative to the AI control plane's decision cycle. The monitoring overhead does not require throttling the control plane.
- *Multiplicity of AI Kinds*: the morphism framework is AI-kind-agnostic. It monitors the quality of the mapping between the AI's behavior and the kernel's ground truth, regardless of whether the AI uses gradient-based learning, symbolic rule evaluation, Bayesian inference, or any combination.
- *Polynomial-time complexity*: sigma(h_S) computation is O(|S_k|) in the worst case (full state enumeration); in practice, sampled estimation runs in O(|sample|) << O(|S_k|).
- *Composed task reliability > SOA*: C_r(h_AB) > C_r(baseline) is the directly testable criterion, where baseline is the behavioral morphism quality of a conventional non-AI scheduling policy.

### 13.6 Summary of Formal Contributions

The following table summarizes the formal constructs introduced in this Part, the aspects of the AI-OS design they formalize, and the design elements they enable.

| Formal Construct | What It Formalizes | Enabled Design Element |
|---|---|---|
| Z_k (Definition 2) | Conventional kernel substrate as Wymore tuple | Trusted reference for all morphism measurements |
| Z_ai (Definition 3) | AI control plane as Wymore tuple with nondeterministic delta_ai | Intelligence layer with acknowledged behavioral uncertainty |
| h: Z_ai -> Z_k (Definition 4) | AI-kernel interface as morphism with component maps h_X, h_Y, h_S | Interface contract: downward API + upward API + state correspondence |
| sigma(h_S) (Definition 5) | Degree of homomorphism of state map | S_a: runtime structural quality metric, continuously measurable |
| S_a (Definition 6) | Structural morphism quality | Drift detection, state model reliability assessment |
| D (Definition 7) | Output distance between predicted and actual kernel behavior | C_r: runtime behavioral quality metric, continuously measurable |
| C_r (Definition 8) | Behavioral morphism quality | Policy effectiveness monitoring |
| Circuit Breaker M (Definition 9) | FSM watchdog on (S_a, C_r) with SHACL trip conditions | Safety mechanism: simpler than and independent of AI control plane |
| Z_AB (Definition 10) | Multi-agent composed system | Formal foundation for delegation protocol governance |
| h_AB (Definition 10) | Composition morphism | Interface contract for multi-agent delegation |
| Composition criterion (Definition 11) | Quality-preserving delegation | Enforcement of delegation depth limits and quality bounds |
| Theorem 1 | Monotone quality degradation under composition | Formal basis for rejecting deep delegation chains |

---

## Section 14: Ontological Grounding

### 14.1 CBTO as the OS Governance Ontology

The Circuit Breaker Trust Ontology (CBTO, Design Specification v4.0 [4]) was designed for a different primary application domain: monitoring the morphism quality between an autonomous AI agent and a physical system it models and controls. However, the CBTO's architecture is deliberately domain-agnostic at the TBox level — it formalizes Wymore tuples, morphism mappings, quality metrics, and circuit breaker states as abstract ontological structures, with domain-specific content confined to the ABox. This makes the CBTO directly reusable as the governance ontology for the AI-OS domain.

**CBTO inventory directly applicable to AI-OS.**

The following CBTO classes and properties apply without modification to the AI-OS context:

| CBTO Entity | Original Purpose | AI-OS Reuse |
|---|---|---|
| cb:SystemModel | Represents a Wymore Z tuple | Models Z_k and Z_ai |
| cb:ReferenceSystemModel | The physical system Z_real | The kernel system Z_k (deterministic reference) |
| cb:AgentSystemModel | The AI's model Z_ai | The AI control plane's model of the kernel |
| cb:MorphismMapping | The mapping h: Z_ai -> Z_real | The interface morphism h: Z_ai -> Z_k |
| cb:StructuralQuality | Sigma — degree of homomorphism | S_a metric for AI-OS |
| cb:BehavioralQuality | D — output distance | C_r metric for AI-OS |
| cb:BreakerState | {Normal, Caution, Restrict, Halt, Lockdown} | Circuit Breaker states for AI-OS |
| cb:MorphismMappingShape | SHACL shape for morphism structural preconditions | Directly applicable to h_X, h_Y, h_S validation |
| cb:FederatedGraphNode | Distributed ontology topology | Distributed AI-OS deployments with multiple kernel nodes |
| prov:Activity (via PROV-O) | Audit trail for AI decisions | Audit trail for AI control plane policy decisions |

**CBTO gaps for the AI-OS domain.** The CBTO was designed for a single AI agent monitoring a single physical system. The AI-OS domain introduces requirements not present in that application context:

1. Agent state as a managed OS resource — the CBTO has no class for the structured multi-component agent state described in Section 10 (execution context, episodic memory, semantic memory, goal state, resource bindings).

2. Resource binding as a kernel-managed object — the CBTO does not model the binding between an agent and hardware resources (CPU quota, GPU memory partition, network bandwidth share), because in its original context the AI agent is external to the infrastructure it monitors.

3. Scheduling policy as an ontological entity — the CBTO has no formal representation of scheduling policy, because in its original context the AI agent emits recommendations but does not directly govern scheduling.

4. Interface contract as a named, versioned artifact — the CBTO's MorphismMapping class represents the mapping h but not the full interface specification (the typed API with version semantics, backward compatibility constraints, and deprecation policies) described in Section 9.

5. Composition morphism — the CBTO is designed for a single morphism h: Z_ai -> Z_real. The composition morphism h_AB: Z_AB -> Z_k of Section 13.5 requires a new class.

**Proposed CBTO extensions for AI-OS.** The following OWL 2 DL additions address the five gaps. They are proposed as a separate ontology module (namespace prefix `aios:`) that imports the CBTO:

```turtle
@prefix aios: <http://aios-wyse.ontology/os#> .
@prefix cb:   <http://circuitbreaker.ontology/trust#> .
@prefix obo:  <http://purl.obolibrary.org/obo/> .
@prefix owl:  <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .

<http://aios-wyse.ontology/os#> a owl:Ontology ;
    owl:imports <http://circuitbreaker.ontology/trust#> ;
    rdfs:label "AIOS-WySE OS Governance Ontology"@en ;
    rdfs:comment "OWL 2 DL module extending CBTO for AI-native operating system governance.
        Defines agent state, resource binding, scheduling policy, interface contract,
        and composition morphism as OS-specific ontological entities."@en .

# ----------------------------------------------------------------
# Gap 1: Agent state as a managed OS resource
# ----------------------------------------------------------------

aios:AgentState a owl:Class ;
    rdfs:subClassOf obo:BFO_0000031 ;
    rdfs:label "Agent State"@en ;
    rdfs:comment "The cognitive and computational state of an AI agent managed by the OS.
        A Generically Dependent Continuant: information content that describes
        the agent's current configuration across all state categories."@en .

aios:ExecutionContext a owl:Class ;
    rdfs:subClassOf aios:AgentState ;
    rdfs:label "Execution Context"@en ;
    rdfs:comment "The agent's current task assignment, tool bindings, in-flight function
        call stack, and pending I/O operations. Volatile; lost on agent restart."@en .

aios:EpisodicMemory a owl:Class ;
    rdfs:subClassOf aios:AgentState ;
    rdfs:label "Episodic Memory"@en ;
    rdfs:comment "The agent's recent interaction history, KV cache contents, and
        session-scoped working memory. Persistence policy: configurable per agent
        class (volatile, checkpoint-on-eviction, or persistent)."@en .

aios:SemanticMemory a owl:Class ;
    rdfs:subClassOf aios:AgentState ;
    rdfs:label "Semantic Memory"@en ;
    rdfs:comment "Retrieved facts, RAG index pointers, learned associations, and
        model-specific embedding cache references. Persistence policy: persistent
        with versioned consistency semantics."@en .

aios:GoalState a owl:Class ;
    rdfs:subClassOf aios:AgentState ;
    rdfs:label "Goal State"@en ;
    rdfs:comment "The agent's current objectives, subgoal decomposition tree, pending
        commitments to other agents, and completion criteria. Persistence policy:
        persistent; must survive agent checkpoint and restore."@en .

aios:hasAgentState a owl:ObjectProperty ;
    rdfs:domain cb:AgentSystemModel ;
    rdfs:range aios:AgentState ;
    rdfs:label "has agent state"@en .

aios:hasExecutionContext a owl:ObjectProperty ;
    rdfs:subPropertyOf aios:hasAgentState ;
    rdfs:domain cb:AgentSystemModel ;
    rdfs:range aios:ExecutionContext ;
    rdfs:label "has execution context"@en .

aios:hasEpisodicMemory a owl:ObjectProperty ;
    rdfs:subPropertyOf aios:hasAgentState ;
    rdfs:domain cb:AgentSystemModel ;
    rdfs:range aios:EpisodicMemory ;
    rdfs:label "has episodic memory"@en .

aios:hasSemanticMemory a owl:ObjectProperty ;
    rdfs:subPropertyOf aios:hasAgentState ;
    rdfs:domain cb:AgentSystemModel ;
    rdfs:range aios:SemanticMemory ;
    rdfs:label "has semantic memory"@en .

aios:hasGoalState a owl:ObjectProperty ;
    rdfs:subPropertyOf aios:hasAgentState ;
    rdfs:domain cb:AgentSystemModel ;
    rdfs:range aios:GoalState ;
    rdfs:label "has goal state"@en .

# ----------------------------------------------------------------
# Gap 2: Resource binding as a kernel-managed object
# ----------------------------------------------------------------

aios:ResourceBinding a owl:Class ;
    rdfs:subClassOf obo:BFO_0000031 ;
    rdfs:label "Resource Binding"@en ;
    rdfs:comment "A formal allocation of kernel-managed hardware resources to a
        specific agent. Encodes the resource type, quantity, isolation tier,
        and expiration policy."@en .

aios:ResourceType a owl:Class ;
    rdfs:subClassOf obo:BFO_0000031 ;
    rdfs:label "Resource Type"@en ;
    owl:equivalentClass [ a owl:Class ;
        owl:oneOf ( aios:CPUResource aios:GPUResource aios:NPUResource
                    aios:MemoryResource aios:NetworkBandwidthResource
                    aios:StorageResource ) ] .

aios:CPUResource         a owl:NamedIndividual, aios:ResourceType .
aios:GPUResource         a owl:NamedIndividual, aios:ResourceType .
aios:NPUResource         a owl:NamedIndividual, aios:ResourceType .
aios:MemoryResource      a owl:NamedIndividual, aios:ResourceType .
aios:NetworkBandwidthResource a owl:NamedIndividual, aios:ResourceType .
aios:StorageResource     a owl:NamedIndividual, aios:ResourceType .

aios:boundToResource a owl:ObjectProperty ;
    rdfs:domain cb:AgentSystemModel ;
    rdfs:range aios:ResourceBinding ;
    rdfs:label "bound to resource"@en .

aios:hasResourceType a owl:ObjectProperty, owl:FunctionalProperty ;
    rdfs:domain aios:ResourceBinding ;
    rdfs:range aios:ResourceType ;
    rdfs:label "has resource type"@en .

aios:allocatedQuantity a owl:DatatypeProperty, owl:FunctionalProperty ;
    rdfs:domain aios:ResourceBinding ;
    rdfs:range xsd:decimal ;
    rdfs:comment "Numeric quantity allocated (interpretation depends on ResourceType:
        CPU cores, GPU memory bytes, NPU TOPS, memory bytes, Mbps, bytes)."@en .

aios:isolationTier a owl:DatatypeProperty, owl:FunctionalProperty ;
    rdfs:domain aios:ResourceBinding ;
    rdfs:range xsd:integer ;
    rdfs:comment "Isolation tier (0=in-process, 1=subprocess, 2=container,
        3=VM/TEE, 4=hardware partition) per Section 11.2."@en .

# ----------------------------------------------------------------
# Gap 3: Scheduling policy as an ontological entity
# ----------------------------------------------------------------

aios:SchedulingPolicy a owl:Class ;
    rdfs:subClassOf obo:BFO_0000031 ;
    rdfs:label "Scheduling Policy"@en ;
    rdfs:comment "A formal specification of the rules governing agent scheduling,
        resource allocation priority, and preemption behavior. Issued by the
        AI control plane; enforced by the kernel via the downward API."@en .

aios:PolicyClass a owl:Class ;
    rdfs:subClassOf obo:BFO_0000031 ;
    rdfs:label "Policy Class"@en ;
    owl:equivalentClass [ a owl:Class ;
        owl:oneOf ( aios:RealTimePolicy aios:BestEffortPolicy
                    aios:BatchPolicy aios:InteractivePolicy ) ] .

aios:RealTimePolicy    a owl:NamedIndividual, aios:PolicyClass .
aios:BestEffortPolicy  a owl:NamedIndividual, aios:PolicyClass .
aios:BatchPolicy       a owl:NamedIndividual, aios:PolicyClass .
aios:InteractivePolicy a owl:NamedIndividual, aios:PolicyClass .

aios:governedByPolicy a owl:ObjectProperty ;
    rdfs:domain cb:AgentSystemModel ;
    rdfs:range aios:SchedulingPolicy ;
    rdfs:label "governed by policy"@en .

aios:hasPolicyClass a owl:ObjectProperty, owl:FunctionalProperty ;
    rdfs:domain aios:SchedulingPolicy ;
    rdfs:range aios:PolicyClass ;
    rdfs:label "has policy class"@en .

aios:latencyBudgetMs a owl:DatatypeProperty, owl:FunctionalProperty ;
    rdfs:domain aios:SchedulingPolicy ;
    rdfs:range xsd:decimal ;
    rdfs:comment "Maximum permitted scheduling latency in milliseconds."@en .

# ----------------------------------------------------------------
# Gap 4: Interface contract as a named, versioned artifact
# ----------------------------------------------------------------

aios:InterfaceContract a owl:Class ;
    rdfs:subClassOf obo:BFO_0000031 ;
    rdfs:label "Interface Contract"@en ;
    rdfs:comment "The formal specification of the AI-Kernel interface morphism h,
        including the downward API (h_X), upward API (h_Y), state correspondence
        (h_S), version identifier, and backward compatibility guarantees."@en .

aios:hasInterfaceContract a owl:ObjectProperty, owl:FunctionalProperty ;
    rdfs:domain cb:SystemModel ;
    rdfs:range aios:InterfaceContract ;
    rdfs:label "has interface contract"@en .

aios:contractVersion a owl:DatatypeProperty, owl:FunctionalProperty ;
    rdfs:domain aios:InterfaceContract ;
    rdfs:range xsd:string ;
    rdfs:comment "Semantic version of the interface contract (e.g., '1.2.0')."@en .

aios:downwardAPIVersion a owl:DatatypeProperty, owl:FunctionalProperty ;
    rdfs:domain aios:InterfaceContract ;
    rdfs:range xsd:string ;
    rdfs:comment "Version of the downward API (AI control plane to kernel primitives)."@en .

aios:upwardAPIVersion a owl:DatatypeProperty, owl:FunctionalProperty ;
    rdfs:domain aios:InterfaceContract ;
    rdfs:range xsd:string ;
    rdfs:comment "Version of the upward API (kernel event stream to control plane)."@en .

aios:backwardCompatibleWith a owl:ObjectProperty ;
    rdfs:domain aios:InterfaceContract ;
    rdfs:range aios:InterfaceContract ;
    rdfs:label "backward compatible with"@en ;
    rdfs:comment "Asserts that this contract version is backward compatible with
        the referenced prior version — i.e., any kernel that satisfied the prior
        contract satisfies this one."@en .

# ----------------------------------------------------------------
# Gap 5: Composition morphism for multi-agent delegation
# ----------------------------------------------------------------

aios:CompositionMorphism a owl:Class ;
    rdfs:subClassOf cb:MorphismMapping ;
    rdfs:label "Composition Morphism"@en ;
    rdfs:comment "A morphism h_AB: Z_AB -> Z_k representing the composed interface
        of two agents A and B in a delegation relationship. The composition
        morphism quality must satisfy the composition correctness criterion
        (Definition 11 of Part IV)."@en .

aios:composedFromPrimary a owl:ObjectProperty, owl:FunctionalProperty ;
    rdfs:domain aios:CompositionMorphism ;
    rdfs:range cb:MorphismMapping ;
    rdfs:label "composed from primary"@en ;
    rdfs:comment "The morphism h_A: Z_A -> Z_k of the delegating agent."@en .

aios:composedFromDelegate a owl:ObjectProperty, owl:FunctionalProperty ;
    rdfs:domain aios:CompositionMorphism ;
    rdfs:range cb:MorphismMapping ;
    rdfs:label "composed from delegate"@en ;
    rdfs:comment "The morphism h_B: Z_B -> Z_k of the delegated-to agent."@en .

aios:compositionTolerance a owl:DatatypeProperty, owl:FunctionalProperty ;
    rdfs:domain aios:CompositionMorphism ;
    rdfs:range xsd:decimal ;
    rdfs:comment "Configurable tolerance epsilon_c in [0.0, 0.1] for permissible
        morphism quality degradation due to composition."@en .

aios:compositionDepth a owl:DatatypeProperty, owl:FunctionalProperty ;
    rdfs:domain aios:CompositionMorphism ;
    rdfs:range xsd:integer ;
    rdfs:comment "Depth of the delegation chain. OS governance rejects
        delegation requests that would exceed the configured maximum depth."@en .
```

### 14.2 SHACL Validation Pipeline for AI-OS Governance

The two-tier validation pattern — advisory syntax validation followed by blocking full validation — is adapted from the GI-JOE portfolio ontology enforcement gate [6] and applied to AI-OS governance.

**Tier 1 (Advisory, target < 2s).** Syntax validation verifies that all required properties are present and correctly typed. This tier runs at agent registration time, at each interface contract version change, and on any SPARQL-detectable structural anomaly. It does not block operation but issues operator notifications.

Representative Tier 1 shapes:

```turtle
aios:AgentSystemModelShape a sh:NodeShape ;
    sh:targetClass cb:AgentSystemModel ;
    sh:property [
        sh:path aios:hasExecutionContext ;
        sh:minCount 1 ;
        sh:class aios:ExecutionContext ;
        sh:severity sh:Warning ;
        sh:message "Agent system model should have an execution context — agent may not be fully initialized." ;
    ] ;
    sh:property [
        sh:path aios:hasGoalState ;
        sh:minCount 1 ;
        sh:class aios:GoalState ;
        sh:severity sh:Warning ;
        sh:message "Agent system model should have a goal state — agent purpose is unspecified." ;
    ] ;
    sh:property [
        sh:path aios:isolationTier ;
        sh:minInclusive "0"^^xsd:integer ;
        sh:maxInclusive "4"^^xsd:integer ;
        sh:severity sh:Violation ;
        sh:message "Isolation tier must be an integer in {0, 1, 2, 3, 4}." ;
    ] .

aios:InterfaceContractShape a sh:NodeShape ;
    sh:targetClass aios:InterfaceContract ;
    sh:property [
        sh:path aios:contractVersion ;
        sh:minCount 1 ;
        sh:maxCount 1 ;
        sh:datatype xsd:string ;
        sh:severity sh:Violation ;
        sh:message "Interface contract must have exactly one semantic version string." ;
    ] ;
    sh:property [
        sh:path aios:downwardAPIVersion ;
        sh:minCount 1 ;
        sh:severity sh:Violation ;
        sh:message "Interface contract must specify the downward API version." ;
    ] ;
    sh:property [
        sh:path aios:upwardAPIVersion ;
        sh:minCount 1 ;
        sh:severity sh:Violation ;
        sh:message "Interface contract must specify the upward API version." ;
    ] .

aios:CompositionMorphismShape a sh:NodeShape ;
    sh:targetClass aios:CompositionMorphism ;
    sh:property [
        sh:path aios:compositionDepth ;
        sh:maxInclusive "5"^^xsd:integer ;
        sh:severity sh:Violation ;
        sh:message "Delegation chain depth exceeds maximum permitted depth of 5." ;
    ] ;
    sh:property [
        sh:path aios:compositionTolerance ;
        sh:maxInclusive "0.1"^^xsd:decimal ;
        sh:minInclusive "0.0"^^xsd:decimal ;
        sh:severity sh:Violation ;
        sh:message "Composition tolerance epsilon_c must be in [0.0, 0.1]." ;
    ] .
```

**Tier 2 (Blocking, target < 10s).** Full validation runs at system startup, after any governance-significant event (interface contract version change, new agent class registration, security policy update), and on demand by operators. Tier 2 executes SHACL shapes plus the SPARQL competency queries defined in Section 14.2.1. A Tier 2 failure blocks the governance-significant action and requires operator resolution.

**14.2.1 Competency Questions for AI-OS Governance.** The following ten SPARQL competency questions (CQs) define the minimum governance knowledge the AIOS-WySE ontology must support. Each CQ is labeled with its domain, expected result type, and monitoring frequency.

| CQ | Domain | Question | Expected Result | Frequency |
|---|---|---|---|---|
| CQ-OS-01 | Structural | How many agents are currently registered and what is their isolation tier distribution? | Count by tier | Per registration event |
| CQ-OS-02 | Trust Metrology | Which agents have S_a below the warning threshold (0.8)? | Agent list with sigma values | Every monitoring cycle |
| CQ-OS-03 | Trust Metrology | What is the mean C_r across all active agents over the last monitoring window? | Scalar in [0,1] | Every monitoring cycle |
| CQ-OS-04 | Security | Which agents share resource bindings of the same type without an explicit sharing policy? | Binding pairs (potential isolation violations) | Every monitoring cycle |
| CQ-OS-05 | Provenance | What is the provenance chain (model weights -> attestation -> deployment) for each active model? | Provenance graph per model | Daily or on deployment |
| CQ-OS-06 | Governance | How many Circuit Breaker trip events occurred in the last 24 hours? | Integer count by breaker state transition | Daily |
| CQ-OS-07 | Architecture | Which agents are in composed configurations and what is their composition morphism quality (S_a and C_r of h_AB)? | Agent pairs with quality pair (S_a, C_r) | Every monitoring cycle |
| CQ-OS-08 | Security | Are there agents with goal states that contain objectives conflicting with system security policies (as defined in the policy rule base)? | Conflict list with policy references | Per goal state update |
| CQ-OS-09 | Resource | What is the total resource allocation across all active agents versus total available capacity, by resource type? | Utilization ratio per resource type | Every monitoring cycle |
| CQ-OS-10 | Integrity | Which models have been loaded without a valid attestation certificate linked to their ResourceBinding? | Model list with missing attestation flags | Per model load event |

Representative SPARQL implementations for CQ-OS-02 and CQ-OS-07:

```sparql
# CQ-OS-02: Agents with structural quality below warning threshold
PREFIX cb:   <http://circuitbreaker.ontology/trust#>
PREFIX aios: <http://aios-wyse.ontology/os#>

SELECT ?agent ?sigma
WHERE {
    ?morphism a cb:MorphismMapping ;
              cb:mapsFrom ?agent ;
              cb:hasStructuralQuality ?sq .
    ?sq cb:sigmaValue ?sigma .
    FILTER (?sigma < 0.8)
}
ORDER BY ASC(?sigma)
```

```sparql
# CQ-OS-07: Composition morphism quality for delegated agents
PREFIX cb:   <http://circuitbreaker.ontology/trust#>
PREFIX aios: <http://aios-wyse.ontology/os#>

SELECT ?composition ?primary ?delegate ?s_a_composed ?c_r_composed
WHERE {
    ?composition a aios:CompositionMorphism ;
                 aios:composedFromPrimary ?h_a ;
                 aios:composedFromDelegate ?h_b ;
                 cb:hasStructuralQuality ?sq ;
                 cb:hasBehavioralQuality ?bq .
    ?h_a cb:mapsFrom ?primary .
    ?h_b cb:mapsFrom ?delegate .
    ?sq  cb:sigmaValue ?s_a_composed .
    ?bq  cb:outputDistance ?d_composed .
    BIND( (1.0 - ?d_composed) AS ?c_r_composed )
}
ORDER BY ASC(?s_a_composed)
```

### 14.3 Relation to Portfolio Ontology

The AIOS-WySE project occupies a specific position in the portfolio governance ontology (GI-JOE, portfolio-abox.ttl [6]). Its ontological relationship to existing portfolio entities is as follows.

**Portfolio ABox integration.** AIOS-WySE is registered as a new individual in the portfolio ABox:

```turtle
@prefix po: <http://joe-g.ontology/portfolio#> .
@prefix aios: <http://aios-wyse.ontology/os#> .

po:AIOS_WySE a po:Hive ;
    po:hiveName "AIOS-WySE" ;
    po:description "Research project developing a morphism-grounded AI operating
        system architecture. Produces the AIOS-WySE technical report,
        executive brief, and practitioner guide." ;
    po:parentHive po:PostWach ;
    po:usesCapability po:FormalMethods ;
    po:usesCapability po:OntologyEngineering ;
    po:dependsOn po:CBTO ;
    po:dependsOn po:WySE_Metamodel ;
    po:targetPublication po:ACM_CAIS_2026 .
```

**Namespace import hierarchy.** The ontology stack for the AIOS-WySE domain is:

    bfo: (BFO 2020 upper ontology)
        |
        cb: (CBTO — Circuit Breaker Trust Ontology)
            |
            aios: (AIOS-WySE OS Governance Ontology — this document)
                |
                po: (Portfolio governance — cross-references only)

The aios: namespace imports cb:, which in turn uses BFO 2020 alignment. The portfolio namespace po: is not imported (imports go up the stack, not sideways); cross-references between aios: individuals and po: individuals are made via external linking triples that can be stored in either the portfolio ABox or a separate alignment file.

**SHACL coverage.** The portfolio ontology's SHACL shapes (portfolio-shacl.ttl [6]) validate that every po:Hive individual has a hiveName, a parentHive, and at least one usesCapability assertion. The AIOS-WySE individual above satisfies these constraints. The aios: SHACL shapes of Section 14.2 validate the AI-OS domain model. The two validation pipelines are independent: portfolio-gate validates governance conformance, and the aios: Tier 1/Tier 2 gate validates runtime system model conformance.

**Long-term ontology evolution.** As the AIOS-WySE architecture matures from technical report to prototype to production, the aios: ontology is expected to evolve in three phases:

1. *Specification phase* (current): The aios: ontology defines intended classes and properties. The ABox is illustrative (a small example deployment, analogous to the CBTO's telecom management ABox [4]).

2. *Prototype phase*: The aios: ontology is populated from runtime telemetry. The SPARQL CQs are executed against a live knowledge graph updated on each monitoring cycle. SHACL validation becomes a runtime check, not a design-time exercise.

3. *Production phase*: The aios: ontology governs real AI-OS deployments. The SHACL shapes become compliance criteria for deployment approval. The SPARQL CQs generate governance dashboards for operators and auditors. The PROV-O audit trail, inherited from the CBTO, satisfies EU AI Act transparency requirements for high-risk AI systems [7].

---

## References (Part IV)

[1] A. W. Wymore, *Model-Based Systems Engineering*. CRC Press, 1993.

[2] P. Wach, "The WySE Metamodel: A Wymorian Systems Engineering Metamodel," in *Proceedings of CSER 2026* (to appear), 2026. [Working title; see [3] for current manuscript.]

[3] P. Wach, N. Sandman, and R. Iyer, "Toward a Library of Isomorphic Patterns for Systems Engineering," in *Proceedings of the Conference on Systems Engineering Research (CSER)*, 2026.

[4] P. Wach, "AI Circuit Breaker: Design Specification v4.0 — Ontology-Grounded Trust Metrology for Autonomous AI Systems," Technical Report, University of Arizona, 2026.

[5] Defense Advanced Research Projects Agency, "Disruption Opportunity: Compositional Learning-And-Reasoning (CLARA)," Solicitation DARPA-PA-25-07-02, 2025.

[6] P. Wach, "GI-JOE Portfolio Governance Ontology v1.1.0," Technical Report, University of Arizona, 2026. Artifacts: portfolio-governance.ttl, portfolio-abox.ttl, portfolio-shacl.ttl.

[7] European Parliament and Council, "Regulation (EU) 2024/1689 of 12 June 2024 laying down harmonised rules on artificial intelligence (Artificial Intelligence Act)," *Official Journal of the European Union*, vol. L, 2024.


---

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

**What stays conventional.** A small, formally verified trusted core occupying the kernel privilege boundary. In the seL4 lineage, the kernel comprises 8,700 lines of C (plus 600 lines of assembler), machine-checked against an Isabelle/HOL specification—a proof corpus representing roughly 200,000 lines. This core provides only the minimum trusted functions: address space management, capability-based access control, inter-process communication (IPC), and thread scheduling. Everything else—device drivers, filesystems, networking, and AI services—runs above the core in user-level protection domains.

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

**Q7: Verification cost reduction.** What is the minimum formal verification investment for a credible AI-native control plane? Can AI-assisted proof generation (vericoding) reduce this investment to economically feasible levels? seL4's 200,000-line proof corpus for 8,700 lines of C establishes a rough upper bound on verification cost for a trusted kernel. An AI-native control plane is larger and more complex. If vericoding can reduce the proof-to-code ratio by an order of magnitude, Architecture C becomes broadly feasible; if vericoding can produce proofs for bounded AI policy modules, Strategy 2 (Section 16.3) becomes achievable. The current state of vericoding tools does not support this assessment; the empirical rate of improvement is an active research question.

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


---

---

## Appendix A: Boundary Test Applied to Five Systems [E]

Section 2.3 defines a three-part test for determining whether a system qualifies as an operating
system, an OS-adjacent platform, or an application-layer framework. The three parts are:

1. **Trusted boot path:** Does the system establish and maintain a hardware root of trust from
   power-on through runtime? Is there a chain from firmware through bootloader to the running
   system that cannot be bypassed without hardware-level access?

2. **Hardware mediation:** Does the system interpose on *all* hardware access by higher-level
   software? Applications and services must not be able to access hardware resources directly;
   all access must flow through the system's managed interfaces.

3. **Stable privileged interface:** Does the system provide a stable, formally specifiable
   interface that higher-level software commits to? Is this interface enforced by hardware
   privilege mechanisms (ring levels, exception levels, capability hardware)?

The test is applied to five candidate systems below.

---

### A.1 Linux (Monolithic General-Purpose OS)

**Trusted boot path:** Yes, with configuration. The standard Linux boot chain -- UEFI secure
boot, GRUB (optionally signed), kernel image verification, initramfs -- provides a root-of-trust
chain from firmware to kernel entry. The chain requires explicit enablement (secure boot
enrollment, dm-verity, IMA/EVM) and is not active by default in most distributions. With proper
configuration, Linux satisfies this criterion.

**Hardware mediation:** Yes. The Linux kernel mediates all hardware access through the system-call
interface. Applications operate in user mode and cannot issue privileged instructions directly;
all hardware interaction flows through driver abstractions, the VFS layer, the socket API, and
so forth. The x86-64 ring 0/3 boundary enforces this at hardware level.

**Stable privileged interface:** Yes. The Linux system call ABI is stable over decades; removing
or breaking a system call is treated as a regression. POSIX compliance is maintained across
distributions. The interface is documented, versioned, and enforced by hardware privilege
separation.

**Verdict: Full OS.** Linux passes all three tests. It is the reference against which other
systems should be compared.

---

### A.2 Kubernetes (Container Orchestration Platform)

**Trusted boot path:** No. Kubernetes does not control the boot process. It runs atop a Linux
(or Windows) host and inherits whatever trust the underlying OS provides. The Kubernetes control
plane starts as a set of user-space processes; there is no Kubernetes equivalent of UEFI secure
boot or kernel integrity measurement.

**Hardware mediation:** No. Kubernetes does not interpose on hardware access. It orchestrates
Linux containers, which are isolated via Linux namespaces and cgroups, but hardware mediation is
performed by the Linux kernel beneath it. Kubernetes can restrict what hardware a container can
access (via PodSecurityPolicy/admission controllers), but it cannot prevent a container from
making system calls to the underlying Linux kernel.

**Stable privileged interface:** Partially. Kubernetes exposes a stable API (the Kubernetes API
server) but this is a management plane API, not a hardware-privilege-enforced interface. The
Kubernetes API is not enforced by processor privilege levels; it is a network-accessible REST
API protected by authentication and authorization at the application layer.

**Verdict: OS-adjacent orchestration platform.** Kubernetes is a powerful infrastructure
management layer that extends and coordinates Linux OS instances, but it is not an OS by the
boundary test. It is sometimes labeled an "OS" in the infrastructure-as-platform sense, which
is the metaphorical usage this report distinguishes from the technical definition.

---

### A.3 AIOS (LLM Agent Operating System, arXiv:2403.16971)

**Trusted boot path:** No. AIOS is a user-space Python framework that runs atop a conventional
OS. It has no boot process, no hardware root of trust, and no kernel-level initialization. It
starts as a set of Python processes.

**Hardware mediation:** No. AIOS accesses hardware through the OS on which it runs. It provides
an abstraction layer over LLM inference, tool execution, and agent scheduling, but all underlying
hardware access flows through the host OS's system calls. AIOS cannot prevent agents from making
direct system calls to the host OS (unless the host OS is configured to restrict this via
seccomp/Landlock).

**Stable privileged interface:** No. AIOS provides an agent API (agent registration, task
submission, context management), but this is an application-layer API enforced by the Python
runtime, not by hardware privilege mechanisms.

**Verdict: OS-metaphor agent framework.** AIOS is a sophisticated agent management layer that
performs scheduling and resource coordination for AI agents. Its architectural contributions
(LLM scheduling, context management as a kernel-like primitive, agent process model) are
genuinely OS-inspired. But by the boundary test, it is not an OS -- it is an agent runtime
framework that uses OS concepts as organizing metaphors. This is not a criticism; the AIOS
contribution is real and the metaphor is productive. It is a distinction that matters for
understanding what AIOS can and cannot guarantee.

---

### A.4 Browser Runtime (Chrome/V8 with Web APIs)

**Trusted boot path:** Partially. A browser does not control the OS boot sequence, but it does
establish a security context at launch: the renderer process is sandboxed at OS level (seccomp
on Linux, AppContainer on Windows), establishing a privilege boundary. The browser's code signing
and update mechanism provides a partial trust chain for the browser itself, though not for the
OS beneath it.

**Hardware mediation:** Partially. The browser mediates web content's access to hardware
(camera, microphone, GPU, storage) through the Web API surface. Web content cannot access these
resources directly; all access flows through browser permission grants. However, the browser does
not mediate access to all system hardware -- native OS applications bypass it entirely -- and the
browser itself accesses hardware through the underlying OS.

**Stable privileged interface:** Partially. The Web Platform APIs (DOM, Web Workers, Service
Workers, WebAssembly, WebGPU) constitute a stable, versioned interface enforced by the browser
runtime. However, this interface is enforced by the browser process, not by hardware privilege
levels. A compromised browser process can bypass it.

**Verdict: Application-layer managed runtime.** The browser is an impressive platform that
manages sandboxed processes, provides a stable API surface, and mediates hardware access for web
content. It satisfies some OS criteria within a bounded scope (web content) but fails the
full-system boundary test. It is a useful comparison point for AI-OS designs that propose
similarly scoped managed runtimes.

---

### A.5 claude-flow (AI Agent Orchestration Framework)

**Trusted boot path:** No. claude-flow is a CLI tool and Node.js library that runs atop a
conventional OS. It initializes as a user-space process with no hardware-level trust
establishment.

**Hardware mediation:** No. claude-flow orchestrates AI agent tasks, manages memory namespaces,
and coordinates swarm topologies, but all hardware access flows through the OS on which it runs.
It does not interpose on hardware access.

**Stable privileged interface:** Partially. claude-flow provides a stable CLI and SDK interface
for agent orchestration, but this is an application-layer contract enforced by the Node.js
runtime, not by hardware privilege mechanisms.

**Verdict: OS-metaphor agent orchestration framework.** claude-flow uses OS concepts (memory
management, process-like agent lifecycle, hierarchical namespacing) as productive organizing
metaphors for agent coordination. Like AIOS, it is not an OS by the boundary test but represents
genuine engineering work in the "OS for AI" problem space. It is the appropriate comparison
point for Architecture B (AI-native control plane) implementations that leverage existing
infrastructure.

---

### Summary Table

| System | Trusted Boot | HW Mediation | Stable Priv. Interface | Verdict |
|--------|-------------|--------------|----------------------|---------|
| Linux | Yes (with config) | Yes | Yes | Full OS |
| Kubernetes | No | No | Partial (app-layer) | OS-adjacent orchestration |
| AIOS | No | No | No | OS-metaphor agent framework |
| Browser runtime | Partial | Partial (scoped) | Partial | App-layer managed runtime |
| claude-flow | No | No | Partial (app-layer) | OS-metaphor agent orchestration |

---

## Appendix B: Glossary of Key Terms [L]

This glossary defines key technical terms used in this report. Definitions are written for the
[L] audience -- no prior technical knowledge is assumed.

**Agent.** An AI-powered software process that can perceive its environment, make decisions, and
take actions autonomously. Unlike a classical program that executes a fixed sequence of
instructions, an agent uses an AI model to decide what to do next. An agent might browse the
web, write code, send emails, or control other software -- depending on what tools it has.

**AI control plane.** The layer of software that uses AI to make policy decisions for a system.
In an AI operating system, the AI control plane decides things like which agents to schedule,
how much memory to allocate to each, and which agents are allowed to communicate with each
other. The control plane sits above the kernel substrate and tells it what to do.

**Attestation.** A cryptographic proof that a piece of software is exactly what it claims to be
and has not been tampered with. Think of it as a notarized certificate for software. Hardware
attestation means the proof comes from a chip that cannot be forged by software alone.

**Behavioral morphism quality (C_r).** A number between 0 and 1 that measures how well an AI
system's decisions match what they are supposed to achieve. A high C_r means the AI does what it
intends to do; a low C_r means its actions are producing unexpected results. See also: structural
morphism quality.

**cgroups (control groups).** A Linux kernel feature that limits and tracks how much CPU, memory,
and other resources a process or group of processes can use. The AIOS-WySE architecture uses
cgroups to enforce resource budgets for AI agents.

**Circuit Breaker.** A safety mechanism that monitors an AI system's quality metrics and
automatically cuts it off from making decisions if its quality falls below a threshold -- just
like an electrical circuit breaker that trips when too much current flows. When the AI circuit
breaker trips, the system falls back to conventional (non-AI) operation until the AI component
recovers.

**Confidential computing.** Technology that protects data while it is being processed, not just
while it is stored or transmitted. Confidential computing uses special hardware (called a Trusted
Execution Environment or TEE) to prevent even the operating system from reading a program's data
while it runs.

**Conventional fallback mode.** The operating mode an AI operating system enters when its AI
control plane has been disabled (by the Circuit Breaker or an explicit override). In this mode,
the system runs using its conventional kernel substrate without AI-driven policy. It is less
intelligent but guaranteed to be safe.

**eBPF (Extended Berkeley Packet Filter).** A Linux technology that allows small programs to be
inserted into the kernel at runtime to observe or modify its behavior, without changing the
kernel's source code. AI agents can use eBPF to monitor system behavior and implement custom
scheduling policies.

**Episodic memory.** A type of agent memory that stores the history of what the agent has done
and experienced -- like a diary. This is different from semantic memory (general knowledge) and
working memory (what the agent is thinking about right now).

**Five-tuple system model.** A formal mathematical description of a system using five components:
inputs (X), outputs (Y), states (S), time domain (T), and two functions -- one that updates
state (delta) and one that produces output (lambda). Developed by A. Wayne Wymore in the 1960s,
this model provides the mathematical foundation for the morphism-grounded interface contract.

**Formal verification.** A mathematical proof that a piece of software does exactly what its
specification says, with no exceptions. Unlike testing (which checks specific cases), formal
verification covers all possible inputs and execution paths. The seL4 microkernel is the most
prominent example of a formally verified OS kernel.

**GPU (Graphics Processing Unit).** Originally designed for rendering graphics, GPUs are now
widely used for AI workloads because they can perform many arithmetic operations in parallel.

**Hardware root of trust.** A piece of hardware (usually a chip) that provides a starting point
for security that cannot be bypassed by software. A hardware root of trust is the first link in
the chain of trust from power-on through to the running system.

**Kernel.** The core of an operating system. The kernel runs at the highest privilege level and
controls all hardware. All other software must ask the kernel for services through the system
call interface.

**KV cache (key-value cache).** A data structure used by large language models to remember the
context of a conversation without having to recompute it from scratch. Managing KV caches for
multiple concurrent AI agents is one of the key agent state management challenges.

**Microkernel.** An OS design where the kernel is kept very small -- it only provides
inter-process communication, scheduling, and memory management. Everything else (device drivers,
filesystems, networking) runs as user-space servers. seL4 is the canonical modern microkernel.

**Model Context Protocol (MCP).** An open protocol published by Anthropic that defines how AI
agents communicate with tools and data sources. MCP is the emerging standard for the "tool
layer" in AI agent architectures. As of December 2025, the MCP SDK had over 97 million monthly
downloads.

**Morphism.** A structure-preserving map between two mathematical objects. In this report, a
morphism h: Z_ai -> Z_k maps the AI control plane's representation of system state to the
kernel's representation, preserving relationships between states, inputs, and outputs. The
quality of this morphism is what the Circuit Breaker monitors.

**NPU (Neural Processing Unit).** A specialized chip designed to accelerate AI computations.
Modern smartphones and laptops increasingly include NPUs alongside CPUs and GPUs.

**Prompt injection.** An attack where malicious content in an AI agent's input manipulates the
agent into taking actions it was not intended to take. One of the primary security threats in AI
operating systems, analogous to a buffer overflow attack in conventional systems.

**sched_ext.** A Linux kernel feature that allows custom scheduling policies to be loaded at
runtime using eBPF programs, without modifying the kernel source. A primary insertion point for
implementing AI-driven scheduling in Architecture B.

**Semantic memory.** A type of agent memory that stores general knowledge and facts the agent
has learned. Often implemented using a vector database that the agent can query.

**seL4.** A formally verified microkernel with a machine-checked proof that its implementation
exactly matches its specification. The verification proof covers 8,700 lines of C (plus 600
lines of assembler) and required approximately 20 person-years to develop.

**Structural morphism quality (S_a).** A number between 0 and 1 that measures how accurately
an AI system's internal model of its environment matches reality. A high S_a means the AI has
an accurate picture of what is happening; a low S_a means its model has drifted from reality.
See also: behavioral morphism quality.

**System call (syscall).** The mechanism by which a program asks the OS kernel for a service.
The system call interface is the boundary between user programs and the kernel.

**TEE (Trusted Execution Environment).** An isolated region of hardware memory and processing
that cannot be read or modified by the rest of the system, not even by the operating system.
The NVIDIA H100 GPU TEE is the first GPU-resident TEE at production scale.

**TRL (Technology Readiness Level).** A 1-to-9 scale originally developed by NASA to describe
how mature a technology is. TRL 1 means basic principles observed; TRL 9 means proven in
operational mission.

**Unikernel.** An OS architecture where a single application is compiled together with exactly
the OS components it needs into a single kernel image. Unikernels have minimal attack surfaces
and fast startup times, making them attractive for stateless AI agent execution.

**WySE Metamodel (Wymorian Systems Engineering Metamodel).** The formal system model used in
this report, grounding the AIOS-WySE architecture in A. Wayne Wymore's mathematical theory of
systems engineering. Defines system interfaces as five-tuple models and inter-system
relationships as morphisms.

---

## Appendix C: Comparison Table -- AIOS vs. MemOS vs. PunkGo vs. claude-flow [P/E]

The four systems below represent different points in the design space of AI-native
infrastructure. This table compares them against four dimensions relevant to the AIOS-WySE
architecture.

**Notes on scope:** AIOS and MemOS are academic research prototypes with published results.
PunkGo (the system described in "Right to History," arXiv:2602.20214) is a research prototype
focused on verifiable execution provenance. claude-flow is an open-source production tool for AI
agent orchestration. None of these is an OS by the boundary test (Appendix A). They are compared
here as representatives of the "OS for AI" design space.

| Dimension | AIOS (arXiv:2403.16971) | MemOS (arXiv:2507.03724) | PunkGo / Right to History (arXiv:2602.20214) | claude-flow |
|-----------|------------------------|--------------------------|----------------------------------------------|-------------|
| **Architecture type** | Agent runtime framework with OS-like scheduling, context management, and storage layers. Runs atop a conventional OS as a Python/Java library. Agents are managed entities with registration, scheduling queue, and context eviction policies. | Memory operating system: extends OS memory management to treat long-term, short-term, and parametric memory as first-class managed resources. Introduces MemCube abstraction unifying heterogeneous memory tiers. | Sovereignty kernel providing verifiable execution logs for AI agents. Implements a hardware-backed append-only log using RFC 6962 Merkle trees, enabling cryptographic auditability of every agent action. | Hierarchical swarm orchestration CLI and SDK. Coordinates multiple AI agents in configurable topologies (hierarchical, mesh, pipeline). Manages memory namespaces, agent lifecycle, and cross-agent communication. |
| **Primary abstraction** | Agent as a managed OS process. The AgentProcess has a scheduler slot, a context window managed like virtual memory (LRU eviction when full), and a storage interface. | MemCube: a unified container for agent memory spanning volatile (in-context), persisted (vector/KV store), and parametric (model weights) tiers, managed with explicit scheduling and migration policies. | Verifiable action log: every agent action is appended to an immutable Merkle log with sub-1.3 ms latency. Inclusion proofs (448 bytes at 10,000 entries) allow auditors to verify action membership without replaying the log. | Agent swarm with hierarchical coordination. Primary abstractions: agents (individual LLM-backed workers), tasks (units of work routed to agents), memory namespaces (scoped key-value stores shared within a swarm). |
| **Formal governance** | None. The paper analyzes scheduling strategies and context eviction policies empirically. No formal specification of the agent-OS interface, no monitored invariants, no circuit-breaker mechanism. | None. MemOS focuses on empirical benchmarking. The MemCube abstraction is described architecturally but not formally specified. | Partial: the Merkle tree log provides cryptographic integrity guarantees for the action history. Formal in the security sense (hash-based tamper evidence) but not in the systems-engineering sense -- there is no formal specification of what correct agent behavior looks like, only a record of what occurred. | None. claude-flow does not have formal governance mechanisms. CLAUDE.md governance files provide human-readable rules for agent behavior but are not enforced by any formal verification or monitoring mechanism. |
| **Maturity level** | Research prototype. Published at COLM 2025; arXiv v4 as of 2026. Demonstrated 2.1x execution speed improvement over baseline agent frameworks. Not in production deployment. | Research prototype. arXiv July 2025 (full version December 2025). Demonstrates 159% improvement in temporal reasoning on LoCoMo. No production deployment reported. | Research prototype. arXiv February 2026. Demonstrates sub-1.3 ms action latency and ~400 actions/sec throughput on benchmark workloads. No production deployment. | Production tool. Actively maintained, globally installable via npm. Used in real research and engineering workflows. Lacks formal governance and OS-level assurances but provides immediate practical value for agent coordination. |

**AIOS-WySE position relative to these systems:** AIOS-WySE is an architectural specification
with formal foundations, not a prototype implementation. It subsumes the concerns of all four
systems: the agent process management of AIOS, the tiered memory management of MemOS, the
verifiable provenance of PunkGo, and the swarm orchestration of claude-flow -- but grounds all
of these in the Wymore morphism interface contract (Section 13) and the Circuit Breaker watchdog
(Section 13.4), and specifies how they integrate into a coherent architecture (Section 15.2,
Architecture B). The near-term prototype path for Architecture B uses Linux with eBPF,
sched_ext, and cgroups v2, which is the substrate on which an enhanced version of AIOS-style
agent management could run with formal governance.

---

## Appendix D: AI-Kernel Interface Primitives

**See Section 9 for full specification.**

Section 9 provides the complete AI-Kernel Interface Contract, including the Interface Definition
Language (IDL) notation for the downward API (AI control plane to kernel) and upward API (kernel
to AI control plane), the policy-vs.-mechanism boundary analysis, and the mapping to existing
Linux insertion points (eBPF, sched_ext, cgroups v2, Landlock LSM).

The IDL primitives specified in Section 9 include: `aios_schedule_hint()`,
`aios_memory_reserve()`, `aios_resource_fence()`, `aios_audit_log()` (downward API); and
`aios_resource_available()`, `aios_security_event()`, `aios_memory_pressure()`,
`aios_lifecycle_event()` (upward API).

---

## Appendix E: CBTO Extension for AI-OS Governance

**See Section 14 for full OWL 2 DL specification.**

Section 14 provides the complete ontological grounding for AIOS-WySE, including: the Circuit
Breaker Trust Ontology (CBTO) extension to AI-OS governance, the OWL 2 DL class additions
required for AI-OS concepts (AgentState, ResourceBinding, SchedulingPolicy), the two-tier SHACL
validation pipeline adapted from the GI-JOE ontology-gate pattern, candidate competency
questions for AI-OS governance, and the relation of AIOS-WySE to the portfolio ontology
(GI-JOE/ontologies/domain/portfolio-governance.ttl).

---

## Appendix F: Unified Reference List

**Note on numbering.** Each part of this report uses its own local reference numbering (e.g.,
[1]-[46] in Part I, [III-1]-[III-N] in Part III). This appendix provides a unified numbered
list eliminating duplicates. Where a work appears with multiple part-local numbers, only one
global number is assigned. The global numbers are the canonical citation keys for the combined
report.

**Reference numbers are per-section; see Appendix F for unified numbering.**

---

### OS Foundations -- Textbooks and Surveys

[1] A. Silberschatz, G. Gagne, and P. B. Galvin, *Operating System Concepts*, 10th ed. Wiley,
2018. ISBN: 9781119320913. https://www.os-book.com/OS10/

[2] A. S. Tanenbaum and H. Bos, *Modern Operating Systems*, 4th ed. Pearson, 2015.
ISBN: 9780133591620. https://dl.acm.org/citation.cfm?id=2655363

[3] R. H. Arpaci-Dusseau and A. C. Arpaci-Dusseau, *Operating Systems: Three Easy Pieces*,
v1.10. Arpaci-Dusseau Books, 2023. https://pages.cs.wisc.edu/~remzi/OSTEP/

[4] Y. Zhang et al., "Integrating Artificial Intelligence into Operating Systems: A Survey on
Techniques, Applications, and Future Directions," arXiv:2407.14567v3, Nov. 2025.
https://arxiv.org/abs/2407.14567

### Kernel Architecture and Formal Verification

[5] G. Klein et al., "seL4: Formal Verification of an OS Kernel," in *Proc. ACM SOSP*, Big Sky,
MT, Oct. 2009, pp. 207-220.
https://www.sigops.org/s/conferences/sosp/2009/papers/klein-sosp09.pdf
[Verified: 8,700 lines of C plus 600 lines of assembler; 20 person-years total.]

[6] T. Murray et al., "seL4: From General Purpose to a Proof of Information Flow Enforcement,"
in *Proc. IEEE S&P*, San Francisco, CA, May 2013, pp. 415-429.

[7] X. Leroy, "Formal Verification of a Realistic Compiler," *Commun. ACM*, vol. 52, no. 7,
pp. 107-115, Jul. 2009. https://dl.acm.org/doi/10.1145/1538788.1538814

[8] R. Krebbers, R. Jung et al., "The Essence of Higher-Order Concurrent Separation Logic,"
in *Proc. ESOP*, LNCS 10201, 2017.
https://iris-project.org/pdfs/2017-esop-iris3-final.pdf

[9] M. Sammler et al., "RefinedC: Automating the Foundational Verification of C Code with
Refined Ownership Types," in *Proc. PLDI 2021*.
https://dl.acm.org/doi/10.1145/3453483.3454036

[10] R. Cox, F. Kaashoek, and R. Morris, *xv6: A Simple, Unix-Like Teaching Operating System*,
MIT, 2023. https://pdos.csail.mit.edu/6.S081/2023/xv6/book-riscv-rev3.pdf

### Operating System Landscape and Modern Variants

[11] Fuchsia Team, "Fuchsia F27 Release Notes," fuchsia.dev, Jul. 15, 2025.
https://fuchsia.dev/whats-new/release-notes/f27

[12] "Unikraft Launches With $6M to Drive Dramatic New Efficiencies in Scale and Cost for Cloud
Computing in the AI Era," BusinessWire, Oct. 9, 2025.
https://www.businesswire.com/news/home/20251009046776/en/Unikraft-Launches-With-$6M-to-Drive-Dramatic-New-Efficiencies-in-Scale-and-Cost-for-Cloud-Computing-in-the-AI-Era

[13] A. Madhavapeddy et al., "Unikernels: Library Operating Systems for the Cloud," in *Proc.
ACM ASPLOS*, 2013.

[14] MINIX 3 Project. https://www.minix3.org/

### AI Agent OS Research

[15] B. Shi et al., "AIOS: LLM Agent Operating System," in *Proc. COLM 2025*,
arXiv:2403.16971v4. https://arxiv.org/abs/2403.16971
[Verified: 2.1x execution speed claim; COLM 2025 publication confirmed.]

[16] T. Li et al., "MemOS: A Memory OS for AI System," arXiv:2507.03724, Jul. 2025
(rev. Dec. 2025). https://arxiv.org/abs/2507.03724
[Verified: 159% improvement in temporal reasoning on LoCoMo benchmark.]

[17] T. Li et al., "MemOS: An Operating System for Memory-Augmented Generation (MAG) in Large
Language Models," arXiv:2505.22101, May 2025. https://arxiv.org/abs/2505.22101
[Short/initial version of [16]; both should be cited when discussing MemOS's evolution.]

[18] "Right to History: A Sovereignty Kernel for Verifiable AI Agent Execution,"
arXiv:2602.20214, Feb. 23, 2026. https://arxiv.org/abs/2602.20214
[Verified: sub-1.3 ms action latency; ~400 actions/sec; 448-byte Merkle proofs at 10,000 entries.
Note: cite 448-byte figure, not "logarithmic-size" -- see reference database.]

[19] Y. Zheng et al., "AgentCgroup: Understanding and Controlling OS Resources of AI Agents,"
arXiv:2602.09345, Feb. 2026. https://arxiv.org/abs/2602.09345
[Verified: OS execution accounts for 56-74% of end-to-end agent task latency.]

[20] Y. Zheng et al., "AgentSight: System-Level Observability for AI Agents Using eBPF,"
in *Proc. 4th Workshop on Practical Adoption Challenges of ML for Systems (ACM)*, 2025,
arXiv:2508.02736. https://arxiv.org/abs/2508.02736

[21] [Author TBD], "Agent.xpu: Efficient Scheduling of Agentic LLM Workloads on Heterogeneous
SoC," arXiv:2506.24045, Jun. 2025 (rev. Jan. 2026). https://arxiv.org/abs/2506.24045
[Verified: 1.2-4.9x proactive throughput improvement; 91% reduction in reactive latency.]

### Security and Isolation for AI Systems

[22] J. Ji et al., "Taming Various Privilege Escalation in LLM-Based Agent Systems: A
Mandatory Access Control Framework," arXiv:2601.11893, Jan. 2026.
https://arxiv.org/abs/2601.11893
[System name: SEAgent. Implements ABAC-based MAC with information flow graph enforcement.]

[23] T. Bodea, M. Misono, J. Pritzi et al., "Trusted AI Agents in the Cloud,"
arXiv:2512.05951, Dec. 2025. https://arxiv.org/abs/2512.05951
[System name: Omega. Nested isolation via VMPL levels within a single CVM.]

[24] [Author TBD], "Confidential Computing on NVIDIA Hopper GPUs: A Performance Benchmark
Study," arXiv:2409.03992, Sep. 2024 (rev. Nov. 2024). https://arxiv.org/abs/2409.03992
[CORRECTED: Overhead is below 7% for typical LLM inference queries; the <5% figure is
incorrect. Near-zero overhead for large models; highest overhead for small models with short
sequences.]

[25] NVIDIA, *H100 GPU Trusted Execution Environment: Technical Overview*, 2023.

[26] AMD, "AMD Secure Encrypted Virtualization -- Secure Nested Paging (SEV-SNP),"
White Paper, 2020.

[27] Intel, "Intel Trust Domain Extensions (TDX)," Architecture Specification, 2023.

### Hardware Substrate

[28] NVIDIA, "Vera Rubin NVL72 Architecture Overview," GTC 2025.

[29] Intel, "Intel Data Center GPU Max Series Architecture."

[30] AMD, "AMD Instinct MI300X Architecture."

### Tool Protocols and Standards

[31] Anthropic, "Model Context Protocol Specification," Nov. 2025.
https://spec.modelcontextprotocol.io/

[32] Anthropic, "Donating the Model Context Protocol and Establishing the Agentic AI
Foundation," Dec. 9, 2025.
https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation
[Verified: over 97 million monthly SDK downloads across Python and TypeScript SDKs.]

[33] NIST CAISI, "Announcing the AI Agent Standards Initiative for Interoperable and Secure
Innovation," Feb. 17, 2026.
https://www.nist.gov/news-events/news/2026/02/announcing-ai-agent-standards-initiative-interoperable-and-secure
[Verified: launched February 17, 2026. Three pillars: standards leadership, open-source
protocol development, AI agent security research.]

[34] Google DeepMind, "Agent-to-Agent (A2A) Protocol Specification," 2025.

### Formal Methods -- Wymore and Applied Category Theory

[35] A. W. Wymore, *A Mathematical Theory of Systems Engineering: The Elements*. John Wiley
& Sons, New York, 1967.
https://openlibrary.org/books/OL5544238M/A_mathematical_theory_of_systems_engineering

[36] A. W. Wymore, *Model-Based Systems Engineering*. CRC Press, Boca Raton, FL, 1993.
ISBN: 9780849380129.
https://www.routledge.com/Model-Based-Systems-Engineering/Wymore/p/book/9780849380129

[37] B. Fong and D. I. Spivak, *An Invitation to Applied Category Theory: Seven Sketches in
Compositionality*. Cambridge University Press, 2019, arXiv:1803.05316.
https://arxiv.org/abs/1803.05316

[38] P. F. Wach et al., "Toward a Library of Isomorphic Patterns for Systems Engineering,"
in *Proc. CSER 2026* (revision of Submission 84). [Preprint in preparation.]

### Runtime Assurance and Safety Architecture

[39] D. Seto, B. Krogh, L. Sha, and A. Chutinan, "The Simplex Architecture for Safe On-Line
Control System Upgrades," in *Proc. American Control Conference*, 1998.
https://experts.illinois.edu/en/publications/the-simplex-architecture-for-safe-on-line-control-system-upgrades/

[40] A. Zuepke and R. Bommert, "AUTOBEST: A United AUTOSAR-OS and ARINC 653 Kernel," in
*Proc. IEEE RTAS*, 2015. https://ieeexplore.ieee.org/document/7108435/

[41] RTCA, *DO-178C: Software Considerations in Airborne Systems and Equipment Certification*,
2011.

[42] ISO, *ISO 26262: Road Vehicles -- Functional Safety*, 2018.

[43] ISO/SAE, *ISO/DPAS 8800: Road Vehicles -- Safety and Artificial Intelligence* (in
progress).

### AI Circuit Breaker and CBTO

[44] P. F. Wach, "AI Circuit Breaker Design Specification v4.0: Ontology-Grounded Trust
Metrology," Technical Report, University of Arizona, 2026.

[45] PROV-O: The PROV Ontology. W3C Recommendation, Apr. 2013.
https://www.w3.org/TR/prov-o/

[46] BFO 2020: Basic Formal Ontology 2.0 (ISO/IEC 21838-2). ISO, 2021.

### Memory and State Management for AI

[47] HeART (Heterogeneous Attention for Retrieval with Tiering). [Citation pending
publication.]

[48] Oaken (KV Cache Isolation Framework). [Citation pending publication.]

### Community Context and Conferences

[49] AgenticOS 2026 Workshop, "Operating Systems Design for AI Agents," co-located with
ASPLOS 2026, Mar. 23, 2026, Pittsburgh. https://os-for-agent.github.io/
[Verified: confirmed for March 23, 2026.]

[50] ACM CAIS 2026, "ACM Conference on AI and Agentic Systems," May 26-29, 2026, San Jose,
CA. https://www.caisconf.org/
[Verified: workshops May 26; main conference May 27-29.]

### AI Assurance and Governance

[51] NIST, *AI Risk Management Framework (AI RMF 1.0)*, Jan. 2023.
https://airc.nist.gov/RMF_Overview

[52] European Parliament and Council, *EU AI Act (Regulation (EU) 2024/1689)*, Jul. 2024.

[53] DARPA, "Compositional Learning-And-Reasoning (CLARA) Program Announcement,"
DARPA-PA-25-07-02, 2025.

### claude-flow

[54] R. L. Robinson (ruv), *claude-flow: AI Agent Orchestration Framework*, v3.1.x.
https://github.com/ruvnet/claude-flow

### Measurement and Uncertainty

[55] JCGM, *Evaluation of Measurement Data -- Guide to the Expression of Uncertainty in
Measurement (GUM)*, JCGM 100:2008.

### AI Formal Reasoning and Proof Automation

[56] P. Jiang et al., "Selene: Automating seL4 Proof Engineering with Large Language
Models," arXiv preprint, 2025. [arXiv number TBC.]

[57] DeepSeek AI, "DeepSeek-Prover-V2: Advancing Formal Mathematics Reasoning," arXiv
preprint, 2025.

---

*Total: 57 numbered entries. The Blue Team recommended additions [B1]-[B13] from the reference
database are incorporated as: [1]-[3] (OS textbooks), [7]-[9] (formal verification), [20]
(AgentSight/eBPF observability), [4] (AI-OS survey), [39]-[40] (runtime assurance/
mixed-criticality), [37] (applied category theory), [35]-[36] (Wymore originals). All 13 Blue
Team recommendations are represented. Several part-local references (particularly in Part III)
use local numbering [III-N] that maps to the entries above; a complete cross-reference table
is deferred to a future editing pass.*

