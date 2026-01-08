# Functional Analysis Skill

## Overview

This skill provides methodology for functional analysis including Banach spaces, Hilbert spaces, bounded operators, and spectral theory. It coordinates with the functional-analyst agent for infinite-dimensional analysis.

## Invocation

```
/functional-analysis [subcommand] [arguments]
```

## Subcommands

### `/functional-analysis space <specification>`
Analyze Banach or Hilbert space properties.

### `/functional-analysis operator <specification>`
Analyze bounded linear operators.

### `/functional-analysis spectrum <operator>`
Compute spectrum and spectral properties.

### `/functional-analysis dual <space>`
Identify dual space and functionals.

### `/functional-analysis compact <operator>`
Analyze compact operator properties.

### `/functional-analysis hilbert <space>`
Analyze Hilbert space structure (orthogonality, bases).

---

## Methodology

### Banach Space Analysis Pipeline

```
BANACH SPACE VERIFICATION
═══════════════════════════════════════════════════════════════

STEP 1: VERIFY VECTOR SPACE
─────────────────────────────────────────
□ Closure under addition
□ Closure under scalar multiplication
□ Contains zero vector

STEP 2: VERIFY NORM
─────────────────────────────────────────
□ ‖x‖ ≥ 0, ‖x‖ = 0 ⟺ x = 0
□ ‖αx‖ = |α| ‖x‖
□ ‖x + y‖ ≤ ‖x‖ + ‖y‖

STEP 3: VERIFY COMPLETENESS
─────────────────────────────────────────
Method A: Show every Cauchy sequence converges
  1. Take Cauchy sequence (xₙ)
  2. Find candidate limit x
  3. Prove xₙ → x in norm
  4. Verify x is in the space

Method B: Use known complete spaces
  □ Closed subspace of Banach is Banach
  □ Product of Banach spaces is Banach
  □ L^p(μ), ℓ^p, C[a,b] are Banach

COMMON BANACH SPACES
─────────────────────────────────────────
Space         Norm                Complete?
─────────────────────────────────────────
ℓ^p          (Σ|xₙ|^p)^{1/p}      Yes
ℓ^∞          sup|xₙ|              Yes
c₀           sup|xₙ|              Yes
C[a,b]       max|f(x)|            Yes
L^p(μ)       (∫|f|^p)^{1/p}       Yes
C¹[a,b]      ‖f‖_∞ + ‖f'‖_∞      Yes
```

### Hilbert Space Analysis Pipeline

```
HILBERT SPACE ANALYSIS
═══════════════════════════════════════════════════════════════

INNER PRODUCT VERIFICATION
─────────────────────────────────────────
□ ⟨x, x⟩ ≥ 0, = 0 ⟺ x = 0
□ ⟨x, y⟩ = ⟨y, x⟩* (conjugate symmetry)
□ ⟨αx + βy, z⟩ = α⟨x,z⟩ + β⟨y,z⟩

INDUCED NORM
─────────────────────────────────────────
‖x‖ = √⟨x,x⟩

Verify parallelogram law:
‖x + y‖² + ‖x - y‖² = 2‖x‖² + 2‖y‖²

ORTHOGONAL DECOMPOSITION
─────────────────────────────────────────
For closed subspace M:
  H = M ⊕ M⊥

Projection onto M:
  P_M x = unique element of M closest to x

ORTHONORMAL BASIS
─────────────────────────────────────────
{eₙ} is ONB if:
□ ⟨eᵢ, eⱼ⟩ = δᵢⱼ
□ span{eₙ} dense in H

Then:
  x = Σ⟨x, eₙ⟩eₙ
  ‖x‖² = Σ|⟨x, eₙ⟩|²  (Parseval)

GRAM-SCHMIDT PROCESS
─────────────────────────────────────────
Input: {v₁, v₂, ...} linearly independent
Output: {e₁, e₂, ...} orthonormal

Algorithm:
  u₁ = v₁, e₁ = u₁/‖u₁‖
  uₖ = vₖ - Σᵢ<ₖ ⟨vₖ, eᵢ⟩eᵢ
  eₖ = uₖ/‖uₖ‖
```

### Operator Analysis Pipeline

```
BOUNDED OPERATOR ANALYSIS
═══════════════════════════════════════════════════════════════

BOUNDEDNESS VERIFICATION
─────────────────────────────────────────
T: X → Y bounded ⟺ any of:
□ ‖T‖ = sup_{‖x‖=1} ‖Tx‖ < ∞
□ T continuous
□ T maps bounded sets to bounded sets

OPERATOR NORM COMPUTATION
─────────────────────────────────────────
‖T‖ = sup_{‖x‖≤1} ‖Tx‖
    = sup_{x≠0} ‖Tx‖/‖x‖

Strategies:
1. Find upper bound: ‖Tx‖ ≤ M‖x‖ ⟹ ‖T‖ ≤ M
2. Find attaining sequence: ‖Txₙ‖/‖xₙ‖ → L ⟹ ‖T‖ ≥ L
3. If tight, ‖T‖ = M = L

ADJOINT (HILBERT SPACE)
─────────────────────────────────────────
T* defined by: ⟨Tx, y⟩ = ⟨x, T*y⟩ for all x, y

Properties:
□ ‖T*‖ = ‖T‖
□ (ST)* = T*S*
□ ‖T*T‖ = ‖T‖²
□ T** = T

SPECIAL OPERATORS
─────────────────────────────────────────
Self-adjoint: T = T*
  □ ⟨Tx, x⟩ real
  □ Eigenvalues real
  □ ‖T‖ = sup|⟨Tx, x⟩|

Normal: TT* = T*T
  □ Unitarily diagonalizable (if compact)

Unitary: T*T = TT* = I
  □ Preserves inner product
  □ Eigenvalues on unit circle

Projection: P² = P = P*
  □ P = P_M for some closed subspace M
```

### Spectral Analysis Pipeline

```
SPECTRUM ANALYSIS
═══════════════════════════════════════════════════════════════

DEFINITIONS
─────────────────────────────────────────
Resolvent set: ρ(T) = {λ : (T - λI)⁻¹ ∈ B(X)}
Spectrum: σ(T) = ℂ \ ρ(T)

Point spectrum: σ_p(T) = {λ : Tx = λx for some x ≠ 0}
Continuous spectrum: (T-λI) injective, dense range, not surjective
Residual spectrum: (T-λI) injective, range not dense

COMPUTING SPECTRUM
─────────────────────────────────────────
Step 1: Find eigenvalues (point spectrum)
  Solve Tx = λx

Step 2: Check approximate eigenvalues
  λ ∈ σ(T) ⟺ ∃(xₙ): ‖xₙ‖ = 1, ‖(T-λI)xₙ‖ → 0

Step 3: Use spectral properties
  □ σ(T) ⊆ {|λ| ≤ ‖T‖}
  □ σ(T) nonempty, compact
  □ r(T) = max|λ| = lim ‖Tⁿ‖^{1/n}

SPECTRAL THEOREM (SELF-ADJOINT)
─────────────────────────────────────────
For T = T* on Hilbert space:
□ σ(T) ⊆ ℝ
□ Eigenvectors for distinct eigenvalues are orthogonal
□ For compact T: H has ONB of eigenvectors, T = Σλₙ⟨·, eₙ⟩eₙ

SPECTRAL THEOREM (GENERAL)
─────────────────────────────────────────
For bounded self-adjoint T:
  T = ∫_{σ(T)} λ dE_λ

where E is the spectral measure (projection-valued).
```

### Compact Operator Analysis Pipeline

```
COMPACT OPERATOR ANALYSIS
═══════════════════════════════════════════════════════════════

COMPACTNESS VERIFICATION
─────────────────────────────────────────
T compact ⟺ any of:
□ T(B_X) has compact closure
□ Every bounded (xₙ) has (Txₙ) with convergent subsequence
□ T is limit of finite-rank operators

PROPERTIES OF COMPACT OPERATORS
─────────────────────────────────────────
□ K(X,Y) is closed in B(X,Y)
□ ST, TS compact if T compact
□ T compact ⟹ T* compact

SPECTRAL PROPERTIES (COMPACT)
─────────────────────────────────────────
For T compact:
□ σ(T) countable with 0 as only accumulation point
□ Every λ ≠ 0 in σ(T) is eigenvalue
□ Eigenspaces for λ ≠ 0 are finite-dimensional

FREDHOLM ALTERNATIVE
─────────────────────────────────────────
For T compact, consider (I - T)x = y:

Either:
  □ Unique solution for every y, OR
  □ (I - T)x = 0 has nontrivial solutions

If nontrivial kernel: Solution exists ⟺ y ⊥ ker(I - T*)

EXAMPLES OF COMPACT OPERATORS
─────────────────────────────────────────
□ Finite rank operators
□ Integral operators with L² kernel
□ Embedding H¹ ↪ L² (Rellich)
□ Hilbert-Schmidt operators
```

### Duality Pipeline

```
DUAL SPACE IDENTIFICATION
═══════════════════════════════════════════════════════════════

STANDARD DUALS
─────────────────────────────────────────
Space         Dual              Pairing
─────────────────────────────────────────
ℓ^p (1<p<∞)   ℓ^q (1/p+1/q=1)   ⟨x,y⟩ = Σxₙyₙ
ℓ¹            ℓ^∞               ⟨x,y⟩ = Σxₙyₙ
c₀            ℓ¹                ⟨x,y⟩ = Σxₙyₙ
L^p (1<p<∞)   L^q               ⟨f,g⟩ = ∫fg
L¹            L^∞               ⟨f,g⟩ = ∫fg
H (Hilbert)   H                 Riesz representation

HAHN-BANACH APPLICATIONS
─────────────────────────────────────────
Extension: f on M extends to F on X with ‖F‖ = ‖f‖

Separation: Disjoint convex sets can be separated

Consequence: X* separates points of X

REFLEXIVITY
─────────────────────────────────────────
X reflexive ⟺ canonical J: X → X** is surjective

Reflexive spaces:
□ Hilbert spaces
□ L^p, ℓ^p for 1 < p < ∞

Not reflexive:
□ ℓ¹, c₀, L¹, L^∞

WEAK TOPOLOGIES
─────────────────────────────────────────
Weak: xₙ ⇀ x ⟺ f(xₙ) → f(x) for all f ∈ X*
Weak*: fₙ ⇀* f ⟺ fₙ(x) → f(x) for all x ∈ X

Banach-Alaoglu: Unit ball in X* is weak* compact
```

---

## Agent Coordination

### Problem Routing

| Problem Type | Primary Agent | Notes |
|--------------|---------------|-------|
| Banach spaces | functional-analyst | Completeness |
| Hilbert spaces | functional-analyst | Inner products |
| Bounded operators | functional-analyst | Norm, spectrum |
| Compact operators | functional-analyst | Fredholm |
| L^p spaces | measure-theorist | Construction |
| PDEs | functional-analyst | Sobolev spaces |

---

## Output Format

### Space Analysis
```
SPACE ANALYSIS
═══════════════════════════════════════════════════════════════

SPACE: [name/description]
NORM: ‖·‖ = [formula]

PROPERTIES
─────────────────────────────────────────
□ Complete (Banach): [Yes/No + proof]
□ Hilbert: [Yes/No]
□ Reflexive: [Yes/No]
□ Separable: [Yes/No]

DUAL SPACE
─────────────────────────────────────────
[Identification]
```

### Spectrum Computation
```
SPECTRAL ANALYSIS
═══════════════════════════════════════════════════════════════

OPERATOR: T: X → X
DEFINITION: [how T acts]

SPECTRUM
─────────────────────────────────────────
σ(T) = [set]

Point spectrum: σ_p(T) = [eigenvalues]
Continuous spectrum: [if applicable]
Residual spectrum: [if applicable]

SPECTRAL RADIUS
─────────────────────────────────────────
r(T) = [value]
```

---

## Examples

### Example: Spectrum of shift operator

```
/functional-analysis spectrum "right shift on ℓ²"

SPECTRAL ANALYSIS
═══════════════════════════════════════════════════════════════

OPERATOR: S: ℓ² → ℓ²
DEFINITION: S(x₁, x₂, x₃, ...) = (0, x₁, x₂, x₃, ...)

PROPERTIES
─────────────────────────────────────────
□ ‖S‖ = 1 (isometry)
□ S is not normal (SS* ≠ S*S)
□ S* is left shift: S*(x₁, x₂, ...) = (x₂, x₃, ...)

POINT SPECTRUM
─────────────────────────────────────────
Sx = λx ⟹ (0, x₁, x₂, ...) = (λx₁, λx₂, ...)
⟹ λx₁ = 0, x₁ = λx₂, x₂ = λx₃, ...

If λ ≠ 0: x₁ = 0 ⟹ all xₙ = 0
σ_p(S) = ∅

SPECTRUM
─────────────────────────────────────────
σ(S) ⊆ {|λ| ≤ 1} since ‖S‖ = 1

For |λ| < 1: Check (S - λI)⁻¹
  Need to solve (0, x₁, x₂, ...) - λ(x₁, x₂, ...) = (y₁, y₂, ...)
  -λx₁ = y₁, x₁ - λx₂ = y₂, ...
  Solution exists and bounded for |λ| < 1

For |λ| = 1: S - λI not surjective
  Range of S - λI doesn't contain (1, 0, 0, ...)

RESULT
─────────────────────────────────────────
σ(S) = {λ : |λ| ≤ 1} (closed unit disk)
σ_p(S) = ∅
σ_c(S) = {λ : |λ| = 1} (unit circle)
σ_r(S) = {λ : |λ| < 1} (open unit disk)
```

---

## References

- Rudin - Functional Analysis
- Conway - A Course in Functional Analysis
- Kreyszig - Introductory Functional Analysis with Applications
- Brezis - Functional Analysis, Sobolev Spaces and PDEs
