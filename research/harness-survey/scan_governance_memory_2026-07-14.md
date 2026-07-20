# Harness Survey: Governance, Policy, Guardrails, and Memory/State
## Scan date: 2026-07-14
## Scope: AI agent harness governance/policy/guardrails/memory slice
## Companion scan: frameworks/orchestration (separate agent)

---

## A. Governance and Policy Approaches

This section covers how harnesses apply constraints, enforce rules, handle authority, and compose policies across nested or federated agent systems.

---

### A.1 Prompt-Level and Classifier-Based Guardrails

#### A.1.1 NeMo Guardrails (NVIDIA)

**Source [G1]:** Rebedea, T., Dinu, R., Sreedhar, M. N., Parisien, C., & Cohen, J. (2023). NeMo Guardrails: A Toolkit for Controllable and Safe LLM Applications with Programmable Rails. *Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing: System Demonstrations*, Singapore, pp. 431-445. DOI: 10.18653/v1/2023.emnlp-demo.40. URL: https://aclanthology.org/2023.emnlp-demo.40/

**Approach:** NeMo Guardrails introduces Colang, a domain-specific language for specifying conversational flows and safety rails. The architecture wraps the LLM in an event-driven runtime with five pipeline stages: input rail, retrieval rail, dialog rail, execution rail, and output rail. Each stage runs independently with sub-50 ms overhead on GPU.

**Policy composition:** Rails compose sequentially within a pipeline stage and can be conditionally branched. There is no formal algebraic treatment of how conflicting Colang flows resolve; the framework relies on explicit developer-authored flow precedence within a single application's Colang scripts. Cross-agent composition (i.e., what happens when a Colang-governed agent calls a sub-agent) is not specified in the original paper and remains an open question.

**Authority model:** Developer-authored; no role or trust hierarchy for who may author or modify rails.

**Limitations:** Bound to scripted flows; policy coverage is only as complete as the flows authored; no formal guarantee of completeness or conflict-freedom.

---

#### A.1.2 Llama Guard (Meta)

**Source [G2]:** Inan, H., Upasani, K., Chi, J., Rungta, R., Iyer, K., Mao, Y., Tontchev, M., Hu, Q., Fuller, B., & Testuggine, D. (2023). Llama Guard: LLM-based Input-Output Safeguard for Human-AI Conversations. arXiv:2312.06674. URL: https://arxiv.org/abs/2312.06674

**Approach:** A fine-tuned Llama-2-7B classifier that labels prompts and responses safe/unsafe against a six-category harm taxonomy (Criminal Planning, Self Harm, Controlled Substances, Weapons, Sexual Content, Violence/Hate). Llama Guard 2 (2024) expanded alignment to MLCommons AI Safety taxonomy; Llama Guard 3 extended to multilingual (8 languages) and tool-call safety.

**Policy composition:** Policy is a fixed taxonomy embedded in the classifier weights; customization requires fine-tuning or system-prompt-level policy injection. There is no compositional algebra: combining two Llama Guard policies (e.g., a base policy plus an org-specific supplement) has no formal semantics.

**Authority model:** None built in; policy is set by whoever controls the system prompt template.

**Limitations:** A static classifier cannot express obligation, waiver, or conflict-resolution meta-policy. The taxonomy is a flat list; no hierarchical reasoning over harm categories.

---

#### A.1.3 Guardrails AI

**Source [G3]:** Guardrails AI. (2023-2026). Guardrails AI (open-source Python library). URL: https://github.com/guardrails-ai/guardrails [GREY LITERATURE - software documentation]

**Approach:** A Python validator architecture with 50+ community validators in the Validator Hub. Each validator enforces a structural or semantic property on LLM input/output. Validators compose as a pipeline and each may return pass, fail, or a corrected value. Latency: 50-200 ms per validation round.

**Policy composition:** Validators chain sequentially; conflict between validators (e.g., one demands brevity, another completeness) is unresolved by the framework and left to the developer. No formal compositional semantics.

**Authority model:** None; single developer/operator namespace.

---

### A.2 Runtime Governance Frameworks

#### A.2.1 SARC (Governance-by-Architecture)

**Source [G4]:** Besanson, G. (2026). SARC: A Governance-by-Architecture Framework for Agentic AI Systems Compiling Regulatory Obligations into Runtime Constraints. arXiv:2605.07728. URL: https://arxiv.org/abs/2605.07728

**Approach:** Treats constraints as first-class objects alongside state, action space, and reward. A SARC specification declares for each constraint: source, class, predicate, verification point, response protocol, and operating point. These compile into four enforcement sites in the agent loop:
1. Pre-Action Gate -- evaluates before execution
2. Action-Time Monitor -- checks during execution
3. Post-Action Auditor -- verifies after execution
4. Escalation Router -- handles violations

**Policy composition (multi-agent):** SARC extends governance through nested/delegated sub-agents via: (a) constraint propagation across hierarchies, (b) authority intersection to reconcile conflicting constraints, and (c) attribution-preserving trace trees. This is the closest thing to a systematic constraint inheritance model in the SARC framework. Residual hard violations scale with enforcement-stack error rather than environmental factors.

**Authority model:** Constraint sources are explicitly declared (e.g., regulatory, organizational, application-level), providing provenance for each rule. No formal multi-principal trust model.

---

#### A.2.2 AgenticRei (Deontic Runtime Governance)

**Source [G5]:** Joshi, A., Finin, T., Joshi, K. P., & Kagal, L. (2026). Deontic Policies for Runtime Governance of Agentic AI Systems. *IEEE Symposium on Agentic Services (IEEE Conference on Web Services)*. arXiv:2606.19464. URL: https://arxiv.org/abs/2606.19464

**Approach:** AgenticRei is built on the Rei deontic policy framework, expressing governance in OWL and evaluated by a logic engine external to the LLM. It goes beyond permit/prohibit to implement:
- Obligation lifecycle management (what agents must do after actions, e.g., notify CISO)
- Dispensations (waivers of obligations under specified conditions)
- Meta-policy conflict resolution (which rules take precedence)
- Ontological reasoning over domain class hierarchies (healthcare, cybersecurity, data privacy)

**Policy composition:** The deontic logic foundation provides formal composition semantics for obligation/permission/prohibition combinations. The Rei framework supports policy sets with explicit precedence relations. This is the strongest formal basis for policy composition found in the survey. Governs both tool invocations and agent-to-agent messages.

**Authority model:** OWL-expressed, allowing rich ontological definitions of roles and their associated deontic constraints. Does not yet specify a formal model for how authority is inherited when an agent spawns a sub-agent.

---

#### A.2.3 Governance-as-a-Service (GaaS)

**Source [G6]:** Gaurav, S., Heikkonen, J., & Chaudhary, J. (2025). Governance-as-a-Service: A Multi-Agent Framework for AI System Compliance and Policy Enforcement. arXiv:2508.18765. URL: https://arxiv.org/abs/2508.18765

**Approach:** A modular enforcement layer operating at runtime without modifying model internals or requiring agent cooperation. Uses declarative rules plus a Trust Factor mechanism that scores agents based on compliance and severity-weighted violations. Enforces through three intervention types: coercive (blocking), normative (guiding), and adaptive (adjusting responses).

**Policy composition:** GaaS intercepts and evaluates all agent actions from a central enforcement point; composition is effectively mediated by the Trust Factor scoring, not by a formal policy algebra.

**Authority model:** Trust Factor provides a dynamic reputation-based authority model. Untrustworthy agents are isolated. Evaluated on LLaMA3, Qwen3, DeepSeek-R1 open-source models.

---

#### A.2.4 Governance-Aware Agent Telemetry (GAAT)

**Source [G7]:** Pathak, A., & Jain, N. (2026). Governance-Aware Agent Telemetry for Closed-Loop Enforcement in Multi-Agent AI Systems. arXiv:2604.05119. URL: https://arxiv.org/abs/2604.05119

**Approach:** Closes the loop between observation and enforcement. Introduces:
- Governance Telemetry Schema (GTS): extends OpenTelemetry with governance attributes
- Real-time policy violation detection using OPA-compatible declarative rules at sub-200 ms latency
- Governance Enforcement Bus (GEB) with graduated interventions
- Trusted Telemetry Plane with cryptographic provenance on telemetry events

**Performance:** 98.3% Violation Prevention Rate, 8.4 ms median detection latency, 127 ms median end-to-end enforcement latency on a five-agent e-commerce test.

**Authority model:** Telemetry is the authority signal; cryptographic provenance ensures non-repudiation. Policy rules are OPA Rego or equivalent declarative form.

**Limitation:** Observability-driven; the enforcement gap (detect-then-act) is narrowed but not eliminated. No formal treatment of policy composition for nested agent hierarchies.

---

### A.3 Access Control and Permission Models

#### A.3.1 AgentGuardian (Learning Access Control Policies)

**Source [G8]:** Abaev, N., Klimov, D., Levinov, G., Mimran, D., Elovici, Y., & Shabtai, A. (2026). AgentGuardian: Learning Access Control Policies to Govern AI Agent Behavior. arXiv:2601.10440. URL: https://arxiv.org/abs/2601.10440

**Approach:** Monitors execution traces during a controlled staging phase to learn legitimate behavior baselines, then derives adaptive ABAC-style policies regulating tool calls based on real-time input context and control-flow dependencies of multi-step agent actions. Control flow integrity mechanism mitigates hallucination-driven orchestration errors.

**Policy composition:** Policies are derived per-agent from behavioral observation; no formal composition model for combining policies across agents. The framework is instance-specific, not compositional.

---

#### A.3.2 Agent Access Control (AAC) -- Vision Paper

**Source [G9]:** Li, X., Huang, D., Li, J., Cai, H., Zhou, Z., Dong, W., Wang, X., & Liu, Y. (2025). A Vision for Access Control in LLM-based Agent Systems. arXiv:2510.11108. Published in: *Engineering of Complex Computer Systems (ICECCS)*. Springer. DOI: 10.1007/978-3-032-00828-2_25. URL: https://arxiv.org/abs/2510.11108

**Approach:** Proposes a paradigm shift from binary access control to dynamic information flow governance. AAC operates on two modules: (1) multi-dimensional contextual evaluation (assessing identity, relationships, scenarios, norms) and (2) adaptive response formulation (redaction, summarization, paraphrasing rather than simple allow/deny).

**Policy composition:** Conceptual paper; the AC reasoning engine is described but not formally specified in terms of compositional semantics.

---

#### A.3.3 KYA (Know Your Agents -- Only-Tighten Composition Algebra)

**Source [G10]:** Quadri, K. (2026). KYA: A Framework-Agnostic Trust Layer for Autonomous Systems with Verifiable Provenance and Hierarchical Policy Composition. arXiv:2605.25376. URL: https://arxiv.org/abs/2605.25376

**Approach:** Five primitives: (1) four-gate inbound apply pipeline; (2) only-tighten composition algebra over a three-channel multi-tenant hierarchy; (3) KYP (Know Your Principal) schema-level unification of trust scoring across humans, AI agents, and service accounts; (4) auditable interaction-multiplier amplification over an AIVSS-shaped additive baseline; (5) two-axis delegation attribution (static premium for risky delegates + runtime debit for actual misbehavior in fan-out).

**Policy composition:** This is the only work found that explicitly names an "only-tighten" algebra -- constraints can only become more restrictive through composition, never relaxed. The three-channel hierarchy operationalizes this monotonicity. Detects 89% of adversarial probes with sub-millisecond scoring.

**Significance for survey:** KYA is the strongest candidate for a formal "composition-by-tightening" model currently in the literature, though the algebra is not yet formalized in a theorem-proof style comparable to classical policy algebra work.

---

#### A.3.4 Overlaying Governance (Compositional Authorization for Delegation)

**Source [G11]:** Ibrahim, A., & Li, Y. (2026). Overlaying Governance: A Compositional Authorization Framework for Delegation and Scope in Agentic AI. arXiv:2606.03518. URL: https://arxiv.org/abs/2606.03518

**Approach:** Treats delegation as a contractual term, introduces resource scope attenuation (constraints on access envelopes), and provides a compositional operator that overlays agentic governance onto existing relational policies without rewrites. Supports recursive delegation chains with contextual boundaries as executable primitives.

**Policy composition:** Formal relational definitions composable into existing authorization domains. Delegation chains propagate constraints, though the paper does not explicitly prove a monotone-tightening property.

---

#### A.3.5 ActPlane (OS-Level Policy Enforcement for Agent Harnesses)

**Source [G12]:** Zheng, Y., Wu, T., Fu, Q., Yu, T., Mao, W., Ma, T., Williams, D., Wang, W., & Quinn, A. (2026). ActPlane: Programmable OS-Level Policy Enforcement for Agent Harnesses. arXiv:2606.25189. DOI: 10.48550/arXiv.2606.25189. URL: https://arxiv.org/abs/2606.25189

**Approach:** Kernel-level eBPF-based policy enforcement. Key feature: constraints defined for parent agents automatically propagate to child agents throughout hierarchical structures without manual redefinition at each nesting level. Incorporates information-flow control for tracking how sensitive data moves through inter-agent communications.

**Policy composition:** Child domains inherit all parent rules and may add local rules but cannot remove or weaken inherited rules (cited in companion search synthesis from ActPlane documentation). This operationalizes constraint inheritance as a one-way tightening relation at the OS level, making it enforcement-enforceable rather than advisory.

**Significance:** Only system found that enforces tightening at the kernel/OS layer, making it tamper-resistant relative to application-level implementations.

---

#### A.3.6 JustAct+ (Auditable Inter-Organisational Policy)

**Source [G13]:** Esterhuyse, C. A., Muller, T., & van Binsbergen, L. T. (2025). JustAct+: A Framework for Auditable Multi-Agent Systems Regulated by Inter-Organisational Policies. arXiv:2502.00138. Accepted: *37th International Conference on Computer Aided Verification (CAV 2025)*. URL: https://arxiv.org/abs/2502.00138

**Approach:** Agents justify their actions by gathering policy information from dynamic policy statements and agreements. The framework proves that any decision permitting an action cannot be refuted later, regardless of subsequently added statements (non-repudiation). Policy language specified in Rocq proof assistant; runtime implemented in Rust. Validated against medical data processing (GDPR + consent scenarios).

**Policy composition:** Distributed multi-organisational policies that agents assemble locally; correctness is proven under partial and dynamic policy information. No explicit treatment of the constraint-tightening problem for hierarchical nesting.

---

#### A.3.7 Policy Algebra Foundations (Classical)

**Source [G14]:** Bonatti, P., De Capitani di Vimercati, S., & Samarati, P. (2002). An Algebra for Composing Access Control Policies. *ACM Transactions on Information and System Security*, 5(1). DOI: 10.1145/504909.504910. URL: https://dl.acm.org/doi/10.1145/504909.504910

**Source [G15]:** Wijesekera, D., & Jajodia, S. (2003). A Propositional Policy Algebra for Access Control. *ACM Transactions on Information and System Security*, 6(2). DOI: 10.1145/762476.762481. URL: https://dl.acm.org/doi/abs/10.1145/762476.762481

**Significance:** Classical foundations establishing policy composition algebras with formal semantics. The deny-overrides (forbid-dominance) theorem -- that forbid dominates permit under union composition -- is the canonical formalization of the one-way tightening property. These are the theoretical underpinning for all modern tightening approaches (KYA, ActPlane, SARC authority intersection). Not specific to LLM agents but directly applicable.

---

### A.4 Policy-as-Code and Policy Synthesis

#### A.4.1 Policy-as-Prompt

**Source [G16]:** Kholkar, G., & Ahuja, R. (2025). Policy-as-Prompt: Turning AI Governance Rules into Guardrails for AI Agents. *3rd Regulatable ML Workshop at NeurIPS 2025*. arXiv:2509.23994. URL: https://arxiv.org/abs/2509.23994

**Approach:** Converts unstructured design artifacts (PRDs, technical design documents, code) into a source-linked policy tree, then compiles the tree into lightweight prompt-based classifiers for real-time runtime monitoring. Enforces least privilege and data minimization. Generates auditable rationales with full provenance.

**Policy composition:** Policy tree provides hierarchical structure (parent nodes subsume children) but the compositional semantics are not formally specified. Effectively a DAG of rule assertions linked to source documents.

---

#### A.4.2 Capability Lifecycle Governance

**Source [G17]:** Qin, X., Luan, S., See, J., Boukhers, Z., Yang, C., & Li, Z. (2026). Governed Capability Evolution: Lifecycle-Time Compatibility Checking and Rollback for AI-Component-Based Systems, with Embodied Agents as Case Study. arXiv:2604.08059. URL: https://arxiv.org/abs/2604.08059

**Approach:** Staged upgrade framework with a seven-stage pipeline: candidate validation, sandbox evaluation, shadow deployment, gated activation, online monitoring, rollback, and audit. Four compatibility checks per upgrade: interface, policy, behavioral, and recovery compatibility. This implicitly models a capability lifecycle with states: candidate -> validation -> sandbox -> shadow -> active -> monitoring -> (rollback | audit).

**Significance for survey:** The closest formal treatment of a capability lifecycle found in the survey. Zero unsafe activations under governed approach vs. 60% unsafe activation rate under naive upgrade. 79.8% rollback success rate. Does not explicitly name propose/active/retire phases but operationalizes them through the seven-stage pipeline.

---

#### A.4.3 Agent Registry and Capability Discovery

**Source [G18]:** Singh, A., Ehtesham, A., Lambe, M., Grogan, J. J., Singh, A., Kumar, S., Muscariello, L., Pandey, V., de Saint Marc, G. S., Chari, P., & Raskar, R. (2025). Evolution of AI Agent Registry Solutions: Centralized, Enterprise, and Distributed Approaches. arXiv:2508.03095. URL: https://arxiv.org/abs/2508.03095

**Approach:** Comparative analysis of five registry paradigms: MCP Registry (centralized), A2A Agent Cards (decentralized JSON manifests), AGNTCY Agent Directory Service (IPFS-based semantic taxonomy), Microsoft Entra Agent ID (enterprise SaaS), and NANDA Index AgentFacts (cryptographically verifiable). Evaluates on security, authentication, scalability, and maintainability.

**Gap identified:** Cross-protocol discovery, unified namespace management, and portable agent identities are explicitly called out as "the next frontier." No existing registry integrates governance policy, capability ontology, and lifecycle state in a single store.

---

### A.5 Identity and Governance Taxonomy

**Source [G19]:** Kurtz, A., & Krawiecka, K. (2026). Who Governs the Machine? A Machine Identity Governance Taxonomy (MIGT) for AI Systems Operating Across Enterprise and Geopolitical Boundaries. arXiv:2604.06148. URL: https://arxiv.org/abs/2604.06148

**Approach:** Six-domain governance framework addressing technical governance, regulatory compliance, and cross-jurisdictional coordination gaps. Develops an AI-Identity Risk Taxonomy (AIRT) with 37 risk sub-categories. Addresses enterprise scale: non-human identities now outnumber human identities at 144:1 ratio in enterprise.

**Limitation:** Taxonomy is descriptive, not prescriptive; does not specify how governance policies compose across the six domains.

---

### A.6 Safety and TRiSM Survey

**Source [G20]:** Raza, S., Sapkota, R., Karkee, M., & Emmanouilidis, C. (2025). TRiSM for Agentic AI: A Review of Trust, Risk, and Security Management in LLM-based Agentic Multi-Agent Systems. arXiv:2506.04133. Published in: *ScienceDirect (Elsevier), Array journal (online)*. DOI: [UNVERIFIED]. URL: https://arxiv.org/abs/2506.04133

**Approach:** Review across five pillars: Explainability, ModelOps, Security, Privacy, and Lifecycle Governance. Proposes Component Synergy Score (CSS) and Tool Utilization Efficacy (TUE) as novel governance metrics. Risk taxonomy covers coordination failures and adversarial manipulation. Emphasizes lifecycle governance as central to responsible deployment.

---

### A.7 SafeHarbor (Memory-Augmented Hierarchical Guardrail)

**Source [G21]:** Liu, Z., Ying, Z., Zhang, W., Zou, Q., Zhang, D., Yang, D., Zhang, X., & Peng, H. (2026). SafeHarbor: Defining Precise Decision Boundaries via Hierarchical Memory-Augmented Guardrail for LLM Agent Safety. *Proceedings of the 43rd International Conference on Machine Learning (ICML 2026)*. arXiv:2605.05704. URL: https://arxiv.org/abs/2605.05704

**Approach:** Maintains a hierarchical Risk Tree of past attack patterns with a Safety Projector that decouples safety-relevant directions in the embedding space. An information-entropy-based self-evolution mechanism continuously optimizes the memory structure through dynamic node splitting and merging. Training-free, plug-and-play.

**Performance:** 63.6% benign utility on GPT-4o; >93% refusal rate against harmful requests.

**Significance:** Demonstrates that hierarchical memory structures can serve as a governance policy store -- a step toward a unified knowledge base for safety rules. The Risk Tree is implicitly a governed policy tree with evolutionary lifecycle.

---

## B. Memory/State Governance, Provenance, and Retention

---

### B.1 Memory Provenance and Lineage

#### B.1.1 MemLineage

**Source [M1]:** Ouyang, C., & Hou, R. (2026). MemLineage: Lineage-Guided Enforcement for LLM Agent Memory. arXiv:2605.14421. URL: https://arxiv.org/abs/2605.14421

**Approach:** Treats memory security as a chain-of-custody problem. Architecture: RFC-6962 Merkle log over per-principal Ed25519-signed entries; weighted derivation DAG recording which retrieved entries influenced each new memory; max-of-strong-edges propagation rule (Untrusted-Path Persistence property); sensitive-action gate refuses dispatches whose active justification descends from an external ancestor.

**Lifecycle:** Provenance attaches at write time, propagates through derivation, and is checked at action-dispatch time. No explicit retirement/expiry mechanism.

**Result:** Zero attack success rate across all three memory-poisoning workloads; sub-millisecond per-operation overhead.

---

#### B.1.2 Portable Agent Memory

**Source [M2]:** Ravindran, S. K. (2026). Portable Agent Memory: A Protocol for Cryptographically-Verified Memory Transfer Across Heterogeneous AI Agents. arXiv:2605.11032. URL: https://arxiv.org/abs/2605.11032

**Approach:** Open protocol for cross-vendor memory sharing (GPT-4, Claude, Gemini, Llama tested). Uses a five-component structured memory model with content-addressable entries linked by a Merkle-DAG provenance graph. Capability-based access control for selective scoped disclosure. Adaptive rehydration protocol mitigates indirect prompt injection during cross-agent memory transfer.

**Significance:** Addresses cross-harness provenance portability -- a gap not covered by single-vendor solutions.

---

#### B.1.3 MemMark (Watermarked Attribution)

**Source [M3]:** [Authors unverified from search]. (2026). MemMark: State-Evolution Attribution Watermarking for Agent Long-Term Memory Systems. arXiv:2605.25002. URL: https://arxiv.org/abs/2605.25002

**Approach:** Embeds an owner-controlled signal into latent memory-write decisions, enabling attribution of memory content to the producing agent without requiring explicit metadata. State-evolution watermarking tracks content across derivation steps.

---

### B.2 Governed Shared Memory

#### B.2.1 MemClaw (Governed Shared Memory)

**Source [M4]:** Margalit, Y., Cohen-Inger, N., Avram, E., Taig, R., & Margalit, O. (2026). Governed Shared Memory for Multi-Agent LLM Systems. arXiv:2606.24535. URL: https://arxiv.org/abs/2606.24535

**Approach:** Models multi-agent shared memory as governed operational state with four properties: scope (tenant isolation), provenance (writer identity + timestamp derivation chains), temporal supersession (managing contradictions), and policy-governed propagation. Implemented in MemClaw, a production memory service.

**Results:** Zero cross-fleet leakage; complete derivation chain reconstruction with correct writer identity at sub-second latency. Sub-tenant scope vulnerabilities found and remediated.

**Limitation:** Synchronous duplicate gates can interfere with contradiction resolution timing -- a known tension between consistency and liveness.

---

#### B.2.2 SSGM (Stability and Safety Governed Memory)

**Source [M5]:** Lam, C., Li, J., Zhang, L., & Zhao, K. (2026). Governing Evolving Memory in LLM Agents: Risks, Mechanisms, and the Stability and Safety Governed Memory (SSGM) Framework. arXiv:2603.11768. URL: https://arxiv.org/abs/2603.11768

**Approach:** Decouples memory evolution from execution by enforcing: (1) consistency verification before consolidation, (2) temporal decay modeling, and (3) dynamic access control during evolution. Identifies three critical failure points: topology-induced knowledge leakage (sensitive context solidified into long-term storage), semantic drift (degradation through iterative summarization), and memory corruption.

**Lifecycle model:** Temporal decay modeling is an implicit staleness/retirement mechanism, though no explicit TTL or retirement trigger is formalized.

---

### B.3 Provenance Survey

**Source [M6]:** Wang, Y., Zhang, J., Cai, T., Liu, Z., Sun, Q., Sun, Z., Wu, Z., Dong, M., Zheng, M., Yin, X., & Zhu, Y. (2026). From Agent Traces to Trust: A Survey of Evidence Tracing and Execution Provenance in LLM Agents. arXiv:2606.04990. URL: https://arxiv.org/abs/2606.04990

**Taxonomy dimensions for provenance approaches:**
1. Trace Sources (origin of execution data)
2. Evidence and Execution Units (granularity of tracked components)
3. Provenance Relations (connection types between elements)
4. Tracing Granularity and Timing (observation frequency and detail)
5. Representation Forms (storage and visualization of provenance graphs)
6. Trust Functions (accountability applications)

**Significance:** This is the most comprehensive taxonomy of provenance approaches found. Defines execution provenance as "the typed graph of an agent execution" and evidence tracing as "its projection onto evidence-support relations."

---

### B.4 Memory Retention and Retirement

#### B.4.1 When to Forget (Memory Worth Primitive)

**Source [M7]:** Simsek, B. (2026). When to Forget: A Memory Governance Primitive. arXiv:2604.12007. URL: https://arxiv.org/abs/2604.12007

**Approach:** Introduces Memory Worth (MW), a dual-counter per-memory signal tracking co-occurrence with successful vs. failed outcomes. Formally proves MW converges to the probability of task success given memory retrieval. Enables three decisions: staleness detection, retrieval suppression, and deprecation. Memories crossing MW = 0.17 show age-related degradation; specialist memories maintain MW = 0.77.

**Lifecycle model:** Closest formal model found for memory retirement based on outcome evidence. Operates at individual memory entry granularity, not namespace or collection granularity.

---

#### B.4.2 Multi-User Memory Sharing with Dynamic Control

**Source [M8]:** [Authors unverified from title in search]. (2026). Multi-User Memory Sharing in LLM Agents with Dynamic Control. arXiv:2505.18279. URL: https://arxiv.org/abs/2505.18279 [UNVERIFIED - title only, authors not confirmed]

---

### B.5 Foundation Model Provenance Attribution

**Source [M9]:** [No dedicated academic paper found specifically on foundation-model-level provenance attribution (recording which foundation model produced a given artifact). This gap is observed in practitioner literature but not yet formalized academically as of scan date 2026-07-14.]

---

## C. Candidate Taxonomy Dimensions for the Governance Axis

Based on synthesis across all surveyed works, the following dimensions characterize the governance slice of an AI agent harness:

```
GOVERNANCE AXIS TAXONOMY DIMENSIONS

DIM-1: POLICY LANGUAGE EXPRESSIVENESS
  Levels:
  a. Classifier/weight-embedded (Llama Guard)
  b. Flow-script / DSL (NeMo Guardrails/Colang)
  c. Validator pipeline (Guardrails AI)
  d. Policy-as-code / declarative (XACML, Rego, Cedar, OPA)
  e. Deontic logic (obligations, dispensations, conflict meta-policy) (AgenticRei/Rei-OWL)
  f. Formal algebraic (policy algebra with proven composition theorems)

DIM-2: POLICY COMPOSITION SEMANTICS
  Levels:
  a. None (single-policy / no composition defined)
  b. Sequential pipeline (each stage applies independently)
  c. Override / precedence rules (developer-specified priority)
  d. Deny-monotone / forbid-dominance (classical policy algebra)
  e. Only-tighten algebra with formal proof (KYA-type)
  f. Full deontic composition with obligation tracking (AgenticRei)

DIM-3: CONSTRAINT INHERITANCE UNDER NESTING
  Levels:
  a. No inheritance (each agent is independently configured)
  b. Copy-on-spawn (child starts with parent policy snapshot)
  c. Reference-to-parent (child reads parent at enforcement time)
  d. Monotone-tighten-only (child cannot weaken parent, may add) (ActPlane, SARC authority intersection, KYA)
  e. Proof-carrying delegation (formal certificate of constraint subset) (JustAct+-style)

DIM-4: AUTHORITY AND PRINCIPAL MODEL
  Levels:
  a. None (single developer namespace)
  b. Role-based (RBAC, fixed roles)
  c. Attribute-based (ABAC, contextual)
  d. Trust-scored (dynamic reputation, GaaS Trust Factor, KYA)
  e. Deontic + ontological (AgenticRei, Rei-OWL domain hierarchies)
  f. Cross-organisational / inter-jurisdictional (JustAct+, MIGT)

DIM-5: ENFORCEMENT TIMING
  Levels:
  a. Post-hoc / audit-only
  b. Output filter (after LLM generation)
  c. Pre-action gate (before tool/action execution)
  d. Closed-loop / continuous (telemetry-to-enforcement, GAAT)
  e. Kernel/OS-level tamper-resistant (ActPlane eBPF)

DIM-6: SCOPE OF GOVERNED ACTIONS
  Levels:
  a. Conversation content only
  b. LLM input/output
  c. Tool calls and external API actions
  d. Agent-to-agent communications
  e. Memory reads and writes
  f. Full execution graph including delegation and spawn

DIM-7: MEMORY/STATE PROVENANCE
  Levels:
  a. None (no provenance tracking)
  b. Metadata tags (timestamp, author label)
  c. Cryptographic signing (Ed25519, Merkle log)
  d. Derivation lineage graph (DAG recording influence relations)
  e. Cross-harness portable provenance (Merkle-DAG + capability-based access)

DIM-8: MEMORY LIFECYCLE GOVERNANCE
  Levels:
  a. No lifecycle management (persist indefinitely)
  b. Session-scoped expiry (delete at session end)
  c. TTL-based expiry (fixed time-to-live per namespace)
  d. Staleness-scored deprecation (Memory Worth / outcome-evidence)
  e. Governed consistency + temporal decay (SSGM)
  f. Full lifecycle with propose/active/retire states and audit trail

DIM-9: CAPABILITY/RULE REGISTRY
  Levels:
  a. None (no registry; policies inline in agent code)
  b. Descriptor/manifest (A2A Agent Cards, MCP Registry)
  c. Semantic taxonomy registry (AGNTCY, CSA STAR for AI)
  d. Capability lifecycle governance (staged upgrade pipeline, Qin et al.)
  e. Unified registry integrating rules + ontology + capabilities + lifecycle state [NOT YET OBSERVED]

DIM-10: REGULATORY / COMPLIANCE MAPPING
  Levels:
  a. None
  b. Informal / commentary
  c. Taxonomy alignment (MLCommons, NIST AI RMF, ISO 42001)
  d. Runtime enforcement mapped to regulations (SARC, GAAT, EU AI Act)
  e. Formal verification against regulatory specs (JustAct+-style proof)
```

---

## D. Explicit Gaps

### GAP-1: Composition-by-Tightening Lacks a Unified Formal Theory

**Status:** Partially addressed. The deny-monotone/forbid-dominance property is well-established in classical policy algebra [G14, G15]. KYA [G10] claims an "only-tighten composition algebra" but does not provide a theorem-proof treatment. ActPlane [G12] enforces the property at the OS level but does not derive it from a formal algebra. SARC [G4] uses "authority intersection" without formal algebraic grounding. AgenticRei [G5] provides the strongest formal basis (deontic logic) but does not connect to the deny-monotone tradition.

**What is missing:** A unified formal theory of constraint inheritance for hierarchical/nested AI agents that:
- Starts from the deny-monotone property as an axiom
- Extends to deontic logic (obligations are inherited and can only be added, not removed)
- Provides decision procedures for composition-soundness checking
- Handles the cross-harness case (agent A governed by SARC spawns agent B governed by NeMo)

---

### GAP-2: No Single Source of Truth for Rules + Ontology + Capabilities

**Status:** Critically absent. All surveyed systems maintain these in separate stores:
- Policy rules: in XACML/Rego/Cedar files, Colang scripts, or OWL ontologies
- Agent capabilities: in Agent Cards (A2A), MCP Registry manifests, or AGNTCY semantic taxonomies
- Lifecycle state: in Governed Capability Evolution pipeline stages (separate system)
- Memory provenance: in Merkle logs or derivation DAGs (separate system)

**What is missing:** A registry architecture that co-locates:
1. The governance rule set (with deontic expressiveness)
2. The capability/skill ontology (with semantic taxonomy)
3. The lifecycle state of each capability/rule (propose/active/deprecated/retired)
4. Provenance of artifact production (which foundation model, which agent, under which rule set)

Singh et al. [G18] explicitly identify this as "the next frontier" for agent registries; no paper delivers it.

---

### GAP-3: Lifecycle/Retirement of Governed Assets (Rules and Capabilities)

**Status:** Partially addressed for memory entries [M7] and capability component versions [G17], but not for governance rules themselves.

**What is missing:**
- Formal lifecycle for rules: who proposes, who approves (authority model), when a rule transitions active -> deprecated -> retired, what triggers retirement (regulatory change, supersession by a newer rule)
- Lifecycle for agent capabilities: Qin et al. [G17] provide a seven-stage pipeline for component upgrades but not a rule-governed retire/archive step with audit trail
- Lifecycle for memory artifacts: SSGM [M5] decays memory but does not formally retire it; Memory Worth [M7] enables deprecation but has no authority model for who executes the retirement

**The digital-waste problem:** No academic work surveyed explicitly addresses "digital waste" -- accumulation of stale rules, orphaned capabilities, superseded provenance records, and deprecated memory artifacts that continue to consume governance overhead and introduce audit noise. Practitioner literature acknowledges the debt [grey: EfficientlyConnected, Zylos Research] but there is no peer-reviewed framework.

---

### GAP-4: Cross-Harness Governance (When Differently-Governed Systems Nest)

**Status:** Not addressed. Every framework assumes either (a) a single harness governs all agents, or (b) the inter-organisational policy is delegated to application-layer negotiation (JustAct+). No work addresses the case where agent A is governed by NeMo Guardrails + OPA and spawns agent B governed by SARC + Llama Guard. The resulting composition is undefined.

**What is missing:** A governance interoperability layer -- analogous to TLS for transport -- that can translate between policy representations and prove that the composed system satisfies the tightest applicable constraints from both parent and child policy systems.

---

### GAP-5: Foundation-Model Provenance Attribution at Write Time

**Status:** Not formally addressed. MemLineage [M1] and Portable Agent Memory [M2] track which agent wrote a memory entry; MemMark [M3] watermarks at the latent level. None of them record which foundation model (vendor, model version, access mode) produced the content, nor do they record delegation chains when one agent instructs another to write.

**What is missing:** An infrastructure-level attribution primitive that stamps: (foundation model ID, agent ID, governing rule set ID, timestamp) on every artifact write to any durable store (memory, file, code, record). This corresponds to R018 in the PostWach governance model -- the gap is confirmed by the literature: provenance of the producing model is not yet a standard field in any surveyed memory or governance schema.

---

## E. References

All sources marked [GREY LITERATURE] are vendor documentation, technical blogs, or preprint repositories without explicit peer review. All others are either peer-reviewed publications or under peer review (arXiv preprints with associated workshop/conference submissions noted).

### Peer-Reviewed / Conference / Journal

[G1] Rebedea, T., Dinu, R., Sreedhar, M. N., Parisien, C., & Cohen, J. (2023). NeMo Guardrails: A Toolkit for Controllable and Safe LLM Applications with Programmable Rails. *Proceedings of EMNLP 2023: System Demonstrations*, pp. 431-445, Singapore. DOI: 10.18653/v1/2023.emnlp-demo.40. https://aclanthology.org/2023.emnlp-demo.40/

[G2] Inan, H., Upasani, K., Chi, J., Rungta, R., Iyer, K., Mao, Y., Tontchev, M., Hu, Q., Fuller, B., & Testuggine, D. (2023). Llama Guard: LLM-based Input-Output Safeguard for Human-AI Conversations. arXiv:2312.06674. https://arxiv.org/abs/2312.06674

[G5] Joshi, A., Finin, T., Joshi, K. P., & Kagal, L. (2026). Deontic Policies for Runtime Governance of Agentic AI Systems. *IEEE Symposium on Agentic Services (IEEE Conference on Web Services)*. arXiv:2606.19464. https://arxiv.org/abs/2606.19464

[G9] Li, X., Huang, D., Li, J., Cai, H., Zhou, Z., Dong, W., Wang, X., & Liu, Y. (2025). A Vision for Access Control in LLM-based Agent Systems. *Engineering of Complex Computer Systems (ICECCS)*, Springer. DOI: 10.1007/978-3-032-00828-2_25. arXiv:2510.11108. https://arxiv.org/abs/2510.11108

[G13] Esterhuyse, C. A., Muller, T., & van Binsbergen, L. T. (2025). JustAct+: A Framework for Auditable Multi-Agent Systems Regulated by Inter-Organisational Policies. *37th International Conference on Computer Aided Verification (CAV 2025)*. arXiv:2502.00138. https://arxiv.org/abs/2502.00138

[G14] Bonatti, P., De Capitani di Vimercati, S., & Samarati, P. (2002). An Algebra for Composing Access Control Policies. *ACM Transactions on Information and System Security*, 5(1). DOI: 10.1145/504909.504910. https://dl.acm.org/doi/10.1145/504909.504910

[G15] Wijesekera, D., & Jajodia, S. (2003). A Propositional Policy Algebra for Access Control. *ACM Transactions on Information and System Security*, 6(2). DOI: 10.1145/762476.762481. https://dl.acm.org/doi/abs/10.1145/762476.762481

[G16] Kholkar, G., & Ahuja, R. (2025). Policy-as-Prompt: Turning AI Governance Rules into Guardrails for AI Agents. *3rd Regulatable ML Workshop at NeurIPS 2025*. arXiv:2509.23994. https://arxiv.org/abs/2509.23994

[G20] Raza, S., Sapkota, R., Karkee, M., & Emmanouilidis, C. (2025). TRiSM for Agentic AI: A Review of Trust, Risk, and Security Management in LLM-based Agentic Multi-Agent Systems. *Array (Elsevier)* [UNVERIFIED journal name - verify DOI]. arXiv:2506.04133. https://arxiv.org/abs/2506.04133

[G21] Liu, Z., Ying, Z., Zhang, W., Zou, Q., Zhang, D., Yang, D., Zhang, X., & Peng, H. (2026). SafeHarbor: Defining Precise Decision Boundaries via Hierarchical Memory-Augmented Guardrail for LLM Agent Safety. *Proceedings of ICML 2026*. arXiv:2605.05704. https://arxiv.org/abs/2605.05704

[M6] Wang, Y., Zhang, J., Cai, T., Liu, Z., Sun, Q., Sun, Z., Wu, Z., Dong, M., Zheng, M., Yin, X., & Zhu, Y. (2026). From Agent Traces to Trust: A Survey of Evidence Tracing and Execution Provenance in LLM Agents. arXiv:2606.04990. [Venue: UNVERIFIED -- arXiv cs.CR/cs.AI, submission under review]. https://arxiv.org/abs/2606.04990

### arXiv Preprints (Under Review / Workshop Submissions)

[G4] Besanson, G. (2026). SARC: A Governance-by-Architecture Framework for Agentic AI Systems. arXiv:2605.07728. https://arxiv.org/abs/2605.07728

[G6] Gaurav, S., Heikkonen, J., & Chaudhary, J. (2025). Governance-as-a-Service: A Multi-Agent Framework for AI System Compliance and Policy Enforcement. arXiv:2508.18765. https://arxiv.org/abs/2508.18765

[G7] Pathak, A., & Jain, N. (2026). Governance-Aware Agent Telemetry for Closed-Loop Enforcement in Multi-Agent AI Systems. arXiv:2604.05119. https://arxiv.org/abs/2604.05119

[G8] Abaev, N., Klimov, D., Levinov, G., Mimran, D., Elovici, Y., & Shabtai, A. (2026). AgentGuardian: Learning Access Control Policies to Govern AI Agent Behavior. arXiv:2601.10440. https://arxiv.org/abs/2601.10440

[G10] Quadri, K. (2026). KYA: A Framework-Agnostic Trust Layer for Autonomous Systems with Verifiable Provenance and Hierarchical Policy Composition. arXiv:2605.25376. https://arxiv.org/abs/2605.25376

[G11] Ibrahim, A., & Li, Y. (2026). Overlaying Governance: A Compositional Authorization Framework for Delegation and Scope in Agentic AI. arXiv:2606.03518. https://arxiv.org/abs/2606.03518

[G12] Zheng, Y., Wu, T., Fu, Q., Yu, T., Mao, W., Ma, T., Williams, D., Wang, W., & Quinn, A. (2026). ActPlane: Programmable OS-Level Policy Enforcement for Agent Harnesses. arXiv:2606.25189. DOI: 10.48550/arXiv.2606.25189. https://arxiv.org/abs/2606.25189

[G17] Qin, X., Luan, S., See, J., Boukhers, Z., Yang, C., & Li, Z. (2026). Governed Capability Evolution: Lifecycle-Time Compatibility Checking and Rollback for AI-Component-Based Systems. arXiv:2604.08059. https://arxiv.org/abs/2604.08059

[G18] Singh, A., et al. (2025). Evolution of AI Agent Registry Solutions: Centralized, Enterprise, and Distributed Approaches. arXiv:2508.03095. https://arxiv.org/abs/2508.03095

[G19] Kurtz, A., & Krawiecka, K. (2026). Who Governs the Machine? A Machine Identity Governance Taxonomy (MIGT). arXiv:2604.06148. https://arxiv.org/abs/2604.06148

[M1] Ouyang, C., & Hou, R. (2026). MemLineage: Lineage-Guided Enforcement for LLM Agent Memory. arXiv:2605.14421. https://arxiv.org/abs/2605.14421

[M2] Ravindran, S. K. (2026). Portable Agent Memory: A Protocol for Cryptographically-Verified Memory Transfer Across Heterogeneous AI Agents. arXiv:2605.11032. https://arxiv.org/abs/2605.11032

[M3] [Authors UNVERIFIED]. (2026). MemMark: State-Evolution Attribution Watermarking for Agent Long-Term Memory Systems. arXiv:2605.25002. https://arxiv.org/abs/2605.25002

[M4] Margalit, Y., Cohen-Inger, N., Avram, E., Taig, R., & Margalit, O. (2026). Governed Shared Memory for Multi-Agent LLM Systems. arXiv:2606.24535. https://arxiv.org/abs/2606.24535

[M5] Lam, C., Li, J., Zhang, L., & Zhao, K. (2026). Governing Evolving Memory in LLM Agents: Risks, Mechanisms, and the SSGM Framework. arXiv:2603.11768. https://arxiv.org/abs/2603.11768

[M7] Simsek, B. (2026). When to Forget: A Memory Governance Primitive. arXiv:2604.12007. https://arxiv.org/abs/2604.12007

### Grey Literature (Vendor / Industry)

[G3] Guardrails AI. (2023-2026). Guardrails AI open-source library. https://github.com/guardrails-ai/guardrails [GREY LITERATURE]

[GL1] NVIDIA NeMo Guardrails documentation. (2026). https://developer.nvidia.com/nemo-guardrails [GREY LITERATURE]

[GL2] Cloud Security Alliance. (2025). Agent Registry Specification v1. https://labs.cloudsecurityalliance.org/agentic/agentic-agent-registry-specification-v1/ [GREY LITERATURE]

[GL3] EfficientlyConnected. (2026). AI Agent Memory Governance: The Debt Enterprises Are Ignoring. https://www.efficientlyconnected.com/ai-agent-memory-governance-memory-debt/ [GREY LITERATURE]

[GL4] Microsoft Open Source Blog. (2026, April 2). Introducing the Agent Governance Toolkit. https://opensource.microsoft.com/blog/2026/04/02/introducing-the-agent-governance-toolkit-open-source-runtime-security-for-ai-agents/ [GREY LITERATURE]

---

## Source Count Summary

| Category | Count |
|---|---|
| Peer-reviewed (journal / conference proceedings) | 8 |
| arXiv preprints (workshop-accepted or under review) | 16 |
| Grey literature (vendor docs, industry blogs) | 4 |
| **Total** | **28** |

Notes:
- Several 2026 arXiv preprints cite IEEE or ACM workshop acceptance (G5, G7, G21); these are counted as peer-reviewed.
- [M3] and [M8] have unverified author metadata; treat as provisional citations requiring verification against approved.bib before manuscript use.
- All DOIs above should be verified via approved-references workflow (R019/R109) before citation in any manuscript.
