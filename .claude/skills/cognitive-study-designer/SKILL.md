---
name: Cognitive Study Designer
description: Design human-subjects studies investigating how engineers reason about cross-domain morphisms, supporting Ideas 20-25 (NSF EDSE Year 3)
---

# Cognitive Study Designer

A study design capability for investigating engineer cognition about cross-domain morphisms. Provides methodology for think-aloud protocols, calibration studies, expert-novice comparisons, and IRB preparation. Does not perform psychometric analysis itself (that is the `psychometrics-analyst` agent) — it provides the study design methodology and templates for all six NSF Year 3 cognitive studies.

## When to Use This Skill

- Designing a study for any of Ideas 20-25 (NSF EDSE Year 3 cognitive studies)
- Creating think-aloud or structured interview protocols for engineer morphism reasoning
- Planning calibration studies comparing engineer confidence to formal morphism quality
- Designing expert-novice comparisons on morphism reasoning tasks
- Preparing IRB applications for human-subjects research with engineers
- Selecting and justifying psychometric methods for measuring morphism reasoning

---

## Quick Start

```bash
# Design a study for a specific idea (e.g., Idea 20: Hidden Beliefs)
claude-flow hive-mind spawn "Design study protocol for Idea 20 (Hidden Beliefs and Calibration). Follow the study design template. Produce protocol, instruments, sample size justification, and IRB elements." \
  --queen research-strategic \
  --workers psychometrics-analyst,methodology-advisor,research-architect,peer-review-responder

# Design calibration instruments (Ideas 20, 21)
claude-flow hive-mind spawn "Design calibration instruments for measuring engineer confidence against morphism quality metric (Idea 6). Include elicitation items, confidence rating scales, and scoring procedures." \
  --queen research-strategic \
  --workers psychometrics-analyst,methodology-advisor,probabilist

# Plan expert-novice comparison (Ideas 22, 24)
claude-flow hive-mind spawn "Design expert-novice comparison study for Idea 22 (Layer-Selective Attention). Define stratification criteria, minimum sample sizes per level, and between-group analysis plan." \
  --queen research-strategic \
  --workers psychometrics-analyst,methodology-advisor,research-architect
```

---

## Core Methodology

### Shared Study Infrastructure

All six Ideas (20-25) share common infrastructure. Design each study using these shared elements before adding idea-specific methods.

**Ground truth instruments:**
- Isomorphism catalog (Idea 5): structured set of formally characterized domain pairs with variable mappings, morphism types, and tier classifications
- Morphism quality metric (Idea 6): 5-layer quantitative measure (structural, behavioral, energy, information, categorical) providing a formal score for any proposed cross-domain mapping

**Participant pool:**
- Engineers stratified by domain expertise: novice (<2 yr cross-domain practice), intermediate (2-10 yr), expert (>10 yr)
- Recruitment from: UA engineering programs (graduate students = novice/intermediate), industry partners (intermediate/expert), professional societies (expert)
- Target: minimum 3 expertise levels for between-group comparisons

**Common instruments:**
- Catalog-based elicitation: present domain pairs from the isomorphism catalog; ask participants to identify variable mappings, assess morphism quality, state confidence
- Confidence rating scales: 0-100 probability scale for "How confident are you that this analogy is structurally valid?" — anchored at 0 (no confidence), 50 (coin flip), 100 (certain)
- Morphism quality scoring: participants' proposed mappings scored against Idea 6 metric by the research team

**IRB requirement:** All six studies involve human subjects performing cognitive tasks. Minimal risk (no deception, no intervention beyond cognitive tasks). See IRB Protocol Framework below.

### Idea-Study Mapping

| Idea | Title | Study Type | Primary Method | Key Measure |
|---|---|---|---|---|
| 20 | Hidden Beliefs & Calibration | Elicitation + Calibration | Think-aloud + structured interview | Assumed vs. actual morphism quality; calibration score |
| 21 | Heuristic Accuracy | Measurement | Heuristic elicitation + metric comparison | Heuristic accuracy (deviation from formal metric) |
| 22 | Layer-Selective Attention | Observation + Intervention | Think-aloud with layer coding | Layer attention distribution; pre/post training comparison |
| 23 | Mental Model Fidelity | Measurement | Model elicitation under load | Mental-model-to-formal-model morphism quality |
| 24 | Tacit Knowledge | Elicitation | Structured interview with catalog | New partial morphisms surfaced; knowledge gap analysis |
| 25 | Decision Traceability | Retrospective analysis | Failure trace-back protocol | Morphism assumption identified per failure |

### Protocol Analysis Methodology

**Think-aloud protocol design (Ericsson & Simon framework):**
- Concurrent verbalization (Level 2): participants verbalize thoughts while performing morphism reasoning tasks; no explanation required, just say what comes to mind
- Warm-up: 2-3 practice problems unrelated to morphisms to establish verbalization habit
- Prompting: use neutral prompts only ("keep talking") when silence exceeds 15 seconds
- Recording: audio + screen capture; video of workspace if physical artifacts used

**Verbal protocol coding scheme (morphism-relevant utterances):**

| Code | Category | Description | Example |
|---|---|---|---|
| VM | Variable mapping | Explicitly maps a variable from one domain to another | "pressure is like voltage here" |
| AA | Analogy assertion | Claims two systems behave similarly | "this circuit acts the same as the fluid system" |
| CE | Confidence expression | States certainty or uncertainty about a mapping | "I'm pretty sure this holds" |
| BR | Boundary recognition | Identifies where an analogy breaks down | "but this doesn't work for nonlinear cases" |
| LA | Layer attention | References a specific morphism layer (structural, behavioral, energy, information, categorical) | "the energy conservation is the same" |
| HE | Heuristic invocation | Uses a rule of thumb for morphism judgment | "if the equations look similar, it's probably fine" |

**Coding reliability standards:**
- Two independent coders minimum
- Target: Cohen's κ ≥ 0.70 (substantial agreement) before proceeding to analysis
- If κ < 0.70: revise codebook, retrain coders, recode 20% sample, reassess
- Report both κ and percent agreement

**Segmentation:** Divide transcripts into utterance-level units (one complete thought). Each unit receives one primary code. Units may receive secondary codes if multiple categories overlap.

### Calibration Study Design (Ideas 20, 21)

**Procedure:**
1. Present engineer with a domain pair from the isomorphism catalog (e.g., "electrical circuit ↔ hydraulic system")
2. Elicit: (a) their assumed variable mapping (which variables correspond?), (b) their assessment of the analogy's correctness (0-100 confidence)
3. Score the proposed mapping against ground truth using the morphism quality metric (Idea 6)
4. Repeat for 15-20 domain pairs spanning exact, partial, and non-morphisms

**Calibration computation:**
- Brier score: mean squared error between stated confidence and actual correctness
- Calibration curve: bin responses by confidence decile, plot actual accuracy per bin
- Over/under-confidence: systematic deviation from the diagonal on calibration curve
- Murphy decomposition: separate reliability (calibration) from resolution (discrimination)

**Sample size:** Target n ≥ 30 per expertise level for adequate calibration estimation (total N ≥ 90 for 3 levels). Power analysis: to detect medium effect (d = 0.5) on calibration score between expert and novice, n = 64 per group at α = 0.05, power = 0.80.

**Design controls:**
- Counterbalance domain pair presentation order
- Include known exact morphisms, known partial morphisms, and known non-morphisms
- Include domain pairs from participant's own expertise area and from unfamiliar areas

### Expert-Novice Comparison Design (Ideas 22, 24)

**Stratification criteria:**
- Years of cross-domain engineering practice (primary)
- Domain breadth: number of distinct engineering domains worked in
- Formal training: whether participant has studied morphisms, analogical reasoning, or systems engineering formally
- Minimum 3 levels: novice (<2 yr), intermediate (2-10 yr), expert (>10 yr)

**Minimum sample per level:** n = 15 for qualitative depth (protocol analysis), n = 30 for quantitative between-group comparison

**Analysis plan:**
- Between-group comparison on key measures using one-way ANOVA (3 levels) or Kruskal-Wallis (if assumptions violated)
- Pairwise comparisons: Tukey HSD (parametric) or Dunn's test (nonparametric)
- Effect size reporting: Cohen's d for each pairwise comparison, η² for overall group effect
- Report both statistical significance and practical significance (effect size interpretation)

**Specific to Idea 22 (Layer-Selective Attention):**
- Code think-aloud protocols for layer attention (LA code from coding scheme)
- Compare distribution of attention across 5 layers by expertise level
- Hypothesis: experts attend to energy and information layers more than novices

**Specific to Idea 24 (Tacit Knowledge):**
- Present catalog entries to experts; ask "what else do you know about this relationship?"
- Code new information not in the catalog as tacit knowledge candidates
- Compare volume and specificity of tacit knowledge by expertise level

### Mental Model Fidelity Measurement (Idea 23)

**Conceptual move:** Apply VMMC morphism analysis reflexively — the engineer's mental model is the "verification model," and the formal system model is the "truth."

**Elicitation procedure:**
1. Present a system description (e.g., thermal-electrical analog)
2. Ask engineer to predict system behavior for a set of test inputs
3. Map their reasoning to morphism components: which variables did they map? which relationships did they preserve? which did they distort or omit?
4. Score the mental-model-to-formal-model morphism quality using Idea 6 metric

**Cognitive load manipulation (within-subjects):**
- Normal condition: unlimited time, no concurrent task
- Degraded condition 1: time pressure (60% of normal completion time)
- Degraded condition 2: concurrent task (verbal shadowing or digit span)
- Within-subjects design: same participants under normal and degraded conditions (counterbalanced order)

**Analysis:**
- Paired t-test or repeated-measures ANOVA on fidelity scores across conditions
- Effect size: Cohen's d for normal vs. degraded; η² for overall condition effect
- Correlation: fidelity score vs. design decision quality (if downstream decisions measured)

### Design Decision Tracing (Idea 25)

**Retrospective protocol:**
1. Start from a known verification failure (from published case studies or industry partners)
2. Present failure description and system documentation to participant
3. Ask participant to trace backward: "What assumptions led to this failure?"
4. Code each identified assumption against morphism layers (structural, behavioral, energy, information, categorical)

**Coding scheme for morphism layer violations:**

| Layer | Example Violated Assumption |
|---|---|
| Structural | "Assumed 1:1 variable mapping but system had unmapped state" |
| Behavioral | "Assumed linear behavior but system was nonlinear in operating range" |
| Energy | "Assumed energy conservation held across the analogy" |
| Information | "Assumed sensor model captured all relevant observables" |
| Categorical | "Assumed functorial composition but morphisms didn't compose" |

**Study design:** Case study approach; 5-10 failure cases with detailed trace-back per participant. Target 10-15 participants (engineers with verification/validation experience).

**Analysis:** Frequency of violations per layer, inter-rater reliability on layer coding, qualitative analysis of trace-back narratives.

### IRB Protocol Framework

**Study category:** Minimal risk — no deception, no intervention beyond cognitive tasks, no vulnerable populations

**Informed consent elements:**
- Purpose: studying how engineers reason about cross-domain relationships
- Procedures: think-aloud tasks, interviews, questionnaires (specify duration: typically 60-90 minutes)
- Risks: minor fatigue from cognitive tasks; no physical, psychological, or social risks beyond those of everyday life
- Benefits: no direct benefit to participants; contributes to engineering education research
- Confidentiality: de-identified transcripts stored on UA-managed encrypted storage; no identifying information in publications
- Right to withdraw: may stop at any time without penalty; partial data may be retained if consent given
- Compensation: standard UA rate for study participation (currently ~$15-20/hour)

**Data handling:**
- Audio recordings transcribed then deleted (retention: within 6 months of study completion)
- Transcripts de-identified using participant codes (P01, P02, ...) before analysis
- Demographic data (expertise level, years of experience, domains) stored separately from transcripts
- Data retention: de-identified transcripts and coded data retained for 5 years per UA policy
- Secure storage: UA Box or equivalent UA-approved encrypted cloud storage

**Vulnerable populations:** None expected. Participants are professional engineers and graduate engineering students (all adults, no power differential with researchers in most cases). If recruiting UA students in courses taught by the PI, use third-party recruitment to avoid coercion.

---

## Study Design Template

Use this template when designing a specific study for any of Ideas 20-25.

```
STUDY DESIGN: Idea [N] — [Title]
Date: [YYYY-MM-DD]
PI: [Name]

RESEARCH QUESTION
  Primary: ___
  Secondary: ___

STUDY TYPE
  [Elicitation / Measurement / Observation / Intervention / Retrospective]

DESIGN
  [Between-subjects / Within-subjects / Mixed]
  Independent variables: ___
  Dependent variables: ___
  Control variables: ___

PARTICIPANTS
  Target N: ___ (per group: ___)
  Expertise levels: [novice / intermediate / expert]
  Inclusion criteria: ___
  Exclusion criteria: ___
  Recruitment: ___

INSTRUMENTS
  Ground truth: [isomorphism catalog / morphism quality metric / both]
  Elicitation: ___
  Rating scales: ___
  Protocol: [think-aloud / structured interview / retrospective / combination]

PROCEDURE
  1. Informed consent and demographics (___ min)
  2. Warm-up / practice (___ min)
  3. Main task (___ min)
  4. [Manipulation if applicable] (___ min)
  5. Debriefing (___ min)
  Total session: ___ min

DATA ANALYSIS
  Quantitative: ___
  Qualitative: ___
  Mixed methods integration: [convergent / explanatory sequential / exploratory sequential]
  Effect sizes to report: ___
  Multiple comparisons correction: ___

SAMPLE SIZE JUSTIFICATION
  Target effect size: ___
  α = 0.05, power = 0.80
  Required N: ___
  Rationale: ___

IRB
  Risk level: Minimal
  Consent: [standard / with recording consent addendum]
  Data handling: [per IRB Protocol Framework above]

TIMELINE
  IRB submission: ___
  Pilot (n = 3-5): ___
  Data collection: ___
  Analysis: ___
  Manuscript target: ___
```

---

## IRB Application Template

Common elements reusable across all six studies. Customize the study-specific sections per the study design template above.

```
IRB APPLICATION — Idea [N]: [Title]

PROTOCOL TITLE
  [Working title from future_research_ideas.md]

PRINCIPAL INVESTIGATOR
  [Name], [Department], University of Arizona

STUDY OBJECTIVES
  [From research question in study design template]

PARTICIPANT POPULATION
  Adults (18+), professional engineers and graduate engineering students
  Estimated enrollment: [N]
  No vulnerable populations

RECRUITMENT
  Methods: [email, professional society listservs, UA engineering departments]
  Inclusion: [engineering background, specific experience criteria]
  Exclusion: [conflicts of interest, prior participation in related study]

PROCEDURES
  [From procedure section of study design template]
  Duration per participant: [60-90] minutes
  Number of sessions: [1 / multiple]
  Location: [UA campus / remote via Zoom]

RISKS AND BENEFITS
  Risks: Minor fatigue from cognitive tasks. No physical, psychological,
         or social risks beyond those of everyday life.
  Benefits: No direct benefit. Contributes to engineering education research.

CONFIDENTIALITY
  De-identified transcripts using participant codes (P01, P02, ...).
  Audio recordings transcribed and deleted within 6 months.
  Data stored on UA-approved encrypted storage.
  No identifying information in publications.

COMPENSATION
  [Standard UA rate, ~$15-20/hour] for [estimated session duration].

INFORMED CONSENT
  Written consent obtained before participation.
  Separate recording consent addendum if audio/video recorded.
  Participants informed of right to withdraw at any time.

DATA MANAGEMENT
  De-identified data retained 5 years per UA policy.
  Raw recordings deleted after transcription.
  Coded data and transcripts on encrypted UA storage.
```

---

## Integration with Claude Flow

### Spawn Commands

```bash
# Full study design for a specific idea
claude-flow hive-mind spawn "Design complete study protocol for Idea [N] ([Title]). Fill in the study design template. Include instrument design, sample size justification, analysis plan, and IRB elements." \
  --queen research-strategic \
  --workers psychometrics-analyst,methodology-advisor,research-architect,peer-review-responder

# Psychometric analysis of pilot data
claude-flow hive-mind spawn "Analyze pilot data for Idea [N] study. Compute inter-rater reliability (κ), calibration scores (Brier), and preliminary effect sizes. Assess whether instruments and procedures need revision." \
  --queen research-strategic \
  --workers psychometrics-analyst,probabilist,methodology-advisor

# Cross-study instrument harmonization
claude-flow hive-mind spawn "Harmonize instruments across Ideas 20-25. Identify shared items, common scales, and consistent coding schemes. Produce unified instrument package for IRB submission." \
  --queen research-strategic \
  --workers psychometrics-analyst,methodology-advisor,research-architect
```

### Memory Storage

```bash
# Store study design
claude-flow memory store \
  --key "cognitive-studies/idea-[N]/design/$(date +%Y-%m-%d)" \
  --value '{"idea": N, "study_type": "...", "n_target": N, "instruments": [...], "status": "designed"}' \
  --namespace research-strategy

# Store pilot results
claude-flow memory store \
  --key "cognitive-studies/idea-[N]/pilot/$(date +%Y-%m-%d)" \
  --value '{"kappa": 0.XX, "brier": 0.XX, "effect_size": 0.XX, "revisions_needed": [...]}' \
  --namespace research-strategy
```

---

## Output Templates

### Study Protocol Report

```
STUDY PROTOCOL REPORT
Idea: [N] — [Title]
Date: [YYYY-MM-DD]
Version: [1.0 / revised]

SUMMARY
  Study type: ___
  Design: ___
  N target: ___
  Key measures: ___

INSTRUMENTS
  [List of instruments with descriptions]

PROCEDURE
  [Step-by-step with timing]

ANALYSIS PLAN
  Primary analysis: ___
  Secondary analyses: ___
  Effect sizes: ___
  Corrections: ___

SAMPLE SIZE JUSTIFICATION
  [Formal power analysis or saturation argument]

IRB STATUS
  Submission date: ___
  Approval: [pending / approved / exempt]

PILOT RESULTS (if available)
  Inter-rater reliability: κ = ___
  Preliminary effect sizes: ___
  Instrument revisions: ___
```

### Psychometric Analysis Report

```
PSYCHOMETRIC ANALYSIS REPORT
Idea: [N] — [Title]
Date: [YYYY-MM-DD]
N analyzed: ___

INTER-RATER RELIABILITY
  Measure: [κ / α / ICC]
  Value: ___
  95% CI: [___, ___]
  Interpretation: ___
  Action: [acceptable / revise codebook / retrain coders]

CALIBRATION (if applicable)
  Brier score: ___ (lower = better)
  ECE: ___
  Over/under-confidence: ___
  Murphy decomposition:
    Reliability: ___
    Resolution: ___
    Uncertainty: ___

EFFECT SIZES
  | Comparison | Measure | Value | 95% CI | Interpretation |
  |---|---|---|---|---|
  | Expert vs. Novice | Cohen's d | ___ | [___, ___] | ___ |
  | Overall group | η² | ___ | [___, ___] | ___ |

RECOMMENDATIONS
  1. ___
  2. ___
```
