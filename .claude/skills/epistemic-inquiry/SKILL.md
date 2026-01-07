---
name: Epistemic Inquiry
version: 1.0.0
description: Structured questioning methodology using Socratic dialogue patterns and belief mapping
category: Philosophical Research Methods
difficulty: Intermediate
estimatedTime: Variable (depends on inquiry scope)
---

# Epistemic Inquiry

A systematic methodology for investigating knowledge claims through structured questioning. Combines Socratic dialogue techniques with contemporary epistemological analysis to surface assumptions, test justifications, and refine understanding.

## What This Skill Does

Epistemic Inquiry enables researchers to:
- Ask questions that reveal hidden assumptions
- Test the justification of knowledge claims
- Map belief structures and their dependencies
- Refine concepts through systematic examination

## Prerequisites

- Basic familiarity with epistemological concepts
- Comfort with abstract reasoning
- Willingness to question assumptions

---

## Core Methodology

### The Inquiry Cycle

```
┌────────────────────────────────────────────────────────┐
│                                                        │
│  1. CLAIM IDENTIFICATION                               │
│     └─> What is being claimed?                         │
│         Who holds this belief?                         │
│         What does it mean?                             │
│                                                        │
│  2. CLARIFICATION                                      │
│     └─> What do key terms mean?                        │
│         Can examples be given?                         │
│         What is the scope?                             │
│                                                        │
│  3. ASSUMPTION SURFACING                               │
│     └─> What must be true for this?                    │
│         What is presupposed?                           │
│         What is taken for granted?                     │
│                                                        │
│  4. JUSTIFICATION PROBING                              │
│     └─> What evidence supports this?                   │
│         Why should we believe this?                    │
│         How do you know?                               │
│                                                        │
│  5. IMPLICATION TRACING                                │
│     └─> If true, what follows?                         │
│         What are the consequences?                     │
│         What else must be true?                        │
│                                                        │
│  6. REVISION AND REFINEMENT                            │
│     └─> Should the claim be modified?                  │
│         What have we learned?                          │
│         What questions remain?                         │
│                                                        │
└────────────────────────────────────────────────────────┘
```

---

## Question Taxonomies

### By Purpose

| Type | Purpose | Example Questions |
|------|---------|-------------------|
| Clarifying | Define meaning | "What do you mean by X?" "Can you give an example?" |
| Probing | Surface assumptions | "What are you assuming?" "What must be true?" |
| Evidence-Seeking | Ground claims | "What evidence supports this?" "How do you know?" |
| Reasoning | Check logic | "How does this follow?" "What's the inference?" |
| Implication | Trace consequences | "If true, what follows?" "What are the implications?" |
| Alternative | Consider options | "Could it be otherwise?" "What's another view?" |
| Meta | Examine the inquiry | "Is this the right question?" "Why does this matter?" |

### By Target

```
CONCEPTUAL QUESTIONS
- What is the definition of X?
- How does X differ from Y?
- Is X a type of Z?

FACTUAL QUESTIONS
- Is it true that P?
- What is the evidence for P?
- How was this determined?

NORMATIVE QUESTIONS
- Should we believe P?
- Is this justified?
- What ought we conclude?

METHODOLOGICAL QUESTIONS
- How should we investigate X?
- What methods are appropriate?
- How can we verify this?
```

---

## Belief Mapping

### Individual Belief Analysis

```
For any belief B:

1. CONTENT
   - What exactly is believed?
   - What does it assert?
   - What would make it true/false?

2. JUSTIFICATION
   - Why is this believed?
   - What supports it?
   - How strong is the support?

3. DEPENDENCIES
   - What other beliefs does it depend on?
   - What depends on it?
   - How connected is it?

4. CONFIDENCE
   - How certain is the believer?
   - How certain should they be?
   - What would change confidence?

5. REVISION CONDITIONS
   - What would defeat this belief?
   - Under what conditions should it be revised?
   - How revisable is it?
```

### Belief Network Mapping

```
MAPPING PROCEDURE

1. Identify core beliefs in domain
2. For each belief, identify:
   - Supporting beliefs (what it depends on)
   - Supported beliefs (what depends on it)
   - Conflicting beliefs (what it tensions with)
3. Draw network showing relationships
4. Identify:
   - Central beliefs (many connections)
   - Peripheral beliefs (few connections)
   - Foundational beliefs (support but not supported)
   - Derived beliefs (supported but don't support)
   - Isolated beliefs (disconnected)
```

---

## Socratic Dialogue Patterns

### Pattern 1: The Elenchus

```
1. Interlocutor states belief
2. Examiner seeks clarification
3. Examiner elicits additional beliefs
4. Examiner shows beliefs are inconsistent
5. Interlocutor revises beliefs
6. Process repeats with refined belief
```

### Pattern 2: Maieutic (Midwifery)

```
1. Examiner asks leading questions
2. Interlocutor discovers answer within
3. Knowledge is "delivered" not transmitted
4. Interlocutor owns the insight
```

### Pattern 3: Dialectic

```
1. Thesis stated
2. Antithesis developed
3. Contradiction exposed
4. Synthesis achieved
5. Synthesis becomes new thesis
```

---

## Assumption Analysis

### Types of Assumptions

| Type | Description | How to Surface |
|------|-------------|----------------|
| Explicit | Stated as premises | "You said X. Is that an assumption?" |
| Implicit | Unstated but present | "What are you taking for granted?" |
| Background | Shared context | "What common ground are we standing on?" |
| Structural | Built into framing | "Does this question assume X?" |

### Assumption Testing Protocol

```
For each assumption A:

1. MAKE EXPLICIT
   - State the assumption clearly
   - Confirm understanding

2. EVALUATE NECESSITY
   - Is A necessary for the claim?
   - Could claim hold without A?

3. ASSESS PLAUSIBILITY
   - How likely is A to be true?
   - What evidence supports A?

4. CONSIDER ALTERNATIVES
   - What if A were false?
   - What would follow?

5. TRACE DEPENDENCIES
   - What does A depend on?
   - What depends on A?
```

---

## Integration with Claude Flow

### Spawning Epistemic Inquiry

```bash
# Run epistemic inquiry
claude-flow hive-mind spawn "Investigate [claim/topic]" \
  --queen epistemic \
  --workers socratic-examiner,empiricist-gatherer,skeptical-challenger
```

### Memory Patterns

```javascript
// Store inquiry state
mcp__claude-flow__memory_usage({
  action: "store",
  key: "inquiry/epistemic/[topic]",
  namespace: "philosophical",
  value: JSON.stringify({
    claimExamined: targetClaim,
    questionsAsked: questionSequence,
    assumptionsSurfaced: identifiedAssumptions,
    justificationsProbed: justificationAnalysis,
    beliefMap: networkVisualization,
    refinedUnderstanding: conclusions
  })
})
```

---

## Output Templates

### Epistemic Inquiry Report

```
EPISTEMIC INQUIRY: [Topic]
Date: [Date]

CLAIM EXAMINED
- Original claim: [Statement]
- Clarified claim: [Refined statement]
- Key terms defined: [Definitions]

ASSUMPTIONS SURFACED
1. [Assumption] - [Evaluation]
2. [Assumption] - [Evaluation]
...

JUSTIFICATION ANALYSIS
- Evidence cited: [List]
- Reasoning examined: [Analysis]
- Gaps identified: [Gaps]

IMPLICATIONS TRACED
- If true: [Consequences]
- Conflicts with: [Tensions]

QUESTIONS ASKED
1. [Question] → [Finding]
2. [Question] → [Finding]
...

BELIEF MAP
[Visualization or description]

REVISED UNDERSTANDING
- Original position: [Statement]
- Revised position: [Statement]
- Confidence level: [Assessment]

REMAINING QUESTIONS
1. [Question]
2. [Question]
...
```

---

## Quality Criteria

Epistemic inquiry is successful when:

1. **Clarity**: Key terms are defined
2. **Depth**: Assumptions are surfaced
3. **Rigor**: Justifications are probed
4. **Fairness**: Positions charitably reconstructed
5. **Productivity**: Understanding advances
6. **Documentation**: Process is recorded

---

## Troubleshooting

### "Questions aren't generating insight"
→ Try different question types
→ Go deeper on assumptions
→ Ask meta-questions about the inquiry

### "Interlocutor is defensive"
→ Emphasize collaborative truth-seeking
→ Use maieutic rather than elenctic approach
→ Acknowledge good points

### "Going in circles"
→ Map the belief network explicitly
→ Identify the loop
→ Find new entry points

### "Too many assumptions to handle"
→ Prioritize by importance
→ Focus on most questionable
→ Accept some as given for now

---

## Learn More

- Plato. Meno, Euthyphro, Theaetetus
- Sosa, E. (1991). Knowledge in Perspective
- Zagzebski, L. (1996). Virtues of the Mind
