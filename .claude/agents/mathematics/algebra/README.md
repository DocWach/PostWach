# Phase 3: Number Theory & Algebra

## Overview

Phase 3 implements the MSC2020 coverage for number theory and abstract algebra, spanning MSC categories 11-18 and 20. This phase provides comprehensive agents for studying integers, primes, algebraic structures, and categorical frameworks.

## MSC Categories Covered

| MSC | Category | Agent(s) |
|-----|----------|----------|
| 11 | Number theory | `number-theorist`, `analytic-number-theorist`, `algebraic-number-theorist` |
| 12 | Field theory and polynomials | `field-theorist` |
| 13 | Commutative algebra | `commutative-algebraist` |
| 15 | Linear and multilinear algebra | `linear-algebraist` |
| 16 | Associative rings and algebras | `ring-theorist` |
| 18 | Category theory | `category-theorist` |
| 20 | Group theory | `group-theorist` |

## Agents (9)

### Number Theory Agents

#### `number-theorist` (MSC 11)
Elementary number theory specialist covering divisibility, primes, congruences, quadratic reciprocity, and Diophantine equations.

**Capabilities:**
- Divisibility and GCD/LCM
- Prime factorization
- Congruences and modular arithmetic
- Chinese Remainder Theorem
- Quadratic residues and reciprocity
- Diophantine equations
- Arithmetic functions

#### `analytic-number-theorist` (MSC 11N)
Analytic number theory specialist focusing on the distribution of primes, L-functions, and asymptotic methods.

**Capabilities:**
- Riemann zeta function
- Prime Number Theorem
- Dirichlet L-functions
- Sieve methods
- Exponential sums
- Additive number theory

#### `algebraic-number-theorist` (MSC 11R)
Algebraic number theory specialist studying number fields, rings of integers, and class field theory.

**Capabilities:**
- Number fields and extensions
- Rings of integers
- Ideal theory and factorization
- Class groups
- Unit groups and Dirichlet's theorem
- Local fields and ramification

### Algebra Agents

#### `field-theorist` (MSC 12)
Field theory specialist covering field extensions, Galois theory, and polynomial equations.

**Capabilities:**
- Field extensions
- Algebraic and transcendental elements
- Galois theory
- Splitting fields
- Solvability by radicals
- Finite fields

#### `commutative-algebraist` (MSC 13)
Commutative algebra specialist studying rings, ideals, modules, and homological methods.

**Capabilities:**
- Prime and maximal ideals
- Localization
- Noetherian rings
- Primary decomposition
- Krull dimension
- Depth and Cohen-Macaulay rings

#### `linear-algebraist` (MSC 15)
Linear algebra specialist covering vector spaces, matrices, eigentheory, and canonical forms.

**Capabilities:**
- Vector spaces and bases
- Linear transformations
- Eigenvalues and eigenvectors
- Diagonalization
- Jordan canonical form
- Inner product spaces
- Singular value decomposition

#### `ring-theorist` (MSC 16)
Ring theory specialist focusing on noncommutative rings, modules, and representation theory.

**Capabilities:**
- Associative rings
- Simple and semisimple rings
- Jacobson radical
- Wedderburn-Artin theorem
- Module theory
- Morita equivalence

#### `group-theorist` (MSC 20)
Group theory specialist covering group structure, Sylow theory, representations, and classification.

**Capabilities:**
- Group structure and subgroups
- Normal subgroups and quotients
- Sylow theorems
- Solvable and nilpotent groups
- Simple groups
- Representation theory
- Character theory

### Category Theory

#### `category-theorist` (MSC 18)
Category theory specialist covering categories, functors, natural transformations, and universal properties.

**Capabilities:**
- Categories and functors
- Natural transformations
- Limits and colimits
- Adjunctions
- Yoneda lemma
- Abelian categories
- Topos theory

## Skills (4)

### `number-theory`
Methodology for number-theoretic investigations across elementary, analytic, and algebraic number theory.

**Subcommands:**
- `/number-theory analyze <expression>` - Analyze number-theoretic properties
- `/number-theory factor <n>` - Factor integers or ideals
- `/number-theory prime <query>` - Investigate prime-related questions
- `/number-theory congruence <equation>` - Solve congruences
- `/number-theory diophantine <equation>` - Analyze Diophantine equations
- `/number-theory field <specification>` - Study number fields

### `abstract-algebra`
Methodology for abstract algebraic investigations across groups, rings, fields, and modules.

**Subcommands:**
- `/abstract-algebra group <spec>` - Analyze group structure
- `/abstract-algebra ring <spec>` - Analyze ring structure
- `/abstract-algebra field <spec>` - Analyze field extensions
- `/abstract-algebra module <spec>` - Analyze module structure
- `/abstract-algebra homomorphism <map>` - Analyze homomorphisms
- `/abstract-algebra classify <structure>` - Classify algebraic structures

### `linear-algebra`
Methodology for linear algebraic computations and theory.

**Subcommands:**
- `/linear-algebra matrix <operation> <matrix>` - Matrix operations
- `/linear-algebra eigen <matrix>` - Eigenvalue analysis
- `/linear-algebra decompose <type> <matrix>` - Matrix decompositions
- `/linear-algebra solve <system>` - Solve linear systems
- `/linear-algebra space <spec>` - Analyze vector spaces
- `/linear-algebra transform <spec>` - Analyze linear transformations

### `category-theory`
Methodology for categorical reasoning and constructions.

**Subcommands:**
- `/category-theory category <spec>` - Analyze a category
- `/category-theory functor <spec>` - Analyze a functor
- `/category-theory natural <transformation>` - Analyze natural transformations
- `/category-theory limit <diagram>` - Compute limits/colimits
- `/category-theory adjunction <pair>` - Analyze adjunctions
- `/category-theory yoneda <application>` - Apply Yoneda lemma

## Worker Type

### `algebra-specialist`
Expert worker coordinating all Phase 3 agents for comprehensive algebraic analysis.

**Capabilities:**
- Elementary, analytic, and algebraic number theory
- Field extensions and Galois theory
- Commutative and noncommutative ring theory
- Linear algebra and eigentheory
- Group structure and representations
- Category theory and functors

## Swarm

### `algebraic-mathematics`
Comprehensive swarm for number theory and abstract algebra problems.

**Workflow Stages:**
1. **problem-classification** - Identify algebraic domain
2. **structure-analysis** - Analyze algebraic structures
3. **technique-selection** - Choose appropriate methods
4. **computation-exploration** - Compute examples, find patterns
5. **proof-development** - Develop rigorous proofs
6. **verification** - Verify correctness
7. **categorical-synthesis** - Place in categorical context

## Directory Structure

```
.claude/
├── agents/
│   └── mathematics/
│       ├── number-theory/
│       │   ├── number-theorist.md
│       │   ├── analytic-number-theorist.md
│       │   └── algebraic-number-theorist.md
│       ├── algebra/
│       │   ├── field-theorist.md
│       │   ├── commutative-algebraist.md
│       │   ├── linear-algebraist.md
│       │   ├── ring-theorist.md
│       │   ├── group-theorist.md
│       │   └── README.md (this file)
│       └── category-theory/
│           └── category-theorist.md
├── skills/
│   ├── number-theory/
│   │   └── SKILL.md
│   ├── abstract-algebra/
│   │   └── SKILL.md
│   ├── linear-algebra/
│   │   └── SKILL.md
│   └── category-theory/
│       └── SKILL.md
└── ...

.hive-mind/
└── config/
    ├── workers.json   (algebra-specialist added)
    └── swarms.json    (algebraic-mathematics added)
```

## Usage Examples

### Number Theory Problem
```
User: Prove that √2 is irrational

Response flow:
1. number-theorist analyzes claim
2. Uses proof by contradiction
3. Derives contradiction from parity
4. Concludes irrationality
```

### Galois Theory Problem
```
User: Find the Galois group of x⁴ - 2 over ℚ

Response flow:
1. field-theorist identifies splitting field ℚ(⁴√2, i)
2. Computes [K:ℚ] = 8
3. group-theorist identifies group structure
4. Determines Gal(K/ℚ) ≅ D₄
```

### Group Classification
```
User: Classify groups of order 12

Response flow:
1. group-theorist applies Sylow theory
2. Determines n₂, n₃ possibilities
3. Identifies five groups: ℤ₁₂, ℤ₂×ℤ₆, A₄, D₆, Q₁₂
4. Describes structure of each
```

### Categorical Problem
```
User: Show that left adjoints preserve colimits

Response flow:
1. category-theorist sets up adjunction F ⊣ G
2. Uses hom-set bijection
3. Applies uniqueness of colimits
4. Proves preservation via universal property
```

## Cross-Domain Integration

Phase 3 agents integrate with:
- **Phase 1 (Foundations)**: Logic and set theory for axiomatic foundations
- **Phase 2 (Discrete)**: Combinatorics for counting problems, lattice theory connections
- **Future phases**: Topology (algebraic topology), Geometry (algebraic geometry)

## Key Theorems Covered

### Number Theory
- Fundamental Theorem of Arithmetic
- Chinese Remainder Theorem
- Quadratic Reciprocity
- Prime Number Theorem
- Dirichlet's Theorem on Primes in Arithmetic Progressions
- Fermat's Last Theorem (statement)

### Algebra
- Fundamental Theorem of Galois Theory
- Fundamental Theorem of Finite Abelian Groups
- Wedderburn-Artin Theorem
- Sylow Theorems
- Jordan-Hölder Theorem
- Classification of Finite Simple Groups (overview)

### Category Theory
- Yoneda Lemma
- Adjoint Functor Theorems
- Equivalence of Categories
- Limits and Colimit Preservation

## References

- Hardy & Wright - An Introduction to the Theory of Numbers
- Dummit & Foote - Abstract Algebra
- Lang - Algebra
- Mac Lane - Categories for the Working Mathematician
- Atiyah & Macdonald - Introduction to Commutative Algebra
- Serre - Linear Representations of Finite Groups
