# Computability Theory Skill

## Overview

This skill provides comprehensive methodologies for working with computability, decidability, reductions, and the foundations of theoretical computer science. It covers Turing machines, recursive functions, undecidability proofs, degree theory, and the arithmetical hierarchy.

## When to Use

- Determining decidability or undecidability of problems
- Constructing reduction arguments
- Working with Turing machines and computation models
- Analyzing computational complexity classes
- Degree-theoretic arguments
- Classifying problems in the arithmetical hierarchy
- Formalizing effective procedures

---

## Models of Computation

```
TURING MACHINES
═══════════════════════════════════════════════════════════════

DEFINITION
─────────────────────────────────────────
A Turing machine M = (Q, Σ, Γ, δ, q₀, qₐ, qᵣ) consists of:
  Q: finite set of states
  Σ: input alphabet (⊆ Γ, not including blank)
  Γ: tape alphabet (includes blank symbol ⊔)
  δ: Q × Γ → Q × Γ × {L, R} (transition function)
  q₀: start state
  qₐ: accept state
  qᵣ: reject state

COMPUTATION
─────────────────────────────────────────
Configuration: (state, tape contents, head position)

M on input w:
  - Start in q₀ with w on tape, head at leftmost symbol
  - Apply δ until reaching qₐ or qᵣ
  - Accept if reach qₐ, reject if reach qᵣ

L(M) = {w : M accepts w}

VARIANTS (all equivalent)
─────────────────────────────────────────
□ Multi-tape TM: Multiple tapes, all heads move independently
□ Nondeterministic TM: δ: Q × Γ → P(Q × Γ × {L,R})
□ Two-way infinite tape
□ Multi-head TM
□ Random access TM

CHURCH-TURING THESIS
─────────────────────────────────────────
Any "effectively calculable" function is Turing-computable.

Evidence:
  - All equivalent models (λ-calculus, recursive functions, etc.)
  - No counter-examples found
  - Physical realizability arguments
```

---

## Recursive Functions

```
PRIMITIVE RECURSIVE FUNCTIONS
═══════════════════════════════════════════════════════════════

BASE FUNCTIONS
─────────────────────────────────────────
Zero: Z(n) = 0
Successor: S(n) = n + 1
Projection: Pᵢⁿ(x₁,...,xₙ) = xᵢ

CLOSURE OPERATIONS
─────────────────────────────────────────
Composition:
  h(x̄) = f(g₁(x̄),...,gₖ(x̄))

Primitive Recursion:
  h(x̄, 0) = f(x̄)
  h(x̄, y+1) = g(x̄, y, h(x̄, y))

EXAMPLES
─────────────────────────────────────────
Addition: add(x, 0) = x
          add(x, y+1) = S(add(x, y))

Multiplication: mult(x, 0) = 0
                mult(x, y+1) = add(x, mult(x, y))

Exponentiation: exp(x, 0) = 1
                exp(x, y+1) = mult(x, exp(x, y))

Predecessor: pred(0) = 0
             pred(y+1) = y

Bounded quantification, bounded search, etc.

μ-RECURSIVE FUNCTIONS
═══════════════════════════════════════════════════════════════

MINIMIZATION (μ-operator)
─────────────────────────────────────────
μy[f(x̄, y) = 0] = least y such that f(x̄, y) = 0
                   (undefined if no such y exists)

PARTIAL RECURSIVE = TURING COMPUTABLE
─────────────────────────────────────────
The partial recursive functions are exactly the Turing-computable
partial functions.

TOTAL RECURSIVE ⊊ PARTIAL RECURSIVE
─────────────────────────────────────────
Total recursive: defined on all inputs
Not all partial recursive functions can be made total.

EXAMPLES OF NON-PRIMITIVE RECURSIVE
─────────────────────────────────────────
Ackermann function:
  A(0, n) = n + 1
  A(m+1, 0) = A(m, 1)
  A(m+1, n+1) = A(m, A(m+1, n))

Grows faster than any primitive recursive function.
```

---

## Decidability and Undecidability

```
DECIDABILITY
═══════════════════════════════════════════════════════════════

DEFINITIONS
─────────────────────────────────────────
Language L is decidable (recursive) if there exists TM M such that:
  - M halts on all inputs
  - M accepts exactly the strings in L

L is recognizable (r.e., semi-decidable) if there exists TM M such that:
  - M accepts exactly the strings in L
  (may not halt on strings not in L)

L is co-recognizable if L̄ is recognizable.

RELATIONSHIPS
─────────────────────────────────────────
L decidable ↔ L is both recognizable and co-recognizable

Decidable ⊊ Recognizable ⊊ All languages

HALTING PROBLEM
═══════════════════════════════════════════════════════════════

DEFINITION
─────────────────────────────────────────
HALT = {⟨M, w⟩ : M halts on w}

THEOREM: HALT is undecidable.

PROOF (diagonalization)
─────────────────────────────────────────
Assume H decides HALT.

Define D on input ⟨M⟩:
  If H(⟨M⟩, ⟨M⟩) accepts, loop forever
  If H(⟨M⟩, ⟨M⟩) rejects, accept

Consider D on ⟨D⟩:
  D(⟨D⟩) halts  ↔  H(⟨D⟩, ⟨D⟩) rejects
                ↔  D(⟨D⟩) doesn't halt
  Contradiction!

RICE'S THEOREM
═══════════════════════════════════════════════════════════════

STATEMENT
─────────────────────────────────────────
Let P be any non-trivial property of r.e. languages.
Then {⟨M⟩ : L(M) has property P} is undecidable.

Non-trivial: Some TMs have P, some don't.

EXAMPLES OF UNDECIDABLE PROPERTIES
─────────────────────────────────────────
□ L(M) = ∅
□ L(M) is finite
□ L(M) = Σ*
□ L(M) is regular
□ M halts on ε
□ L(M) contains a specific string
```

---

## Reductions

```
MANY-ONE REDUCTIONS
═══════════════════════════════════════════════════════════════

DEFINITION
─────────────────────────────────────────
A ≤ₘ B (A many-one reduces to B) if there exists computable f such that:
  x ∈ A ↔ f(x) ∈ B

PROPERTIES
─────────────────────────────────────────
□ Transitive: A ≤ₘ B and B ≤ₘ C implies A ≤ₘ C
□ Reflexive: A ≤ₘ A
□ If A ≤ₘ B and B decidable, then A decidable
□ If A ≤ₘ B and A undecidable, then B undecidable

USE FOR UNDECIDABILITY
─────────────────────────────────────────
To show B is undecidable:
  1. Find known undecidable A
  2. Construct reduction A ≤ₘ B
  3. Conclude B undecidable

TURING REDUCTIONS
═══════════════════════════════════════════════════════════════

DEFINITION
─────────────────────────────────────────
A ≤ₜ B (A Turing reduces to B) if A is decidable with oracle for B.

Oracle TM: Has special query tape and states to ask "is y ∈ B?"

PROPERTIES
─────────────────────────────────────────
□ More flexible than ≤ₘ: can ask multiple queries
□ A ≤ₘ B implies A ≤ₜ B
□ A ≤ₜ B means "A is no harder than B"

COMMON REDUCTIONS
─────────────────────────────────────────
HALT ≤ₘ A_TM ≤ₘ HALT_ε
E_TM ≤ₘ EQ_TM
A_TM ≤ₘ complement not possible (A_TM not co-r.e.)
```

---

## Turing Degrees

```
DEGREE STRUCTURE
═══════════════════════════════════════════════════════════════

DEFINITION
─────────────────────────────────────────
Turing degree: deg(A) = {B : A ≡ₜ B}
  where A ≡ₜ B means A ≤ₜ B and B ≤ₜ A

Partial order: deg(A) ≤ deg(B) iff A ≤ₜ B

SPECIAL DEGREES
─────────────────────────────────────────
0 = deg(∅) = deg(decidable sets)
  The lowest degree

0' = deg(HALT) = deg(K)
  The halting problem's degree
  K = {e : φₑ(e)↓}

0'' = (0')' = deg(HALT')
  The degree of "does TM halt on HALT?"

0⁽ⁿ⁾ = nth jump of 0

JUMP OPERATOR
─────────────────────────────────────────
For any set A:
  A' = {e : φₑᴬ(e)↓}

Properties:
  □ A <ₜ A' (strictly)
  □ A ≤ₜ B → A' ≤ₜ B'
  □ A ≤ₜ B' ↔ A is r.e. in B

POST'S THEOREM
─────────────────────────────────────────
A is Σₙ iff A is r.e. in 0⁽ⁿ⁻¹⁾
A is Δₙ iff A ≤ₜ 0⁽ⁿ⁻¹⁾

STRUCTURE RESULTS
─────────────────────────────────────────
□ Degrees form an upper semi-lattice
□ Every countable partial order embeds into degrees
□ There exist minimal degrees > 0
□ There exist incomparable degrees
□ There exist degrees between 0 and 0'
```

---

## Arithmetical Hierarchy

```
HIERARCHY DEFINITION
═══════════════════════════════════════════════════════════════

ARITHMETIC FORMULAS
─────────────────────────────────────────
Language of arithmetic: 0, S, +, ×, <

Σ₀ = Π₀ = Δ₀: Bounded quantifier formulas
  ∀x < t and ∃x < t only

Σₙ₊₁: ∃x₁...∃xₖ ψ where ψ ∈ Πₙ
Πₙ₊₁: ∀x₁...∀xₖ ψ where ψ ∈ Σₙ
Δₙ₊₁: Both Σₙ₊₁ and Πₙ₊₁

ARITHMETICAL SETS
─────────────────────────────────────────
A ⊆ ℕ is Σₙ if A = {x : ℕ ⊨ φ(x)} for Σₙ formula φ.

EXAMPLES
─────────────────────────────────────────
Σ₁ (r.e.):
  □ Halt = {⟨M,w⟩ : M halts on w}
  □ K = {e : φₑ(e)↓}
  □ Range of computable function

Π₁ (co-r.e.):
  □ Complement of Halt
  □ TOT = {e : φₑ is total}... no wait, this is Π₂
  □ Infinite sets (complement of finite)

Σ₂:
  □ FIN = {e : Wₑ is finite}
  □ COF = {e : Wₑ is cofinite}

Π₂:
  □ INF = {e : Wₑ is infinite}
  □ TOT = {e : φₑ is total}

HIERARCHY THEOREM
─────────────────────────────────────────
For all n: Σₙ ⊊ Σₙ₊₁ and Πₙ ⊊ Πₙ₊₁

Σₙ-complete: Hardest sets in Σₙ
Πₙ-complete: Hardest sets in Πₙ

Complete examples:
  K is Σ₁-complete
  TOT is Π₂-complete
  FIN is Σ₂-complete
```

---

## Proof Templates

```
COMPUTABILITY PROOF PATTERNS
═══════════════════════════════════════════════════════════════

DECIDABILITY PROOF
─────────────────────────────────────────
To show L is decidable:
  1. Design TM M that decides L
  2. Prove M halts on all inputs
  3. Prove M accepts iff input ∈ L

UNDECIDABILITY BY REDUCTION
─────────────────────────────────────────
To show L is undecidable:
  1. Choose known undecidable A (often HALT or A_TM)
  2. Design computable f: Σ* → Σ*
  3. Prove: x ∈ A iff f(x) ∈ L
  4. Conclude: A ≤ₘ L, so L undecidable

DIAGONALIZATION
─────────────────────────────────────────
To prove no TM has property P:
  1. Assume M has property P
  2. Construct D using M that differs from M on ⟨D⟩
  3. Derive contradiction

HIERARCHY CLASSIFICATION
─────────────────────────────────────────
To show A is Σₙ-complete:
  1. Show A ∈ Σₙ (express A with Σₙ formula)
  2. Show every Σₙ set reduces to A

ORACLE CONSTRUCTION
─────────────────────────────────────────
To show A ≤ₜ B:
  1. Design oracle TM M^B
  2. Prove M^B decides A using B-queries
  3. M^B must halt on all inputs

FIXED POINT ARGUMENTS
─────────────────────────────────────────
Kleene's recursion theorem:
  For any computable f, there exists e with φₑ = φ_{f(e)}

Use: Construct self-referential TMs
```

---

## Key Theorems Reference

```
FUNDAMENTAL THEOREMS
═══════════════════════════════════════════════════════════════

UNIVERSAL TM
─────────────────────────────────────────
There exists U such that U(⟨M⟩, w) = M(w).
(Simulation with at most polynomial slowdown)

s-m-n THEOREM
─────────────────────────────────────────
For each m, n there is computable s such that:
  φₛ(e,x₁,...,xₘ)(y₁,...,yₙ) = φₑ(x₁,...,xₘ,y₁,...,yₙ)

RECURSION THEOREM (Kleene)
─────────────────────────────────────────
For computable f, ∃e: φₑ = φ_{f(e)}
Equivalently: ∃e: φₑ(x) = f(e, x)

RICE'S THEOREM
─────────────────────────────────────────
Non-trivial semantic properties of r.e. sets are undecidable.

POST'S THEOREM
─────────────────────────────────────────
Connects arithmetic hierarchy with Turing degrees.
Σₙ = r.e. in 0^(n-1)

FRIEDBERG-MUCHNIK
─────────────────────────────────────────
There exist r.e. sets A, B with A ≰ₜ B and B ≰ₜ A.
(Incomparable r.e. degrees exist)
```

---

## Integration with Agents

### Recommended Agent Combinations

- **computability-theorist**: Primary computability reasoning
- **general-logician**: Logical foundations, Gödel encoding
- **set-theorist**: Ordinal analysis, transfinite computation
- **proof-constructor**: Formal undecidability proofs
- **algorithm-designer**: Complexity connections

---

## References

- Sipser, M. (2012). Introduction to the Theory of Computation (3rd ed.)
- Rogers, H. (1987). Theory of Recursive Functions and Effective Computability
- Soare, R.I. (2016). Turing Computability
- Odifreddi, P. (1989, 1999). Classical Recursion Theory (2 vols.)
- Cooper, S.B. (2004). Computability Theory
