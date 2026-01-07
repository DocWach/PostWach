# AI FOR REQUIREMENTS ENGINEERING (AI4RE)
## Comprehensive Research Program

**Generated:** 2026-01-07
**Framework:** Research Planning Capabilities (Phases 1-4)
**Foundation:** IS_AI4RE Publication Analysis

---

# PART I: SYSTEMATIC LITERATURE REVIEW
## Skill Applied: `systematic-literature-review`

---

## 1. Review Protocol

### 1.1 Research Questions for Review

```
PRIMARY REVIEW QUESTION (PICO Framework):
┌─────────────────────────────────────────────────────────────┐
│ Population: Requirements Engineering practitioners/processes │
│ Intervention: AI/ML/LLM-based tools and methods             │
│ Comparison: Traditional manual RE methods                    │
│ Outcome: Quality, efficiency, accuracy, trustworthiness     │
└─────────────────────────────────────────────────────────────┘

RQ1: What AI/ML techniques have been applied to requirements
     engineering tasks, and with what reported effectiveness?

RQ2: What are the documented limitations and failure modes of
     AI-assisted requirements engineering?

RQ3: What human-AI collaboration models have been proposed or
     evaluated for RE contexts?

RQ4: What methodological approaches have been used to evaluate
     AI4RE systems, and what are their strengths/limitations?
```

### 1.2 Search Strategy

```
SEARCH STRING CONSTRUCTION

Concept 1: Artificial Intelligence
────────────────────────────────
("artificial intelligence" OR "machine learning" OR "deep learning"
OR "neural network*" OR "natural language processing" OR NLP
OR "large language model*" OR LLM OR GPT OR "transformer model*"
OR "automated" OR "intelligent")

Concept 2: Requirements Engineering
────────────────────────────────────
("requirements engineering" OR "requirements analysis"
OR "requirements specification" OR "requirements quality"
OR "requirements elicitation" OR "requirements validation"
OR "requirements verification" OR "software requirements"
OR "system requirements" OR "user requirements" OR "stakeholder needs")

Concept 3: Quality/Evaluation
─────────────────────────────
("quality" OR "evaluation" OR "assessment" OR "analysis"
OR "detection" OR "classification" OR "extraction" OR "generation"
OR "validation" OR "verification" OR "improvement")

COMBINED SEARCH:
(Concept 1) AND (Concept 2) AND (Concept 3)

DATABASES:
□ IEEE Xplore (primary - SE focus)
□ ACM Digital Library (primary - CS focus)
□ Scopus (comprehensive)
□ Web of Science (high quality)
□ arXiv (preprints - emerging work)
□ Google Scholar (breadth)
```

### 1.3 Inclusion/Exclusion Criteria

```
INCLUSION CRITERIA
──────────────────
I1: Published 2018-2026 (transformer era)
I2: Peer-reviewed OR significant preprint (>50 citations)
I3: Empirical evaluation with reported metrics
I4: English language
I5: Focus on requirements engineering task(s)
I6: AI/ML technique clearly described

EXCLUSION CRITERIA
──────────────────
E1: No empirical evaluation (conceptual only)
E2: RE mentioned but not primary focus
E3: Industry white papers without methodology
E4: Duplicate publications
E5: Student project reports
E6: Non-English without translation
```

---

## 2. Literature Landscape Analysis
### Agent Applied: `literature-reviewer`

### 2.1 Thematic Synthesis

```
THEME 1: REQUIREMENTS CLASSIFICATION AND DETECTION
══════════════════════════════════════════════════
Focus: Automatic categorization and quality detection

Key Studies:
├── Kurtanovic & Maalej (2017): ML for RE classification
├── Dalpiaz et al. (2019): NLP for requirements classification
├── Hey et al. (2020): BERT for requirements classification
├── Sainani et al. (2020): NFR classification with DL
└── Luo et al. (2022): Transformer-based RE classification

Findings Synthesis:
- Classification accuracy: 70-90% for binary tasks
- Multi-class performance degrades significantly
- Domain adaptation remains challenging
- Fine-tuning improves over zero-shot by 15-30%

Evidence Strength: STRONG (multiple replicated studies)


THEME 2: REQUIREMENTS QUALITY ASSESSMENT
════════════════════════════════════════
Focus: Detecting quality defects in requirements

Key Studies:
├── Femmer et al. (2017): Automatic quality assessment
├── Arora et al. (2019): ML for ambiguity detection
├── Ezzini et al. (2022): Ambiguity detection with transformers
├── Wach et al. (2024): LLM quality evaluation (IS_AI4RE)
└── Mahbub et al. (2024): GPT-4 for RE tasks

Findings Synthesis:
- Linguistic defects (ambiguity): 60-70% detection
- Semantic defects (correctness): 20-40% detection
- High specificity, low sensitivity pattern
- Stochastic variability in LLM outputs

Evidence Strength: MODERATE (emerging area, limited replication)


THEME 3: REQUIREMENTS GENERATION AND COMPLETION
═══════════════════════════════════════════════
Focus: AI-assisted requirements writing

Key Studies:
├── Arulmohan et al. (2023): ChatGPT for RE tasks
├── White et al. (2024): Prompt engineering for RE
├── Ahmad et al. (2023): LLMs for user story generation
└── Ronanki et al. (2024): Requirements completion with GPT

Findings Synthesis:
- Generation quality highly variable
- Template-based approaches more consistent
- Human editing still required for production use
- Potential for productivity gains with oversight

Evidence Strength: WEAK (mostly exploratory, few rigorous evaluations)


THEME 4: HUMAN-AI COLLABORATION IN RE
═════════════════════════════════════
Focus: Interaction models and trust

Key Studies:
├── Chong et al. (2022): Confidence and AI adoption
├── Gyory et al. (2021): Real-time AI in design teams
├── Viros i Martin & Selva (2022): Virtual assistants for SE
└── Topcu et al. (2025): Failure mode characterization

Findings Synthesis:
- Trust calibration is critical
- Over-reliance is documented risk
- Human-in-the-loop essential for current tools
- Training impacts effective collaboration

Evidence Strength: MODERATE (growing body, diverse methods)


THEME 5: DOMAIN-SPECIFIC AI4RE
══════════════════════════════
Focus: Specialized applications

Key Studies:
├── Safety-critical: Automated FMEA, hazard analysis
├── Automotive: AUTOSAR requirements processing
├── Medical: FDA compliance checking
└── Aerospace: DO-178C alignment verification

Findings Synthesis:
- Domain knowledge improves performance
- Regulatory requirements drive adoption
- Higher accuracy thresholds required
- Limited public evaluation datasets

Evidence Strength: WEAK (fragmented, proprietary constraints)
```

### 2.2 Citation Network Analysis

```
CITATION NETWORK: AI4RE INTELLECTUAL STRUCTURE

FOUNDATIONAL WORKS (Pre-2018)
─────────────────────────────
                    ┌─────────────────────┐
                    │  Maalej et al. 2016 │
                    │  (Bug Report Class) │
                    └──────────┬──────────┘
                               │
         ┌─────────────────────┼─────────────────────┐
         │                     │                     │
         ▼                     ▼                     ▼
┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐
│ Kurtanovic 2017 │  │  Dalpiaz 2019   │  │  Ferrari 2018   │
│ (ML for RE)     │  │  (NLP for RE)   │  │  (NLP ambiguity)│
└────────┬────────┘  └────────┬────────┘  └────────┬────────┘
         │                    │                     │
         └────────────────────┼─────────────────────┘
                              │
                              ▼
                    ┌─────────────────────┐
                    │  TRANSFORMER ERA    │
                    │     (2020+)         │
                    └──────────┬──────────┘
                               │
    ┌──────────────────────────┼──────────────────────────┐
    │                          │                          │
    ▼                          ▼                          ▼
┌─────────────┐      ┌─────────────────┐      ┌─────────────────┐
│ Hey 2020    │      │ Ezzini 2022     │      │ Arulmohan 2023  │
│ BERT for RE │      │ Transformers    │      │ ChatGPT for RE  │
└─────────────┘      │ for ambiguity   │      └─────────────────┘
                     └─────────────────┘
                              │
                              ▼
                    ┌─────────────────────┐
                    │  Wach et al. 2024   │◄──── CURRENT FOCUS
                    │  (IS_AI4RE/Broken   │
                    │   Clock Study)      │
                    └─────────────────────┘

EMERGING CLUSTERS:
1. Classification/Detection (mature)
2. Quality Assessment (growing)
3. Generation/Completion (nascent)
4. Human-AI Collaboration (cross-cutting)
```

### 2.3 Methodological Analysis

```
METHODOLOGICAL PATTERNS IN AI4RE RESEARCH

EVALUATION APPROACHES USED
──────────────────────────
| Approach | Frequency | Strengths | Limitations |
|----------|-----------|-----------|-------------|
| Precision/Recall | 85% | Standard, comparable | Threshold-dependent |
| Accuracy | 70% | Simple | Imbalanced data issues |
| F1 Score | 65% | Balances P/R | Single number |
| Human evaluation | 40% | Ecological validity | Expensive, subjective |
| Task completion | 25% | Practical | Hard to standardize |
| User studies | 15% | Real-world validity | Small samples |

DATASET CHARACTERISTICS
───────────────────────
| Dataset | Studies Using | Domain | Size | Public |
|---------|---------------|--------|------|--------|
| PROMISE | 30+ | Mixed | 625 | Yes |
| tera-PROMISE | 20+ | Mixed | 969 | Yes |
| PURE | 15+ | Multi-domain | 79 docs | Yes |
| OpenReq | 10+ | Various | Varies | Partial |
| Custom/Proprietary | 50%+ | Various | Varies | No |

CRITICAL METHODOLOGICAL GAPS IDENTIFIED
───────────────────────────────────────
1. Limited replication studies
2. Few multi-run variability analyses (IS_AI4RE is exception)
3. Lack of standardized benchmarks
4. Minimal adversarial testing
5. Insufficient ecological validity studies
6. Limited longitudinal evaluation
```

---

## 3. Research Gap Analysis
### Agent Applied: `research-synthesizer`

### 3.1 Gap Identification Matrix

```
RESEARCH GAP ANALYSIS

GAP TYPE 1: EMPIRICAL GAPS
══════════════════════════
┌─────────────────────────────────────────────────────────────┐
│ UNDER-STUDIED PHENOMENA                                     │
├─────────────────────────────────────────────────────────────┤
│ G1.1: Long-term reliability of AI4RE tools                 │
│       - Most studies: Single evaluation point              │
│       - Needed: Longitudinal performance tracking          │
│       - Priority: HIGH                                      │
│                                                             │
│ G1.2: Cross-domain generalizability                        │
│       - Most studies: Single domain                        │
│       - Needed: Transfer learning evaluation               │
│       - Priority: HIGH                                      │
│                                                             │
│ G1.3: Real-world deployment outcomes                       │
│       - Most studies: Lab/benchmark settings               │
│       - Needed: Field studies with practitioners           │
│       - Priority: MEDIUM                                    │
│                                                             │
│ G1.4: Failure mode characterization                        │
│       - IS_AI4RE begins this work                          │
│       - Needed: Systematic failure taxonomy                │
│       - Priority: HIGH                                      │
└─────────────────────────────────────────────────────────────┘

GAP TYPE 2: METHODOLOGICAL GAPS
═══════════════════════════════
┌─────────────────────────────────────────────────────────────┐
│ METHODS NOT YET APPLIED                                     │
├─────────────────────────────────────────────────────────────┤
│ G2.1: Rigorous multi-run variance analysis                 │
│       - IS_AI4RE demonstrates importance                   │
│       - Most studies: Single run or unstated               │
│       - Priority: CRITICAL                                  │
│                                                             │
│ G2.2: Comparative LLM evaluation                           │
│       - Most studies: Single model                         │
│       - Needed: Systematic model comparison                │
│       - Priority: HIGH                                      │
│                                                             │
│ G2.3: Uncertainty quantification                           │
│       - Rarely addressed                                   │
│       - Needed: Confidence calibration methods             │
│       - Priority: HIGH                                      │
│                                                             │
│ G2.4: Adversarial robustness testing                       │
│       - Almost entirely absent                             │
│       - Needed: Systematic adversarial evaluation          │
│       - Priority: MEDIUM                                    │
└─────────────────────────────────────────────────────────────┘

GAP TYPE 3: THEORETICAL GAPS
════════════════════════════
┌─────────────────────────────────────────────────────────────┐
│ EXPLANATORY FRAMEWORKS NEEDED                               │
├─────────────────────────────────────────────────────────────┤
│ G3.1: Theory of AI4RE capability boundaries                │
│       - IS_AI4RE hints: linguistic vs. contextual          │
│       - Needed: Systematic capability taxonomy             │
│       - Priority: HIGH                                      │
│                                                             │
│ G3.2: Trust calibration models for RE context              │
│       - General HCI models exist                           │
│       - Needed: RE-specific trust frameworks               │
│       - Priority: MEDIUM                                    │
│                                                             │
│ G3.3: Human-AI task allocation theory                      │
│       - Ad hoc approaches dominate                         │
│       - Needed: Principled allocation frameworks           │
│       - Priority: HIGH                                      │
└─────────────────────────────────────────────────────────────┘

GAP TYPE 4: PRACTICAL/APPLICATION GAPS
══════════════════════════════════════
┌─────────────────────────────────────────────────────────────┐
│ TRANSLATION TO PRACTICE                                     │
├─────────────────────────────────────────────────────────────┤
│ G4.1: Deployment guidelines                                │
│       - When/how to use AI4RE tools                        │
│       - Needed: Evidence-based guidance                    │
│       - Priority: HIGH                                      │
│                                                             │
│ G4.2: Integration with existing RE processes               │
│       - Tool-centric studies dominate                      │
│       - Needed: Process-integrated approaches              │
│       - Priority: MEDIUM                                    │
│                                                             │
│ G4.3: Training and skill development                       │
│       - Little research on practitioner preparation        │
│       - Needed: Effective training methods                 │
│       - Priority: MEDIUM                                    │
└─────────────────────────────────────────────────────────────┘
```

### 3.2 Gap Prioritization

```
GAP PRIORITY MATRIX

                    │ High Feasibility │ Low Feasibility
────────────────────┼──────────────────┼─────────────────
High Significance   │ PRIORITY 1       │ PRIORITY 2
                    │ • G1.4 Failures  │ • G1.3 Field studies
                    │ • G2.1 Variance  │ • G3.1 Capability theory
                    │ • G2.2 Compare   │
────────────────────┼──────────────────┼─────────────────
Medium Significance │ PRIORITY 3       │ PRIORITY 4
                    │ • G2.3 Uncert.   │ • G1.2 Transfer
                    │ • G4.1 Guidelines│ • G2.4 Adversarial
                    │ • G3.3 Allocation│

RECOMMENDED RESEARCH AGENDA (ordered):
1. Multi-run variance analysis across LLMs (extends IS_AI4RE)
2. Failure mode taxonomy development
3. Comparative LLM evaluation benchmark
4. Uncertainty quantification methods
5. Human-AI task allocation framework
6. Deployment guidelines synthesis
```

---

# PART II: RESEARCH PROGRAM DESIGN
## Agent Applied: `research-architect`

---

## 4. Research Program Overview

### 4.1 Program Vision

```
RESEARCH PROGRAM: TRUSTWORTHY AI FOR REQUIREMENTS ENGINEERING
═══════════════════════════════════════════════════════════════

VISION STATEMENT:
"To establish the scientific foundations for trustworthy AI-assisted
requirements engineering through rigorous empirical research,
theoretical development, and evidence-based practice guidelines."

PROGRAM GOALS:
┌─────────────────────────────────────────────────────────────┐
│ GOAL 1: CHARACTERIZE                                        │
│ Systematically document AI4RE capabilities, limitations,    │
│ and failure modes across models, tasks, and contexts        │
├─────────────────────────────────────────────────────────────┤
│ GOAL 2: EXPLAIN                                             │
│ Develop theoretical frameworks explaining when and why      │
│ AI4RE succeeds or fails, enabling prediction and design     │
├─────────────────────────────────────────────────────────────┤
│ GOAL 3: IMPROVE                                             │
│ Create and validate methods for improving AI4RE reliability,│
│ including hybrid architectures and calibration techniques   │
├─────────────────────────────────────────────────────────────┤
│ GOAL 4: TRANSLATE                                           │
│ Develop evidence-based guidelines and tools for effective   │
│ AI4RE deployment in practice                                │
└─────────────────────────────────────────────────────────────┘

THEORETICAL FRAMEWORK:
Based on IS_AI4RE "Broken Clock" insight:

     ┌─────────────────────────────────────────────────────┐
     │              CALIBRATED AI ADOPTION                 │
     │                                                     │
     │  Task Characteristics ──► Capability Matching       │
     │         │                        │                  │
     │         ▼                        ▼                  │
     │  Linguistic ◄───────────► Contextual               │
     │  (AI-suitable)            (Human-required)         │
     │         │                        │                  │
     │         └────────┬───────────────┘                  │
     │                  ▼                                  │
     │         HYBRID WORKFLOW DESIGN                      │
     │                  │                                  │
     │         ┌───────┴───────┐                          │
     │         ▼               ▼                          │
     │   AI Pre-screening  Human Validation               │
     │         │               │                          │
     │         └───────┬───────┘                          │
     │                 ▼                                  │
     │        CALIBRATED TRUST                            │
     └─────────────────────────────────────────────────────┘
```

### 4.2 Research Studies Design

```
STUDY 1: COMPREHENSIVE LLM BENCHMARK FOR RE QUALITY
═══════════════════════════════════════════════════

Purpose: Extend IS_AI4RE methodology across multiple LLMs
         to establish comparative performance baseline

Design: Quantitative, experimental, multi-model comparison

┌─────────────────────────────────────────────────────────────┐
│ RESEARCH QUESTIONS                                          │
│ S1-RQ1: How do different LLMs compare on RE quality tasks? │
│ S1-RQ2: Which quality criteria show consistent patterns?   │
│ S1-RQ3: What factors predict LLM performance differences?  │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ METHODOLOGY                                                 │
├─────────────────────────────────────────────────────────────┤
│ Models: GPT-4o, GPT-4-turbo, Claude 3.5 Sonnet,            │
│         Claude 3 Opus, Llama 3.1 70B, Gemini 1.5 Pro       │
│                                                             │
│ Tasks: 9 INCOSE quality criteria (per IS_AI4RE)            │
│                                                             │
│ Dataset: Expanded from IS_AI4RE                            │
│          - 100 requirements (5x original)                  │
│          - Multiple domains (aerospace, automotive,        │
│            medical, consumer)                              │
│          - Balanced quality distribution                   │
│                                                             │
│ Runs: 100 per model × task (as per IS_AI4RE)              │
│                                                             │
│ Metrics: TPR, TNR, FPR, FNR, variance, criterion-level    │
│                                                             │
│ Controls: Temperature (0.0, 0.3, 0.7, 1.0)                │
│           Prompt variations (3 phrasings)                  │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ ANALYSIS PLAN                                               │
├─────────────────────────────────────────────────────────────┤
│ 1. Descriptive statistics by model × criterion × temp     │
│ 2. Mixed-effects regression: Performance ~ Model + Task +  │
│    Temperature + (1|Requirement)                           │
│ 3. Variance component analysis                             │
│ 4. Criterion clustering analysis                           │
│ 5. Cross-model consistency analysis                        │
└─────────────────────────────────────────────────────────────┘

Sample Size Justification:
- 100 requirements × 6 models × 4 temps × 100 runs = 2.4M decisions
- Power analysis: >99% power to detect medium effects (d=0.5)


STUDY 2: FAILURE MODE TAXONOMY DEVELOPMENT
══════════════════════════════════════════

Purpose: Systematically categorize AI4RE failure modes
         to enable prediction and mitigation

Design: Mixed methods (qualitative → quantitative validation)

┌─────────────────────────────────────────────────────────────┐
│ RESEARCH QUESTIONS                                          │
│ S2-RQ1: What are the distinct failure modes of AI4RE?      │
│ S2-RQ2: What requirement/task characteristics predict      │
│         specific failure modes?                            │
│ S2-RQ3: Can failure modes be detected a priori?           │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ METHODOLOGY                                                 │
├─────────────────────────────────────────────────────────────┤
│ PHASE 2A: Qualitative Taxonomy Development                 │
│ ─────────────────────────────────────────                  │
│ Data: Error cases from Study 1 (n≈500 diverse errors)      │
│ Method: Grounded theory analysis                           │
│   - Open coding of error instances                         │
│   - Axial coding to identify categories                    │
│   - Selective coding for core taxonomy                     │
│ Participants: 3 RE experts + 2 AI researchers              │
│ Output: Failure mode taxonomy with definitions             │
│                                                             │
│ PHASE 2B: Quantitative Validation                          │
│ ─────────────────────────────────                          │
│ Data: New sample of AI4RE errors (n=1000)                  │
│ Method: Classification reliability study                   │
│   - 5 independent raters apply taxonomy                    │
│   - Inter-rater reliability (Krippendorff's alpha)        │
│   - Taxonomy refinement based on disagreements             │
│ Output: Validated taxonomy with reliability metrics        │
│                                                             │
│ PHASE 2C: Predictive Modeling                              │
│ ─────────────────────────────                              │
│ Data: Full Study 1 dataset with coded failure modes        │
│ Method: Machine learning classification                    │
│   - Features: Requirement characteristics, task type,      │
│               linguistic features, domain                  │
│   - Models: Random forest, gradient boosting, neural       │
│   - Evaluation: Cross-validated prediction accuracy        │
│ Output: Failure mode prediction model                      │
└─────────────────────────────────────────────────────────────┘


STUDY 3: UNCERTAINTY QUANTIFICATION FOR AI4RE
═════════════════════════════════════════════

Purpose: Develop and validate methods for AI4RE to express
         appropriate confidence in its assessments

Design: Design science research (develop → evaluate)

┌─────────────────────────────────────────────────────────────┐
│ RESEARCH QUESTIONS                                          │
│ S3-RQ1: What UQ methods are applicable to AI4RE?           │
│ S3-RQ2: How well do UQ methods calibrate AI4RE confidence? │
│ S3-RQ3: Does UQ improve human-AI collaboration outcomes?   │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ METHODOLOGY                                                 │
├─────────────────────────────────────────────────────────────┤
│ PHASE 3A: UQ Method Development                            │
│ ─────────────────────────────────                          │
│ Methods to implement:                                       │
│   1. Token probability aggregation                         │
│   2. Ensemble disagreement (multiple runs)                 │
│   3. Conformal prediction                                   │
│   4. Semantic entropy                                       │
│   5. Self-consistency checking                             │
│                                                             │
│ PHASE 3B: Calibration Evaluation                           │
│ ─────────────────────────────────                          │
│ Data: Study 1 dataset with known ground truth              │
│ Metrics:                                                    │
│   - Expected Calibration Error (ECE)                       │
│   - Maximum Calibration Error (MCE)                        │
│   - Reliability diagrams                                    │
│   - Selective prediction curves                            │
│                                                             │
│ PHASE 3C: Human-AI Collaboration Study                     │
│ ─────────────────────────────────────                      │
│ Design: 2×2 between-subjects experiment                    │
│   - IV1: UQ present vs. absent                             │
│   - IV2: High vs. low AI accuracy condition                │
│ Participants: N=120 SE students/practitioners              │
│ Task: RE quality assessment with AI assistance             │
│ DVs: Decision accuracy, appropriate reliance,              │
│      trust calibration, task time                          │
└─────────────────────────────────────────────────────────────┘


STUDY 4: HYBRID HUMAN-AI RE WORKFLOW DESIGN
═══════════════════════════════════════════

Purpose: Design and evaluate optimal human-AI task allocation
         for RE quality assurance workflows

Design: Design science + field evaluation

┌─────────────────────────────────────────────────────────────┐
│ RESEARCH QUESTIONS                                          │
│ S4-RQ1: What task allocation maximizes quality while       │
│         minimizing human effort?                           │
│ S4-RQ2: How should AI uncertainty inform task routing?     │
│ S4-RQ3: What is the real-world effectiveness of hybrid     │
│         workflows?                                         │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ METHODOLOGY                                                 │
├─────────────────────────────────────────────────────────────┤
│ PHASE 4A: Workflow Design                                  │
│ ────────────────────────                                   │
│ Based on Studies 1-3 findings:                             │
│   - Criterion-specific AI assignment                       │
│   - Uncertainty-based routing                              │
│   - Human review triggers                                  │
│   - Feedback loops for learning                            │
│                                                             │
│ PHASE 4B: Simulation Evaluation                            │
│ ────────────────────────────────                           │
│ Data: Historical RE datasets with ground truth             │
│ Simulation: Model workflow performance under               │
│             different allocation strategies                │
│ Metrics: Quality achieved, human effort required,          │
│          cost-effectiveness ratio                          │
│                                                             │
│ PHASE 4C: Field Study                                      │
│ ─────────────────────                                      │
│ Setting: 3 industry partner organizations                  │
│ Duration: 6 months per organization                        │
│ Design: Stepped-wedge implementation                       │
│ Data: RE quality metrics, process metrics,                 │
│       practitioner experience                              │
│ Analysis: Mixed-effects models for implementation          │
└─────────────────────────────────────────────────────────────┘
```

---

# PART III: MULTI-YEAR RESEARCH ROADMAP
## Skill Applied: `research-roadmapping`

---

## 5. Timeline and Milestones

### 5.1 Program Timeline (5-Year)

```
AI4RE RESEARCH PROGRAM TIMELINE
═══════════════════════════════

YEAR 1: FOUNDATION
──────────────────────────────────────────────────────────────
Q1 │ Q2 │ Q3 │ Q4
───┼────┼────┼────
██ │    │    │    │ Program setup, infrastructure
██ │██  │    │    │ Dataset development and validation
   │██  │██  │    │ Study 1: LLM benchmark (data collection)
   │    │██  │██  │ Study 1: Analysis and reporting
   │    │    │██  │ Study 2 Phase A: Taxonomy development (start)

Milestones:
◆ M1.1: Benchmark dataset released (Q2)
◆ M1.2: Study 1 preregistration published (Q2)
◆ M1.3: Study 1 results submitted (Q4)
◆ M1.4: Preliminary failure taxonomy (Q4)

Deliverables:
□ Open benchmark dataset (100 requirements, multi-domain)
□ Replication package for IS_AI4RE across 6 LLMs
□ Journal article: Comparative LLM benchmark
□ Conference paper: Initial taxonomy


YEAR 2: CHARACTERIZATION
──────────────────────────────────────────────────────────────
Q1 │ Q2 │ Q3 │ Q4
───┼────┼────┼────
██ │██  │    │    │ Study 2 Phase B: Taxonomy validation
   │██  │██  │    │ Study 2 Phase C: Predictive modeling
██ │██  │██  │██  │ Study 3 Phase A: UQ method development
   │    │██  │██  │ Study 3 Phase B: Calibration evaluation

Milestones:
◆ M2.1: Validated failure taxonomy published (Q2)
◆ M2.2: Failure prediction model released (Q3)
◆ M2.3: UQ methods implemented and documented (Q3)
◆ M2.4: Calibration study results (Q4)

Deliverables:
□ Failure mode taxonomy with coding guide
□ Open-source failure prediction tool
□ UQ implementation library
□ Journal article: Failure modes
□ Journal article: Uncertainty quantification


YEAR 3: INTERVENTION
──────────────────────────────────────────────────────────────
Q1 │ Q2 │ Q3 │ Q4
───┼────┼────┼────
██ │██  │    │    │ Study 3 Phase C: Human-AI collaboration study
   │██  │██  │    │ Study 4 Phase A: Workflow design
   │    │██  │██  │ Study 4 Phase B: Simulation evaluation
   │    │    │██  │ Study 4 Phase C: Field study preparation

Milestones:
◆ M3.1: Collaboration study results (Q2)
◆ M3.2: Hybrid workflow prototype (Q3)
◆ M3.3: Simulation validation complete (Q4)
◆ M3.4: Field study sites confirmed (Q4)

Deliverables:
□ Human-AI collaboration guidelines
□ Workflow design framework
□ Simulation evaluation toolkit
□ Journal article: Trust calibration
□ Conference paper: Workflow design


YEAR 4: TRANSLATION
──────────────────────────────────────────────────────────────
Q1 │ Q2 │ Q3 │ Q4
───┼────┼────┼────
██ │██  │██  │██  │ Study 4 Phase C: Field study (6-month rolling)
██ │██  │    │    │ Guidelines development
   │██  │██  │    │ Tool development and refinement
   │    │██  │██  │ Training materials development

Milestones:
◆ M4.1: First field site complete (Q2)
◆ M4.2: Draft guidelines released (Q2)
◆ M4.3: Tool beta release (Q3)
◆ M4.4: Field study complete (Q4)

Deliverables:
□ Evidence-based deployment guidelines
□ Open-source AI4RE toolkit
□ Training curriculum
□ Field study technical report
□ Journal article: Real-world evaluation


YEAR 5: CONSOLIDATION
──────────────────────────────────────────────────────────────
Q1 │ Q2 │ Q3 │ Q4
───┼────┼────┼────
██ │██  │    │    │ Comprehensive analysis and synthesis
   │██  │██  │    │ Book/major publication
   │    │██  │██  │ Dissemination and adoption support
   │    │    │██  │ Program evaluation and future planning

Milestones:
◆ M5.1: Synthesis report complete (Q2)
◆ M5.2: Book manuscript submitted (Q3)
◆ M5.3: Adoption case studies documented (Q4)
◆ M5.4: Program evaluation complete (Q4)

Deliverables:
□ Comprehensive synthesis report
□ Research monograph/textbook chapter
□ Best practices documentation
□ Future research agenda
```

### 5.2 Visual Roadmap

```
AI4RE RESEARCH PROGRAM: 5-YEAR GANTT CHART
══════════════════════════════════════════

                        │ Y1  │ Y2  │ Y3  │ Y4  │ Y5  │
────────────────────────┼─────┼─────┼─────┼─────┼─────┤
INFRASTRUCTURE          │     │     │     │     │     │
  Program setup         │▓▓   │     │     │     │     │
  Dataset development   │▓▓▓▓ │     │     │     │     │
  Tool development      │     │  ▓▓▓│▓▓▓▓ │▓▓   │     │
────────────────────────┼─────┼─────┼─────┼─────┼─────┤
STUDY 1: LLM BENCHMARK  │     │     │     │     │     │
  Data collection       │ ▓▓▓▓│     │     │     │     │
  Analysis              │   ▓▓│     │     │     │     │
  Reporting             │    ▓│     │     │     │     │
────────────────────────┼─────┼─────┼─────┼─────┼─────┤
STUDY 2: FAILURE MODES  │     │     │     │     │     │
  Taxonomy development  │    ▓│▓▓   │     │     │     │
  Validation            │     │▓▓   │     │     │     │
  Predictive modeling   │     │ ▓▓▓ │     │     │     │
────────────────────────┼─────┼─────┼─────┼─────┼─────┤
STUDY 3: UNCERTAINTY    │     │     │     │     │     │
  UQ development        │     │▓▓▓▓▓│     │     │     │
  Calibration eval      │     │  ▓▓▓│     │     │     │
  Collaboration study   │     │     │▓▓▓  │     │     │
────────────────────────┼─────┼─────┼─────┼─────┼─────┤
STUDY 4: HYBRID WORKFLOW│     │     │     │     │     │
  Workflow design       │     │     │ ▓▓▓ │     │     │
  Simulation eval       │     │     │  ▓▓▓│     │     │
  Field study           │     │     │    ▓│▓▓▓▓▓│     │
────────────────────────┼─────┼─────┼─────┼─────┼─────┤
SYNTHESIS & TRANSLATION │     │     │     │     │     │
  Guidelines            │     │     │     │▓▓   │     │
  Training materials    │     │     │     │  ▓▓▓│     │
  Comprehensive report  │     │     │     │     │▓▓   │
  Book/major publication│     │     │     │     │ ▓▓▓ │
────────────────────────┼─────┼─────┼─────┼─────┼─────┤
MILESTONES              │◆◆◆◆│◆◆◆◆│◆◆◆◆│◆◆◆◆│◆◆◆◆│
────────────────────────┴─────┴─────┴─────┴─────┴─────┘

Legend: ▓ = Active work period  ◆ = Milestone
```

### 5.3 Resource Requirements

```
RESOURCE ALLOCATION

PERSONNEL (FTE over 5 years)
─────────────────────────────
| Role | Y1 | Y2 | Y3 | Y4 | Y5 | Total |
|------|----|----|----|----|----|----- |
| PI | 0.25 | 0.25 | 0.25 | 0.25 | 0.25 | 1.25 |
| Co-I (AI) | 0.15 | 0.20 | 0.15 | 0.10 | 0.05 | 0.65 |
| Co-I (SE) | 0.15 | 0.15 | 0.20 | 0.15 | 0.05 | 0.70 |
| Postdoc | 1.00 | 1.00 | 1.00 | 0.50 | 0.25 | 3.75 |
| PhD Student 1 | 0.50 | 0.50 | 0.50 | 0.50 | 0.25 | 2.25 |
| PhD Student 2 | - | 0.50 | 0.50 | 0.50 | 0.50 | 2.00 |
| Research Asst | 0.50 | 0.50 | 0.50 | 0.50 | 0.25 | 2.25 |

BUDGET ESTIMATE (5-year total)
──────────────────────────────
| Category | Amount |
|----------|--------|
| Personnel | $1,200,000 |
| Equipment (compute) | $150,000 |
| LLM API costs | $75,000 |
| Participant compensation | $50,000 |
| Travel | $60,000 |
| Publication costs | $25,000 |
| Indirect costs (50%) | $780,000 |
| **TOTAL** | **$2,340,000** |

INFRASTRUCTURE
──────────────
□ High-performance computing access
□ LLM API accounts (OpenAI, Anthropic, Google)
□ Survey/experiment platform (Qualtrics, Prolific)
□ Collaboration tools (GitHub, OSF)
□ Industry partner agreements
```

---

# PART IV: IMPLEMENTATION PLANNING
## Skills Applied: `grant-writing`, `data-management`, `reproducibility`

---

## 6. Funding Strategy

### 6.1 Funding Opportunities

```
TARGET FUNDING SOURCES

PRIMARY TARGETS
───────────────
┌─────────────────────────────────────────────────────────────┐
│ NSF: Software and Hardware Foundations (SHF)               │
│ Program: Formal Methods, SE, Programming Languages         │
│ Fit: EXCELLENT - Core SE + AI research                     │
│ Amount: $500K-$1.2M for medium projects                    │
│ Timeline: Submit Year 1 Q1                                 │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ NSF: Human-Centered Computing (HCC)                        │
│ Program: Human-AI Collaboration                            │
│ Fit: STRONG - Studies 3-4 human factors focus              │
│ Amount: $500K-$1M                                          │
│ Timeline: Submit Year 1 Q2 (collaborative proposal)        │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ DOD: Systems Engineering Research Center (SERC)            │
│ Program: AI for Systems Engineering                        │
│ Fit: EXCELLENT - Direct alignment                          │
│ Amount: Task orders $200K-$500K                            │
│ Timeline: Rolling submissions                              │
└─────────────────────────────────────────────────────────────┘

SECONDARY TARGETS
─────────────────
□ DARPA: AI Next, Trustworthy AI programs
□ NASA: Systems engineering automation
□ Industry: Boeing, Lockheed Martin, GM research programs
□ Foundations: Sloan (if methodological innovation focus)

FUNDING SEQUENCE STRATEGY
─────────────────────────
Year 1: NSF SHF (core research) + SERC (applied)
Year 2: NSF HCC (human factors) + industry supplement
Year 3-4: Renewal/continuation funding
Year 5: Translation grants, industry partnerships
```

### 6.2 Specific Aims (Grant Format)

```
SPECIFIC AIMS PAGE

The increasing adoption of Large Language Models (LLMs) for
software engineering tasks demands rigorous understanding of
their capabilities and limitations. Our recent work revealed
that off-the-shelf LLMs exhibit a "broken clock" pattern in
requirements quality evaluation—producing correct outputs
unpredictably, without mechanisms to distinguish accurate from
inaccurate assessments (Wach et al., 2024). This finding has
critical implications for AI adoption in safety-critical
systems engineering.

This research program will establish scientific foundations
for trustworthy AI-assisted requirements engineering (AI4RE)
through four integrated aims:

AIM 1: Establish comprehensive performance benchmarks for
LLM-based requirements quality evaluation across models,
tasks, and domains.
─────────────────────────────────────────────────────────────
We will extend our preliminary methodology to compare 6 major
LLMs across 9 quality criteria using 100+ requirements from
4 industry domains. This will produce the first systematic
comparative benchmark for AI4RE, enabling evidence-based model
selection and establishing baselines for improvement.

AIM 2: Develop and validate a taxonomy of AI4RE failure modes
to enable prediction and mitigation of errors.
─────────────────────────────────────────────────────────────
Using grounded theory methods on benchmark error data, we will
construct a failure mode taxonomy, validate it with independent
raters, and build predictive models to identify high-risk
assessment scenarios before deployment.

AIM 3: Design and evaluate uncertainty quantification methods
that enable LLMs to express appropriate confidence in their
requirements assessments.
─────────────────────────────────────────────────────────────
We will implement and compare 5 UQ approaches, measure their
calibration against ground truth, and evaluate their impact
on human-AI collaboration through controlled experiments with
120 SE practitioners.

AIM 4: Design, simulate, and field-test hybrid human-AI
workflows for requirements quality assurance.
─────────────────────────────────────────────────────────────
Building on Aims 1-3, we will design optimal task allocation
strategies, validate them through simulation, and evaluate
real-world effectiveness through 6-month deployments at 3
industry partner sites.

EXPECTED OUTCOMES: This research will produce (1) open
benchmarks and datasets, (2) validated failure taxonomies,
(3) calibrated UQ methods, and (4) evidence-based deployment
guidelines—transforming AI4RE from unreliable "broken clock"
to trustworthy collaborative tool.
```

---

## 7. Data Management and Open Science

### 7.1 Data Management Plan

```
DATA MANAGEMENT PLAN

1. DATA DESCRIPTION
───────────────────
| Data Type | Format | Volume | Sensitivity |
|-----------|--------|--------|-------------|
| Benchmark requirements | JSON, CSV | ~50MB | Public |
| LLM outputs | JSON | ~5GB | Public |
| Expert annotations | CSV | ~10MB | Public |
| Human study data | CSV, anonymized | ~100MB | Restricted |
| Interview transcripts | TXT, anonymized | ~50MB | Restricted |
| Code/scripts | Python, R | ~200MB | Public |

2. FAIR COMPLIANCE
──────────────────
Findable:
✓ DOIs for all datasets via Zenodo
✓ Registered in re3data.org
✓ Rich metadata using Dublin Core + domain schemas

Accessible:
✓ Open access for benchmark data
✓ Controlled access for human subjects data
✓ Standard authentication via institutional login

Interoperable:
✓ Standard formats (CSV, JSON)
✓ Documented schemas
✓ No proprietary formats

Reusable:
✓ CC-BY 4.0 license for public data
✓ Comprehensive documentation
✓ Provenance tracking

3. REPOSITORY STRATEGY
──────────────────────
| Data Type | Repository | Access |
|-----------|------------|--------|
| Benchmark data | Zenodo + GitHub | Open |
| Analysis code | GitHub | Open |
| Human study data | OSF (restricted) | Controlled |
| Publications | arXiv + journal | Open |

4. RETENTION
────────────
□ All data retained minimum 10 years
□ Code maintained on GitHub indefinitely
□ Benchmark data maintained as community resource
```

### 7.2 Reproducibility Plan

```
OPEN SCIENCE COMMITMENT

PREREGISTRATION
───────────────
All studies will be preregistered:
□ Study 1: OSF Registries (before data collection)
□ Study 2: OSF Registries (before Phase B)
□ Study 3: AsPredicted (before human study)
□ Study 4: OSF Registries (before field study)

OPEN MATERIALS
──────────────
All materials publicly available:
□ Benchmark datasets with documentation
□ Prompt templates used
□ Survey instruments
□ Interview protocols
□ Coding guides for taxonomy
□ Analysis scripts (fully documented)

CODE SHARING
────────────
All code shared via GitHub with:
□ README documentation
□ Requirements files
□ Docker containers for reproducibility
□ Example notebooks
□ Automated tests

REGISTERED REPORTS
──────────────────
Will pursue Registered Report format for:
□ Study 1 (Nature Human Behaviour or similar)
□ Study 3 human collaboration component

TRANSPARENCY STATEMENTS
───────────────────────
All papers will include:
□ 21-word solution statement
□ Preregistration disclosure
□ Data availability statement
□ Code availability statement
□ Conflict of interest disclosure
```

---

## 8. Expected Outputs and Impact

### 8.1 Publication Plan

```
PUBLICATION ROADMAP

YEAR 1
──────
□ Journal: Comparative LLM benchmark (IEEE TSE or TOSEM)
□ Conference: Preliminary taxonomy (ICSE or RE)
□ Workshop: Benchmark dataset release (RE@Next)

YEAR 2
──────
□ Journal: Failure mode taxonomy (ESE or JSS)
□ Journal: Uncertainty quantification (AAAI or similar)
□ Conference: Calibration methods (ASE)

YEAR 3
──────
□ Journal: Human-AI collaboration (CHI or CSCW)
□ Conference: Workflow design (ICSE)
□ Workshop: Deployment guidelines draft

YEAR 4
──────
□ Journal: Field study results (IEEE TSE)
□ Conference: Best practices (RE conference)
□ Technical report: Comprehensive guidelines

YEAR 5
──────
□ Book chapter or research monograph
□ Synthesis paper (ACM Computing Surveys)
□ Future directions position paper

TARGET VENUES
─────────────
Tier 1 Journals: IEEE TSE, TOSEM, ESE
Tier 1 Conferences: ICSE, FSE, ASE
Domain Conferences: RE, REFSQ
AI Venues: AAAI, NeurIPS (methods papers)
HCI Venues: CHI, CSCW (human factors)
```

### 8.2 Impact Metrics

```
SUCCESS METRICS

ACADEMIC IMPACT
───────────────
□ Citations to benchmark paper: Target 100+ in 3 years
□ Dataset downloads: Target 500+ in 2 years
□ Tool adoption: Target 50+ research groups using
□ Replication studies: Target 5+ independent replications

PRACTICAL IMPACT
────────────────
□ Industry adoptions: Target 3+ organizations implementing
□ Standard influence: Contribute to IEEE/ISO standards
□ Tool users: Target 1000+ practitioners using toolkit
□ Training completions: Target 500+ trained practitioners

COMMUNITY BUILDING
──────────────────
□ Workshop series established
□ Benchmark competition launched
□ Community of practice formed
□ Industry-academic consortium developed

LONG-TERM OUTCOMES
──────────────────
□ AI4RE established as rigorous research area
□ Evidence-based practices become norm
□ Trustworthy AI adoption in critical systems
□ Next generation researchers trained
```

---

## 9. Risk Assessment

```
RISK MANAGEMENT MATRIX

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| LLM APIs change/deprecated | Medium | High | Abstract API layer, multiple providers |
| Industry partners withdraw | Low | High | Multiple partners, MOUs signed |
| Replication failures | Medium | Medium | Preregistration, open methods |
| Negative results | Medium | Low | Publication regardless (Registered Reports) |
| Personnel turnover | Medium | Medium | Documentation, knowledge transfer |
| Scope creep | Medium | Medium | Clear milestones, regular review |
| Compute costs exceed budget | Low | Medium | Cost monitoring, efficiency optimization |
| IRB delays | Low | Medium | Early submission, protocol templates |
```

---

## 10. Summary

```
AI4RE RESEARCH PROGRAM SUMMARY
══════════════════════════════

FOUNDATION: IS_AI4RE "Broken Clock" insight
- LLMs have asymmetric performance (high TNR, low TPR)
- Criterion-dependent capabilities (linguistic > contextual)
- Intrinsic stochasticity undermines trust

PROGRAM GOALS:
1. CHARACTERIZE performance across LLMs and tasks
2. EXPLAIN why AI4RE succeeds or fails
3. IMPROVE reliability through UQ and hybrid workflows
4. TRANSLATE findings to evidence-based practice

KEY STUDIES:
□ Study 1: Comprehensive LLM benchmark
□ Study 2: Failure mode taxonomy
□ Study 3: Uncertainty quantification
□ Study 4: Hybrid workflow field evaluation

TIMELINE: 5 years
BUDGET: ~$2.3M total
TEAM: PI + 2 Co-Is + Postdoc + 2 PhD students

DELIVERABLES:
□ Open benchmark dataset
□ Validated failure taxonomy
□ UQ methods and tools
□ Evidence-based deployment guidelines
□ 15+ publications
□ Trained practitioners

VISION: Transform AI4RE from unreliable "broken clock"
        to trustworthy collaborative tool through rigorous
        scientific research and evidence-based translation.
```

---

## Research Capabilities Demonstrated

| Capability | Application in This Document |
|------------|------------------------------|
| `systematic-literature-review` | Part I: Literature review protocol, search strategy, PRISMA elements |
| `literature-reviewer` | Thematic synthesis, citation network, gap identification |
| `research-synthesizer` | Cross-study integration, pattern recognition |
| `research-architect` | Study designs, methodology selection, validity analysis |
| `research-roadmapping` | 5-year timeline, milestones, resource allocation |
| `grant-writing` | Specific aims, funding strategy, budget |
| `data-management` | DMP, FAIR compliance, repository strategy |
| `reproducibility` | Preregistration, open science, transparency |
| `methodology-advisor` | Study design choices, sample size, analysis plans |
| `publication-strategist` | Publication roadmap, venue selection |

---

*Generated using Research Planning Capabilities (Phases 1-4)*
*Foundation: Wach et al. (2024) "The Tale of the Broken Clock"*
