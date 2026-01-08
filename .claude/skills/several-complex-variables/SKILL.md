# Several Complex Variables Skill

## Overview

This skill provides methodology for several complex variables, including holomorphic functions, domains of holomorphy, and the ∂̄-problem. It coordinates with the several-complex-variables-analyst agent.

## Invocation

```
/several-complex-variables [subcommand] [arguments]
```

## Subcommands

### `/several-complex-variables domain <domain>`
Analyze a domain in ℂⁿ.

### `/several-complex-variables pseudoconvex <domain>`
Check pseudoconvexity and compute Levi form.

### `/several-complex-variables dbar <form>`
Solve the ∂̄-problem.

### `/several-complex-variables extension <function>`
Analyze holomorphic extension properties.

### `/several-complex-variables stein <manifold>`
Check Stein property and apply Cartan theorems.

### `/several-complex-variables bergman <domain>`
Compute Bergman kernel and metric.

---

## Methodology

### Domain Classification

```
DOMAIN CLASSIFICATION
═══════════════════════════════════════════════════════════════

STEP 1: GEOMETRIC PROPERTIES
─────────────────────────────────────────
- Bounded/unbounded
- Smoothly bounded?
- Defining function ρ

STEP 2: CONVEXITY HIERARCHY
─────────────────────────────────────────
Convex ⟹ Strictly pseudoconvex ⟹ Pseudoconvex

Check Levi form:
L_ρ(z;w) = Σ (∂²ρ/∂zᵢ∂z̄ⱼ) wᵢw̄ⱼ

STEP 3: HOLOMORPHIC PROPERTIES
─────────────────────────────────────────
Domain of holomorphy ⟺ Pseudoconvex
Stein ⟺ Holomorphically convex + separation
```

### ∂̄-Problem Solution

```
∂̄-PROBLEM
═══════════════════════════════════════════════════════════════

PROBLEM: Given ∂̄f = 0, find u with ∂̄u = f

STEP 1: VERIFY COMPATIBILITY
─────────────────────────────────────────
∂̄f = 0 (necessary condition)

STEP 2: DOMAIN TYPE
─────────────────────────────────────────
Pseudoconvex → Hörmander L² estimates apply
Strictly pseudoconvex → C^∞ regularity

STEP 3: SOLVE
─────────────────────────────────────────
u exists with ∫|u|²e^{-φ} ≤ C∫|f|²e^{-φ}
for suitable plurisubharmonic weight φ
```

---

## Output Format

### SCV Analysis Report
```
SEVERAL COMPLEX VARIABLES ANALYSIS
═══════════════════════════════════════════════════════════════

DOMAIN
─────────────────────────────────────────
[Specification]

PSEUDOCONVEXITY
─────────────────────────────────────────
[Levi form, classification]

STEIN PROPERTY
─────────────────────────────────────────
[Yes/No, justification]

∂̄-COHOMOLOGY
─────────────────────────────────────────
[Vanishing or non-vanishing]

FUNCTION THEORY
─────────────────────────────────────────
[Key properties]
```

---

## Examples

### Example: Hartogs Triangle

```
/several-complex-variables domain "Hartogs triangle"

ANALYSIS: Hartogs Triangle
═══════════════════════════════════════════════════════════════

DOMAIN
─────────────────────────────────────────
H = {(z,w) ∈ ℂ² : |z| < |w| < 1}

PROPERTIES
─────────────────────────────────────────
Bounded: Yes
Simply connected: No (π₁ = ℤ)
Smoothly bounded: No (corner at origin)

PSEUDOCONVEXITY
─────────────────────────────────────────
Pseudoconvex: Yes
Strictly pseudoconvex: No (flat boundary parts)

HARTOGS PHENOMENON
─────────────────────────────────────────
Every holomorphic function on H extends to
{(z,w) : |w| < 1}

This demonstrates the envelope of holomorphy
is strictly larger than H.

∂̄-COHOMOLOGY
─────────────────────────────────────────
H^{0,1}(H) ≠ 0 (non-trivial, not Stein)
```

---

## References

- Hörmander, L. (1990). An Introduction to Complex Analysis in Several Variables
- Krantz, S. (2001). Function Theory of Several Complex Variables
- Range, R.M. (1986). Holomorphic Functions and Integral Representations
