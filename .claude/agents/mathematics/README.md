# Mathematics Agent Architecture

## Overview

This directory contains a comprehensive collection of specialized agents for mathematical reasoning, computation, and research. The architecture is designed to support rigorous mathematical work from initial exploration through formal proof and publication.

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────────┐
│                    MATHEMATICS AGENT ARCHITECTURE                    │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐     │
│  │   FOUNDATIONS   │  │    ANALYSIS     │  │   COMPUTATION   │     │
│  ├─────────────────┤  ├─────────────────┤  ├─────────────────┤     │
│  │ proof-          │  │ counterexample- │  │ algorithm-      │     │
│  │   constructor   │  │   hunter        │  │   designer      │     │
│  │                 │  │                 │  │                 │     │
│  │ axiom-          │  │ pattern-        │  │ numerical-      │     │
│  │   architect     │  │   detector      │  │   analyst       │     │
│  │                 │  │                 │  │                 │     │
│  │ logic-          │  │ conjecture-     │  │ symbolic-       │     │
│  │   validator     │  │   generator     │  │   computer      │     │
│  └────────┬────────┘  └────────┬────────┘  └────────┬────────┘     │
│           │                    │                    │               │
│           └────────────────────┼────────────────────┘               │
│                                │                                    │
│                    ┌───────────▼───────────┐                       │
│                    │     INTEGRATION       │                       │
│                    ├───────────────────────┤                       │
│                    │ math-philosophy-      │                       │
│                    │   bridge              │                       │
│                    │                       │                       │
│                    │ math-research-        │                       │
│                    │   connector           │                       │
│                    │                       │                       │
│                    │ theorem-              │                       │
│                    │   documenter          │                       │
│                    └───────────────────────┘                       │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

## Directory Structure

```
mathematics/
├── README.md                 # This file
├── foundations/              # Core logical and proof-theoretic agents
│   ├── proof-constructor.md      # Builds formal proofs
│   ├── axiom-architect.md        # Designs axiom systems
│   └── logic-validator.md        # Validates logical correctness
├── analysis/                 # Pattern recognition and conjecture agents
│   ├── counterexample-hunter.md  # Finds counterexamples
│   ├── pattern-detector.md       # Identifies mathematical patterns
│   └── conjecture-generator.md   # Formulates conjectures
├── computation/              # Algorithmic and numerical agents
│   ├── algorithm-designer.md     # Designs algorithms
│   ├── numerical-analyst.md      # Numerical methods analysis
│   └── symbolic-computer.md      # Symbolic computation
└── integration/              # Cross-domain connection agents
    ├── math-philosophy-bridge.md # Connects math and philosophy
    ├── math-research-connector.md # Research and publication
    └── theorem-documenter.md     # Documentation specialist
```

## Agent Categories

### Foundations (3 agents)

These agents handle the logical bedrock of mathematical reasoning.

| Agent | Purpose | Key Capabilities |
|-------|---------|------------------|
| **proof-constructor** | Build formal proofs | Direct, contradiction, induction, contrapositive |
| **axiom-architect** | Design axiom systems | Consistency, independence, foundation selection |
| **logic-validator** | Verify logical correctness | Inference validation, gap detection |

### Analysis (3 agents)

These agents support mathematical exploration and discovery.

| Agent | Purpose | Key Capabilities |
|-------|---------|------------------|
| **counterexample-hunter** | Find counterexamples | Boundary testing, pathological construction |
| **pattern-detector** | Identify patterns | Sequence analysis, symmetry detection |
| **conjecture-generator** | Formulate conjectures | Generalization, plausibility assessment |

### Computation (3 agents)

These agents handle algorithmic and numerical work.

| Agent | Purpose | Key Capabilities |
|-------|---------|------------------|
| **algorithm-designer** | Design algorithms | Complexity analysis, correctness proofs |
| **numerical-analyst** | Numerical methods | Error analysis, stability, convergence |
| **symbolic-computer** | Symbolic computation | Algebraic manipulation, symbolic calculus |

### Integration (3 agents)

These agents connect mathematical work with broader contexts.

| Agent | Purpose | Key Capabilities |
|-------|---------|------------------|
| **math-philosophy-bridge** | Philosophy connection | Epistemological grounding, conceptual clarity |
| **math-research-connector** | Research integration | Literature, publication, collaboration |
| **theorem-documenter** | Documentation | Theorem cards, proof records, examples |

## Related Skills

The agents work with these skills from `.claude/skills/`:

| Skill | Purpose |
|-------|---------|
| `formal-proof` | Proof writing methodology and templates |
| `mathematical-modeling` | Model formulation and validation |
| `latex-typesetting` | Mathematical document formatting |

## Hive Integration

### Queen Types

Three mathematical queen types coordinate agent work:

| Queen | Focus | Decision Style |
|-------|-------|----------------|
| `mathematical-foundational` | Proofs and rigor | Deductive |
| `mathematical-computational` | Algorithms and numerics | Algorithmic |
| `mathematical-exploratory` | Patterns and discovery | Abductive |

### Worker Types

Five worker types group agents by function:

| Worker | Agents |
|--------|--------|
| `theorem-prover` | proof-constructor, axiom-architect, logic-validator |
| `counterexample-seeker` | counterexample-hunter |
| `computation-specialist` | algorithm-designer, numerical-analyst, symbolic-computer |
| `pattern-analyst` | pattern-detector, conjecture-generator |
| `math-integrator` | math-philosophy-bridge, math-research-connector, theorem-documenter |

### Swarm Configurations

Four pre-configured swarms for common workflows:

| Swarm | Purpose | Key Agents |
|-------|---------|------------|
| `proof-development` | Formal proof construction | theorem-prover, counterexample-seeker |
| `computational-mathematics` | Algorithm and numerical work | computation-specialist, theorem-prover |
| `mathematical-discovery` | Pattern finding and conjectures | pattern-analyst, counterexample-seeker |
| `theorem-verification` | Rigorous claim validation | counterexample-seeker, theorem-prover |

## Workflow Examples

### Example 1: Proving a Theorem

```
1. conjecture-generator     → Formulate precise claim
2. counterexample-hunter    → Test claim validity
3. proof-constructor        → Build formal proof
4. logic-validator          → Verify proof correctness
5. theorem-documenter       → Document the result
6. math-research-connector  → Prepare for publication
```

### Example 2: Algorithm Development

```
1. algorithm-designer       → Design the algorithm
2. numerical-analyst        → Analyze numerical properties
3. proof-constructor        → Prove correctness
4. symbolic-computer        → Verify symbolic computations
5. theorem-documenter       → Document the algorithm
```

### Example 3: Mathematical Exploration

```
1. pattern-detector         → Identify patterns in data
2. conjecture-generator     → Formulate conjectures
3. counterexample-hunter    → Test conjectures
4. proof-constructor        → Attempt proofs
5. math-philosophy-bridge   → Interpret significance
```

## Integration with Philosophy Agents

The mathematics agents connect with philosophy agents for deeper analysis:

| Math Agent | Philosophy Partners |
|------------|---------------------|
| proof-constructor | rationalist-synthesizer, foundationalist-validator |
| axiom-architect | foundationalist-validator, skeptical-challenger |
| conjecture-generator | empiricist-gatherer, skeptical-challenger |
| math-philosophy-bridge | All epistemology agents |

## Usage Guidelines

### When to Use Each Agent

- **Starting a proof**: Begin with `conjecture-generator` to clarify the claim, then `counterexample-hunter` to validate
- **Stuck on a proof**: Use `pattern-detector` to find structure, or `counterexample-hunter` to check if claim is false
- **Need computation**: Use `algorithm-designer` for discrete problems, `numerical-analyst` for continuous
- **Publishing results**: Use `math-research-connector` for context, `theorem-documenter` for documentation

### Best Practices

1. **Always validate before proving**: Run counterexample search before extensive proof attempts
2. **Document as you go**: Use theorem-documenter throughout, not just at the end
3. **Connect to philosophy**: Use math-philosophy-bridge for foundational questions
4. **Use appropriate queens**: Match queen type to task (foundational, computational, exploratory)

## Quality Standards

All agents follow these standards:

- **Rigor**: Every claim must be justified
- **Clarity**: Explanations accessible to target audience
- **Completeness**: No gaps in reasoning
- **Verification**: Results independently checkable
- **Documentation**: Comprehensive records maintained

## References

Key texts informing these agents:

- Velleman, D.J. (2019). *How to Prove It*
- Cormen, T.H. et al. (2009). *Introduction to Algorithms*
- Trefethen, L.N. & Bau, D. (1997). *Numerical Linear Algebra*
- Polya, G. (1954). *Mathematics and Plausible Reasoning*
- Shapiro, S. (2000). *Thinking about Mathematics*

