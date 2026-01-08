# Mathematical Physics Skill

## Overview

This skill provides methodology for mathematical physics, including classical mechanics, continuum mechanics, electromagnetism, thermodynamics, and relativity. It coordinates with the mathematical-physicist agent.

## Invocation

```
/mathematical-physics [subcommand] [arguments]
```

## Subcommands

### `/mathematical-physics lagrangian <system>`
Derive Lagrangian and equations of motion.

### `/mathematical-physics hamiltonian <system>`
Derive Hamiltonian and canonical equations.

### `/mathematical-physics conservation <system>`
Find conservation laws from symmetries.

### `/mathematical-physics maxwell <configuration>`
Solve Maxwell's equations for given configuration.

### `/mathematical-physics fluid <flow>`
Analyze fluid flow (Euler, Navier-Stokes).

### `/mathematical-physics relativity <spacetime>`
Analyze relativistic systems.

---

## Methodology

### Lagrangian Mechanics

```
LAGRANGIAN MECHANICS
═══════════════════════════════════════════════════════════════

STEP 1: CHOOSE COORDINATES
─────────────────────────────────────────
Generalized coordinates q = (q₁,...,qₙ)
Account for constraints.

STEP 2: COMPUTE T AND V
─────────────────────────────────────────
Kinetic energy T = ½m|ṙ|² = T(q, q̇)
Potential energy V = V(q)

STEP 3: FORM LAGRANGIAN
─────────────────────────────────────────
L = T - V

STEP 4: EULER-LAGRANGE
─────────────────────────────────────────
d/dt(∂L/∂q̇ᵢ) - ∂L/∂qᵢ = 0

STEP 5: IDENTIFY CONSERVED QUANTITIES
─────────────────────────────────────────
Cyclic coordinate qᵢ (∂L/∂qᵢ = 0) → pᵢ = ∂L/∂q̇ᵢ conserved
```

### Conservation Laws

```
NOETHER'S THEOREM
═══════════════════════════════════════════════════════════════

SYMMETRY → CONSERVATION LAW
─────────────────────────────────────────
Time translation → Energy
Space translation → Linear momentum
Rotation → Angular momentum
Boost → Center of mass motion

FINDING CONSERVED QUANTITIES
─────────────────────────────────────────
1. Identify symmetry transformation
2. Compute Noether current
3. Verify dJ/dt = 0
```

### Maxwell's Equations

```
MAXWELL'S EQUATIONS
═══════════════════════════════════════════════════════════════

EQUATIONS
─────────────────────────────────────────
∇·E = ρ/ε₀
∇·B = 0
∇×E = -∂B/∂t
∇×B = μ₀J + μ₀ε₀∂E/∂t

SOLUTION STRATEGY
─────────────────────────────────────────
1. Identify symmetry (static, planar, cylindrical, spherical)
2. Choose appropriate coordinates
3. Apply boundary conditions
4. Use potentials if helpful: B = ∇×A, E = -∇φ - ∂A/∂t
```

---

## Output Format

### Physical Analysis
```
PHYSICAL ANALYSIS
═══════════════════════════════════════════════════════════════

SYSTEM
─────────────────────────────────────────
[Physical description]

COORDINATES
─────────────────────────────────────────
[Generalized coordinates with justification]

LAGRANGIAN/HAMILTONIAN
─────────────────────────────────────────
L = [expression]
H = [expression]

EQUATIONS OF MOTION
─────────────────────────────────────────
[Derived equations]

CONSERVATION LAWS
─────────────────────────────────────────
[Conserved quantities from symmetries]

SOLUTION
─────────────────────────────────────────
[Analytical solution or qualitative behavior]
```

---

## Examples

### Example: Simple pendulum

```
/mathematical-physics lagrangian "simple pendulum"

LAGRANGIAN ANALYSIS: Simple Pendulum
═══════════════════════════════════════════════════════════════

SYSTEM
─────────────────────────────────────────
Mass m on massless rod of length ℓ, gravity g.

COORDINATE
─────────────────────────────────────────
θ = angle from vertical (1 DOF)

KINEMATICS
─────────────────────────────────────────
Position: (ℓ sin θ, -ℓ cos θ)
Velocity: |v|² = ℓ²θ̇²

ENERGIES
─────────────────────────────────────────
T = ½mℓ²θ̇²
V = -mgℓ cos θ (taking θ = π/2 as reference)

LAGRANGIAN
─────────────────────────────────────────
L = T - V = ½mℓ²θ̇² + mgℓ cos θ

EULER-LAGRANGE
─────────────────────────────────────────
d/dt(mℓ²θ̇) - (-mgℓ sin θ) = 0
mℓ²θ̈ + mgℓ sin θ = 0
θ̈ + (g/ℓ) sin θ = 0

CONSERVATION
─────────────────────────────────────────
Energy: E = ½mℓ²θ̇² - mgℓ cos θ = constant
(L independent of t explicitly)

SMALL OSCILLATIONS
─────────────────────────────────────────
sin θ ≈ θ: θ̈ + (g/ℓ)θ = 0
SHM with period T = 2π√(ℓ/g)
```

---

## References

- Goldstein, Poole, Safko (2002). Classical Mechanics
- Landau & Lifshitz - Course of Theoretical Physics
- Jackson (1999). Classical Electrodynamics
