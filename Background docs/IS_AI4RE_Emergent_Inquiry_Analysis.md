# EMERGENT INQUIRY ANALYSIS
## Publication: "The Tale of the Broken Clock: How LLMs Evaluate Requirement Quality and Where They Fail"

**Analysis Date:** 2026-01-07
**Framework Applied:** Hybrid Framework ("The Symposium")
**Methodology:** Emergent Inquiry (6-Phase Cycle)

---

## PHASE 1: ORIENTATION (Meta-Observer)

### Phenomenon Identification
**Primary Phenomenon**: The stochastic and asymmetric performance of LLMs in requirements quality evaluation—characterized by the metaphor of a "broken clock" (occasionally correct, but not reliably so).

### Multi-Level Analysis

| Level | Phenomenon | Agents Engaged |
|-------|-----------|----------------|
| **Micro** | Individual LLM inference decisions; token-level stochastic sampling | empiricist-gatherer, skeptical-challenger |
| **Meso** | Performance patterns across quality criteria categories | emergence-observer, connection-mapper |
| **Macro** | Implications for AI4SE trustworthiness and human-AI collaboration paradigms | justice-arbiter, dialectical-synthesizer |
| **Meta** | Epistemological status of AI-generated knowledge claims | network-epistemologist, meta-observer |

### Initial Assumptions to Examine
1. That LLM performance can be meaningfully evaluated against "ground truth"
2. That INCOSE criteria represent valid quality markers
3. That 100 runs capture sufficient variability
4. That "off-the-shelf" represents typical deployment conditions
5. That binary detection is the appropriate evaluation frame

---

## PHASE 2: QUESTIONING (Socratic Examiner + Skeptical Challenger)

### Foundational Questions

**Epistemological Layer** (socratic-examiner):
```
Q1: What constitutes "ground truth" in requirements quality?
    → The paper uses expert consensus, but acknowledges this
       is itself a constructed standard

Q2: Can stochastic tools produce "knowledge" or merely "outputs"?
    → This cuts to the heart of whether LLM evaluations
       constitute justified belief

Q3: What is the relationship between linguistic detection
    and semantic understanding?
    → The paper reveals LLMs succeed at linguistic patterns
       but fail at contextual reasoning
```

**Methodological Layer** (skeptical-challenger):
```
CHALLENGE 1: Sample Size Adequacy
- 20 requirements × 9 criteria × 100 runs = 18,000 decisions
- But only 20 unique requirements limits generalizability
- Purposefully poor-quality requirements may not represent
  typical distributions

CHALLENGE 2: Ground Truth Validity
- Expert consensus ≠ objective truth
- Intercoder reliability not quantified
- INCOSE criteria are themselves normative constructs

CHALLENGE 3: Temperature Setting
- 0.7 temperature is arbitrary baseline
- Lower temperatures might show different patterns
- Production systems may use different configurations

CHALLENGE 4: Model Selection
- ChatGPT 4.o was newest available on n8n platform
- But not newest available overall
- No comparison to other LLMs (Claude, Llama, etc.)
```

### Probing Questions by Quality Criterion

| Criterion | Critical Question |
|-----------|------------------|
| **Correctness** | How can correctness be assessed without full stakeholder context? |
| **Necessity** | Can necessity ever be evaluated without the complete requirement set? |
| **Boundedness** | Are cross-requirement constraints fundamentally relational? |
| **Ambiguity** | Is ambiguity detection truly "understanding" or pattern matching? |
| **Verifiability** | Does linguistic structure suffice for verifiability assessment? |

---

## PHASE 3: MAPPING (Network Epistemologist + Connection Mapper)

### Knowledge Network Analysis

```
CITATION NETWORK STRUCTURE

Core Theoretical Foundations:
├── Requirements Engineering Theory
│   ├── Pohl (1996) - RE fundamentals
│   ├── Nuseibeh & Easterbrook (2000) - RE roadmap
│   └── INCOSE (2023) - Handbook standards
│
├── AI for Systems Engineering (AI4SE)
│   ├── McDermott et al. (2020) - AI4SE roadmap
│   ├── Allison et al. (2022) - AI in design
│   └── Husain, Wach, & Topcu (2024) - LLM for SE artifacts
│
├── NLP/LLM Development
│   ├── Ashish (2017) - Transformer architecture
│   ├── Hochreiter & Schmidhuber (1997) - LSTM
│   └── Elman (1990) - Finding structure in time
│
└── Human-AI Collaboration
    ├── Gyory et al. (2021) - Real-time design teams
    ├── Chong et al. (2022) - Confidence and adoption
    └── Viros i Martin & Selva (2022) - Virtual assistants

KEY OBSERVATION: The paper bridges three distinct
epistemic communities (SE, AI/ML, HCI) with different
evidential standards and theoretical commitments.
```

### Conceptual Dependency Map

```
                    ┌─────────────────────┐
                    │  TRUSTWORTHY AI     │
                    │  (Ultimate Goal)    │
                    └─────────┬───────────┘
                              │
            ┌─────────────────┼─────────────────┐
            │                 │                 │
    ┌───────▼───────┐ ┌───────▼───────┐ ┌───────▼───────┐
    │  Performance  │ │  Reliability  │ │ Transparency  │
    │  (TPR/TNR)    │ │  (Variance)   │ │ (Explaintic.) │
    └───────┬───────┘ └───────┬───────┘ └───────────────┘
            │                 │
    ┌───────▼─────────────────▼───────┐
    │      EMPIRICAL FINDINGS         │
    │  - 35% TPR (issue detection)    │
    │  - 83% TNR (false alarm avoid)  │
    │  - High variability across runs │
    └───────┬─────────────────────────┘
            │
    ┌───────▼───────────────────────────────┐
    │         IMPLICATIONS                  │
    │  - Not ready for autonomous use       │
    │  - Suitable for decision support      │
    │  - Human-in-the-loop essential        │
    └───────────────────────────────────────┘
```

### Testimony Chain Analysis

```
KNOWLEDGE PROVENANCE TRACE

Claim: "LLMs exhibit low TPR and high FNR in RE quality"
       │
       ├─> Direct Evidence: 100 experimental runs
       │   ├─> Ground Truth: Expert consensus (3+ researchers)
       │   │   └─> Standards: INCOSE criteria (community standard)
       │   └─> Test Data: UT Dallas requirement set
       │       └─> Subjects: 1,208 pre-service engineers
       │
       └─> Corroborating Literature:
           ├─> Mahbub et al. (2024): GPT-4 precision 41-61%
           ├─> Doris et al. (2024): Multimodal LLM shortcomings
           └─> Topcu et al. (2025): Failure mode characterization

TESTIMONY STRENGTH: MODERATE-HIGH
- Direct experimental evidence (strong)
- Single system context (limits generalizability)
- Consistent with prior findings (corroborated)
```

---

## PHASE 4: VERIFICATION (Emergence Verifier + Empiricist Gatherer)

### Emergent Pattern Assessment

**Pattern 1: Performance Asymmetry**
```
EMERGENCE VERIFICATION

Observation: TPR (0.35) << TNR (0.83)

Is this emergent or predictable?
├── Training data likely contains more "good" than "bad" examples
├── LLMs optimize for plausibility, not accuracy
├── Conservative flagging minimizes cognitive dissonance
└── VERDICT: SEMI-EMERGENT
    - The asymmetry emerges from training dynamics
    - Not explicitly designed but reproducible
    - Represents a "basin of attraction" in LLM behavior
```

**Pattern 2: Criterion-Dependent Performance**
```
PERFORMANCE HIERARCHY (TPR):
1. Ambiguity     (0.69) ─┐
2. Verifiability (0.64) ─┼─> Linguistic/Syntactic
3. Formatting    (0.30) ─┘
4. Correctness   (0.24) ─┐
5. Boundedness   (0.17) ─┼─> Contextual/Semantic
6. Necessity     (0.00) ─┘
7. Conciseness   (0.00) ─┘

EMERGENCE ANALYSIS:
- Strong correlation with linguistic explicitness
- Context-dependent criteria cluster at bottom
- Pattern suggests fundamental architectural limitation
- VERDICT: ROBUST EMERGENT PATTERN
```

**Pattern 3: Execution Variability**
```
STOCHASTICITY ANALYSIS

Standard Deviations by Metric:
- TPR: 0.05 (moderate variability)
- TNR: 0.02 (low variability)
- FPR: 0.02 (low variability)
- FNR: 0.05 (moderate variability)

Interpretation:
- Variability is asymmetric (detection varies more than avoidance)
- Suggests stochastic effects concentrate in decision boundaries
- "Same input, different outputs" undermines trustworthiness
- VERDICT: INTRINSIC STOCHASTICITY (not experimental error)
```

### Evidence Strength Assessment

| Finding | Evidence Type | Strength | Confidence |
|---------|--------------|----------|------------|
| Low TPR overall | Quantitative/100 runs | Strong | High |
| High TNR overall | Quantitative/100 runs | Strong | High |
| Criterion hierarchy | Comparative analysis | Strong | High |
| Generalizability | Single system | Weak | Low |
| LLM comparison | Single model | Weak | Low |
| Temperature effects | Single setting | Weak | Low |

---

## PHASE 5: SYNTHESIS (Dialectical Synthesizer + Collective Intelligence Curator)

### Dialectical Analysis

**Thesis 1**: LLMs can automate requirements quality evaluation
**Antithesis 1**: LLMs demonstrate unacceptable error rates and variability

```
DIALECTICAL RESOLUTION (Aufhebung):

SYNTHESIS: LLMs can partially automate RE quality evaluation
           in specific, bounded contexts

Preserved from Thesis:
- LLMs do detect some quality issues
- Linguistic/syntactic issues are identifiable
- High TNR prevents excessive false alarms

Preserved from Antithesis:
- Autonomous operation is not trustworthy
- Context-dependent criteria require human judgment
- Stochastic nature demands verification

Transcended Insight:
→ The question shifts from "Can LLMs do this?" to
   "What role should LLMs play in hybrid workflows?"
```

**Thesis 2**: AI assistants should replicate expert behavior
**Antithesis 2**: AI exhibits fundamentally different failure modes than humans

```
DIALECTICAL RESOLUTION:

SYNTHESIS: AI should complement rather than replicate
           human expertise

Evidence from Paper:
- LLMs fail on "SE judgment" criteria (Correctness, Necessity)
- LLMs succeed on "linguistic detection" criteria (Ambiguity)
- Human experts apply contextual reasoning LLMs lack

Transcended Insight:
→ AI4RE value lies in division of cognitive labor:
   - LLMs: Surface-level pattern detection
   - Humans: Contextual judgment and validation
   - Together: Augmented quality assurance
```

**Thesis 3**: More data/fine-tuning will solve performance issues
**Antithesis 3**: Stochasticity is intrinsic to transformer architecture

```
DIALECTICAL RESOLUTION:

SYNTHESIS: Improvement is possible but fundamental
           limits likely exist

Paper's Contribution:
- Documents that even "best-case" execution shows significant errors
- Variability persists across identical conditions
- Some criteria may be architecturally unsuited to LLM evaluation

Transcended Insight:
→ The research agenda should pursue:
   (a) Task decomposition (which sub-tasks are LLM-suitable?)
   (b) Hybrid architectures (how to combine symbolic and neural?)
   (c) Uncertainty quantification (when should LLMs abstain?)
```

### Integrated Framework

```
EMERGENT SYNTHESIS: THE BROKEN CLOCK PARADIGM

Core Insight: Like a broken clock that's right twice a day,
off-the-shelf LLMs provide correct evaluations some of the
time—but without mechanisms to distinguish correct from
incorrect instances.

Implications:

1. EPISTEMOLOGICAL
   - LLM outputs are not "knowledge" in classical sense
   - They are probabilistic assertions requiring verification
   - The "knowing that you know" criterion fails

2. ETHICAL
   - Deployment without human oversight creates moral hazard
   - False confidence in AI recommendations risks harm
   - Responsibility attribution becomes unclear

3. PRACTICAL
   - Task-specific evaluation before deployment is essential
   - Human-in-the-loop is not optional but mandatory
   - Agentic frameworks should use LLMs for specific roles only

4. METHODOLOGICAL
   - Variance characterization is as important as mean performance
   - Criterion-level analysis reveals actionable insights
   - Single-run evaluation is insufficient
```

### Collective Intelligence Curation

**Expert Perspectives Synthesized**:

| Perspective | Key Insight | Source |
|-------------|-------------|--------|
| SE Practice | Requirements errors cause 40-50% of rework costs | Boehm & Papaccio (1988) |
| HCI Research | Trust calibration is critical for AI adoption | Chong et al. (2022) |
| AI Safety | Stochastic systems require uncertainty awareness | Huang et al. (2023) |
| RE Community | NLP for RE is mature but quality assessment is nascent | Zhao et al. (2022) |

**Consensus Position**:
> Off-the-shelf LLMs are insufficient for autonomous RE quality evaluation, but represent a promising component of carefully designed human-AI workflows.

---

## PHASE 6: REFLECTION (Meta-Observer)

### Process Observation

```
INQUIRY PROCESS ANALYSIS

Phases Completed:
✓ Orientation - Multi-level phenomenon identification
✓ Questioning - Foundational and methodological challenges
✓ Mapping - Knowledge network and dependency analysis
✓ Verification - Emergence assessment and evidence evaluation
✓ Synthesis - Dialectical resolutions and integration
✓ Reflection - Meta-observation (current)

Methodological Observations:
1. Paper provides unusually rich empirical data for philosophical analysis
2. The "broken clock" metaphor is epistemologically significant
3. Criterion-level analysis enables precise claims
4. Variability findings challenge deterministic AI assumptions
```

### Bias Detection

```
POTENTIAL BIASES IDENTIFIED

1. SELECTION BIAS
   - Paper uses purposefully poor requirements
   - May not represent realistic requirement distributions
   - Mitigation: Authors acknowledge this limitation

2. CONFIRMATION BIAS (in analysis)
   - Findings align with emerging AI skepticism narrative
   - Counter-evidence (high TNR) also documented
   - Mitigation: Both positive and negative findings reported

3. FRAMING BIAS
   - "Broken clock" metaphor emphasizes unreliability
   - Alternative frame: "Useful but imperfect assistant"
   - Mitigation: Discussion acknowledges potential value

4. METHODOLOGICAL BIAS
   - Binary detection may miss nuanced quality assessment
   - Temperature 0.7 is one of many possible settings
   - Single LLM limits generalization
   - Mitigation: Authors acknowledge as limitations
```

### Validity Assessment

| Validity Type | Assessment | Justification |
|---------------|------------|---------------|
| **Internal** | HIGH | Controlled methodology, 100 runs, clear metrics |
| **External** | MODERATE | Single system, single LLM, specific context |
| **Construct** | HIGH | INCOSE criteria are established standards |
| **Ecological** | MODERATE | Notional system vs. real SE programs |

### Reflexive Monitoring Report

```
INQUIRY QUALITY ASSESSMENT

Strengths of This Analysis:
+ Multi-framework integration (epistemology, ethics, pragmatism)
+ Evidence-grounded claims
+ Dialectical synthesis provides actionable insights
+ Meta-level awareness of limitations

Limitations of This Analysis:
- Cannot verify claims independently
- Relies on paper's reported data
- Single publication (no cross-study synthesis)
- Philosophical interpretation may exceed empirical warrant

Residual Questions:
1. How would findings differ with other LLMs (including me)?
2. What specific agentic architectures would mitigate failures?
3. Can uncertainty quantification be meaningfully implemented?
4. What training interventions would improve criterion-specific performance?

Recommendations for Future Inquiry:
1. Replicate with multiple LLMs
2. Test on real-world requirement sets
3. Develop hybrid human-AI evaluation protocols
4. Create criterion-specific specialized agents
```

---

## PHILOSOPHICAL IMPLICATIONS

### For AI4SE Practice

The study provides empirical grounding for what might be called **"Calibrated AI Adoption"**:

```
CALIBRATED ADOPTION FRAMEWORK

1. TASK ANALYSIS
   → Decompose RE tasks by cognitive requirements
   → Match LLM capabilities to linguistic/syntactic tasks
   → Reserve contextual judgment for human experts

2. UNCERTAINTY ACKNOWLEDGMENT
   → LLMs should express confidence levels
   → Single-run evaluations are insufficient
   → Ensemble methods may improve reliability

3. WORKFLOW DESIGN
   → Human-in-the-loop is mandatory, not optional
   → AI recommendations require validation
   → Division of cognitive labor based on strengths

4. TRUST CALIBRATION
   → Train users on actual AI performance characteristics
   → Prevent over-reliance through transparency
   → Provide mechanisms for feedback and correction
```

### For Trustworthy AI

The paper contributes to emerging discourse on **AI Trustworthiness** by:

1. **Documenting failure modes empirically** - Moving beyond theoretical concerns
2. **Quantifying variability** - Showing reliability challenges concretely
3. **Identifying capability boundaries** - Linguistic vs. contextual reasoning
4. **Recommending governance approaches** - Human-in-the-loop requirements

### Ethical Considerations (Justice Arbiter + Care Ethicist)

```
ETHICAL ANALYSIS

STAKEHOLDER IMPACTS:
├── Systems Engineers
│   + Potential workload reduction
│   - Risk of skill atrophy
│   - Responsibility diffusion
│
├── Project Managers
│   + Faster RE cycle times
│   - False confidence risks
│   - Accountability unclear
│
├── End Users/Society
│   + Better systems if AI assists well
│   - Worse systems if AI fails silently
│   - Safety implications in critical domains
│
└── AI Developers
    + Demonstrates value proposition
    - Reveals current limitations
    - Creates improvement roadmap

JUSTICE CONSIDERATIONS:
- Who bears the burden of AI errors?
- Is automation equitably distributed?
- Are vulnerable stakeholders (novice engineers) protected?

CARE CONSIDERATIONS:
- Does AI assistance preserve meaningful human work?
- Are relationships of trust with stakeholders maintained?
- Is the care for system users adequately prioritized?
```

---

## SYNTHESIS SUMMARY

### Key Findings (Emergent-Epistemic Integration)

1. **LLMs exhibit characteristic asymmetry**: Better at avoiding false alarms (TNR 83%) than detecting real issues (TPR 35%)

2. **Performance is criterion-dependent**: Linguistic/syntactic criteria (Ambiguity, Verifiability) are detectable; contextual criteria (Correctness, Necessity, Boundedness) are not

3. **Stochasticity is intrinsic**: Variability across runs is not experimental error but inherent to LLM architecture

4. **Autonomous operation is premature**: Current off-the-shelf LLMs cannot be trusted for unsupervised RE quality evaluation

5. **Hybrid workflows are viable**: LLMs can serve specialized roles within carefully designed human-AI systems

### Contribution to AI4SE Discourse

This paper advances the field by:
- Providing first quantitative evidence of LLM RE quality performance
- Characterizing error distributions beyond mean performance
- Identifying specific capability boundaries
- Grounding recommendations in empirical findings

### The Broken Clock Insight

The paper's central metaphor—the broken clock—captures a profound truth about current AI capabilities:

> **A broken clock is right twice a day, but you don't know which two times.**

This encapsulates the epistemological challenge: LLMs produce correct outputs some of the time, but without reliable mechanisms to distinguish correct from incorrect instances, their outputs cannot constitute *knowledge* in the classical sense of justified true belief. The justification component is missing.

---

## AGENTS APPLIED

| Agent | Role in Analysis | Key Contribution |
|-------|------------------|------------------|
| **meta-observer** | Process monitoring, bias detection | Reflexive quality assessment |
| **socratic-examiner** | Foundational questioning | Epistemological probes |
| **skeptical-challenger** | Methodological critique | Identified limitations |
| **network-epistemologist** | Citation/knowledge mapping | Testimony chain analysis |
| **connection-mapper** | Conceptual dependencies | Dependency visualization |
| **emergence-verifier** | Pattern validation | Emergent phenomena assessment |
| **empiricist-gatherer** | Evidence collection | Strength ratings |
| **dialectical-synthesizer** | Thesis-antithesis-synthesis | Aufhebung resolutions |
| **collective-intelligence-curator** | Multi-source integration | Consensus synthesis |
| **justice-arbiter** | Fairness analysis | Stakeholder impacts |
| **care-ethicist-connector** | Relationship focus | Care considerations |

---

## SKILLS APPLIED

| Skill | Application |
|-------|-------------|
| **emergent-inquiry** | 6-phase analysis cycle |
| **network-knowledge** | Citation network analysis |
| **dialectical-synthesis** | Thesis-antithesis resolution |
| **reflexive-monitoring** | Bias detection and validity |
| **stakeholder-analysis** | Impact assessment |
| **ethical-deliberation** | Multi-framework ethics |

---

*Analysis conducted using the Hybrid Framework ("The Symposium") - Emergent-Epistemic Queen*
