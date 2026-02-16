# 5. Computational Demonstration

## Section Purpose
Verify key isomorphisms computationally and demonstrate degradation.

## Outline

### 5.1 Setup
- Python implementation of state-space models
- Simulation via scipy ODE integration
- Parameters: M=1, B=0.5, K=2 (mechanical); L=1, R=0.5, C=0.5 (electrical, mapped)

### 5.2 Demo 1: MSD/RLC Continuous Isomorphism
- Step response, impulse response, sinusoidal forcing
- Output overlay showing D=0 under variable mapping
- Symbolic verification: identical transfer functions (sympy)

### 5.3 Demo 2: Discretization Degradation
- Euler, RK4, exact discretization at varying dt
- D vs. dt curves showing O(dt), O(dt^4), D=0 respectively
- Implication: method choice determines whether isomorphism is preserved

### 5.4 Demo 3: Partial Isomorphism (Electrical-Thermal)
- Full RLC vs. thermal RC: D > 0 (missing inductance)
- RC-only vs. thermal RC: D = 0 (restricted subcategory)
- Quantitative characterization of partial homomorphism

### 5.5 Discussion of Results
- Connection to VMMC types
- Implications for verification model selection
