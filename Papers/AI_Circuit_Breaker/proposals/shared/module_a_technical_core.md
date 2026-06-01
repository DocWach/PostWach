# Module A --- Technical Core: Morphism-Grounded Trust Metrology

**Shared module for all proposals. Source: AI Circuit Breaker Design Spec v4.0, updated 2026-03-23.**

---

## A.1 Core Thesis

AI trustworthiness is a morphism quality problem. An autonomous AI agent operates on an internal model of the world (Z_ai). The physical world is a separate system (Z_real). The agent is trustworthy to the degree that its model is *homomorphic* to reality --- that is, the mapping h: Z_ai --> Z_real preserves structure and produces equivalent outputs within engineering tolerances.

This framework unifies two traditions:

- **Systems-theoretic morphisms** (Wymore [5], WySE Metamodel [4]) provide the formal definition of what it means for two system models to be equivalent, and quantitative metrics for characterizing the distance from equivalence.
- **Metrology** (GUM [24]) provides the measurement science for tracking morphism quality in real time: traceable reference standards, calibrated instruments, quantified uncertainty, and statistical process control.

The AI Circuit Breaker is the **instrument that continuously measures the morphism quality between the AI's model of the world and the world itself**, then renders a verdict with known confidence bounds.

## A.2 Formal Framework: Wymore Tuples and Homomorphism

Following Wymore [5], a system model Z is a five-tuple Z = (S, I, O, N, R), where S is the set of states, I is the set of inputs, O is the set of outputs, N: S x I --> S is the next-state function, and R: S --> O is the readout function.

A homomorphism h: Z_ai --> Z_real exists if and only if surjections (hi, ho, hq) satisfy commutativity: mapping-then-transitioning yields the same result as transitioning-then-mapping [5]. When all surjections are bijective, the mapping is an **isomorphism** --- the AI's model is structurally identical to reality.

In practice, no AI model is perfectly isomorphic to reality. The question is: *how far from isomorphic is it, and is that distance within engineering tolerances?*

## A.3 The Homomorphic Distance D_h

Building on [22] and the WySE Metamodel [4], we characterize the distance from isomorphism as the vector **D_h = (D_s, D_b)**, where D_s and D_b measure two orthogonal axes of morphism quality:

**Structural distance D_s:** Measures how far the mapping is from bijective. Defined as the complement of the degree of homomorphism [22]:

    D_s = 1 - sigma, where sigma = (1/|S|) * sum_j [ 1 / |hq^{-1}(s_j)| ]

- D_s = 0: Bijective (isomorphism). The AI distinguishes every state that reality distinguishes.
- D_s > 0: Many-to-one (proper homomorphism). The AI lumps distinct real states together.

**Behavioral distance D_b:** Measures the maximum discrepancy between predicted and observed outputs:

    D_b = max_t |R_ai(s_ai(t)) - R_real(s_real(t))|

- D_b = 0: Perfect behavioral match.
- D_b > 0: AI outputs deviate from reality.

**Key insight [22]:** These axes are independent. An AI can have D_s = 0 but D_b >> 0 (structurally adequate, numerically wrong), or D_s >> 0 but D_b ~ 0 (coarse model, correct outputs). Both axes must be measured to characterize morphism quality. D_h = (0, 0) is the isomorphic ideal.

**Scope of the current formulation.** D_s as defined above assumes discrete, enumerable state spaces with exact surjective homomorphisms. For systems with continuous state spaces or approximate mappings (such as neural network representations), the structural distance generalizes to the mutual information ratio: D_s_continuous = 1 - I(X;Y)/H(X), where X is the reference state variable and Y is the mapped variable. This generalization parallels the relationship between Wymore's T3SD and Zeigler's DEVS: the combinatorial metric embeds ordinally into the information-theoretic framework while the latter handles continuous and approximate cases. Phase 1 validates the exact formulation on discrete clinical categories; Phase 2 extends to continuous representations.

## A.4 The Morphism Composition Chain

In observation-mediated systems, Z_real is not directly accessible. Instead, information flows through a chain of transformations, each a morphism with its own distance from isomorphism:

    h1: Physical system --> Sensor observation
    h2: Sensor observation --> Digitized signal
    h3: Digitized signal --> Processed signal
    h4: Processed signal --> Feature representation
    h5: Feature representation --> Classification output

The composition theorem applies across the chain:

    D_s_total >= max(D_s_i)    (structural: the weakest link bounds the total)
    D_b_total <= sum(D_b_i)    (behavioral: errors accumulate additively)

This chain structure yields three engineering-useful results:

1. **Bottleneck identification.** The composition theorem tells you where to invest: if D_s(h1) dominates (a physical limitation), no downstream processing can recover the lost structural fidelity.
2. **Staged reference standards.** Each h_i has its own reference: physics models for h1, ADC specifications for h2, filter transfer functions for h3, feature extraction algorithms for h4, clinical guidelines for h5.
3. **Hierarchical monitoring.** The circuit breaker can monitor at the chain level (end-to-end D_h) and at stage boundaries (per-link anomaly detection), enabling fault isolation when the chain-level breaker trips.

## A.5 The Circuit Breaker as Morphism Quality Monitor

The circuit breaker continuously monitors D_h across the morphism chain. Its instruments include:

| Instrument | What It Measures | Metric |
|------------|-----------------|--------|
| Structural fidelity instrument | Does the AI's classification preserve the state distinctions that the domain ontology defines? | D_s (degree of homomorphism) |
| Behavioral distance instrument | Do the AI's output values match sensor ground truth? | D_b (output distance) |
| Cosine alignment monitor | Per-inference angular distance between AI intent vector and ground truth vector | d_cos = 1 - cos(I, N_o) |
| Longitudinal reliability | Mean time between morphism quality exceedances | MTBH |

The cosine alignment monitor (d_cos) serves as a fast runtime sentinel. It correlates with degradation on both axes but does not decompose it into structural vs. behavioral components. When d_cos exceeds a data-derived threshold (SPC control limit), the circuit breaker triggers a graduated response.

Each instrument has a formal **uncertainty budget** (Type A: statistical variance from operational data; Type B: prior knowledge including ontology completeness and sensor calibration). Uncertainty is propagated via GUM [24] linear propagation at every stage.

## A.6 Five-Layer Architecture

The architecture organizes as five layers corresponding to metrological functions:

**Layer 1 --- Reference Standards (Z_real specification).** Defines the formal specification of valid system behavior: vocabularies, domain ontologies (encoding N_real and R_real), staged reference standards for each link in the morphism chain. Calibrated reference standards with version control, uncertainty bounds, and recalibration schedules.

**Layer 2 --- Morphism Instruments.** Instruments that measure D_h = (D_s, D_b) in real time, plus the d_cos alignment monitor. Each instrument has defined input range, resolution, uncertainty budget, calibration interval, and out-of-tolerance response.

**Layer 3 --- Statistical Process Control.** Monitors morphism quality over time using SPC control charts. Control limits derived from baseline operational data (minimum 25 subgroups per SPC convention), not arbitrary thresholds. Western Electric rules and CUSUM detect gradual quality trends. Graduated response: Normal --> Caution --> Restrict --> Halt --> Lockdown.

**Layer 4 --- Closed-Loop Morphism Maintenance.** Feedback system that maintains morphism quality over time. Includes morphism state capture, positive/negative learning pipelines, an Ontology Enhancement Gate with automated consistency checks (SHACL + SPARQL validation), and bounded control dynamics (stability analysis, gain scheduling).

**Layer 5 --- Underwriting Interface.** The human operator serves as the ultimate underwriter of morphism quality. Displays D_s and D_b on SPC charts (two-axis view), MTBH reliability panel, cognitive load monitor, and a PROV-O-backed audit trail making every decision's provenance queryable via SPARQL.

## A.7 Ontological Grounding: The Circuit Breaker Trust Ontology (CBTO)

The framework is formalized as the CBTO --- an OWL 2 DL knowledge graph with selective BFO 2020 alignment:

- **25 classes** (System Model domain, Morphism domain, Architecture domain, Provenance domain, Sensor domain)
- **20 object properties** linking tuple components, morphism mappings, architecture elements, and provenance chains
- **12 data properties** for metric values, versions, timestamps, and control limits
- **6 SHACL validation shapes** (two-tier severity: Violation/Warning)
- **10 SPARQL competency queries** across 4 domains (Trust Metrology, Architecture, Provenance, Structural)
- **PROV-O** provenance model replacing opaque audit hashes with queryable lineage

OWL reasoning and SPARQL competency queries operate at design-time/release-time only. Runtime morphism assessment (< 25 ms at ~40 Hz) uses pre-computed embeddings and cached SPARQL results.

## A.8 Metrological Traceability Chain

Every valid measurement requires four elements (GUM [24]):

| Element | Circuit Breaker Analog |
|---------|----------------------|
| Measurand | Morphism quality D_h = (D_s, D_b) between Z_ai and Z_real |
| Measurement procedure | Structural: D_s. Behavioral: D_b. Runtime: d_cos. Longitudinal: MTBH |
| Uncertainty budget | Type A + Type B per metric, propagated via GUM |
| Traceability | Staged reference standards: sensor ground truth (sensor-deterministic) + versioned domain ontologies (consensus-deterministic) at each link in the morphism chain |

The traceability chain is itself a composition of morphisms: h1 --> h2 --> ... --> h_n. By the composition theorem: D_s_total >= max(D_s_i) and D_b_total <= sum(D_b_i). The weakest structural link bounds overall morphism quality.

---

*References: [4] Wach et al., CSER 2026. [5] Wymore, 1993. [22] Wach, CSER 2025. [24] JCGM 100:2008 (GUM). [25] Wach, Portfolio Governance Ontology, 2026.*
