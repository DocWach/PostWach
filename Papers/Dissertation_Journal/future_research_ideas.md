# Future Research Ideas

*Repository for research directions identified during the dissertation-to-journal conversion project*

---

## Overarching Research Program Vision

**Informal Objective:** Learn the fundamental, transdisciplinary patterns that establish systems engineering as truly domain agnostic.

**Three Overarching Impacts:**

1. **Education:** Explores whether (or the extent to which) systems engineering is a fundamental discipline that should be studied as part of all engineering programs — not merely a graduate specialization but a foundational science of engineered systems.
2. **Practice:** Establishes reuse of engineering knowledge across domains through a scientific (rather than heuristic) approach — enabling engineers to formally transfer solutions between domains with quantified confidence.
3. **Fundamental science:** Challenges and/or confirms assumptions — provides formal tools to test whether the cross-domain patterns engineers rely on are mathematically valid, and to what degree.

**Relationship to Individual Proposals:** The 26 ideas below constitute a research portfolio. Individual grant proposals (e.g., NSF EDSE) should be scoped to specific, granular subsets of this portfolio while connecting to this overarching vision. The first planned proposal focuses on verification model fidelity (Ideas 5, 6, 3, 20, 21, 23).

*Vision captured: February 16, 2026*

---

## 1. Mathematical Rigor Analysis of SysML v2

**Working Title:** *A Critical Analysis of the Mathematical Foundations of SysML v2 Verification Constructs*

**Problem Statement:**
SysML v2 introduces verification constructs (VerificationCase, VerdictKind, RequirementVerificationMembership) that improve modeling capabilities over v1, but the language lacks mathematical rigor for verification model definition.

**Key Gaps Identified:**
- No relationship between verification model and system design (same as v1)
- No theoretical foundation for *how* to define verification models
- No mathematical characterization of representativeness
- No quantitative fidelity conditions
- Descriptive rather than prescriptive approach

**Research Approach:**
- Extend Table 4 comparison (Wach & Salado, 2024) to include SysML v2
- Systematic analysis of SysML v2 verification constructs against WySE metamodel
- Identify what SysML v2 can/cannot express mathematically
- Propose extensions or complementary frameworks

**SysML v2 Verification Constructs (from stdlib):**
| Construct | Description |
|-----------|-------------|
| VerificationCase | Main element for verification activities |
| VerificationCaseDefinition/Usage | Definition and usage patterns |
| VerdictKind | Enumeration: pass, fail, inconclusive, error |
| VerificationMethodKind | Enumeration: inspect, analyze, demo, test |
| RequirementVerificationMembership | Links verification to requirements via verifiedRequirement |
| RequirementCheck | Evaluation of requirements within verification objectives |
| SatisfyRequirementUsage | Asserts a feature satisfies a requirement |

**Draft Comparison Table (SysML v2 vs WySE):**

| Aspect | SysML v2 | WySE |
|--------|----------|------|
| VM ↔ System Requirements | Explicit via verifiedRequirement | Explicit, quantitative |
| VM ↔ Verification Requirements | Explicit via VerificationCase | Explicit, quantitative |
| VM ↔ System Design | **Does not exist** | Explicit, quantitative |
| Theoretical foundation | No | Yes (T3SD + DEVS) |
| Representativeness basis | Qualitative (method kinds) | Quantitative (morphisms) |
| Fidelity characterization | Not addressed | VMMC framework |

**Citable References:**
- OMG (2025). *OMG Systems Modeling Language (SysML) Specification, Version 2.0*. Object Management Group. https://www.omg.org/spec/SysML/2.0/About-SysML
- Friedenthal, S. (2024). *SysML v2 Basics*. INCOSE IW Presentation.
- OMG (2023). *Object Management Group Approves SysML V2 Beta Specifications*. https://www.omg.org/news/releases/pr2023/07-10-23.htm
- Systems Modeling Community. *SysML v2 Release Repository*. GitHub. https://github.com/Systems-Modeling/SysML-v2-Release

**Target Venues:**
- Systems Engineering (Wiley)
- INCOSE International Symposium
- CSER (Conference on Systems Engineering Research)

**Status:** Idea captured (January 25, 2026)

---

## 2. Verification Models and Digital Twins: Intersection and Integration

**Working Title:** *Bridging Verification Model Theory and Digital Twin Practice: A Comparative Analysis and Integration Framework*

**Problem Statement:**
Digital twins and verification models both span the entire system lifecycle and both face the fidelity question—yet they are defined by different characteristics and serve different primary purposes. No formal framework connects these two domains.

**Key Observations from Research:**

| Aspect | Digital Twin | Verification Model |
|--------|--------------|-------------------|
| Defining characteristic | Real-time data connection to physical asset | Purpose of demonstrating requirement satisfaction |
| What is represented | Physical system state | System design (for verification purposes) |
| Data flow | Continuous, bidirectional with physical asset | Not necessarily connected to physical asset |
| Primary question | "Is virtual synchronized with physical?" | "Does design satisfy requirements?" |
| Fidelity definition | "Degree of precision and accuracy" (DTC) - qualitative | Morphic conditions (WySE) - quantitative |

**Research Directions:**

1. **Comparative Analysis:**
   - Formal comparison of digital twin fidelity vs. verification model representativeness
   - Mapping DTC concepts to WySE metamodel constructs
   - Identifying where digital twins could serve as verification models

2. **WySE → Digital Twins:**
   - How can morphic equivalence theory inform digital twin fidelity determination?
   - Can VMMC framework provide mathematical foundation for DTC's qualitative fidelity?
   - Extending WySE to address physical-virtual synchronization

3. **Digital Twins → Verification:**
   - When can a digital twin serve as a verification model?
   - What additional conditions are needed for a DT to be a valid VM?
   - Runtime verification using digital twins with WySE-grounded fidelity

**Key Gap:**
DTC defines fidelity as "the degree of precision and accuracy applied to the virtual representation" but provides no mathematical foundation for determining what fidelity is "sufficient for the desired use-cases." WySE's morphic equivalence framework could potentially fill this gap.

**Relevant References:**
- Digital Twin Consortium (2024). *The Definition of a Digital Twin*.
- Digital Twin Consortium (2020). *Digital Twin Consortium Defines Digital Twin*.
- National Academies (2024). *Foundational Research Gaps and Future Directions for Digital Twins*.
- DTC Digital Engineering Working Group (2024) - "systematic verification of fidelity, accuracy, and predictive capabilities"

**Target Venues:**
- Systems Engineering (Wiley)
- Journal of Systems and Software
- INCOSE International Symposium
- IEEE Systems Journal

**Status:** Idea captured (January 25, 2026)

**Open Conceptual Questions (from January 25, 2026 discussion):**

The following questions reached an impasse and require deeper analysis:

1. **What is being represented?**
   - VM represents System Design (SD) — a model of a model
   - DT represents Physical Asset — a real thing
   - These are fundamentally different targets of representation

2. **Nature of the model:**
   - VM can be digital OR physical
   - DT is always digital (by definition)

3. **When is a VM a digital twin?**
   - The VM must be digital (not physical)
   - Must have real-time data connection to... what? The SD? A physical asset?
   - If a VM connects to a physical asset, is it still representing the SD?

4. **When is a digital twin a VM?**
   - The DT must be used for verification purposes
   - But DT represents the physical system, not the SD
   - Can a DT verify that the *physical system* (not the SD) satisfies requirements?
   - How does this relate to the VM→SD relationship in WySE?

5. **Relationship summary:**

   | Aspect | VM | DT |
   |--------|----|----|
   | Nature | Digital or physical | Always digital |
   | Represents | System Design (a model) | Physical asset (a real thing) |
   | Relationship | VM ↔ SD | Virtual ↔ Physical |

These questions need resolution before the comparison/integration paper can proceed.

**Connection to VVUQ and Confidence (from January 25, 2026 discussion):**

The National Academies (2024) identified gaps in VVUQ standards and confidence in modeling outputs for digital twins. The connection to fidelity is implicit but can be made explicit:

- **Fidelity determination is foundational to VVUQ and confidence:**
  - Validation assesses whether the model accurately represents reality—but this depends on knowing what fidelity is appropriate for the use case
  - Uncertainty quantification requires understanding sources of error, including errors arising from fidelity choices
  - Confidence in outputs depends on knowing whether the model's fidelity is appropriate for the decision being made

- **Argument:** Without a theoretical basis for determining fidelity, VVUQ and confidence *cannot* be systematically addressed. The National Academies gap is *symptomatic* of the underlying fidelity gap.

This argument positions fidelity as foundational to the VVUQ challenges identified. This connection should be developed in this paper AND in the Bayesian confidence paper (see Idea #3).

---

## 3. Bayesian Methods for Verification Model Confidence

**Working Title:** *Connecting Morphic Equivalence to Confidence Assessment: A Bayesian Framework for Verification Model Fidelity*

**Status:** NEXT JOURNAL PAPER - Draft already exists from prior work

**Problem Statement:**
The WySE metamodel provides mathematical foundations for verification model definition through morphic equivalence. However, the connection between theoretical fidelity conditions and practical confidence in verification outcomes has not been formally established. Bayesian methods offer a rigorous approach to quantifying confidence given evidence.

**Key Research Questions:**
1. How can morphic equivalence conditions inform prior distributions for verification confidence?
2. What is the relationship between VMMC levels and uncertainty quantification?
3. How do fidelity choices propagate to confidence in verification outcomes?

**Connection to Digital Twin Paper:**
The National Academies (2024) identified gaps in VVUQ and confidence for digital twins. The argument that fidelity determination is *foundational* to VVUQ and confidence applies here:
- Without theoretical basis for fidelity → cannot systematically address VVUQ → cannot establish confidence
- Morphic equivalence (WySE) provides the theoretical basis for fidelity
- Bayesian methods can then connect fidelity to confidence quantification

**Potential Contribution:**
- Bridge between WySE theoretical foundations and practical confidence assessment
- Formal connection: morphic conditions → uncertainty bounds → Bayesian confidence
- Address the National Academies VVUQ gap through foundational theory

**Status:** Idea captured (January 25, 2026); draft exists from prior work

---

## 4. Closed World Assumption and Neuro-Symbolic Approaches

**Working Title:** *Beyond the Closed World Assumption: Neuro-Symbolic Approaches for Verification Model Definition*

**Problem Statement:**
Ontology-based approaches to systems engineering (e.g., VDP) operate under the closed world assumption (CWA)—what is not explicitly stated is assumed to be false. This limits expressiveness and adaptability, particularly for verification model definition where unknown or emergent behaviors may be relevant.

**Key Questions:**
1. How does the closed world assumption constrain ontology-based verification approaches?
2. What verification-relevant knowledge cannot be captured under CWA?
3. To what extent can neuro-symbolic approaches (combining neural networks with symbolic reasoning) resolve or mitigate CWA limitations?
4. Can neuro-symbolic methods enable open-world reasoning for verification model definition?

**Research Directions:**

1. **CWA Limitations Analysis:**
   - Characterize how CWA affects VDP and similar ontology-based verification frameworks
   - Identify verification scenarios where CWA is problematic (emergent behavior, incomplete specifications, novel failure modes)
   - Compare CWA vs open world assumption (OWA) implications for verification

2. **Neuro-Symbolic Verification:**
   - Survey neuro-symbolic architectures (neural theorem provers, differentiable reasoning, knowledge graph embeddings)
   - Assess which approaches can handle open-world reasoning
   - Evaluate applicability to verification model definition

3. **Integration with WySE:**
   - Can neuro-symbolic methods complement the mathematical rigor of systems theoretic approaches?
   - Hybrid framework: WySE for formal structure + neuro-symbolic for uncertainty/incompleteness

**Connection to Current Work:**
The VDP discussion in the literature review notes that VDP uses category theory but lacks explicit mathematical structures. The ontological foundation of VDP brings CWA constraints. This research would explore whether neuro-symbolic approaches offer a path forward that maintains rigor while addressing CWA limitations.

**Relevant Background:**
- Closed world assumption (Reiter, 1978) vs open world assumption
- Neuro-symbolic AI (Garcez et al., 2019; Marcus, 2020)
- Knowledge graph reasoning under uncertainty
- Neural theorem provers and differentiable logic

**Target Venues:**
- AI venues: NeurIPS, AAAI, IJCAI
- Systems Engineering: Systems Engineering (Wiley), INCOSE IS
- Interdisciplinary: IEEE Systems Journal

**Status:** Idea captured (January 26, 2026)

---

## 5. Library of Cross-Domain Isomorphisms/Homomorphisms

**Working Title:** *A Systematic Catalog of Cross-Domain Isomorphisms and Homomorphisms for Systems Engineering*

**Core Question:** What isomorphisms exist across engineering domains, and how do they connect to SE formalism (T3SD/DEVS)?

**Scope:** Systematic catalog of known cross-domain isomorphisms (mechanical-electrical, thermal, hydraulic, acoustic, etc.) with variable mappings, governing equations, and mathematical characterization. Connection to T3SD/DEVS morphism framework. Bond graph / port-Hamiltonian unification perspective.

**Project Location:** `Papers/SE_Math_Foundations/`

**Status:** In progress (February 2026) — CURRENT PAPER

---

## 6. Degrees of Homomorphism Metric

**Working Title:** *Quantifying Morphism Quality: A Layered Metric for Degree of Homomorphism in Systems Engineering*

**Core Question:** Can we quantify "how isomorphic" two systems are?

**Scope:** 5-layer metric (structural, behavioral, energy, information, categorical) measuring morphism quality. Must map onto the 6 VMMC types from the dissertation as calibration points. Connects to approximate bisimulation (Girard & Pappas).

**Status:** Idea captured (February 2026)

---

## 7. Characterization of Verification Requirements Relative to System Requirements

**Working Title:** *A Mathematical Characterization of Verification Requirement Types*

**Core Question:** What types of verification requirements exist and what does that mean mathematically?

**Connection:** Dissertation future topic #4. Connects to VMMC types.

**Status:** Idea captured (February 2026)

---

## 8. Biological/Engineered Systems and Biomimetics

**Working Title:** *Formal Morphisms Between Biological and Engineered Systems*

**Core Question:** What morphisms exist between biological and engineered systems?

**Scope:** Extends beyond classical physical-domain analogies to biological systems (neural/RLC, SIR/circuit, immune/cybersecurity). Formal morphism characterization where currently only informal analogies exist.

**Status:** Idea captured (February 2026)

---

## 9. Ontological Representations for SE Morphisms

**Working Title:** *Ontological and Database Representations for Systems Engineering Morphisms*

**Core Question:** How should morphism knowledge be represented? Ontology + database design.

**Connection:** VDP ontological approach; Idea #4 (neuro-symbolic/CWA).

**Status:** Idea captured (February 2026)

---

## 10. Compositional Emergence vs. Parts

**Working Title:** *When Does System Composition Create Emergent Properties? A Category-Theoretic Analysis*

**Core Question:** When does system composition create properties not present in components?

**Scope:** Category theory monoidal structure, operads for composition patterns. When does S1 ⊗ S2 have properties not predictable from S1 and S2 individually?

**Status:** Idea captured (February 2026)

---

## 11. Sufficiency/Insufficiency of DEVS and T3SD

**Working Title:** *Where Do DEVS and T3SD Break? A Systematic Analysis of Formalism Boundaries*

**Core Question:** Where exactly do these formalisms break, and what fills the gaps?

**Key Findings (from dissertation sec. 101):**
- Sufficient for: discrete, deterministic, open systems; 28 morphism proofs; verification model definition
- Insufficient: set theory vs. topology; no time advance in T3SD; limited to verification (not validation); no continuous/probabilistic support; methods are "notably manual"

**Status:** Idea captured (February 2026)

---

## 12. Immune System vs. Cybersecurity Morphisms

**Working Title:** *Formal Isomorphism Between Immune Defense and Cyber Defense*

**Core Question:** Is there a formal isomorphism between immune defense mechanisms and cybersecurity defense?

**Connection:** Subset of Idea #8 (biomimetics). Structural parallels: antigen recognition / threat detection, immune memory / threat databases, adaptive response / incident response.

**Status:** Idea captured (February 2026)

---

## 13. Morphisms vs. Transfer Learning

**Working Title:** *System-Theoretic Morphisms and Machine Learning Transfer: A Structural Comparison*

**Core Question:** How do system-theoretic morphisms relate to ML transfer learning?

**Key Insight:** Both are "structure-preserving maps across domains." Is transfer learning a computational approximation to an underlying system-theoretic morphism?

**Status:** Idea captured (February 2026)

---

## 14. Intersection with Set-Based Design

**Working Title:** *Morphisms Within Design Spaces: Connecting Set-Based Design to Formal Equivalence*

**Core Question:** How do morphisms characterize equivalences within design spaces?

**Scope:** SBD explores sets of alternatives; morphisms characterize equivalences within those sets. VMMC's "problem spaces of functions" may connect to SBD's "sets of alternatives."

**Status:** Idea captured (February 2026)

---

## 15. Homomorphic Encryption Structural Parallels

**Working Title:** *Algebraic Homomorphism in Encryption and Systems Engineering: Structural Parallels*

**Core Question:** Does algebraic homomorphism in encryption share structure with SE morphisms?

**Key Insight:** Homomorphic encryption preserves algebraic structure under encryption (computation on ciphertexts = computation on plaintexts). This is literally a homomorphism. The structural parallel to SE morphisms (operations on VMs correspond to operations on system designs) is more than metaphorical.

**Status:** Idea captured (February 2026) — may be a short communication

---

## 16. Categorical Framework for SE (Full Treatment)

**Working Title:** *A Rigorous Category-Theoretic Framework for Systems Engineering*

**Core Question:** Can category theory provide a rigorous unification of all SE morphism types?

**Scope:** Category Sys, domain subcategories, cross-domain functors, DEVS hierarchy as forgetful functors, natural transformations, monoidal structure, enriched categories, sheaves, operads. The full formal treatment.

**Status:** Idea captured (February 2026)

---

## 17. AI/Swarm Architecture for Morphism Discovery

**Working Title:** *Agentic AI for Mathematical Structure Discovery in Systems Engineering*

**Core Question:** Can AI agents find, verify, and catalog morphisms?

**Connection:** Builds on Agentic_AI_Swarms_SE survey/vision papers and SE_Math_Foundations catalog + metric.

**Status:** Idea captured (February 2026)

---

## 18. Human-in-the-Loop V&V with Morphism-Guided Verification

**Working Title:** *Human Expert Judgment in Morphism-Based Verification and Validation*

**Core Question:** Where does human judgment enter morphism-based verification?

**Scope:** Selecting VMMC type, validating morphism results against engineering intuition, adjudicating borderline cases, domain expert review. Connects to Idea #3 (Bayesian confidence — human judgment as prior information).

**Status:** Idea captured (February 2026)

---

## 19. Minimum Mathematical Toolkit for SE

**Working Title:** *The Minimum Mathematical Toolkit for Systems Engineering: A Synthesis*

**Core Question:** What is the smallest set of mathematical structures SE needs?

**Scope:** Capstone paper synthesizing Ideas 5-18. Five essential structures: set-theoretic morphisms, topological morphisms, category-theoretic functors, energy-based generalized variables, behavioral metrics.

**Status:** Idea captured (February 2026) — capstone paper, to be written last

---

## 20. Hidden Beliefs and Calibration in Engineering Morphism Reasoning

**Working Title:** *Surfacing and Measuring Implicit Morphism Assumptions in Engineering Judgment*

**Core Question:** When engineers use cross-domain analogies, what morphism conditions do they implicitly assume, and how accurate are those assumptions?

**Scope:** Use the formal morphism framework (Ideas 5, 6) as diagnostic ground truth. Elicit engineers' assumed variable mappings and compare against formally correct ones. Identify believed-but-false isomorphism conditions (they think a property is preserved when it isn't) and true-but-unrecognized conditions. Measure calibration — when engineers express confidence in an analogy, does that confidence correlate with actual morphism quality?

**Methodology:** Protocol analysis (think-aloud), structured interviews using the isomorphism catalog as elicitation instrument, calibration studies comparing subjective confidence to metric-derived morphism quality.

**Connection:** Merges cognitive "hidden beliefs" and "calibration" perspectives. Depends on Ideas 5 and 6 for ground truth. Feeds into Idea 18 (Human-in-the-Loop V&V). Part of NSF EDSE proposal Year 3.

**Target Venues:** Research in Engineering Design, Design Studies, Systems Engineering (Wiley), ASME IDETC

**Status:** Idea captured (February 2026) — NSF proposal Year 3 sub-objective (primary)

---

## 21. Quantifying Heuristic Accuracy in Cross-Domain Engineering Reasoning

**Working Title:** *How Good Are Engineering Heuristics? Measuring Cross-Domain Reasoning Accuracy with Formal Morphism Metrics*

**Core Question:** How accurate are common engineering heuristics about cross-domain relationships, and what is the cost of heuristic error?

**Scope:** Engineers routinely use "good enough" and "close enough" judgments about analogies. The morphism quality metric (Idea 6) provides ground truth. Measure how accurate common heuristics are in morphism-quality terms. Identify systematically optimistic vs. pessimistic heuristics. Determine whether heuristic accuracy varies by domain pair. Quantify downstream impact of heuristic error on verification confidence.

**Connection:** Depends on Ideas 5 and 6 for formal metric. Part of NSF EDSE proposal Year 3.

**Target Venues:** Research in Engineering Design, Design Studies, Journal of Mechanical Design

**Status:** Idea captured (February 2026) — NSF proposal Year 3 sub-objective (primary)

---

## 22. Layer-Selective Attention in Cross-Domain Engineering Reasoning

**Working Title:** *What Do Engineers See and Miss? Layer-Selective Attention in Cross-Domain Morphism Reasoning*

**Core Question:** Which layers of morphism quality (structural, behavioral, energy, information, categorical) do engineers naturally attend to, and which do they neglect?

**Scope:** The 5-layer metric (Idea 6) decomposes morphism quality. Study which layers engineers reason about naturally. Hypothesize that engineers attend primarily to structural and behavioral layers while neglecting energy and information layers. Compare expert vs. novice layer attention. Determine which layers are most predictive of design success/failure. Assess whether training on neglected layers improves judgment.

**Connection:** Depends on Idea 6 for the layered metric. Part of NSF EDSE proposal Year 3.

**Target Venues:** Design Studies, Research in Engineering Design, ASME IDETC

**Status:** Idea captured (February 2026) — NSF proposal Year 3 sub-objective

---

## 23. Mental Model Fidelity Characterization

**Working Title:** *Applying Verification Model Fidelity Theory to Engineering Mental Models*

**Core Question:** Can the VMMC framework be applied to characterize the fidelity of an engineer's mental model of a system?

**Scope:** An engineer's mental model is itself a representation used to make judgments about whether a design satisfies requirements — functionally a "verification model." Apply VMMC-type morphism analysis to the mental model. Characterize morphism quality between mental model and formal system model. Measure mental model degradation under time pressure, cognitive load, or domain unfamiliarity. Study whether engineers with higher mental-model-fidelity make better design decisions.

**Key Insight:** This is the conceptual move of turning the formal framework reflexively onto the engineer — using the theory of model fidelity to study the fidelity of the engineer's own internal model.

**Connection:** Extends VMMC framework into cognitive domain. Depends on Ideas 5, 6, and dissertation VMMC. Part of NSF EDSE proposal Year 3.

**Target Venues:** Design Studies, Cognitive Science, Research in Engineering Design, Systems Engineering (Wiley)

**Status:** Idea captured (February 2026) — NSF proposal Year 3 sub-objective

---

## 24. Tacit Knowledge Formalization via Morphism Elicitation

**Working Title:** *Formalizing Tacit Engineering Knowledge Through Structured Morphism Elicitation*

**Core Question:** Can the formal morphism catalog serve as an elicitation instrument to surface and formalize tacit expert knowledge about cross-domain relationships?

**Scope:** Senior engineers carry tacit knowledge about where analogies work and break — knowledge transmitted only through apprenticeship. Use the isomorphism catalog (Idea 5) as a structured interview protocol. Surface expert knowledge about morphism boundaries not found in textbooks. Discover new partial morphisms that experts know intuitively but have never been formally documented. Bridge the expert-novice gap through formalized tacit knowledge.

**Connection:** Depends on Idea 5 for the catalog. Connects to Idea 18. Part of NSF EDSE proposal Year 3 (broader impacts angle).

**Target Venues:** Research in Engineering Design, Knowledge Management Research & Practice, ASME IDETC

**Status:** Idea captured (February 2026) — NSF proposal Year 3 sub-objective

---

## 25. Design Decision Traceability to Morphism Assumptions

**Working Title:** *Tracing Verification Failures to Implicit Morphism Assumptions in Design Decisions*

**Core Question:** When a verification model fails to predict system behavior, can the failure be traced to an incorrect implicit morphism assumption?

**Scope:** Trace verification failures backward through the morphism chain. Identify which morphism layer broke down. Connect design decisions to their implicit morphism assumptions. Develop a morphism-aware design review protocol that surfaces assumptions before they cause failures.

**Connection:** Depends on Ideas 5 and 6 for formal framework. Connects to Idea 18. Part of NSF EDSE proposal Year 3.

**Target Venues:** Systems Engineering (Wiley), Journal of Mechanical Design, INCOSE IS

**Status:** Idea captured (February 2026) — NSF proposal Year 3 sub-objective

---

## 26. Neuromorphic Computing as Engineered Neural Morphism

**Working Title:** *Neuromorphic Computing Through the Lens of Formal Morphisms: Characterizing the Biological-to-Silicon Map*

**Core Question:** To what extent is the biological neuron → neuromorphic hardware map a formal morphism, and where does the mapping break down?

**Problem Statement:**
Neuromorphic computing explicitly mimics biological neural architecture in silicon — spiking neural networks, event-driven computation, memristive synapses, dendritic processing. Unlike most cross-domain analogies (which are discovered post hoc), this morphism is *intentional by design*. Yet the mapping is known to be partial: engineers deliberately simplify (e.g., point neurons vs. compartmental models, discrete spikes vs. continuous dendritic integration, static vs. plastic connectivity). No formal characterization of what is preserved and what is lost exists in morphism-theoretic terms.

**Research Directions:**

1. **Morphism characterization across layers:**
   - Structural: network topology preservation (small-world, scale-free properties)
   - Behavioral: spike-timing dynamics, temporal coding fidelity
   - Energy: biological metabolic efficiency vs. neuromorphic power efficiency (event-driven advantage)
   - Information: neural coding schemes vs. hardware encoding (rate coding, temporal coding, population coding)

2. **Intentional vs. emergent morphism properties:**
   - Which morphism layers are preserved by design (structural topology, spike-based communication)?
   - Which emerge unintentionally (power scaling laws, fault tolerance)?
   - Which are deliberately broken (dendritic computation, glial interactions, neuroplasticity timescales)?

3. **Morphism quality across neuromorphic platforms:**
   - Compare Intel Loihi, IBM TrueNorth, SpiNNaker, BrainScaleS, and memristive crossbar arrays
   - Each platform preserves different morphism layers — formal characterization via Idea 6 metric
   - Determine whether platforms with higher biological morphism quality perform better on specific task classes

4. **Implications for verification:**
   - When a neuromorphic system is used as a verification model for a biological neural system (or vice versa), what fidelity conditions apply?
   - Connection to VMMC framework: what VMMC type characterizes the bio-neuromorphic relationship?

**Key Insight:** Neuromorphic computing is the *strongest test case* for the morphism framework because the mapping is intentional, well-documented, and spans all five metric layers. If the morphism quality metric (Idea 6) cannot meaningfully distinguish between neuromorphic platforms' biological fidelity, the metric needs revision.

**Connection:** Extends Idea 8 (Biomimetics) with the most engineering-mature biological morphism. Uses Idea 6 metric as evaluation instrument. Connects to Idea 11 (DEVS/T3SD sufficiency) — event-driven neuromorphic systems align well with DEVS discrete-event formalism. Potential connection to Idea 13 (Transfer Learning) — neuromorphic hardware for efficient transfer learning execution.

**Relevant Background:**
- Mead, C. (1990). *Neuromorphic electronic systems*. Proceedings of the IEEE, 78(10), 1629-1636.
- Davies, M., et al. (2018). Loihi: A neuromorphic manycore processor with on-chip learning. IEEE Micro, 38(1), 82-99.
- Schuman, C. D., et al. (2022). Opportunities for neuromorphic computing algorithms and applications. Nature Computational Science, 2(1), 10-19.
- Indiveri, G., & Liu, S.-C. (2015). Memory and information processing in neuromorphic systems. Proceedings of the IEEE, 103(8), 1379-1397.

**Target Venues:**
- Nature Computational Science
- IEEE Transactions on Neural Networks and Learning Systems
- Frontiers in Neuroscience (Neuromorphic Engineering)
- Systems Engineering (Wiley) — if framed as verification model fidelity
- INCOSE IS — if framed as cross-domain morphism case study

**Status:** Idea captured (February 2026)

---

*File created: January 25, 2026*
*Last updated: February 25, 2026*

**Ideas captured:**
1. SysML v2 Mathematical Rigor Analysis
2. Verification Models and Digital Twins Integration
3. Bayesian Methods for Verification Model Confidence ← NEXT PAPER (draft exists)
4. Closed World Assumption and Neuro-Symbolic Approaches
5. Library of Cross-Domain Isomorphisms/Homomorphisms ← CURRENT PAPER
6. Degrees of Homomorphism Metric
7. Characterization of Verification Requirements
8. Biological/Engineered Systems and Biomimetics
9. Ontological Representations for SE Morphisms
10. Compositional Emergence vs. Parts
11. Sufficiency/Insufficiency of DEVS and T3SD
12. Immune System vs. Cybersecurity Morphisms
13. Morphisms vs. Transfer Learning
14. Intersection with Set-Based Design
15. Homomorphic Encryption Structural Parallels
16. Categorical Framework for SE (Full Treatment)
17. AI/Swarm Architecture for Morphism Discovery
18. Human-in-the-Loop V&V with Morphism-Guided Verification
19. Minimum Mathematical Toolkit for SE (Capstone)
20. Hidden Beliefs and Calibration in Engineering Morphism Reasoning ← NSF Year 3
21. Quantifying Heuristic Accuracy in Cross-Domain Reasoning ← NSF Year 3
22. Layer-Selective Attention in Cross-Domain Reasoning ← NSF Year 3
23. Mental Model Fidelity Characterization ← NSF Year 3
24. Tacit Knowledge Formalization via Morphism Elicitation ← NSF Year 3
25. Design Decision Traceability to Morphism Assumptions ← NSF Year 3
26. Neuromorphic Computing as Engineered Neural Morphism
