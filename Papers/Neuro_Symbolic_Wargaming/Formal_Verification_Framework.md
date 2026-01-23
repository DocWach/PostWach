# Formal Verification Framework for Neuro-Symbolic Wargaming

**Document Version:** 1.0
**Date:** 2026-01-23
**Author:** University of Arizona PostDoc Research
**Status:** TAP Supporting Document
**Classification:** UNCLASSIFIED // FOR OFFICIAL USE ONLY
**Purpose:** Define formal verification methods, safety case structure, and certification pathway for NATO-grade guarantees in neuro-symbolic wargaming systems

---

## Executive Summary

This document establishes the **Formal Verification Framework** for the neuro-symbolic wargaming system. Unlike typical AI systems validated through empirical testing alone, defense acquisition decisions require **formal guarantees** that system properties hold under all conditions. This framework provides:

- Formal specification of safety and liveness properties
- Model checking strategy for system verification
- Theorem proving approach for correctness claims
- Formal confidence quantification with Bayesian foundations
- Safety case structure following GSN with formal backing
- Certification pathway aligned with defense standards

The framework ensures that AI-augmented wargaming insights meet the evidentiary standards required for NATO capability development and acquisition decisions.

---

## Table of Contents

1. [Introduction](#1-introduction)
2. [Formal Specification](#2-formal-specification)
3. [Temporal Logic Specifications](#3-temporal-logic-specifications)
4. [Model Checking Strategy](#4-model-checking-strategy)
5. [Theorem Proving](#5-theorem-proving)
6. [Constraint Satisfaction Formalism](#6-constraint-satisfaction-formalism)
7. [Formal Confidence Quantification](#7-formal-confidence-quantification)
8. [Traceability Formalism](#8-traceability-formalism)
9. [Safety Case Structure](#9-safety-case-structure)
10. [Neural-Symbolic Interface Contract](#10-neural-symbolic-interface-contract)
11. [Certification Pathway](#11-certification-pathway)
12. [Implementation Roadmap](#12-implementation-roadmap)

---

## 1. Introduction

### 1.1 Why Formal Guarantees Matter for NATO

Defense acquisition decisions allocate resources that affect national security. These decisions must be:

| Requirement | Informal Approach | Formal Approach |
|-------------|-------------------|-----------------|
| **Justified** | "SMEs agreed it's credible" | "Provenance chain complete, confidence bounds proven" |
| **Traceable** | "The insight came from wargame X" | "∀insight. hasProvenance(insight) ∧ complete(provenance)" |
| **Bounded** | "Confidence is about 85%" | "P(correct | evidence) ∈ [0.82, 0.88] with 95% credibility" |
| **Safe** | "We haven't seen failures" | "□(AIOutput → ConstraintsSatisfied)" |
| **Reliable** | "It usually works" | "◇(Query) → ◇(Response) within T" |

### 1.2 Scope of Formal Verification

**What We Verify:**
- Ontology consistency and completeness
- Constraint satisfaction guarantees
- Traceability chain integrity
- Confidence bound correctness
- Neural-symbolic interface contracts
- Safety property preservation

**What We Do Not Verify:**
- Neural network internal correctness (black box)
- Real-world outcome accuracy (beyond system scope)
- Human decision quality (human-in-the-loop)

### 1.3 Formal Methods Philosophy

We adopt a **defense-in-depth** approach:

```
Level 1: Type System (Static Analysis)
    ↓
Level 2: Constraint Checking (SHACL/OPA)
    ↓
Level 3: Model Checking (Temporal Properties)
    ↓
Level 4: Theorem Proving (Correctness Proofs)
    ↓
Level 5: Runtime Monitoring (Dynamic Verification)
```

Each level catches different classes of defects; together they provide comprehensive assurance.

---

## 2. Formal Specification

### 2.1 Specification Language Selection

**Primary Languages:**

| Language | Use Case | Rationale |
|----------|----------|-----------|
| **Z Notation** | Data type specifications | Rigorous, well-understood, tool support |
| **Alloy** | Structural modeling, constraint analysis | Automatic bounded verification |
| **TLA+** | Temporal behavior, distributed systems | Proven for concurrent systems |
| **Isabelle/HOL** | Theorem proving, correctness proofs | Industrial-strength, large library |

### 2.2 System Properties Classification

**Property Categories:**

```
Properties
├── Safety Properties (bad things never happen)
│   ├── Constraint Satisfaction
│   ├── Classification Enforcement
│   └── Provenance Integrity
├── Liveness Properties (good things eventually happen)
│   ├── Query Response
│   ├── Insight Generation
│   └── Validation Completion
├── Fairness Properties (equitable behavior)
│   ├── No Participant Bias
│   ├── Coalition Neutrality
│   └── Evidence Weighting
└── Invariants (always-true conditions)
    ├── Confidence Bounds
    ├── Traceability Completeness
    └── Ontology Consistency
```

### 2.3 Z Specification: Core Data Types

```z
[ENTITY, CONFIDENCE, TIMESTAMP, CLASSIFICATION]

INSIGHT == [
  id: ℕ;
  content: seq CHAR;
  confidence: CONFIDENCE;
  provenance: PROVENANCE;
  classification: CLASSIFICATION
  |
  0 ≤ confidence ≤ 1
]

PROVENANCE == [
  sources: ℙ ENTITY;
  method: DERIVATION_METHOD;
  agents: seq AGENT;
  timestamps: seq TIMESTAMP
  |
  #sources > 0 ∧
  #agents = #timestamps ∧
  sorted(timestamps)
]

TRACEABILITY_CHAIN == [
  insight: INSIGHT;
  outcome: OUTCOME;
  move: MOVE;
  wargame: WARGAME;
  gap_question: GAP_QUESTION
  |
  insight.provenance.sources ⊇ {outcome} ∧
  outcome ∈ moves(move) ∧
  move ∈ moves(wargame) ∧
  gap_question ∈ addresses(wargame)
]
```

### 2.4 Alloy Model: Structural Constraints

```alloy
module NeuroSymbolicWargaming

sig Entity {}

sig Wargame extends Entity {
  addresses: set GapQuestion,
  hasMove: set Move,
  produces: set Insight,
  classification: one Classification
}

sig Move extends Entity {
  resultsIn: set Outcome,
  madeBy: one Participant,
  timestamp: one Timestamp
}

sig Outcome extends Entity {
  ledTo: set Insight
}

sig Insight extends Entity {
  hasProvenance: one Provenance,
  supports: set Requirement,
  confidence: one Confidence
}

sig Provenance {
  sources: set Entity,
  validatedBy: lone HumanValidator
}

sig GapQuestion extends Entity {}
sig Requirement extends Entity {}
sig Participant extends Entity {}
sig HumanValidator extends Entity {}

-- Confidence is a value between 0 and 1
sig Confidence {
  value: one Int
} { value >= 0 and value <= 100 }

-- Classification levels
abstract sig Classification {}
one sig UNCLASS, RESTRICTED, SECRET, TOP_SECRET extends Classification {}

sig Timestamp {
  value: one Int
} { value >= 0 }

-- FACT: Every insight must have provenance
fact InsightProvenance {
  all i: Insight | some i.hasProvenance.sources
}

-- FACT: Insights trace back to wargames
fact InsightTraceability {
  all i: Insight | some w: Wargame, o: Outcome |
    o in w.hasMove.resultsIn and i in o.ledTo
}

-- FACT: Classification propagates upward
fact ClassificationPropagation {
  all i: Insight, w: Wargame |
    (some o: w.hasMove.resultsIn | i in o.ledTo) implies
    classificationLevel[i.classification] >= classificationLevel[w.classification]
}

fun classificationLevel[c: Classification]: Int {
  c = UNCLASS implies 0 else
  c = RESTRICTED implies 1 else
  c = SECRET implies 2 else
  3
}

-- ASSERTION: No orphan insights
assert NoOrphanInsights {
  all i: Insight | some w: Wargame, m: Move, o: Outcome |
    m in w.hasMove and o in m.resultsIn and i in o.ledTo
}

check NoOrphanInsights for 10
```

---

## 3. Temporal Logic Specifications

### 3.1 LTL for Safety Properties

**Linear Temporal Logic (LTL)** specifies properties over execution traces.

**Notation:**
- □ (always): property holds in all future states
- ◇ (eventually): property holds in some future state
- ○ (next): property holds in the next state
- U (until): property holds until another becomes true
- → (implies): logical implication

### 3.2 Safety Property Formalization

**Property S1: Constraint Satisfaction**
```ltl
□(AIOutput → ConstraintsSatisfied)
```
*Interpretation: Every AI output satisfies all defined constraints.*

**Property S2: Classification Enforcement**
```ltl
□(DerivedData → (Classification(DerivedData) ≥ max(Classification(Sources))))
```
*Interpretation: Derived data is at least as classified as its sources.*

**Property S3: Provenance Integrity**
```ltl
□(Insight → hasValidProvenance(Insight))
```
*Interpretation: Every insight has valid, complete provenance.*

**Property S4: Human Oversight**
```ltl
□(HighImpactDecision → ○(HumanReview))
```
*Interpretation: High-impact decisions are always followed by human review.*

**Property S5: No Unauthorized Declassification**
```ltl
□(¬(Declassify ∧ ¬AuthorizedReviewer))
```
*Interpretation: Declassification never occurs without authorized reviewer.*

### 3.3 Liveness Property Formalization

**Property L1: Query Response**
```ltl
□(Query → ◇Response)
```
*Interpretation: Every query eventually receives a response.*

**Property L2: Bounded Response Time**
```mtl
□(Query → ◇≤T Response)
```
*Interpretation: Response occurs within time bound T (Metric Temporal Logic).*

**Property L3: Insight Validation**
```ltl
□(AIInsight → ◇(Validated ∨ Rejected))
```
*Interpretation: Every AI insight is eventually validated or rejected.*

**Property L4: Gap Resolution Progress**
```ltl
□(GapIdentified → ◇(EvidenceGathered ∨ GapClosed ∨ GapInvalidated))
```
*Interpretation: Identified gaps make progress toward resolution.*

### 3.4 Fairness Properties

**Property F1: No Participant Bias**
```ltl
□(∀p1,p2: Participant. SimilarMoves(p1,p2) → SimilarEvaluation(p1,p2))
```
*Interpretation: Similar moves receive similar evaluations regardless of participant.*

**Property F2: Evidence Weighting Fairness**
```ltl
□(∀e1,e2: Evidence. SameQuality(e1,e2) → SameWeight(e1,e2))
```
*Interpretation: Equal-quality evidence receives equal weight.*

### 3.5 Property Patterns for Wargaming

| Pattern | Template | Wargaming Application |
|---------|----------|----------------------|
| **Absence** | □(¬P) | No constraint violations |
| **Existence** | ◇P | Eventually generate insight |
| **Universality** | □P | Always maintain provenance |
| **Precedence** | □(P → (¬Q U R)) | Validate before releasing |
| **Response** | □(P → ◇Q) | Query leads to answer |
| **Bounded Response** | □(P → ◇≤T Q) | Answer within time limit |

---

## 4. Model Checking Strategy

### 4.1 Tool Selection

| Tool | Strength | Application |
|------|----------|-------------|
| **UPPAAL** | Timed automata, real-time | Response time verification |
| **NuSMV** | CTL/LTL, BDD-based | Safety properties |
| **SPIN** | LTL, explicit state | Protocol verification |
| **TLA+ Model Checker** | Distributed systems | Coordination protocols |

### 4.2 State Space Management

**Challenge:** State explosion in complex systems.

**Mitigation Strategies:**

| Strategy | Description | Application |
|----------|-------------|-------------|
| **Abstraction** | Remove irrelevant details | Abstract confidence to {low, medium, high} |
| **Symmetry Reduction** | Exploit structural symmetry | Interchangeable participants |
| **Partial Order Reduction** | Reduce interleaving | Independent operations |
| **Bounded Verification** | Verify up to bound k | "No bugs in first k steps" |
| **Compositional Verification** | Verify components separately | Verify each neural component independently |

### 4.3 Abstraction Techniques

**Predicate Abstraction:**
```
Concrete: confidence ∈ [0, 1]
Abstract: confidence ∈ {LOW, MEDIUM, HIGH}
         LOW    = [0, 0.5)
         MEDIUM = [0.5, 0.8)
         HIGH   = [0.8, 1.0]
```

**Data Abstraction:**
```
Concrete: InsightSet = finite set of insight objects
Abstract: InsightCount ∈ {ZERO, FEW, MANY}
         ZERO = |InsightSet| = 0
         FEW  = 1 ≤ |InsightSet| ≤ 10
         MANY = |InsightSet| > 10
```

### 4.4 Verification Protocol

```
┌─────────────────────────────────────────────────────────────────┐
│                  MODEL CHECKING PROTOCOL                          │
│                                                                  │
│  1. Specify property in temporal logic                           │
│                     ↓                                            │
│  2. Build finite-state model (with abstraction)                  │
│                     ↓                                            │
│  3. Run model checker                                            │
│                     ↓                                            │
│  4. If property holds: VERIFIED                                  │
│     If counterexample found:                                     │
│        - Analyze counterexample                                  │
│        - If spurious: refine abstraction, goto 2                 │
│        - If real: fix system, goto 2                            │
└─────────────────────────────────────────────────────────────────┘
```

### 4.5 Scalability Approach

**Modular Verification:**
```
System = NeuralComponents ∥ SymbolicComponents ∥ IntegrationLayer

Verify independently:
1. NeuralComponents: Input → Output (black-box behavioral spec)
2. SymbolicComponents: Query → Inference (correctness properties)
3. IntegrationLayer: NeuralOutput → SymbolicValidated (interface contract)

Compose results:
If (1) ∧ (2) ∧ (3) then System properties hold
```

---

## 5. Theorem Proving

### 5.1 Proof Obligations

Theorem proving establishes correctness with mathematical certainty.

**Core Theorems to Prove:**

| Theorem | Statement | Proof Technique |
|---------|-----------|-----------------|
| T1: Provenance Completeness | Every insight has a complete provenance chain | Structural induction |
| T2: Classification Monotonicity | Classification never decreases through derivation | Lattice theory |
| T3: Confidence Bound Correctness | Confidence intervals contain true probability | Bayesian analysis |
| T4: Constraint Satisfiability | Valid configurations exist | SAT/SMT solving |
| T5: Traceability Preservation | Traceability survives all transformations | Invariant preservation |

### 5.2 Isabelle/HOL Formalization

**Ontology Formalization:**
```isabelle
theory NeuroSymbolicWargaming
imports Main
begin

datatype classification = UNCLASS | RESTRICTED | SECRET | TOP_SECRET

fun class_ord :: "classification ⇒ nat" where
  "class_ord UNCLASS = 0" |
  "class_ord RESTRICTED = 1" |
  "class_ord SECRET = 2" |
  "class_ord TOP_SECRET = 3"

definition class_leq :: "classification ⇒ classification ⇒ bool" where
  "class_leq c1 c2 ≡ class_ord c1 ≤ class_ord c2"

record insight =
  content :: string
  confidence :: real
  sources :: "entity set"
  classification :: classification

record provenance =
  derivation_method :: string
  source_entities :: "entity set"
  timestamps :: "nat list"

-- Axiom: Confidence is bounded
definition valid_confidence :: "real ⇒ bool" where
  "valid_confidence c ≡ 0 ≤ c ∧ c ≤ 1"

-- Theorem: Classification propagates upward
theorem classification_propagation:
  assumes "derived_from i s"
  assumes "classification s = c"
  assumes "¬ downgraded i"
  shows "class_leq c (classification i)"
  sorry -- Proof to be completed

end
```

### 5.3 Proof Strategy

**Structural Induction for Provenance:**
```
Theorem: ∀i: Insight. hasCompleteProvenance(i)

Proof by structural induction on insight derivation:

Base case: i is directly observed
  - Observer recorded as source
  - Timestamp recorded
  - Method = "direct_observation"
  - hasCompleteProvenance(i) holds ✓

Inductive case: i is derived from {i₁, ..., iₙ}
  - By IH, hasCompleteProvenance(iⱼ) for all j
  - Derivation records sources = {i₁, ..., iₙ}
  - Timestamp recorded for derivation
  - Method = derivation method
  - hasCompleteProvenance(i) holds ✓

QED
```

### 5.4 Automation Level

| Proof Type | Automation | Human Effort |
|------------|------------|--------------|
| Type checking | Fully automatic | None |
| Simple properties | Mostly automatic | Lemma hints |
| Complex properties | Semi-automatic | Proof structure |
| Novel theorems | Mostly manual | Full proof |

**Target:** 80% of proofs fully automated, 20% requiring human guidance.

---

## 6. Constraint Satisfaction Formalism

### 6.1 CSP Formalization

Model constraint satisfaction as a CSP (Constraint Satisfaction Problem):

**Definition:**
```
CSP = ⟨X, D, C⟩ where:
  X = {x₁, ..., xₙ}     -- Variables (wargame parameters)
  D = {D₁, ..., Dₙ}     -- Domains (valid values)
  C = {c₁, ..., cₘ}     -- Constraints (rules)
```

**Wargaming CSP Example:**
```
Variables:
  scenario_type ∈ {MATRIX, SEMINAR, TABLETOP, COMPUTATIONAL}
  participant_count ∈ {1..100}
  classification ∈ {UNCLASS, RESTRICTED, SECRET, TOP_SECRET}
  gap_coverage ∈ subsets(GapQuestions)
  duration ∈ {1..30} days

Constraints:
  c1: scenario_type = MATRIX → participant_count ≤ 30
  c2: classification = TOP_SECRET → participant_count ≤ 15
  c3: |gap_coverage| ≥ 1
  c4: scenario_type = COMPUTATIONAL → duration ≥ 1
  c5: ∀g ∈ gap_coverage. hasScenario(g)
```

### 6.2 Decidability Proofs

**Theorem 6.2.1 (CSP Decidability):**
*The wargaming CSP is decidable.*

**Proof:**
1. All variable domains are finite
2. All constraints are expressible in first-order logic over finite domains
3. Finite-domain CSP is decidable (NP-complete)
4. Therefore, satisfiability can be determined in finite time ∎

**Complexity Analysis:**
- Variables: n (bounded by system design)
- Domain size: d (bounded by specification)
- Constraints: m (bounded by rules)
- Worst-case: O(d^n) for naive search
- With constraint propagation: typically much better

### 6.3 Conflict Detection and Resolution

**Conflict Types:**

| Type | Example | Resolution |
|------|---------|------------|
| **Hard Conflict** | Classification violation | Block action |
| **Soft Conflict** | Resource overload | Suggest alternative |
| **Preference Conflict** | Multiple valid options | Present to user |

**Resolution Algorithm:**
```python
def resolve_conflicts(constraints, assignment):
    """
    Detect and resolve constraint conflicts.
    Returns: (is_satisfiable, resolution)
    """
    violations = check_violations(constraints, assignment)

    if not violations:
        return (True, assignment)

    for violation in violations:
        if violation.is_hard():
            # Cannot proceed - report violation
            return (False, explain_violation(violation))
        else:
            # Soft constraint - find alternative
            alternatives = find_alternatives(violation, constraints)
            if alternatives:
                return (True, suggest_alternatives(alternatives))

    return (False, "No resolution found")
```

### 6.4 Correctness Guarantees

**Theorem 6.4.1 (Constraint Satisfaction Soundness):**
*If the constraint checker accepts an assignment, all constraints are satisfied.*

**Proof:**
1. Constraint checker implements explicit checking of each constraint
2. Each constraint c_i has decision procedure P_i
3. Checker returns True iff ∀i. P_i(assignment) = True
4. Therefore, acceptance implies satisfaction ∎

**Theorem 6.4.2 (Constraint Satisfaction Completeness):**
*If all constraints are satisfied by an assignment, the constraint checker accepts.*

**Proof:**
1. Each decision procedure P_i is complete for its constraint type
2. All constraint types have complete decision procedures
3. Checker iterates all constraints
4. Therefore, satisfying assignments are accepted ∎

---

## 7. Formal Confidence Quantification

### 7.1 Bayesian Probability Foundations

Confidence quantification uses Bayesian probability theory:

**Fundamental Equation:**
```
P(H|E) = P(E|H) · P(H) / P(E)

where:
  H = hypothesis (e.g., "capability gap exists")
  E = evidence (wargame observations)
  P(H|E) = posterior probability (confidence after evidence)
  P(E|H) = likelihood (probability of evidence given hypothesis)
  P(H) = prior probability (confidence before evidence)
  P(E) = marginal likelihood (normalizing constant)
```

### 7.2 Measure-Theoretic Framework

**Probability Space:**
```
(Ω, F, P) where:
  Ω = sample space (all possible world states)
  F = σ-algebra on Ω (events we can reason about)
  P: F → [0,1] (probability measure)
```

**Properties:**
1. P(Ω) = 1 (something happens)
2. P(∅) = 0 (nothing doesn't happen)
3. Countable additivity: P(∪ᵢ Aᵢ) = Σᵢ P(Aᵢ) for disjoint Aᵢ

### 7.3 Calibration Bounds (Formal Proofs)

**Definition 7.3.1 (Calibration):**
A confidence estimator C is ε-calibrated if:
```
∀p ∈ [0,1]. |P(correct | C = p) - p| ≤ ε
```

**Theorem 7.3.1 (Calibration Bound):**
*Given n independent predictions with confidence scores, the empirical calibration error converges to the true calibration error as n → ∞.*

**Proof Sketch:**
1. By the law of large numbers, empirical frequencies converge to probabilities
2. For each confidence bucket [p-δ, p+δ], empirical accuracy → P(correct | p)
3. Taking δ → 0, we recover point-wise calibration
4. Convergence rate is O(1/√n) by CLT ∎

**Calibration Verification Protocol:**
```python
def verify_calibration(predictions, outcomes, epsilon=0.1):
    """
    Verify that confidence scores are epsilon-calibrated.

    Args:
        predictions: list of (confidence, predicted_outcome)
        outcomes: list of actual outcomes
        epsilon: calibration tolerance

    Returns:
        (is_calibrated, calibration_error, confidence_interval)
    """
    # Bin predictions by confidence
    bins = partition_by_confidence(predictions, num_bins=10)

    calibration_errors = []
    for bin_center, bin_preds in bins:
        empirical_accuracy = compute_accuracy(bin_preds, outcomes)
        error = abs(empirical_accuracy - bin_center)
        calibration_errors.append(error)

    max_error = max(calibration_errors)
    mean_error = mean(calibration_errors)

    # Compute confidence interval using bootstrap
    ci = bootstrap_confidence_interval(calibration_errors, alpha=0.05)

    return (max_error <= epsilon, mean_error, ci)
```

### 7.4 Uncertainty Propagation

**Propagation Rules:**

| Operation | Uncertainty Propagation |
|-----------|------------------------|
| Conjunction | P(A ∧ B) ≤ min(P(A), P(B)) |
| Disjunction | P(A ∨ B) ≤ P(A) + P(B) |
| Derivation | P(derived) ≤ P(source) · P(method_correct) |
| Aggregation | P(aggregate) = f(P(items)) based on aggregation rule |

**Uncertainty Interval Arithmetic:**
```
[a, b] + [c, d] = [a+c, b+d]
[a, b] × [c, d] = [min(ac,ad,bc,bd), max(ac,ad,bc,bd)]

For confidence intervals:
conf(A ∧ B) ∈ [max(0, conf(A) + conf(B) - 1), min(conf(A), conf(B))]
```

### 7.5 Information-Theoretic Measures

**Entropy of Confidence:**
```
H(C) = -Σᵢ P(cᵢ) log P(cᵢ)
```
*High entropy = high uncertainty about confidence level*

**Information Gain from Evidence:**
```
IG(H; E) = H(H) - H(H|E)
```
*Quantifies how much evidence reduces uncertainty*

**Theorem 7.5.1 (Information Gain Non-Negativity):**
*Information gain is always non-negative: IG(H; E) ≥ 0*

**Proof:**
By the properties of conditional entropy and the data processing inequality ∎

---

## 8. Traceability Formalism

### 8.1 Formal Definition of Completeness

**Definition 8.1.1 (Traceability Chain):**
A traceability chain T for insight i is a sequence:
```
T = (i, o, m, w, g) where:
  i: Insight
  o: Outcome such that ledTo(o, i)
  m: Move such that resultsIn(m, o)
  w: Wargame such that hasMove(w, m)
  g: GapQuestion such that addresses(w, g)
```

**Definition 8.1.2 (Complete Traceability):**
Traceability for insight i is complete iff:
```
Complete(T) ≡
  T.i = i ∧
  ∃o. ledTo(o, i) ∧ T.o = o ∧
  ∃m. resultsIn(m, o) ∧ T.m = m ∧
  ∃w. hasMove(w, m) ∧ T.w = w ∧
  ∃g. addresses(w, g) ∧ T.g = g
```

### 8.2 Provenance Chain Validity Proofs

**Theorem 8.2.1 (Provenance Preservation):**
*If an insight has complete provenance at creation, all transformations preserve provenance completeness.*

**Proof by Induction on Transformation Sequence:**

**Base Case:** Insight i created with complete provenance T.
- By definition, T satisfies Complete(T).
- T is stored with i.

**Inductive Case:** Transformation τ applied to insight i with provenance T.
- Case τ = copy: i' = copy(i), T' = T. Complete(T) → Complete(T').
- Case τ = derive: i' = f(i, i₁, ..., iₙ), T' = merge(T, T₁, ..., Tₙ).
  - merge preserves all chain elements
  - Complete(T) ∧ ∀j.Complete(Tⱼ) → Complete(T')
- Case τ = aggregate: Similar to derive.

All cases preserve completeness ∎

### 8.3 Dependency Graph Formalization

**Definition 8.3.1 (Dependency Graph):**
```
G = (V, E) where:
  V = Insights ∪ Outcomes ∪ Moves ∪ Wargames ∪ GapQuestions
  E = {(u, v) | dependsOn(u, v)}
```

**Properties:**
- G is a directed acyclic graph (DAG)
- Every insight has a path to at least one gap question
- Path length is bounded (by wargame structure)

**Theorem 8.3.1 (Dependency Graph Acyclicity):**
*The dependency graph G is acyclic.*

**Proof:**
1. Edges follow temporal order (derived after source)
2. Temporal order is a strict partial order
3. DAGs have no cycles by definition of strict partial order ∎

### 8.4 Conflict Resolution Semantics

**Conflict Types in Provenance:**

| Conflict | Definition | Resolution |
|----------|------------|------------|
| **Contradiction** | Two insights with opposite conclusions from same evidence | Flag for human review |
| **Inconsistency** | Insight conclusions violate ontology constraints | Reject insight |
| **Ambiguity** | Multiple valid interpretations | Present alternatives |

**Formal Resolution Rules:**
```
Rule R1 (Contradiction):
  contradicts(i₁, i₂) ∧ sameEvidence(i₁, i₂) →
    requiresHumanReview(i₁) ∧ requiresHumanReview(i₂)

Rule R2 (Inconsistency):
  violatesOntology(i) → invalid(i)

Rule R3 (Precedence):
  higherConfidence(i₁, i₂) ∧ ¬contradicts(i₁, i₂) →
    preferred(i₁, i₂)
```

---

## 9. Safety Case Structure

### 9.1 Goal Structuring Notation (GSN)

The safety case uses GSN to structure arguments with formal backing:

```
┌─────────────────────────────────────────────────────────────────────────┐
│                          SAFETY CASE STRUCTURE                           │
│                                                                          │
│                        ┌─────────────────────┐                          │
│                        │ G1: System is       │                          │
│                        │ acceptably safe for │                          │
│                        │ acquisition support │                          │
│                        └──────────┬──────────┘                          │
│                                   │                                      │
│              ┌────────────────────┼────────────────────┐                │
│              │                    │                    │                │
│              ▼                    ▼                    ▼                │
│   ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐        │
│   │ G2: All outputs │  │ G3: Traceability│  │ G4: Human       │        │
│   │ satisfy         │  │ is complete     │  │ oversight       │        │
│   │ constraints     │  │ and correct     │  │ maintained      │        │
│   └────────┬────────┘  └────────┬────────┘  └────────┬────────┘        │
│            │                    │                    │                  │
│            ▼                    ▼                    ▼                  │
│   ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐        │
│   │ S1: Argument by │  │ S2: Argument by │  │ S3: Argument by │        │
│   │ formal          │  │ structural      │  │ operational     │        │
│   │ verification    │  │ induction       │  │ procedures      │        │
│   └────────┬────────┘  └────────┬────────┘  └────────┬────────┘        │
│            │                    │                    │                  │
│            ▼                    ▼                    ▼                  │
│   ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐        │
│   │ E1: Model       │  │ E2: Theorem     │  │ E3: Operational │        │
│   │ checking        │  │ proof in        │  │ audit logs,     │        │
│   │ results         │  │ Isabelle        │  │ training records│        │
│   └─────────────────┘  └─────────────────┘  └─────────────────┘        │
└─────────────────────────────────────────────────────────────────────────┘
```

### 9.2 Formal Backing for Claims

Each GSN claim has formal backing:

| Claim | Formal Backing | Verification Method |
|-------|----------------|---------------------|
| G2: Outputs satisfy constraints | □(AIOutput → ConstraintsSatisfied) | Model checking |
| G3: Traceability complete | ∀i.hasCompleteProvenance(i) | Theorem proving |
| G4: Human oversight | □(HighImpact → HumanReview) | Model checking |
| G5: Confidence calibrated | |P(correct|conf) - conf| ≤ ε | Statistical analysis |
| G6: No unauthorized access | □(Access → Authorized) | Model checking |

### 9.3 Evidence Requirements

**Evidence Categories:**

| Category | Evidence Type | Sufficiency Criteria |
|----------|---------------|---------------------|
| **Formal Proof** | Theorem proof certificate | Verified by proof checker |
| **Model Check** | State space exploration log | No counterexamples, complete coverage |
| **Testing** | Test execution records | Coverage > 95%, all tests pass |
| **Review** | Expert review reports | Independent review, no critical findings |
| **Operational** | Deployment records | Successful operation period |

### 9.4 Assurance Level Mapping

| Assurance Level | Formal Methods Required | Application |
|-----------------|------------------------|-------------|
| **AL1** | None (review only) | Internal exploration |
| **AL2** | Static analysis | Prototype deployment |
| **AL3** | Model checking | Operational use (limited) |
| **AL4** | Model checking + limited theorem proving | Full operational use |
| **AL5** | Full formal verification | Safety-critical decisions |

---

## 10. Neural-Symbolic Interface Contract

### 10.1 The "Neural Proposes, Symbolic Disposes" Pattern

**Principle:** Neural components generate candidates; symbolic components validate and constrain.

```
┌─────────────────────────────────────────────────────────────────────────┐
│                NEURAL PROPOSES, SYMBOLIC DISPOSES                        │
│                                                                          │
│  ┌─────────────────┐                    ┌─────────────────────────────┐│
│  │ NEURAL LAYER    │                    │ SYMBOLIC LAYER              ││
│  │                 │                    │                             ││
│  │ Generate:       │    Proposals       │ Validate:                   ││
│  │ - Scenarios     │───────────────────►│ - Constraint satisfaction   ││
│  │ - Patterns      │                    │ - Ontology consistency      ││
│  │ - Predictions   │                    │ - Classification rules      ││
│  │ - Insights      │    Validated       │ - Provenance requirements   ││
│  │                 │◄───────────────────│                             ││
│  │ With metadata:  │                    │ Returns:                    ││
│  │ - Confidence    │                    │ - Accept/Reject             ││
│  │ - Uncertainty   │                    │ - Violations found          ││
│  │ - Source refs   │                    │ - Repair suggestions        ││
│  └─────────────────┘                    └─────────────────────────────┘│
│                                                                          │
│  INVARIANT: No neural output reaches users without symbolic validation   │
└─────────────────────────────────────────────────────────────────────────┘
```

### 10.2 Formal Interface Contract

**Contract Specification (Design by Contract):**

```python
@dataclass
class NeuralOutput:
    """Output from any neural component."""
    content: Any
    confidence: float  # Precondition: 0 <= confidence <= 1
    sources: List[EntityRef]
    timestamp: datetime
    component_id: str

@dataclass
class SymbolicValidation:
    """Result of symbolic validation."""
    is_valid: bool
    violations: List[Violation]
    repairs: List[Repair]
    validated_output: Optional[ValidatedOutput]

class InterfaceContract:
    """
    Formal contract between neural and symbolic layers.

    Preconditions (Neural → Symbolic):
      - output.confidence ∈ [0, 1]
      - output.sources is non-empty
      - output.timestamp ≤ now()

    Postconditions (Symbolic → System):
      - If is_valid: validated_output satisfies all constraints
      - If not is_valid: violations is non-empty
      - validation.timestamp ≥ output.timestamp

    Invariants:
      - No unvalidated neural output reaches user interface
      - All validated outputs have provenance
      - Classification is preserved or elevated
    """

    def validate(self, output: NeuralOutput) -> SymbolicValidation:
        # Precondition checking
        assert 0 <= output.confidence <= 1, "Confidence out of bounds"
        assert len(output.sources) > 0, "No sources provided"
        assert output.timestamp <= datetime.now(), "Future timestamp"

        # Validation logic
        violations = self.check_constraints(output)

        if violations:
            repairs = self.suggest_repairs(violations)
            return SymbolicValidation(
                is_valid=False,
                violations=violations,
                repairs=repairs,
                validated_output=None
            )
        else:
            validated = self.add_provenance(output)
            # Postcondition: validated output satisfies constraints
            assert self.check_constraints(validated) == [], "Postcondition failed"
            return SymbolicValidation(
                is_valid=True,
                violations=[],
                repairs=[],
                validated_output=validated
            )
```

### 10.3 Guarantee Preservation Proofs

**Theorem 10.3.1 (Guarantee Preservation):**
*If symbolic validation accepts a neural output, all system guarantees hold.*

**Proof:**
1. Let G = {g₁, ..., gₙ} be system guarantees
2. Each guarantee gᵢ corresponds to constraint cᵢ
3. Validation checks all constraints C = {c₁, ..., cₙ}
4. Validation accepts iff ∀i. cᵢ(output) = True
5. By construction, gᵢ holds iff cᵢ is satisfied
6. Therefore, acceptance implies all guarantees hold ∎

### 10.4 Validation Gates

**Gate 1: Structural Validation**
- JSON schema compliance
- Required fields present
- Type correctness

**Gate 2: Ontological Validation**
- Entity references exist in knowledge graph
- Relationship types valid
- Class membership correct

**Gate 3: Constraint Validation**
- SHACL shapes satisfied
- Domain rules met
- Classification rules enforced

**Gate 4: Semantic Validation**
- Consistency with existing knowledge
- No contradictions introduced
- Provenance is complete

---

## 11. Certification Pathway

### 11.1 Relation to Defense Standards

| Standard | Domain | Relevance to Project |
|----------|--------|---------------------|
| **DO-178C** | Aviation software | Formal methods supplement (DO-333) |
| **IEC 61508** | Functional safety | Safety integrity levels concept |
| **MIL-STD-882** | System safety | Hazard analysis methodology |
| **ISO 26262** | Automotive safety | ASIL concept adaptation |
| **Common Criteria** | Security evaluation | EAL structure |

### 11.2 Adapted Certification Framework

We adapt DO-178C concepts for AI wargaming:

| DO-178C Concept | Wargaming Adaptation |
|-----------------|---------------------|
| Software Level | Decision Impact Level |
| Design Assurance Level | Verification Rigor Level |
| Requirements | Competency Questions |
| Design | Ontology + Architecture |
| Code | Implementation |
| Test | Validation Framework |

**Decision Impact Levels:**

| Level | Impact | Verification Required |
|-------|--------|----------------------|
| **DIL-A** | Catastrophic (war/peace decision) | Full formal verification |
| **DIL-B** | Major (significant investment) | Model checking + testing |
| **DIL-C** | Moderate (program-level decision) | Testing + review |
| **DIL-D** | Minor (exploratory analysis) | Basic testing |
| **DIL-E** | Negligible (training/education) | Minimal |

### 11.3 Certification Artifacts

| Artifact | Purpose | DIL Requirement |
|----------|---------|-----------------|
| System Requirements | Define what system must do | A, B, C, D |
| Safety Assessment | Identify hazards and mitigations | A, B, C |
| Formal Specification | Mathematically precise requirements | A, B |
| Model Checking Results | Automated property verification | A, B |
| Theorem Proofs | Mathematical correctness proofs | A |
| Test Cases | Executable validation | All |
| Review Records | Expert examination | All |
| Operational Procedures | Usage guidelines | All |

### 11.4 Certification Process

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    CERTIFICATION PROCESS                                 │
│                                                                          │
│  Phase 1: Planning                                                       │
│  ├─ Define Decision Impact Level                                        │
│  ├─ Select verification methods                                         │
│  └─ Develop certification plan                                          │
│                                                                          │
│  Phase 2: Development with Verification                                  │
│  ├─ Requirements → Formal specification                                 │
│  ├─ Design → Model checking                                             │
│  ├─ Implementation → Testing + analysis                                 │
│  └─ Integration → System verification                                   │
│                                                                          │
│  Phase 3: Certification Evidence                                         │
│  ├─ Compile verification results                                        │
│  ├─ Construct safety case (GSN)                                         │
│  ├─ Independent assessment                                              │
│  └─ Authority review                                                    │
│                                                                          │
│  Phase 4: Approval and Deployment                                        │
│  ├─ Certification authority approval                                    │
│  ├─ Operational constraints defined                                     │
│  └─ Monitoring requirements established                                 │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 12. Implementation Roadmap

### 12.1 Phase 1: Specification (Months 1-6)

| Task | Duration | Deliverable |
|------|----------|-------------|
| Property specification | M1-M3 | LTL/MTL property catalog |
| Z specification | M2-M4 | Data type specifications |
| Alloy modeling | M3-M5 | Structural model |
| Proof obligation identification | M4-M6 | Theorem catalog |

**Milestone F1.1**: Complete formal specification (M6)

### 12.2 Phase 2: Verification Infrastructure (Months 7-12)

| Task | Duration | Deliverable |
|------|----------|-------------|
| Model checker setup | M7-M8 | NuSMV/UPPAAL environment |
| Theorem prover setup | M8-M10 | Isabelle theories |
| CI/CD integration | M9-M11 | Automated verification pipeline |
| Initial proofs | M10-M12 | Core theorem proofs |

**Milestone F1.2**: Verification infrastructure operational (M12)

### 12.3 Phase 3: Full Verification (Months 13-18)

| Task | Duration | Deliverable |
|------|----------|-------------|
| Complete model checking | M13-M15 | All safety properties verified |
| Complete theorem proving | M14-M17 | All theorems proven |
| Safety case construction | M16-M18 | GSN safety case |
| Independent review | M17-M18 | Review report |

**Milestone F1.3**: Full verification complete (M18)

### 12.4 Resource Requirements

| Resource | Phase 1 | Phase 2 | Phase 3 |
|----------|---------|---------|---------|
| Formal Methods Experts (FTE) | 2 | 3 | 2 |
| Tool Licenses | Basic | Full | Full |
| Computing (Model Checking) | Low | High | High |
| Independent Reviewer | - | - | 1 |

---

## Appendices

### Appendix A: Property Catalog

| ID | Property | Type | LTL Formula |
|----|----------|------|-------------|
| S1 | Constraint satisfaction | Safety | □(AIOutput → ConstraintsSatisfied) |
| S2 | Classification enforcement | Safety | □(DerivedData → ClassUpward) |
| S3 | Provenance integrity | Safety | □(Insight → hasValidProvenance) |
| S4 | Human oversight | Safety | □(HighImpact → ○HumanReview) |
| S5 | No unauthorized declassification | Safety | □(¬(Declassify ∧ ¬Authorized)) |
| L1 | Query response | Liveness | □(Query → ◇Response) |
| L2 | Bounded response | Liveness | □(Query → ◇≤T Response) |
| L3 | Insight validation | Liveness | □(AIInsight → ◇Validated) |

### Appendix B: Tool Configuration

**NuSMV Configuration:**
```nusmv
MODULE main
VAR
  state : {idle, processing, validating, outputting};
  constraint_satisfied : boolean;
  provenance_complete : boolean;

ASSIGN
  init(state) := idle;
  next(state) := case
    state = idle & input_received : processing;
    state = processing : validating;
    state = validating & constraint_satisfied : outputting;
    state = validating & !constraint_satisfied : idle;
    state = outputting : idle;
    TRUE : state;
  esac;

-- Safety property: No output without constraint satisfaction
SPEC AG(state = outputting -> constraint_satisfied)

-- Liveness property: Processing eventually completes
SPEC AG(state = processing -> AF(state = idle | state = outputting))
```

### Appendix C: Proof Templates

**Isabelle Proof Template:**
```isabelle
theorem property_name:
  assumes "precondition1"
  assumes "precondition2"
  shows "conclusion"
proof -
  have step1: "intermediate_result1" using assms by auto
  have step2: "intermediate_result2" using step1 by auto
  show ?thesis using step2 by auto
qed
```

### Appendix D: Glossary

| Term | Definition |
|------|------------|
| **LTL** | Linear Temporal Logic |
| **MTL** | Metric Temporal Logic |
| **CSP** | Constraint Satisfaction Problem |
| **GSN** | Goal Structuring Notation |
| **DIL** | Decision Impact Level |
| **Safety Property** | Property asserting bad states are never reached |
| **Liveness Property** | Property asserting good states are eventually reached |
| **Model Checking** | Exhaustive state space exploration |
| **Theorem Proving** | Deductive verification using logic |

---

*Document prepared for NATO STO TAP development.*
*Version 1.0 - 2026-01-23*
