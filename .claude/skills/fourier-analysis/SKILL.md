# Fourier Analysis Skill

## Overview

Methodology for Fourier analysis including series, transforms, and singular integrals.

## Invocation

```
/fourier-analysis [subcommand] [arguments]
```

## Subcommands

- `/fourier-analysis series <function>` - Compute Fourier series
- `/fourier-analysis transform <function>` - Compute Fourier transform
- `/fourier-analysis inverse <transform>` - Invert transform
- `/fourier-analysis convergence <series>` - Analyze convergence
- `/fourier-analysis singular <operator>` - Analyze singular integrals

## Key Formulas

```
FOURIER SERIES
f(x) = Σ cₙ e^{inx}
cₙ = (1/2π) ∫₀^{2π} f(x)e^{-inx} dx

FOURIER TRANSFORM
f̂(ξ) = ∫ f(x)e^{-ixξ} dx
f(x) = (2π)^{-n} ∫ f̂(ξ)e^{ixξ} dξ
```

## References

- Stein & Weiss (1971). Fourier Analysis on Euclidean Spaces
- Grafakos (2014). Classical Fourier Analysis
