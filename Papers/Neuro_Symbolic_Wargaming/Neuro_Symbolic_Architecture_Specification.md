# Neuro-Symbolic Architecture Specification

**Document Version:** 1.0
**Date:** 2026-01-22
**Author:** University of Arizona PostDoc Research
**Status:** TAP-Ready Draft
**Purpose:** Define the technical architecture for neuro-symbolic AI integration in wargaming for mission engineering and acquisition decision support

---

## Executive Summary

This specification defines a **neuro-symbolic AI architecture** for integrating wargaming with mission engineering (ME) and acquisition decision-making. The architecture combines:

- **Neural Components**: Pattern learning, scenario generation, prediction, optimization
- **Symbolic Components**: Knowledge representation, constraint enforcement, explanation, traceability
- **Integration Layer**: Bidirectional neural-symbolic coupling with grounding and abstraction

The architecture supports the **42 ME gap questions** mapped in the ME-Wargame Mapping Matrix and aligns with the **10 NATO STO research topics** for AI-augmented wargaming.

---

## Table of Contents

1. [Architecture Overview](#1-architecture-overview)
2. [Formal Foundations](#2-formal-foundations)
3. [Knowledge Graph Schema](#3-knowledge-graph-schema)
4. [Neural Component Specification](#4-neural-component-specification)
5. [Symbolic Component Specification](#5-symbolic-component-specification)
6. [Neuro-Symbolic Integration Layer](#6-neuro-symbolic-integration-layer)
7. [Wargaming Lifecycle Integration](#7-wargaming-lifecycle-integration)
8. [Data Flow Architecture](#8-data-flow-architecture)
9. [API Specifications](#9-api-specifications)
10. [Security and Governance](#10-security-and-governance)
11. [Implementation Roadmap](#11-implementation-roadmap)
12. [Validation Framework](#12-validation-framework)

---

## 1. Architecture Overview

### 1.1 Design Principles

| Principle | Description | Rationale |
|-----------|-------------|-----------|
| **Explainability First** | All AI outputs must be traceable to inputs and reasoning | Acquisition decisions require defensible justification |
| **Human-in-the-Loop** | Humans retain decision authority; AI augments, not replaces | NATO responsible AI principles |
| **Modular Composition** | Components can be deployed independently or integrated | Incremental adoption pathway |
| **Knowledge Persistence** | Insights accumulate across wargames | Cross-game synthesis requirement |
| **Doctrinal Grounding** | Neural outputs constrained by symbolic rules | Ensures operational relevance |
| **Multinational Compatibility** | Supports classification boundaries and national caveats | NATO coalition requirement |

### 1.2 High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           USER INTERFACE LAYER                               │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐        │
│  │ Wargame     │  │ Analysis    │  │ Decision    │  │ Audit &     │        │
│  │ Facilitation│  │ Dashboard   │  │ Support     │  │ Traceability│        │
│  └─────────────┘  └─────────────┘  └─────────────┘  └─────────────┘        │
└─────────────────────────────────────────────────────────────────────────────┘
                                      │
                                      ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                        NEURO-SYMBOLIC INTEGRATION LAYER                      │
│  ┌───────────────────────────────────────────────────────────────────────┐  │
│  │                    Bidirectional Coupling Engine                       │  │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  │  │
│  │  │ Neural      │  │ Symbolic    │  │ Confidence  │  │ Explanation │  │  │
│  │  │ Grounding   │  │ Abstraction │  │ Calibration │  │ Generator   │  │  │
│  │  └─────────────┘  └─────────────┘  └─────────────┘  └─────────────┘  │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────────────┘
          │                                                    │
          ▼                                                    ▼
┌─────────────────────────────┐          ┌─────────────────────────────────────┐
│     NEURAL COMPONENT        │          │       SYMBOLIC COMPONENT             │
│  ┌───────────────────────┐  │          │  ┌─────────────────────────────────┐│
│  │ Scenario Generator    │  │          │  │ Knowledge Graph                 ││
│  │ - Transformer models  │  │          │  │ - Ontology (OWL/SHACL)         ││
│  │ - Adversary modeling  │  │          │  │ - Rules (SWRL/SPARQL)          ││
│  │ - Edge case discovery │  │          │  │ - Constraints                   ││
│  └───────────────────────┘  │          │  └─────────────────────────────────┘│
│  ┌───────────────────────┐  │          │  ┌─────────────────────────────────┐│
│  │ Pattern Learner       │  │          │  │ Reasoning Engine                ││
│  │ - Historical analysis │  │◄────────►│  │ - Deductive inference          ││
│  │ - Trend detection     │  │          │  │ - Constraint satisfaction       ││
│  │ - Anomaly detection   │  │          │  │ - Consistency checking          ││
│  └───────────────────────┘  │          │  └─────────────────────────────────┘│
│  ┌───────────────────────┐  │          │  ┌─────────────────────────────────┐│
│  │ Prediction Engine     │  │          │  │ Traceability Manager            ││
│  │ - Outcome forecasting │  │          │  │ - Provenance tracking           ││
│  │ - Threshold detection │  │          │  │ - Decision chains               ││
│  │ - Risk assessment     │  │          │  │ - Audit logging                 ││
│  └───────────────────────┘  │          │  └─────────────────────────────────┘│
│  ┌───────────────────────┐  │          │  ┌─────────────────────────────────┐│
│  │ Optimization Engine   │  │          │  │ Explanation Engine              ││
│  │ - Resource allocation │  │          │  │ - Natural language generation   ││
│  │ - Sequencing          │  │          │  │ - Counterfactual reasoning      ││
│  │ - Multi-objective     │  │          │  │ - Confidence communication      ││
│  └───────────────────────┘  │          │  └─────────────────────────────────┘│
└─────────────────────────────┘          └─────────────────────────────────────┘
                                      │
                                      ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                           DATA & PERSISTENCE LAYER                           │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐        │
│  │ Wargame     │  │ ME Gap      │  │ Doctrine &  │  │ Historical  │        │
│  │ Artifacts   │  │ Repository  │  │ Policy KB   │  │ Wargame DB  │        │
│  └─────────────┘  └─────────────┘  └─────────────┘  └─────────────┘        │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 1.3 Technology Stack Overview

| Layer | Technologies | Rationale |
|-------|--------------|-----------|
| **Neural** | PyTorch, Transformers, LangChain | Industry standard, extensible |
| **Symbolic** | Apache Jena, OWL 2, SHACL, SPARQL | W3C standards, interoperable |
| **Integration** | Custom middleware, gRPC | High performance, type safety |
| **Persistence** | Neo4j (graph), PostgreSQL (relational), Vector DB | Hybrid storage needs |
| **Interface** | React, D3.js, FastAPI | Modern, interactive visualization |

---

## 2. Formal Foundations

This section establishes the formal basis for the neuro-symbolic architecture, ensuring NATO-grade guarantees for acquisition decision support. The symbolic layer serves as the **foundational constraint system** that all neural outputs must satisfy.

### 2.1 Formal Semantics for Key Predicates

The following predicates have formally defined semantics:

**Predicate 2.1.1: hasCompleteProvenance(i)**
```
hasCompleteProvenance(i) ≡
    ∃T. TraceabilityChain(T) ∧ T.insight = i ∧
    ∃o. Outcome(o) ∧ ledTo(o, i) ∧ T.outcome = o ∧
    ∃m. Move(m) ∧ resultsIn(m, o) ∧ T.move = m ∧
    ∃w. Wargame(w) ∧ hasMove(w, m) ∧ T.wargame = w ∧
    ∃g. GapQuestion(g) ∧ addresses(w, g) ∧ T.gap = g
```

**Predicate 2.1.2: analyticallyCredible(i)**
```
analyticallyCredible(i) ≡
    Insight(i) ∧
    hasConfidence(i, c) ∧ c ≥ θ_credible ∧
    hasCompleteProvenance(i) ∧
    (∃v. SMEValidated(i, v) ∨ formallyVerified(i)) ∧
    hasComprehensibleExplanation(i) ∧
    ¬hasContradiction(i)
```

**Predicate 2.1.3: constraintSatisfied(output)**
```
constraintSatisfied(output) ≡
    ∀c ∈ Constraints. c.applies(output) → c.satisfied(output)
```

### 2.2 Decidability Guarantees for Reasoning

The system guarantees decidable reasoning through careful ontology profile selection:

| Reasoning Task | Profile | Decidability | Complexity |
|----------------|---------|--------------|------------|
| Class consistency | OWL 2 DL | Decidable | 2-NEXPTIME |
| Instance checking | OWL 2 DL | Decidable | 2-NEXPTIME |
| Conjunctive queries | OWL 2 RL | Decidable | PTIME |
| SHACL validation | SHACL Core | Decidable | PTIME |
| Rule inference | SWRL-DL | Decidable | 2-NEXPTIME |

**Theorem 2.2.1 (Reasoning Termination):**
*All reasoning operations in the production system terminate in bounded time.*

*Proof:* The production system uses OWL 2 RL for runtime reasoning, which is PTIME-decidable. Combined with bounded ABox size (finite wargame artifacts), termination is guaranteed. □

### 2.3 Soundness and Completeness Properties

**Soundness (Theorem 2.3.1):**
*If the reasoning engine derives a conclusion, that conclusion is logically entailed by the knowledge base.*

**Completeness (Theorem 2.3.2 - Qualified):**
*For the OWL 2 RL subset, if a conclusion is logically entailed and expressible in the profile, the reasoning engine derives it.*

Note: Full OWL 2 DL completeness is achieved in offline analysis; runtime uses the sound RL subset.

### 2.4 The "Neural Proposes, Symbolic Disposes" Pattern

This fundamental architectural pattern ensures neural components cannot violate system guarantees:

```
┌─────────────────────────────────────────────────────────────────────────┐
│              NEURAL PROPOSES, SYMBOLIC DISPOSES PATTERN                  │
│                                                                          │
│  INVARIANT: No neural output reaches users without symbolic validation   │
│                                                                          │
│  ┌───────────────────┐                    ┌─────────────────────────┐  │
│  │   NEURAL LAYER    │    Proposals       │   SYMBOLIC LAYER        │  │
│  │                   │───────────────────►│                         │  │
│  │  • Unconstrained  │                    │  • Validates all rules  │  │
│  │    generation     │                    │  • Checks consistency   │  │
│  │  • Pattern recog  │                    │  • Enforces security    │  │
│  │  • Predictions    │    Accept/Reject   │  • Maintains provenance │  │
│  │  • Confidence     │◄───────────────────│  • Generates explanations│ │
│  │    estimates      │                    │                         │  │
│  └───────────────────┘                    └─────────────────────────┘  │
│                                                                          │
│  Contract:                                                               │
│    PRE:  Neural output has confidence ∈ [0,1], sources non-empty        │
│    POST: If accepted, output satisfies all constraints                  │
│    INV:  Classification never decreases through system                  │
└─────────────────────────────────────────────────────────────────────────┘
```

**Formal Interface Contract:**
```python
@dataclass
class NeuralOutput:
    content: Any
    confidence: float  # Invariant: 0 ≤ confidence ≤ 1
    sources: List[EntityRef]  # Invariant: len(sources) > 0
    timestamp: datetime

@dataclass
class ValidationResult:
    is_valid: bool
    violations: List[Constraint]
    repairs: List[Suggestion]
    validated_output: Optional[ValidatedOutput]

def validate(neural_output: NeuralOutput) -> ValidationResult:
    """
    Symbolic validation gate.

    Guarantees:
    - If is_valid=True, all constraints satisfied
    - If is_valid=False, violations list explains why
    - Classification is preserved or elevated
    - Provenance chain is extended
    """
```

### 2.5 Guarantee Preservation Through Integration

**Theorem 2.5.1 (Guarantee Preservation):**
*System guarantees G hold for all outputs that pass symbolic validation.*

*Proof:*
1. Let G = {g₁, ..., gₙ} be the set of system guarantees
2. Each gᵢ is encoded as constraint cᵢ in SHACL/OWL
3. Symbolic validation checks all constraints
4. Validation accepts iff ∀i. cᵢ(output) = true
5. Therefore, acceptance ⟹ all guarantees hold □

### 2.6 References to Supporting Documents

For detailed formal specifications, see:
- **Ontology Engineering Strategy**: Methodology, axiomatization, decidability analysis
- **Formal Verification Framework**: Model checking, theorem proving, safety case

---

## 3. Knowledge Graph Schema

### 2.1 Core Ontology Structure

The knowledge graph uses OWL 2 ontology with SHACL constraints, organized into the following namespaces:

```
@prefix nsw: <http://nato.int/neuro-symbolic-wargaming#> .
@prefix me: <http://nato.int/mission-engineering#> .
@prefix wg: <http://nato.int/wargaming#> .
@prefix acq: <http://nato.int/acquisition#> .
@prefix dotmlpfi: <http://nato.int/dotmlpfi#> .
```

### 2.2 Entity Classes

#### 2.2.1 Mission Engineering Entities

```turtle
me:MissionEngineeringGap a owl:Class ;
    rdfs:label "Mission Engineering Gap" ;
    rdfs:comment "A capability gap identified through mission engineering analysis" .

me:GapArea a owl:Class ;
    rdfs:label "Gap Area" ;
    rdfs:comment "A thematic category of ME gaps (e.g., Coalition, Comms-Denied)" .

me:GapQuestion a owl:Class ;
    rdfs:label "Gap Question" ;
    rdfs:comment "A specific research question within a gap area" ;
    rdfs:subClassOf me:MissionEngineeringGap .

me:MeasureOfEffectiveness a owl:Class ;
    rdfs:label "Measure of Effectiveness" ;
    rdfs:comment "Metric indicating degree of mission success" .

me:MeasureOfPerformance a owl:Class ;
    rdfs:label "Measure of Performance" ;
    rdfs:comment "Metric indicating system/process performance" .
```

#### 2.2.2 Wargaming Entities

```turtle
wg:Wargame a owl:Class ;
    rdfs:label "Wargame" ;
    rdfs:comment "A structured analytical game for exploring operational problems" .

wg:WargameType a owl:Class ;
    rdfs:label "Wargame Type" ;
    owl:oneOf (wg:Seminar wg:Tabletop wg:Matrix wg:Computational
               wg:LVC wg:RedTeam wg:Campaign wg:Crisis) .

wg:Scenario a owl:Class ;
    rdfs:label "Scenario" ;
    rdfs:comment "A narrative context for wargame execution" .

wg:Move a owl:Class ;
    rdfs:label "Move" ;
    rdfs:comment "A discrete decision or action within a wargame" .

wg:Outcome a owl:Class ;
    rdfs:label "Outcome" ;
    rdfs:comment "Result of a move or sequence of moves" .

wg:Insight a owl:Class ;
    rdfs:label "Insight" ;
    rdfs:comment "An analytical finding derived from wargame execution" .

wg:Participant a owl:Class ;
    rdfs:label "Participant" ;
    rdfs:comment "Human or AI actor in a wargame" .

wg:Adjudication a owl:Class ;
    rdfs:label "Adjudication" ;
    rdfs:comment "Resolution of move outcomes by rules or judgment" .
```

#### 2.2.3 Acquisition Entities

```turtle
acq:CapabilityGap a owl:Class ;
    rdfs:label "Capability Gap" ;
    rdfs:comment "A validated shortfall in operational capability" .

acq:Requirement a owl:Class ;
    rdfs:label "Requirement" ;
    rdfs:comment "A documented capability need for acquisition" .

acq:AcquisitionMilestone a owl:Class ;
    rdfs:label "Acquisition Milestone" ;
    owl:oneOf (acq:MSA acq:MSB acq:MSC acq:IOC acq:FOC) .

acq:Program a owl:Class ;
    rdfs:label "Program" ;
    rdfs:comment "An acquisition program developing a capability" .

acq:Alternative a owl:Class ;
    rdfs:label "Alternative" ;
    rdfs:comment "A candidate solution for addressing a capability gap" .
```

#### 2.2.4 DOTMLPFI Entities

```turtle
dotmlpfi:Domain a owl:Class ;
    rdfs:label "DOTMLPFI Domain" ;
    owl:oneOf (dotmlpfi:Doctrine dotmlpfi:Organization dotmlpfi:Training
               dotmlpfi:Materiel dotmlpfi:Leadership dotmlpfi:Personnel
               dotmlpfi:Facilities dotmlpfi:Interoperability) .

dotmlpfi:Implication a owl:Class ;
    rdfs:label "DOTMLPFI Implication" ;
    rdfs:comment "Impact of a gap or solution on a DOTMLPFI domain" .
```

### 2.3 Relationship Properties

```turtle
# Mission Engineering Relationships
me:belongsToGapArea a owl:ObjectProperty ;
    rdfs:domain me:GapQuestion ;
    rdfs:range me:GapArea .

me:hasMoE a owl:ObjectProperty ;
    rdfs:domain me:GapQuestion ;
    rdfs:range me:MeasureOfEffectiveness .

me:hasMoP a owl:ObjectProperty ;
    rdfs:domain me:GapQuestion ;
    rdfs:range me:MeasureOfPerformance .

# Wargaming Relationships
wg:addressesGap a owl:ObjectProperty ;
    rdfs:domain wg:Wargame ;
    rdfs:range me:GapQuestion .

wg:hasScenario a owl:ObjectProperty ;
    rdfs:domain wg:Wargame ;
    rdfs:range wg:Scenario .

wg:producesInsight a owl:ObjectProperty ;
    rdfs:domain wg:Wargame ;
    rdfs:range wg:Insight .

wg:hasMove a owl:ObjectProperty ;
    rdfs:domain wg:Wargame ;
    rdfs:range wg:Move .

wg:resultsIn a owl:ObjectProperty ;
    rdfs:domain wg:Move ;
    rdfs:range wg:Outcome .

wg:ledTo a owl:ObjectProperty ;
    rdfs:domain wg:Outcome ;
    rdfs:range wg:Insight ;
    rdfs:comment "Traceability from outcome to insight" .

# Cross-Domain Relationships
nsw:supportsRequirement a owl:ObjectProperty ;
    rdfs:domain wg:Insight ;
    rdfs:range acq:Requirement .

nsw:validatesGap a owl:ObjectProperty ;
    rdfs:domain wg:Wargame ;
    rdfs:range acq:CapabilityGap .

nsw:informsMilestone a owl:ObjectProperty ;
    rdfs:domain wg:Insight ;
    rdfs:range acq:AcquisitionMilestone .

nsw:hasDOTMLPFIImplication a owl:ObjectProperty ;
    rdfs:domain [owl:unionOf (me:GapQuestion wg:Insight acq:CapabilityGap)] ;
    rdfs:range dotmlpfi:Implication .
```

### 2.4 Provenance and Traceability Schema

```turtle
# Provenance Classes
nsw:ProvenanceRecord a owl:Class ;
    rdfs:label "Provenance Record" ;
    rdfs:comment "Audit trail for any entity in the knowledge graph" .

nsw:AIContribution a owl:Class ;
    rdfs:subClassOf nsw:ProvenanceRecord ;
    rdfs:comment "Record of AI-generated or AI-augmented content" .

nsw:HumanContribution a owl:Class ;
    rdfs:subClassOf nsw:ProvenanceRecord ;
    rdfs:comment "Record of human-generated content" .

# Provenance Properties
nsw:hasProvenance a owl:ObjectProperty ;
    rdfs:range nsw:ProvenanceRecord .

nsw:generatedBy a owl:ObjectProperty ;
    rdfs:domain nsw:AIContribution ;
    rdfs:range nsw:AIComponent .

nsw:confidence a owl:DatatypeProperty ;
    rdfs:domain nsw:AIContribution ;
    rdfs:range xsd:decimal ;
    rdfs:comment "Confidence score 0.0-1.0" .

nsw:timestamp a owl:DatatypeProperty ;
    rdfs:domain nsw:ProvenanceRecord ;
    rdfs:range xsd:dateTime .

nsw:validatedBy a owl:ObjectProperty ;
    rdfs:domain nsw:AIContribution ;
    rdfs:range wg:Participant ;
    rdfs:comment "Human who validated AI output" .
```

### 2.5 Knowledge Graph Instance Example

```turtle
# Gap Question Instance
me:COALITION-Q01 a me:GapQuestion ;
    rdfs:label "Data Classification Constraints" ;
    me:belongsToGapArea me:CoalitionOperations ;
    me:questionText "What data classification constraints and release policies limit mission-critical information sharing with coalition partners?" ;
    me:hasMoE me:JointMissionEffectiveness ;
    me:hasMoP me:DataReleaseLatency ;
    nsw:hasDOTMLPFIImplication dotmlpfi:InteroperabilityImplication ;
    nsw:pilotPriority "HIGH" .

# Wargame Instance
wg:CoalitionMatrixGame2026 a wg:Wargame ;
    wg:hasType wg:Matrix ;
    wg:addressesGap me:COALITION-Q01 ;
    wg:hasScenario wg:MultiClassificationScenario ;
    wg:duration "2 days" ;
    wg:participantCount 20 .

# Insight Instance with Provenance
wg:Insight2026-001 a wg:Insight ;
    rdfs:label "Classification friction delays averaged 4.2 hours" ;
    nsw:hasProvenance [
        a nsw:AIContribution ;
        nsw:generatedBy nsw:PatternLearner ;
        nsw:confidence 0.85 ;
        nsw:timestamp "2026-01-22T14:30:00Z" ;
        nsw:validatedBy wg:SME-Johnson
    ] ;
    nsw:supportsRequirement acq:C4ISR-REQ-042 .
```

---

## 4. Neural Component Specification

### 3.1 Component Overview

| Component | Purpose | Input | Output | ME Gap Coverage |
|-----------|---------|-------|--------|-----------------|
| **Scenario Generator** | Create diverse, realistic scenarios | Gap question, constraints | Scenario narratives | 25 questions |
| **Pattern Learner** | Identify patterns in historical data | Wargame transcripts, outcomes | Pattern descriptions | 42 questions |
| **Prediction Engine** | Forecast outcomes and thresholds | Current state, actions | Probability distributions | 30 questions |
| **Optimization Engine** | Find optimal configurations | Objectives, constraints | Ranked alternatives | 15 questions |
| **Adversary Modeler** | Simulate opponent behavior | Doctrine, capabilities | Adversary actions | 12 questions |

### 3.2 Scenario Generator

#### 3.2.1 Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    SCENARIO GENERATOR                            │
│  ┌─────────────────────────────────────────────────────────────┐│
│  │                   Input Processing                           ││
│  │  ┌───────────┐  ┌───────────┐  ┌───────────┐               ││
│  │  │ Gap       │  │ Constraint│  │ Historical│               ││
│  │  │ Question  │  │ Parser    │  │ Context   │               ││
│  │  └─────┬─────┘  └─────┬─────┘  └─────┬─────┘               ││
│  │        └──────────────┼──────────────┘                      ││
│  │                       ▼                                      ││
│  │  ┌─────────────────────────────────────────────────────────┐││
│  │  │              Transformer Encoder                         │││
│  │  │              (Fine-tuned LLM)                            │││
│  │  └─────────────────────────────────────────────────────────┘││
│  │                       │                                      ││
│  │        ┌──────────────┼──────────────┐                      ││
│  │        ▼              ▼              ▼                      ││
│  │  ┌───────────┐  ┌───────────┐  ┌───────────┐               ││
│  │  │ Narrative │  │ ORBAT     │  │ Event     │               ││
│  │  │ Generator │  │ Generator │  │ Injector  │               ││
│  │  └───────────┘  └───────────┘  └───────────┘               ││
│  └─────────────────────────────────────────────────────────────┘│
│                       │                                          │
│                       ▼                                          │
│  ┌─────────────────────────────────────────────────────────────┐│
│  │              Symbolic Constraint Filter                      ││
│  │  (Ensures doctrinal plausibility via Knowledge Graph)        ││
│  └─────────────────────────────────────────────────────────────┘│
│                       │                                          │
│                       ▼                                          │
│               [Validated Scenario]                               │
└─────────────────────────────────────────────────────────────────┘
```

#### 3.2.2 Model Specifications

| Aspect | Specification |
|--------|---------------|
| **Base Model** | LLaMA-3 70B or GPT-4 class (fine-tuned) |
| **Fine-tuning Data** | NATO exercise AARs, doctrine documents, historical wargames |
| **Context Window** | 32K tokens minimum |
| **Output Format** | Structured JSON with narrative, ORBAT, timeline, injects |
| **Constraint Interface** | SPARQL queries to Knowledge Graph for validation |
| **Diversity Mechanism** | Temperature sampling with adversarial filtering |

#### 3.2.3 Output Schema

```json
{
  "scenario_id": "string",
  "gap_question_ref": "me:COALITION-Q01",
  "narrative": {
    "title": "string",
    "background": "string",
    "situation": "string",
    "mission": "string",
    "execution_constraints": ["string"]
  },
  "orbat": {
    "blue_forces": [...],
    "red_forces": [...],
    "neutral_actors": [...]
  },
  "timeline": {
    "phases": [
      {
        "phase_id": "string",
        "duration": "string",
        "key_events": ["string"],
        "decision_points": ["string"]
      }
    ]
  },
  "injects": [
    {
      "inject_id": "string",
      "trigger_condition": "string",
      "content": "string",
      "expected_response_type": "string"
    }
  ],
  "provenance": {
    "generated_by": "nsw:ScenarioGenerator",
    "timestamp": "ISO8601",
    "confidence": 0.0-1.0,
    "constraints_satisfied": ["string"]
  }
}
```

### 3.3 Pattern Learner

#### 3.3.1 Capabilities

| Capability | Description | Techniques |
|------------|-------------|------------|
| **Historical Pattern Mining** | Extract recurring patterns from past wargames | Sequence mining, association rules |
| **Trend Detection** | Identify emerging patterns over time | Time series analysis, change point detection |
| **Anomaly Detection** | Flag unusual outcomes or behaviors | Isolation forests, autoencoders |
| **Cross-Game Synthesis** | Aggregate insights across multiple wargames | Meta-learning, transfer learning |
| **Degradation Curve Learning** | Model effectiveness vs. constraint relationships | Regression, Gaussian processes |

#### 3.3.2 Training Data Requirements

| Data Source | Volume | Format | Classification |
|-------------|--------|--------|----------------|
| NATO Exercise AARs | 500+ documents | Text, structured | Up to NATO SECRET |
| Historical Wargame Transcripts | 100+ games | JSON, video transcripts | UNCLASSIFIED-FOUO |
| Simulation Logs | 10M+ events | Structured logs | UNCLASSIFIED |
| Doctrine Documents | 200+ documents | PDF, text | UNCLASSIFIED |
| Subject Matter Expert Annotations | 5K+ annotations | Labeled data | UNCLASSIFIED |

#### 3.3.3 Output Types

```python
class PatternOutput:
    pattern_id: str
    pattern_type: Literal["recurring", "emerging", "anomalous"]
    description: str
    supporting_evidence: List[Evidence]
    confidence: float  # 0.0-1.0
    gap_questions_relevant: List[str]  # References to ME gap questions
    cross_game_frequency: int  # How many wargames exhibited this pattern

class Evidence:
    source_wargame: str
    source_move: str
    timestamp: datetime
    context: str
```

### 3.4 Prediction Engine

#### 3.4.1 Prediction Types

| Prediction Type | Input | Output | ME Gap Application |
|-----------------|-------|--------|-------------------|
| **Outcome Forecasting** | Current state, proposed action | Probability distribution over outcomes | All tactical questions |
| **Threshold Detection** | Degradation parameter | Critical threshold value | Comms-Denied Q01 |
| **Risk Assessment** | Configuration, threat | Risk score with uncertainty | Failure Modes, Temporal |
| **Timeline Prediction** | Development plan | Completion probability over time | Temporal Q01, Q04 |

#### 3.4.2 Model Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    PREDICTION ENGINE                             │
│                                                                  │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐      │
│  │ State        │    │ Action       │    │ Context      │      │
│  │ Encoder      │    │ Encoder      │    │ Encoder      │      │
│  │ (GNN)        │    │ (Transformer)│    │ (Retrieval)  │      │
│  └──────┬───────┘    └──────┬───────┘    └──────┬───────┘      │
│         │                   │                   │               │
│         └───────────────────┼───────────────────┘               │
│                             ▼                                    │
│  ┌─────────────────────────────────────────────────────────────┐│
│  │                 Fusion Layer (Cross-Attention)               ││
│  └─────────────────────────────────────────────────────────────┘│
│                             │                                    │
│         ┌───────────────────┼───────────────────┐               │
│         ▼                   ▼                   ▼               │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐      │
│  │ Outcome      │    │ Confidence   │    │ Uncertainty  │      │
│  │ Predictor    │    │ Estimator    │    │ Quantifier   │      │
│  └──────────────┘    └──────────────┘    └──────────────┘      │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

#### 3.4.3 Uncertainty Quantification

All predictions include uncertainty estimates using:

- **Epistemic Uncertainty**: Model uncertainty (ensemble disagreement)
- **Aleatoric Uncertainty**: Data uncertainty (inherent randomness)
- **Calibration**: Predictions calibrated against historical outcomes

```python
class Prediction:
    outcome_distribution: Dict[str, float]  # Outcome -> probability
    point_estimate: str  # Most likely outcome
    confidence_interval: Tuple[float, float]  # 95% CI
    epistemic_uncertainty: float
    aleatoric_uncertainty: float
    calibration_score: float  # 0.0-1.0, how well-calibrated historically
```

### 3.5 Optimization Engine

#### 3.5.1 Optimization Problem Types

| Problem Type | Objective | Constraints | ME Gap Application |
|--------------|-----------|-------------|-------------------|
| **Resource Allocation** | Maximize effectiveness | Budget, capacity | Sustainment, Training |
| **Sequencing** | Minimize risk, maximize cumulative value | Dependencies, timelines | Temporal Q02, Q04 |
| **Configuration** | Optimize system setup | Operational requirements | Coalition Q02, HMT Q01 |
| **Multi-Objective** | Pareto frontier | Multiple competing objectives | Stakeholder conflicts |

#### 3.5.2 Algorithms

| Algorithm | Use Case | Constraint Handling |
|-----------|----------|---------------------|
| **Genetic Algorithms** | Large discrete spaces | Penalty functions |
| **Bayesian Optimization** | Expensive evaluations | Acquisition functions |
| **Mixed-Integer Programming** | Linear constraints | Solver-native |
| **Multi-Objective Evolutionary** | Pareto problems | Dominance-based |
| **Reinforcement Learning** | Sequential decisions | Reward shaping |

---

## 5. Symbolic Component Specification

**The symbolic layer serves as the foundational constraint system for the entire architecture.** Neural components operate within boundaries defined by symbolic rules, and all outputs must pass symbolic validation before reaching users.

### 5.1 Component Overview

| Component | Purpose | Technology | ME Gap Coverage | Formal Guarantee |
|-----------|---------|------------|-----------------|------------------|
| **Knowledge Graph** | Store and query domain knowledge | Neo4j, Apache Jena | All 42 questions | Ontology consistency |
| **Reasoning Engine** | Perform logical inference | Pellet, HermiT | 35 questions | Sound & decidable |
| **Constraint Manager** | Enforce rules and policies | SHACL, OPA | 35 questions | Constraint satisfaction |
| **Traceability Manager** | Track provenance and decisions | Custom + PROV-O | All 42 questions | Provenance completeness |
| **Explanation Engine** | Generate human-readable explanations | Template + NLG | 30 questions | Explanation fidelity |

### 5.1.1 Formal Constraint Satisfaction (Beyond SHACL Checking)

The Constraint Manager provides **formal guarantees** beyond simple SHACL shape validation:

**Three-Level Constraint Architecture:**
```
Level 1: SHACL Shapes (Structural)
├── Required fields present
├── Data types correct
├── Cardinality constraints
└── Value restrictions

Level 2: OWL Axioms (Semantic)
├── Class membership entailments
├── Property restrictions
├── Disjointness enforcement
└── Consistency verification

Level 3: Domain Rules (Business Logic)
├── Classification propagation
├── ROE compliance
├── Temporal ordering
└── Provenance chain validity
```

**Decidability Guarantee:** All constraints are expressible in decidable fragments. Constraint checking terminates in polynomial time for SHACL Core and OWL 2 RL.

### 5.1.2 Reasoning Engine Formal Properties

| Property | Guarantee | Verification Method |
|----------|-----------|---------------------|
| **Soundness** | Derived conclusions are logically entailed | Reasoner certification |
| **Completeness** | All entailed conclusions derivable (for RL) | Profile compliance |
| **Termination** | Reasoning always completes | OWL 2 RL decidability |
| **Consistency Preservation** | Consistent input → consistent output | Formal proof |

### 5.1.3 Provenance Chain Formal Model

**Definition:** A provenance chain P for insight i is valid iff:
```
valid(P) ≡ P.insight = i ∧ ledTo(P.outcome, i) ∧ resultsIn(P.move, P.outcome) ∧
           hasMove(P.wargame, P.move) ∧ addresses(P.wargame, P.gap)
```

See **Formal_Verification_Framework.md** Section 8 for detailed proofs.

### 5.2 Reasoning Engine

#### 5.2.1 Reasoning Types

| Reasoning Type | Description | Implementation |
|----------------|-------------|----------------|
| **Deductive** | Derive conclusions from rules | OWL 2 RL + SWRL rules |
| **Constraint Satisfaction** | Find valid configurations | SHACL + custom solver |
| **Consistency Checking** | Detect contradictions | OWL 2 DL reasoner |
| **Temporal Reasoning** | Handle time-based logic | Allen's interval algebra |
| **Defeasible Reasoning** | Handle exceptions and defaults | Prioritized rules |

#### 5.2.2 Rule Examples

```swrl
# Rule: If a move violates ROE, flag for human review
wg:Move(?m) ∧ wg:violatesConstraint(?m, ?c) ∧
nsw:constraintType(?c, "ROE") → nsw:requiresHumanReview(?m, true)

# Rule: Propagate classification to derived insights
wg:Outcome(?o) ∧ wg:ledTo(?o, ?i) ∧
nsw:hasClassification(?o, ?class) → nsw:hasClassification(?i, ?class)

# Rule: Coalition interoperability requirement
wg:Wargame(?w) ∧ wg:hasType(?w, wg:Multinational) ∧
wg:hasParticipant(?w, ?p1) ∧ wg:hasParticipant(?w, ?p2) ∧
wg:nationality(?p1, ?n1) ∧ wg:nationality(?p2, ?n2) ∧
differentFrom(?n1, ?n2) → nsw:requiresInteroperabilityCheck(?w, true)
```

#### 5.2.3 SHACL Constraint Examples

```turtle
# Constraint: Every insight must have provenance
nsw:InsightProvenanceShape a sh:NodeShape ;
    sh:targetClass wg:Insight ;
    sh:property [
        sh:path nsw:hasProvenance ;
        sh:minCount 1 ;
        sh:message "Every insight must have provenance record"
    ] .

# Constraint: AI-generated content must have confidence score
nsw:AIConfidenceShape a sh:NodeShape ;
    sh:targetClass nsw:AIContribution ;
    sh:property [
        sh:path nsw:confidence ;
        sh:minCount 1 ;
        sh:datatype xsd:decimal ;
        sh:minInclusive 0.0 ;
        sh:maxInclusive 1.0 ;
        sh:message "AI contributions must have confidence score 0.0-1.0"
    ] .

# Constraint: Wargame addressing ethics gap must have legal SME
nsw:EthicsWargameShape a sh:NodeShape ;
    sh:targetClass wg:Wargame ;
    sh:sparql [
        sh:select """
            SELECT $this
            WHERE {
                $this wg:addressesGap ?gap .
                ?gap me:belongsToGapArea me:EthicsLegal .
                FILTER NOT EXISTS {
                    $this wg:hasParticipant ?p .
                    ?p wg:role "Legal SME" .
                }
            }
        """ ;
        sh:message "Wargames addressing ethics gaps must include Legal SME"
    ] .
```

### 5.3 Traceability Manager

#### 5.3.1 Traceability Chain Schema

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│ Gap Question│───►│ Wargame     │───►│ Move/       │───►│ Outcome     │
│             │    │ Design      │    │ Decision    │    │             │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
                                                                │
                                                                ▼
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│ Acquisition │◄───│ Requirement │◄───│ Capability  │◄───│ Insight     │
│ Decision    │    │             │    │ Gap         │    │             │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
```

#### 5.3.2 Provenance Query Examples

```sparql
# Query: Trace an insight back to its source gap question
SELECT ?gapQuestion ?wargame ?move ?outcome ?insight
WHERE {
    ?insight a wg:Insight .
    ?outcome wg:ledTo ?insight .
    ?move wg:resultsIn ?outcome .
    ?wargame wg:hasMove ?move .
    ?wargame wg:addressesGap ?gapQuestion .
    FILTER (?insight = <specific_insight_uri>)
}

# Query: Find all insights supporting a requirement
SELECT ?insight ?confidence ?validator
WHERE {
    ?insight nsw:supportsRequirement ?req .
    ?insight nsw:hasProvenance ?prov .
    ?prov nsw:confidence ?confidence .
    OPTIONAL { ?prov nsw:validatedBy ?validator }
    FILTER (?req = acq:C4ISR-REQ-042)
}
ORDER BY DESC(?confidence)

# Query: Audit trail for AI-generated content
SELECT ?entity ?aiComponent ?timestamp ?confidence ?humanValidator
WHERE {
    ?entity nsw:hasProvenance ?prov .
    ?prov a nsw:AIContribution .
    ?prov nsw:generatedBy ?aiComponent .
    ?prov nsw:timestamp ?timestamp .
    ?prov nsw:confidence ?confidence .
    OPTIONAL { ?prov nsw:validatedBy ?humanValidator }
}
ORDER BY DESC(?timestamp)
```

### 5.4 Explanation Engine

#### 5.4.1 Explanation Types

| Explanation Type | Purpose | Technique |
|------------------|---------|-----------|
| **Factual** | What the AI concluded | Template-based NLG |
| **Counterfactual** | What would change the conclusion | Contrastive explanation |
| **Causal** | Why the AI reached this conclusion | Causal graph traversal |
| **Confidence** | How certain the AI is | Uncertainty communication |
| **Limitation** | What the AI doesn't know | Known unknown enumeration |

#### 5.4.2 Explanation Templates

```python
# Factual explanation template
FACTUAL_TEMPLATE = """
Based on analysis of {wargame_count} wargames addressing {gap_area},
the system identified that {pattern_description}.

This insight is supported by:
{evidence_list}

Confidence: {confidence}% ({confidence_interpretation})
"""

# Counterfactual explanation template
COUNTERFACTUAL_TEMPLATE = """
The current conclusion is: {conclusion}

This conclusion would change if:
- {counterfactual_1}
- {counterfactual_2}

The most influential factor is: {most_influential_factor}
"""

# Confidence communication template
CONFIDENCE_TEMPLATE = """
Confidence Level: {confidence_level} ({confidence_percentage}%)

This means:
- The model has seen {similar_cases} similar cases
- In {accuracy_rate}% of similar cases, predictions were accurate
- Key uncertainty sources: {uncertainty_sources}

Recommendation: {recommendation_based_on_confidence}
"""
```

#### 5.4.3 Explanation API

```python
class ExplanationRequest:
    entity_uri: str  # What to explain
    explanation_types: List[ExplanationType]  # Which explanation types
    audience: Literal["technical", "decision-maker", "operator"]
    detail_level: Literal["summary", "detailed", "comprehensive"]

class ExplanationResponse:
    entity_uri: str
    explanations: Dict[ExplanationType, str]
    supporting_evidence: List[Evidence]
    confidence_summary: ConfidenceSummary
    limitations: List[str]
    suggested_questions: List[str]  # Questions to probe further
```

---

## 6. Neuro-Symbolic Integration Layer

### 6.1 Integration Patterns

#### 6.1.1 Neural → Symbolic (Grounding)

Neural outputs are grounded in symbolic knowledge to ensure consistency and validity.

```
┌─────────────────────────────────────────────────────────────────┐
│                    NEURAL GROUNDING PIPELINE                     │
│                                                                  │
│  Neural Output ──► Entity Recognition ──► Knowledge Graph Lookup │
│                           │                        │             │
│                           ▼                        ▼             │
│                   Constraint Checking ◄── Symbolic Validation    │
│                           │                                      │
│                           ▼                                      │
│                   ┌───────────────┐                              │
│                   │ Valid?        │                              │
│                   │ Yes: Accept   │                              │
│                   │ No: Repair or │                              │
│                   │     Reject    │                              │
│                   └───────────────┘                              │
└─────────────────────────────────────────────────────────────────┘
```

**Grounding Operations:**

| Operation | Description | Example |
|-----------|-------------|---------|
| **Entity Linking** | Map neural mentions to KG entities | "F-35" → `nato:F35_Aircraft` |
| **Constraint Validation** | Check outputs against SHACL rules | Scenario must have valid ORBAT |
| **Consistency Check** | Ensure no contradictions with KG | New insight consistent with doctrine |
| **Classification Enforcement** | Apply security labels | Derived data inherits classification |

#### 6.1.2 Symbolic → Neural (Abstraction)

Symbolic knowledge is abstracted into neural representations for learning and generation.

```
┌─────────────────────────────────────────────────────────────────┐
│                  SYMBOLIC ABSTRACTION PIPELINE                   │
│                                                                  │
│  Knowledge Graph ──► Subgraph Extraction ──► Graph Embedding     │
│                              │                      │            │
│                              ▼                      ▼            │
│  Rule Encoding ──────► Constraint Vectors ──► Neural Context     │
│                                                     │            │
│                                                     ▼            │
│                                            Neural Component      │
│                                            (Constrained)         │
└─────────────────────────────────────────────────────────────────┘
```

**Abstraction Operations:**

| Operation | Description | Example |
|-----------|-------------|---------|
| **Graph Embedding** | Convert KG subgraphs to vectors | ME gap context → embedding |
| **Rule Vectorization** | Encode constraints as soft constraints | ROE rules → constraint vector |
| **Context Retrieval** | Provide relevant KG context to neural | Historical similar wargames |
| **Template Instantiation** | Fill neural templates with KG facts | Scenario template + ORBAT facts |

### 6.2 Bidirectional Coupling Engine

#### 6.2.1 Architecture

```python
class NeuralSymbolicCoupler:
    """
    Manages bidirectional flow between neural and symbolic components.
    """

    def __init__(self, knowledge_graph, neural_components):
        self.kg = knowledge_graph
        self.neural = neural_components
        self.constraint_checker = ConstraintChecker(knowledge_graph)
        self.entity_linker = EntityLinker(knowledge_graph)
        self.explanation_generator = ExplanationGenerator()

    def neural_to_symbolic(self, neural_output: NeuralOutput) -> SymbolicEntity:
        """Ground neural output in symbolic knowledge."""
        # Step 1: Entity linking
        entities = self.entity_linker.link(neural_output.text)

        # Step 2: Structure extraction
        structured = self.extract_structure(neural_output, entities)

        # Step 3: Constraint validation
        validation = self.constraint_checker.validate(structured)

        if validation.is_valid:
            # Step 4: Create KG entity with provenance
            return self.kg.create_entity(
                structured,
                provenance=AIProvenance(
                    source=neural_output.source_component,
                    confidence=neural_output.confidence,
                    timestamp=datetime.now()
                )
            )
        else:
            # Step 5: Attempt repair or reject
            return self.handle_validation_failure(neural_output, validation)

    def symbolic_to_neural(self, query: SymbolicQuery) -> NeuralContext:
        """Abstract symbolic knowledge for neural consumption."""
        # Step 1: Execute query
        results = self.kg.query(query)

        # Step 2: Extract relevant subgraph
        subgraph = self.kg.extract_subgraph(results)

        # Step 3: Generate embeddings
        embeddings = self.graph_embedder.embed(subgraph)

        # Step 4: Extract constraints
        constraints = self.constraint_checker.get_applicable_constraints(subgraph)
        constraint_vectors = self.constraint_encoder.encode(constraints)

        # Step 5: Generate text context
        text_context = self.context_generator.generate(subgraph)

        return NeuralContext(
            embeddings=embeddings,
            constraint_vectors=constraint_vectors,
            text_context=text_context,
            source_entities=[r.uri for r in results]
        )
```

### 6.3 Confidence Calibration

#### 6.3.1 Calibration Framework

```python
class ConfidenceCalibrator:
    """
    Ensures neural confidence scores are well-calibrated against
    actual accuracy, critical for acquisition decision support.
    """

    def __init__(self):
        self.calibration_data = CalibrationDataset()
        self.calibration_model = IsotonicRegression()

    def calibrate(self, raw_confidence: float,
                  prediction_type: str) -> CalibratedConfidence:
        """Convert raw neural confidence to calibrated probability."""

        # Apply type-specific calibration
        calibrated = self.calibration_model.predict(
            raw_confidence,
            prediction_type
        )

        # Compute uncertainty bounds
        uncertainty = self.compute_uncertainty(raw_confidence, prediction_type)

        # Generate confidence interpretation
        interpretation = self.interpret_confidence(calibrated, prediction_type)

        return CalibratedConfidence(
            raw=raw_confidence,
            calibrated=calibrated,
            lower_bound=calibrated - uncertainty,
            upper_bound=calibrated + uncertainty,
            interpretation=interpretation,
            recommendation=self.get_recommendation(calibrated)
        )

    def interpret_confidence(self, confidence: float,
                            prediction_type: str) -> str:
        """Generate human-readable confidence interpretation."""

        if confidence >= 0.9:
            return "Very High - Suitable for direct decision support"
        elif confidence >= 0.7:
            return "High - Suitable for informing decisions with SME review"
        elif confidence >= 0.5:
            return "Moderate - Requires significant human validation"
        elif confidence >= 0.3:
            return "Low - Use as hypothesis only, not decision basis"
        else:
            return "Very Low - Exploratory only, high uncertainty"
```

---

## 7. Wargaming Lifecycle Integration

### 6.1 Lifecycle Phases

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        WARGAMING LIFECYCLE                                   │
│                                                                              │
│  ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐ │
│  │ Problem  │──►│ Design   │──►│ Execution│──►│ Analysis │──►│Exploitation│
│  │ Framing  │   │          │   │          │   │          │   │          │ │
│  └──────────┘   └──────────┘   └──────────┘   └──────────┘   └──────────┘ │
│       │              │              │              │              │         │
│       ▼              ▼              ▼              ▼              ▼         │
│  ┌──────────────────────────────────────────────────────────────────────┐  │
│  │                    NEURO-SYMBOLIC AI SUPPORT                          │  │
│  │                                                                        │  │
│  │  Problem    Design       Execution    Analysis     Exploitation       │  │
│  │  Framing:   Support:     Support:     Support:     Support:           │  │
│  │  • Gap      • Scenario   • Real-time  • Pattern    • Insight          │  │
│  │    mapping    generation   adjudication  extraction   synthesis       │  │
│  │  • Question • ORBAT      • Move       • Outcome    • Requirement      │  │
│  │    refinement generation   validation   prediction   tracing          │  │
│  │  • MoE/MoP  • Inject     • Adversary  • Trend      • Gap              │  │
│  │    definition creation    modeling     detection    validation        │  │
│  └──────────────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 6.2 Phase-Specific AI Capabilities

#### 6.2.1 Problem Framing Phase

| Capability | Neural Contribution | Symbolic Contribution |
|------------|--------------------|-----------------------|
| Gap Question Selection | Recommend relevant questions based on sponsor objectives | Validate question-to-objective traceability |
| MoE/MoP Refinement | Suggest metrics based on historical wargames | Ensure metrics align with doctrine |
| Scope Definition | Predict resource requirements | Enforce feasibility constraints |

#### 6.2.2 Design Phase

| Capability | Neural Contribution | Symbolic Contribution |
|------------|--------------------|-----------------------|
| Scenario Generation | Create diverse, realistic scenarios | Validate doctrinal plausibility |
| ORBAT Generation | Generate force structures | Ensure capability realism |
| Inject Creation | Generate stress-testing events | Enforce scenario consistency |
| Schedule Optimization | Optimize wargame timeline | Validate participant availability |

#### 6.2.3 Execution Phase

| Capability | Neural Contribution | Symbolic Contribution |
|------------|--------------------|-----------------------|
| Real-time Adjudication | Predict move outcomes | Enforce rule compliance |
| Adversary Modeling | Generate opponent responses | Ensure doctrinal consistency |
| Facilitator Assistance | Suggest probing questions | Track discussion coverage |
| Move Validation | Detect implausible moves | Enforce constraint compliance |

#### 6.2.4 Analysis Phase

| Capability | Neural Contribution | Symbolic Contribution |
|------------|--------------------|-----------------------|
| Pattern Extraction | Identify recurring patterns | Validate pattern significance |
| Outcome Prediction | Predict alternative outcomes | Explain causal chains |
| Trend Detection | Identify emerging themes | Categorize findings |
| Insight Generation | Synthesize observations | Ensure insight traceability |

#### 6.2.5 Exploitation Phase

| Capability | Neural Contribution | Symbolic Contribution |
|------------|--------------------|-----------------------|
| Insight Synthesis | Aggregate across wargames | Maintain provenance chains |
| Requirement Tracing | Link insights to requirements | Validate traceability completeness |
| Gap Validation | Assess gap hypothesis confidence | Verify evidence sufficiency |
| Report Generation | Draft narrative sections | Ensure doctrinal accuracy |

---

## 8. Data Flow Architecture

### 7.1 Data Flow Diagram

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           DATA FLOW ARCHITECTURE                             │
│                                                                              │
│  ┌─────────────────────┐                                                    │
│  │   INPUT SOURCES     │                                                    │
│  │  • ME Gap Questions │                                                    │
│  │  • Doctrine Docs    │                                                    │
│  │  • Historical Games │──────────┐                                         │
│  │  • SME Input        │          │                                         │
│  │  • Live Wargame     │          │                                         │
│  └─────────────────────┘          │                                         │
│                                   ▼                                         │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                        INGESTION LAYER                               │   │
│  │  ┌───────────┐  ┌───────────┐  ┌───────────┐  ┌───────────┐        │   │
│  │  │ Document  │  │ Structured│  │ Real-time │  │ Human     │        │   │
│  │  │ Parser    │  │ Data ETL  │  │ Stream    │  │ Input     │        │   │
│  │  └───────────┘  └───────────┘  └───────────┘  └───────────┘        │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                   │                                         │
│                                   ▼                                         │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                      PROCESSING LAYER                                │   │
│  │                                                                       │   │
│  │  ┌─────────────────────────────────────────────────────────────┐    │   │
│  │  │              NEURO-SYMBOLIC ENGINE                           │    │   │
│  │  │                                                               │    │   │
│  │  │   Neural Components ◄────────────► Symbolic Components       │    │   │
│  │  │   • Scenario Gen    │  Coupling  │  • Knowledge Graph        │    │   │
│  │  │   • Pattern Learn   │   Engine   │  • Reasoning Engine       │    │   │
│  │  │   • Prediction      │            │  • Constraint Manager     │    │   │
│  │  │   • Optimization    │            │  • Traceability Manager   │    │   │
│  │  └─────────────────────────────────────────────────────────────┘    │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                   │                                         │
│                                   ▼                                         │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                       OUTPUT LAYER                                   │   │
│  │  ┌───────────┐  ┌───────────┐  ┌───────────┐  ┌───────────┐        │   │
│  │  │ Wargame   │  │ Analysis  │  │ Decision  │  │ Audit     │        │   │
│  │  │ Artifacts │  │ Reports   │  │ Support   │  │ Trails    │        │   │
│  │  └───────────┘  └───────────┘  └───────────┘  └───────────┘        │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                   │                                         │
│                                   ▼                                         │
│  ┌─────────────────────┐                                                    │
│  │   OUTPUT CONSUMERS  │                                                    │
│  │  • Wargame Team     │                                                    │
│  │  • ME Analysts      │                                                    │
│  │  • Acquisition PMs  │                                                    │
│  │  • Decision Makers  │                                                    │
│  │  • Auditors         │                                                    │
│  └─────────────────────┘                                                    │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 7.2 Data Classification Handling

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    CLASSIFICATION BOUNDARY MANAGEMENT                        │
│                                                                              │
│  ┌───────────────────┐    ┌───────────────────┐    ┌───────────────────┐   │
│  │   UNCLASSIFIED    │    │   NATO SECRET     │    │  COSMIC TOP SECRET│   │
│  │                   │    │                   │    │                   │   │
│  │  • Public doctrine│    │  • Exercise AARs  │    │  • Intel-informed │   │
│  │  • Published      │    │  • Classified     │    │    scenarios      │   │
│  │    research       │    │    capability data│    │  • Red force      │   │
│  │  • Generic        │    │  • Sensitive      │    │    order of battle│   │
│  │    scenarios      │    │    insights       │    │                   │   │
│  └─────────┬─────────┘    └─────────┬─────────┘    └─────────┬─────────┘   │
│            │                        │                        │              │
│            └────────────────────────┼────────────────────────┘              │
│                                     │                                        │
│                                     ▼                                        │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                  CLASSIFICATION ENFORCEMENT                          │   │
│  │  • Automatic labeling propagation                                    │   │
│  │  • Cross-domain solution integration                                 │   │
│  │  • Audit trail for all data movements                               │   │
│  │  • Sanitization for lower classification outputs                    │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 9. API Specifications

### 8.1 Core APIs

#### 8.1.1 Scenario Generation API

```yaml
openapi: 3.0.0
paths:
  /api/v1/scenarios/generate:
    post:
      summary: Generate a wargame scenario
      requestBody:
        content:
          application/json:
            schema:
              type: object
              required:
                - gap_question_id
              properties:
                gap_question_id:
                  type: string
                  description: ME gap question URI
                constraints:
                  type: array
                  items:
                    type: object
                    properties:
                      type:
                        type: string
                      value:
                        type: string
                diversity_params:
                  type: object
                  properties:
                    num_scenarios:
                      type: integer
                      default: 1
                    temperature:
                      type: number
                      default: 0.7
      responses:
        200:
          description: Generated scenario(s)
          content:
            application/json:
              schema:
                type: object
                properties:
                  scenarios:
                    type: array
                    items:
                      $ref: '#/components/schemas/Scenario'
                  provenance:
                    $ref: '#/components/schemas/Provenance'
```

#### 8.1.2 Pattern Query API

```yaml
paths:
  /api/v1/patterns/query:
    post:
      summary: Query for patterns in historical wargames
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                gap_area:
                  type: string
                  description: Filter by gap area
                pattern_type:
                  type: string
                  enum: [recurring, emerging, anomalous]
                min_confidence:
                  type: number
                  minimum: 0
                  maximum: 1
                  default: 0.5
                cross_game_minimum:
                  type: integer
                  description: Minimum wargames exhibiting pattern
                  default: 2
      responses:
        200:
          description: Matching patterns
          content:
            application/json:
              schema:
                type: object
                properties:
                  patterns:
                    type: array
                    items:
                      $ref: '#/components/schemas/Pattern'
                  total_count:
                    type: integer
```

#### 8.1.3 Traceability API

```yaml
paths:
  /api/v1/traceability/chain:
    get:
      summary: Get traceability chain for an entity
      parameters:
        - name: entity_uri
          in: query
          required: true
          schema:
            type: string
        - name: direction
          in: query
          schema:
            type: string
            enum: [upstream, downstream, both]
            default: both
        - name: max_depth
          in: query
          schema:
            type: integer
            default: 10
      responses:
        200:
          description: Traceability chain
          content:
            application/json:
              schema:
                type: object
                properties:
                  entity:
                    type: string
                  upstream_chain:
                    type: array
                    items:
                      $ref: '#/components/schemas/TraceabilityNode'
                  downstream_chain:
                    type: array
                    items:
                      $ref: '#/components/schemas/TraceabilityNode'
```

#### 8.1.4 Explanation API

```yaml
paths:
  /api/v1/explanations/generate:
    post:
      summary: Generate explanation for AI output
      requestBody:
        content:
          application/json:
            schema:
              type: object
              required:
                - entity_uri
              properties:
                entity_uri:
                  type: string
                explanation_types:
                  type: array
                  items:
                    type: string
                    enum: [factual, counterfactual, causal, confidence, limitation]
                  default: [factual, confidence]
                audience:
                  type: string
                  enum: [technical, decision-maker, operator]
                  default: decision-maker
                detail_level:
                  type: string
                  enum: [summary, detailed, comprehensive]
                  default: detailed
      responses:
        200:
          description: Generated explanations
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ExplanationResponse'
```

### 8.2 Integration Schemas

```yaml
components:
  schemas:
    Scenario:
      type: object
      properties:
        scenario_id:
          type: string
        gap_question_ref:
          type: string
        narrative:
          type: object
          properties:
            title:
              type: string
            background:
              type: string
            situation:
              type: string
            mission:
              type: string
        orbat:
          type: object
        timeline:
          type: object
        injects:
          type: array
        provenance:
          $ref: '#/components/schemas/Provenance'

    Pattern:
      type: object
      properties:
        pattern_id:
          type: string
        pattern_type:
          type: string
        description:
          type: string
        supporting_evidence:
          type: array
        confidence:
          type: number
        gap_questions_relevant:
          type: array
          items:
            type: string

    Provenance:
      type: object
      properties:
        generated_by:
          type: string
        timestamp:
          type: string
          format: date-time
        confidence:
          type: number
        validated_by:
          type: string
        constraints_satisfied:
          type: array
          items:
            type: string

    TraceabilityNode:
      type: object
      properties:
        entity_uri:
          type: string
        entity_type:
          type: string
        label:
          type: string
        relationship:
          type: string
        provenance:
          $ref: '#/components/schemas/Provenance'

    ExplanationResponse:
      type: object
      properties:
        entity_uri:
          type: string
        explanations:
          type: object
          additionalProperties:
            type: string
        supporting_evidence:
          type: array
        confidence_summary:
          type: object
        limitations:
          type: array
          items:
            type: string
```

---

## 10. Security and Governance

### 9.1 Security Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        SECURITY ARCHITECTURE                                 │
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                    AUTHENTICATION & AUTHORIZATION                    │   │
│  │  • NATO Federated Identity (NFIP)                                   │   │
│  │  • Role-Based Access Control (RBAC)                                 │   │
│  │  • Attribute-Based Access Control (ABAC)                            │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                    DATA PROTECTION                                   │   │
│  │  • Encryption at rest (AES-256)                                     │   │
│  │  • Encryption in transit (TLS 1.3)                                  │   │
│  │  • Classification labeling (NATO marking)                           │   │
│  │  • Data loss prevention                                              │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                    AI-SPECIFIC SECURITY                              │   │
│  │  • Model access control                                              │   │
│  │  • Input validation (prompt injection prevention)                   │   │
│  │  • Output filtering (sensitive data detection)                      │   │
│  │  • Adversarial robustness testing                                   │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                    AUDIT & COMPLIANCE                                │   │
│  │  • Comprehensive audit logging                                       │   │
│  │  • Tamper-evident audit trails                                      │   │
│  │  • Compliance reporting (NATO, GDPR, national)                      │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 9.2 Responsible AI Governance

#### 9.2.1 Governance Framework

| Governance Element | Description | Implementation |
|--------------------|-------------|----------------|
| **Human Oversight** | Humans retain final decision authority | Mandatory human validation for high-impact outputs |
| **Transparency** | AI reasoning must be explainable | Explanation engine with traceability |
| **Accountability** | Clear responsibility for AI outcomes | Provenance tracking, audit trails |
| **Bias Mitigation** | Detect and mitigate algorithmic bias | Bias testing suite, diverse training data |
| **Robustness** | Reliable performance under stress | Adversarial testing, uncertainty quantification |
| **Privacy** | Protect sensitive information | Data minimization, access controls |

#### 9.2.2 AI Risk Management

| Risk Category | Mitigation | Monitoring |
|---------------|------------|------------|
| **Hallucination** | Symbolic grounding, constraint checking | Hallucination detection metrics |
| **Bias** | Diverse training data, debiasing techniques | Fairness metrics across nations |
| **Over-confidence** | Calibration, uncertainty quantification | Calibration error tracking |
| **Adversarial Attack** | Input validation, robustness testing | Anomaly detection |
| **Misuse** | Access controls, audit trails | Usage pattern monitoring |
| **Drift** | Continuous monitoring, retraining triggers | Performance degradation alerts |

---

## 11. Implementation Roadmap

### 10.1 Phase 1: Foundation (Year 1)

| Milestone | Deliverable | TRL/KRL Target |
|-----------|-------------|----------------|
| **M1.1** | Knowledge graph schema finalized | KRL 3 |
| **M1.2** | Core ontology implemented (OWL/SHACL) | KRL 3 |
| **M1.3** | Basic scenario generator prototype | TRL 3 |
| **M1.4** | Traceability manager MVP | TRL 3 |
| **M1.5** | Integration layer architecture validated | TRL 3 |

### 10.2 Phase 2: Pilot Implementation (Year 2)

| Milestone | Deliverable | TRL/KRL Target |
|-----------|-------------|----------------|
| **M2.1** | Full scenario generator with constraints | TRL 4 |
| **M2.2** | Pattern learner trained on historical data | TRL 4 |
| **M2.3** | Explanation engine operational | TRL 4 |
| **M2.4** | Pilot wargame 1: Coalition Operations | TRL 4, KRL 4 |
| **M2.5** | Pilot wargame 2: Human-Machine Teaming | TRL 4, KRL 4 |

### 10.3 Phase 3: Validation & Transition (Year 3)

| Milestone | Deliverable | TRL/KRL Target |
|-----------|-------------|----------------|
| **M3.1** | Prediction engine with calibration | TRL 5 |
| **M3.2** | Cross-game synthesis demonstrated | KRL 5 |
| **M3.3** | Optimization engine operational | TRL 5 |
| **M3.4** | Full system integration validated | TRL 5 |
| **M3.5** | Transition roadmap for operationalization | TRL 6 ready |

### 10.4 Resource Requirements

| Resource | Phase 1 | Phase 2 | Phase 3 |
|----------|---------|---------|---------|
| **Personnel (FTE)** | 4 | 8 | 6 |
| **Compute (GPU-hours/month)** | 1,000 | 5,000 | 3,000 |
| **Data (classified access)** | Limited | Full | Full |
| **SME Engagement (days)** | 30 | 60 | 40 |

---

## 12. Validation Framework

### 11.1 Validation Approach

| Validation Type | Method | Success Criteria |
|-----------------|--------|------------------|
| **Analytical Credibility** | Expert panel comparison | AI insights rated ≥80% as credible by SMEs |
| **Traceability Completeness** | Audit trail verification | 100% of insights have complete provenance chains |
| **Explanation Quality** | User study | Decision-makers rate explanations ≥4/5 for clarity |
| **Confidence Calibration** | Historical accuracy analysis | Calibration error <10% |
| **Cross-Game Synthesis** | Cumulative learning demonstration | Demonstrable knowledge accumulation across 3+ wargames |
| **Constraint Compliance** | Automated testing | 100% of outputs satisfy defined constraints |

### 11.2 Metrics Dashboard

| Metric Category | Metrics |
|-----------------|---------|
| **Quality** | Insight credibility score, explanation clarity, constraint compliance rate |
| **Performance** | Scenario generation time, query response time, throughput |
| **Reliability** | System uptime, error rate, recovery time |
| **Usage** | Active users, wargames supported, insights generated |
| **Learning** | Pattern discovery rate, cross-game transfer, model improvement |

### 11.3 Continuous Improvement

```
┌─────────────────────────────────────────────────────────────────┐
│               CONTINUOUS IMPROVEMENT CYCLE                       │
│                                                                  │
│  ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐    │
│  │ Monitor  │──►│ Analyze  │──►│ Improve  │──►│ Deploy   │───┐│
│  │ Metrics  │   │ Gaps     │   │ Models   │   │ Updates  │   ││
│  └──────────┘   └──────────┘   └──────────┘   └──────────┘   ││
│       ▲                                                       │ │
│       └───────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
```

---

## Appendices

### Appendix A: Glossary

| Term | Definition |
|------|------------|
| **Neuro-Symbolic AI** | AI combining neural networks (learning, pattern recognition) with symbolic reasoning (logic, knowledge representation) |
| **Knowledge Graph** | Graph-structured knowledge base representing entities and relationships |
| **Grounding** | Process of linking neural outputs to symbolic knowledge |
| **Provenance** | Record of origin and transformations of data |
| **DOTMLPFI** | Doctrine, Organization, Training, Materiel, Leadership, Personnel, Facilities, Interoperability |
| **MoE** | Measure of Effectiveness - metric of mission success |
| **MoP** | Measure of Performance - metric of system/process performance |

### Appendix B: References

1. NATO STO Potential Topics for AI-Augmented Wargaming (2026)
2. ME-Wargame Mapping Matrix v1.0 (2026)
3. NATO STO Research Topics Expanded v1.0 (2026)
4. Integrated Readiness Level SE Lifecycle Matrix v1.0 (2026)
5. W3C OWL 2 Web Ontology Language
6. W3C SHACL Shapes Constraint Language
7. PROV-O: The PROV Ontology

### Appendix C: Related Documents

| Document | Purpose |
|----------|---------|
| ME-Wargame Mapping Matrix | Maps 42 ME gap questions to wargame designs |
| NATO STO Research Topics Expanded | 80 research questions across 10 topics |
| NATO STO Research Topics Critique | Gap analysis of original research topics |
| Integrated Readiness Level Matrix | TRL/MRL/IRL/HRL/ORL/KRL alignment |
| **Ontology_Engineering_Strategy.md** | Methodology, NATO alignment, formal axiomatization |
| **Formal_Verification_Framework.md** | Model checking, theorem proving, safety case structure |

---

*Document prepared for NATO STO TAP development.*
*Version 1.0 - 2026-01-22*
