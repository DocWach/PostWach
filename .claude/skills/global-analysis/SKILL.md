# Global Analysis Skill

## Overview

This skill provides methodology for global analysis on manifolds, including differential operators, index theory, and spectral geometry. It coordinates with the global-analyst agent.

## Invocation

```
/global-analysis [subcommand] [arguments]
```

## Subcommands

### `/global-analysis operator <operator>`
Analyze a differential operator on a manifold.

### `/global-analysis index <operator>`
Compute index using Atiyah-Singer theorem.

### `/global-analysis spectrum <operator>`
Analyze spectrum and eigenvalues.

### `/global-analysis heat-kernel <operator>`
Compute heat kernel expansion.

### `/global-analysis hodge <manifold>`
Apply Hodge theory.

### `/global-analysis variational <functional>`
Analyze variational problem on manifold.

---

## Methodology

### Elliptic Operator Analysis

```
ELLIPTIC OPERATOR ANALYSIS
═══════════════════════════════════════════════════════════════

STEP 1: SYMBOL COMPUTATION
─────────────────────────────────────────
For D = Σ aα(x)∂^α:
σ(D)(x,ξ) = Σ_{|α|=m} aα(x)ξ^α

Elliptic: σ(D)(x,ξ) ≠ 0 for ξ ≠ 0

STEP 2: FREDHOLM PROPERTY
─────────────────────────────────────────
On compact M: elliptic ⟹ Fredholm
- ker(D) finite-dimensional
- coker(D) finite-dimensional
- ind(D) = dim ker - dim coker

STEP 3: INDEX COMPUTATION
─────────────────────────────────────────
Atiyah-Singer: ind(D) = ∫_M ch(σ(D)) · Td(M)
```

### Index Theorem Applications

```
INDEX THEOREM APPLICATIONS
═══════════════════════════════════════════════════════════════

DE RHAM COMPLEX
─────────────────────────────────────────
d + d*: Ω^{even} → Ω^{odd}
ind = χ(M) (Euler characteristic)

SIGNATURE OPERATOR
─────────────────────────────────────────
d + d*: Ω⁺ → Ω⁻ (self-dual/anti-self-dual)
ind = sign(M) (signature)

DIRAC OPERATOR
─────────────────────────────────────────
∂̸: S⁺ → S⁻
ind = Â(M) (A-hat genus)

DOLBEAULT COMPLEX
─────────────────────────────────────────
∂̄: Ω^{0,even} → Ω^{0,odd}
ind = χ(M, O) (holomorphic Euler char)
```

---

## Output Format

### Global Analysis Report
```
GLOBAL ANALYSIS
═══════════════════════════════════════════════════════════════

OPERATOR/MANIFOLD
─────────────────────────────────────────
[Specification]

ELLIPTICITY
─────────────────────────────────────────
Symbol: [expression]
Type: [elliptic/parabolic/hyperbolic]

INDEX/SPECTRUM
─────────────────────────────────────────
[Index computation or spectral data]

TOPOLOGICAL IMPLICATIONS
─────────────────────────────────────────
[Characteristic classes, invariants]
```

---

## Examples

### Example: Laplacian on Torus

```
/global-analysis spectrum "Laplacian on T²"

SPECTRAL ANALYSIS: Laplacian on T²
═══════════════════════════════════════════════════════════════

MANIFOLD
─────────────────────────────────────────
T² = ℝ²/ℤ² (flat torus)
Metric: ds² = dx² + dy²

OPERATOR
─────────────────────────────────────────
Δ = -∂²/∂x² - ∂²/∂y²
Type: Elliptic (symbol |ξ|²)

SPECTRUM
─────────────────────────────────────────
Eigenvalues: λ_{m,n} = 4π²(m² + n²)
for (m,n) ∈ ℤ²

Eigenfunctions: e^{2πi(mx + ny)}

MULTIPLICITY
─────────────────────────────────────────
mult(λ) = #{(m,n) : m² + n² = λ/4π²}
= r₂(k) (sum of two squares function)

WEYL'S LAW
─────────────────────────────────────────
N(λ) ~ (Area/4π)λ = λ/4π as λ → ∞

HEAT KERNEL
─────────────────────────────────────────
K_t(x,y) = Σ_{m,n} e^{-4π²(m²+n²)t} e^{2πi(m(x₁-y₁)+n(x₂-y₂))}

tr(e^{-tΔ}) = 1/4πt · (1 + O(e^{-c/t}))
```

### Example: Index of Dirac on S⁴

```
/global-analysis index "Dirac on S⁴"

INDEX COMPUTATION: Dirac on S⁴
═══════════════════════════════════════════════════════════════

MANIFOLD
─────────────────────────────────────────
S⁴ = 4-sphere with round metric
Spin structure: unique

OPERATOR
─────────────────────────────────────────
∂̸: Γ(S⁺) → Γ(S⁻)
S± = positive/negative spinor bundles
rank(S±) = 2

ATIYAH-SINGER
─────────────────────────────────────────
ind(∂̸) = ∫_{S⁴} Â(S⁴)

Â(S⁴) = 1 - p₁/24 + ...

For S⁴: p₁ = 0 (conformally flat)

RESULT
─────────────────────────────────────────
ind(∂̸) = 0

INTERPRETATION
─────────────────────────────────────────
S⁴ has positive scalar curvature
By Lichnerowicz: ker(∂̸) = 0
Hence both ker(∂̸⁺) = ker(∂̸⁻) = 0
```

---

## References

- Berline, Getzler, Vergne (1992). Heat Kernels and Dirac Operators
- Gilkey, P. (1995). Invariance Theory, the Heat Equation, and the Atiyah-Singer Index Theorem
- Lawson & Michelsohn (1989). Spin Geometry
