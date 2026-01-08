# Phase 6: Applied Mathematics

## Overview

Phase 6 implements the MSC2020 coverage for applied mathematics, spanning MSC categories 34, 35, 37, 49, 60, 62, 65, 70-83, and 90. This phase provides comprehensive agents for differential equations, numerical methods, probability and statistics, optimization, and mathematical physics.

## MSC Categories Covered

| MSC | Category | Agent(s) |
|-----|----------|----------|
| 34 | Ordinary differential equations | `ode-dynamicist` |
| 35 | Partial differential equations | `pde-specialist` |
| 37 | Dynamical systems and ergodic theory | `ode-dynamicist` |
| 49 | Calculus of variations and optimal control | `optimization-specialist` |
| 60 | Probability theory and stochastic processes | `probabilist` |
| 62 | Statistics | `probabilist` |
| 65 | Numerical analysis | `numerical-analyst` |
| 70 | Mechanics of particles and systems | `mathematical-physicist` |
| 74 | Mechanics of deformable solids | `mathematical-physicist` |
| 76 | Fluid mechanics | `mathematical-physicist` |
| 78 | Optics, electromagnetic theory | `mathematical-physicist` |
| 80 | Classical thermodynamics, heat transfer | `mathematical-physicist` |
| 82 | Statistical mechanics | `mathematical-physicist` |
| 83 | Relativity and gravitational theory | `mathematical-physicist` |
| 90 | Operations research, mathematical programming | `optimization-specialist` |

## Agents (6)

### `ode-dynamicist` (MSC 34, 37)
ODE and dynamical systems specialist covering existence/uniqueness, stability, bifurcations, and chaos.

**Capabilities:**
- Existence and uniqueness theorems
- Linear systems and matrix exponentials
- Phase portrait analysis
- Stability (Lyapunov methods)
- Bifurcation theory (saddle-node, Hopf)
- Chaos and strange attractors
- Ergodic theory

**Key Theorems:**
- Picard-Lindelöf Theorem
- Hartman-Grobman Theorem
- Poincaré-Bendixson Theorem
- Lyapunov Stability Theorems
- Birkhoff Ergodic Theorem

### `pde-specialist` (MSC 35)
PDE specialist covering classification, well-posedness, weak solutions, and solution techniques.

**Capabilities:**
- PDE classification (elliptic, parabolic, hyperbolic)
- Well-posedness (Hadamard)
- Separation of variables
- Method of characteristics
- Green's functions
- Weak solutions and Sobolev spaces
- Variational methods (Lax-Milgram)

**Key Theorems:**
- Maximum Principles
- Harnack's Inequality
- Sobolev Embedding Theorems
- Lax-Milgram Theorem
- Regularity Theory

### `numerical-analyst` (MSC 65)
Numerical analysis specialist covering approximation, linear algebra, ODEs, and PDEs.

**Capabilities:**
- Interpolation (Lagrange, Newton, splines)
- Numerical quadrature (Newton-Cotes, Gauss)
- Numerical linear algebra (LU, QR, iterative)
- ODE solvers (Runge-Kutta, multistep)
- PDE discretization (finite differences, FEM)
- Error and stability analysis

**Key Theorems:**
- Lax Equivalence Theorem
- Convergence of Runge-Kutta Methods
- CFL Condition
- Finite Element Error Estimates

### `probabilist` (MSC 60, 62)
Probability and statistics specialist covering theory, stochastic processes, and inference.

**Capabilities:**
- Probability spaces and random variables
- Expectation and moments
- Convergence modes
- Laws of large numbers
- Central limit theorem
- Markov chains and martingales
- Brownian motion
- Statistical inference (MLE, Bayesian)

**Key Theorems:**
- Strong/Weak Law of Large Numbers
- Central Limit Theorem
- Martingale Convergence Theorem
- Optional Stopping Theorem
- Cramér-Rao Bound

### `optimization-specialist` (MSC 49, 90)
Optimization specialist covering calculus of variations, optimal control, and mathematical programming.

**Capabilities:**
- Euler-Lagrange equations
- Optimal control (Pontryagin, HJB)
- Linear programming (simplex, duality)
- Nonlinear programming (KKT conditions)
- Convex optimization
- Lagrangian duality
- Numerical algorithms (gradient, Newton)

**Key Theorems:**
- Euler-Lagrange Equations
- Pontryagin Maximum Principle
- KKT Conditions
- Strong Duality (Slater)
- Convergence of Gradient Descent

### `mathematical-physicist` (MSC 70-83)
Mathematical physics specialist covering mechanics, field theories, and relativity.

**Capabilities:**
- Classical mechanics (Lagrangian, Hamiltonian)
- Conservation laws (Noether)
- Continuum mechanics (elasticity, fluids)
- Electromagnetism (Maxwell)
- Thermodynamics and statistical mechanics
- Special and general relativity

**Key Equations:**
- Euler-Lagrange/Hamilton's Equations
- Navier-Stokes Equations
- Maxwell's Equations
- Einstein Field Equations
- Boltzmann Distribution

## Skills (6)

### `ode-dynamical-systems`
Methodology for ODE and dynamical systems analysis.

**Subcommands:**
- `/ode-dynamical-systems solve <equation>` - Solve ODEs
- `/ode-dynamical-systems stability <system>` - Stability analysis
- `/ode-dynamical-systems phase-portrait <system>` - Phase portraits
- `/ode-dynamical-systems bifurcation <system>` - Bifurcation analysis
- `/ode-dynamical-systems linearize <system>` - Linearization
- `/ode-dynamical-systems lyapunov <system>` - Lyapunov functions

### `pde-methods`
Methodology for PDE analysis and solution.

**Subcommands:**
- `/pde-methods classify <equation>` - PDE classification
- `/pde-methods solve <equation>` - Solve PDEs
- `/pde-methods weak-form <equation>` - Weak formulation
- `/pde-methods separation <equation>` - Separation of variables
- `/pde-methods characteristics <equation>` - Method of characteristics
- `/pde-methods maximum-principle <equation>` - Maximum principles

### `numerical-methods`
Methodology for numerical analysis and computation.

**Subcommands:**
- `/numerical-methods interpolate <data>` - Interpolation
- `/numerical-methods integrate <function>` - Numerical quadrature
- `/numerical-methods solve-linear <system>` - Linear systems
- `/numerical-methods ode <equation>` - ODE solvers
- `/numerical-methods pde <equation>` - PDE discretization
- `/numerical-methods error <method>` - Error analysis

### `probability-statistics`
Methodology for probability and statistical analysis.

**Subcommands:**
- `/probability-statistics distribution <spec>` - Distribution analysis
- `/probability-statistics expectation <expression>` - Expectations
- `/probability-statistics limit-theorem <sequence>` - Limit theorems
- `/probability-statistics markov <chain>` - Markov chains
- `/probability-statistics inference <data>` - Statistical inference
- `/probability-statistics test <hypothesis>` - Hypothesis testing

### `optimization`
Methodology for optimization problems.

**Subcommands:**
- `/optimization variational <functional>` - Calculus of variations
- `/optimization control <system>` - Optimal control
- `/optimization linear <program>` - Linear programming
- `/optimization kkt <problem>` - KKT conditions
- `/optimization convex <problem>` - Convex optimization
- `/optimization algorithm <problem>` - Numerical algorithms

### `mathematical-physics`
Methodology for mathematical physics problems.

**Subcommands:**
- `/mathematical-physics lagrangian <system>` - Lagrangian mechanics
- `/mathematical-physics hamiltonian <system>` - Hamiltonian mechanics
- `/mathematical-physics conservation <system>` - Conservation laws
- `/mathematical-physics maxwell <configuration>` - Electromagnetism
- `/mathematical-physics fluid <flow>` - Fluid dynamics
- `/mathematical-physics relativity <spacetime>` - Relativity

## Worker Type

### `applied-math-specialist`
Expert worker coordinating all Phase 6 agents for comprehensive applied mathematics problems.

**Capabilities:**
- Differential equations (ODEs, PDEs)
- Numerical methods and computation
- Probability and statistics
- Optimization (variational, LP, convex)
- Mathematical physics

## Swarm

### `applied-mathematics`
Comprehensive swarm for applied mathematics problems across all six agents.

**Workflow Stages:**
1. **problem-classification** - Identify problem domain
2. **model-formulation** - Formulate mathematical model
3. **method-selection** - Choose solution method
4. **solution-computation** - Compute solutions
5. **analysis-verification** - Verify and analyze
6. **interpretation** - Physical interpretation

## Directory Structure

```
.claude/
├── agents/
│   └── mathematics/
│       └── applied/
│           ├── ode-dynamicist.md
│           ├── pde-specialist.md
│           ├── numerical-analyst.md
│           ├── probabilist.md
│           ├── optimization-specialist.md
│           ├── mathematical-physicist.md
│           └── README.md (this file)
├── skills/
│   ├── ode-dynamical-systems/
│   │   └── SKILL.md
│   ├── pde-methods/
│   │   └── SKILL.md
│   ├── numerical-methods/
│   │   └── SKILL.md
│   ├── probability-statistics/
│   │   └── SKILL.md
│   ├── optimization/
│   │   └── SKILL.md
│   └── mathematical-physics/
│       └── SKILL.md
└── ...

.hive-mind/
└── config/
    ├── workers.json   (applied-math-specialist added)
    └── swarms.json    (applied-mathematics added)
```

## Usage Examples

### Stability Analysis
```
User: Analyze stability of ẋ = x(1-x)(x-a) for 0 < a < 1

Response flow:
1. ode-dynamicist finds equilibria: x* = 0, a, 1
2. Linearizes at each equilibrium
3. Classifies stability from eigenvalues
4. Constructs bifurcation diagram in a
```

### Heat Equation
```
User: Solve uₜ = uₓₓ on [0,π] with u(0)=u(π)=0, u(x,0)=sin(x)

Response flow:
1. pde-specialist classifies as parabolic
2. Applies separation of variables
3. Finds eigenvalues λₙ = n²
4. Computes u(x,t) = sin(x)e^{-t}
```

### Monte Carlo
```
User: Estimate π using Monte Carlo simulation

Response flow:
1. numerical-analyst designs simulation
2. probabilist provides convergence rate √n
3. Implements and runs simulation
4. Provides confidence interval for estimate
```

### Optimal Control
```
User: Minimize ∫₀¹ (x² + u²)dt with ẋ = u, x(0)=1, x(1)=0

Response flow:
1. optimization-specialist sets up Hamiltonian
2. Applies Pontryagin principle
3. Solves two-point BVP
4. Finds optimal u* and trajectory x*
```

## Cross-Domain Integration

Phase 6 agents integrate with:
- **Phase 1 (Foundations)**: Logic for rigorous proofs
- **Phase 3 (Algebra)**: Linear algebra for systems
- **Phase 4 (Analysis)**: Functional analysis for PDEs
- **Phase 5 (Topology/Geometry)**: Manifolds, differential forms
- **Future phases**: Computational mathematics, data science

## Key Concepts

### Differential Equations
- Existence, uniqueness, continuation
- Stability (Lyapunov, linearization)
- Bifurcations and qualitative changes
- Well-posedness (Hadamard)

### Numerical Analysis
- Truncation vs roundoff error
- Stability and convergence
- Condition numbers
- Order of accuracy

### Probability & Statistics
- Convergence modes
- Limit theorems
- Bayesian vs frequentist
- Markov property

### Optimization
- Necessary vs sufficient conditions
- Duality theory
- Convexity advantages
- Algorithm convergence

### Mathematical Physics
- Variational principles
- Conservation from symmetry
- Field equations
- Dimensional analysis

## References

- Strogatz, S. (2015). Nonlinear Dynamics and Chaos
- Evans, L.C. (2010). Partial Differential Equations
- Trefethen, L.N., Bau, D. (1997). Numerical Linear Algebra
- Durrett, R. (2019). Probability: Theory and Examples
- Boyd, S., Vandenberghe, L. (2004). Convex Optimization
- Goldstein, H. et al. (2002). Classical Mechanics
