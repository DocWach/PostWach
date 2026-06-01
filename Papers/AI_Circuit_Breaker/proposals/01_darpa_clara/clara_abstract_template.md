# DARPA-PA-25-07-02 Abstract — Template Format

## Cover Sheet

| Field | Value |
|-------|-------|
| **Abstract Summary Title** | Morphism-Grounded Compositional Assurance for Autonomous AI Systems |
| **Proposer Organization** | University of Arizona |
| **Technical POC** | Paul F. Wach, Ph.D. / Dept. of Systems & Industrial Engineering / [phone] / [email] |
| **Administrative POC** | [UA Sponsored Projects — name, address, phone, email] |

---

## Abstract Technical Description

*[The following answers three Heilmeier Catechism questions per the CLARA Abstract Template. This text goes on page 2 of the .docx template.]*

### 1. What is the proposed work attempting to accomplish?

We propose a compositional ML/AR framework that provides formal, composable assurance guarantees for AI systems of systems. The framework couples an AR scaffold — OWL 2 DL ontology with SHACL constraint shapes and logic-based graduated response rules — with ML components — transformer-based neural network encodings and Bayesian statistical process control — to continuously measure and bound the trustworthiness of composed AI subsystems. AR defines the compositional structure and enforces validity constraints on ML outputs; ML provides runtime evidence that AR reasons over. The composition is inherent in the measurement theory, not bolted on. Phase 1 delivers open-source software (Apache 2.0) composing Logic Programs (AR) with Neural Networks (ML), evaluated on a safety-critical task domain with explicit SOA benchmarks.

### 2. How is the work performed today, and what are the limitations?

Current approaches bolt AR onto ML as external guardrails — the failure mode CLARA identifies. Three limitations persist. (1) No formal composition theory: trust in a system of systems is assumed, not derived from component trust; no framework bounds composite trustworthiness. (2) No measurement rigor: runtime monitors use ad-hoc thresholds with no traceability to specifications and no uncertainty quantification. (3) Single-axis monitoring: existing approaches check structural fidelity or behavioral accuracy but never both, missing half the failure space. DeepProbLog and similar systems begin to address AR-based ML but lack polynomial tractability and high-expressiveness AR features (defeasible argumentation, restraint) that CLARA requires.

### 3. What is new in your approach, and why will it succeed?

**Core innovation.** We ground AI trustworthiness in systems-theoretic morphisms — structure-preserving mappings between formal system models. An AI agent's internal model Z_ai and the physical world Z_real are formalized as system specifications. Trustworthiness is the measurable quality of the mapping h: Z_ai → Z_real, decomposed along two orthogonal axes: structural quality σ (degree of homomorphism — an AR computation via ontology alignment and graph homomorphism checking) and behavioral quality D (output distance — an ML computation via embedding similarity and sensor fusion). Neither axis alone suffices; both are jointly necessary, making the ML/AR composition inherent rather than tacked on.

**Compositional guarantees.** Morphism quality bounds compose functorially: σ_total ≤ min(σ_component) and D_total ≤ Σ(D_component), directly addressing CLARA's hierarchical composition requirement. SHACL validation ensures ontological consistency across composed subsystems. PROV-O provenance graphs provide hierarchical, fine-grained explainability with low unfolding depth.

**Why it will meet CLARA's metrics.** (1) *Verifiability without loss of performance:* morphism bounds provide automatic proofs of composite trust; SOA benchmarks will be established against ad-hoc threshold monitors. (2) *Multiplicity of AI kinds:* the framework is kind-agnostic — Phase 1 composes Neural Networks (ML) with Logic Programs (AR); Phase 2 extends to additional kinds. (3) *Polynomial time complexity:* structural morphism quality (σ) computes in O(n·k) via approximate nearest-neighbor search; behavioral quality (D) is O(m) sensor fusion. (4) *Composed task reliability > SOA:* dual-axis monitoring detects failures that single-axis monitors miss, demonstrated via hallucination injection at 1–25% rates on the selected task domain.

**Technical basis.** The PI has published directly on morphism-based system verification, degree-of-homomorphism metrics, conjoining systems-theoretic and DEVS formalisms, and pairing Bayesian methods with systems theory for T&E of learning-based systems — the precise theoretical foundations this approach requires.
