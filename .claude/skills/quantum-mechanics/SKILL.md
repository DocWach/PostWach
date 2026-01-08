# Quantum Mechanics Skill

## Overview

Methodology for mathematical quantum mechanics, including operator theory, spectral analysis, and scattering.

## Invocation

```
/quantum-mechanics [subcommand] [arguments]
```

## Subcommands

- `/quantum-mechanics hamiltonian <system>` - Analyze Hamiltonian
- `/quantum-mechanics spectrum <operator>` - Compute spectrum
- `/quantum-mechanics eigenstates <operator>` - Find eigenstates
- `/quantum-mechanics dynamics <initial>` - Time evolution
- `/quantum-mechanics scattering <potential>` - Scattering analysis
- `/quantum-mechanics uncertainty <observables>` - Uncertainty relations

## Key Methods

```
SPECTRAL ANALYSIS
1. Identify domain D(H)
2. Check self-adjointness
3. Classify spectrum (point, continuous, residual)
4. Find eigenfunctions/generalized eigenfunctions

PERTURBATION THEORY
H = H₀ + λV
E_n(λ) = E_n^{(0)} + λE_n^{(1)} + λ²E_n^{(2)} + ...

VARIATIONAL METHOD
E₀ ≤ ⟨ψ|H|ψ⟩/⟨ψ|ψ⟩ for any trial ψ
```

## References

- Reed & Simon. Methods of Modern Mathematical Physics
- Hall (2013). Quantum Theory for Mathematicians
