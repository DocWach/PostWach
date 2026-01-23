# Critique: NATO STO Potential Topics - Research Questions Analysis

**Document Version:** 1.0
**Date:** 2026-01-22
**Author:** University of Arizona PostDoc Research
**Source Document:** Background docs/NATO/NATO STO Potential Topics.pdf

---

## Executive Summary

This critique analyzes the nine research topics proposed in the NATO STO Potential Topics document, focusing on the sufficiency of core research questions. While the document provides a solid foundation for a Technical Activity Proposal (TAP), several significant gaps exist that could undermine the research program's ability to deliver on its central promise: producing "analytically credible, reusable, and decision-relevant insights."

**Key findings:**
- Validation and verification questions are systematically underaddressed
- Multinational/coalition considerations need strengthening given the NATO context
- The connection to Mission Engineering and acquisition lifecycle is underdeveloped
- Failure modes and adversarial considerations are largely absent
- A 10th topic on comparative effectiveness should be added

---

## Topic-by-Topic Analysis

### Topic 1: Methodological Foundations of AI-Augmented Wargaming

**Current Core Questions:**
1. What elements of the wargaming lifecycle are most amenable to AI augmentation?
2. How does AI-augmented wargaming differ methodologically from traditional approaches?
3. What minimum methodological standards are required for analytical credibility?
4. How can uncertainty, assumptions, and limitations be documented and audited?

**Assessment:** Questions are reasonable but assume answers to foundational issues.

**Gaps Identified:**

| Gap | Issue | Impact |
|-----|-------|--------|
| Validation criteria | No empirical approach to determine methodology produces better outcomes | Cannot demonstrate value |
| Reproducibility | No question about whether different teams reach similar conclusions | Undermines credibility |
| Boundary conditions | Which wargame types (seminar, matrix, computational) does methodology apply to? | Overgeneralization risk |
| Credibility definition | "Analytical credibility" is assumed but never operationally defined | Circular reasoning |

**Recommended Additions:**

> **RQ 1.5:** What empirical validation approaches can establish that AI-augmented wargaming produces demonstrably superior insights compared to traditional methods, and how should baseline performance be established?

> **RQ 1.6:** Under what conditions (wargame type, participant expertise, problem domain) does the methodology produce reproducible results across different implementation teams?

> **RQ 1.7:** What operational criteria define "analytical credibility" for AI-augmented wargaming, and who has authority to certify compliance?

---

### Topic 2: Human-AI Teaming and Cognitive Roles in Wargaming

**Current Core Questions:**
1. What cognitive roles should AI play (facilitator, challenger, synthesizer, etc.)?
2. How does AI influence group dynamics, cognitive bias, anchoring, and groupthink?
3. Under what conditions does AI improve vs. degrade human judgment?
4. What training, guardrails, and interfaces ensure humans remain accountable?

**Assessment:** Good coverage of immediate teaming concerns; weak on long-term and cross-cultural issues.

**Gaps Identified:**

| Gap | Issue | Impact |
|-----|-------|--------|
| Trust calibration | When *should* humans override AI? When defer? | Under/over-reliance |
| Skill atrophy | Long-term effect on human analyst capability | Institutional capacity loss |
| Cultural variance | NATO nations have different AI comfort levels | Adoption friction |
| Disagreement resolution | What happens when AI and humans disagree? | Decision paralysis |
| Workload distribution | How is cognitive load managed in teaming? | Burnout, errors |

**Recommended Additions:**

> **RQ 2.5:** How should appropriate trust calibration be developed, and what indicators help humans know when to defer to vs. override AI recommendations?

> **RQ 2.6:** What are the long-term effects of AI augmentation on human analyst expertise development and institutional analytic capacity?

> **RQ 2.7:** How do national and cultural differences in AI acceptance affect human-AI teaming effectiveness in multinational wargaming contexts?

> **RQ 2.8:** What protocols should govern resolution when AI recommendations conflict with expert human judgment?

---

### Topic 3: AI-Supported Generation of Core Wargaming Artifacts

**Current Core Questions:**
1. Which artifacts can AI reliably generate or co-generate?
2. How can AI outputs be constrained to doctrinally/technically/politically plausible bounds?
3. How should provenance, assumptions, and confidence levels be represented?
4. How do AI-generated artifacts compare in quality to human-generated ones?

**Assessment:** Generation-focused but weak on verification and robustness.

**Gaps Identified:**

| Gap | Issue | Impact |
|-----|-------|--------|
| Verification | How verify artifacts are *correct*, not just plausible? | Plausibility ≠ validity |
| Adversarial robustness | Can generated scenarios be gamed by participants? | Manipulation vulnerability |
| Distribution shift | How handle scenarios outside training data? | Novel situation failure |
| Interoperability | Integration with NATO formats (STANAGs, ORBATs)? | Adoption barrier |
| Computational requirements | What resources needed for generation? | Feasibility constraints |

**Recommended Additions:**

> **RQ 3.5:** How can AI-generated artifacts be verified for correctness rather than merely plausibility, and what independent validation is required before operational use?

> **RQ 3.6:** What safeguards prevent sophisticated participants from gaming AI-generated scenarios by exploiting knowledge of AI behavior patterns?

> **RQ 3.7:** How should AI systems handle scenario generation requests that fall outside their training distribution, and how are such boundary conditions detected?

> **RQ 3.8:** What technical standards ensure AI-generated artifacts are interoperable with existing NATO data formats and systems?

---

### Topic 4: Knowledge Management, Traceability, and Analytic Memory

**Current Core Questions:**
1. How can wargaming knowledge be structured for long-term reuse?
2. What models support traceability from scenario → gameplay → insight → recommendation?
3. How can AI support cross-game synthesis and longitudinal analysis?
4. How should sensitive, classified, and releasable knowledge be partitioned?

**Assessment:** Good structural focus but weak on knowledge lifecycle and contradictions.

**Gaps Identified:**

| Gap | Issue | Impact |
|-----|-------|--------|
| Knowledge decay | When does wargaming knowledge become obsolete? | Stale insights persist |
| Contradiction handling | What if different wargames produce conflicting conclusions? | Incoherent knowledge base |
| Existing systems | Integration with NATO knowledge management infrastructure | Parallel systems |
| Attribution | Who owns knowledge in multinational contexts? | IP and caveat issues |
| Version control | How does knowledge evolve over time? | Audit trail gaps |

**Recommended Additions:**

> **RQ 4.5:** How should contradictions between insights from different wargames be detected, analyzed, and resolved to maintain knowledge base coherence?

> **RQ 4.6:** What criteria determine when wargaming knowledge has become obsolete, and what processes govern knowledge retirement?

> **RQ 4.7:** How should knowledge attribution and national caveats be managed when insights derive from multinational classified contributions?

> **RQ 4.8:** How does the proposed knowledge management approach integrate with existing NATO and national knowledge management systems?

---

### Topic 5: Integration with Modelling & Simulation (M&S) Ecosystems

**Current Core Questions:**
1. How can AI-supported qualitative wargaming be coupled with quantitative M&S?
2. What interfaces are required between narrative gameplay and simulation I/O?
3. How can AI assist in selecting, configuring, or interpreting M&S models?
4. Where are the limits of integration due to fidelity, data, or epistemic mismatch?

**Assessment:** Addresses coupling but weak on validation and standards.

**Gaps Identified:**

| Gap | Issue | Impact |
|-----|-------|--------|
| Integration validation | Does combining approaches actually improve results? | Assumed but unproven |
| Uncertainty propagation | How do M&S and wargame uncertainties combine? | Miscalibrated confidence |
| Standards compliance | Compatibility with HLA, DIS, SISO standards | Interoperability barriers |
| Computational feasibility | Real-time integration requirements | Practical constraints |
| Model selection criteria | How choose among competing M&S options? | Suboptimal model use |

**Recommended Additions:**

> **RQ 5.5:** How should uncertainty from M&S models be propagated through and combined with uncertainty from human wargame judgments to produce calibrated confidence estimates?

> **RQ 5.6:** What evidence demonstrates that integrated qualitative-quantitative approaches produce superior insights compared to either method alone?

> **RQ 5.7:** How does the proposed integration architecture comply with existing M&S interoperability standards (HLA, DIS, SISO)?

> **RQ 5.8:** What computational resources and latency constraints apply to real-time M&S integration during wargame execution?

---

### Topic 6: Capability Gap Identification and Hypothesis Testing

**Current Core Questions:**
1. How can AI help formulate, challenge, and refine capability gap hypotheses?
2. What constitutes sufficient evidentiary support for an identified gap?
3. How can alternative explanations and confounding factors be explored?
4. How should confidence, risk, and prioritization be communicated to acquisition authorities?

**Assessment:** This is the weakest topic despite being critical for acquisition decisions.

**Gaps Identified:**

| Gap | Issue | Impact |
|-----|-------|--------|
| False discovery | How distinguish genuine gaps from AI artifacts/bias? | Spurious gaps drive acquisition |
| Gap prioritization | How rank multiple gaps for resource allocation? | Suboptimal investment |
| Temporal dynamics | How do gaps evolve as threats change? | Static analysis of dynamic problem |
| DOTMLPFI mapping | How do gaps map to solution spaces? | Disconnected from solutions |
| Process integration | How integrate with NDPP, JCIDS? | Parallel processes |
| Negative evidence | How demonstrate a gap does NOT exist? | Confirmation bias |

**Recommended Additions:**

> **RQ 6.5:** How can false positive gap identification (spurious gaps from AI bias or wargame design artifacts) be distinguished from genuine capability shortfalls, and what evidentiary thresholds govern gap validation?

> **RQ 6.6:** How should AI-identified capability gaps be mapped to DOTMLPFI solution spaces and integrated with existing NATO Defence Planning Process outputs?

> **RQ 6.7:** What framework governs gap prioritization when multiple gaps compete for limited acquisition resources?

> **RQ 6.8:** How should the temporal evolution of capability gaps be tracked and incorporated into dynamic planning processes?

> **RQ 6.9:** What constitutes sufficient evidence to conclude that a hypothesized capability gap does NOT exist (negative findings)?

---

### Topic 7: Sponsor Engagement, Transparency, and Decision Confidence

**Current Core Questions:**
1. How can AI improve sponsor understanding of assumptions, trade-offs, and decision logic?
2. What visualization and narrative techniques best convey AI-supported insights?
3. How does AI affect sponsor confidence, perceived legitimacy, and willingness to act?
4. What governance mechanisms ensure responsible use in sponsor-facing contexts?

**Assessment:** Communication-focused but weak on accountability and conflict.

**Gaps Identified:**

| Gap | Issue | Impact |
|-----|-------|--------|
| Expectation management | How communicate AI limitations without undermining confidence? | Over/under-trust |
| Accountability | Who is accountable when AI-informed decisions fail? | Responsibility diffusion |
| Multi-stakeholder conflict | What when sponsors draw different conclusions? | Decision gridlock |
| Political sensitivity | Some gaps may be politically inconvenient | Suppression pressure |
| Escalation pathways | When should AI insights escalate to higher authority? | Information flow gaps |

**Recommended Additions:**

> **RQ 7.5:** How should accountability be assigned when acquisition decisions informed by AI-augmented wargaming produce suboptimal outcomes?

> **RQ 7.6:** What protocols govern situations where different sponsors or nations draw conflicting conclusions from the same AI-supported analysis?

> **RQ 7.7:** How should AI limitations be communicated to sponsors in ways that calibrate expectations without undermining confidence in valid outputs?

> **RQ 7.8:** What escalation pathways should exist when AI-augmented analysis identifies findings with significant political or strategic implications?

---

### Topic 8: Ethics, Governance, and Responsible Use of AI in Wargaming

**Current Core Questions:**
1. What ethical risks arise from AI-supported scenario generation and adversary modeling?
2. How should bias, hallucination, and over-confidence be detected and mitigated?
3. What governance models are appropriate for multinational AI-enabled processes?
4. How do NATO values and legal frameworks constrain AI use?

**Assessment:** Covers basics but weak on red lines and accountability mechanisms.

**Gaps Identified:**

| Gap | Issue | Impact |
|-----|-------|--------|
| Red lines | What should AI NEVER do in wargaming? | Boundary ambiguity |
| Data provenance | Governance of AI training data | Legal/ethical exposure |
| Dual-use risk | Could AI wargaming capabilities be misused? | Security vulnerability |
| Audit mechanisms | How are AI decisions logged for review? | Accountability gaps |
| Emergent behavior | How govern behavior from multi-component AI? | Unpredictable outputs |
| Environmental impact | Resource consumption of AI systems | Sustainability concerns |

**Recommended Additions:**

> **RQ 8.5:** What red lines should absolutely constrain AI behavior in wargaming (e.g., modeling specific real-world leaders, generating certain scenario types), and how are these enforced?

> **RQ 8.6:** What governance applies to data used to train AI systems for wargaming, including consent, provenance, and retention requirements?

> **RQ 8.7:** How should emergent behaviors from multi-component AI systems be monitored, and what intervention mechanisms exist when unexpected behaviors occur?

> **RQ 8.8:** What audit trails and logging requirements ensure AI-influenced decisions can be reconstructed and reviewed post-hoc?

> **RQ 8.9:** What safeguards prevent AI wargaming capabilities from being misused for unauthorized purposes or by adversaries?

---

### Topic 9: Pathways to Operationalization and Future CDTs

**Current Core Questions:**
1. What elements are ready for transition into CDTs?
2. What operational environments are best suited for early adoption?
3. What technical and organizational barriers must be resolved?
4. How should success be measured in future trials?

**Assessment:** Addresses transition but weak on sustainment and workforce.

**Gaps Identified:**

| Gap | Issue | Impact |
|-----|-------|--------|
| Sustainment model | Who maintains capability long-term? | Capability decay |
| Workforce development | What training pipeline needed? | Skill shortages |
| Acquisition strategy | Build, buy, or partner? | Suboptimal procurement |
| Regression testing | How ensure capability doesn't degrade with updates? | Silent failure |
| Cost-benefit analysis | What's the business case? | Unjustified investment |
| Technology refresh | How keep pace with AI advancement? | Obsolescence |

**Recommended Additions:**

> **RQ 9.5:** What sustainment model (personnel, funding, governance, technology refresh) is required for long-term viability of AI-augmented wargaming capabilities across the Alliance?

> **RQ 9.6:** What workforce development and training pipeline is required to develop and maintain AI wargaming practitioners?

> **RQ 9.7:** What acquisition strategy (build, buy, partner, hybrid) best serves Alliance interests for AI wargaming capabilities?

> **RQ 9.8:** What regression testing and continuous validation processes ensure capability does not degrade as AI models are updated or environments change?

> **RQ 9.9:** What cost-benefit framework should govern investment decisions in AI-augmented wargaming capabilities?

---

## Cross-Cutting Gaps

Several themes are systematically underaddressed across all nine topics:

### 1. Validation and Baseline Establishment

**Problem:** No questions establish how to measure current (non-AI) wargaming effectiveness to demonstrate improvement.

**Impact:** Without baselines, claims of "improvement" are unfalsifiable.

**Recommendation:** Add explicit questions about baseline measurement and comparative effectiveness to Topics 1, 3, 5, and 6.

### 2. Adversary Considerations

**Problem:** The document focuses on NATO's use of AI but ignores how adversaries might:
- Exploit AI-augmented wargaming outputs
- Counter AI analysis through deception
- Develop their own AI wargaming capabilities

**Impact:** Single-sided analysis of a competitive domain.

**Recommendation:** Add adversarial analysis questions to Topics 3, 6, and 8.

### 3. Technical Architecture

**Problem:** No questions address actual infrastructure requirements:
- Cloud vs. on-premise deployment
- Security classification handling
- Data sovereignty across nations
- Computational resource requirements

**Impact:** Theoretical capability without implementation path.

**Recommendation:** Add technical architecture questions to Topics 3, 4, 5, and 9.

### 4. Failure Modes

**Problem:** No systematic treatment of:
- What happens when AI fails or hallucinates
- How failures are detected
- Recovery and fallback procedures
- Learning from failures

**Impact:** No resilience against inevitable AI failures.

**Recommendation:** Add failure mode questions to Topics 1, 2, 3, and 6.

### 5. Time and Tempo

**Problem:** No questions about whether AI-augmented wargaming can operate at decision-relevant timescales.

**Impact:** May produce excellent analysis too late to inform decisions.

**Recommendation:** Add tempo questions to Topics 1, 5, and 6.

### 6. Mission Engineering Linkage

**Problem:** Given the proposal's focus on ME-wargaming-acquisition integration, the connection is underdeveloped.

**Impact:** Disconnected from the core research proposition.

**Recommendation:** Strengthen Topic 6 with explicit ME integration questions; add ME references to Topics 3, 4, and 7.

### 7. Multinational Interoperability

**Problem:** Insufficient attention to nations with:
- Different AI policies and regulations
- Different classification levels and releasability
- Different legal frameworks for AI use
- Different comfort levels with AI

**Impact:** NATO-wide adoption blocked by national constraints.

**Recommendation:** Add multinational considerations to Topics 2, 4, 7, and 8.

---

## Recommended Additional Topic

### Topic 10: Validation, Verification, and Comparative Effectiveness

**Why this matters:**
Without rigorous comparative evaluation, the entire research program risks producing capabilities that *feel* better but aren't demonstrably superior. This topic directly supports the overarching research question about "measurably improving" capability development.

**Core Research Questions:**

> **RQ 10.1:** How should baseline wargaming effectiveness be measured to enable rigorous comparison with AI-augmented approaches?

> **RQ 10.2:** What experimental designs can isolate the contribution of AI from other factors (facilitator skill, scenario quality, participant expertise, game mechanics)?

> **RQ 10.3:** How should AI-augmented wargaming be validated against historical cases, expert consensus, or operational outcomes?

> **RQ 10.4:** What constitutes sufficient evidence that AI augmentation improves the quality of acquisition decisions derived from wargaming?

> **RQ 10.5:** How should comparative studies be designed to account for the uniqueness of individual wargames and the difficulty of controlled experimentation?

> **RQ 10.6:** What metrics beyond traditional wargaming evaluation (insight quality, decision confidence) should be used to assess AI contribution?

**Expected Advancement:**
- Rigorous evidence base for AI-augmented wargaming value proposition
- Empirically validated claims for sponsor engagement
- TRL alignment: Cross-cutting validation framework

**KRL Alignment:** 4-6 (moving from hypothesis to replication)

---

## Summary of Recommended Changes

| Topic | Current RQs | Recommended Additions | Priority |
|-------|-------------|----------------------|----------|
| 1. Methodology | 4 | +3 (validation, reproducibility, credibility definition) | High |
| 2. Human-AI Teaming | 4 | +4 (trust calibration, skill atrophy, culture, disagreement) | High |
| 3. Artifact Generation | 4 | +4 (verification, adversarial, distribution shift, interop) | High |
| 4. Knowledge Management | 4 | +4 (decay, contradictions, attribution, integration) | Medium |
| 5. M&S Integration | 4 | +4 (uncertainty, validation, standards, computation) | Medium |
| 6. Gap Identification | 4 | +5 (false discovery, DOTMLPFI, prioritization, temporal, negative) | **Critical** |
| 7. Sponsor Engagement | 4 | +4 (accountability, conflict, limitations, escalation) | Medium |
| 8. Ethics/Governance | 4 | +5 (red lines, data, emergent, audit, dual-use) | High |
| 9. Operationalization | 4 | +5 (sustainment, workforce, acquisition, regression, cost-benefit) | Medium |
| **10. NEW: Validation** | 0 | +6 (baseline, experimental design, historical validation, evidence standards) | **Critical** |

**Total:** 36 current questions → 80 recommended questions (44 additions)

---

## Conclusion

The NATO STO Potential Topics document provides a credible starting point but requires significant strengthening to deliver on its promise of "analytically credible, reusable, and decision-relevant insights." The most critical gaps are:

1. **Validation framework** (new Topic 10) - Cannot claim improvement without measurement
2. **Topic 6 strengthening** - The acquisition bridge is underdeveloped
3. **Failure mode analysis** - No resilience against inevitable AI failures
4. **Multinational considerations** - NATO context demands attention to national variance

Addressing these gaps will strengthen the TAP and increase the probability of producing research that actually improves capability development and acquisition decisions.

---

*Document prepared for NATO STO TAP development.*
*Version 1.0 - 2026-01-22*
