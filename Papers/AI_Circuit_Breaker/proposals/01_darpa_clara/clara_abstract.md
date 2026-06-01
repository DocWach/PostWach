# DARPA CLARA Abstract

## Morphism-Grounded Compositional Assurance for Autonomous AI Systems

---

**Solicitation:** DARPA-PA-25-07-02 (CLARA)
**Technical Area:** TA1 — High-Assurance ML/AR Composition
**PI:** Paul F. Wach, Ph.D., University of Arizona, Dept. of Systems & Industrial Engineering
**Co-PI:** Jeffrey Wallk, The Value Enablement Group, LLC
**Period of Performance:** 24 months (Phase 1: 15 mo, Phase 2: 9 mo)
**Estimated Cost:** $1.85M total ($1.1M Phase 1, $0.75M Phase 2) — ROM, subject to validation

---

## 1. Problem

CLARA observes that the dominant approach to AI assurance --- bolting automated reasoning (AR) onto machine learning (ML) as guardrails --- produces weak, non-compositional safety. We agree. Current trust frameworks suffer from a foundational epistemological error and three specific technical failures.

**The epistemological error.** Existing AI governance treats trust as binary certification: a system is approved or it is not. But trust is not a credential --- it is a calibrated, provisional epistemic commitment that must be continuously earned through reproducible evidence and that can be legitimately revoked when that evidentiary basis erodes. A one-time evaluation cannot warrant ongoing trust in a non-deterministic system whose behavior shifts with data, context, and interaction history. What is needed is an instrument that continuously monitors whether the evidentiary conditions for trust remain intact at any given moment.

The technical failures follow directly:

1. **No formal composition theory.** Trust in an AI system-of-systems is assumed, not derived from component trust. When an LLM is composed with a knowledge graph and a planner, no existing framework can bound the composite system's trustworthiness from the components.

2. **No measurement rigor.** Runtime monitors use ad-hoc thresholds (e.g., "cosine similarity > 0.85") with no traceability to a system specification and no uncertainty quantification. These are not measurements --- they are guesses.

3. **Single-axis monitoring.** Existing approaches check either structural fidelity (does the AI's world model match reality?) or behavioral accuracy (do its outputs match ground truth?) --- never both simultaneously. An AI can be structurally perfect yet numerically wrong, or structurally coarse yet operationally adequate. Single-axis monitors miss half the failure space.

## 2. What's New: Trust as Morphism Quality

We propose a compositional ML/AR framework grounded in systems-theoretic morphisms --- structure-preserving mappings between formal system models [1], [2], [3]. The core insight:

> An AI agent maintains an internal model Z_ai. The physical world is a separate system Z_real. **Trustworthiness is the quality of the structure-preserving mapping h: Z_ai → Z_real.** This is a measurable, composable, formally bounded quantity.

Morphism quality decomposes along two orthogonal axes [4], [5]:

- **Structural (σ):** Degree of homomorphism --- does the AI distinguish every state that reality distinguishes? σ = 1.0 is isomorphism; σ < 1.0 is abstraction-induced degradation. *This is an AR problem* --- computed via ontology alignment and graph homomorphism checking.

- **Behavioral (D):** Output distance --- do the AI's predictions match sensor ground truth? D = 0 is perfect fidelity. *This is an ML problem* --- computed via embedding similarity and sensor fusion.

**Why this is a compositional ML/AR approach, not a tack-on:** The two axes are formally independent but jointly necessary. Neither ML nor AR alone can characterize trust. The composition is inherent in the measurement theory, not bolted on after the fact. When components are composed, morphism quality bounds compose functorially: σ_total ≤ min(σ_component) and D_total ≤ Σ(D_component). Trust in the whole is formally bounded by trust in the parts.

## 3. Technical Approach

We instantiate this theory as an **AI Circuit Breaker** --- an instrument that continuously measures morphism quality and renders graduated verdicts. Just as trust is not binary, the breaker's response is not binary: it operates across graduated states (Normal → Caution → Restrict → Halt → Lockdown) that correspond to the strength of the evidentiary basis for continued trust in the monitored system.

**AR components:**
- OWL 2 DL ontology (the Circuit Breaker Trust Ontology) formalizes system models, morphism mappings, and trust constraints as queryable semantic infrastructure
- SHACL shapes enforce structural preconditions on morphism configurations
- SPARQL competency queries verify ontology completeness and compositional integrity
- Logic-based graduated response rules map measurement outcomes to operational verdicts

**ML components:**
- Transformer-based intent encoding maps AI actions into the reference embedding space
- Approximate nearest-neighbor search computes structural morphism quality (σ) in real-time
- Sensor fusion computes behavioral morphism quality (D) from multi-channel ground truth

**Composition interface:**
- AR constrains which ML outputs are valid (SHACL shapes reject morphism configurations that violate ontological preconditions)
- ML provides runtime evidence that AR reasons over (embedding distances feed into ontology-grounded verdict logic)
- Statistical process control (SPC) monitors both axes over time, deriving control limits from data rather than ad-hoc thresholds --- extending prior work pairing Bayesian methods with systems theory for test and evaluation of learning-based systems [6]
- PROV-O provenance graph makes every verdict traceable through the full AR/ML composition chain

**Three provable compositional properties:**
1. **Trust bounding:** Composite system trust is formally bounded by component trust (functorial composition)
2. **Consistency:** SHACL validation ensures component ontologies remain consistent when composed
3. **Traceability:** PROV-O records which AR and ML components contributed to each verdict, enabling post-hoc compositional verification

## 4. Evaluation Plan

**Domain:** The framework is domain-agnostic by design. Phase 1 evaluation will target a representative safety-critical domain where an LLM-based agent operates against a well-defined physical or logical ground truth. Candidate domains include telecom network management (PI's domain expertise, with industry collaboration under discussion), supply chain logistics (explicitly identified in CLARA's scope), and autonomous system simulation. Final domain selection will be confirmed in the full proposal based on data access and partnership commitments.

**Phase 1 key experiments:**
- Hallucination injection at 1--25% rates → measure detection accuracy on both axes
- Compositional integrity → degrade one component's ontology, verify composite σ degrades within formal bounds
- Data-derived vs. fixed thresholds → demonstrate SPC reduces false positive rate vs. static thresholds
- Graduated response validation → verify that breaker state transitions (Normal through Lockdown) correspond to measurable changes in evidentiary basis

**Phase 1 deliverable:** Open-source prototype (ontology, SHACL shapes, measurement engine, SPC pipeline) evaluated on the selected testbed. All code released under permissive open-source license per CLARA requirements.

**Phase 2:** Extend to a second domain, add adaptive regulation mechanisms, capstone publication.

## 5. Team

- **Paul F. Wach, Ph.D.** (PI, University of Arizona) --- Morphism theory, ontology engineering, measurement frameworks. Published on conjoining systems-theoretic and DEVS formalisms [3], morphism-based verification models [2], [7], degree-of-homomorphism metrics [4], Bayesian-systems-theoretic T&E [6], WySE Metamodel [8], and isomorphic degradation [5].
- **Jeffrey Wallk** (Co-PI, The Value Enablement Group, LLC) --- Systems architecture, AI safety engineering, on-prem/cloud integration. 20+ years in data architecture and autonomous systems.

## 6. Cost Summary

| Phase | Duration | Cost | Focus |
|-------|----------|------|-------|
| 1 | 15 months | $1.1M | Theory formalization, prototype, testbed evaluation |
| 2 | 9 months | $0.75M | Second domain, adaptive extensions, open-source release |
| **Total** | **24 months** | **$1.85M** | |

*Note: All cost figures are rough order of magnitude (ROM) estimates and will require validation during proposal development.*

---

## References

[1] A. W. Wymore, *Model-Based Systems Engineering*. Boca Raton, FL: CRC Press, 1993.

[2] P. F. Wach, "Study of equivalence in systems engineering within the frame of verification," Ph.D. dissertation, Virginia Tech, 2022.

[3] P. Wach, B. P. Zeigler, and A. Salado, "Conjoining Wymore's systems theoretic framework and the DEVS modeling formalism: Toward scientific foundations for MBSE," *Applied Sciences*, vol. 11, no. 11, p. 4936, 2021.

[4] P. Wach, A. Iyer, B. Shanmugam, C. Curran, and B. Ashok, "Systems theoretic co-pilot MVP," in *Conf. Syst. Eng. Res. (CSER)*, Long Beach, CA, 2025.

[5] P. Wach, B. Sandmann, and A. Iyer, "Toward a library of isomorphic patterns for systems engineering," in *Conf. Syst. Eng. Res. (CSER)*, 2026 (in revision).

[6] P. Wach, J. Krometis, A. Sonanis, A. Verma, D. Panchal, J. Freeman, L. Freeman, *et al.*, "Pairing Bayesian methods and systems theory to enable test and evaluation of learning-based systems," *INSIGHT*, vol. 25, pp. 65--70, 2022.

[7] P. F. Wach and A. Salado, "Theoretical underpinnings to establish fidelity conditions for defining verification models," in *INCOSE Int. Symp.*, Dublin, Ireland, 2024.

[8] P. F. Wach, "Initial systems theoretic metamodel of verification artifacts," in *INCOSE Int. Symp.*, 2022.
