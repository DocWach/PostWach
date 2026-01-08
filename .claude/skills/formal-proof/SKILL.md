# Formal Proof Skill

## Overview

This skill provides comprehensive methodologies for constructing, verifying, and documenting formal mathematical proofs. It covers proof strategies, logical inference rules, proof writing conventions, and quality standards for rigorous mathematical argumentation.

## When to Use

- Proving mathematical theorems and lemmas
- Verifying logical arguments
- Writing rigorous proofs for publication
- Teaching proof techniques
- Formalizing intuitive arguments
- Checking proof correctness

---

## Proof Writing Methodology

### Pre-Proof Checklist

```
BEFORE STARTING A PROOF
═══════════════════════════════════════════════════════════════

□ Understand the claim completely
  - What are the hypotheses?
  - What is the conclusion?
  - What do all terms mean?

□ Check if claim is likely true
  - Test small cases
  - Look for counterexamples
  - Verify boundary cases

□ Identify relevant tools
  - Which definitions apply?
  - Which theorems might help?
  - What techniques suit this problem?

□ Plan the proof strategy
  - Direct? Contradiction? Induction?
  - What's the key insight?
  - What are the main steps?

□ Set up notation
  - Consistent variable names
  - Clear quantifier scope
  - Standard conventions
```

### Proof Structure Template

```
STANDARD PROOF STRUCTURE
═══════════════════════════════════════════════════════════════

THEOREM/LEMMA/PROPOSITION [Number] ([Name])
Statement of the claim in precise mathematical language.

PROOF:
[Setup] Introduce notation, state what we'll prove.

[Main argument] Series of logical steps, each justified.

[Conclusion] Therefore, [restate what was proven]. □

EXAMPLE:
─────────────────────────────────────────
Theorem 1 (Infinitude of Primes)
There are infinitely many prime numbers.

Proof:
Suppose, for contradiction, that there are only finitely many
primes: p₁, p₂, ..., pₙ.

Consider N = p₁p₂···pₙ + 1.

Since N > 1, N has a prime divisor p.

For each i, we have pᵢ | p₁p₂···pₙ, so pᵢ ∤ N
(since pᵢ | N would imply pᵢ | 1).

Thus p ≠ pᵢ for all i, contradicting that p₁,...,pₙ are
all the primes.

Therefore, there are infinitely many primes. □
```

---

## Logical Foundations

### Inference Rules Reference

```
PROPOSITIONAL LOGIC RULES
═══════════════════════════════════════════════════════════════

INTRODUCTION RULES (how to prove)
─────────────────────────────────────────

∧-Introduction (Conjunction):
  From P and Q, conclude P ∧ Q

  P    Q
  ─────── (∧I)
   P ∧ Q

∨-Introduction (Disjunction):
  From P, conclude P ∨ Q (either side)

    P              Q
  ───── (∨I₁)   ───── (∨I₂)
  P ∨ Q         P ∨ Q

→-Introduction (Conditional):
  Assume P, derive Q, conclude P → Q

  [P]
   ⋮
   Q
  ───── (→I)
  P → Q

¬-Introduction (Negation):
  Assume P, derive ⊥, conclude ¬P

  [P]
   ⋮
   ⊥
  ───── (¬I)
   ¬P

ELIMINATION RULES (how to use)
─────────────────────────────────────────

∧-Elimination:
  From P ∧ Q, conclude P (or Q)

  P ∧ Q         P ∧ Q
  ───── (∧E₁)   ───── (∧E₂)
    P             Q

∨-Elimination (Case analysis):
  From P ∨ Q, P → R, Q → R, conclude R

  P ∨ Q   [P]→R   [Q]→R
  ─────────────────────── (∨E)
            R

→-Elimination (Modus Ponens):
  From P and P → Q, conclude Q

  P    P → Q
  ────────── (→E)
      Q

¬-Elimination (Contradiction):
  From P and ¬P, conclude anything

  P    ¬P
  ──────── (¬E)
     ⊥

Double Negation Elimination (classical):
  From ¬¬P, conclude P

   ¬¬P
  ───── (DNE)
    P
```

### Quantifier Rules

```
PREDICATE LOGIC RULES
═══════════════════════════════════════════════════════════════

UNIVERSAL QUANTIFIER (∀)
─────────────────────────────────────────

∀-Introduction:
  Prove P(x) for arbitrary x, conclude ∀x.P(x)

  P(x)   [x arbitrary, no assumptions about x]
  ───────────────────────────────────────────── (∀I)
                    ∀x.P(x)

∀-Elimination (Universal Instantiation):
  From ∀x.P(x), conclude P(t) for any term t

  ∀x.P(x)
  ──────── (∀E)
   P(t)

EXISTENTIAL QUANTIFIER (∃)
─────────────────────────────────────────

∃-Introduction (Existential Generalization):
  From P(t) for some term t, conclude ∃x.P(x)

   P(t)
  ────── (∃I)
  ∃x.P(x)

∃-Elimination:
  From ∃x.P(x) and [P(c) → Q] for fresh c, conclude Q

  ∃x.P(x)   [P(c)]→Q   [c fresh]
  ────────────────────────────── (∃E)
              Q

COMMON PATTERNS
─────────────────────────────────────────

Proving ∀x.P(x):
  "Let x be arbitrary."
  [Show P(x)]
  "Since x was arbitrary, ∀x.P(x)."

Proving ∃x.P(x):
  "Consider t = [specific value]."
  [Show P(t)]
  "Thus ∃x.P(x)."

Using ∀x.P(x):
  "Since ∀x.P(x), we have P(a) in particular."

Using ∃x.P(x):
  "Since ∃x.P(x), let c be such that P(c)."
  [Use P(c), derive conclusion Q not mentioning c]
```

---

## Proof Strategies Handbook

### Strategy Selection Guide

```
CHOOSING A PROOF STRATEGY
═══════════════════════════════════════════════════════════════

CLAIM STRUCTURE → SUGGESTED STRATEGY
─────────────────────────────────────────

P → Q (conditional)
  Primary: Direct proof (assume P, derive Q)
  Alternative: Contrapositive (assume ¬Q, derive ¬P)
  Alternative: Contradiction (assume P ∧ ¬Q, derive ⊥)

∀x.P(x) (universal)
  Primary: Let x be arbitrary, prove P(x)
  If domain is ℕ: Consider induction
  If finite domain: Case exhaustion

∃x.P(x) (existential)
  Primary: Exhibit witness (construct specific x)
  Alternative: Contradiction (assume none exists)
  Alternative: Probabilistic/counting argument

P ↔ Q (biconditional)
  Primary: Prove P → Q and Q → P separately
  Alternative: Chain of equivalences

¬P (negation)
  Primary: Contradiction (assume P, derive ⊥)
  Alternative: Direct proof of negation

P ∨ Q (disjunction)
  Primary: Prove one disjunct
  Alternative: Case analysis on some condition
  Alternative: Contradiction of ¬P ∧ ¬Q

a = b (equality)
  Primary: Chain of equalities
  Alternative: Show a ≤ b and b ≤ a
  Alternative: Uniqueness argument

a < b (inequality)
  Primary: Direct estimation
  Alternative: Prove a ≤ c < b for some c
  Alternative: Contradiction of a ≥ b
```

### Direct Proof Methodology

```
DIRECT PROOF
═══════════════════════════════════════════════════════════════

PATTERN: To prove P → Q
─────────────────────────────────────────
1. Write: "Assume P." (or "Suppose P." or "Let P hold.")
2. Unpack definitions as needed
3. Apply known theorems and logical steps
4. Arrive at Q
5. Write: "Therefore, P → Q." (or just conclude Q)

KEY TECHNIQUES
─────────────────────────────────────────

Element chasing (for set containment A ⊆ B):
  "Let x ∈ A be arbitrary."
  [Show x has property defining B]
  "Thus x ∈ B."
  "Since x was arbitrary, A ⊆ B."

Equality chaining:
  "LHS = [expression 1]    (by [reason])
       = [expression 2]    (by [reason])
       = ...
       = RHS."

Forward reasoning:
  Start from hypotheses, derive consequences toward goal

Backward reasoning:
  Start from goal, identify sufficient conditions,
  work back to hypotheses

EXAMPLE: √2 is irrational
─────────────────────────────────────────
Claim: √2 is irrational.

Proof (by contradiction):
Suppose √2 is rational. Then √2 = a/b for some integers
a, b with b ≠ 0 and gcd(a,b) = 1 (lowest terms).

Squaring: 2 = a²/b², so a² = 2b².

Thus a² is even, so a is even. Write a = 2k.

Then 4k² = 2b², so b² = 2k².

Thus b² is even, so b is even.

But then gcd(a,b) ≥ 2, contradicting gcd(a,b) = 1.

Therefore, √2 is irrational. □
```

### Mathematical Induction Methodology

```
INDUCTION TECHNIQUES
═══════════════════════════════════════════════════════════════

SIMPLE INDUCTION TEMPLATE
─────────────────────────────────────────
Claim: For all n ≥ n₀, P(n).

Proof by induction on n.

Base case (n = n₀):
  [Verify P(n₀) directly]

Inductive step:
  Let k ≥ n₀ and assume P(k). [This is the IH]
  [Prove P(k+1), using IH]

By induction, P(n) holds for all n ≥ n₀. □

STRONG INDUCTION TEMPLATE
─────────────────────────────────────────
Claim: For all n ≥ n₀, P(n).

Proof by strong induction on n.

Base case(s):
  [Verify P(n₀), possibly P(n₀+1), etc.]

Inductive step:
  Let k > n₀ and assume P(j) for all n₀ ≤ j < k. [Strong IH]
  [Prove P(k), using any P(j) with j < k]

By strong induction, P(n) holds for all n ≥ n₀. □

STRUCTURAL INDUCTION TEMPLATE
─────────────────────────────────────────
Claim: For all x in inductively-defined set S, P(x).

Proof by structural induction.

Base case(s):
  For each base constructor c: [Verify P(c)]

Inductive step(s):
  For each recursive constructor f:
    Assume P(x₁), ..., P(xₖ) for components.
    [Prove P(f(x₁,...,xₖ))]

By structural induction, P(x) holds for all x ∈ S. □

COMMON INDUCTION PITFALLS
─────────────────────────────────────────
✗ Wrong base case (off by one)
✗ Assuming P(k+1) instead of P(k) in IH
✗ Not actually using the IH
✗ IH doesn't apply (index mismatch)
✗ Hidden assumptions in inductive step
✗ Insufficient base cases for strong induction
```

---

## Proof Writing Standards

### Style Guidelines

```
PROOF WRITING CONVENTIONS
═══════════════════════════════════════════════════════════════

LANGUAGE AND PHRASING
─────────────────────────────────────────

Starting a proof:
  ✓ "Let x ∈ A be arbitrary."
  ✓ "Suppose P holds."
  ✓ "Assume, for contradiction, that ¬Q."
  ✗ "We will prove..." (just prove it)

Making deductions:
  ✓ "Thus P." / "Hence P." / "Therefore P."
  ✓ "It follows that P."
  ✓ "This implies P."
  ✓ "By [theorem name], P."

Citing reasons:
  ✓ "by definition of [term]"
  ✓ "by [Theorem X]"
  ✓ "by the inductive hypothesis"
  ✓ "by assumption"
  ✓ "since [previous statement]"

Ending a proof:
  ✓ "Therefore, [conclusion]. □"
  ✓ "This completes the proof. □"
  ✓ "QED" or "∎" (less common now)

STRUCTURE AND ORGANIZATION
─────────────────────────────────────────

Do:
  ✓ State clearly what you're proving
  ✓ Introduce notation before using it
  ✓ Give reasons for each step
  ✓ Use paragraph breaks for logical sections
  ✓ Label cases clearly
  ✓ Mark end of proof with □

Don't:
  ✗ Skip "obvious" steps (they often aren't)
  ✗ Use undefined notation
  ✗ Write walls of symbols without explanation
  ✗ Leave the reader to guess the strategy
  ✗ Introduce unnecessary notation

LEVEL OF DETAIL
─────────────────────────────────────────

Include:
  ✓ Key insights and ideas
  ✓ Non-trivial deductions
  ✓ Where major theorems are used
  ✓ Where hypotheses are used

May omit (with "clearly" or "straightforward"):
  ○ Routine algebraic manipulations
  ○ Standard epsilon-delta estimates
  ○ Well-known facts
  But be sure they really are routine/standard!

Never omit:
  ✗ Steps that use the main hypothesis
  ✗ The key insight of the proof
  ✗ Why the argument actually works
```

### Common Proof Errors

```
PROOF ERRORS TO AVOID
═══════════════════════════════════════════════════════════════

LOGICAL ERRORS
─────────────────────────────────────────

Affirming the consequent:
  ✗ "If P then Q. Q holds. Therefore P."
  This is INVALID.

Circular reasoning:
  ✗ Using what you're trying to prove as a step
  Watch for: assuming the conclusion in disguise

Proof by example:
  ✗ "P(3) is true. Therefore ∀n.P(n)."
  Examples support but don't prove universals.

Proof by lack of counterexample:
  ✗ "I can't find a counterexample, so it's true."
  This is not a proof.

Converse error:
  ✗ Proving Q → P when asked to prove P → Q
  These are different statements!

QUANTIFIER ERRORS
─────────────────────────────────────────

Order of quantifiers:
  ✗ Treating "∀x∃y" same as "∃y∀x"
  ∀x∃y.P(x,y): for each x, there's a y (may depend on x)
  ∃y∀x.P(x,y): one y works for all x

Fresh variable violation:
  ✗ Using ∃-elimination with a variable already in scope
  The witness variable must be fresh.

Universal generalization error:
  ✗ Concluding ∀x.P(x) from P(a) where a was special
  The variable must have been truly arbitrary.

INDUCTION ERRORS
─────────────────────────────────────────

Base case wrong:
  ✗ Starting induction at wrong value
  ✗ Forgetting to verify base case at all

IH not actually used:
  ✗ Proving P(k+1) without using P(k)
  This usually means the "proof" is wrong.

IH used incorrectly:
  ✗ Applying IH to k+1 instead of k
  ✗ Applying IH outside its valid range

Insufficient base cases:
  ✗ Strong induction needing P(0) and P(1) but only showing P(0)
```

---

## Proof Verification Checklist

```
PROOF VERIFICATION
═══════════════════════════════════════════════════════════════

□ STRUCTURE CHECK
  □ Claim is clearly stated
  □ Proof strategy is identifiable
  □ All cases are covered
  □ Conclusion matches claim

□ LOGICAL CHECK
  □ Each step follows from previous
  □ All inferences are valid
  □ No circular reasoning
  □ Quantifiers handled correctly

□ COMPLETENESS CHECK
  □ All hypotheses used (or noted if not needed)
  □ No hidden assumptions
  □ Edge cases addressed
  □ No gaps in reasoning

□ NOTATION CHECK
  □ All symbols defined
  □ Notation consistent throughout
  □ Quantifier scope clear
  □ No variable capture issues

□ READABILITY CHECK
  □ Strategy is clear to reader
  □ Key steps are explained
  □ Appropriate level of detail
  □ Well-organized presentation
```

---

## Integration with Agents

### Recommended Agent Combinations

- **proof-constructor**: Primary proof building
- **axiom-architect**: Foundation verification
- **counterexample-hunter**: Pre-proof claim validation
- **skeptical-challenger**: Post-proof verification
- **rationalist-synthesizer**: Logical structure design

---

## References

- Velleman, D.J. (2019). How to Prove It (3rd ed.)
- Hammack, R. (2018). Book of Proof
- Houston, K. (2009). How to Think Like a Mathematician
- Halmos, P. (1970). How to Write Mathematics
- Krantz, S.G. (2017). A Primer of Mathematical Writing
