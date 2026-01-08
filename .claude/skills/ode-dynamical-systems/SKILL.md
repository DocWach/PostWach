# ODE & Dynamical Systems Skill

## Overview

This skill provides methodology for ordinary differential equations and dynamical systems, including existence/uniqueness, stability analysis, bifurcation theory, and chaos. It coordinates with the ode-dynamicist agent.

## Invocation

```
/ode-dynamical-systems [subcommand] [arguments]
```

## Subcommands

### `/ode-dynamical-systems solve <equation>`
Solve ODEs using analytical or qualitative methods.

### `/ode-dynamical-systems stability <system>`
Analyze stability of equilibria.

### `/ode-dynamical-systems phase-portrait <system>`
Construct phase portrait for 2D systems.

### `/ode-dynamical-systems bifurcation <system> <parameter>`
Analyze bifurcations as parameter varies.

### `/ode-dynamical-systems linearize <system> <equilibrium>`
Linearize system about equilibrium.

### `/ode-dynamical-systems lyapunov <system>`
Find Lyapunov functions for stability.

---

## Methodology

### ODE Solution Pipeline

```
ODE ANALYSIS WORKFLOW
═══════════════════════════════════════════════════════════════

STEP 1: CLASSIFY EQUATION
─────────────────────────────────────────
□ Linear vs nonlinear
□ Autonomous vs non-autonomous
□ Order and dimension
□ Homogeneous vs forced

STEP 2: EXISTENCE/UNIQUENESS
─────────────────────────────────────────
Check Lipschitz condition for f(t,x):
  |f(t,x) - f(t,y)| ≤ L|x - y|

If satisfied: Unique local solution exists.

STEP 3: FIND EQUILIBRIA
─────────────────────────────────────────
Solve f(x*) = 0 for autonomous systems.

STEP 4: ANALYZE STABILITY
─────────────────────────────────────────
Linearize: A = Df(x*)
Eigenvalues determine local behavior.

STEP 5: GLOBAL ANALYSIS
─────────────────────────────────────────
Phase portrait, Lyapunov functions, invariant sets.
```

### Linear System Analysis

```
LINEAR SYSTEMS: ẋ = Ax
═══════════════════════════════════════════════════════════════

STEP 1: FIND EIGENVALUES
─────────────────────────────────────────
Solve det(A - λI) = 0

STEP 2: CLASSIFY (2D)
─────────────────────────────────────────
Real λ₁, λ₂:
  □ Both negative: Stable node
  □ Both positive: Unstable node
  □ Opposite signs: Saddle

Complex α ± iβ:
  □ α < 0: Stable spiral
  □ α = 0: Center
  □ α > 0: Unstable spiral

STEP 3: COMPUTE SOLUTION
─────────────────────────────────────────
x(t) = e^{At} x₀

For diagonal A: e^{At} = diag(e^{λ₁t}, e^{λ₂t},...)
```

### Stability Analysis

```
LYAPUNOV STABILITY ANALYSIS
═══════════════════════════════════════════════════════════════

STEP 1: CONSTRUCT CANDIDATE V(x)
─────────────────────────────────────────
Common choices:
□ Quadratic: V = x'Px for P > 0
□ Energy-like: V = T + U
□ Sum of squares

STEP 2: VERIFY POSITIVE DEFINITENESS
─────────────────────────────────────────
V(0) = 0 and V(x) > 0 for x ≠ 0

STEP 3: COMPUTE V̇
─────────────────────────────────────────
V̇ = ∇V · f(x)

STEP 4: CONCLUDE
─────────────────────────────────────────
□ V̇ ≤ 0: Stable
□ V̇ < 0 (x ≠ 0): Asymptotically stable
□ V̇ > 0: Unstable
```

### Bifurcation Analysis

```
BIFURCATION ANALYSIS
═══════════════════════════════════════════════════════════════

STEP 1: FIND EQUILIBRIA AS FUNCTION OF μ
─────────────────────────────────────────
Solve f(x, μ) = 0 for x = x*(μ)

STEP 2: TRACK EIGENVALUES
─────────────────────────────────────────
Compute λ(μ) = eigenvalues of Df(x*(μ), μ)

STEP 3: IDENTIFY BIFURCATION POINTS
─────────────────────────────────────────
□ Saddle-node: λ = 0 crosses
□ Hopf: Re(λ) = 0 with Im(λ) ≠ 0

STEP 4: DETERMINE TYPE
─────────────────────────────────────────
Compute normal form coefficients.
Supercritical vs subcritical.
```

---

## Output Format

### Stability Analysis
```
STABILITY ANALYSIS
═══════════════════════════════════════════════════════════════

SYSTEM: ẋ = f(x)

EQUILIBRIA
─────────────────────────────────────────
x* = [values]

LINEARIZATION AT x*
─────────────────────────────────────────
A = Df(x*) = [matrix]
Eigenvalues: λ₁ = ..., λ₂ = ...

CLASSIFICATION
─────────────────────────────────────────
[Node/Saddle/Spiral/Center]
[Stable/Unstable]

LYAPUNOV FUNCTION (if found)
─────────────────────────────────────────
V(x) = [expression]
V̇ = [expression] [≤0 / <0]
```

---

## Examples

### Example: Analyze ẋ = x - x³

```
/ode-dynamical-systems stability "dx/dt = x - x³"

STABILITY ANALYSIS: ẋ = x - x³
═══════════════════════════════════════════════════════════════

EQUILIBRIA
─────────────────────────────────────────
x - x³ = x(1 - x²) = 0
x* = 0, ±1

LINEARIZATION
─────────────────────────────────────────
f'(x) = 1 - 3x²

At x* = 0: f'(0) = 1 > 0 → Unstable
At x* = 1: f'(1) = -2 < 0 → Stable
At x* = -1: f'(-1) = -2 < 0 → Stable

PHASE PORTRAIT
─────────────────────────────────────────
←←← -1 →→→ 0 ←←← +1 →→→

Arrows point toward ±1, away from 0.

CONCLUSION
─────────────────────────────────────────
Supercritical pitchfork bifurcation structure.
Stable equilibria at x = ±1.
Unstable equilibrium at x = 0.
```

---

## References

- Strogatz, S. (2015). Nonlinear Dynamics and Chaos
- Hirsch, Smale, Devaney (2013). Differential Equations, Dynamical Systems, and an Introduction to Chaos
- Perko, L. (2001). Differential Equations and Dynamical Systems
