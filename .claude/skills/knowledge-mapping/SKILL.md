---
name: Knowledge Mapping
version: 1.0.0
description: Epistemic state visualization through known/unknown tracking and belief dependency networks
category: Philosophical Research Methods
difficulty: Intermediate
estimatedTime: Variable (depends on domain complexity)
---

# Knowledge Mapping

A methodology for visualizing and tracking epistemic states - what is known, unknown, uncertain, and how beliefs relate to each other. Enables researchers to see the structure of their knowledge, identify gaps, and understand how beliefs depend on one another.

## What This Skill Does

Knowledge Mapping enables researchers to:
- Track what is known vs. unknown in a domain
- Visualize belief structures and dependencies
- Identify knowledge gaps and priorities
- Monitor epistemic progress over time

## Prerequisites

- Basic understanding of epistemological concepts
- Familiarity with network/graph concepts
- Experience with research documentation

---

## Core Concepts

### The Epistemic State Space

```
KNOWLEDGE STATES

┌─────────────────────────────────────────────────────┐
│                                                     │
│   KNOWN                 UNCERTAIN                   │
│   ┌─────────┐          ┌─────────────┐              │
│   │Justified│          │ Partially   │              │
│   │ True    │          │ Justified   │              │
│   │ Belief  │          │             │              │
│   └─────────┘          └─────────────┘              │
│                                                     │
│   UNKNOWN              MISTAKEN                     │
│   ┌─────────┐          ┌─────────────┐              │
│   │Questions│          │  Justified  │              │
│   │Not Yet  │          │  False      │              │
│   │Answered │          │  Belief     │              │
│   └─────────┘          └─────────────┘              │
│                                                     │
│   META-UNKNOWN                                      │
│   ┌─────────────────────────────────┐               │
│   │ Don't know what we don't know   │               │
│   └─────────────────────────────────┘               │
│                                                     │
└─────────────────────────────────────────────────────┘
```

### Belief Relationships

```
DEPENDENCY TYPES

SUPPORT: A supports B
├── Entailment: A logically implies B
├── Evidence: A is evidence for B
├── Explanation: A explains B
└── Coherence: A fits well with B

CONFLICT: A conflicts with B
├── Contradiction: A and not-A
├── Tension: A makes B less likely
└── Competition: A and B compete to explain C

DERIVATION: B is derived from A
├── Deduction: B follows logically from A
├── Induction: B generalizes from A
└── Abduction: B best explains A
```

---

## Knowledge Inventory

### Inventory Protocol

```
Phase 1: Domain Scoping
- What domain are we mapping?
- What are the boundaries?
- What level of granularity?

Phase 2: Belief Collection
- What do we believe about this domain?
- What claims are we committed to?
- What assumptions are we making?

Phase 3: Confidence Rating
- How confident are we in each belief?
- What justifies this confidence?
- How would we rate our uncertainty?

Phase 4: Status Classification
- Known (justified true belief)
- Believed (held but uncertain)
- Suspected (weakly held)
- Unknown (recognized gap)
- Questionable (under doubt)

Phase 5: Relationship Mapping
- What supports what?
- What conflicts with what?
- What depends on what?
```

### Belief Inventory Template

| Belief | Content | Confidence | Status | Justification | Dependencies |
|--------|---------|------------|--------|---------------|--------------|
| B1 | [Statement] | [0-1] | [Status] | [Why believed] | [What it depends on] |
| B2 | [Statement] | [0-1] | [Status] | [Why believed] | [What it depends on] |
| ... | ... | ... | ... | ... | ... |

---

## Known/Unknown Tracking

### Unknown Classification

| Type | Description | Example |
|------|-------------|---------|
| **Identified Unknown** | Know we don't know | "We don't know the mechanism" |
| **Bounded Unknown** | Know the space of possibilities | "Either A, B, or C, but which?" |
| **Open Unknown** | Don't know the possibilities | "Something is causing X" |
| **Meta-Unknown** | Don't know what we don't know | "What are we missing?" |

### Gap Analysis Protocol

```
For each domain area:

1. INVENTORY QUESTIONS
   - What questions have answers?
   - What questions lack answers?
   - What questions haven't been asked?

2. CLASSIFY GAPS
   - Answerable with existing methods?
   - Requires new methods/data?
   - May be unanswerable?

3. PRIORITIZE GAPS
   - Importance for goals?
   - Feasibility of filling?
   - Dependencies on filling?

4. TRACK PROGRESS
   - Gaps filled over time
   - New gaps discovered
   - Gap status changes
```

### Knowledge Progress Dashboard

```
DOMAIN: [Name]
As of: [Date]

COVERAGE
├── Known: [X%]
├── Uncertain: [Y%]
├── Unknown: [Z%]
└── Meta-Unknown: [?%]

KEY KNOWNS
1. [Statement] (Confidence: High)
2. [Statement] (Confidence: High)
...

KEY UNKNOWNS
1. [Question] (Priority: High)
2. [Question] (Priority: Medium)
...

RECENT CHANGES
├── Newly known: [List]
├── Confidence raised: [List]
├── Confidence lowered: [List]
└── New questions: [List]
```

---

## Belief Dependency Networks

### Network Construction

```
BUILDING THE NETWORK

Nodes:
- Each belief is a node
- Color by status (known/uncertain/unknown)
- Size by importance
- Shape by type (factual/normative/conceptual)

Edges:
- Support relations (solid lines)
- Conflict relations (dashed lines)
- Derivation chains (arrows)
- Strength by line thickness

Clusters:
- Group related beliefs
- Identify isolated beliefs
- Find central/peripheral beliefs
```

### Network Analysis

```
STRUCTURAL ANALYSIS

Centrality
- Which beliefs are most connected?
- Which are most depended upon?
- Which are bridges between clusters?

Vulnerability
- Single points of failure?
- What if foundational beliefs are wrong?
- Which beliefs are least supported?

Coherence
- Well-integrated clusters?
- Isolated beliefs needing connection?
- Conflicts needing resolution?

Foundations
- What are the basic beliefs?
- How deep do justification chains go?
- Are foundations solid?
```

### Network Metrics

```javascript
networkMetrics = {
  totalBeliefs: n,
  knownBeliefs: n_known,
  uncertainBeliefs: n_uncertain,
  unknownQuestions: n_unknown,

  supportConnections: n_support,
  conflictConnections: n_conflict,

  avgConnections: avg_degree,
  clustering: clustering_coefficient,

  foundationalBeliefs: foundations,
  centralBeliefs: high_centrality,
  vulnerableBeliefs: low_support
}
```

---

## Justification Graphs

### Graph Construction

```
JUSTIFICATION STRUCTURE

For belief B:

B is justified by:
├── Evidence E1, E2, ...
├── Reasoning R1, R2, ...
├── Testimony T1, T2, ...
└── Other beliefs B1, B2, ...

Tracing backward:
B ← B1 ← B2 ← ... ← Foundation

Graph shows:
- What ultimately grounds B?
- How long are justification chains?
- Where are the weak links?
```

### Chain Quality Assessment

```
For each justification chain:

COMPLETENESS
- Are all links present?
- Any gaps in reasoning?
- Implicit steps made explicit?

STRENGTH
- Each link strong or weak?
- Overall chain strength?
- Weakest link identified?

TERMINATION
- Reaches foundation?
- Circular?
- Infinite regress?
- Arbitrary stop?

Quality Rating: [Strong / Moderate / Weak / Problematic]
```

---

## Integration with Claude Flow

### Spawning Knowledge Mapping

```bash
# Run knowledge mapping
claude-flow hive-mind spawn "Map knowledge state for [domain]" \
  --queen epistemic \
  --workers coherentist-integrator,foundationalist-validator,network-epistemologist
```

### Memory Patterns

```javascript
// Store knowledge map
mcp__claude-flow__memory_usage({
  action: "store",
  key: "knowledge/map/[domain]",
  namespace: "philosophical",
  value: JSON.stringify({
    domain: domainName,
    beliefInventory: beliefs,
    networkStructure: networkGraph,
    knownUnknownStatus: statusCounts,
    gapAnalysis: identifiedGaps,
    justificationChains: justificationGraph,
    metrics: networkMetrics,
    lastUpdated: timestamp
  })
})
```

---

## Output Templates

### Knowledge Map Report

```
KNOWLEDGE MAP: [Domain]
Date: [Date]

SCOPE
[Description of domain boundaries]

SUMMARY STATISTICS
- Total beliefs mapped: [N]
- Known (high confidence): [N]
- Uncertain (medium confidence): [N]
- Low confidence: [N]
- Identified unknowns: [N]

CORE KNOWLEDGE
Foundational beliefs:
1. [Belief] - [Justification summary]
2. [Belief] - [Justification summary]
...

Central beliefs (highly connected):
1. [Belief] - [Why central]
2. [Belief] - [Why central]
...

GAP ANALYSIS
High-priority unknowns:
1. [Question] - [Why important]
2. [Question] - [Why important]
...

Known limitations:
- [Limitation 1]
- [Limitation 2]
...

NETWORK STRUCTURE
[Visual or description]
- Clusters identified: [List]
- Isolated beliefs: [List]
- Conflicts present: [List]

VULNERABILITY ASSESSMENT
- Single points of failure: [List]
- Weak justification chains: [List]
- Beliefs needing more support: [List]

RECOMMENDATIONS
1. [Priority action]
2. [Priority action]
...
```

### Knowledge Change Log

```
KNOWLEDGE CHANGE LOG: [Domain]

[Date] - [Change Type] - [Description]
├── ADDED: New belief added
├── REVISED: Belief content changed
├── CONFIDENCE_UP: Confidence increased
├── CONFIDENCE_DOWN: Confidence decreased
├── REMOVED: Belief removed
├── GAP_FILLED: Unknown became known
├── GAP_DISCOVERED: New unknown identified
└── CONNECTION: New relationship mapped
```

---

## Quality Criteria

Knowledge mapping is successful when:

1. **Completeness**: Relevant beliefs inventoried
2. **Accuracy**: Relationships correctly mapped
3. **Clarity**: Status distinctions clear
4. **Usefulness**: Gaps and priorities identified
5. **Currency**: Map updated as knowledge changes
6. **Actionability**: Recommendations are practical

---

## Troubleshooting

### "Too many beliefs to map"
→ Focus on core domain
→ Increase granularity level
→ Map in sections

### "Dependencies unclear"
→ Ask "what justifies this?"
→ Trace backward systematically
→ Accept some uncertainty

### "Can't identify unknowns"
→ Look for questions in literature
→ Ask experts what's contested
→ Examine assumptions critically

### "Map is getting outdated"
→ Schedule regular updates
→ Log changes incrementally
→ Flag time-sensitive beliefs

---

## Learn More

- Pritchard, D. (2018). What is this thing called Knowledge?
- Sosa, E. et al. (2008). Epistemology: An Anthology
- Goldman, A. & Blanchard, T. (2018). Social Epistemology
