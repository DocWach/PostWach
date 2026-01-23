# Ontology Engineering Strategy for Neuro-Symbolic Wargaming

**Document Version:** 1.0
**Date:** 2026-01-23
**Author:** University of Arizona PostDoc Research
**Status:** TAP Supporting Document
**Classification:** UNCLASSIFIED // FOR OFFICIAL USE ONLY
**Purpose:** Define the ontology development methodology, NATO standards alignment, and formal axiomatization approach for the neuro-symbolic wargaming system

---

## Executive Summary

This document specifies the **ontology engineering strategy** for the neuro-symbolic wargaming system. The ontology serves as the **foundational knowledge representation** that constrains neural components, enables formal reasoning, and ensures NATO interoperability. Unlike typical software ontologies focused on data exchange, this ontology must support **formal verification** and **acquisition-grade traceability** required for defense decision-making.

The strategy addresses:
- Rigorous methodology adapted from NeOn and METHONTOLOGY
- Formal axiomatization enabling logical guarantees
- Alignment with NATO standards (MIP DEM, JC3IEDM, APP-6, STANAG 4774/4778)
- Decidability analysis and OWL 2 profile selection
- Governance procedures for multinational evolution

---

## Table of Contents

1. [Introduction](#1-introduction)
2. [Methodology Selection](#2-methodology-selection)
3. [NATO Standards Alignment](#3-nato-standards-alignment)
4. [Formal Axiomatization](#4-formal-axiomatization)
5. [OWL Profile Selection](#5-owl-profile-selection)
6. [Competency Questions](#6-competency-questions)
7. [Knowledge Acquisition](#7-knowledge-acquisition)
8. [Ontology Governance](#8-ontology-governance)
9. [Verification and Validation](#9-verification-and-validation)
10. [Implementation Roadmap](#10-implementation-roadmap)

---

## 1. Introduction

### 1.1 Purpose and Scope

The wargaming ontology serves multiple critical functions:

| Function | Description | Stakeholder Need |
|----------|-------------|------------------|
| **Knowledge Representation** | Encode domain concepts, relationships, and constraints | Enable machine reasoning about wargaming |
| **Semantic Interoperability** | Provide shared vocabulary across systems and nations | Support multinational coalition wargaming |
| **Formal Constraint Specification** | Define rules that neural outputs must satisfy | Ensure doctrinal compliance |
| **Traceability Foundation** | Structure provenance chains from insight to evidence | Support acquisition decision justification |
| **Formal Verification Anchor** | Enable theorem proving and model checking | Provide NATO-grade guarantees |

### 1.2 Relationship to NATO Formal Requirements

NATO acquisition decisions require **defensible justification**. The ontology must support:

**Formal Verification Requirements:**
- Decidable reasoning (guaranteed termination)
- Sound inference (conclusions follow from premises)
- Complete coverage (all relevant domain concepts)
- Traceable provenance (every insight to evidence)

**Standards Compliance Requirements:**
- Alignment with NATO Architecture Framework (NAF)
- Compatibility with Multilateral Interoperability Programme (MIP)
- Support for STANAG classification handling
- Integration with NATO Defence Planning Process (NDPP)

### 1.3 Scope Boundaries

**In Scope:**
- Mission engineering concepts (gaps, questions, measures)
- Wargaming lifecycle (design, execution, analysis, exploitation)
- Acquisition concepts (requirements, programs, milestones)
- DOTMLPFI analysis dimensions
- Provenance and confidence metadata

**Out of Scope:**
- Detailed weapons system specifications
- Intelligence data models
- Personnel management systems
- Financial/budget systems

---

## 2. Methodology Selection

### 2.1 NeOn Methodology Adaptation

The NeOn methodology provides a framework for building ontology networks. We adapt it for defense wargaming:

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    NeON ADAPTED LIFECYCLE                                │
│                                                                          │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐│
│  │ Initiation   │─►│ Reuse        │─►│ Reengineering│─►│ Design       ││
│  │              │  │              │  │              │  │              ││
│  │ - Scope      │  │ - NATO stds  │  │ - Adapt MIP  │  │ - Modular    ││
│  │ - Competency │  │ - JC3IEDM    │  │ - Extend for │  │   architecture│
│  │   questions  │  │ - PROV-O     │  │   wargaming  │  │ - Axioms     ││
│  └──────────────┘  └──────────────┘  └──────────────┘  └──────────────┘│
│         │                                                      │        │
│         │              ┌──────────────┐                       │        │
│         │              │ Evaluation   │◄──────────────────────┘        │
│         │              │              │                                 │
│         │              │ - Competency │                                 │
│         │              │ - Consistency│                                 │
│         │              │ - Formal     │                                 │
│         │              │   validation │                                 │
│         │              └──────────────┘                                 │
│         │                     │                                         │
│         └─────────────────────┼─────────────────────────────────────────│
│                               ▼                                         │
│                    ┌──────────────┐                                     │
│                    │ Maintenance  │                                     │
│                    │              │                                     │
│                    │ - Versioning │                                     │
│                    │ - Governance │                                     │
│                    │ - Evolution  │                                     │
│                    └──────────────┘                                     │
└─────────────────────────────────────────────────────────────────────────┘
```

### 2.2 Competency Question Approach

The ontology is defined by the questions it must answer. We use competency questions (CQs) as:
- **Requirements specification**: What the ontology must represent
- **Validation criteria**: Tests the ontology must pass
- **Scope definition**: What the ontology need not address

### 2.3 Iterative Refinement Process

| Phase | Duration | Activities | Exit Criteria |
|-------|----------|------------|---------------|
| **Initial** | M1-M3 | Core concepts, SME elicitation | CQ coverage >50% |
| **Development** | M4-M9 | Full concept coverage, alignment | CQ coverage >90% |
| **Validation** | M10-M12 | Formal verification, expert review | All CQs pass |
| **Operational** | M13+ | Continuous refinement | Governance active |

### 2.4 Methodological Principles

1. **Reuse Before Create**: Leverage existing NATO/defense ontologies
2. **Formalize Completely**: Every concept has formal definition
3. **Modular Design**: Independent modules for extensibility
4. **Document Decisions**: Rationale for all design choices
5. **Verify Continuously**: Automated consistency checking

---

## 3. NATO Standards Alignment

### 3.1 MIP Data Exchange Model (DEM)

The Multilateral Interoperability Programme DEM provides foundational defense concepts:

**Reused Concepts:**
```
MIP DEM (v3.1)
├── Unit (Organization)
│   ├── Force
│   ├── Capability
│   └── Location
├── Operation
│   ├── Task
│   ├── Order
│   └── Report
├── Materiel
│   ├── Equipment
│   ├── Supply
│   └── Facility
└── Information
    ├── Intelligence
    ├── Situation
    └── Assessment
```

**Alignment Mappings:**
| MIP DEM Concept | Wargaming Ontology Concept | Relationship |
|-----------------|---------------------------|--------------|
| `mip:Unit` | `wg:Force` | equivalentClass |
| `mip:Task` | `wg:Move` | superClassOf |
| `mip:Assessment` | `wg:Insight` | superClassOf |
| `mip:Capability` | `me:CapabilityGap` | relatedTo |

### 3.2 JC3IEDM Heritage

Joint C3 Information Exchange Data Model concepts incorporated:

```turtle
# JC3IEDM-derived concepts
wg:OperationalContext owl:equivalentClass jc3iedm:OperationalEnvironment .
wg:ForceSide owl:equivalentClass jc3iedm:AffiliationCategoryCode .
wg:OperationalPhase rdfs:subClassOf jc3iedm:Phase .
```

### 3.3 APP-6 Military Symbology

NATO APP-6(D) symbology codes integrated for:
- Force representation (2525D SIDC)
- Equipment type classification
- Status and operational condition
- Echelon and command relationships

**Integration Pattern:**
```turtle
wg:Force a owl:Class ;
    rdfs:subClassOf [
        a owl:Restriction ;
        owl:onProperty wg:app6Symbol ;
        owl:allValuesFrom xsd:string ;
        rdfs:comment "APP-6D Symbol ID Code (SIDC)"
    ] .
```

### 3.4 STANAG 4774/4778 (C2 Interoperability)

**STANAG 4774** (Metadata Binding Mechanism):
- All wargaming artifacts carry bound metadata
- Classification markings at element level
- Provenance metadata linked to binding

**STANAG 4778** (Security Label):
```turtle
nsw:SecurityLabel a owl:Class ;
    rdfs:subClassOf [
        a owl:Restriction ;
        owl:onProperty nsw:classification ;
        owl:oneOf (nsw:UNCLASSIFIED nsw:RESTRICTED nsw:CONFIDENTIAL
                   nsw:SECRET nsw:COSMIC_TOP_SECRET)
    ] ;
    rdfs:subClassOf [
        a owl:Restriction ;
        owl:onProperty nsw:releasableTo ;
        owl:allValuesFrom nsw:NATONation
    ] .
```

### 3.5 NIEM and Exchange Standards

National Information Exchange Model patterns for:
- Message structure definitions
- Type libraries
- Exchange specifications

**Alignment Strategy:**
1. Map NIEM types to OWL classes
2. Preserve NIEM naming conventions where practical
3. Document deviations with rationale

---

## 4. Formal Axiomatization

### 4.1 First-Order Logic Foundations

The ontology formalizes wargaming concepts in first-order logic with description logic expressivity:

**Domain of Discourse:**
- Entities: Wargames, Moves, Outcomes, Insights, Gaps, Requirements
- Relations: produces, addresses, supports, tracesTo, validates
- Functions: confidence, timestamp, classification

**Signature Definition:**
```
Σ = ⟨C, R, I⟩ where:
  C = {Wargame, Move, Outcome, Insight, Gap, Requirement, ...}
  R = {produces, addresses, supports, tracesTo, validates, ...}
  I = {wg001, move001, insight001, ...}
```

### 4.2 Domain Axioms for Wargaming

**Axiom 1: Insight Provenance Completeness**
```
∀i. Insight(i) → ∃w,o. Wargame(w) ∧ Outcome(o) ∧ produces(w,o) ∧ ledTo(o,i)
```
*Every insight traces to an outcome from a wargame.*

**Axiom 2: Gap-Insight Relevance**
```
∀i,g. supports(i,g) → ∃w. Wargame(w) ∧ addresses(w,g) ∧ produces(w,i)
```
*An insight supports a gap only if the wargame addressed that gap.*

**Axiom 3: Classification Propagation**
```
∀x,y,c. (derivedFrom(x,y) ∧ hasClassification(y,c) ∧ ¬isDowngraded(x))
        → hasClassification(x,c)
```
*Derived artifacts inherit classification from sources unless explicitly downgraded.*

**Axiom 4: Confidence Bounds**
```
∀x. hasConfidence(x,c) → 0 ≤ c ≤ 1
```
*Confidence values are normalized probabilities.*

**Axiom 5: Temporal Ordering**
```
∀m1,m2. precedes(m1,m2) → timestamp(m1) < timestamp(m2)
```
*Precedence implies temporal ordering.*

### 4.3 Formal Definitions

**Definition 4.3.1: Capability Gap**
```
CapabilityGap(g) ≡
    ∃m,r. MissionContext(m) ∧ Requirement(r) ∧
          requiredFor(r,m) ∧ ¬satisfied(r) ∧ represents(g,r)
```
*A capability gap represents an unsatisfied requirement in a mission context.*

**Definition 4.3.2: Wargame Insight**
```
Insight(i) ≡
    ∃w,e,c. Wargame(w) ∧ Evidence(e) ∧ Confidence(c) ∧
            derivedFrom(i,w) ∧ supportedBy(i,e) ∧ hasConfidence(i,c) ∧
            c > θ_insight
```
*An insight is a wargame-derived finding with evidence and sufficient confidence.*

**Definition 4.3.3: Evidence**
```
Evidence(e) ≡
    ∃s,v. Source(s) ∧ Validator(v) ∧
          originates(e,s) ∧ validatedBy(e,v) ∧
          hasProvenance(e)
```
*Evidence has traceable origin, validation, and provenance.*

**Definition 4.3.4: Analytical Credibility (Operational Definition)**
```
AnalyticallyCredible(i) ≡
    Insight(i) ∧
    hasConfidence(i,c) ∧ c ≥ θ_credible ∧
    hasTraceability(i,t) ∧ complete(t) ∧
    hasValidation(i,v) ∧ (SMEValidated(v) ∨ FormallyVerified(v)) ∧
    hasExplanation(i,e) ∧ comprehensible(e) ∧
    ¬hasContradiction(i)
```
*Analytical credibility requires sufficient confidence, complete traceability, expert or formal validation, comprehensible explanation, and freedom from contradiction.*

### 4.4 Closed-World vs Open-World Assumptions

| Assumption | Domain | Rationale |
|------------|--------|-----------|
| **Closed-World** | Classification labels | Unknown classification = UNCLASSIFIED |
| **Closed-World** | Validation status | Unvalidated insights are not validated |
| **Open-World** | Capability gaps | Unknown gaps may exist |
| **Open-World** | Insight relevance | New relevance may be discovered |

**Implementation:**
- SHACL constraints enforce closed-world semantics where needed
- OWL reasoning operates under open-world assumption
- Explicit negation-as-failure for specific predicates

---

## 5. OWL Profile Selection

### 5.1 OWL 2 Profile Analysis

| Profile | Expressivity | Decidability | Complexity | Use Case |
|---------|--------------|--------------|------------|----------|
| **OWL 2 Full** | Maximal | Undecidable | - | Research exploration |
| **OWL 2 DL** | High | Decidable | 2-NEXPTIME | Full reasoning |
| **OWL 2 EL** | Limited | Decidable | PTIME | Large taxonomies |
| **OWL 2 QL** | Query-focused | Decidable | NLogSpace | Query answering |
| **OWL 2 RL** | Rule-based | Decidable | PTIME | Rule inference |

### 5.2 Decision: OWL 2 DL with RL Subset for Runtime

**Design Decision:**
- **Full Ontology**: OWL 2 DL for complete expressivity during development
- **Runtime Reasoning**: OWL 2 RL subset for production inference
- **Query Answering**: SPARQL with RL entailment regime

**Rationale:**
1. OWL 2 DL supports all required constructors (qualified cardinality, complex class expressions)
2. OWL 2 RL guarantees polynomial-time reasoning for production
3. RL/RIF alignment enables rule-based integration

### 5.3 Decidability Guarantees

**Theorem 5.3.1 (Decidability)**
*The wargaming ontology, when restricted to OWL 2 DL constructs, guarantees decidable entailment.*

**Proof Sketch:**
1. OWL 2 DL corresponds to SROIQ(D) description logic
2. SROIQ(D) is decidable with 2-NEXPTIME complexity
3. All ontology axioms are expressible in SROIQ(D)
4. Therefore, entailment checking terminates

**Complexity Bounds:**
- TBox reasoning: 2-NEXPTIME in ontology size
- ABox reasoning: NP-complete for instance checking
- Conjunctive query answering: Decidable under OWA

### 5.4 Expressivity Restrictions

To ensure decidability, the ontology avoids:
- Non-simple roles in cardinality restrictions
- Cyclic role inclusions
- Property chains with self-reference
- Negated property assertions in class expressions

---

## 6. Competency Questions

### 6.1 Core Competency Questions

**CQ-01 through CQ-10: Mission Engineering Integration**

| ID | Competency Question | Priority |
|----|---------------------|----------|
| CQ-01 | Which capability gaps does a given wargame address? | HIGH |
| CQ-02 | What evidence supports a specific insight? | HIGH |
| CQ-03 | What is the complete provenance chain for an insight? | HIGH |
| CQ-04 | Which insights support a given acquisition requirement? | HIGH |
| CQ-05 | What is the confidence level of a gap hypothesis? | HIGH |
| CQ-06 | Which wargames have addressed similar gap questions? | MEDIUM |
| CQ-07 | What DOTMLPFI implications does a gap have? | MEDIUM |
| CQ-08 | Which measures (MoE/MoP) apply to a gap question? | MEDIUM |
| CQ-09 | What scenarios are appropriate for testing a gap? | MEDIUM |
| CQ-10 | Which stakeholders are affected by a gap? | MEDIUM |

**CQ-11 through CQ-20: Wargaming Lifecycle**

| ID | Competency Question | Priority |
|----|---------------------|----------|
| CQ-11 | What moves occurred in a wargame turn? | HIGH |
| CQ-12 | What outcomes resulted from a move? | HIGH |
| CQ-13 | Which participant made a specific move? | HIGH |
| CQ-14 | What adjudication method resolved an outcome? | MEDIUM |
| CQ-15 | What constraints applied to a move? | HIGH |
| CQ-16 | Were any constraints violated during gameplay? | HIGH |
| CQ-17 | What injects were delivered during execution? | MEDIUM |
| CQ-18 | How did participants respond to injects? | MEDIUM |
| CQ-19 | What is the classification level of wargame artifacts? | HIGH |
| CQ-20 | Who validated AI-generated content? | HIGH |

**CQ-21 through CQ-30: Acquisition Integration**

| ID | Competency Question | Priority |
|----|---------------------|----------|
| CQ-21 | Which requirements are supported by wargame evidence? | HIGH |
| CQ-22 | What acquisition milestone is informed by an insight? | HIGH |
| CQ-23 | Is the evidence sufficient for milestone decision? | HIGH |
| CQ-24 | What alternatives were evaluated in the wargame? | MEDIUM |
| CQ-25 | How do alternatives compare on key measures? | MEDIUM |
| CQ-26 | What risks were identified through wargaming? | HIGH |
| CQ-27 | What mitigation strategies emerged? | MEDIUM |
| CQ-28 | What is the traceability completeness for a decision? | HIGH |
| CQ-29 | Are there contradictory insights for a decision? | HIGH |
| CQ-30 | What confidence threshold applies to this decision? | HIGH |

### 6.2 Coverage Analysis Matrix

| Domain Area | CQs Defined | CQs Covered | Coverage % |
|-------------|-------------|-------------|------------|
| Mission Engineering | 10 | 10 | 100% |
| Wargaming Lifecycle | 10 | 10 | 100% |
| Acquisition Integration | 10 | 10 | 100% |
| **Total** | **30** | **30** | **100%** |

### 6.3 SPARQL Encodings

**CQ-03 Implementation: Complete Provenance Chain**
```sparql
PREFIX nsw: <http://nato.int/neuro-symbolic-wargaming#>
PREFIX wg: <http://nato.int/wargaming#>
PREFIX prov: <http://www.w3.org/ns/prov#>

SELECT ?insight ?outcome ?move ?wargame ?gapQuestion ?confidence
WHERE {
    ?insight a wg:Insight ;
             wg:hasProvenance ?prov .
    ?prov nsw:confidence ?confidence .

    ?outcome wg:ledTo ?insight .
    ?move wg:resultsIn ?outcome .
    ?wargame wg:hasMove ?move ;
             wg:addressesGap ?gapQuestion .

    FILTER (?insight = <specific_insight_uri>)
}
ORDER BY ?move
```

**CQ-28 Implementation: Traceability Completeness**
```sparql
PREFIX nsw: <http://nato.int/neuro-symbolic-wargaming#>
PREFIX wg: <http://nato.int/wargaming#>

SELECT ?decision
       (COUNT(?insight) as ?insightCount)
       (COUNT(?traceComplete) as ?completeTraces)
       ((?completeTraces / ?insightCount) as ?completenessRatio)
WHERE {
    ?decision a acq:AcquisitionDecision ;
              nsw:informedBy ?insight .

    OPTIONAL {
        ?insight wg:hasProvenance ?prov .
        ?prov nsw:traceabilityStatus "complete" .
        BIND(?insight as ?traceComplete)
    }

    FILTER (?decision = <specific_decision_uri>)
}
GROUP BY ?decision
HAVING (?completenessRatio >= 1.0)
```

---

## 7. Knowledge Acquisition

### 7.1 SME Elicitation Protocols

**Protocol 7.1.1: Concept Elicitation**
1. Present domain area (e.g., "wargaming outcomes")
2. Request enumeration of key concepts
3. For each concept, elicit:
   - Definition in domain terms
   - Relationships to other concepts
   - Examples and counter-examples
   - Constraints/invariants
4. Validate against existing ontologies
5. Document with provenance

**Protocol 7.1.2: Axiom Validation**
1. Present axiom in natural language
2. Request SME agreement/disagreement
3. If disagreement:
   - Elicit counter-examples
   - Refine axiom
   - Re-validate
4. Document validation with SME identifier

### 7.2 Doctrine Encoding Procedures

**Step 1: Document Analysis**
- Identify relevant doctrine documents (STANAGs, AJPs, national)
- Extract defined terms and relationships
- Map to existing ontology concepts

**Step 2: Formalization**
```
Doctrine Statement: "A move that violates ROE must be reviewed by legal SME"

Formalization:
∀m. Move(m) ∧ violatesROE(m) → requiresReview(m, LegalSME)
```

**Step 3: Validation**
- Cross-check with legal advisors
- Test against historical examples
- Document exceptions

### 7.3 Validation with Domain Experts

**Expert Panel Composition:**
- Wargaming practitioners (2-3)
- Mission engineers (2-3)
- Acquisition professionals (2-3)
- Knowledge engineers (1-2)
- Legal advisors (1)

**Validation Process:**
| Phase | Duration | Activities |
|-------|----------|------------|
| Initial Review | 2 weeks | Individual CQ validation |
| Panel Discussion | 2 days | Consensus on conflicts |
| Revision | 1 week | Implement changes |
| Final Approval | 1 day | Sign-off on version |

### 7.4 Iterative Refinement

```
┌─────────────────────────────────────────────────────────────────┐
│                ITERATIVE REFINEMENT CYCLE                        │
│                                                                  │
│  ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐    │
│  │ Elicit   │──►│ Formalize│──►│ Validate │──►│ Integrate│───┐│
│  │ Knowledge│   │ Axioms   │   │ with SME │   │ & Test   │   ││
│  └──────────┘   └──────────┘   └──────────┘   └──────────┘   ││
│       ▲                                              │         │
│       └──────────────────────────────────────────────┘         │
│                        Feedback Loop                            │
└─────────────────────────────────────────────────────────────────┘
```

---

## 8. Ontology Governance

### 8.1 Change Management

**Change Request Process:**
1. **Submission**: Requester submits CR with justification
2. **Triage**: Governance board assesses impact (minor/major)
3. **Analysis**: Technical team evaluates compatibility
4. **Decision**: Board approves/rejects/defers
5. **Implementation**: Change implemented with versioning
6. **Communication**: Stakeholders notified

**Impact Classification:**
| Level | Definition | Approval Required |
|-------|------------|-------------------|
| **Minor** | Annotation/documentation changes | Technical lead |
| **Moderate** | New properties, subclasses | Governance board |
| **Major** | Core class changes, axiom modifications | Steering committee |
| **Breaking** | Incompatible changes requiring migration | All stakeholders |

### 8.2 Version Control

**Semantic Versioning:**
- `MAJOR.MINOR.PATCH` (e.g., 2.1.3)
- MAJOR: Breaking changes
- MINOR: Backward-compatible additions
- PATCH: Bug fixes, documentation

**Version URI Strategy:**
```
http://nato.int/neuro-symbolic-wargaming/v1.0/
http://nato.int/neuro-symbolic-wargaming/v2.0/
```

**Compatibility Policy:**
- Support N-1 versions for 2 years
- Provide migration scripts for major versions
- Document deprecation with replacement paths

### 8.3 Multinational Coordination

**National Extension Mechanism:**
```turtle
# Core ontology
nsw:Wargame a owl:Class .

# US Extension
@prefix nsw-us: <http://nato.int/neuro-symbolic-wargaming/extensions/us#> .
nsw-us:JCIDSWargame rdfs:subClassOf nsw:Wargame .

# UK Extension
@prefix nsw-uk: <http://nato.int/neuro-symbolic-wargaming/extensions/uk#> .
nsw-uk:MODWargame rdfs:subClassOf nsw:Wargame .
```

**Coordination Bodies:**
| Body | Role | Meeting Frequency |
|------|------|-------------------|
| Ontology Working Group | Technical coordination | Bi-weekly |
| National Representatives | National requirements | Monthly |
| Governance Board | Change approval | Quarterly |
| Steering Committee | Strategic direction | Annual |

### 8.4 Evolution Procedures

**Ontology Evolution Lifecycle:**
1. **Trigger**: New requirement, standard change, or gap identified
2. **Analysis**: Impact assessment on existing users
3. **Design**: Propose changes with rationale
4. **Review**: Technical and stakeholder review
5. **Approval**: Governance decision
6. **Implementation**: Develop, test, release
7. **Migration**: Support user transition
8. **Deprecation**: Phase out old versions

---

## 9. Verification and Validation

### 9.1 Competency Question Testing

**Automated CQ Testing:**
```python
class CompetencyQuestionTest:
    """Automated competency question validation."""

    def __init__(self, ontology, test_data):
        self.onto = ontology
        self.data = test_data

    def test_cq03_provenance_chain(self):
        """CQ-03: What is the complete provenance chain for an insight?"""
        for insight in self.data.insights:
            chain = self.query_provenance_chain(insight)
            assert chain is not None, f"No chain for {insight}"
            assert chain.has_wargame(), "Missing wargame in chain"
            assert chain.has_gap_question(), "Missing gap question"
            assert chain.is_complete(), "Incomplete provenance"

    def test_cq28_traceability_completeness(self):
        """CQ-28: Is traceability complete for a decision?"""
        for decision in self.data.decisions:
            completeness = self.compute_traceability_completeness(decision)
            assert completeness == 1.0, f"Incomplete: {completeness}"
```

### 9.2 Consistency Checking

**Consistency Verification Protocol:**
1. Load ontology into DL reasoner (HermiT/Pellet)
2. Check for unsatisfiable classes
3. Check for disjointness violations
4. Verify axiom consistency
5. Report any inconsistencies

**Continuous Integration:**
```yaml
# .github/workflows/ontology-check.yml
name: Ontology Consistency Check
on: [push, pull_request]
jobs:
  consistency:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Run HermiT Reasoner
        run: java -jar hermit.jar --consistency ontology.owl
      - name: Run SHACL Validation
        run: shacl validate -s shapes.ttl -d ontology.owl
```

### 9.3 Coverage Analysis

**Structural Coverage:**
| Metric | Formula | Target |
|--------|---------|--------|
| Class Coverage | (defined classes / required classes) × 100 | 100% |
| Property Coverage | (defined properties / required properties) × 100 | 100% |
| Axiom Coverage | (formalized axioms / identified axioms) × 100 | 100% |
| CQ Coverage | (answerable CQs / total CQs) × 100 | 100% |

**Semantic Coverage:**
- Expert agreement on domain coverage
- Comparison with reference ontologies
- Gap analysis against standards

### 9.4 Formal Proof of Ontological Sufficiency

**Theorem 9.4.1 (Ontological Sufficiency)**
*The wargaming ontology O is sufficient for the wargaming domain D if and only if every competency question CQ can be answered by queries over O.*

**Proof Obligation:**
For each CQ_i ∈ {CQ-01, ..., CQ-30}:
1. Define SPARQL query Q_i
2. Show Q_i is expressible over ontology schema
3. Demonstrate Q_i returns correct results for test data
4. Verify Q_i terminates in bounded time

**Sufficiency Certificate:**
```
Certificate of Ontological Sufficiency
Version: 1.0
Date: 2026-XX-XX

Verified by: [Knowledge Engineers]
Validated by: [SME Panel]

Competency Questions: 30/30 answerable
Consistency: Verified by HermiT 1.4.3
Completeness: Verified against MIP DEM, JC3IEDM
Decidability: OWL 2 DL profile confirmed
```

---

## 10. Implementation Roadmap

### 10.1 Phase 1: Foundation (Months 1-6)

| Task | Duration | Deliverable |
|------|----------|-------------|
| Requirements gathering | M1-M2 | Requirements document |
| NATO standards analysis | M1-M3 | Alignment report |
| Core concept identification | M2-M4 | Concept model |
| Initial axiomatization | M4-M6 | Draft ontology v0.1 |
| SME validation (round 1) | M5-M6 | Validation report |

**Milestone M1.1**: Draft ontology with core concepts (M6)

### 10.2 Phase 2: Development (Months 7-12)

| Task | Duration | Deliverable |
|------|----------|-------------|
| Full concept coverage | M7-M9 | Ontology v0.5 |
| SHACL constraints | M8-M10 | Constraint set |
| CQ implementation | M9-M11 | SPARQL queries |
| Integration testing | M10-M12 | Test report |
| SME validation (round 2) | M11-M12 | Final validation |

**Milestone M1.2**: Complete ontology v1.0 (M12)

### 10.3 Phase 3: Operational (Months 13+)

| Task | Duration | Deliverable |
|------|----------|-------------|
| Governance establishment | M13-M15 | Governance charter |
| National extensions | M13-M18 | Extension templates |
| Continuous refinement | Ongoing | Version updates |
| Standards alignment | Annual | Compliance reports |

**Milestone M1.3**: Operational governance (M15)

### 10.4 Resource Requirements

| Resource | Phase 1 | Phase 2 | Phase 3 |
|----------|---------|---------|---------|
| Knowledge Engineers (FTE) | 2 | 3 | 1 |
| SME Engagement (days/month) | 5 | 10 | 3 |
| Computing (Reasoner) | Basic | Moderate | Production |
| Tools | Protégé, SPARQL | + SHACL, CI/CD | + Monitoring |

---

## Appendices

### Appendix A: Ontology Namespace Registry

| Prefix | Namespace | Description |
|--------|-----------|-------------|
| `nsw` | `http://nato.int/neuro-symbolic-wargaming#` | Core ontology |
| `me` | `http://nato.int/mission-engineering#` | Mission engineering |
| `wg` | `http://nato.int/wargaming#` | Wargaming concepts |
| `acq` | `http://nato.int/acquisition#` | Acquisition domain |
| `dotmlpfi` | `http://nato.int/dotmlpfi#` | DOTMLPFI dimensions |
| `prov` | `http://www.w3.org/ns/prov#` | W3C Provenance |
| `mip` | `http://mip-interop.org/dem#` | MIP DEM |
| `jc3iedm` | `http://nato.int/jc3iedm#` | JC3IEDM legacy |

### Appendix B: Glossary of Formal Terms

| Term | Definition |
|------|------------|
| **Axiom** | A statement asserted to be true in the ontology |
| **Class** | A set of individuals sharing common characteristics |
| **Decidability** | Property that reasoning algorithm terminates |
| **DL** | Description Logic - formal basis for OWL |
| **Entailment** | Logical consequence derivable from axioms |
| **OWA** | Open World Assumption - unknown ≠ false |
| **SHACL** | Shapes Constraint Language for validation |
| **TBox** | Terminological component (class definitions) |
| **ABox** | Assertional component (individual facts) |

### Appendix C: Reference Documents

1. W3C OWL 2 Web Ontology Language Specification
2. W3C SHACL Shapes Constraint Language
3. MIP Data Exchange Model v3.1
4. JC3IEDM Specification
5. NATO APP-6(D) Military Symbology
6. STANAG 4774 Metadata Binding Mechanism
7. STANAG 4778 Security Label
8. NeOn Methodology Handbook

---

*Document prepared for NATO STO TAP development.*
*Version 1.0 - 2026-01-23*
