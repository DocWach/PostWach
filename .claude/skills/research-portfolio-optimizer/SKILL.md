---
name: Research Portfolio Optimizer
description: Decide which of the 25 SE Math Foundations research ideas to pursue next, based on expected research value, feasibility, dependency chains, and resource constraints
---

# Research Portfolio Optimizer

A meta-research capability for the SE Math Foundations 25-idea portfolio. It does not do the research — it helps decide what research to do and when, using expected-value reasoning, dependency analysis, and resource-constrained optimization.

## When to Use This Skill

- Choosing the next idea to pursue after finishing a paper
- Scoping an NSF proposal (which subset of ideas maximizes proposal strength?)
- Quarterly portfolio review (are priorities still correct given new information?)
- Evaluating whether to investigate an idea further before committing resources
- Rebalancing after a paper is rejected, accepted, or an opportunity emerges

---

## Quick Start

```bash
# Run full portfolio analysis
claude-flow hive-mind spawn "Analyze SE Math Foundations portfolio: score all 25 ideas, identify optimal next idea given current state" \
  --queen research-strategic \
  --workers probabilist,optimization-specialist,consequence-tracer,fallibilist-reviewer
```

---

## Core Methodology

### Portfolio Assessment Framework

Score each idea on 5 dimensions (1-5 scale each, anchored below):

#### 1. Research Value (RV)

How much does this idea contribute to the field if successful?

| Score | Anchor |
|---|---|
| 5 | Novel framework or paradigm shift; highly citable |
| 4 | Significant extension of existing theory; fills a recognized gap |
| 3 | Useful contribution; incremental advance |
| 2 | Confirmatory or replication study; limited novelty |
| 1 | Minor variation; unlikely to attract citations |

#### 2. Feasibility (F)

Can this idea be executed with available methodology, data, and expertise?

| Score | Anchor |
|---|---|
| 5 | Methodology proven, data in hand, expertise available |
| 4 | Methodology exists, minor adaptation needed |
| 3 | Methodology exists but requires substantial development |
| 2 | Methodology uncertain; significant unknowns |
| 1 | No clear methodology; fundamental obstacles |

#### 3. Strategic Alignment (SA)

Does this idea serve near-term strategic objectives?

| Score | Anchor |
|---|---|
| 5 | Directly serves active NSF proposal year; satisfies multiple dependencies |
| 4 | Serves upcoming proposal year; satisfies one dependency |
| 3 | Indirectly supports portfolio; no immediate proposal link |
| 2 | Tangential; opportunistic only |
| 1 | Does not serve any current strategic objective |

#### 4. Resource Cost (RC)

How much effort and coordination does this idea require? (Inverted: lower cost = higher score)

| Score | Anchor |
|---|---|
| 5 | Solo author, < 3 months, no IRB, no special equipment |
| 4 | Solo or 2 authors, 3-6 months, minor logistics |
| 3 | Small team, 6-12 months, moderate logistics |
| 2 | Multi-institution team, > 12 months, IRB required |
| 1 | Large team, multi-year, significant infrastructure/funding |

#### 5. Dependency Readiness (DR)

Are prerequisite ideas complete or sufficiently advanced?

| Score | Anchor |
|---|---|
| 5 | No dependencies, or all dependencies complete |
| 4 | Dependencies in progress and on track |
| 3 | One dependency incomplete but workaround exists |
| 2 | Multiple incomplete dependencies |
| 1 | Critical dependency blocked or not started |

#### Composite Score

```
Expected Portfolio Value (EPV) = w_rv * RV + w_f * F + w_sa * SA + w_rc * RC + w_dr * DR
```

Default weights (sum to 1.0):
- w_rv = 0.25 (Research Value)
- w_f  = 0.20 (Feasibility)
- w_sa = 0.25 (Strategic Alignment)
- w_rc = 0.10 (Resource Cost)
- w_dr = 0.20 (Dependency Readiness)

Adjust weights per decision context (e.g., increase w_sa when scoping a proposal, increase w_f when time-constrained).

---

### Dependency Graph

The 25 ideas form a directed acyclic graph. Arrows indicate "must precede" (finish-to-start) relationships.

```
DEPENDENCY STRUCTURE

Foundation Layer (must come first):
  Idea 5 (Isomorphism Catalog) ──→ Idea 6 (Morphism Metric)
                                        │
                                        ▼
                                   Idea 3 (Bayesian Confidence)

Idea 5 ──→ Ideas 20, 21, 22, 23, 24, 25 (Year 3 cognitive studies)
Idea 6 ──→ Ideas 20, 21, 22, 23, 24, 25 (Year 3 cognitive studies)

Containment:
  Idea 8 (Biomimetics) ⊃ Idea 12 (Immune/Cyber)
  — Idea 12 is a subset/special case of Idea 8

Capstone:
  Ideas 5-18 ──→ Idea 19 (Minimum Math Toolkit synthesis)

Independent (no inbound dependencies):
  Ideas 1, 2, 4, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18

NSF First Proposal Cluster:
  Ideas 5, 6, 3, 20, 21, 23
  Critical path: 5 → 6 → 3 (formal foundations)
                 5,6 → 20,21,23 (cognitive studies, Year 3)
```

#### Current State (as of February 2026)

| Idea | Status | Notes |
|---|---|---|
| 5 | In Progress | Current paper (isomorphism catalog) |
| 3 | Next | Draft exists from prior work |
| 1-2, 4, 6-25 | Captured | Ideas documented, not yet started |

---

### Expected Value of Information (EVOI)

Before committing to an idea, ask: **is it worth investigating further first?**

```
EVOI = (Value of optimal decision with more info) - (Value of optimal decision now)
```

Use EVOI when:
- An idea scores high on RV but low on F (uncertain feasibility — would a pilot study resolve it?)
- Two ideas are close in EPV (would reading 5 more papers clarify which is stronger?)
- An external event may change SA scores (wait for NSF solicitation release?)

#### EVOI Decision Rule

| EVOI vs. Investigation Cost | Action |
|---|---|
| EVOI >> Cost | Investigate before committing |
| EVOI ≈ Cost | Judgment call; consider risk tolerance |
| EVOI << Cost | Commit now; investigation not worth the delay |

Investigation actions (low cost): targeted literature scan, 1-hour feasibility sketch, email a potential co-author, check data availability.

---

### Portfolio Optimization

Given scores and constraints, select the subset of ideas that maximizes total expected value.

#### Constraint Types

1. **Time budget:** Total available research-months in the planning horizon
2. **Dependency ordering:** Cannot start an idea before its prerequisites reach a sufficient state
3. **Proposal coherence:** Ideas in an NSF proposal must form a coherent narrative
4. **Parallelism limit:** At most N ideas in progress simultaneously (typically 2-3)

#### Selection Algorithm

```
1. Score all 25 ideas on the 5 dimensions
2. Compute EPV for each idea
3. Filter out ideas with DR < 3 (dependencies not ready)
4. Rank remaining ideas by EPV
5. Apply constraints:
   a. Check time budget against RC estimates
   b. Verify dependency ordering is respected
   c. If scoping a proposal, check narrative coherence
6. Select top-K ideas that satisfy all constraints
7. Identify the single "next idea" (highest EPV among ready ideas)
```

---

## Scoring Templates

### Per-Idea Assessment

```
IDEA ASSESSMENT: Idea [#] — [Title]
Date: [YYYY-MM-DD]
Assessor: [Name]

Research Value (RV):     [1-5]  Rationale: ___
Feasibility (F):         [1-5]  Rationale: ___
Strategic Alignment (SA):[1-5]  Rationale: ___
Resource Cost (RC):      [1-5]  Rationale: ___
Dependency Readiness (DR):[1-5] Rationale: ___

EPV = 0.25*[RV] + 0.20*[F] + 0.25*[SA] + 0.10*[RC] + 0.20*[DR] = ___

EVOI Assessment:
- Key uncertainty: ___
- Investigation action: ___
- Estimated EVOI: [High/Medium/Low]
- Estimated investigation cost: [Hours/days]
- Decision: [Investigate first / Commit now / Defer]

Notes: ___
```

### Portfolio Summary Matrix

```
PORTFOLIO SUMMARY — [Date]

| # | Idea (short) | RV | F | SA | RC | DR | EPV | Status | Decision |
|---|---|---|---|---|---|---|---|---|---|
| 1 | SysML v2 Analysis | | | | | | | Captured | |
| 2 | VM & Digital Twins | | | | | | | Captured | |
| 3 | Bayesian Confidence | | | | | | | Next | |
| 4 | CWA / Neuro-Symbolic | | | | | | | Captured | |
| 5 | Isomorphism Catalog | | | | | | | In Progress | |
| 6 | Morphism Metric | | | | | | | Captured | |
| 7 | Verification Req Types | | | | | | | Captured | |
| 8 | Biomimetics | | | | | | | Captured | |
| 9 | Ontological Repr. | | | | | | | Captured | |
| 10 | Compositional Emergence | | | | | | | Captured | |
| 11 | DEVS/T3SD Boundaries | | | | | | | Captured | |
| 12 | Immune/Cyber | | | | | | | Captured | |
| 13 | Morphisms vs. TL | | | | | | | Captured | |
| 14 | Set-Based Design | | | | | | | Captured | |
| 15 | Homomorphic Encryption | | | | | | | Captured | |
| 16 | Category Theory SE | | | | | | | Captured | |
| 17 | AI Morphism Discovery | | | | | | | Captured | |
| 18 | Human-in-Loop V&V | | | | | | | Captured | |
| 19 | Min Math Toolkit | | | | | | | Captured | |
| 20 | Hidden Beliefs | | | | | | | Captured | |
| 21 | Heuristic Accuracy | | | | | | | Captured | |
| 22 | Layer-Selective Attn | | | | | | | Captured | |
| 23 | Mental Model Fidelity | | | | | | | Captured | |
| 24 | Tacit Knowledge | | | | | | | Captured | |
| 25 | Design Decision Trace | | | | | | | Captured | |

Top 3 by EPV: Idea __, Idea __, Idea __
Recommended next: Idea __ because ___
```

---

## Decision Protocols

### "What Should I Work on Next?"

1. Update current state (which ideas changed status since last review?)
2. Re-score any ideas whose inputs changed (new dependency completed, new information)
3. Run the selection algorithm
4. Check EVOI for the top candidate — is investigation warranted?
5. Commit or investigate

### NSF Proposal Scoping

1. Identify the proposal year and available budget
2. Filter ideas to those aligned with the proposal theme
3. Score the filtered set with w_sa = 0.35 (elevated strategic weight)
4. Verify the selected subset forms a coherent narrative arc
5. Check that the critical path fits within the proposal timeline
6. Confirm the first-proposal cluster: Ideas 5, 6, 3, 20, 21, 23

### Quarterly Review

1. Update all 25 idea statuses
2. Re-score ideas with changed circumstances
3. Review the dependency graph for newly unblocked ideas
4. Check alignment with NSF proposal timeline
5. Adjust weights if strategic context shifted
6. Document decisions in the portfolio summary matrix
7. Store results to Claude Flow memory for longitudinal tracking

---

## Integration with Claude Flow

### Spawn Portfolio Analysis

```bash
# Full portfolio scoring
claude-flow hive-mind spawn "Score all 25 SE Math Foundations ideas using the 5-dimension portfolio framework. Current state: Idea 5 in progress, Idea 3 next. Compute EPV with default weights." \
  --queen research-strategic \
  --workers probabilist,optimization-specialist,consequence-tracer,fallibilist-reviewer

# Next-idea recommendation
claude-flow hive-mind spawn "Given current portfolio state, recommend the single best next idea to pursue. Apply EVOI check to top 3 candidates." \
  --queen research-strategic \
  --workers probabilist,optimization-specialist,fallibilist-reviewer

# NSF proposal scoping
claude-flow hive-mind spawn "Scope NSF EDSE first proposal. Evaluate coherence and timeline feasibility of Ideas 5,6,3,20,21,23. Identify risks." \
  --queen research-strategic \
  --workers probabilist,consequence-tracer,fallibilist-reviewer
```

### Memory Storage

```bash
# Store portfolio assessment
claude-flow memory store \
  --key "portfolio/assessment/$(date +%Y-%m-%d)" \
  --value '{"ideas": [scored_ideas], "weights": {...}, "recommendation": "...", "next_review": "..."}' \
  --namespace research-strategy

# Store individual idea score
claude-flow memory store \
  --key "portfolio/idea/[N]/score/$(date +%Y-%m-%d)" \
  --value '{"RV": N, "F": N, "SA": N, "RC": N, "DR": N, "EPV": N, "decision": "..."}' \
  --namespace research-strategy

# Retrieve last assessment for comparison
claude-flow memory search --query "portfolio assessment" --namespace research-strategy
```

---

## Output Templates

### Recommendation Memo

```
PORTFOLIO RECOMMENDATION MEMO
Date: [YYYY-MM-DD]
Context: [Next paper / NSF scoping / Quarterly review]

CURRENT STATE:
- Ideas in progress: [list]
- Ideas completed: [list]
- Newly unblocked: [list]

RECOMMENDATION: Pursue Idea [#] — [Title]

RATIONALE:
- EPV: [score] (rank [X] of 25)
- Key strengths: [dimensions]
- Key risks: [dimensions]
- EVOI check: [result]

ALTERNATIVE CONSIDERED: Idea [#] — [Title]
- EPV: [score]
- Why not chosen: ___

DEPENDENCY IMPACT:
- Completing this idea unblocks: [list]
- Completing this idea advances proposal: [yes/no, which]

RESOURCE ESTIMATE:
- Duration: [months]
- Team: [solo / co-author needed]
- Special requirements: [IRB, data, equipment]

NEXT REVIEW: [date]
```

### Idea Comparison Matrix

```
HEAD-TO-HEAD COMPARISON: Idea [A] vs Idea [B]

| Dimension | Idea [A] | Idea [B] | Advantage |
|---|---|---|---|
| Research Value | | | |
| Feasibility | | | |
| Strategic Alignment | | | |
| Resource Cost | | | |
| Dependency Readiness | | | |
| EPV | | | |

Qualitative factors:
- ___
- ___

Recommendation: Idea [__] because ___
```
