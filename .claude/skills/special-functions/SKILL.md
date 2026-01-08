# Special Functions Skill

## Overview

Methodology for special functions including orthogonal polynomials and hypergeometric functions.

## Invocation

```
/special-functions [subcommand] [arguments]
```

## Subcommands

- `/special-functions orthogonal <family>` - Analyze orthogonal polynomials
- `/special-functions hypergeometric <parameters>` - Evaluate hypergeometric functions
- `/special-functions bessel <order>` - Bessel function analysis
- `/special-functions gamma <expression>` - Gamma function identities
- `/special-functions asymptotic <function>` - Asymptotic expansions

## Key Functions

```
ORTHOGONAL POLYNOMIALS
Legendre: Pₙ(x), weight 1 on [-1,1]
Hermite: Hₙ(x), weight e^{-x²} on ℝ
Laguerre: Lₙ(x), weight e^{-x} on [0,∞)
Chebyshev: Tₙ(x), weight (1-x²)^{-1/2} on [-1,1]

HYPERGEOMETRIC
₂F₁(a,b;c;z) = Σ (a)ₙ(b)ₙ/(c)ₙn! z^n
```

## References

- NIST DLMF (dlmf.nist.gov)
- Andrews, Askey, Roy (1999). Special Functions
