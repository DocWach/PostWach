# Mathematics Agent Workflows

## Overview

This document describes detailed workflows for common mathematical tasks using the agent architecture. Each workflow specifies which agents to invoke, in what order, and how they interact.

---

## Workflow 1: Theorem Proving Pipeline

### Purpose
Develop a complete, verified proof of a mathematical theorem from initial claim to documented result.

### Swarm Configuration
Use: `proof-development` swarm with `mathematical-foundational` queen

### Stages

```
┌─────────────────────────────────────────────────────────────────────┐
│                    THEOREM PROVING PIPELINE                          │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐          │
│  │   STAGE 1    │───▶│   STAGE 2    │───▶│   STAGE 3    │          │
│  │  Formulation │    │  Validation  │    │ Construction │          │
│  └──────────────┘    └──────────────┘    └──────────────┘          │
│         │                   │                   │                   │
│         ▼                   ▼                   ▼                   │
│  conjecture-         counterexample-     proof-                     │
│  generator           hunter              constructor                │
│                                                                      │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐          │
│  │   STAGE 4    │───▶│   STAGE 5    │───▶│   STAGE 6    │          │
│  │ Verification │    │Documentation │    │ Publication  │          │
│  └──────────────┘    └──────────────┘    └──────────────┘          │
│         │                   │                   │                   │
│         ▼                   ▼                   ▼                   │
│  logic-              theorem-            math-research-             │
│  validator           documenter          connector                  │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

### Stage Details

#### Stage 1: Claim Formulation
**Agent**: `conjecture-generator`

**Input**: Informal mathematical observation or hypothesis

**Tasks**:
- Formalize the claim precisely
- Identify all hypotheses and conclusions
- State equivalent formulations
- Classify claim type (existence, universal, etc.)

**Output**: Formal theorem statement

**Example**:
```
Input: "I think the sum of the first n odd numbers equals n²"

Output:
  Theorem: For all n ∈ ℕ, Σᵢ₌₁ⁿ (2i-1) = n²

  Equivalent: 1 + 3 + 5 + ... + (2n-1) = n²

  Type: Universal statement over ℕ
  Suggested proof method: Mathematical induction
```

#### Stage 2: Claim Validation
**Agent**: `counterexample-hunter`

**Input**: Formal theorem statement

**Tasks**:
- Test small cases (n = 1, 2, 3, ...)
- Check boundary conditions
- Search for counterexamples
- Identify potential edge cases

**Output**: Validation report

**Example**:
```
Validation Report:
  n=1: 1 = 1² ✓
  n=2: 1+3 = 4 = 2² ✓
  n=3: 1+3+5 = 9 = 3² ✓
  n=4: 1+3+5+7 = 16 = 4² ✓
  n=5: 1+3+5+7+9 = 25 = 5² ✓

  No counterexamples found.
  Edge cases (n=0, n=1) verified.
  Recommendation: Proceed to proof construction.
```

#### Stage 3: Proof Construction
**Agent**: `proof-constructor`

**Input**: Validated theorem statement

**Tasks**:
- Select proof strategy
- Construct step-by-step proof
- Prove necessary lemmas
- Justify each inference

**Output**: Complete formal proof

**Example**:
```
Proof by mathematical induction on n.

Base case (n=1):
  LHS = 1, RHS = 1² = 1. ✓

Inductive step:
  Assume Σᵢ₌₁ᵏ (2i-1) = k² for some k ≥ 1.

  Σᵢ₌₁ᵏ⁺¹ (2i-1) = Σᵢ₌₁ᵏ (2i-1) + (2(k+1)-1)
                  = k² + (2k+1)           [by IH]
                  = k² + 2k + 1
                  = (k+1)²

By induction, the theorem holds for all n ∈ ℕ. □
```

#### Stage 4: Proof Verification
**Agent**: `logic-validator`

**Input**: Complete proof

**Tasks**:
- Validate each inference step
- Check for logical gaps
- Verify base case sufficiency
- Confirm inductive hypothesis usage

**Output**: Validation certificate

**Example**:
```
VALIDATION CERTIFICATE

Theorem: Σᵢ₌₁ⁿ (2i-1) = n²
Proof Strategy: Mathematical induction

Step-by-step validation:
  ✓ Base case (n=1): Correctly verified
  ✓ IH statement: Properly stated for k ≥ 1
  ✓ Inductive step: Uses IH at line 3
  ✓ Algebraic manipulation: Correct
  ✓ Conclusion: Properly derived

Issues found: 0
Status: VALID
```

#### Stage 5: Documentation
**Agent**: `theorem-documenter`

**Input**: Verified proof

**Tasks**:
- Create theorem card
- Document proof with explanations
- Add examples and intuition
- Map dependencies

**Output**: Complete theorem documentation

#### Stage 6: Publication Preparation
**Agent**: `math-research-connector`

**Input**: Documented theorem

**Tasks**:
- Contextualize in literature
- Assess novelty and significance
- Format for publication
- Prepare submission materials

**Output**: Publication-ready materials

---

## Workflow 2: Algorithm Development Pipeline

### Purpose
Design, analyze, and verify a mathematical algorithm.

### Swarm Configuration
Use: `computational-mathematics` swarm with `mathematical-computational` queen

### Stages

```
┌─────────────────────────────────────────────────────────────────────┐
│                  ALGORITHM DEVELOPMENT PIPELINE                      │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐          │
│  │   STAGE 1    │───▶│   STAGE 2    │───▶│   STAGE 3    │          │
│  │Specification │    │    Design    │    │  Analysis    │          │
│  └──────────────┘    └──────────────┘    └──────────────┘          │
│         │                   │                   │                   │
│         ▼                   ▼                   ▼                   │
│  algorithm-          algorithm-          algorithm-                 │
│  designer            designer            designer                   │
│                                                                      │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐          │
│  │   STAGE 4    │───▶│   STAGE 5    │───▶│   STAGE 6    │          │
│  │  Correctness │    │  Numerical   │    │Documentation │          │
│  └──────────────┘    └──────────────┘    └──────────────┘          │
│         │                   │                   │                   │
│         ▼                   ▼                   ▼                   │
│  proof-              numerical-          theorem-                   │
│  constructor         analyst             documenter                 │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

### Stage Details

#### Stage 1: Problem Specification
**Agent**: `algorithm-designer`

**Tasks**:
- Define input/output precisely
- State preconditions and postconditions
- Identify constraints and requirements
- Specify complexity goals

#### Stage 2: Algorithm Design
**Agent**: `algorithm-designer`

**Tasks**:
- Select algorithmic paradigm
- Design step-by-step procedure
- Handle edge cases
- Write pseudocode

#### Stage 3: Complexity Analysis
**Agent**: `algorithm-designer`

**Tasks**:
- Analyze time complexity
- Analyze space complexity
- Identify best/worst/average cases
- Compare with lower bounds

#### Stage 4: Correctness Proof
**Agent**: `proof-constructor`

**Tasks**:
- Identify loop invariants
- Prove partial correctness
- Prove termination
- Verify postcondition

#### Stage 5: Numerical Analysis
**Agent**: `numerical-analyst`

**Tasks**:
- Analyze numerical stability
- Bound error propagation
- Assess conditioning
- Recommend precision requirements

#### Stage 6: Documentation
**Agent**: `theorem-documenter`

**Tasks**:
- Document algorithm specification
- Record complexity results
- Include correctness proof
- Provide implementation notes

---

## Workflow 3: Mathematical Discovery Pipeline

### Purpose
Explore mathematical structures to discover patterns, formulate conjectures, and attempt proofs.

### Swarm Configuration
Use: `mathematical-discovery` swarm with `mathematical-exploratory` queen

### Stages

```
┌─────────────────────────────────────────────────────────────────────┐
│                  MATHEMATICAL DISCOVERY PIPELINE                     │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐          │
│  │   STAGE 1    │───▶│   STAGE 2    │───▶│   STAGE 3    │          │
│  │  Exploration │    │   Pattern    │    │  Conjecture  │          │
│  └──────────────┘    └──────────────┘    └──────────────┘          │
│         │                   │                   │                   │
│         ▼                   ▼                   ▼                   │
│  pattern-            pattern-            conjecture-                │
│  detector            detector            generator                  │
│                                                                      │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐          │
│  │   STAGE 4    │───▶│   STAGE 5    │───▶│   STAGE 6    │          │
│  │   Testing    │    │    Proof     │    │Interpretation│          │
│  └──────────────┘    └──────────────┘    └──────────────┘          │
│         │                   │                   │                   │
│         ▼                   ▼                   ▼                   │
│  counterexample-     proof-             math-philosophy-            │
│  hunter              constructor        bridge                      │
│                                                                      │
│         │                                                           │
│         ▼                                                           │
│  ┌──────────────┐                                                   │
│  │   ITERATE    │◀──────────────────────────────────────────────────┤
│  │  if needed   │                                                   │
│  └──────────────┘                                                   │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

### Stage Details

#### Stage 1: Data Exploration
**Agent**: `pattern-detector`

**Tasks**:
- Generate examples
- Compute derived quantities
- Visualize data
- Identify anomalies

#### Stage 2: Pattern Recognition
**Agent**: `pattern-detector`

**Tasks**:
- Apply difference/ratio analysis
- Detect symmetries
- Find recurrences
- Identify structural patterns

#### Stage 3: Conjecture Formulation
**Agent**: `conjecture-generator`

**Tasks**:
- Transform patterns to claims
- State conjectures precisely
- Identify generalizations
- Assess plausibility

#### Stage 4: Conjecture Testing
**Agent**: `counterexample-hunter`

**Tasks**:
- Test additional cases
- Search for counterexamples
- Refine conjectures if needed
- Validate edge cases

**Decision Point**:
- Counterexample found → Refine conjecture, return to Stage 3
- No counterexample → Proceed to Stage 5

#### Stage 5: Proof Attempt
**Agent**: `proof-constructor`

**Tasks**:
- Select proof strategy
- Attempt formal proof
- Identify obstacles
- Note partial progress

**Decision Point**:
- Proof succeeds → Proceed to Stage 6
- Proof fails → Return to Stage 2 for more patterns, or document as open problem

#### Stage 6: Philosophical Interpretation
**Agent**: `math-philosophy-bridge`

**Tasks**:
- Interpret significance
- Connect to broader themes
- Analyze conceptual implications
- Ground epistemologically

---

## Workflow 4: Claim Verification Pipeline

### Purpose
Rigorously test and validate a mathematical claim before accepting it.

### Swarm Configuration
Use: `theorem-verification` swarm with `mathematical-foundational` queen

### Stages

```
┌─────────────────────────────────────────────────────────────────────┐
│                    CLAIM VERIFICATION PIPELINE                       │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐          │
│  │   STAGE 1    │───▶│   STAGE 2    │───▶│   STAGE 3    │          │
│  │Decomposition │    │   Testing    │    │ Deep Search  │          │
│  └──────────────┘    └──────────────┘    └──────────────┘          │
│         │                   │                   │                   │
│         ▼                   ▼                   ▼                   │
│  counterexample-     counterexample-     counterexample-            │
│  hunter              hunter              hunter                     │
│                                                                      │
│  ┌──────────────┐    ┌──────────────┐                               │
│  │   STAGE 4    │───▶│   STAGE 5    │                               │
│  │   Defense    │    │   Verdict    │                               │
│  └──────────────┘    └──────────────┘                               │
│         │                   │                                       │
│         ▼                   ▼                                       │
│  proof-              logic-                                         │
│  constructor         validator                                      │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

### Stage Details

#### Stage 1: Claim Decomposition
Break claim into testable components

#### Stage 2: Systematic Testing
Test against standard counterexample libraries

#### Stage 3: Deep Search
Construct pathological examples targeting potential weaknesses

#### Stage 4: Defense
Address any issues found; strengthen claim if needed

#### Stage 5: Verdict
Issue final validation certificate

---

## Workflow 5: Publication Pipeline

### Purpose
Prepare mathematical results for academic publication.

### Agents Involved
- `math-research-connector` (primary)
- `theorem-documenter`
- All agents that produced the results

### Stages

1. **Literature Survey**: Map related work
2. **Novelty Assessment**: Evaluate contribution
3. **Manuscript Preparation**: Structure paper
4. **Formatting**: Apply LaTeX typesetting skill
5. **Review Preparation**: Anticipate referee concerns
6. **Submission**: Prepare submission package

---

## Agent Interaction Patterns

### Sequential Handoff
One agent completes, passes output to next:
```
Agent A → output → Agent B → output → Agent C
```

### Parallel Validation
Multiple agents check same input:
```
         ┌→ Agent A (check X) ─┐
Input ───┼→ Agent B (check Y) ─┼→ Combine results
         └→ Agent C (check Z) ─┘
```

### Iterative Refinement
Loop between agents until convergence:
```
Agent A ←→ Agent B (iterate until done)
```

### Adversarial Testing
One agent challenges another:
```
proof-constructor ←→ counterexample-hunter
    (defend)            (attack)
```

---

## Best Practices

1. **Start with validation**: Always use counterexample-hunter before extensive proof work
2. **Document continuously**: Invoke theorem-documenter at each major milestone
3. **Match queen to task**: Use appropriate queen type for the workflow
4. **Iterate when stuck**: If proof fails, return to pattern detection
5. **Connect to philosophy**: For foundational work, include math-philosophy-bridge
6. **Verify before publishing**: Always run full verification before submission

