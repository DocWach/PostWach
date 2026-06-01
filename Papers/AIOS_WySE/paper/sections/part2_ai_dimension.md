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
