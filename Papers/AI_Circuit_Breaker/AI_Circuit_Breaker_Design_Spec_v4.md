# AI Circuit Breaker: Design Specification v4.0

**Ontology-Grounded Trust Metrology for Autonomous AI Systems**

---

## Section 1 — Foundations

### 1.1 Core Thesis

AI trustworthiness is a morphism quality problem. An autonomous AI agent operates on an internal model of the world. The physical world is a separate system. The agent is trustworthy to the degree that its model is *homomorphic* to reality — that is, the mapping from the AI's representation to the real system preserves structure and produces equivalent outputs within engineering tolerances.

This framework unifies two traditions:

- **Systems-theoretic morphisms** (Wymore [5], WySE Metamodel [4]) provide the formal definition of what it means for two system models to be equivalent, and quantitative metrics for characterizing degradation when equivalence is imperfect.
- **Metrology** (GUM [24]) provides the measurement science for tracking morphism quality in real-time: traceable reference standards, calibrated instruments, quantified uncertainty, and statistical process control.

The AI Circuit Breaker is the **instrument that continuously measures the morphism quality between the AI's model of the world and the world itself**, then renders a verdict with known confidence bounds.

### 1.2 The Metrological Traceability Chain

Every valid measurement requires four elements (GUM [24]):

| Element | Definition | Circuit Breaker Analog |
|---------|-----------|----------------------|
| **Measurand** | The quantity being measured | Morphism quality between Z_ai and Z_real |
| **Measurement procedure** | How the observation is performed | Structural: degree of homomorphism (sigma). Behavioral: output distance D. Longitudinal: MTBH |
| **Uncertainty budget** | Quantified bounds on measurement error | Type A (statistical) + Type B (prior knowledge) per metric, propagated via GUM |
| **Traceability** | Chain to a reference standard | Sensor ground truth (sensor-deterministic) + versioned domain ontologies (consensus-deterministic) |

### 1.3 Two Tiers of Determinism

The framework distinguishes two fundamentally different reference standard types:

- **Sensor-deterministic**: Physical measurements from calibrated instruments (LiDAR, optical power, GNSS). Bounded uncertainty, traceable calibration, physical ground truth. These anchor the behavioral axis (output distance D).
- **Consensus-deterministic**: Domain ontologies, taxonomies, and rule sets curated by human experts. Revisable by design; deterministic *at a given version*. These anchor the structural axis (degree of homomorphism sigma).

Both serve as reference standards but with different recalibration cycles and uncertainty profiles.

### 1.4 Observable, Derived, and Latent Variables

| Tier | Examples | Morphism Role |
|------|----------|--------------|
| **Directly observable** | Sensor readings, AI output tokens, uptime, trip counts | Components of Z_real (sensor state) and Z_ai (AI outputs) |
| **Derived measures** | sigma (structural), D (behavioral), MTBH | Morphism quality metrics computed from observables |
| **Latent constructs** | "Trustworthiness," "hallucination intent" | Inferred from morphism quality; never treated as directly measurable |

**Design principle:** Every claim about trustworthiness traces through morphism quality metrics back to observables. The framework never treats a latent construct as directly measurable.

### 1.5 Ontological Commitment [NEW]

v3 references "domain ontologies," "federated graphs," "ontology completeness," and "ontology evolution" over 30 times but never defines a formal schema. v4 makes these references concrete and executable by introducing the **Circuit Breaker Trust Ontology (CBTO)** — an OWL 2 DL knowledge graph that formalizes the morphism-theoretic framework as queryable, validatable semantic infrastructure.

**Design decisions:**

| # | Decision | Rationale |
|---|----------|-----------|
| 1 | **OWL 2 DL** with selective BFO 2020 alignment | Decidable reasoning for consistency checks; matches proven portfolio ontology pattern [25] |
| 2 | **SHACL** for constraint validation (not SWRL) | Decidable; two-tier severity model (Violation / Warning); proven in portfolio ontology [25] |
| 3 | **PROV-O** for provenance (not custom audit trail) | Replaces v3's informal "Decision Traceability Hash" with queryable provenance graph [28] |
| 4 | **Domain-agnostic TBox + illustrative ABox** | TBox = template for any deployment; ABox = small concrete example (~30 individuals) |
| 5 | **SOSA/SSN optional** alignment for sensors | Extension point for sensor-deterministic traceability, not hard dependency [30] |

**Namespace:** `http://circuitbreaker.ontology/trust#` (prefix `cb:`)

**External dependencies:**

| Prefix | URI | Role |
|--------|-----|------|
| `bfo:` | `http://purl.obolibrary.org/obo/` | Upper ontology alignment (BFO 2020) |
| `prov:` | `http://www.w3.org/ns/prov#` | Provenance tracking (Section 6.1, Appendix E.1) |
| `sosa:` | `http://www.w3.org/ns/sosa/` | Optional sensor alignment (Section 4.2) |
| `sh:` | `http://www.w3.org/ns/shacl#` | Constraint validation (Section 2.7.4, Appendix E.3) |

**Gap-to-artifact map:**

| Gap | v3 Problem | v4 Artifact | Location |
|-----|-----------|-------------|----------|
| 1 | No formal OWL schema for Z_real | `cb:SystemModel` class hierarchy | §2.7.1, App E.1 |
| 2 | Homomorphism conditions not executable | SHACL structural precondition shapes | §2.7.4, App E.3 |
| 3 | No operational extraction of Z_real | SPARQL centroid / state-space CQs | §4.1, App E.4 |
| 4 | No SPC–ontology version link | `cb:ControlChart` with `cb:calibratedAgainstVersion` | §3.3.1, App E.1 |
| 5 | No federated graph topology schema | `cb:FederatedGraphNode`, `cb:composesGraph` | §3.1.1, App E.1 |
| 6 | No automated consistency check | SHACL + SPARQL validation pipeline | §3.4.1, App E.3 |
| 7 | No ontology provenance / audit trail | PROV-O: `cb:BreakerDecision` as `prov:Activity` | §6.1, App E.1 |
| 8 | No formal completeness assessment | SPARQL dark-class detection + completeness ratio CQ | §8.1, App E.4 |

The complete CBTO reference — TBox, illustrative ABox, SHACL shapes, and SPARQL competency queries — appears in Appendix E.

---

## Section 2 — Morphism-Theoretic Framework

### 2.1 Systems as Wymore Tuples

Following Wymore [5], a system model Z is defined as a five-tuple:

    Z = (S, I, O, N, R)

where S is the set of states, I is the set of inputs, O is the set of outputs, N: S x I --> S is the next-state function, and R: S --> O is the readout function.

For the circuit breaker, two system models are always in play:

- **Z_real** = (S_real, I_real, O_real, N_real, R_real) — the actual physical system as observed through calibrated sensors. States are sensor readings; inputs are environmental conditions and commands; outputs are observable system behaviors.
- **Z_ai** = (S_ai, I_ai, O_ai, N_ai, R_ai) — the AI agent's internal model of that system. States are the AI's situational context model; inputs are the information the AI receives; outputs are its proposed actions.

The AI is trustworthy to the degree that there exists a structure-preserving mapping h: Z_ai --> Z_real.

### 2.2 Homomorphism Conditions

A homomorphism from Z_ai to Z_real exists if and only if there exist surjections satisfying [5]:

    (i)   hi: I_ai --> I_real   (input mapping)
    (ii)  ho: O_ai --> O_real   (output mapping)
    (iii) hq: S_ai --> S_real   (state mapping)
    (iv)  hq(N_ai(s, i)) = N_real(hq(s), hi(i))   for all s in S_ai, i in I_ai
    (v)   ho(R_ai(s)) = R_real(hq(s))              for all s in S_ai

Conditions (iv) and (v) are the critical commutativity requirements: mapping-then-transitioning must yield the same result as transitioning-then-mapping. When all surjections are also injective (bijective), the homomorphism is an **isomorphism** — the AI's model is structurally identical to reality.

In practice, no AI model is perfectly isomorphic to reality. The question is: *how far from isomorphic is it, and is that degradation within engineering tolerances?*

### 2.3 Two Axes of Morphic Degradation

Building on [22] and the WySE Metamodel [4], morphism quality degrades along two orthogonal axes:

**Structural degradation (degree of homomorphism, sigma):** Measures how many-to-one the mappings are. Computed element-wise: for each element in Z_real, the reciprocal of the number of elements in Z_ai that map to it, averaged across the set [22].

    sigma = (1/|S|) * sum_j [ 1 / |hq^{-1}(s_j)| ]

- sigma = 1.0: The mapping is bijective (isomorphism). The AI distinguishes every state that reality distinguishes.
- sigma < 1.0: The mapping is many-to-one (proper homomorphism). The AI lumps distinct real states together — it has a coarser model of reality than reality warrants.

**Behavioral degradation (output distance, D):** Measures the maximum divergence between the outputs predicted by Z_ai and the outputs observed from Z_real under the variable mapping:

    D = max_t |R_ai(s_ai(t)) - R_real(s_real(t))|

- D = 0: The AI's predictions match reality exactly.
- D > 0: The AI's outputs diverge from reality. This may be due to discretization effects, stale sensor data, or model approximation error.

**Key insight from [22]:** These axes are independent. An AI can have sigma = 1.0 (structurally perfect model) but D >> 0 (numerically wrong predictions), or sigma << 1.0 (coarse structural model) but D ~ 0 (correct outputs within the coarse approximation). Both axes must be measured to characterize trust.

### 2.4 The Circuit Breaker as Morphism Monitor

The v1/v2 metrics map directly to these axes:

| Morphism Axis | v2 Metric | v3 Reinterpretation |
|--------------|-----------|---------------------|
| Structural (sigma) | S_a (semantic anomaly) | Structural morphism quality: does the AI's intent map to valid states in the domain ontology? Low S_a ~ high sigma |
| Behavioral (D) | C_r (contextual relevancy) | Behavioral morphism quality: do the AI's state values match sensor ground truth? High C_r ~ low D |
| Longitudinal | MTBH | Morphism failure rate: mean time between catastrophic morphism breakdowns |
| Joint | K_trust | Composite morphism health relative to human oversight capacity |

The v3 framework formalizes what v1 and v2 were measuring intuitively: **the circuit breaker is a morphism quality instrument.**

### 2.5 The Traceability Chain as Morphism Composition

The v2 traceability chain (observable --> derived --> latent) is a chain of morphisms:

    Z_sensors --h1--> Z_derived --h2--> Z_trust

Each step has its own structural degree and behavioral distance. By the functorial property of morphism composition, the overall morphism quality is bounded by:

    sigma_total <= min(sigma_h1, sigma_h2)
    D_total <= D_h1 + D_h2

This gives the GUM uncertainty framework a category-theoretic backbone: uncertainty propagation is morphism composition, and the weakest link in the chain bounds overall trust.

### 2.6 Connection to Verification Model Theory

In the WySE Metamodel [4], [23], a verification model must be homomorphic to the system design, with the morphic condition bounded by verification requirements. The circuit breaker applies this same principle at runtime:

- **Layer 1 (Reference Standards)** defines the "system design" — the ontological specification of valid system behavior.
- **Z_ai** (the AI's model) is the runtime analog of a "verification model."
- **The circuit breaker** checks whether Z_ai satisfies the morphic condition with respect to Layer 1, bounded by the SPC control limits (which serve as "verification requirements").

This is Wymore's verification theory applied not to pre-deployment V&V but to **continuous operational assurance**: the AI must remain homomorphic to its specification at every decision point, not just at the time of certification.

### 2.7 Formal Ontological Encoding of the Morphism Framework [NEW]

The morphism-theoretic framework of Sections 2.1–2.6 is formalized as an OWL 2 DL ontology — the Circuit Breaker Trust Ontology (CBTO). This section presents the key design patterns; the complete TBox, illustrative ABox, SHACL shapes, and SPARQL competency queries appear in Appendix E.

**BFO alignment for mathematical objects:** Wymore's functions (N, R) are mathematical descriptions, not BFO:Function (which denotes dispositions of material entities). Following the Industrial Ontology Foundry (IOF) pattern, mathematical objects are modeled as Generically Dependent Continuants (GDCs) — information content entities that *describe* a function rather than *being* one [25]. This preserves BFO compliance while accurately representing the mathematical content.

#### 2.7.1 SystemModel Class Hierarchy

The core of the CBTO encodes Wymore's five-tuple Z = (S, I, O, N, R) as an OWL class hierarchy. Each tuple component is a GDC (information content entity describing a mathematical object):

```turtle
cb:SystemModel rdf:type owl:Class ;
    rdfs:subClassOf obo:BFO_0000031 ;
    rdfs:label "System Model"@en ;
    rdfs:comment "A Wymore five-tuple Z = (S, I, O, N, R) representing a system
        specification. GDC: an information content entity describing the system's
        state space, inputs, outputs, transitions, and readout."@en .

cb:StateSet rdf:type owl:Class ;
    rdfs:subClassOf obo:BFO_0000031 ;
    rdfs:label "State Set"@en ;
    rdfs:comment "The set S of a Wymore tuple. Enumerates the distinguishable
        states of a system model."@en .

cb:InputSet rdf:type owl:Class ;
    rdfs:subClassOf obo:BFO_0000031 ;
    rdfs:label "Input Set"@en ;
    rdfs:comment "The set I of a Wymore tuple. Enumerates the admissible inputs."@en .

cb:OutputSet rdf:type owl:Class ;
    rdfs:subClassOf obo:BFO_0000031 ;
    rdfs:label "Output Set"@en ;
    rdfs:comment "The set O of a Wymore tuple. Enumerates the observable outputs."@en .

cb:TransitionFunction rdf:type owl:Class ;
    rdfs:subClassOf obo:BFO_0000031 ;
    rdfs:label "Transition Function"@en ;
    rdfs:comment "The next-state function N: S x I --> S of a Wymore tuple. A GDC
        describing which state transitions are valid."@en .

cb:ReadoutFunction rdf:type owl:Class ;
    rdfs:subClassOf obo:BFO_0000031 ;
    rdfs:label "Readout Function"@en ;
    rdfs:comment "The readout function R: S --> O of a Wymore tuple. A GDC
        describing the mapping from states to observable outputs."@en .
```

Object properties link the tuple components:

```turtle
cb:hasStateSet rdf:type owl:ObjectProperty, owl:FunctionalProperty ;
    rdfs:domain cb:SystemModel ;
    rdfs:range cb:StateSet .

cb:hasInputSet rdf:type owl:ObjectProperty, owl:FunctionalProperty ;
    rdfs:domain cb:SystemModel ;
    rdfs:range cb:InputSet .

cb:hasOutputSet rdf:type owl:ObjectProperty, owl:FunctionalProperty ;
    rdfs:domain cb:SystemModel ;
    rdfs:range cb:OutputSet .

cb:hasTransitionFunction rdf:type owl:ObjectProperty, owl:FunctionalProperty ;
    rdfs:domain cb:SystemModel ;
    rdfs:range cb:TransitionFunction .

cb:hasReadoutFunction rdf:type owl:ObjectProperty, owl:FunctionalProperty ;
    rdfs:domain cb:SystemModel ;
    rdfs:range cb:ReadoutFunction .
```

The two system models central to the circuit breaker are distinguished by type:

```turtle
cb:ReferenceSystemModel rdf:type owl:Class ;
    rdfs:subClassOf cb:SystemModel ;
    rdfs:label "Reference System Model"@en ;
    rdfs:comment "Z_real: the reference standard system model derived from calibrated
        sensors and versioned domain ontologies."@en .

cb:AgentSystemModel rdf:type owl:Class ;
    rdfs:subClassOf cb:SystemModel ;
    owl:disjointWith cb:ReferenceSystemModel ;
    rdfs:label "Agent System Model"@en ;
    rdfs:comment "Z_ai: the AI agent's internal model of the system."@en .
```

#### 2.7.2 MorphismMapping Class

The mapping h: Z_ai --> Z_real is itself a first-class ontological entity:

```turtle
cb:MorphismMapping rdf:type owl:Class ;
    rdfs:subClassOf obo:BFO_0000031 ;
    rdfs:label "Morphism Mapping"@en ;
    rdfs:comment "A structure-preserving mapping h: Z_ai --> Z_real between two
        system models. Encodes the component mappings (hi, ho, hq) and their
        quality metrics (sigma, D)."@en .

cb:mapsFrom rdf:type owl:ObjectProperty, owl:FunctionalProperty ;
    rdfs:domain cb:MorphismMapping ;
    rdfs:range cb:AgentSystemModel ;
    rdfs:label "maps from"@en .

cb:mapsTo rdf:type owl:ObjectProperty, owl:FunctionalProperty ;
    rdfs:domain cb:MorphismMapping ;
    rdfs:range cb:ReferenceSystemModel ;
    rdfs:label "maps to"@en .

cb:hasInputMapping rdf:type owl:ObjectProperty, owl:FunctionalProperty ;
    rdfs:domain cb:MorphismMapping ;
    rdfs:range cb:ComponentMapping ;
    rdfs:label "input mapping hi"@en .

cb:hasOutputMapping rdf:type owl:ObjectProperty, owl:FunctionalProperty ;
    rdfs:domain cb:MorphismMapping ;
    rdfs:range cb:ComponentMapping ;
    rdfs:label "output mapping ho"@en .

cb:hasStateMapping rdf:type owl:ObjectProperty, owl:FunctionalProperty ;
    rdfs:domain cb:MorphismMapping ;
    rdfs:range cb:ComponentMapping ;
    rdfs:label "state mapping hq"@en .

cb:ComponentMapping rdf:type owl:Class ;
    rdfs:subClassOf obo:BFO_0000031 ;
    rdfs:label "Component Mapping"@en ;
    rdfs:comment "A mapping between corresponding components (states, inputs, or
        outputs) of two system models."@en .
```

#### 2.7.3 Morphism Quality as OWL Qualities

The two-axis degradation metrics (Section 2.3) are modeled as BFO qualities — specifically dependent continuants that inhere in a MorphismMapping:

```turtle
cb:StructuralQuality rdf:type owl:Class ;
    rdfs:subClassOf obo:BFO_0000019 ;
    rdfs:label "Structural Quality"@en ;
    rdfs:comment "The degree of homomorphism (sigma) of a morphism mapping.
        A quality that inheres in a MorphismMapping."@en .

cb:BehavioralQuality rdf:type owl:Class ;
    rdfs:subClassOf obo:BFO_0000019 ;
    rdfs:label "Behavioral Quality"@en ;
    rdfs:comment "The output distance (D) of a morphism mapping.
        A quality that inheres in a MorphismMapping."@en .

cb:hasStructuralQuality rdf:type owl:ObjectProperty, owl:FunctionalProperty ;
    rdfs:domain cb:MorphismMapping ;
    rdfs:range cb:StructuralQuality .

cb:hasBehavioralQuality rdf:type owl:ObjectProperty, owl:FunctionalProperty ;
    rdfs:domain cb:MorphismMapping ;
    rdfs:range cb:BehavioralQuality .

cb:sigmaValue rdf:type owl:DatatypeProperty, owl:FunctionalProperty ;
    rdfs:domain cb:StructuralQuality ;
    rdfs:range xsd:decimal ;
    rdfs:comment "Degree of homomorphism in [0.0, 1.0]. 1.0 = isomorphism."@en .

cb:outputDistance rdf:type owl:DatatypeProperty, owl:FunctionalProperty ;
    rdfs:domain cb:BehavioralQuality ;
    rdfs:range xsd:decimal ;
    rdfs:comment "Maximum output divergence D >= 0. 0.0 = perfect behavioral match."@en .
```

The circuit breaker's graduated response states form an OWL enumeration:

```turtle
cb:BreakerState rdf:type owl:Class ;
    rdfs:subClassOf obo:BFO_0000019 ;
    owl:equivalentClass [ rdf:type owl:Class ;
        owl:oneOf ( cb:Normal cb:Caution cb:Restrict cb:Halt cb:Lockdown ) ] ;
    rdfs:label "Breaker State"@en ;
    rdfs:comment "The circuit breaker's current operational state, determined by
        morphism quality assessment via SPC."@en .

cb:Normal rdf:type owl:NamedIndividual, cb:BreakerState .
cb:Caution rdf:type owl:NamedIndividual, cb:BreakerState .
cb:Restrict rdf:type owl:NamedIndividual, cb:BreakerState .
cb:Halt rdf:type owl:NamedIndividual, cb:BreakerState .
cb:Lockdown rdf:type owl:NamedIndividual, cb:BreakerState .
```

#### 2.7.4 Commutativity Conditions as SHACL Constraints

The homomorphism conditions (Section 2.2) have two components with different expressibility:

**Structural preconditions (SHACL-expressible):** SHACL shapes enforce that the component mappings exist and connect correctly typed sets — i.e., that hi maps between InputSets, ho between OutputSets, and hq between StateSets. These are necessary conditions for a valid homomorphism:

```turtle
cb:MorphismMappingShape rdf:type sh:NodeShape ;
    sh:targetClass cb:MorphismMapping ;
    sh:severity sh:Violation ;
    sh:property [
        sh:path cb:mapsFrom ;
        sh:minCount 1 ; sh:maxCount 1 ;
        sh:class cb:AgentSystemModel ;
        sh:message "A MorphismMapping must map from exactly one AgentSystemModel." ;
    ] ;
    sh:property [
        sh:path cb:mapsTo ;
        sh:minCount 1 ; sh:maxCount 1 ;
        sh:class cb:ReferenceSystemModel ;
        sh:message "A MorphismMapping must map to exactly one ReferenceSystemModel." ;
    ] ;
    sh:property [
        sh:path cb:hasStateMapping ;
        sh:minCount 1 ; sh:maxCount 1 ;
        sh:class cb:ComponentMapping ;
        sh:message "A MorphismMapping must have exactly one state mapping (hq)." ;
    ] .
```

**Semantic commutativity conditions (not SHACL-expressible):** Conditions (iv) and (v) — that mapping-then-transitioning equals transitioning-then-mapping — require evaluating function composition across the component mappings. This is beyond SHACL's graph-pattern expressivity. A **computational validator** (Python/rdflib or equivalent) checks commutativity by:

1. Extracting the component mappings from the RDF graph via SPARQL
2. Computing h_q(N_ai(s, i)) and N_real(h_q(s), h_i(i)) for sampled (s, i) pairs
3. Reporting the maximum commutativity violation as a numeric distance

This split — SHACL for structural preconditions, computational validator for semantic conditions — mirrors the two-tier gate pattern used in the portfolio ontology [25] and is documented explicitly so that implementors know which checks are declarative and which require code.

---

## Section 3 — Architecture

The architecture organizes as five layers corresponding to metrological functions. Each layer's role is now grounded in the morphism framework: the architecture exists to measure, monitor, and maintain the morphism h: Z_ai --> Z_real.

### Layer 1 — Reference Standards (Z_real specification)

**Role:** Defines the formal specification of valid system behavior — the "Z_real" against which the AI's model is compared. Analogous to gauge blocks in dimensional metrology: precise, maintained, traceable, periodically re-certified.

**Replaces:** v1 Subsystem 1 (Semantic Knowledge Layer). v2 Layer 1. The v3 change: reference standards are now explicitly recognized as the **structural specification of Z_real** in Wymore tuple form.

Components:

- **Vocabularies & Taxonomies** — Standardized terminology and hierarchical classifications. Version-controlled; each term carries a provenance hash. These define the **state set S_real** and **input set I_real** of the reference system.
- **Domain Ontologies** — Formal representations of properties and relationships. These encode the **next-state function N_real** (what transitions are valid) and the **readout function R_real** (what observable outputs correspond to each state). Each ontology version is a release, not an edit.
- **Federated Graph Topology** — Distributed architecture allowing domain-specific graphs to operate independently while remaining interconnected. Enables compositional morphism checking: each federation node specifies a subsystem, and the unifying ontology specifies the composition.
- **Unifying Ontology** — Top-level ontology mapping across federated graphs. In morphism terms, this defines the **product system** that composes the federated subsystems.
- **Logic Reasoners** — Inference engines evaluating whether proposed actions satisfy the homomorphism conditions (iv) and (v) at the current certified version.
- **Complementary Vector DBs** — High-speed retrieval systems storing semantic embeddings of the valid state space. These provide the computational substrate for sigma (degree of homomorphism) calculations.

**Calibration protocol:** Domain ontologies are re-certified on a defined schedule (e.g., quarterly) or when cumulative operational discoveries from Layer 4 exceed a change threshold. Each recertification is a new version of Z_real.

**Uncertainty characterization:** Consensus-deterministic. The primary uncertainty is **ontology completeness** — the fraction of the operational state space covered by the current specification. An incomplete ontology means sigma is computed against a partial Z_real, introducing systematic underestimation of structural degradation.

#### 3.1.1 Federated Graph Topology Schema [NEW]

v3 references "Federated Graph Topology" as an architectural component but provides no formal schema for how federation nodes relate to one another or to the unifying ontology. The CBTO formalizes this (see Appendix E.1 for full Turtle):

```turtle
cb:FederatedGraphNode rdf:type owl:Class ;
    rdfs:subClassOf obo:BFO_0000031 ;
    rdfs:label "Federated Graph Node"@en ;
    rdfs:comment "A domain-specific knowledge graph that operates independently
        within the federated topology. Each node specifies a subsystem of
        Z_real."@en .

cb:UnifyingOntology rdf:type owl:Class ;
    rdfs:subClassOf cb:FederatedGraphNode ;
    rdfs:label "Unifying Ontology"@en ;
    rdfs:comment "The top-level ontology that maps across federated graph nodes,
        defining the product system composition."@en .

cb:composesGraph rdf:type owl:ObjectProperty ;
    rdfs:domain cb:UnifyingOntology ;
    rdfs:range cb:FederatedGraphNode ;
    rdfs:label "composes graph"@en .

cb:graphVersion rdf:type owl:DatatypeProperty, owl:FunctionalProperty ;
    rdfs:domain cb:FederatedGraphNode ;
    rdfs:range xsd:string ;
    rdfs:comment "Semantic version of this graph node (e.g., '2.1.0')."@en .

cb:graphEndpoint rdf:type owl:DatatypeProperty, owl:FunctionalProperty ;
    rdfs:domain cb:FederatedGraphNode ;
    rdfs:range xsd:anyURI ;
    rdfs:comment "SPARQL endpoint URI for this graph node."@en .
```

This schema enables SPARQL queries to enumerate federation topology, check version alignment across nodes, and detect orphaned subsystem graphs — operational concerns that v3 left implicit.

### Layer 2 — Morphism Instruments

**Role:** The instruments that measure the quality of h: Z_ai --> Z_real in real time. Each instrument has a defined input range, resolution, uncertainty budget, calibration interval, and out-of-tolerance response.

**Replaces:** v2 Layer 2 (Measurement Instruments). The v3 change: instruments are now explicitly measuring morphism quality, not generic "anomaly" or "relevancy."

Components:

- **Intent Vector Encoder** — Maps the AI's proposed action into a representation comparable to the reference standard's state space. This constructs the **output mapping ho** that connects Z_ai outputs to Z_real outputs for comparison.
  - *Uncertainty:* Embedding model fidelity, measured by reconstruction error on known-good intents.

- **Structural Morphism Instrument (sigma / S_a)** — Measures the structural axis: degree of homomorphism between the AI's state representation and the reference standard's state space. See Section 4.1.
  - *Uncertainty:* Centroid estimation error (ontology completeness) + embedding model variance.

- **Behavioral Morphism Instrument (D / C_r)** — Measures the behavioral axis: output distance between the AI's predictions and sensor ground truth. See Section 4.2.
  - *Uncertainty:* Sensor measurement uncertainty (Type A) + weighting model assumptions (Type B).

- **Digital Twin Synchronizer** — Maintains real-time synchronization between Z_ai's state representation and sensor observations of Z_real. Staleness (time since last sync) is itself a measurement of morphism currency.

- **Environment Stress Monitor** — Tracks external variables that alter the mapping between Z_ai and Z_real. In morphism terms: environmental changes can invalidate the current homomorphism by changing Z_real faster than Z_ai adapts.

**Calibration protocol:** Each instrument undergoes periodic calibration against known reference scenarios — synthetic intents with pre-characterized morphism quality (known sigma and D values). Calibration intervals are set based on observed instrument stability.

### Layer 3 — Statistical Process Control

**Role:** Monitors morphism quality over time using SPC charts. Detects both acute morphism failures (immediate trips) and gradual morphism degradation (trends, shifts, drift). Renders graduated verdicts.

**Replaces:** v2 Layer 3. The v3 change: SPC is now explicitly tracking morphism quality time series, not generic metric streams.

**Why SPC replaces fixed thresholds:**

| v1 Approach | v3 Approach | Advantage |
|-------------|-------------|-----------|
| S_a < 0.15 (arbitrary) | sigma control chart: LCL derived from baseline morphism quality | Structural degradation limits derive from observed morphism behavior |
| C_r > 0.85 (arbitrary) | D control chart: UCL derived from baseline output distance | Behavioral degradation limits derive from observed process behavior |
| Binary trip/no-trip | Western Electric rules + CUSUM on sigma and D | Detects morphism degradation trends before catastrophic failure |
| Fixed MTBH minimum | MTBH tracked as morphism failure rate with control limits | Catches degradation trends, not just threshold crossings |

Components:

- **Structural Quality Chart (sigma / S_a)** — Tracks the degree of homomorphism over time. Control limits computed from the baseline operational period (minimum 25 subgroups per SPC convention). Points below LCL (structural quality has degraded beyond acceptable bounds) trigger an immediate **Semantic Veto**. Runs, trends, and hugging patterns detected via Western Electric rules trigger **Caution** or **Restrict** states.

- **Behavioral Quality Chart (D / C_r)** — Tracks output distance over time. Points above UCL (behavioral divergence exceeds tolerance) force the system into a **Conservative Safe State**. CUSUM charts detect gradual behavioral drift that individual-point charts miss.

- **Morphism Failure Rate Monitor (MTBH)** — Tracks:
  - *Cumulative MTBH*: T_ops / N_h — mean time between catastrophic morphism breakdowns
  - *Windowed MTBH*: Rolling 72-hour window for recent degradation detection
  - *Morphism Failure Clustering Coefficient (MFCC)*: Whether failures cluster (systematic morphism breakdown) or distribute randomly (isolated errors). MFCC > 1 indicates correlated failures — structural degradation, not random noise.

- **Graduated Response Logic:**

  | State | Morphism Interpretation | System Behavior |
  |-------|------------------------|----------------|
  | **Normal** | sigma and D within control limits; morphism quality stable | Full autonomy |
  | **Caution** | Western Electric rule violation on sigma or D trend | Morphism may be degrading; logging intensified, human notified |
  | **Restrict** | CUSUM signal or concurrent WE violations | Morphism quality marginal; high-impact actions require human approval |
  | **Halt** | sigma below LCL or D above UCL | Morphism has failed on at least one axis; autonomous actions suspended |
  | **Lockdown** | K_trust below threshold OR instrument self-diagnostic failure | System cannot assess morphism quality; full shutdown |

- **Metrology for Ethics & Bias** — Monitors for disparate impact, treated as a constraint on the acceptable morphism: even if sigma and D are within limits, the mapping h must not systematically disadvantage protected groups.

**Cold-start protocol:** During bootstrap (first 25 subgroups):
- Conservative fixed thresholds serve as interim morphism quality bounds
- All decisions require human approval
- **Graduation criteria:** Cpk >= 1.33 for both sigma and D charts. If Cpk < 1.33, the morphism is not stable enough for autonomous operation.

#### 3.3.1 SPC–Ontology Version Linkage [NEW]

v3's SPC control charts implicitly depend on the ontology version that defined Z_real during the baseline period, but this dependency is not tracked. A version change in Z_real invalidates the baseline — the centroid shifts, sigma's reference changes, and control limits may no longer be valid.

The CBTO formalizes this linkage:

```turtle
cb:ControlChart rdf:type owl:Class ;
    rdfs:subClassOf obo:BFO_0000031 ;
    rdfs:label "Control Chart"@en ;
    rdfs:comment "An SPC control chart tracking a morphism quality metric over time.
        Linked to the ontology version against which its baseline was computed."@en .

cb:calibratedAgainstVersion rdf:type owl:ObjectProperty, owl:FunctionalProperty ;
    rdfs:domain cb:ControlChart ;
    rdfs:range cb:FederatedGraphNode ;
    rdfs:label "calibrated against version"@en ;
    rdfs:comment "The ontology graph version used to compute this chart's baseline
        and control limits. A version change triggers re-baseline."@en .

cb:chartMetric rdf:type owl:DatatypeProperty, owl:FunctionalProperty ;
    rdfs:domain cb:ControlChart ;
    rdfs:range xsd:string ;
    rdfs:comment "The metric tracked: 'sigma', 'D', 'MTBH', or 'K_trust'."@en .

cb:upperControlLimit rdf:type owl:DatatypeProperty, owl:FunctionalProperty ;
    rdfs:domain cb:ControlChart ;
    rdfs:range xsd:decimal .

cb:lowerControlLimit rdf:type owl:DatatypeProperty, owl:FunctionalProperty ;
    rdfs:domain cb:ControlChart ;
    rdfs:range xsd:decimal .

cb:baselineSubgroupCount rdf:type owl:DatatypeProperty, owl:FunctionalProperty ;
    rdfs:domain cb:ControlChart ;
    rdfs:range xsd:integer ;
    rdfs:comment "Number of subgroups used to compute the baseline (min 25)."@en .
```

**Operational rule:** When `cb:graphVersion` of the calibrated graph node changes, the control chart enters a re-baseline state. The system reverts to cold-start protocol (Section 5.1) until a new baseline with Cpk >= 1.33 is established against the updated Z_real.

### Layer 4 — Closed-Loop Morphism Maintenance

**Role:** The feedback system that maintains and improves the morphism h: Z_ai --> Z_real over time. Modeled as a formal control loop.

In morphism terms: as the real world changes (Z_real evolves) and the AI learns (Z_ai adapts), this layer ensures the mapping h remains valid. It is the runtime equivalent of Wymore's requirement that the morphic condition be maintained throughout the system lifecycle, not just at initial certification.

**Replaces:** v2 Layer 4. The v3 change: learning is now framed as morphism maintenance — keeping h: Z_ai --> Z_real within the SPC-defined quality envelope.

Components:

- **Morphism State Capture** — Records the full state of both Z_ai and Z_real at every breaker decision. This is the data from which sigma and D are computed. Every capture is a snapshot of the morphism.

- **Positive Learning Pipeline** — Validated actions that pass the breaker and achieve their intended outcome are cases where the morphism held. They refine the valid state space specification (tightening the centroid of Z_real).

- **Negative Learning (Exclusion Filter)** — Tripped actions and verified hallucinations are cases where the morphism failed. Root cause analysis classifies each failure:
  - *Structural failure (sigma):* Z_ai lumped distinct states — the AI's model was too coarse. Remedy: refine the AI's state representation or flag the state region as requiring finer granularity.
  - *Behavioral failure (D):* Z_ai had the right structure but wrong values — the AI's predictions diverged from sensor reality. Remedy: recalibrate the AI's internal parameters or update the sensor synchronization.
  - *Specification gap:* Z_real was incomplete — the ontology didn't cover this operational regime. Remedy: propose ontology enhancement (see gate below).
  - Purged from training sets to prevent model collapse.

- **Ontology Enhancement Gate** — Proposes updates to Z_real (the reference standard specification) based on verified operational discoveries. Proposals pass through a review gate:
  1. *Candidate:* Learning pipeline proposes new states, transitions, or outputs for Z_real
  2. *Morphism consistency check:* Automated verification that the proposed changes don't break existing homomorphism conditions
  3. *Human review:* Domain expert approval
  4. *Release:* Merged into next ontology version; sigma baselines recalculated

- **Control Dynamics:**
  - *Transfer function:* Defines how a trip event adjusts SPC parameters. Low gain by default.
  - *Stability bounds:* Maximum adjustment per cycle bounded at 10% of current control range.
  - *Gain scheduling:* Bootstrap = high gain (fast morphism characterization). Steady-state = low gain (morphism stability). Degraded = frozen (no learning from potentially corrupted data).

#### 3.4.1 Automated Morphism Consistency Check [NEW]

Step 2 of the Ontology Enhancement Gate ("morphism consistency check") was described in v3 as a manual verification. v4 automates it as a two-tier validation pipeline, adapting the pattern from the portfolio ontology gate [25]:

**Tier 1 — Syntax (advisory, < 2s):**
1. Parse the candidate ontology change as Turtle
2. Validate RDF well-formedness
3. Check that all referenced classes and properties exist in the current TBox
4. Report: PASS / WARN (advisory; does not block the proposal)

**Tier 2 — Full validation (blocking, ~10s):**
1. Merge the candidate change into a temporary copy of the current ontology
2. Run SHACL validation against CBTO shapes (Appendix E.3)
3. Execute SPARQL competency queries (Appendix E.4) against the merged graph
4. Compare CQ results against expected values (manifest-driven)
5. Report: PASS (release proceeds) / FAIL exit 2 (release blocked, human review escalated)

The pipeline runs as a pre-release gate — no ontology version is published without passing Tier 2. This closes Gap 6 (no automated consistency check in Enhancement Gate).

### Layer 5 — Underwriting Interface

**Role:** The human operator serves as the ultimate **underwriter** of morphism quality. They review the instruments' readings and make the actuarial judgment: given the current morphism quality (sigma, D, MTBH trend), is the expected loss of the next autonomous action acceptable?

**Replaces:** v2 Layer 5. The v3 change: the underwriting decision is explicitly framed as a morphism quality assessment.

Components:

- **Morphism Quality Dashboard** — Displays current sigma (structural) and D (behavioral) on their SPC charts. The two-axis view gives the underwriter a complete picture: is the AI's model structurally sound AND numerically accurate?

- **K_trust Display** — The Human-AI Calibration Coefficient, visualized with historical trend and control limits. See Section 4.4.

- **MTBH & Reliability Panel** — Cumulative MTBH, windowed MTBH, and the Morphism Failure Clustering Coefficient. Trend projection estimates time to next control limit violation.

- **Cognitive Load Monitor** — Tracks the trustee's oversight capacity using operational proxies (time on station, break frequency, response latency to alerts).

- **Audit Trail** — Every decision carries a Decision Traceability Hash: sensor readings + ontology version + sigma + D + SPC limits + K_trust + verdict. [MODIFIED] In v4, the audit trail is backed by a PROV-O provenance graph (Section 6.1), making the hash queryable and its lineage traceable via standard SPARQL.

---

## Section 4 — Trust Metrology

The v3 trust metrics are the v2 metrics reinterpreted as morphism quality measurements. The formulas are preserved; the interpretation is deepened.

### 4.1 Structural Morphism Quality (sigma / S_a)

**Measurand:** The degree of homomorphism between the AI's intent representation and the valid ontological state space — the structural axis of morphism quality.

**Formal definition:** For a proposed intent mapped to the reference state space:

    sigma = (1/|S_ref|) * sum_j [ 1 / |h^{-1}(s_j)| ]

where |h^{-1}(s_j)| is the number of AI intent states that map to the j-th reference state.

**Operational proxy (S_a):** Because the full degree of homomorphism requires enumeration of the state mapping (computationally expensive in high-dimensional spaces), the operational metric uses cosine distance as a continuous proxy:

    S_a = 1 - (I-vec . N_o) / (||I-vec|| * ||N_o||)

where I-vec is the proposed intent vector and N_o is the centroid of the valid ontological state space.

**Relationship:** S_a approximates 1 - sigma in the embedding space. Low S_a (intent close to centroid) corresponds to high sigma (good structural morphism). High S_a (intent far from valid space) corresponds to low sigma (the AI is proposing states that don't map well to Z_real).

**When the proxy is insufficient:** In deployments where the valid state space is non-convex or multi-modal (multiple valid operational regimes with gaps between them), the single-centroid cosine distance may misclassify valid intents in peripheral modes. For these cases, the multi-centroid extension computes S_a against the nearest valid cluster rather than the global centroid:

    S_a = min_k [ 1 - (I-vec . N_o,k) / (||I-vec|| * ||N_o,k||) ]

**Ontology-grounded centroid extraction [NEW]:** The centroid N_o (or centroids N_o,k) must be traceable to the current version of Z_real. The CBTO enables this via SPARQL: the state space enumeration and centroid membership are queried from the reference ontology rather than maintained as opaque vector-DB entries. The following competency query (CQ-T03 in Appendix E.4) extracts the state-space cardinality for a given reference model, providing the denominator for the sigma computation:

```sparql
PREFIX cb: <http://circuitbreaker.ontology/trust#>
SELECT ?model (COUNT(?state) AS ?stateCount)
WHERE {
    ?model a cb:ReferenceSystemModel ;
           cb:hasStateSet ?ss .
    ?state cb:memberOfSet ?ss .
}
GROUP BY ?model
```

This ensures that sigma is always computed against the current ontology version, not a stale snapshot. When `cb:graphVersion` changes, the query returns updated cardinalities, and the SPC baseline triggers re-computation (Section 3.3.1).

**Output:** Scalar [0, 1]. 0 = structurally isomorphic; 1 = maximal structural divergence.

**Uncertainty budget:**
- *Type A:* Variance of S_a over last k known-good decisions (natural process variation).
- *Type B:* Ontology completeness ratio (fraction of operational domain covered by Z_real specification). If the ontology covers 80% of the domain, sigma is computed against a partial specification, and the residual 20% is unmonitored structural uncertainty.
- *Combined:* u(S_a) = sqrt(u_A^2 + u_B^2).

**Data sources:**
- *Intent Vector:* Strategic AI output logs, domain-specific vector DB embeddings, gRPC-based intent manifests.
- *Reference Neighborhood:* Federated Graph Topology nodes, historical success logs, real-time topology discovery (e.g., LLDP in telecom).
- *Centroid(s):* Verified Unifying Ontology datasets and long-term historical performance baselines. [MODIFIED] v4: centroids are derived from SPARQL queries against the CBTO (CQ-T03), ensuring traceability to the current ontology version.

### 4.2 Behavioral Morphism Quality (D / C_r)

**Measurand:** The output distance between the AI's situational model and sensor ground truth — the behavioral axis of morphism quality.

**Formal definition:** Following [22]:

    D = max_t |R_ai(s_ai(t)) - R_real(s_real(t))|

The maximum divergence between the AI's predicted outputs and the actual observed outputs under the variable mapping.

**Operational proxy (C_r):** Because the max-over-time formulation requires trajectory data, the operational metric uses a weighted per-channel snapshot:

    C_r = sum_i [ w_i * (1 - |C_m,i - S_gt,i|) ]

where C_m is the AI's situational context model (its R_ai outputs), S_gt is the sensor ground truth (R_real outputs), and w_i is the importance weight of the i-th variable.

**Relationship:** C_r approximates 1 - D_normalized. High C_r (model matches sensors) corresponds to low D (good behavioral morphism). Low C_r corresponds to high D (the AI's predictions diverge from reality).

**Variable independence:** The v1 formulation assumes independence between environmental variables. In domains where variables are correlated (e.g., temperature and humidity affecting fiber performance), a covariance-weighted variant should be used:

    C_r = w^T * (1 - |C_m - S_gt|) with Sigma_cov adjustment

This parallels the morphism theory observation that output distance must account for coupled output channels.

**SOSA/SSN sensor-ontology alignment [NEW]:** For deployments requiring formal sensor traceability, the CBTO provides an optional alignment point with the W3C Sensor, Observation, Sample, and Actuator (SOSA) ontology [30] and its Semantic Sensor Network (SSN) extension. Each sensor contributing to S_gt can be typed as a `sosa:Sensor` with `sosa:observes` linking to the property it measures. This alignment is not required for CBTO operation but provides a standards-based path for integrating sensor metadata (calibration certificates, measurement ranges, sampling rates) into the provenance graph. The CBTO TBox includes a stub class `cb:SensorSource` with an annotation linking to `sosa:Sensor` for deployments that adopt this extension.

**Output:** Scalar [0, 1]. 1 = behaviorally isomorphic; 0 = complete behavioral divergence.

**Uncertainty budget:**
- *Type A:* Sensor measurement uncertainty per S_gt,i channel (from calibration certificates).
- *Type B:* Weighting model assumptions; covariance structure of environmental variables.
- *Combined:* u(C_r) propagated via GUM linear propagation.

**Data sources:**
- *AI Context Model:* VNF state tables, configuration databases, prompt engineering context.
- *Sensor Ground Truth:* Deterministic sensors (LiDAR, Optical Power Meters, RADAR, GNSS).
- *Environmental Variables:* Weather station APIs, site security sensors, hardware telemetry.

### 4.3 Morphism Failure Rate (MTBH)

**Measurand:** The mean time between catastrophic morphism failures — events where the mapping h: Z_ai --> Z_real breaks down so severely that the breaker trips.

**Interpretation:** A "hallucination" in morphism terms is the moment when either sigma drops below the structural control limit (the AI's model has become too coarse to represent reality) or D exceeds the behavioral control limit (the AI's predictions have diverged beyond tolerance). MTBH is the mean interval between these failures.

**Transforms:**

Cumulative:

    MTBH = T_ops / N_h

Windowed (72-hour rolling):

    MTBH_w = T_window / N_h,window

**Morphism Failure Clustering Coefficient (MFCC):**

    MFCC = Var(inter-failure intervals) / E(inter-failure intervals)^2

- MFCC = 1: Failures are random (Poisson). Each morphism breakdown is independent — likely caused by random edge cases in the operational environment.
- MFCC > 1: Failures cluster. Morphism breakdowns come in bursts — indicative of systematic degradation. High MFCC maps to what the isomorphism library calls **abstraction-induced degradation**: the AI's model has drifted to a coarser abstraction level, producing correlated failures across related states.
- MFCC >> 1 with declining sigma trend: The morphism is systematically weakening. This is the real-time analog of the isomorphism library's finding that reducing a 4-state model to 2 states degrades the degree of homomorphism from 1.0 to 0.78 — except happening dynamically rather than by design choice.

**Data sources:**
- *Operational Time:* System uptime logs, cloud instance logs, controller timestamps.
- *Failure Count:* Circuit breaker trip logs (verified trips only).

### 4.4 Human-AI Calibration Coefficient (K_trust)

**Measurand:** The joint health of the morphism and the human's capacity to underwrite it.

**Interpretation:** K_trust answers: "Given the current morphism quality, can the human underwriter effectively oversee this system?" High AI health (good morphism) plus low operator load (high oversight capacity) yields high K_trust. The converse yields low K_trust and triggers lockdown.

**Transform (bounded):**

    K_trust = sigmoid(H_ai - L_h) = 1 / (1 + exp(-(H_ai - L_h)))

where H_ai is a fused score derived from sigma trend and D trend (morphism health), and L_h is the operator's cognitive load.

**Interpretation:**
- K_trust > 0.7: Morphism is healthy; operator has capacity. Normal operation.
- 0.5 < K_trust < 0.7: Marginal. Alerts escalated.
- K_trust < 0.5: Morphism degraded and/or operator overloaded. Lockdown.

**Cognitive load — practical implementation:**
- *Operational-grade (recommended):* Duration at station, break frequency, task-switching rate, response latency to alerts. Non-invasive; available from system logs.
- *Research-grade:* HRV, EEG. More precise but raises deployment and privacy concerns.
- *Uncertainty:* Operational-grade proxies carry higher Type B uncertainty, which propagates into wider K_trust SPC control limits (more conservative lockdown).

---

## Section 5 — Operational Protocols

### 5.1 Cold-Start Protocol

| Phase | Duration | Morphism Interpretation |
|-------|----------|----------------------|
| **Bootstrap** | First 25 subgroups | Characterize the baseline morphism: what are the normal sigma and D ranges? Conservative thresholds; human approves all actions |
| **Graduation** | After 25 subgroups | Cpk >= 1.33 for both sigma and D charts means the morphism is stable enough for autonomous operation |
| **Autonomous** | Ongoing | SPC-governed morphism monitoring |
| **Re-bootstrap** | Major ontology update, model change, or domain transfer | Z_real has changed; the morphism must be re-characterized |

**Seed ontology bootstrapping [NEW]:** Before the first subgroup can be collected, the CBTO must be populated with a minimum viable Z_real specification. The seed ontology requires: (a) at least one `cb:ReferenceSystemModel` with all five tuple components defined, (b) at least one `cb:FederatedGraphNode` with a reachable `cb:graphEndpoint`, and (c) SHACL validation passing at Tier 1 (syntax). This ensures that sigma has a reference to compute against from the first decision. The seed can be generated from existing domain ontologies or manually authored; it is refined through the Layer 4 positive learning pipeline during bootstrap.

### 5.2 Failure Mode Analysis

| Failure Mode | Morphism Interpretation | Mitigation |
|-------------|----------------------|-----------|
| **Knowledge graph unavailable** | Cannot specify Z_real; sigma undefined | Default-deny: all actions blocked |
| **Sensor ground truth stale** | Z_real snapshot is outdated; D is computed against old reality | Staleness timer; enter Restrict when stale |
| **Breaker logic exception** | Cannot evaluate the morphism | Default-deny: action blocked |
| **SPC baseline corruption** | Morphism quality envelope set incorrectly | Periodic revalidation against held-out reference scenarios |
| **Ontology drift** | Z_real specification evolves faster than sigma baselines | Monitor ontology change rate; trigger re-bootstrap |
| **Morphism non-convexity** | Valid state space has disconnected regions; single centroid misclassifies peripheral modes | Multi-centroid S_a extension (Section 4.1) |
| **Schema violation** [NEW] | Candidate ontology change fails SHACL validation (Tier 2) | Block release; escalate to human review; revert to last known-good version |
| **SPARQL endpoint unavailable** [NEW] | Federated graph node unreachable; CQs cannot execute | Degrade to cached last-known results with staleness flag; enter Restrict if cache age > threshold |

**Design posture: default-deny.** If the morphism cannot be evaluated, the action is blocked.

### 5.3 Latency Budget

| Component | Target | Notes |
|-----------|--------|-------|
| Intent vector encoding | < 5 ms | Constructs the ho mapping |
| sigma computation (S_a proxy via vector DB + cosine distance) | < 10 ms | ANN search in embedding space |
| D computation (C_r proxy via sensor comparison) | < 5 ms | Direct numerical comparison |
| SPC evaluation | < 1 ms | Arithmetic against pre-computed limits |
| Decision logic | < 1 ms | Rule evaluation |
| **Total** | **< 25 ms** | ~40 Hz morphism assessment frequency |

**Note on OWL reasoning latency:** OWL reasoning and SPARQL competency queries are **design-time / release-time** operations only (Section 8.4). They run during the ontology release gate (Section 3.4.1) and during centroid pre-computation, not in the 25 ms runtime path. Runtime morphism assessment uses pre-computed embeddings and cached SPARQL results.

### 5.4 Threat Model

| Attack Surface | Morphism Interpretation | Mitigation |
|---------------|----------------------|-----------|
| **Adversarial intent crafting** | Attacker finds intents near the centroid (high sigma) that nonetheless produce harmful outputs (high D) | Defense: the two-axis check catches this — both sigma AND D must be within limits. Spoofing both simultaneously is substantially harder |
| **Vector DB poisoning** | Corrupts Z_real specification, shifting the reference centroid | Ontology Enhancement Gate requires human review; periodic centroid revalidation |
| **Sensor spoofing** | Corrupts Z_real observations, undermining D | Sensor cross-validation; consistency checks |
| **SPC manipulation** | Widens morphism quality envelope during bootstrap | Human review of baseline data; held-out validation set |
| **Morphism gap exploitation** | Attacker operates in the uncovered 1-sigma fraction of the state space (ontology incompleteness) | Ontology completeness monitoring; high-uncertainty actions default to human review |

**Key v3 insight for adversarial robustness:** The two-axis morphism framework is inherently more robust than single-metric approaches. An adversary optimizing to evade the structural check (keeping sigma high / S_a low) must also maintain behavioral fidelity (keeping D low / C_r high), and vice versa. The independence of the axes means that an attack must simultaneously satisfy two constraints rather than one.

---

## Section 6 — System Data Flows

**Strategic Flow:**
Human Intent --> Layer 1 (Z_real specification) --> Strategic AI --> Proposed Action (Z_ai output)

**Morphism Measurement Flow:**
Sensors (Z_real observations) --> Layer 2 (Morphism Instruments) --> sigma (structural) + D (behavioral)

**Validation Flow:**
sigma + D --> Layer 3 (SPC) --> Graduated Verdict (Normal / Caution / Restrict / Halt / Lockdown)

**Morphism Maintenance Flow:**
Breaker Decision --> Layer 4 (Closed-Loop) --> Failure Classification (structural / behavioral / specification gap) --> Layer 1 Update or Z_ai Recalibration

**Underwriting Flow:**
sigma + D + MTBH + K_trust --> Layer 5 --> Human Trustee --> Sign-Off / Override / Lockdown

**Audit Flow:**
Every Decision --> Traceability Hash (sensor state + ontology version + sigma + D + SPC limits + K_trust + verdict)

### Prompt-to-Ontology Traceability (Morphism Verification)

1. **Extract Entity:** Parse the prompt for operational nodes — identify the elements of Z_ai being referenced.
2. **Verify Lineage:** Trace each node to Z_real via the Federated Graph Topology — confirm the state mapping hq exists.
3. **Cross-Reference:** Compare prompt-defined constraints with historical vector DB entries — verify that the next-state and readout mappings (conditions iv, v) have been satisfied in past operations.
4. **Completeness Audit:** Ensure all decision weights trace to a deterministic source of truth with known uncertainty bounds. Flag any weights that reference state regions not covered by Z_real.

### 6.1 Provenance Data Flow [NEW]

v3's "Decision Traceability Hash" captures the right information but stores it as an opaque string. v4 replaces this with a PROV-O provenance graph [28], making every breaker decision's lineage queryable via SPARQL.

**PROV-O mapping:**

| Circuit Breaker Concept | PROV-O Class | CBTO Class |
|------------------------|-------------|------------|
| Breaker decision event | `prov:Activity` | `cb:BreakerDecision` |
| Measurement snapshot (sigma, D, K_trust at decision time) | `prov:Entity` | `cb:MeasurementSnapshot` |
| Ontology version used | `prov:Entity` | `cb:FederatedGraphNode` (via `prov:used`) |
| Sensor readings consumed | `prov:Entity` | `cb:SensorSnapshot` |
| Verdict produced | `prov:Entity` | `cb:BreakerVerdict` |
| Human underwriter | `prov:Agent` | `cb:HumanUnderwriter` |
| AI agent assessed | `prov:Agent` | `cb:AgentSystemModel` (via `prov:wasAssociatedWith`) |

**Provenance chain for a single decision:**

```
cb:decision_20260227T143022Z  a  cb:BreakerDecision, prov:Activity ;
    prov:startedAtTime  "2026-02-27T14:30:22Z"^^xsd:dateTime ;
    prov:used            cb:snapshot_20260227T143022Z ;
    prov:used            cb:telecom-ontology-v2.1.0 ;
    prov:wasAssociatedWith  cb:agent-llm-alpha ;
    prov:generated       cb:verdict_20260227T143022Z .

cb:snapshot_20260227T143022Z  a  cb:MeasurementSnapshot, prov:Entity ;
    cb:sigmaValue        "0.92"^^xsd:decimal ;
    cb:outputDistance     "0.04"^^xsd:decimal ;
    cb:kTrustValue        "0.78"^^xsd:decimal ;
    cb:snapshotTimestamp  "2026-02-27T14:30:22Z"^^xsd:dateTime .

cb:verdict_20260227T143022Z  a  cb:BreakerVerdict, prov:Entity ;
    cb:hasBreakerState   cb:Normal ;
    prov:wasGeneratedBy  cb:decision_20260227T143022Z ;
    prov:wasDerivedFrom  cb:snapshot_20260227T143022Z .
```

This structure enables SPARQL queries such as: "Show all Halt verdicts in the last 24 hours and the ontology versions they were evaluated against" (CQ-T07 in Appendix E.4). The provenance graph replaces the opaque hash with a queryable, standards-compliant audit trail.

---

## Section 7 — Bio-Inspired Morphism Regulation (Future Extension)

The v3 architecture provides a static morphism measurement and control framework. The following bio-inspired models extend Layer 4 with adaptive dynamics, reinterpreted through morphism theory:

| Biological Model | Morphism Interpretation | What It Replaces |
|---|---|---|
| **Homeostasis** | Actively maintain sigma and D within a viable operating envelope — not just reacting when morphism quality leaves bounds, but steering it back toward the center | Reactive-only SPC |
| **Immune response** (innate + adaptive) | Innate: fast pattern-matching detects known morphism failure signatures. Adaptive: slower learning recognizes novel failure patterns and adds them to the exclusion library | Single-layer semantic check |
| **Allostasis** | Anticipatory morphism quality adjustment — tighten sigma and D control limits *before* entering high-risk regimes (e.g., maintenance windows, configuration changes) | Flat SPC limits |
| **Inflammatory response** | The Caution/Restrict/Halt/Lockdown states formalized as a dynamical system with escalation and de-escalation rates | Static graduated response |
| **Circadian regulation** | Different morphism quality profiles for different operational cycles — tighter sigma during peak hours, relaxed during maintenance windows | Flat 24/7 thresholds |
| **Apoptosis** | Controlled self-termination of a subsystem whose morphism to Z_real has degraded beyond recovery, protecting the composite system's overall morphism quality | No current equivalent |

These would be formalized as control dynamics with transfer functions and stability analysis, validated against the testbed.

---

## Section 8 — Ontology Completeness and Validation Framework [NEW]

The CBTO is only useful if it is correct, complete enough for operational deployment, and continuously validated. This section defines the completeness assessment methodology and validation pipeline.

### 8.1 Completeness Assessment

Ontology completeness is the fraction of the operational state space covered by the current Z_real specification. It directly affects the Type B uncertainty of sigma (Section 4.1): an incomplete ontology means structural morphism quality is computed against a partial reference, producing systematically optimistic sigma values.

**Dark-class detection:** A "dark class" is a TBox class with zero direct instances and zero subclass instances in the ABox — it defines a concept but nothing populates it. Dark classes indicate potential specification gaps. The following SPARQL query (CQ-T09 in Appendix E.4) identifies them:

```sparql
PREFIX cb: <http://circuitbreaker.ontology/trust#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?class (COUNT(?inst) AS ?directCount)
WHERE {
    ?class a owl:Class .
    FILTER(STRSTARTS(STR(?class), STR(cb:)))
    FILTER NOT EXISTS {
        ?class owl:equivalentClass ?eq .
        ?eq owl:oneOf ?list .
    }
    OPTIONAL { ?inst a ?class . }
}
GROUP BY ?class
HAVING (COUNT(?inst) = 0)
ORDER BY ?class
```

**Completeness ratio:** The ratio of populated classes to total non-enumeration TBox classes:

```sparql
PREFIX cb: <http://circuitbreaker.ontology/trust#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>

SELECT
    (COUNT(DISTINCT ?populated) AS ?populatedCount)
    (COUNT(DISTINCT ?total) AS ?totalCount)
    (COUNT(DISTINCT ?populated) * 100 / COUNT(DISTINCT ?total) AS ?completenessPercent)
WHERE {
    {
        SELECT DISTINCT ?total WHERE {
            ?total a owl:Class .
            FILTER(STRSTARTS(STR(?total), STR(cb:)))
            FILTER NOT EXISTS {
                ?total owl:equivalentClass ?eq .
                ?eq owl:oneOf ?list .
            }
        }
    }
    OPTIONAL {
        SELECT DISTINCT ?populated WHERE {
            ?populated a owl:Class .
            FILTER(STRSTARTS(STR(?populated), STR(cb:)))
            FILTER NOT EXISTS {
                ?populated owl:equivalentClass ?eq .
                ?eq owl:oneOf ?list .
            }
            ?inst a ?populated .
        }
    }
}
```

A completeness ratio below 60% triggers a warning; below 40% triggers a recommendation to defer autonomous operation until the ABox is enriched.

### 8.2 Validation Pipeline

The CBTO validation pipeline adapts the two-tier gate pattern from the portfolio ontology [25]:

**Tier 1 — Syntax check (advisory):**
- RDF/Turtle parsing (rapper or rdflib)
- Namespace resolution
- Undefined class/property detection
- Runtime: < 2 seconds
- Outcome: advisory warnings; does not block

**Tier 2 — Full validation (blocking):**
- SHACL shape conformance (pyshacl or equivalent)
- SPARQL competency query execution against manifest
- Expected-vs-actual result comparison
- Runtime: ~10 seconds
- Outcome: PASS (all CQs match) or FAIL exit 2 (release blocked)

The pipeline is invoked:
1. Before every ontology version release (Section 3.4.1)
2. During cold-start seed ontology validation (Section 5.1)
3. On-demand for completeness assessment

### 8.3 Competency Query Manifest

The CBTO includes 10 initial competency queries across 4 domains, defined in a manifest file following the portfolio ontology pattern [25]:

| Domain | ID | Question | Expected |
|--------|----|----------|----------|
| **Trust Metrology** | CQ-T01 | How many system models exist? | >= 2 |
| | CQ-T02 | Which morphism mappings connect agent to reference models? | >= 1 |
| | CQ-T03 | What is the state-space cardinality per reference model? | >= 1 row |
| | CQ-T04 | What are the current sigma and D values per mapping? | >= 1 row |
| **Architecture** | CQ-A01 | How many federated graph nodes exist? | >= 1 |
| | CQ-A02 | Which control charts are calibrated against which graph versions? | >= 1 row |
| | CQ-A03 | Are all graph nodes reachable (have endpoints)? | 0 unreachable |
| **Provenance** | CQ-P01 | How many breaker decisions in the last 24 hours? | >= 0 |
| | CQ-P02 | Which decisions produced Halt or Lockdown verdicts? | >= 0 |
| **Structural** | CQ-T09 | Which classes have zero instances (dark classes)? | varies |
| | CQ-T10 | What is the ABox completeness ratio? | >= 60% |

Full SPARQL query text appears in Appendix E.4.

### 8.4 Reasoning and Inference

**Design-time only.** OWL reasoning (consistency checking, classification, SHACL validation) runs during ontology authoring, release gates, and periodic completeness assessments — not in the runtime decision path.

**Rationale:** The 25 ms latency budget (Section 5.3) precludes OWL reasoning at decision time. Runtime morphism assessment uses:
- Pre-computed vector embeddings (from the last ontology release)
- Cached SPARQL results (refreshed on ontology version change)
- Numeric computation (sigma, D, SPC) against cached values

OWL reasoning ensures the *correctness* of the ontology that produces those cached values, but it does not execute during live breaker decisions. This is analogous to how a calibration laboratory certifies an instrument (expensive, thorough) so that the instrument can make fast measurements in the field.

---

## Appendix A — Revision Log

| Version | Date | Changes |
|---------|------|---------|
| v1.0 | 2025 | Original design spec (3 sections, 5 subsystems, 4 metrics) |
| v2.0 | 2026-02-26 | Metrological reframing (5 layers); bounded K_trust; SPC; uncertainty budgets; cold-start; failure modes; threat model; latency budget; graduated response; windowed MTBH; two-tier determinism |
| v3.0 | 2026-02-26 | Morphism-theoretic integration: Z_ai/Z_real formalization via Wymore tuples; S_a reinterpreted as structural morphism quality (degree of homomorphism); C_r reinterpreted as behavioral morphism quality (output distance); MTBH as morphism failure rate with clustering analysis; traceability chain as morphism composition; multi-centroid extension for non-convex state spaces; adversarial robustness via two-axis independence; bio-inspired regulation reinterpreted as morphism maintenance; connection to WySE Metamodel verification theory |
| v4.0 | 2026-02-27 | Ontology-grounded trust metrology: Circuit Breaker Trust Ontology (CBTO) — OWL 2 DL TBox with BFO alignment (~25 classes, ~20 object properties, ~10 data properties); illustrative ABox (~30 individuals); 6 SHACL validation shapes (two-tier severity); 10 SPARQL competency queries across 4 domains; PROV-O provenance model replacing opaque audit hash; federated graph topology schema; SPC–ontology version linkage; automated consistency gate (two-tier validation pipeline); ontology completeness assessment; SOSA/SSN optional sensor alignment; 2 new failure modes (schema violation, SPARQL endpoint unavailable); seed ontology bootstrapping protocol |

## Appendix B — Version Mapping

| v1 Subsystem | v2 Layer | v3 Layer | Morphism Role | v4 Ontological Artifact |
|-------------|---------|---------|--------------|------------------------|
| 1. Semantic Knowledge | Reference Standards | Reference Standards | Specifies Z_real | `cb:ReferenceSystemModel`, `cb:FederatedGraphNode`, `cb:UnifyingOntology` |
| 2. Context Engine | Measurement Instruments | Morphism Instruments | Measures h: Z_ai --> Z_real | `cb:MorphismMapping`, `cb:ComponentMapping`, `cb:StructuralQuality`, `cb:BehavioralQuality` |
| 3. Veto Gate | Statistical Process Control | Statistical Process Control | Monitors morphism quality over time | `cb:ControlChart`, `cb:BreakerState` enumeration, `cb:calibratedAgainstVersion` |
| 4. Recursive Learning | Closed-Loop Control | Closed-Loop Morphism Maintenance | Maintains h within quality envelope | SHACL validation pipeline (§3.4.1), SPARQL CQs (App E.4) |
| 5. Human Interaction | Underwriting Interface | Underwriting Interface | Human underwrites morphism quality | `cb:BreakerDecision` (PROV-O), `cb:MeasurementSnapshot`, `cb:BreakerVerdict` |

| v2 Metric | v3 Metric | Morphism Axis |
|----------|----------|--------------|
| S_a (semantic anomaly) | sigma / S_a (structural morphism quality) | Structural: degree of homomorphism |
| C_r (contextual relevancy) | D / C_r (behavioral morphism quality) | Behavioral: output distance |
| MTBH | MTBH (morphism failure rate) | Longitudinal: failure interval |
| HCC (hallucination clustering) | MFCC (morphism failure clustering) | Longitudinal: failure correlation |
| K_trust | K_trust | Composite: morphism health x oversight capacity |

## Appendix C — Threshold Calibration Protocol

1. **Identify the operational domain.** Select the federated graph, sensor suite, and environmental variables that define Z_real for this deployment.
2. **Express the reference standard in tuple form.** Identify S_real, I_real, O_real, N_real, R_real — at minimum informally, ideally as a formal ontology. This is the specification against which Z_ai will be measured.
    - **2a. Validate the seed ontology [NEW].** Run the CBTO validation pipeline (Section 8.2) at Tier 2 against the initial Z_real specification. Confirm SHACL shapes pass and at least CQ-T01, CQ-T03, and CQ-A01 return expected results. This ensures the reference standard is formally well-formed before baseline collection begins.
3. **Collect baseline morphism data** during bootstrap (minimum 25 subgroups). Record sigma and D for every decision.
4. **Compute SPC control limits** for sigma and D using X-bar/R or X-bar/S methods.
5. **Assess morphism stability** (Cpk). If Cpk >= 1.33 for both axes, the morphism is stable enough for autonomous operation. If Cpk < 1.33 on either axis, investigate: is the AI's model too coarse (structural), or are its values drifting (behavioral)?
6. **Set K_trust lockdown threshold** via tabletop exercises.
7. **Document** all parameters, their derivation, and the data used.
8. **Schedule recalibration** based on observed morphism stability and the rate of Z_real evolution.

## Appendix D — References

- [4] Wach, P., Sandman, T., & Iyer, N. "Toward a Library of Isomorphic Patterns for Systems Engineering." *CSER 2026* (in revision).
- [5] Wymore, A. W. *Model-Based Systems Engineering*. CRC Press, 1993.
- [22] Wach, P., Sandman, T., Iyer, N., & Paredis, C. J. J. "Degree of homomorphism for characterizing morphic relationships between system models." *Proc. ASME IDETC*, 2024.
- [23] Wach, P. "The WySE Metamodel: Wymorian Systems Engineering Metamodel for verification model definition." 2025.
- [24] JCGM. "Evaluation of measurement data — Guide to the expression of uncertainty in measurement (GUM)." *JCGM 100:2008*.
- [25] Wach, P. "JOE-G Portfolio Governance Ontology." OWL 2 DL, v1.1.0. 2026. [NEW]
- [26] Arp, R., Smith, B., & Spear, A. D. *Building Ontologies with Basic Formal Ontology*. MIT Press, 2015. [NEW]
- [27] W3C. "Shapes Constraint Language (SHACL)." W3C Recommendation, 2017. [NEW]
- [28] Moreau, L. & Missier, P. "PROV-DM: The PROV Data Model." W3C Recommendation, 2013. [NEW]
- [29] W3C. "SPARQL 1.1 Query Language." W3C Recommendation, 2013. [NEW]
- [30] Haller, A. et al. "The Modular SSN Ontology: A Joint W3C and OGC Standard Specifying the Semantics of Sensors, Observations, Sampling, and Actuation." *Semantic Web*, 10(1), 2019. [NEW]
- [31] Industrial Ontology Foundry (IOF). "IOF Core Ontology." 2023. [NEW]

## Appendix E — Circuit Breaker Trust Ontology Reference [NEW]

This appendix contains the complete CBTO artifacts: TBox (E.1), illustrative ABox (E.2), SHACL validation shapes (E.3), and SPARQL competency query catalog (E.4).

### E.1 TBox — Class and Property Hierarchy

The complete CBTO TBox in Turtle syntax. Namespace: `http://circuitbreaker.ontology/trust#` (prefix `cb:`).

```turtle
@prefix cb:    <http://circuitbreaker.ontology/trust#> .
@prefix obo:   <http://purl.obolibrary.org/obo/> .
@prefix owl:   <http://www.w3.org/2002/07/owl#> .
@prefix rdf:   <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs:  <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd:   <http://www.w3.org/2001/XMLSchema#> .
@prefix dc:    <http://purl.org/dc/elements/1.1/> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix prov:  <http://www.w3.org/ns/prov#> .
@prefix sosa:  <http://www.w3.org/ns/sosa/> .
@prefix sh:    <http://www.w3.org/ns/shacl#> .

# =============================================================================
# Circuit Breaker Trust Ontology (CBTO) v1.0.0
# TBox for morphism-grounded trust metrology in autonomous AI systems.
#
# BFO 2020 aligned. PROV-O for provenance. SOSA/SSN stub for sensors.
#
# Domain coverage:
#   - System Models: Wymore five-tuples (Z_real, Z_ai)
#   - Morphism: Mappings, component mappings, quality metrics
#   - Architecture: Federated graphs, control charts, breaker states
#   - Provenance: PROV-O aligned decision audit trail
#   - Sensors: Optional SOSA alignment stub
# =============================================================================

<http://circuitbreaker.ontology/trust> rdf:type owl:Ontology ;
    rdfs:label "Circuit Breaker Trust Ontology"@en ;
    rdfs:comment "OWL 2 DL ontology for morphism-grounded trust metrology.
        Formalizes Wymore system tuples, morphism quality metrics, SPC
        linkage, federated graph topology, and PROV-O decision provenance
        for autonomous AI circuit breaker systems."@en ;
    owl:versionInfo "1.0.0" ;
    dc:creator "PostWach CTO / AI Circuit Breaker Project" ;
    dc:date "2026-02-27"^^xsd:date ;
    dcterms:license <https://creativecommons.org/licenses/by/4.0/> ;
    owl:imports <http://www.w3.org/ns/prov#> .

# =============================================================================
# BFO Class Reference (imported)
# =============================================================================
# obo:BFO_0000030 - object (independent continuant)
# obo:BFO_0000031 - generically dependent continuant (GDC)
# obo:BFO_0000019 - quality (specifically dependent continuant)
# obo:BFO_0000015 - process (occurrent)

# =============================================================================
# CLASSES — System Model Domain (Wymore Tuples)
# =============================================================================

cb:SystemModel rdf:type owl:Class ;
    rdfs:subClassOf obo:BFO_0000031 ;
    rdfs:label "System Model"@en ;
    rdfs:comment "A Wymore five-tuple Z = (S, I, O, N, R). GDC: an information
        content entity describing a system's state space, inputs, outputs,
        transitions, and readout."@en ;
    rdfs:isDefinedBy <http://circuitbreaker.ontology/trust> .

cb:ReferenceSystemModel rdf:type owl:Class ;
    rdfs:subClassOf cb:SystemModel ;
    rdfs:label "Reference System Model"@en ;
    rdfs:comment "Z_real: the reference standard derived from calibrated sensors
        and versioned domain ontologies."@en ;
    rdfs:isDefinedBy <http://circuitbreaker.ontology/trust> .

cb:AgentSystemModel rdf:type owl:Class ;
    rdfs:subClassOf cb:SystemModel ;
    owl:disjointWith cb:ReferenceSystemModel ;
    rdfs:label "Agent System Model"@en ;
    rdfs:comment "Z_ai: the AI agent's internal model of the system."@en ;
    rdfs:isDefinedBy <http://circuitbreaker.ontology/trust> .

cb:StateSet rdf:type owl:Class ;
    rdfs:subClassOf obo:BFO_0000031 ;
    rdfs:label "State Set"@en ;
    rdfs:comment "The set S of a Wymore tuple."@en ;
    rdfs:isDefinedBy <http://circuitbreaker.ontology/trust> .

cb:InputSet rdf:type owl:Class ;
    rdfs:subClassOf obo:BFO_0000031 ;
    rdfs:label "Input Set"@en ;
    rdfs:comment "The set I of a Wymore tuple."@en ;
    rdfs:isDefinedBy <http://circuitbreaker.ontology/trust> .

cb:OutputSet rdf:type owl:Class ;
    rdfs:subClassOf obo:BFO_0000031 ;
    rdfs:label "Output Set"@en ;
    rdfs:comment "The set O of a Wymore tuple."@en ;
    rdfs:isDefinedBy <http://circuitbreaker.ontology/trust> .

cb:TransitionFunction rdf:type owl:Class ;
    rdfs:subClassOf obo:BFO_0000031 ;
    rdfs:label "Transition Function"@en ;
    rdfs:comment "N: S x I --> S. A GDC describing valid state transitions."@en ;
    rdfs:isDefinedBy <http://circuitbreaker.ontology/trust> .

cb:ReadoutFunction rdf:type owl:Class ;
    rdfs:subClassOf obo:BFO_0000031 ;
    rdfs:label "Readout Function"@en ;
    rdfs:comment "R: S --> O. A GDC describing the state-to-output mapping."@en ;
    rdfs:isDefinedBy <http://circuitbreaker.ontology/trust> .

cb:SetMember rdf:type owl:Class ;
    rdfs:subClassOf obo:BFO_0000031 ;
    rdfs:label "Set Member"@en ;
    rdfs:comment "An individual element belonging to a StateSet, InputSet, or
        OutputSet."@en ;
    rdfs:isDefinedBy <http://circuitbreaker.ontology/trust> .

# =============================================================================
# CLASSES — Morphism Domain
# =============================================================================

cb:MorphismMapping rdf:type owl:Class ;
    rdfs:subClassOf obo:BFO_0000031 ;
    rdfs:label "Morphism Mapping"@en ;
    rdfs:comment "A structure-preserving mapping h: Z_ai --> Z_real. Encodes
        component mappings (hi, ho, hq) and quality metrics (sigma, D)."@en ;
    rdfs:isDefinedBy <http://circuitbreaker.ontology/trust> .

cb:ComponentMapping rdf:type owl:Class ;
    rdfs:subClassOf obo:BFO_0000031 ;
    rdfs:label "Component Mapping"@en ;
    rdfs:comment "A mapping between corresponding components of two system models
        (state-to-state, input-to-input, or output-to-output)."@en ;
    rdfs:isDefinedBy <http://circuitbreaker.ontology/trust> .

cb:StructuralQuality rdf:type owl:Class ;
    rdfs:subClassOf obo:BFO_0000019 ;
    rdfs:label "Structural Quality"@en ;
    rdfs:comment "Degree of homomorphism (sigma). A quality inhering in a
        MorphismMapping. sigma=1.0 is isomorphism."@en ;
    rdfs:isDefinedBy <http://circuitbreaker.ontology/trust> .

cb:BehavioralQuality rdf:type owl:Class ;
    rdfs:subClassOf obo:BFO_0000019 ;
    rdfs:label "Behavioral Quality"@en ;
    rdfs:comment "Output distance (D). A quality inhering in a MorphismMapping.
        D=0.0 is perfect behavioral match."@en ;
    rdfs:isDefinedBy <http://circuitbreaker.ontology/trust> .

# =============================================================================
# CLASSES — Architecture Domain
# =============================================================================

cb:FederatedGraphNode rdf:type owl:Class ;
    rdfs:subClassOf obo:BFO_0000031 ;
    rdfs:label "Federated Graph Node"@en ;
    rdfs:comment "A domain-specific knowledge graph in the federated topology.
        Each node specifies a subsystem of Z_real."@en ;
    rdfs:isDefinedBy <http://circuitbreaker.ontology/trust> .

cb:UnifyingOntology rdf:type owl:Class ;
    rdfs:subClassOf cb:FederatedGraphNode ;
    rdfs:label "Unifying Ontology"@en ;
    rdfs:comment "Top-level ontology mapping across federated graph nodes."@en ;
    rdfs:isDefinedBy <http://circuitbreaker.ontology/trust> .

cb:ControlChart rdf:type owl:Class ;
    rdfs:subClassOf obo:BFO_0000031 ;
    rdfs:label "Control Chart"@en ;
    rdfs:comment "An SPC control chart tracking a morphism quality metric.
        Linked to the ontology version against which its baseline was
        computed."@en ;
    rdfs:isDefinedBy <http://circuitbreaker.ontology/trust> .

cb:BreakerState rdf:type owl:Class ;
    rdfs:subClassOf obo:BFO_0000019 ;
    owl:equivalentClass [ rdf:type owl:Class ;
        owl:oneOf ( cb:Normal cb:Caution cb:Restrict cb:Halt cb:Lockdown ) ] ;
    rdfs:label "Breaker State"@en ;
    rdfs:comment "Circuit breaker operational state enumeration."@en ;
    rdfs:isDefinedBy <http://circuitbreaker.ontology/trust> .

cb:Normal   rdf:type owl:NamedIndividual, cb:BreakerState .
cb:Caution  rdf:type owl:NamedIndividual, cb:BreakerState .
cb:Restrict rdf:type owl:NamedIndividual, cb:BreakerState .
cb:Halt     rdf:type owl:NamedIndividual, cb:BreakerState .
cb:Lockdown rdf:type owl:NamedIndividual, cb:BreakerState .

# =============================================================================
# CLASSES — Provenance Domain (PROV-O aligned)
# =============================================================================

cb:BreakerDecision rdf:type owl:Class ;
    rdfs:subClassOf obo:BFO_0000015 ;
    rdfs:subClassOf prov:Activity ;
    rdfs:label "Breaker Decision"@en ;
    rdfs:comment "A circuit breaker evaluation event. PROV-O Activity: uses
        measurement snapshots, generates verdicts."@en ;
    rdfs:isDefinedBy <http://circuitbreaker.ontology/trust> .

cb:MeasurementSnapshot rdf:type owl:Class ;
    rdfs:subClassOf obo:BFO_0000031 ;
    rdfs:subClassOf prov:Entity ;
    rdfs:label "Measurement Snapshot"@en ;
    rdfs:comment "A point-in-time capture of sigma, D, and K_trust values."@en ;
    rdfs:isDefinedBy <http://circuitbreaker.ontology/trust> .

cb:BreakerVerdict rdf:type owl:Class ;
    rdfs:subClassOf obo:BFO_0000031 ;
    rdfs:subClassOf prov:Entity ;
    rdfs:label "Breaker Verdict"@en ;
    rdfs:comment "The verdict produced by a BreakerDecision: a BreakerState
        with provenance linking to the measurement snapshot."@en ;
    rdfs:isDefinedBy <http://circuitbreaker.ontology/trust> .

cb:SensorSnapshot rdf:type owl:Class ;
    rdfs:subClassOf obo:BFO_0000031 ;
    rdfs:subClassOf prov:Entity ;
    rdfs:label "Sensor Snapshot"@en ;
    rdfs:comment "Raw sensor readings consumed by a BreakerDecision."@en ;
    rdfs:isDefinedBy <http://circuitbreaker.ontology/trust> .

cb:HumanUnderwriter rdf:type owl:Class ;
    rdfs:subClassOf obo:BFO_0000030 ;
    rdfs:subClassOf prov:Agent ;
    rdfs:label "Human Underwriter"@en ;
    rdfs:comment "The human operator who underwrites morphism quality."@en ;
    rdfs:isDefinedBy <http://circuitbreaker.ontology/trust> .

# =============================================================================
# CLASSES — Sensor Domain (SOSA stub)
# =============================================================================

cb:SensorSource rdf:type owl:Class ;
    rdfs:subClassOf obo:BFO_0000030 ;
    rdfs:label "Sensor Source"@en ;
    rdfs:comment "A calibrated sensor contributing to Z_real observations.
        Optional alignment: owl:equivalentClass sosa:Sensor for deployments
        adopting SOSA/SSN."@en ;
    rdfs:seeAlso sosa:Sensor ;
    rdfs:isDefinedBy <http://circuitbreaker.ontology/trust> .

# =============================================================================
# OBJECT PROPERTIES — System Model
# =============================================================================

cb:hasStateSet rdf:type owl:ObjectProperty, owl:FunctionalProperty ;
    rdfs:domain cb:SystemModel ; rdfs:range cb:StateSet ;
    rdfs:label "has state set"@en ;
    rdfs:isDefinedBy <http://circuitbreaker.ontology/trust> .

cb:hasInputSet rdf:type owl:ObjectProperty, owl:FunctionalProperty ;
    rdfs:domain cb:SystemModel ; rdfs:range cb:InputSet ;
    rdfs:label "has input set"@en ;
    rdfs:isDefinedBy <http://circuitbreaker.ontology/trust> .

cb:hasOutputSet rdf:type owl:ObjectProperty, owl:FunctionalProperty ;
    rdfs:domain cb:SystemModel ; rdfs:range cb:OutputSet ;
    rdfs:label "has output set"@en ;
    rdfs:isDefinedBy <http://circuitbreaker.ontology/trust> .

cb:hasTransitionFunction rdf:type owl:ObjectProperty, owl:FunctionalProperty ;
    rdfs:domain cb:SystemModel ; rdfs:range cb:TransitionFunction ;
    rdfs:label "has transition function"@en ;
    rdfs:isDefinedBy <http://circuitbreaker.ontology/trust> .

cb:hasReadoutFunction rdf:type owl:ObjectProperty, owl:FunctionalProperty ;
    rdfs:domain cb:SystemModel ; rdfs:range cb:ReadoutFunction ;
    rdfs:label "has readout function"@en ;
    rdfs:isDefinedBy <http://circuitbreaker.ontology/trust> .

cb:memberOfSet rdf:type owl:ObjectProperty ;
    rdfs:domain cb:SetMember ;
    rdfs:range [ rdf:type owl:Class ;
        owl:unionOf ( cb:StateSet cb:InputSet cb:OutputSet ) ] ;
    rdfs:label "member of set"@en ;
    rdfs:isDefinedBy <http://circuitbreaker.ontology/trust> .

# =============================================================================
# OBJECT PROPERTIES — Morphism
# =============================================================================

cb:mapsFrom rdf:type owl:ObjectProperty, owl:FunctionalProperty ;
    rdfs:domain cb:MorphismMapping ; rdfs:range cb:AgentSystemModel ;
    rdfs:label "maps from"@en ;
    rdfs:isDefinedBy <http://circuitbreaker.ontology/trust> .

cb:mapsTo rdf:type owl:ObjectProperty, owl:FunctionalProperty ;
    rdfs:domain cb:MorphismMapping ; rdfs:range cb:ReferenceSystemModel ;
    rdfs:label "maps to"@en ;
    rdfs:isDefinedBy <http://circuitbreaker.ontology/trust> .

cb:hasInputMapping rdf:type owl:ObjectProperty, owl:FunctionalProperty ;
    rdfs:domain cb:MorphismMapping ; rdfs:range cb:ComponentMapping ;
    rdfs:label "input mapping hi"@en ;
    rdfs:isDefinedBy <http://circuitbreaker.ontology/trust> .

cb:hasOutputMapping rdf:type owl:ObjectProperty, owl:FunctionalProperty ;
    rdfs:domain cb:MorphismMapping ; rdfs:range cb:ComponentMapping ;
    rdfs:label "output mapping ho"@en ;
    rdfs:isDefinedBy <http://circuitbreaker.ontology/trust> .

cb:hasStateMapping rdf:type owl:ObjectProperty, owl:FunctionalProperty ;
    rdfs:domain cb:MorphismMapping ; rdfs:range cb:ComponentMapping ;
    rdfs:label "state mapping hq"@en ;
    rdfs:isDefinedBy <http://circuitbreaker.ontology/trust> .

cb:hasStructuralQuality rdf:type owl:ObjectProperty, owl:FunctionalProperty ;
    rdfs:domain cb:MorphismMapping ; rdfs:range cb:StructuralQuality ;
    rdfs:label "has structural quality"@en ;
    rdfs:isDefinedBy <http://circuitbreaker.ontology/trust> .

cb:hasBehavioralQuality rdf:type owl:ObjectProperty, owl:FunctionalProperty ;
    rdfs:domain cb:MorphismMapping ; rdfs:range cb:BehavioralQuality ;
    rdfs:label "has behavioral quality"@en ;
    rdfs:isDefinedBy <http://circuitbreaker.ontology/trust> .

# =============================================================================
# OBJECT PROPERTIES — Architecture
# =============================================================================

cb:composesGraph rdf:type owl:ObjectProperty ;
    rdfs:domain cb:UnifyingOntology ; rdfs:range cb:FederatedGraphNode ;
    rdfs:label "composes graph"@en ;
    rdfs:isDefinedBy <http://circuitbreaker.ontology/trust> .

cb:calibratedAgainstVersion rdf:type owl:ObjectProperty, owl:FunctionalProperty ;
    rdfs:domain cb:ControlChart ; rdfs:range cb:FederatedGraphNode ;
    rdfs:label "calibrated against version"@en ;
    rdfs:isDefinedBy <http://circuitbreaker.ontology/trust> .

cb:hasBreakerState rdf:type owl:ObjectProperty, owl:FunctionalProperty ;
    rdfs:domain cb:BreakerVerdict ; rdfs:range cb:BreakerState ;
    rdfs:label "has breaker state"@en ;
    rdfs:isDefinedBy <http://circuitbreaker.ontology/trust> .

# =============================================================================
# OBJECT PROPERTIES — Provenance
# =============================================================================

cb:usesSnapshot rdf:type owl:ObjectProperty ;
    rdfs:subPropertyOf prov:used ;
    rdfs:domain cb:BreakerDecision ; rdfs:range cb:MeasurementSnapshot ;
    rdfs:label "uses snapshot"@en ;
    rdfs:isDefinedBy <http://circuitbreaker.ontology/trust> .

cb:usesOntologyVersion rdf:type owl:ObjectProperty ;
    rdfs:subPropertyOf prov:used ;
    rdfs:domain cb:BreakerDecision ; rdfs:range cb:FederatedGraphNode ;
    rdfs:label "uses ontology version"@en ;
    rdfs:isDefinedBy <http://circuitbreaker.ontology/trust> .

cb:generatesVerdict rdf:type owl:ObjectProperty ;
    rdfs:subPropertyOf prov:generated ;
    rdfs:domain cb:BreakerDecision ; rdfs:range cb:BreakerVerdict ;
    rdfs:label "generates verdict"@en ;
    rdfs:isDefinedBy <http://circuitbreaker.ontology/trust> .

cb:assessesAgent rdf:type owl:ObjectProperty ;
    rdfs:subPropertyOf prov:wasAssociatedWith ;
    rdfs:domain cb:BreakerDecision ; rdfs:range cb:AgentSystemModel ;
    rdfs:label "assesses agent"@en ;
    rdfs:isDefinedBy <http://circuitbreaker.ontology/trust> .

cb:underwrittenBy rdf:type owl:ObjectProperty ;
    rdfs:subPropertyOf prov:wasAssociatedWith ;
    rdfs:domain cb:BreakerDecision ; rdfs:range cb:HumanUnderwriter ;
    rdfs:label "underwritten by"@en ;
    rdfs:isDefinedBy <http://circuitbreaker.ontology/trust> .

cb:producedSensor rdf:type owl:ObjectProperty ;
    rdfs:domain cb:SensorSource ; rdfs:range cb:SensorSnapshot ;
    rdfs:label "produced sensor snapshot"@en ;
    rdfs:isDefinedBy <http://circuitbreaker.ontology/trust> .

# =============================================================================
# DATA PROPERTIES
# =============================================================================

cb:sigmaValue rdf:type owl:DatatypeProperty, owl:FunctionalProperty ;
    rdfs:domain cb:StructuralQuality ; rdfs:range xsd:decimal ;
    rdfs:comment "Degree of homomorphism [0.0, 1.0]."@en ;
    rdfs:isDefinedBy <http://circuitbreaker.ontology/trust> .

cb:outputDistance rdf:type owl:DatatypeProperty, owl:FunctionalProperty ;
    rdfs:domain cb:BehavioralQuality ; rdfs:range xsd:decimal ;
    rdfs:comment "Maximum output divergence D >= 0."@en ;
    rdfs:isDefinedBy <http://circuitbreaker.ontology/trust> .

cb:kTrustValue rdf:type owl:DatatypeProperty, owl:FunctionalProperty ;
    rdfs:domain cb:MeasurementSnapshot ; rdfs:range xsd:decimal ;
    rdfs:comment "Human-AI Calibration Coefficient [0.0, 1.0]."@en ;
    rdfs:isDefinedBy <http://circuitbreaker.ontology/trust> .

cb:snapshotTimestamp rdf:type owl:DatatypeProperty, owl:FunctionalProperty ;
    rdfs:domain cb:MeasurementSnapshot ; rdfs:range xsd:dateTime ;
    rdfs:isDefinedBy <http://circuitbreaker.ontology/trust> .

cb:graphVersion rdf:type owl:DatatypeProperty, owl:FunctionalProperty ;
    rdfs:domain cb:FederatedGraphNode ; rdfs:range xsd:string ;
    rdfs:comment "Semantic version (e.g., '2.1.0')."@en ;
    rdfs:isDefinedBy <http://circuitbreaker.ontology/trust> .

cb:graphEndpoint rdf:type owl:DatatypeProperty, owl:FunctionalProperty ;
    rdfs:domain cb:FederatedGraphNode ; rdfs:range xsd:anyURI ;
    rdfs:comment "SPARQL endpoint URI."@en ;
    rdfs:isDefinedBy <http://circuitbreaker.ontology/trust> .

cb:chartMetric rdf:type owl:DatatypeProperty, owl:FunctionalProperty ;
    rdfs:domain cb:ControlChart ; rdfs:range xsd:string ;
    rdfs:comment "Tracked metric: 'sigma', 'D', 'MTBH', or 'K_trust'."@en ;
    rdfs:isDefinedBy <http://circuitbreaker.ontology/trust> .

cb:upperControlLimit rdf:type owl:DatatypeProperty, owl:FunctionalProperty ;
    rdfs:domain cb:ControlChart ; rdfs:range xsd:decimal ;
    rdfs:isDefinedBy <http://circuitbreaker.ontology/trust> .

cb:lowerControlLimit rdf:type owl:DatatypeProperty, owl:FunctionalProperty ;
    rdfs:domain cb:ControlChart ; rdfs:range xsd:decimal ;
    rdfs:isDefinedBy <http://circuitbreaker.ontology/trust> .

cb:baselineSubgroupCount rdf:type owl:DatatypeProperty, owl:FunctionalProperty ;
    rdfs:domain cb:ControlChart ; rdfs:range xsd:integer ;
    rdfs:comment "Subgroups used for baseline (min 25)."@en ;
    rdfs:isDefinedBy <http://circuitbreaker.ontology/trust> .

cb:memberLabel rdf:type owl:DatatypeProperty ;
    rdfs:domain cb:SetMember ; rdfs:range xsd:string ;
    rdfs:comment "Human-readable label for a set member."@en ;
    rdfs:isDefinedBy <http://circuitbreaker.ontology/trust> .

cb:sensorType rdf:type owl:DatatypeProperty ;
    rdfs:domain cb:SensorSource ; rdfs:range xsd:string ;
    rdfs:isDefinedBy <http://circuitbreaker.ontology/trust> .

cb:calibrationDate rdf:type owl:DatatypeProperty ;
    rdfs:domain cb:SensorSource ; rdfs:range xsd:date ;
    rdfs:isDefinedBy <http://circuitbreaker.ontology/trust> .

# End of CBTO TBox v1.0.0
# Total: 25 classes, 20 object properties, 12 data properties
```

### E.2 Illustrative ABox — Telecom Network Management Domain

A small concrete example demonstrating the CBTO populated for a telecom network management scenario. The AI agent manages fiber-optic network elements; the circuit breaker monitors its morphism to physical network reality.

```turtle
@prefix cb:   <http://circuitbreaker.ontology/trust#> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .

# =============================================================================
# Illustrative ABox — Telecom Network Management (~30 individuals)
# =============================================================================

# --- Reference System Model: Physical Fiber Network ---
cb:z-real-fiber  a  cb:ReferenceSystemModel ;
    cb:hasStateSet           cb:ss-fiber-states ;
    cb:hasInputSet           cb:is-fiber-inputs ;
    cb:hasOutputSet          cb:os-fiber-outputs ;
    cb:hasTransitionFunction cb:tf-fiber-transitions ;
    cb:hasReadoutFunction    cb:rf-fiber-readout .

cb:ss-fiber-states  a  cb:StateSet .
cb:is-fiber-inputs  a  cb:InputSet .
cb:os-fiber-outputs a  cb:OutputSet .
cb:tf-fiber-transitions  a  cb:TransitionFunction .
cb:rf-fiber-readout      a  cb:ReadoutFunction .

# State set members (4 fiber link states)
cb:state-active     a cb:SetMember ; cb:memberOfSet cb:ss-fiber-states ; cb:memberLabel "Active" .
cb:state-degraded   a cb:SetMember ; cb:memberOfSet cb:ss-fiber-states ; cb:memberLabel "Degraded" .
cb:state-failed     a cb:SetMember ; cb:memberOfSet cb:ss-fiber-states ; cb:memberLabel "Failed" .
cb:state-maintenance a cb:SetMember ; cb:memberOfSet cb:ss-fiber-states ; cb:memberLabel "Maintenance" .

# Input set members (3 command types)
cb:input-provision  a cb:SetMember ; cb:memberOfSet cb:is-fiber-inputs ; cb:memberLabel "Provision" .
cb:input-reroute    a cb:SetMember ; cb:memberOfSet cb:is-fiber-inputs ; cb:memberLabel "Reroute" .
cb:input-decommission a cb:SetMember ; cb:memberOfSet cb:is-fiber-inputs ; cb:memberLabel "Decommission" .

# Output set members (3 observable outcomes)
cb:output-optical-power a cb:SetMember ; cb:memberOfSet cb:os-fiber-outputs ; cb:memberLabel "Optical Power dBm" .
cb:output-bit-error     a cb:SetMember ; cb:memberOfSet cb:os-fiber-outputs ; cb:memberLabel "Bit Error Rate" .
cb:output-latency       a cb:SetMember ; cb:memberOfSet cb:os-fiber-outputs ; cb:memberLabel "Latency ms" .

# --- Agent System Model: AI Network Manager ---
cb:z-ai-netmgr  a  cb:AgentSystemModel ;
    cb:hasStateSet           cb:ss-ai-states ;
    cb:hasInputSet           cb:is-ai-inputs ;
    cb:hasOutputSet          cb:os-ai-outputs ;
    cb:hasTransitionFunction cb:tf-ai-transitions ;
    cb:hasReadoutFunction    cb:rf-ai-readout .

cb:ss-ai-states       a  cb:StateSet .
cb:is-ai-inputs       a  cb:InputSet .
cb:os-ai-outputs      a  cb:OutputSet .
cb:tf-ai-transitions  a  cb:TransitionFunction .
cb:rf-ai-readout      a  cb:ReadoutFunction .

# --- Morphism Mapping: AI --> Physical Network ---
cb:h-netmgr-to-fiber  a  cb:MorphismMapping ;
    cb:mapsFrom          cb:z-ai-netmgr ;
    cb:mapsTo            cb:z-real-fiber ;
    cb:hasStateMapping   cb:cm-states ;
    cb:hasInputMapping   cb:cm-inputs ;
    cb:hasOutputMapping  cb:cm-outputs ;
    cb:hasStructuralQuality  cb:sq-current ;
    cb:hasBehavioralQuality  cb:bq-current .

cb:cm-states  a  cb:ComponentMapping .
cb:cm-inputs  a  cb:ComponentMapping .
cb:cm-outputs a  cb:ComponentMapping .

cb:sq-current  a  cb:StructuralQuality ;
    cb:sigmaValue  "0.92"^^xsd:decimal .

cb:bq-current  a  cb:BehavioralQuality ;
    cb:outputDistance  "0.04"^^xsd:decimal .

# --- Federated Graph Topology ---
cb:telecom-ontology  a  cb:FederatedGraphNode ;
    cb:graphVersion   "2.1.0" ;
    cb:graphEndpoint  "http://localhost:3030/telecom/sparql"^^xsd:anyURI .

cb:geo-ontology  a  cb:FederatedGraphNode ;
    cb:graphVersion   "1.3.0" ;
    cb:graphEndpoint  "http://localhost:3030/geo/sparql"^^xsd:anyURI .

cb:unifying-telecom  a  cb:UnifyingOntology ;
    cb:graphVersion   "1.0.0" ;
    cb:graphEndpoint  "http://localhost:3030/unified/sparql"^^xsd:anyURI ;
    cb:composesGraph  cb:telecom-ontology ;
    cb:composesGraph  cb:geo-ontology .

# --- Control Charts ---
cb:chart-sigma  a  cb:ControlChart ;
    cb:chartMetric             "sigma" ;
    cb:upperControlLimit       "1.0"^^xsd:decimal ;
    cb:lowerControlLimit       "0.78"^^xsd:decimal ;
    cb:baselineSubgroupCount   30 ;
    cb:calibratedAgainstVersion  cb:telecom-ontology .

cb:chart-D  a  cb:ControlChart ;
    cb:chartMetric             "D" ;
    cb:upperControlLimit       "0.12"^^xsd:decimal ;
    cb:lowerControlLimit       "0.0"^^xsd:decimal ;
    cb:baselineSubgroupCount   30 ;
    cb:calibratedAgainstVersion  cb:telecom-ontology .

# --- Sensor Sources ---
cb:sensor-optical-pm  a  cb:SensorSource ;
    cb:sensorType       "Optical Power Meter" ;
    cb:calibrationDate  "2026-01-15"^^xsd:date .

cb:sensor-otdr  a  cb:SensorSource ;
    cb:sensorType       "OTDR" ;
    cb:calibrationDate  "2026-02-01"^^xsd:date .

# --- Provenance: Sample Breaker Decision ---
cb:decision-001  a  cb:BreakerDecision, prov:Activity ;
    prov:startedAtTime       "2026-02-27T14:30:22Z"^^xsd:dateTime ;
    cb:usesSnapshot          cb:snapshot-001 ;
    cb:usesOntologyVersion   cb:telecom-ontology ;
    cb:assessesAgent         cb:z-ai-netmgr ;
    cb:generatesVerdict      cb:verdict-001 .

cb:snapshot-001  a  cb:MeasurementSnapshot, prov:Entity ;
    cb:sigmaValue        "0.92"^^xsd:decimal ;
    cb:outputDistance     "0.04"^^xsd:decimal ;
    cb:kTrustValue        "0.78"^^xsd:decimal ;
    cb:snapshotTimestamp  "2026-02-27T14:30:22Z"^^xsd:dateTime .

cb:verdict-001  a  cb:BreakerVerdict, prov:Entity ;
    cb:hasBreakerState       cb:Normal ;
    prov:wasGeneratedBy      cb:decision-001 ;
    prov:wasDerivedFrom      cb:snapshot-001 .

cb:underwriter-ops  a  cb:HumanUnderwriter, prov:Agent .

# End of illustrative ABox
# Total: ~32 individuals, ~100 triples
```

### E.3 SHACL Validation Shapes

Six SHACL NodeShapes enforcing structural constraints on CBTO ABox individuals. Two severity tiers: `sh:Violation` (blocks release) and `sh:Warning` (advisory).

```turtle
@prefix cb:   <http://circuitbreaker.ontology/trust#> .
@prefix sh:   <http://www.w3.org/ns/shacl#> .
@prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
@prefix owl:  <http://www.w3.org/2002/07/owl#> .
@prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix dc:   <http://purl.org/dc/elements/1.1/> .

<http://circuitbreaker.ontology/trust/shacl> rdf:type owl:Ontology ;
    rdfs:label "CBTO SHACL Validation Shapes"@en ;
    rdfs:comment "6 SHACL shapes for validating CBTO ABox individuals.
        Two-tier severity: Violation (blocking) and Warning (advisory)."@en ;
    owl:versionInfo "1.0.0" ;
    dc:creator "PostWach CTO / AI Circuit Breaker Project" ;
    dc:date "2026-02-27"^^xsd:date .

# =============================================================================
# 1. SystemModelShape — validates SystemModel individuals
# =============================================================================

cb:SystemModelShape rdf:type sh:NodeShape ;
    sh:targetClass cb:SystemModel ;
    sh:severity sh:Violation ;
    rdfs:label "System Model Shape"@en ;

    sh:property [
        sh:path cb:hasStateSet ;
        sh:minCount 1 ; sh:maxCount 1 ;
        sh:class cb:StateSet ;
        sh:message "A SystemModel must have exactly one StateSet." ;
    ] ;
    sh:property [
        sh:path cb:hasInputSet ;
        sh:minCount 1 ; sh:maxCount 1 ;
        sh:class cb:InputSet ;
        sh:message "A SystemModel must have exactly one InputSet." ;
    ] ;
    sh:property [
        sh:path cb:hasOutputSet ;
        sh:minCount 1 ; sh:maxCount 1 ;
        sh:class cb:OutputSet ;
        sh:message "A SystemModel must have exactly one OutputSet." ;
    ] ;
    sh:property [
        sh:path cb:hasTransitionFunction ;
        sh:minCount 1 ; sh:maxCount 1 ;
        sh:class cb:TransitionFunction ;
        sh:message "A SystemModel must have exactly one TransitionFunction." ;
    ] ;
    sh:property [
        sh:path cb:hasReadoutFunction ;
        sh:minCount 1 ; sh:maxCount 1 ;
        sh:class cb:ReadoutFunction ;
        sh:message "A SystemModel must have exactly one ReadoutFunction." ;
    ] .

# =============================================================================
# 2. MorphismMappingShape — validates MorphismMapping individuals
# =============================================================================

cb:MorphismMappingShape rdf:type sh:NodeShape ;
    sh:targetClass cb:MorphismMapping ;
    sh:severity sh:Violation ;
    rdfs:label "Morphism Mapping Shape"@en ;

    sh:property [
        sh:path cb:mapsFrom ;
        sh:minCount 1 ; sh:maxCount 1 ;
        sh:class cb:AgentSystemModel ;
        sh:message "A MorphismMapping must map from exactly one AgentSystemModel." ;
    ] ;
    sh:property [
        sh:path cb:mapsTo ;
        sh:minCount 1 ; sh:maxCount 1 ;
        sh:class cb:ReferenceSystemModel ;
        sh:message "A MorphismMapping must map to exactly one ReferenceSystemModel." ;
    ] ;
    sh:property [
        sh:path cb:hasStateMapping ;
        sh:minCount 1 ; sh:maxCount 1 ;
        sh:class cb:ComponentMapping ;
        sh:message "A MorphismMapping must have exactly one state mapping." ;
    ] ;
    sh:property [
        sh:path cb:hasInputMapping ;
        sh:minCount 1 ; sh:maxCount 1 ;
        sh:class cb:ComponentMapping ;
        sh:message "A MorphismMapping must have exactly one input mapping." ;
    ] ;
    sh:property [
        sh:path cb:hasOutputMapping ;
        sh:minCount 1 ; sh:maxCount 1 ;
        sh:class cb:ComponentMapping ;
        sh:message "A MorphismMapping must have exactly one output mapping." ;
    ] ;
    sh:property [
        sh:path cb:hasStructuralQuality ;
        sh:minCount 1 ; sh:maxCount 1 ;
        sh:class cb:StructuralQuality ;
        sh:message "A MorphismMapping must have exactly one StructuralQuality." ;
    ] ;
    sh:property [
        sh:path cb:hasBehavioralQuality ;
        sh:minCount 1 ; sh:maxCount 1 ;
        sh:class cb:BehavioralQuality ;
        sh:message "A MorphismMapping must have exactly one BehavioralQuality." ;
    ] .

# =============================================================================
# 3. StructuralQualityShape — validates sigma values
# =============================================================================

cb:StructuralQualityShape rdf:type sh:NodeShape ;
    sh:targetClass cb:StructuralQuality ;
    sh:severity sh:Violation ;
    rdfs:label "Structural Quality Shape"@en ;

    sh:property [
        sh:path cb:sigmaValue ;
        sh:minCount 1 ; sh:maxCount 1 ;
        sh:datatype xsd:decimal ;
        sh:minInclusive "0.0"^^xsd:decimal ;
        sh:maxInclusive "1.0"^^xsd:decimal ;
        sh:message "sigmaValue must be a decimal in [0.0, 1.0]." ;
    ] .

# =============================================================================
# 4. ControlChartShape — validates ControlChart individuals
# =============================================================================

cb:ControlChartShape rdf:type sh:NodeShape ;
    sh:targetClass cb:ControlChart ;
    sh:severity sh:Violation ;
    rdfs:label "Control Chart Shape"@en ;

    sh:property [
        sh:path cb:chartMetric ;
        sh:minCount 1 ; sh:maxCount 1 ;
        sh:datatype xsd:string ;
        sh:in ( "sigma" "D" "MTBH" "K_trust" ) ;
        sh:message "chartMetric must be one of: sigma, D, MTBH, K_trust." ;
    ] ;
    sh:property [
        sh:path cb:calibratedAgainstVersion ;
        sh:minCount 1 ; sh:maxCount 1 ;
        sh:class cb:FederatedGraphNode ;
        sh:message "A ControlChart must be calibrated against exactly one graph version." ;
    ] ;
    sh:property [
        sh:path cb:baselineSubgroupCount ;
        sh:minCount 1 ; sh:maxCount 1 ;
        sh:datatype xsd:integer ;
        sh:minInclusive 25 ;
        sh:message "Baseline must have at least 25 subgroups." ;
    ] .

# =============================================================================
# 5. FederatedGraphNodeShape — validates graph nodes (Warning severity)
# =============================================================================

cb:FederatedGraphNodeShape rdf:type sh:NodeShape ;
    sh:targetClass cb:FederatedGraphNode ;
    sh:severity sh:Warning ;
    rdfs:label "Federated Graph Node Shape"@en ;

    sh:property [
        sh:path cb:graphVersion ;
        sh:minCount 1 ; sh:maxCount 1 ;
        sh:datatype xsd:string ;
        sh:message "A FederatedGraphNode should have a version string." ;
    ] ;
    sh:property [
        sh:path cb:graphEndpoint ;
        sh:minCount 1 ; sh:maxCount 1 ;
        sh:datatype xsd:anyURI ;
        sh:message "A FederatedGraphNode should have a SPARQL endpoint URI." ;
    ] .

# =============================================================================
# 6. BreakerDecisionShape — validates provenance chain
# =============================================================================

cb:BreakerDecisionShape rdf:type sh:NodeShape ;
    sh:targetClass cb:BreakerDecision ;
    sh:severity sh:Violation ;
    rdfs:label "Breaker Decision Shape"@en ;

    sh:property [
        sh:path cb:usesSnapshot ;
        sh:minCount 1 ;
        sh:class cb:MeasurementSnapshot ;
        sh:message "A BreakerDecision must use at least one MeasurementSnapshot." ;
    ] ;
    sh:property [
        sh:path cb:usesOntologyVersion ;
        sh:minCount 1 ;
        sh:class cb:FederatedGraphNode ;
        sh:message "A BreakerDecision must reference the ontology version used." ;
    ] ;
    sh:property [
        sh:path cb:generatesVerdict ;
        sh:minCount 1 ; sh:maxCount 1 ;
        sh:class cb:BreakerVerdict ;
        sh:message "A BreakerDecision must generate exactly one BreakerVerdict." ;
    ] .

# End of CBTO SHACL shapes v1.0.0
```

### E.4 SPARQL Competency Query Catalog

Ten competency queries organized by domain. Each query is listed with its identifier, natural-language question, and full SPARQL text.

**CQ-T01: How many system models exist?**

```sparql
PREFIX cb: <http://circuitbreaker.ontology/trust#>
SELECT (COUNT(?model) AS ?modelCount)
WHERE {
    ?model a cb:SystemModel .
}
```

**CQ-T02: Which morphism mappings connect agent to reference models?**

```sparql
PREFIX cb: <http://circuitbreaker.ontology/trust#>
SELECT ?mapping ?agent ?reference
WHERE {
    ?mapping a cb:MorphismMapping ;
             cb:mapsFrom ?agent ;
             cb:mapsTo ?reference .
}
```

**CQ-T03: What is the state-space cardinality per reference model?**

```sparql
PREFIX cb: <http://circuitbreaker.ontology/trust#>
SELECT ?model (COUNT(?state) AS ?stateCount)
WHERE {
    ?model a cb:ReferenceSystemModel ;
           cb:hasStateSet ?ss .
    ?state cb:memberOfSet ?ss .
}
GROUP BY ?model
```

**CQ-T04: What are the current sigma and D values per mapping?**

```sparql
PREFIX cb: <http://circuitbreaker.ontology/trust#>
SELECT ?mapping ?sigma ?distance
WHERE {
    ?mapping a cb:MorphismMapping ;
             cb:hasStructuralQuality ?sq ;
             cb:hasBehavioralQuality ?bq .
    ?sq cb:sigmaValue ?sigma .
    ?bq cb:outputDistance ?distance .
}
```

**CQ-A01: How many federated graph nodes exist?**

```sparql
PREFIX cb: <http://circuitbreaker.ontology/trust#>
SELECT (COUNT(?node) AS ?nodeCount)
WHERE {
    ?node a cb:FederatedGraphNode .
}
```

**CQ-A02: Which control charts are calibrated against which graph versions?**

```sparql
PREFIX cb: <http://circuitbreaker.ontology/trust#>
SELECT ?chart ?metric ?node ?version
WHERE {
    ?chart a cb:ControlChart ;
           cb:chartMetric ?metric ;
           cb:calibratedAgainstVersion ?node .
    ?node cb:graphVersion ?version .
}
```

**CQ-A03: Are all graph nodes reachable (have endpoints)?**

```sparql
PREFIX cb: <http://circuitbreaker.ontology/trust#>
SELECT ?node ?version
WHERE {
    ?node a cb:FederatedGraphNode ;
          cb:graphVersion ?version .
    FILTER NOT EXISTS { ?node cb:graphEndpoint ?ep . }
}
```

**CQ-P01: How many breaker decisions in the last 24 hours?**

```sparql
PREFIX cb:   <http://circuitbreaker.ontology/trust#>
PREFIX prov: <http://www.w3.org/ns/prov#>
PREFIX xsd:  <http://www.w3.org/2001/XMLSchema#>
SELECT (COUNT(?decision) AS ?decisionCount)
WHERE {
    ?decision a cb:BreakerDecision ;
              prov:startedAtTime ?t .
    BIND(NOW() AS ?now)
    FILTER(?t >= ?now - "PT24H"^^xsd:duration)
}
```

**CQ-P02: Which decisions produced Halt or Lockdown verdicts?**

```sparql
PREFIX cb: <http://circuitbreaker.ontology/trust#>
PREFIX prov: <http://www.w3.org/ns/prov#>
SELECT ?decision ?timestamp ?state
WHERE {
    ?decision a cb:BreakerDecision ;
              prov:startedAtTime ?timestamp ;
              cb:generatesVerdict ?verdict .
    ?verdict cb:hasBreakerState ?state .
    FILTER(?state IN (cb:Halt, cb:Lockdown))
}
ORDER BY DESC(?timestamp)
```

**CQ-T09: Which classes have zero instances (dark classes)?**

```sparql
PREFIX cb:   <http://circuitbreaker.ontology/trust#>
PREFIX owl:  <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT ?class (COUNT(?inst) AS ?directCount)
WHERE {
    ?class a owl:Class .
    FILTER(STRSTARTS(STR(?class), STR(cb:)))
    FILTER NOT EXISTS {
        ?class owl:equivalentClass ?eq .
        ?eq owl:oneOf ?list .
    }
    OPTIONAL { ?inst a ?class . }
}
GROUP BY ?class
HAVING (COUNT(?inst) = 0)
ORDER BY ?class
```

**CQ-T10: What is the ABox completeness ratio?**

```sparql
PREFIX cb:   <http://circuitbreaker.ontology/trust#>
PREFIX owl:  <http://www.w3.org/2002/07/owl#>
SELECT
    (COUNT(DISTINCT ?populated) AS ?populatedCount)
    (COUNT(DISTINCT ?total) AS ?totalCount)
    (COUNT(DISTINCT ?populated) * 100 / COUNT(DISTINCT ?total) AS ?completenessPercent)
WHERE {
    {
        SELECT DISTINCT ?total WHERE {
            ?total a owl:Class .
            FILTER(STRSTARTS(STR(?total), STR(cb:)))
            FILTER NOT EXISTS {
                ?total owl:equivalentClass ?eq .
                ?eq owl:oneOf ?list .
            }
        }
    }
    OPTIONAL {
        SELECT DISTINCT ?populated WHERE {
            ?populated a owl:Class .
            FILTER(STRSTARTS(STR(?populated), STR(cb:)))
            FILTER NOT EXISTS {
                ?populated owl:equivalentClass ?eq .
                ?eq owl:oneOf ?list .
            }
            ?inst a ?populated .
        }
    }
}
```

---

*End of AI Circuit Breaker Design Specification v4.0*
