# Lie Algebras Skill

## Overview

This skill provides methodology for Lie algebra analysis, including structure theory, classification, and representation theory. It coordinates with the lie-algebraist agent.

## Invocation

```
/lie-algebras [subcommand] [arguments]
```

## Subcommands

### `/lie-algebras structure <algebra>`
Analyze Lie algebra structure (solvable, nilpotent, semisimple).

### `/lie-algebras roots <algebra>`
Compute root system and Cartan subalgebra.

### `/lie-algebras classify <algebra>`
Classify a semisimple Lie algebra.

### `/lie-algebras representation <algebra> <weight>`
Analyze representation with given highest weight.

### `/lie-algebras decompose <algebra>`
Apply Levi decomposition.

### `/lie-algebras bracket <elements>`
Compute Lie brackets.

---

## Methodology

### Structure Analysis

```
STRUCTURE ANALYSIS
═══════════════════════════════════════════════════════════════

STEP 1: BASIC INVARIANTS
─────────────────────────────────────────
- Dimension
- Center Z(𝔤) = {x : [x,y] = 0 ∀y}
- Derived algebra [𝔤,𝔤]

STEP 2: SOLVABILITY/NILPOTENCY
─────────────────────────────────────────
Derived series: 𝔤⁽⁰⁾ = 𝔤, 𝔤⁽ⁱ⁺¹⁾ = [𝔤⁽ⁱ⁾, 𝔤⁽ⁱ⁾]
Lower central: 𝔤₀ = 𝔤, 𝔤ᵢ₊₁ = [𝔤, 𝔤ᵢ]

Solvable: 𝔤⁽ⁿ⁾ = 0 for some n
Nilpotent: 𝔤ₙ = 0 for some n

STEP 3: KILLING FORM
─────────────────────────────────────────
κ(x,y) = tr(ad_x ∘ ad_y)
Semisimple ⟺ κ non-degenerate
```

### Root System Computation

```
ROOT SYSTEM COMPUTATION
═══════════════════════════════════════════════════════════════

STEP 1: CARTAN SUBALGEBRA
─────────────────────────────────────────
Find maximal toral subalgebra 𝔥
(abelian, ad_h diagonalizable ∀h ∈ 𝔥)

STEP 2: ROOT SPACES
─────────────────────────────────────────
For α ∈ 𝔥*:
𝔤_α = {x ∈ 𝔤 : [h,x] = α(h)x ∀h ∈ 𝔥}

Roots Φ = {α ≠ 0 : 𝔤_α ≠ 0}

STEP 3: SIMPLE ROOTS
─────────────────────────────────────────
Choose Φ⁺ (positive roots)
Δ = {simple roots} = indecomposable positives
Cartan matrix: aᵢⱼ = ⟨αᵢ, αⱼ∨⟩

STEP 4: DYNKIN DIAGRAM
─────────────────────────────────────────
Nodes = simple roots
Edges encode angles and length ratios
```

---

## Output Format

### Lie Algebra Report
```
LIE ALGEBRA ANALYSIS
═══════════════════════════════════════════════════════════════

ALGEBRA
─────────────────────────────────────────
[Definition/presentation]

STRUCTURE
─────────────────────────────────────────
Dimension: [dim]
Center: [description]
Type: [solvable/nilpotent/semisimple/reductive]

ROOT SYSTEM (if semisimple)
─────────────────────────────────────────
Rank: [rank]
Roots: [list]
Dynkin type: [A_n, B_n, etc.]

KEY PROPERTIES
─────────────────────────────────────────
[Specific features]
```

---

## Examples

### Example: Structure of 𝔤𝔩(n)

```
/lie-algebras structure "𝔤𝔩(n, ℂ)"

LIE ALGEBRA ANALYSIS: 𝔤𝔩(n, ℂ)
═══════════════════════════════════════════════════════════════

ALGEBRA
─────────────────────────────────────────
𝔤𝔩(n, ℂ) = all n×n complex matrices
Bracket: [A, B] = AB - BA

STRUCTURE
─────────────────────────────────────────
Dimension: n²
Center: Z = ℂ·I (scalar matrices)
[𝔤𝔩, 𝔤𝔩] = 𝔰𝔩(n) (traceless matrices)

TYPE
─────────────────────────────────────────
Reductive: 𝔤𝔩(n) = 𝔰𝔩(n) ⊕ ℂ (center)
𝔰𝔩(n) is simple (type A_{n-1})

DECOMPOSITION
─────────────────────────────────────────
𝔤𝔩(n) = 𝔰𝔩(n) ⊕ Z(𝔤𝔩(n))
       = (semisimple) ⊕ (abelian)
```

### Example: Root System of 𝔰𝔩(3)

```
/lie-algebras roots "𝔰𝔩(3, ℂ)"

ROOT SYSTEM: 𝔰𝔩(3, ℂ)
═══════════════════════════════════════════════════════════════

CARTAN SUBALGEBRA
─────────────────────────────────────────
𝔥 = diagonal traceless matrices
dim 𝔥 = 2 (rank 2)

Basis: h₁ = diag(1,-1,0), h₂ = diag(0,1,-1)

ROOTS
─────────────────────────────────────────
Φ = {±α₁, ±α₂, ±(α₁+α₂)}

α₁(h₁) = 2, α₁(h₂) = -1
α₂(h₁) = -1, α₂(h₂) = 2

SIMPLE ROOTS
─────────────────────────────────────────
Δ = {α₁, α₂}

CARTAN MATRIX
─────────────────────────────────────────
A = ( 2  -1)
    (-1   2)

DYNKIN DIAGRAM
─────────────────────────────────────────
○───○
α₁  α₂

Type: A₂
```

---

## References

- Humphreys, J.E. (1972). Introduction to Lie Algebras and Representation Theory
- Knapp, A.W. (2002). Lie Groups Beyond an Introduction
- Serre, J.-P. (2001). Complex Semisimple Lie Algebras
