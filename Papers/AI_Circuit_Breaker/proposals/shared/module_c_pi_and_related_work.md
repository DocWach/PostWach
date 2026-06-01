# Module C --- Principal Investigator and Related Work

**Shared module for all proposals. Tailor PI section per solicitation requirements.**

---

## C.1 Principal Investigator

**Paul F. Wach, Ph.D.** --- Postdoctoral Research Associate, University of Arizona, Department of Systems and Industrial Engineering.

**Qualifications:** Dr. Wach's research sits at the intersection of systems engineering, AI trustworthiness, and formal metrology --- the exact combination this project demands. His published work establishes the mathematical foundations upon which the circuit breaker is built:

- **Degree of homomorphism metric** [22]: Introduced the first quantitative measure for characterizing structural degradation between system models. Published at CSER 2025. This metric (sigma) is the structural axis of the circuit breaker's trust measurement.
- **Isomorphism library** [4]: Developing a catalog of isomorphic patterns for systems engineering, with simulation infrastructure for validating morphic relationships computationally. Under revision for CSER 2026. Provides the methodological backbone for the project's formal framework.
- **WySE Metamodel** [23]: Defined the Wymorian Systems Engineering Metamodel for verification model definition, extending Wymore's tuple formalism to modern model-based systems engineering practice. This metamodel is the theoretical basis for the circuit breaker's runtime verification approach.
- **Portfolio governance ontology** [25]: Designed and validated an OWL 2 DL ontology for research portfolio governance (8 organizational units, 119 individuals, 778 triples, 20 SPARQL competency queries, SHACL validation). Demonstrates the PI's hands-on capability with the exact ontology engineering methods the CBTO requires.

**Domain expertise:** Prior industry experience in telecom network operations and data architecture. Co-PI Jeffrey Wallk brings ECG domain expertise through a comprehensive Technical Design Document (TDD v2.0) for diagnostic-grade ECG signal processing.

**Institutional support:** University of Arizona, a Carnegie R1 research university and designated Hispanic-Serving Institution, provides computational infrastructure and access to interdisciplinary collaborators in systems engineering, computer science, and measurement science.

## C.2 Related Work

### Formal Foundations

- **Wymore [5]:** Model-Based Systems Engineering (1993). Defines system models as five-tuples and homomorphism conditions. The foundational formalism on which the circuit breaker's morphism framework rests.
- **GUM [24]:** JCGM 100:2008 (Guide to the Expression of Uncertainty in Measurement). The international standard for measurement uncertainty. Our project applies GUM to AI trust metrics --- a novel application domain.

### AI Safety and Trustworthiness Frameworks

- **NIST AI RMF (2023):** Provides risk management categories (Govern, Map, Measure, Manage) but no quantitative measurement procedures or uncertainty budgets. Our project fills the "Measure" function with metrological rigor.
- **IEEE P7000 series:** Ethical design standards. Normative but not operational. Our enforcement architecture operationalizes these norms.
- **EU AI Act (2024):** Risk-based regulation requiring "appropriate levels of accuracy, robustness and cybersecurity." Our framework provides the measurement infrastructure to demonstrate compliance quantitatively.

### Runtime AI Monitoring

- **NeMo Guardrails (NVIDIA, 2023):** Programmable rails for LLM output filtering. Rule-based, no uncertainty quantification, no morphism-theoretic foundation.
- **Rebuff / LLM Guard:** Prompt injection detection. Single-layer defense; no two-axis measurement, no SPC.
- **Runtime verification literature (Leucker & Schallhart, 2009):** Monitors execution traces against formal specifications. Our contribution: extending runtime verification from Boolean property checking to continuous morphism quality measurement with uncertainty bounds.

### Training-Time Alignment

- **RLHF (Christiano et al., 2017; Ouyang et al., 2022):** Reinforcement learning from human feedback. Effective for training-time alignment but provides no runtime measurement or assurance.
- **Constitutional AI (Bai et al., 2022):** Self-supervised alignment. Same limitation: no continuous operational measurement.

### Statistical Process Control in AI

- **SPC for ML monitoring (Klaise et al., 2021; Faber et al., 2021):** Applies drift detection to ML model outputs. Our contribution: connecting SPC to a formal morphism framework with GUM uncertainty propagation, not just empirical drift detection.

### Ontology-Based AI Assurance

- **BFO 2020 (Arp et al., 2015):** Upper ontology for scientific domains. Our CBTO aligns with BFO for interoperability.
- **PROV-O (W3C, 2013):** Provenance data model. Our CBTO uses PROV-O for queryable audit trails.
- **SOSA/SSN (W3C/OGC, 2019):** Sensor ontology. Optional alignment point for sensor-deterministic traceability.

---

*References: [4] Wach et al., CSER 2026. [5] Wymore, 1993. [22] Wach et al., CSER 2025. [23] Wach, WySE Metamodel, 2025. [24] JCGM 100:2008. [25] Wach, Portfolio Governance Ontology, 2026.*
