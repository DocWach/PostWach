# K-Theory Skill

## Overview

This skill provides methodology for K-theory, including topological K-theory, algebraic K-theory, and applications to geometry and number theory. It coordinates with the k-theorist agent.

## Invocation

```
/k-theory [subcommand] [arguments]
```

## Subcommands

### `/k-theory topological <space>`
Compute topological K-theory of a space.

### `/k-theory algebraic <ring>`
Compute algebraic K-groups of a ring.

### `/k-theory chern <bundle>`
Compute Chern character and classes.

### `/k-theory adams <element>`
Apply Adams operations.

### `/k-theory index <operator>`
Apply index theorem.

### `/k-theory grothendieck <morphism>`
Apply Grothendieck-Riemann-Roch.

---

## Methodology

### Topological K-Theory Computation

```
TOPOLOGICAL K-THEORY
═══════════════════════════════════════════════════════════════

STEP 1: IDENTIFY SPACE TYPE
─────────────────────────────────────────
- CW complex structure
- Known spaces (spheres, projective, Grassmannians)
- Products and suspensions

STEP 2: APPLY TECHNIQUES
─────────────────────────────────────────
- Bott periodicity: K(X × S²) ≅ K(X) ⊕ K(X)
- Long exact sequence for pairs
- Mayer-Vietoris for unions
- Splitting principle for calculations

STEP 3: COMPUTE STRUCTURE
─────────────────────────────────────────
- Ring structure (tensor product)
- Adams operations
- Chern character to cohomology
```

### Algebraic K-Theory Computation

```
ALGEBRAIC K-THEORY
═══════════════════════════════════════════════════════════════

K₀ COMPUTATION
─────────────────────────────────────────
1. Identify projective modules
2. Compute Grothendieck group
3. For Dedekind: K₀ = ℤ ⊕ Cl

K₁ COMPUTATION
─────────────────────────────────────────
1. K₁ = GL(R)^{ab}
2. Compute determinant map det: K₁ → R*
3. SK₁ = ker(det)

LOCALIZATION
─────────────────────────────────────────
For (X, Z): ... → Kₙ(Z) → Kₙ(X) → Kₙ(X-Z) → ...
```

### Chern Character

```
CHERN CHARACTER COMPUTATION
═══════════════════════════════════════════════════════════════

FOR VECTOR BUNDLES
─────────────────────────────────────────
ch(E) = rank + c₁ + (c₁² - 2c₂)/2 + ...

Splitting: If E = L₁ ⊕ ... ⊕ Lᵣ
ch(E) = e^{x₁} + ... + e^{xᵣ} where xᵢ = c₁(Lᵢ)

PROPERTIES
─────────────────────────────────────────
ch(E ⊕ F) = ch(E) + ch(F)
ch(E ⊗ F) = ch(E) · ch(F)
ch(E∨) = ch(E)* (dual)
```

---

## Output Format

### K-Theory Report
```
K-THEORY COMPUTATION
═══════════════════════════════════════════════════════════════

OBJECT
─────────────────────────────────────────
[Space/Ring/Scheme]

K-GROUPS
─────────────────────────────────────────
K⁰ = [result]
K¹ = [result]
(Higher groups if relevant)

GENERATORS
─────────────────────────────────────────
[Explicit generators]

RING STRUCTURE
─────────────────────────────────────────
[Product, Adams operations]

COMPARISON MAPS
─────────────────────────────────────────
[Chern character, other invariants]
```

---

## Examples

### Example: K-theory of Sphere

```
/k-theory topological "S²"

K-THEORY: 2-Sphere
═══════════════════════════════════════════════════════════════

OBJECT
─────────────────────────────────────────
X = S² (2-sphere)

K-GROUPS
─────────────────────────────────────────
K⁰(S²) = ℤ ⊕ ℤ
K¹(S²) = 0

GENERATORS
─────────────────────────────────────────
K⁰: [1] = trivial bundle, [H] = Hopf bundle - 1
where H = tautological bundle on ℂℙ¹ ≅ S²

RING STRUCTURE
─────────────────────────────────────────
[H]² = 0 (since S² = ℂℙ¹)
K⁰(S²) ≅ ℤ[H]/(H²)

ADAMS OPERATIONS
─────────────────────────────────────────
ψᵏ([H]) = k·[H]

CHERN CHARACTER
─────────────────────────────────────────
ch: K⁰(S²) → H*(S²; ℚ) = ℚ ⊕ ℚ
ch([H]) = e^h - 1 = h (where h generates H²)
```

### Example: K₀ of Dedekind Domain

```
/k-theory algebraic "ℤ[√-5]"

K-THEORY: ℤ[√-5]
═══════════════════════════════════════════════════════════════

OBJECT
─────────────────────────────────────────
R = ℤ[√-5] (ring of integers of ℚ(√-5))

K-GROUPS
─────────────────────────────────────────
K₀(R) = ℤ ⊕ ℤ/2
K₁(R) = R* = {±1}

EXPLANATION
─────────────────────────────────────────
Class number h = 2
Cl(R) = ℤ/2 generated by 𝔭 = (2, 1+√-5)

K₀ GENERATORS
─────────────────────────────────────────
ℤ factor: [R] (rank)
ℤ/2 factor: [𝔭] (non-principal ideal)

VERIFICATION
─────────────────────────────────────────
𝔭² = (2) is principal
2·[𝔭] = [𝔭²] = [(2)] = [R] in K₀
Non-trivial: 6 = 2·3 = (1+√-5)(1-√-5)
shows unique factorization fails
```

---

## References

- Atiyah, M.F. (1967). K-Theory
- Weibel, C. (2013). The K-book
- Karoubi, M. (2008). K-Theory: An Introduction
