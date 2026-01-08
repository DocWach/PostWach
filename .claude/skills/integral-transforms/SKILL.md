# Integral Transforms Skill

## Overview

Methodology for integral transforms including Laplace, Mellin, and Hankel transforms.

## Invocation

```
/integral-transforms [subcommand] [arguments]
```

## Subcommands

- `/integral-transforms laplace <function>` - Laplace transform
- `/integral-transforms inverse-laplace <transform>` - Inverse Laplace
- `/integral-transforms mellin <function>` - Mellin transform
- `/integral-transforms hankel <function>` - Hankel transform
- `/integral-transforms solve-ode <equation>` - Solve ODE via transforms

## Key Transforms

```
LAPLACE
ℒ{f}(s) = ∫₀^∞ f(t)e^{-st} dt

MELLIN
ℳ{f}(s) = ∫₀^∞ f(x)x^{s-1} dx

HANKEL
ℋᵥ{f}(s) = ∫₀^∞ f(r)Jᵥ(sr)r dr
```

## References

- Davies (2002). Integral Transforms and Their Applications
