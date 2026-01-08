# Numerical Methods Skill

## Overview

This skill provides methodology for numerical analysis, including interpolation, quadrature, linear algebra, ODE/PDE solvers, and error analysis. It coordinates with the numerical-analyst agent.

## Invocation

```
/numerical-methods [subcommand] [arguments]
```

## Subcommands

### `/numerical-methods interpolate <data>`
Construct interpolating polynomial or spline.

### `/numerical-methods integrate <function> <interval>`
Apply numerical quadrature.

### `/numerical-methods solve-linear <system>`
Solve linear systems (direct or iterative).

### `/numerical-methods ode <equation> <method>`
Solve ODE using specified numerical method.

### `/numerical-methods pde <equation> <method>`
Discretize and solve PDE.

### `/numerical-methods error <method>`
Analyze error and convergence.

---

## Methodology

### Interpolation Pipeline

```
INTERPOLATION
═══════════════════════════════════════════════════════════════

POLYNOMIAL INTERPOLATION
─────────────────────────────────────────
Given (x₀,y₀),...,(xₙ,yₙ):

Lagrange: p(x) = Σ yᵢ ∏_{j≠i} (x-xⱼ)/(xᵢ-xⱼ)

Newton: p(x) = Σ f[x₀,...,xₖ] ∏_{j<k}(x-xⱼ)

Error: |f(x) - p(x)| ≤ |f^{(n+1)}(ξ)|/(n+1)! |∏(x-xᵢ)|

NODE SELECTION
─────────────────────────────────────────
Equispaced: Runge phenomenon near endpoints
Chebyshev: xₖ = cos((2k+1)π/(2n+2)), near-optimal

SPLINES
─────────────────────────────────────────
Cubic spline: Piecewise cubic, C² continuous
Natural: S''(a) = S''(b) = 0
```

### ODE Solver Pipeline

```
ODE NUMERICAL METHODS
═══════════════════════════════════════════════════════════════

EULER'S METHOD
─────────────────────────────────────────
yₙ₊₁ = yₙ + h f(tₙ, yₙ)
Order 1, conditionally stable

RK4
─────────────────────────────────────────
k₁ = f(tₙ, yₙ)
k₂ = f(tₙ + h/2, yₙ + hk₁/2)
k₃ = f(tₙ + h/2, yₙ + hk₂/2)
k₄ = f(tₙ + h, yₙ + hk₃)
yₙ₊₁ = yₙ + (h/6)(k₁ + 2k₂ + 2k₃ + k₄)
Order 4

STABILITY ANALYSIS
─────────────────────────────────────────
Test equation: y' = λy
Stability region: |yₙ₊₁/yₙ| ≤ 1

A-stable: Entire left half-plane stable
```

### Error Analysis

```
ERROR ANALYSIS
═══════════════════════════════════════════════════════════════

LOCAL TRUNCATION ERROR
─────────────────────────────────────────
Error from one step with exact data.

GLOBAL ERROR
─────────────────────────────────────────
Accumulated error after n steps.

ORDER OF ACCURACY
─────────────────────────────────────────
Method order p if global error = O(hᵖ).

STABILITY + CONSISTENCY → CONVERGENCE
─────────────────────────────────────────
Lax Equivalence Theorem (for linear problems).
```

---

## Output Format

### Numerical Solution Report
```
NUMERICAL SOLUTION
═══════════════════════════════════════════════════════════════

PROBLEM
─────────────────────────────────────────
[Equation/System]

METHOD
─────────────────────────────────────────
[Algorithm with parameters]

ERROR ANALYSIS
─────────────────────────────────────────
Order: [value]
Stability: [conditions]
Error bound: [expression]

RESULTS
─────────────────────────────────────────
[Solution values or convergence data]
```

---

## Examples

### Example: Trapezoidal rule error

```
/numerical-methods error "trapezoidal rule"

ERROR ANALYSIS: Trapezoidal Rule
═══════════════════════════════════════════════════════════════

RULE
─────────────────────────────────────────
∫ₐᵇ f(x)dx ≈ (b-a)/2 [f(a) + f(b)]

LOCAL ERROR
─────────────────────────────────────────
E = -(b-a)³/12 f''(ξ) = O(h³)

COMPOSITE (n subintervals)
─────────────────────────────────────────
∫ₐᵇ f ≈ h/2 [f(a) + 2Σf(xᵢ) + f(b)]

Global error: -(b-a)h²/12 f''(ξ) = O(h²)

CONVERGENCE
─────────────────────────────────────────
Second-order accurate.
Halving h reduces error by factor of 4.
```

---

## References

- Trefethen & Bau (1997). Numerical Linear Algebra
- Hairer, Nørsett, Wanner (1993). Solving ODEs I
- LeVeque (2007). Finite Difference Methods
