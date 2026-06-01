# DARPA CLARA Abstract v2 — Option B Framing

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

CLARA identifies that current AI systems-of-systems lack compositional assurance: when ML and AR components are composed, no existing framework can formally bound the composite system's trustworthiness from its parts. We agree, and identify the root cause: there is no shared formal language in which ML and AR components can express, verify, and compose guarantees about what their models represent and how faithfully those representations track reality.

The technical failures are:

1. **No composition theory for model fidelity.** When an LLM is composed with a knowledge graph and a planner, each component maintains an internal model of its domain. No existing framework formally characterizes how faithfully each component's model represents reality, or how that fidelity degrades (or is preserved) under composition.

2. **AR is bolted on, not built in.** Current approaches use AR as post-hoc guardrails on ML outputs. The AR has no role in how the ML learns or reasons; it merely filters. This produces weak assurance because the AR cannot verify properties of the ML's internal representations.

3. **No measurement rigor in composition.** When components are composed, there is no principled way to derive the composite system's assurance level from component-level guarantees. Trust in the whole is assumed, not proven.

## 2. What's New: Morphism Theory as AR Foundation for ML

We propose that systems-theoretic morphisms, structure-preserving mappings between formal system models [1], [2], [3], provide the AR foundation on which high-assurance ML can be built. The core insight:

> Every AI component maintains an internal model Z_ai of some aspect of reality Z_real. **A morphism h: Z_ai -> Z_real is the formal object that makes the component's representational fidelity measurable, verifiable, and composable.** When AR encodes morphism constraints, ML can be trained and evaluated within those constraints, producing AR-based ML with compositional guarantees.

This yields three properties CLARA requires:

- **Verifiability:** Morphism conditions (structural D_s, behavioral D_b) are formally defined via Wymore five-tuples [1] and can be automatically verified through ontology reasoning and logic program evaluation.
- **Composability:** When components are composed, morphism quality bounds compose functorially: D_s_total >= max(D_s_component) and D_b_total <= sum(D_b_component). Trust in the whole is formally bounded by trust in the parts. This is a mathematical theorem, not an assumption.
- **Explainability:** Every assurance verdict traces through a morphism proof chain: which component's model diverged from reality, along which axis (structural or behavioral), by how much, and why. This produces hierarchical, fine-grained explanations with bounded unfolding depth.

## 3. Technical Approach

We instantiate this theory as a compositional AR-ML framework with two tightly coupled layers:

**AR Layer (Description Logic + Bayesian Logic Programs):**
- OWL 2 DL ontology (the STOIC family [7]) formalizes system models as Wymore five-tuples, morphism mappings as typed relations, and composition constraints as SHACL shapes
- Bayesian Logic Programs encode probabilistic morphism quality assessment: given evidence from ML components, compute posterior probability that morphism conditions hold
- Logic program rules encode graduated composition policies: which component combinations are valid, under what morphism quality bounds, with what confidence

**ML Layer (Neural Networks + Bayesian Methods):**
- Transformer-based encoders map component states into morphism-grounded embedding spaces defined by the AR ontology
- Training is AR-constrained: loss functions incorporate morphism quality penalties derived from the ontology's structural and behavioral bounds
- Bayesian inference provides uncertainty quantification on morphism quality estimates, enabling principled composition under uncertainty

**Tight Coupling (AR governs ML, ML informs AR):**
- AR defines the valid morphism space; ML operates within it. AR is not a post-hoc filter but a structural constraint on what the ML can learn and output.
- ML provides runtime evidence (embedding distances, output comparisons) that AR reasons over to compute compositional assurance verdicts
- Statistical Process Control (SPC) monitors both axes over time, deriving control limits from data rather than ad-hoc thresholds, extending prior work pairing Bayesian methods with systems theory [6]
- PROV-O provenance graph makes every verdict traceable through the full AR/ML composition chain

**Phase 1 (15 months):** Formalize the morphism-grounded AR-ML composition theory. Implement a working prototype composing Neural Networks (ML) with Description Logic + Bayesian Logic Programs (AR). Demonstrate on an FDA-regulated ECG arrhythmia classification testbed (PTB-XL dataset) with explicit SOA comparison against FDA-cleared devices. Achieve: fully verifiable, error rate <= SOA, >= 2 kinds tightly composed, polynomial inferencing.

**Phase 2 (9 months):** Extend to a second ML kind (Bayesian methods or RL). Demonstrate AR-constrained ML training with polynomial complexity. Deepen ECG pipeline to three composed tasks with domain-transfer cost analysis. Participate in Phase 2 Hackathon.

## 4. Team

- **Paul F. Wach, Ph.D.** (PI, University of Arizona) — Morphism theory, ontology engineering, measurement frameworks. Published on systems-theoretic morphisms [2], [3], degree-of-homomorphism metrics [4], Bayesian-systems-theoretic T&E [6], and isomorphic degradation [5].
- **Jeffrey Wallk** (Co-PI, The Value Enablement Group, LLC) — Systems architecture, AI safety engineering, data architecture.

## 5. Cost Summary

| Phase | Duration | Cost | Focus |
|-------|----------|------|-------|
| 1 | 15 months | $1.1M | Theory formalization, AR-ML prototype, ECG testbed |
| 2 | 9 months | $0.75M | Second ML kind, AR-constrained training, deepened ECG pipeline |
| **Total** | **24 months** | **$1.85M** | |

---

## References

[1] A. W. Wymore, *Model-Based Systems Engineering*. Boca Raton, FL: CRC Press, 1993.
[2] P. F. Wach, "Study of equivalence in systems engineering within the frame of verification," Ph.D. dissertation, Virginia Tech, 2022.
[3] P. Wach, B. P. Zeigler, and A. Salado, "Conjoining Wymore's systems theoretic framework and the DEVS modeling formalism," *Applied Sciences*, vol. 11, no. 11, p. 4936, 2021.
[4] P. Wach, A. Iyer, B. Shanmugam, C. Curran, and B. Ashok, "Systems theoretic co-pilot MVP," in *CSER*, Long Beach, CA, 2025.
[5] P. Wach, B. Sandmann, and A. Iyer, "Toward a library of isomorphic patterns for systems engineering," in *CSER*, 2026 (in revision).
[6] P. Wach, J. Krometis, A. Sonanis, A. Verma, D. Panchal, J. Freeman, L. Freeman, *et al.*, "Pairing Bayesian methods and systems theory to enable test and evaluation of learning-based systems," *INSIGHT*, vol. 25, pp. 65--70, 2022.
[7] STOIC Ontology Family: stoic-devs.ttl, stoic-t3sd.ttl, stoic-bridge.ttl. University of Arizona, 2026.
[8] P. F. Wach, "Initial systems theoretic metamodel of verification artifacts," in *INCOSE Int. Symp.*, 2022.
