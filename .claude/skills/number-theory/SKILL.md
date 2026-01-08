# Number Theory Skill

## Overview

This skill provides methodology for number-theoretic investigations across elementary, analytic, and algebraic number theory. It coordinates the specialized number theory agents to solve problems about integers, primes, and algebraic numbers.

## Invocation

```
/number-theory [subcommand] [arguments]
```

## Subcommands

### `/number-theory analyze <expression>`
Analyze number-theoretic properties of an expression or problem.

### `/number-theory factor <n>`
Factor an integer or analyze factorization in a number ring.

### `/number-theory prime <query>`
Investigate prime-related questions (distribution, primality, gaps).

### `/number-theory congruence <equation>`
Solve congruences and modular arithmetic problems.

### `/number-theory diophantine <equation>`
Analyze and solve Diophantine equations.

### `/number-theory field <specification>`
Study number fields and their arithmetic.

---

## Methodology

### Elementary Number Theory Pipeline

```
DIVISIBILITY ANALYSIS
═══════════════════════════════════════════════════════════════

INPUT CLASSIFICATION
─────────────────────────────────────────
1. Integer factorization problem
2. Divisibility question
3. GCD/LCM computation
4. Perfect number/amicable investigation

TECHNIQUE SELECTION
─────────────────────────────────────────
□ Trial division for small numbers
□ Euclidean algorithm for GCD
□ Fundamental theorem application
□ Multiplicative function properties

OUTPUT: Factorization, divisibility structure
```

### Congruence Solving Pipeline

```
MODULAR ARITHMETIC
═══════════════════════════════════════════════════════════════

PROBLEM ANALYSIS
─────────────────────────────────────────
1. Linear congruence: ax ≡ b (mod m)
2. System of congruences
3. Polynomial congruence
4. Order and primitive roots

SOLUTION METHOD
─────────────────────────────────────────
Linear: Check gcd(a,m) | b, then solve
System: Chinese Remainder Theorem
  - Check pairwise coprimality
  - Apply CRT construction
Polynomial: Hensel lifting if applicable
Order: Compute ord_m(a) via divisors of φ(m)

VERIFICATION
─────────────────────────────────────────
□ Substitute back into original
□ Check all solutions modulo lcm
□ Verify completeness of solution set
```

### Quadratic Reciprocity Pipeline

```
QUADRATIC RESIDUES
═══════════════════════════════════════════════════════════════

PROBLEM: Is a a quadratic residue mod p?

STEP 1: Compute Legendre symbol (a/p)
─────────────────────────────────────────
□ If p | a: (a/p) = 0
□ Use multiplicativity: (ab/p) = (a/p)(b/p)
□ Factor a into primes

STEP 2: Apply reciprocity laws
─────────────────────────────────────────
□ (2/p) = (-1)^((p²-1)/8)
□ (-1/p) = (-1)^((p-1)/2)
□ For odd primes q: (p/q)(q/p) = (-1)^((p-1)(q-1)/4)

STEP 3: Reduce to computable form
─────────────────────────────────────────
Chain of applications until resolved
```

### Analytic Number Theory Pipeline

```
ASYMPTOTIC ANALYSIS
═══════════════════════════════════════════════════════════════

COUNTING PROBLEM
─────────────────────────────────────────
Given: Arithmetic function f(n) or set S
Find: Asymptotic behavior of Σf(n) or |S ∩ [1,x]|

TECHNIQUE SELECTION
─────────────────────────────────────────
1. Elementary estimates
   □ Partial summation
   □ Comparison with integrals
   □ Möbius inversion

2. Analytic methods
   □ Generating Dirichlet series
   □ Locate poles and residues
   □ Apply Perron's formula

3. Sieve methods
   □ Eratosthenes sieve for primes
   □ Selberg sieve for upper bounds
   □ Linear sieve for lower bounds

OUTPUT FORMAT
─────────────────────────────────────────
Main term + error term: f(x) = g(x) + O(h(x))
With explicit constants when possible
```

### Prime Distribution Analysis

```
PRIME COUNTING
═══════════════════════════════════════════════════════════════

FUNCTIONS
─────────────────────────────────────────
π(x) = #{p ≤ x : p prime}
θ(x) = Σ_{p≤x} log p
ψ(x) = Σ_{p^k≤x} log p

ASYMPTOTIC RELATIONS
─────────────────────────────────────────
PNT: π(x) ~ x/log x
Refined: π(x) = Li(x) + O(x exp(-c√log x))
θ(x) ~ x, ψ(x) ~ x

ARITHMETIC PROGRESSIONS
─────────────────────────────────────────
Dirichlet: Infinitely many primes in {a + nd : n ≥ 0}
           when gcd(a,d) = 1
Quantitative: π(x; d, a) ~ Li(x)/φ(d)
```

### Algebraic Number Theory Pipeline

```
NUMBER FIELD ANALYSIS
═══════════════════════════════════════════════════════════════

FIELD SPECIFICATION
─────────────────────────────────────────
K = ℚ(α) where α = root of f(x) ∈ ℤ[x]
[K:ℚ] = deg(f)

COMPUTE INVARIANTS
─────────────────────────────────────────
1. Ring of integers O_K
   □ Find integral basis
   □ Compute discriminant d_K

2. Ideal structure
   □ Factor rational primes in O_K
   □ Compute ramification indices e_i
   □ Compute residue degrees f_i

3. Class group Cl(K)
   □ Minkowski bound
   □ Factor ideals of small norm
   □ Determine relations
   □ Present group structure

4. Unit group O_K*
   □ Compute rank r + s - 1
   □ Find fundamental units
   □ Regulator computation

EXAMPLE: QUADRATIC FIELDS
─────────────────────────────────────────
K = ℚ(√d), d squarefree

O_K = { ℤ[√d]           if d ≡ 2, 3 (mod 4)
      { ℤ[(1+√d)/2]     if d ≡ 1 (mod 4)

Prime p splits/inerts/ramifies based on (d/p)
```

### Diophantine Equation Pipeline

```
DIOPHANTINE ANALYSIS
═══════════════════════════════════════════════════════════════

CLASSIFICATION
─────────────────────────────────────────
1. Linear: ax + by = c
2. Quadratic: ax² + bxy + cy² = d
3. Pythagorean-type: x² + y² = z²
4. Higher degree: Fermat, Mordell, Thue
5. Exponential: a^x + b^y = c^z

SOLUTION STRATEGY
─────────────────────────────────────────
Linear:
  □ Exists iff gcd(a,b) | c
  □ Find particular solution via extended Euclidean
  □ General solution: x = x₀ + (b/d)t, y = y₀ - (a/d)t

Quadratic forms:
  □ Compute discriminant Δ = b² - 4ac
  □ Δ > 0: Infinitely many or none (Pell)
  □ Δ < 0: Finitely many, enumerate
  □ Δ = 0: Reduce to linear

Pell equation x² - Dy² = 1:
  □ Fundamental solution via continued fractions
  □ All solutions from (x₁ + y₁√D)^n

Higher degree:
  □ Local obstructions (mod p analysis)
  □ Descent methods
  □ Modern: Modularity, ABC conjecture
```

---

## Agent Coordination

### Problem Routing

| Problem Type | Primary Agent | Supporting Agents |
|--------------|---------------|-------------------|
| Factorization, divisibility | number-theorist | - |
| Prime distribution | analytic-number-theorist | number-theorist |
| L-functions, zeta | analytic-number-theorist | - |
| Number fields | algebraic-number-theorist | field-theorist |
| Diophantine equations | number-theorist | algebraic-number-theorist |
| Class field theory | algebraic-number-theorist | - |

### Workflow: Complete Analysis

```
1. number-theorist
   └─ Elementary analysis and problem classification

2. Route by type:
   ├─ Prime/asymptotic → analytic-number-theorist
   ├─ Field arithmetic → algebraic-number-theorist
   └─ Elementary → continue with number-theorist

3. Synthesis
   └─ Combine results, state theorem with proof
```

---

## Output Format

### Theorem Statement
```
THEOREM
═══════════════════════════════════════════════════════════════
[Clear statement of result]

PROOF
─────────────────────────────────────────
[Structured proof with key steps]

COROLLARIES
─────────────────────────────────────────
[Immediate consequences]
```

### Computation Result
```
COMPUTATION: [Problem description]
═══════════════════════════════════════════════════════════════

INPUT
─────────────────────────────────────────
[Given data]

METHOD
─────────────────────────────────────────
[Algorithm/technique used]

RESULT
─────────────────────────────────────────
[Answer with verification]
```

---

## Examples

### Example 1: Solve x² ≡ 2 (mod 17)

```
/number-theory congruence "x^2 ≡ 2 (mod 17)"

SOLUTION
═══════════════════════════════════════════════════════════════

STEP 1: Check solvability via Legendre symbol
─────────────────────────────────────────
(2/17) = (-1)^((17²-1)/8) = (-1)^36 = 1

2 is a quadratic residue mod 17. ✓

STEP 2: Find square root
─────────────────────────────────────────
Since 17 ≡ 1 (mod 8), use Tonelli-Shanks or direct search.
6² = 36 ≡ 2 (mod 17) ✓

RESULT
─────────────────────────────────────────
x ≡ ±6 (mod 17)
Solutions: x ∈ {6, 11} in {0, 1, ..., 16}
```

### Example 2: Factor (2) in ℤ[√-5]

```
/number-theory field "factor (2) in Q(√-5)"

FACTORIZATION IN O_K
═══════════════════════════════════════════════════════════════

FIELD: K = ℚ(√-5), d_K = -20

RING OF INTEGERS: O_K = ℤ[√-5]  (since -5 ≡ 3 mod 4)

FACTORIZATION OF (2)
─────────────────────────────────────────
Check: Is -5 a square mod 2?
-5 ≡ 1 (mod 2), and 1² ≡ 1 (mod 2) ✓

So 2 splits: (2) = 𝔭𝔭̄

Factor: (2) = (2, 1 + √-5)(2, 1 - √-5)

VERIFICATION
─────────────────────────────────────────
N(𝔭) = 2, confirming 𝔭 is prime ideal of norm 2.
```

---

## References

- Hardy, G.H. & Wright, E.M. - An Introduction to the Theory of Numbers
- Ireland, K. & Rosen, M. - A Classical Introduction to Modern Number Theory
- Neukirch, J. - Algebraic Number Theory
- Iwaniec, H. & Kowalski, E. - Analytic Number Theory
