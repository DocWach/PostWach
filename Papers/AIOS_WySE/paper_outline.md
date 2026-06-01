# AIOS-WySE: Toward a Morphism-Grounded AI Operating System
## Paper Outline v0.1 — March 7, 2026

### Deliverable Set
1. **Full Technical Report** (40-50 pages) — single document with layered reading guide
   - Audience markers: [L] = Labrador (entry), [P] = Practitioner, [E] = Expert
   - Publishable at: IEEE Software, ACM Computing Surveys, or as standalone technical report
2. **Executive Brief** (3-5 pages) — extracted from the report
   - Audience: PMs, executives, NNSA leadership, non-technical stakeholders
3. **Practitioner Guide** (15-20 pages) — extracted from the report
   - Audience: Software architects, AI engineers, systems engineers building AI-native platforms

### Publication Targets
- AgenticOS 2026 @ ASPLOS (March 23, 2026 — likely too soon for full paper, but position paper possible)
- ACM CAIS 2026 (May 26-29, 2026, San Jose — first dedicated conference on agentic systems)
- IEEE Software special issue (if available) or EMSE
- CSER 2027 (workshop paper, ~Sep 2026 submission)
- Journal: ACM Computing Surveys, IEEE TSE, or JSS

---

## Full Technical Report Structure

### Front Matter
- Title: "Toward a Morphism-Grounded AI Operating System: Architecture, Formal Foundations, and Research Roadmap"
- Abstract (300 words)
- Reading Guide (how labrador/practitioner/expert should navigate)
- Table of Contents

---

### Part I: Foundations (What exists today)

#### 1. Introduction and Scope [L/P/E]
- 1.1 What people mean when they say "AI operating system" [L]
  - The metaphor problem: smartphones, cloud orchestrators, agent frameworks all called "OS"
  - Three concrete things the phrase can mean (preview of Section 7)
- 1.2 The two orthogonal research programs [P/E] **[NEW — addresses Gap 1]**
  - **"AI for OS"**: AI replaces/augments kernel functions (scheduling, memory, security)
  - **"OS for AI"**: OS provides resource management for AI agents as first-class workloads
  - Why conflating these produces untestable claims
  - Table: side-by-side comparison of requirements, metrics, threat models
- 1.3 Scope and method
  - Covers both programs; flags which is being discussed at each point
  - Sources: primary systems research, industry documentation, standards, formal methods
- 1.4 What this report adds beyond existing surveys
  - Formal interface contract (WySE morphisms)
  - Runtime governance mechanism (Circuit Breaker)
  - Agent state architecture (the hardest unsolved problem)
  - Empirical grounding from 2025-2026 literature explosion

#### 2. What Is an Operating System? [L/P/E]
- 2.1 The beginner definition [L]
  - Software that starts first, stays in control, lets other software use the machine
  - NIST definition, OSTEP framing (virtualization, concurrency, persistence)
- 2.2 The systems-level definition [P]
  - Table 1: Classical OS responsibilities (boot, execution, resources, persistence, protection)
  - The system call boundary: application ↔ kernel interface
  - UEFI boot → ExitBootServices() → kernel assumes control
- 2.3 The boundary test [E]
  - Three-part test: trusted boot path, hardware mediation, stable privileged interfaces
  - When something is "OS-adjacent" vs. a real OS (Kubernetes, browser runtimes, agent frameworks)
  - Formal definition candidate: OS as a triple (H, K, I) where H = hardware, K = kernel, I = interface contract
- **Retained from ChatGPT draft:** Table 1 (expanded), boundary test appendix content

#### 3. OS Taxonomy: Categories, Architecture, Standards [P/E]
- 3.1 By purpose [P]
  - General-purpose, mobile, embedded/RTOS, safety-critical, distributed control plane
  - **[NEW]** Add: unikernels (Unikraft, MirageOS) as a category — specialized single-application OS
  - **[NEW]** Add: capability-based OS (Fuchsia/Zircon) as architectural variant
  - Table 2: expanded taxonomy with unikernels and capability-based entries
- 3.2 By kernel architecture [E]
  - Monolithic (Linux), microkernel (seL4, MINIX 3), hybrid (Windows NT, macOS XNU)
  - **[NEW]** Unikernel (Unikraft): one app = one kernel image, minimal attack surface
  - **[NEW]** Library OS / exokernel lineage → WASM/WASI as modern descendant
  - Fuchsia/Zircon: capability-based object model, zero-default-privilege
- 3.3 By standards regime [E]
  - POSIX/SUS, AUTOSAR Adaptive, ARINC 653, DO-178C, ISO 26262
  - **[NEW]** Emerging AI-adjacent standards: MCP, A2A, NIST AI Agent Standards Initiative
  - **[NEW]** The standards gap: no POSIX equivalent for AI-OS interfaces (this is an open problem)
- **Retained from ChatGPT draft:** Table 2 (expanded), standards discussion

#### 4. Hardware Substrate and Platform Evolution [P/E]
- 4.1 The hardware spectrum [P]
  - MCU → mobile SoC → desktop → server → accelerator-rich/disaggregated
  - Table 3 retained and expanded
- 4.2 The heterogeneity inflection [E]
  - NPUs (40+ TOPS → 80-100 TOPS trajectory), DPUs (BlueField), CXL memory pooling
  - **[NEW]** Confidential computing hardware: AMD SEV-SNP, Intel TDX, ARM CCA, NVIDIA H100 GPU TEE
  - **[NEW]** Rack-scale confidential computing (Vera Rubin NVL72) — TEE spans entire AI compute rack
  - The OS implication: "how do I manage a heterogeneous, partially disaggregated, policy-rich compute fabric?"
- 4.3 What this means for AI-OS design [E]
  - Intelligence will not execute on "the CPU" — placement, locality, attestation, fallback all needed
  - **[NEW]** Energy/thermal management as first-class scheduling constraint (SoC thermal envelopes)
- **Retained from ChatGPT draft:** Table 3 (expanded), hardware lesson

#### 5. How to Create an Operating System [P/E]
- 5.1 The engineering pipeline [P]
  - Scope → architecture → boot → kernel → resource managers → user-space → ecosystem
  - Why most "new OS" efforts fail (boot, drivers, memory safety, compatibility, ecosystem gravity)
- 5.2 The minimum viable kernel [E]
  - Privilege separation, trap/interrupt handling, timer, context switching, memory init
  - Then: scheduler, memory management, filesystem
  - Then: device support, user-space contract, development discipline
- 5.3 The ecosystem burden [P/E]
  - ABIs, executable formats, system-call conventions, drivers, tooling
  - Why reusing existing substrates is the credible near-term path
  - **[NEW]** The verification burden: seL4 took ~20 person-years for ~10K lines of C
- **Retained from ChatGPT draft:** Section 5 mostly intact, strengthened

---

### Part II: The AI Dimension (What AI brings to the table)

#### 6. AI Taxonomy Relevant to an AI-Based OS [P/E]
- 6.1 A five-layer framework [P]
  - Layer 1: Knowledge and reasoning (expert systems, PGMs, causal, neuro-symbolic)
  - Layer 2: Learning and adaptation (RL, continual learning, transfer learning)
  - Layer 3: Foundation-model substrate (LLMs, code models, multimodal)
  - Layer 4: Decision and autonomy (planning, single-agent, multi-agent, swarms)
  - Layer 5: Embodiment and world models
  - Table 4 retained
- 6.2 Comparative fit to OS responsibilities [E]
  - Table 5 retained and expanded
  - **[NEW]** Add: eBPF + ML as a concrete "AI for OS" mechanism (not just a paradigm)
  - **[NEW]** Add: WASM/WASI as a portable AI runtime layer (not just a container alternative)
  - Key insight: no single AI family will "be the OS" — composition is mandatory

#### 7. What Counts as an AI-Based OS? [L/P/E]
- 7.1 Three meanings, precisely defined [L/P]
  - Type A: AI-augmented conventional OS (Copilot+ PC, Apple Intelligence)
  - Type B: AI-native control plane over conventional substrate (recommended near-term)
  - Type C: Clean-sheet AI OS (AIOS, MemOS — research frontier)
- 7.2 The "OS for AI" vs. "AI for OS" mapping [E] **[NEW]**
  - Type A and B can serve both programs
  - Type C is primarily "OS for AI" — agents as first-class entities
  - Table: which types serve which programs, with what tradeoffs
- 7.3 Industry evidence: what has shipped [P] **[NEW]**
  - Microsoft Windows AI Foundry / Copilot-in-kernel (Type A → B transition)
  - Apple Intelligence: NPU-prefill + GPU-decode, Neural Engine as OS-managed hardware (Type A)
  - Google AICore / Gemini Nano: foundation model as system service (Type A)
  - AIOS v5 / COLM 2025: agent scheduling, context management as kernel primitives (Type C)
  - MemOS: memory as first-class OS resource with MemCube abstraction (Type C variant)
- **Retained from ChatGPT draft:** Three-way definition, AIOS discussion (updated to v5)

---

### Part III: The Architecture (What must be built) **[MAJOR NEW CONTENT]**

#### 8. Engineering Requirements [P/E]
- 8.1 The seven requirements (retained, each expanded with concrete mechanisms)
  1. Trusted substrate (kernel, boot, isolation, hardware mediation)
  2. AI runtime and resource manager (agent scheduling, context, memory)
  3. Tool and interoperability layers (MCP Nov 2025 spec, A2A, NIST standards)
  4. Model lifecycle management (provenance, rollback, drift, evaluation)
  5. Hardware-aware heterogeneous scheduler (CPU/GPU/NPU/DPU placement + thermal)
  6. Operator control and auditability (audit logs, override, transparency)
  7. Risk management and governance (NIST AI RMF as baseline, not ceiling)
- 8.2 **[NEW]** Eighth requirement: Agent state management
  - Execution context, episodic memory, semantic memory, goal state, resource bindings
  - Ownership model, consistency semantics, persistence policy
  - Why this is the hardest new OS problem
- 8.3 **[NEW]** Ninth requirement: Energy and thermal governance
  - AI inference competes with OS overhead for power budget on modern SoCs
  - Without thermal-aware scheduling, throttling is unpredictable

#### 9. The AI-Kernel Interface Contract [E] **[ENTIRELY NEW — addresses Gap 2]**
- 9.1 Why the interface is the architecture
  - Layered systems stand or fall on the interface between layers
  - Without a specified contract, "control plane" is a metaphor
- 9.2 Downward API: AI control plane → Kernel
  - Resource hints (scheduling intent, latency budgets, priority classes)
  - Memory reservation (agent working sets, eviction policies)
  - Resource fencing (hardware partition binding)
  - Audit logging (kernel-enforced immutable trail)
  - Candidate primitives (illustrative IDL)
- 9.3 Upward API: Kernel → AI control plane
  - Resource availability and contention signals
  - Security events (anomalous syscall patterns, privilege escalation attempts)
  - Memory pressure events requiring agent context eviction
  - Process/container lifecycle events
- 9.4 Policy vs. mechanism boundary
  - Kernel enforces mechanism (isolation, scheduling quantum, memory protection)
  - AI control plane sets policy (which agents communicate, resource allocation priorities)
  - Where the line falls and why
- 9.5 **Existing insertion points** [P/E]
  - eBPF + sched_ext: the Linux-native path to AI-influenced scheduling (AgentCgroup results)
  - cgroups v2: hierarchical resource control aligned to agent boundaries
  - Landlock LSM: capability-based tool sandboxing
  - Why these are sufficient for near-term prototyping but not for the full vision

#### 10. Agent State Architecture [E] **[ENTIRELY NEW — addresses Gap 4]**
- 10.1 The state taxonomy
  - Execution context (current task, tool bindings, in-flight calls)
  - Episodic memory (interaction history, KV cache)
  - Semantic memory (retrieved facts, RAG index pointers, learned associations)
  - Goal state (objectives, subgoal decomposition, pending commitments)
  - Resource bindings (file descriptors, GPU memory, network connections, API sessions)
- 10.2 Storage substrates per category
  - In-process volatile, dedicated state store, kernel-managed, distributed
  - Tradeoffs: consistency, latency, failure behavior
- 10.3 Ownership and isolation
  - Who can read/write each state component
  - Agent delegation: if A invokes B, who owns the state B modifies?
  - KV cache isolation (active research: HeART, Oaken — unsolved at scale)
- 10.4 Consistency model
  - Which state components require strong consistency, eventual consistency, or can be discarded
  - Checkpoint/restore semantics for agent migration
- 10.5 Relation to MemOS
  - MemCube as a unifying abstraction for heterogeneous memory tiers
  - How MemOS's design choices compare to what we propose
- 10.6 The "Everything is Context" alternative
  - Unix "everything is a file" → "everything is context" (Xu et al. 2025)
  - Context as a mountable, governed filesystem abstraction

#### 11. Security Architecture [E] **[ENTIRELY NEW — addresses security gap]**
- 11.1 Threat model for an AI-native OS
  - Prompt injection as privilege escalation (not just an application bug)
  - Confused deputy in multi-agent systems (SEAgent, MAC framework)
  - Model supply chain compromise (poisoned weights, corrupted adapters)
  - Side-channel attacks on shared AI inference resources
- 11.2 Agent isolation tiers
  - Tier 0: Same process (no isolation — fast, unsafe, internal-only agents)
  - Tier 1: Separate processes with capability-based communication (Plan 9 / seL4 model)
  - Tier 2: Separate containers (Docker-equivalent, ~1-5ms overhead)
  - Tier 3: Separate VMs / TEEs (highest isolation, ~100ms startup)
  - Tier 4: Hardware partitions (MIG, SR-IOV — GPU-level isolation)
  - Policy: which trust class of agent maps to which tier
- 11.3 Tool capability model
  - Agents invoke tools (MCP, A2A) that access filesystems, networks, external APIs
  - Least-privilege enforcement: capability tokens, not ambient authority
  - Landlock + seccomp as near-term mechanisms; formal capability model for the full vision
- 11.4 Model integrity chain
  - Cryptographic signing of model weights
  - Attestation of loading process (TPM or TEE)
  - Policy engine: which models are permitted for which workloads
- 11.5 Tamper-evident provenance
  - PunkGo / Right to History: Merkle tree audit logs as kernel primitive
  - PROV-O integration (from CBTO v4.0)
  - EU AI Act compliance implications
- 11.6 Confidential computing substrate
  - GPU TEE (NVIDIA H100/Blackwell) — <5% overhead for LLM inference
  - Intel TDX Connect: secure CPU-GPU channels
  - Omega system: nested isolation within single CVM
  - Rack-scale confidential computing (Vera Rubin NVL72)

#### 12. Failure Taxonomy and Recovery [E] **[ENTIRELY NEW — addresses Gap 3]**
- 12.1 AI control plane failure modes
  - Process crash (segfault, OOM)
  - Inference livelock (unresponsive reasoning loop)
  - Catastrophically wrong policy decision (safety failure)
  - Adversarial compromise (OS-level prompt injection)
  - Model weight corruption (integrity failure)
  - Split-brain (AI layer and kernel disagree on system state)
- 12.2 Detection, containment, recovery for each mode
  - Table: failure mode → detection mechanism → containment boundary → recovery procedure → time bound
- 12.3 Degraded mode specification
  - When the AI control plane is unavailable, the conventional substrate runs standalone
  - What capabilities are lost; what guarantees are preserved
  - Explicit name for this mode (proposal: "conventional fallback mode")
- 12.4 The watchdog problem
  - Conventional watchdog can be preempted by what it monitors
  - AI watchdog monitoring AI has infinite regress
  - Resolution: the Circuit Breaker (Section 13)

---

### Part IV: Formal Foundations (The differentiator) **[ENTIRELY NEW]**

#### 13. Morphism-Grounded Interface Specification [E]
- 13.1 The Wymore formalism for system interfaces
  - System Z = (X, Y, S, T, Omega, delta, lambda) — the five-tuple
  - Kernel as Z_k, AI control plane as Z_ai
  - The interface contract as morphism h: Z_ai → Z_k
- 13.2 Structural morphism quality (S_a)
  - Degree of homomorphism: average reciprocal mapping cardinality across states, inputs, outputs
  - S_a declining = AI control plane's model of kernel state diverging from reality
  - Measurable, monitorable, computable at runtime
- 13.3 Behavioral morphism quality (C_r)
  - Output distance D = max_t |y_ai(t) - y_k(t)|
  - C_r declining = AI policy decisions producing unexpected outcomes
  - The two axes (structural, behavioral) are orthogonal — both required
- 13.4 The Circuit Breaker as watchdog
  - Monitors S_a and C_r continuously
  - Trip conditions expressed as SHACL constraints (from CBTO v4.0)
  - Simpler than the AI control plane by construction (two scalar metrics vs. thresholds)
  - Cannot be compromised by the AI control plane (operates on observable system metrics, not AI-generated text)
  - On trip: transition to conventional fallback mode (Section 12.3)
- 13.5 Composition correctness via morphism composition
  - Agent A delegates to B: composed system (A compose B) should preserve morphism quality
  - Violation (quality of composed morphism < quality of A alone) triggers re-sync or rollback
  - Extension path: multi-agent composition as category of morphisms (future work)
- 13.6 Connection to DARPA CLARA
  - "Compositional Learning-And-Reasoning" = compositional morphisms with verifiable quality bounds
  - The AI-OS formal framework IS the CLARA architecture applied to the OS domain
  - Polynomial-time complexity requirement: morphism quality can be computed in O(n) per monitoring cycle

#### 14. Ontological Grounding [E]
- 14.1 CBTO as the OS governance ontology
  - OWL 2 DL, BFO 2020 aligned, 25 classes, 20 object properties, 12 data properties
  - Reusable for AI-OS: TrustMetric, SystemModel, MorphismRelation classes apply directly
  - Extension needed: AgentState, ResourceBinding, SchedulingPolicy classes
- 14.2 SHACL validation pipeline for AI-OS governance
  - Two-tier: syntax advisory (fast, non-blocking) + full validation (SHACL + SPARQL CQs, blocking)
  - Adapted from GI-JOE ontology-gate.sh pattern
  - Competency questions for AI-OS (candidate set of 10-15 CQs)
- 14.3 Relation to portfolio ontology
  - AIOS-WySE as a new individual in the portfolio ABox
  - Cross-references to existing ontology entities (WySE, CBTO, claude-flow)

---

### Part V: Reference Architectures and Roadmap

#### 15. Reference Architectures (Revised) [P/E]
- 15.1 Architecture A: AI-augmented conventional OS
  - What stays conventional: everything
  - Where AI sits: user-space applications and system services
  - Deployed examples: Copilot+ PC, Apple Intelligence, Android AICore
  - Main advantage: fastest adoption, lowest risk
  - Main weakness: AI remains peripheral, no formal governance
- 15.2 Architecture B: AI-native control plane over conventional substrate (recommended)
  - What stays conventional: boot, isolation, memory safety, interrupt handling, device mediation
  - Where AI sits: primary policy/orchestration layer above substrate
  - Interface contract: Section 9's API specification
  - Watchdog: Circuit Breaker (Section 13)
  - Near-term prototype path: eBPF + sched_ext + cgroups v2 on Linux
  - **[NEW]** Detailed component diagram (C4 level 2)
  - **[NEW]** Sequence diagrams for: agent launch, resource allocation decision, failure recovery
- 15.3 Architecture C: Microkernel/high-assurance substrate + AI services
  - What stays conventional: small trusted core (seL4-class)
  - Where AI sits: isolated services above the core
  - Strongest security/safety story; highest integration cost
  - The verification cost problem (seL4 = ~20 person-years for ~10K LoC)
  - **[NEW]** Formal methods + AI: vericoding, LLM-assisted proof generation (Selene framework)
- 15.4 Architecture D: Clean-sheet AI OS
  - Models, tools, agents as first-class entities
  - AIOS v5, MemOS as research exemplars
  - Maximum conceptual freedom; immature, ecosystem-poor
  - **[NEW]** WASM/WASI as a possible substrate (library OS for AI)
- Table 6: revised comparison with interface contract, watchdog, state model columns

#### 16. Safety-Critical Considerations [E] **[NEW]**
- 16.1 The certification gap
  - DO-178C (avionics) and ISO 26262 (automotive) assume deterministic, statically analyzable software
  - Neural networks violate MC/DC coverage, freedom from interference, static analyzability
  - ISO/DPAS 8800 (AI safety for automotive) in progress but not ratified
- 16.2 Mixed-criticality AI OS
  - Safety-critical functions in certified RTOS partitions (ARINC 653 temporal/spatial isolation)
  - AI advisory functions in separate partition with no safety guarantee
  - AUTOBEST as kernel-level mechanism
  - The only technically defensible near-term architecture for safety-critical AI-OS domains
- 16.3 Path to certifiable AI components
  - Runtime monitors (Circuit Breaker) as safety mechanism — monitor is certifiable even if AI is not
  - Proof-carrying code for AI policy modules (future work)
  - The separation argument: if the AI control plane is provably non-safety-critical (can be removed and system continues), certification applies only to the conventional substrate

#### 17. Roadmap and Open Questions [L/P/E]
- 17.1 Phase 0: AI-augmented operations (current state, 2024-2026)
  - NL search, diagnostic assistance, policy drafting, developer support
  - TRL 4-6 (lab validated to system demonstrated)
- 17.2 Phase 1: Bounded policy automation (2025-2027)
  - Workload placement, resource tuning, tool invocation under policy limits
  - eBPF + sched_ext prototypes, cgroup-aligned agent boundaries
  - TRL 3-5 (proof of concept to component validated)
- 17.3 Phase 2: AI-native control plane (2026-2029)
  - Agents as managed system entities with scheduling, memory, access control
  - Circuit Breaker watchdog operational
  - Formal interface contract implemented and verified
  - TRL 2-4 (technology formulated to lab validated)
- 17.4 Phase 3: Heterogeneous resource fabric (2028-2032)
  - Distributed AI-OS spanning CPUs, NPUs, DPUs, disaggregated memory
  - Cross-node agent migration with consistent state
  - TRL 1-3 (basic principles to proof of concept)
- 17.5 Open research questions (10-15 precisely stated questions)
  - Which decisions must remain deterministic?
  - What is the right contract between kernel, models, and agent services?
  - How should provenance, rollback, and attestation work for AI-driven actions?
  - How can transfer learning and continual learning be exploited without destabilizing the platform?
  - What is the right boundary between a node OS and a distributed agent-control fabric?
  - Can morphism quality metrics be standardized across AI-OS implementations?
  - What is the minimum formal verification investment for a credible AI-native control plane?
  - How does agent state persistence interact with confidential computing constraints?
  - What governance structures prevent prompt injection from becoming a systemic OS vulnerability?
  - How should mixed-criticality partitioning evolve as AI components become more capable?

---

### Back Matter

#### Appendix A: Boundary Test (retained from ChatGPT draft, expanded)
#### Appendix B: Glossary of Terms [L]
#### Appendix C: Comparison with Existing AI-OS Projects (AIOS, MemOS, PunkGo, claude-flow)
#### Appendix D: Candidate AI-Kernel Interface Primitives (IDL notation)
#### Appendix E: CBTO Extension for AI-OS Governance (OWL 2 DL class additions)
#### Appendix F: Numbered References (target: 80-100 references)

---

## Derivative Deliverables

### Executive Brief (3-5 pages)
Extracted from: Sections 1.1, 2.1, 7.1, 7.3 (industry evidence), 15 (Table 6), 17.1-17.4
Tone: No equations, no IDL, no ontology notation. Clear English with decision-relevant framing.
Audience: NNSA program managers, university administrators, non-technical collaborators.

### Practitioner Guide (15-20 pages)
Extracted from: Sections 1-8, 9 (API overview without IDL), 11 (threat model and isolation tiers), 12.3 (degraded mode), 15 (architectures with component diagrams), 16.2 (mixed-criticality summary), 17
Tone: Technical but implementation-focused. "Here's what you need to build." Includes tables and diagrams.
Audience: Software architects, AI platform engineers, systems engineers evaluating AI-OS designs.

---

## Key Differentiators vs. ChatGPT Draft

| Dimension | ChatGPT Draft | AIOS-WySE |
|---|---|---|
| "OS for AI" vs. "AI for OS" | Conflated | Explicitly split in Section 1 |
| Interface contract | Named, not designed | Specified API (Section 9) |
| Agent state management | Not addressed | Full architecture (Section 10) |
| Security model | Brief TEE mention | Threat model + 5-tier isolation + capability model (Section 11) |
| Failure modes | "Safe fallbacks" once | Failure taxonomy + FMEA table + degraded mode (Section 12) |
| Formal grounding | None | WySE morphisms + Circuit Breaker + CBTO (Sections 13-14) |
| Industry evidence | None (published Mar 6) | Microsoft, Apple, Google deployments (Section 7.3) |
| References | 46 (mostly documentation) | 80-100 (primary research + documentation) |
| Audience layering | Reading guide (text) | Audience markers + 3 derivative deliverables |
| Missing literature | ~20 key papers absent | AgentCgroup, MemOS, PunkGo, SEAgent, etc. all integrated |
| Safety-critical | AUTOSAR/ARINC named | DO-178C/ISO 26262 gap analyzed, mixed-criticality designed (Section 16) |
| Roadmap | Phases without metrics | TRL-referenced milestones (Section 17) |

---

## Estimated Effort
- Full technical report: 5-8 sessions (writing + research iterations)
- Executive brief: 1 session (extraction + editing)
- Practitioner guide: 1-2 sessions (extraction + editing)
- Figures and diagrams: 2-3 sessions (C4 diagrams, sequence diagrams, tables)
- Reference verification: 1 session (confirm all URLs, check arXiv versions)
- Total: ~10-14 sessions

## Connection to Other Active Work
- DARPA CLARA (Apr 10): Sections 13-14 become the formal methods section of the full proposal
- NNSA Roadmap: Section 17 feeds directly into "beyond the horizon" capabilities assessment
- AI Swarm Productivity paper: AIOS-WySE writing sessions generate scorecard data
- WySE Ontology Stack: Sections 13-14 force the ontology formalization that's been overdue
- AI Circuit Breaker: Section 12-13 extend CBTO to the OS domain (new contribution)
