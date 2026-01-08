# Optimization Skill

## Overview

This skill provides methodology for optimization, including calculus of variations, optimal control, linear/nonlinear programming, and convex optimization. It coordinates with the optimization-specialist agent.

## Invocation

```
/optimization [subcommand] [arguments]
```

## Subcommands

### `/optimization variational <functional>`
Derive Euler-Lagrange equations for variational problems.

### `/optimization control <system> <cost>`
Apply Pontryagin or HJB for optimal control.

### `/optimization linear <program>`
Solve linear program (simplex or dual).

### `/optimization kkt <problem>`
Derive and solve KKT conditions.

### `/optimization convex <problem>`
Analyze convex optimization problem.

### `/optimization algorithm <problem> <method>`
Apply numerical optimization algorithm.

---

## Methodology

### Calculus of Variations

```
VARIATIONAL PROBLEM
═══════════════════════════════════════════════════════════════

PROBLEM: min J[y] = ∫ₐᵇ F(x, y, y') dx

EULER-LAGRANGE EQUATION
─────────────────────────────────────────
∂F/∂y - d/dx(∂F/∂y') = 0

SPECIAL CASES
─────────────────────────────────────────
F independent of y: ∂F/∂y' = constant
F independent of x: F - y'∂F/∂y' = constant (Beltrami)

CONSTRAINED (ISOPERIMETRIC)
─────────────────────────────────────────
min J[y] s.t. K[y] = ℓ
Use Lagrange multiplier: F - λG
```

### KKT Conditions

```
KKT CONDITIONS
═══════════════════════════════════════════════════════════════

PROBLEM
─────────────────────────────────────────
min f(x)
s.t. gᵢ(x) ≤ 0, hⱼ(x) = 0

CONDITIONS
─────────────────────────────────────────
1. Stationarity: ∇f + Σλᵢ∇gᵢ + Σμⱼ∇hⱼ = 0
2. Primal feasibility: gᵢ(x) ≤ 0, hⱼ(x) = 0
3. Dual feasibility: λᵢ ≥ 0
4. Complementary slackness: λᵢgᵢ(x) = 0

For convex problems: KKT ⟺ optimal
```

### Convex Optimization

```
CONVEX OPTIMIZATION
═══════════════════════════════════════════════════════════════

PROPERTIES
─────────────────────────────────────────
□ Local minimum = global minimum
□ KKT sufficient (not just necessary)
□ Strong duality (with Slater condition)

DUALITY
─────────────────────────────────────────
Lagrangian: L(x, λ, μ) = f + λ'g + μ'h
Dual: max_{λ≥0} min_x L(x, λ, μ)

p* = d* (strong duality)
```

---

## Output Format

### Optimization Solution
```
OPTIMIZATION SOLUTION
═══════════════════════════════════════════════════════════════

PROBLEM
─────────────────────────────────────────
[Objective and constraints]

METHOD
─────────────────────────────────────────
[E-L, KKT, LP, etc.]

OPTIMALITY CONDITIONS
─────────────────────────────────────────
[Necessary/sufficient conditions]

SOLUTION
─────────────────────────────────────────
x* = [optimal point]
f(x*) = [optimal value]

VERIFICATION
─────────────────────────────────────────
[Conditions satisfied]
```

---

## Examples

### Example: Lagrange multipliers

```
/optimization kkt "min x² + y² s.t. x + y = 1"

KKT SOLUTION
═══════════════════════════════════════════════════════════════

PROBLEM
─────────────────────────────────────────
min f(x,y) = x² + y²
s.t. h(x,y) = x + y - 1 = 0

LAGRANGIAN
─────────────────────────────────────────
L = x² + y² + λ(x + y - 1)

KKT CONDITIONS
─────────────────────────────────────────
∂L/∂x = 2x + λ = 0
∂L/∂y = 2y + λ = 0
x + y = 1

SOLUTION
─────────────────────────────────────────
2x = 2y ⟹ x = y
x + y = 1 ⟹ x = y = 1/2
λ = -1

x* = (1/2, 1/2)
f(x*) = 1/4 + 1/4 = 1/2

VERIFICATION
─────────────────────────────────────────
Hessian of f: 2I (positive definite)
Problem is convex → x* is global minimum.
```

---

## References

- Boyd & Vandenberghe (2004). Convex Optimization
- Nocedal & Wright (2006). Numerical Optimization
- Liberzon (2012). Calculus of Variations and Optimal Control
