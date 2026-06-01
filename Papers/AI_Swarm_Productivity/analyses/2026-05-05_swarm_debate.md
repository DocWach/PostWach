# AI-Swarm Productivity Scorecards — Stage 3 Dialectical Synthesis

**Date:** 2026-05-05
**Synthesizer:** dialectical-synthesis agent (Stage 3 of 3)
**Input dataset:** 110 valid + 4 parse-failed scorecards, 2026-02-25 through 2026-05-04
**Stage 1 inputs:** researcher / pattern-detector / counterexample-hunter briefs
**Stage 2 inputs:** Champion / Skeptic / Methodologist / Reflexivist position papers
**Target venues:** CSER 2027, ESEM 2027, EMSE
**Researcher of record:** Paul Wach, University of Arizona (Systems Engineering & AI)
**Artifact tag (per [R016]):** This synthesis is a **(b) demonstrated capability** — a multi-agent debate pipeline produced a defensible analytical position; it is not yet **(c) integrated** with the manuscript pipeline or external review.

---

## Table of Contents

1. [Headline Finding](#1-headline-finding)
2. [Dataset Snapshot](#2-dataset-snapshot)
3. [The Four Positions](#3-the-four-positions)
4. [Convergence: Where the four agents agree](#4-convergence)
5. [Divergence: Where the four agents disagree](#5-divergence)
6. [Conclusions per RQ](#6-conclusions-per-rq)
7. [Recommended Paper Framing](#7-recommended-paper-framing)
8. [Threats to Validity (consolidated)](#8-threats-to-validity)
9. [Next-Step Inputs (Cycle 2 future work)](#9-next-step-inputs)
10. [Operational Recommendations](#10-operational-recommendations)
11. [Appendix A: Data Quality Issues](#appendix-a-data-quality-issues)
12. [Appendix B: Outliers Worth Excluding from Headline Computations](#appendix-b-outliers)

---

<a id="1-headline-finding"></a>
## 1. Headline Finding

> **A 14-week longitudinal action study (N=110 sessions, 6 hives, single researcher) produced a *measurement-publication coupled* trajectory in which a calibrated authoring-equivalent throughput of 5–12 pg/hr was sustained on substantive research writing — roughly 1.5–3× the 0.75 pg/hr academic baseline — while the unfiltered raw mean of 41.35 pg/hr (≈55× baseline) was driven by mechanical-conversion outliers and is not defensible as a productivity claim. The dataset's most reliable signals are second-order: a topology-by-agent-count effect on rework (8+ agents median rework 0.064 vs star-topology failure-association 8/10), a multi-axis March-to-May maturation trajectory (median pph 2.55 → 3.12, agents/session 2.72 → 3.77, utilization 0.904 → 0.977, failure-sessions 8 → 2), and a Windows/OneDrive/ARM64 environmental friction floor that bounded ~29% of blocked sessions.**

This sentence is the only one of any length in this report that the user may quote directly without further qualification. It survives all four Stage 2 lenses because it (i) abandons the 41.35/55× headline that the Skeptic shows is contaminated by `pypdf`-style mechanical conversion (e.g., `2026-03-07-postwach-05` at 950pp = `pypdf` extraction of Zeigler TMS2018), (ii) keeps the Champion's calibrated band but wraps it in the Reflexivist's *measurement-publication coupling* qualifier, and (iii) leads with second-order findings (topology × rework, maturation trajectory, Windows friction) that the Methodologist judged GQM-defensible.

---

<a id="2-dataset-snapshot"></a>
## 2. Dataset Snapshot

| Property | Value |
|----------|-------|
| Valid scorecards loaded | 110 |
| YAML parse failures (excluded) | 4 (2 of these are top-decile sessions per counterexample-hunter) |
| Total files in scorecard directory | 114 |
| Date range | 2026-02-25 → 2026-05-04 |
| Hives | PostWach 85 (77.3%), GI-JOE 13, SEAD 5, SysMLv2 4, MACQ 2, Roadmapping 1 |
| Sessions with valid timing | 69 of 110 |
| Raw mean pph (timed sessions) | 41.35 (≈55.13× academic baseline 0.75 pg/hr) |
| PostWach pph mean | 47.19 |
| PostWach pph median | 2.50 |
| Sessions with cost data | <1% (1 of 110) |
| Sessions with quality-gate `fail` row | small minority (e.g., `2026-03-26-postwach-02` records one gate fail; pass-only construction dominates) |
| Topology distribution | none 61, star 30, hierarchical 11, mesh 6, hybrid 1, hierarchical-mesh 1 |
| Topology medians (pph) | none 1.20, star 3.00, hierarchical 11.92, mesh 7.87 |
| Agent-count medians (pph) | 0 agents 1.13, 1–3 agents 3.60, 4–7 agents 3.43, 8+ agents 7.33 |
| Agent-count rework (8+ bin) | 0.064 (lowest of all bins) |
| Researcher field anomaly | 1 of 110 = "Gemini CLI" (`2026-05-04-postwach-04`) |
| Top blocker categories | Windows/OneDrive/ARM64 friction (29%), agent coordination/timeouts (20%), rework loops (14%) |
| Temporal halves (median pph) | March 2.55 → April–May 3.12 |
| Temporal halves (agents/session mean) | March 2.72 → April–May 3.77 |
| Temporal halves (utilization) | March 0.904 → April–May 0.977 |
| Temporal halves (failure sessions) | March 8 → April–May 2 |

Source: Stage 1 briefs; spot-verification on `2026-03-26-postwach-02`, `2026-03-07-postwach-05`, `2026-03-07-gi-joe-02`, `2026-04-12-postwach-01`, `2026-05-04-postwach-04`, `2026-03-03-postwach-01`.

---

<a id="3-the-four-positions"></a>
## 3. The Four Positions

### 3.1 Champion (researcher)
The 41.35/55× headline is dead, but a *calibrated* 5–12 pg/hr authoring-equivalent rate survives — 1.5–3× the academic baseline — with PostWach median 2.50 across 85 sessions, a topology effect that survives outlier removal (hierarchical median 11.92, mesh 7.87 vs none 1.20), agent-count medians monotonic into the 8+ bin (7.33) with the lowest rework ratio (0.064), and a multi-axis March-to-May maturation signal (rate +22%, agents +38%, utilization +7 pp, failures −75%). The pattern replicates within-dataset in two harder domains (GI-JOE ontology n=13 at 5.23 median; MACQ NNSA proposals n=2 at 16.67). Long-session collapse to 0.57–2.5 pg/hr is *workmode discrimination*, not failure: short bounded tasks pull high pph; cognitively heavy lifting earns low pph but high downstream value.

### 3.2 Skeptic (skeptical-challenger)
Even 5–12 pg/hr should not be reported. The instrument is the subject and the subject is the author. METR (2025) showed a 43-point swing between perceived and actual speedup in experienced developers; this dataset's calibrated estimate is generated from the same self-report apparatus. `perception_note` is a smoking gun (verbatim "dramatically faster" appears in `2026-03-03-postwach-02` and `2026-03-04-postwach-02`; subject-generated counterfactuals like "2-3 person-weeks of experienced ontology engineer + domain expert" appear in `2026-03-07-gi-joe-02`, "6-12 person-weeks" in `2026-03-09-gi-joe-01`, and "4-6 hours manual equivalent compressed to ~1.5 hours" in `2026-03-03-postwach-01` — all without instrumented baselines). Date gaps (03-13→03-16, 04-15→04-19, 04-23→04-28) are silent denominators; "Gemini CLI" entry (`2026-05-04-postwach-04`) is existence proof of agent-authored measurement; "page" smuggles in `pypdf` extraction (`2026-03-07-postwach-05` = 950pp) and Python/Dockerfile/CI YAML (`2026-04-12-postwach-01` = 67pp). Recommends reframing as a **measurement-methodology paper** with title candidates "What 110 Self-Reported AI-Swarm Sessions Cannot Tell Us" or "The Instrument Problem in Single-Operator AI Productivity Studies."

### 3.3 Methodologist (methodology-advisor)
Attacks the framework, not the numbers. The GQM cascade is implicit and reverse-engineering reveals the GQM-defensible fields are `blocked_minutes`, `tests_passed`, `tests_failed`, `agent_failures`, `retries`; the measured-because-easy fields are `pages_produced`, `agents_spawned`, `first_pass_quality_pct`. By construct: D1 (Output) has a severe construct-congruence violation — "pages" cannot mean ontology triples, prose, code LOC, and scaffolding all at once and must be replaced with stratified counts; D2 (AI Efficiency) is empirically intractable as specified (`agents_spawned` polysemy, cost 99.1% missing makes RQ2 unanswerable, topology default-or-unset is instrument failure); D3 (Quality) is contaminated by pass-only construction (survivorship analog) and circular `first_pass_quality_pct`; D4 (Process) is mostly defensible but `rework_files` schema indiscipline (int vs list) is symptomatic. Net judgment: the dataset can answer RQ1 *descriptively*; RQ2 cannot be answered (no paired traditional-mode observations); RQ3 only *partially* via medians and IQRs. Recommends Pydantic schema enforcement at scorecard creation, artifact-type-stratified output fields, mandatory failure logging, MCP-telemetry-driven cost capture, and explicit reframing as **action-research Cycle 1 (Staron 2020) — pilot diagnose+action+evaluate**, with Cycles 2–3 as follow-on publications. Under that frame, the construct threats become contributions; under the original frame they are fatal.

### 3.4 Reflexivist (meta-observer)
The instrument designer, swarm orchestrator, governance-rule author, eventual paper author, and study subject are the same person. This is methodologically coherent for action research only if the loop closure is named. [R014] mandates self-measurement on penalty of governance violation, making `perception_note` dual-purpose (raw self-report and authorial framing for the future reader); `gates_run` is what-the-researcher-chose-to-test with an endogenous denominator. The Gemini-CLI scorecard (`2026-05-04-postwach-04`) is not just an outlier — it makes the measurement process of the other 109 entries ambiguous (typed by Paul vs drafted by Claude under review vs pasted from template?). This synthesis itself is the 111th measurement event, and either the dataset includes the meta-level (paper analyzes a corpus that includes analysis-of-corpus) or has a hole exactly where the meta-level lives. The honest framing names this **"measurement-publication coupling"**: the perception_note voice shifts from log to story, two cards contain verbatim "Most productive session... to date" implying running narrative curation, and `MEMORY.md` (350 lines, 43.3 KB) autocorrelates every session — these are not 110 i.i.d. observations but 1 trajectory through a slowly-evolving researcher-AI joint state. The honest abstract names study, instrument, designer, orchestrator, governance author, and 1-of-110 AI-authored scorecard explicitly.

---

<a id="4-convergence"></a>
## 4. Convergence: Load-Bearing Findings That Survive All Four Lenses

These are the claims publishable in CSER 2027 / ESEM 2027 / EMSE under any of the four reframings. They are robust to Champion's calibration, Skeptic's instrument critique, Methodologist's GQM audit, and Reflexivist's measurement-publication coupling.

### C1. The 41.35 pg/hr / 55× academic-baseline headline is not defensible.
All four agents agree (Champion explicitly retires it; Skeptic attacks it; Methodologist labels it construct-violating; Reflexivist treats it as the Hawthorne+publication artifact). It survives in the paper only as a *naive analysis sidebar* that motivates the calibration step. **Tag: (a) research artifact** — a number computable from the YAML files but not a productivity claim about anything.

### C2. The instrument is the subject is the author is the architect.
All four agents stipulate this without dispute. The disagreement is whether this is **fatal** (Skeptic), **frame-correcting** (Methodologist, "this is action research"), **structurally honest** (Reflexivist, "name it"), or **disclosable but not paper-killing** (Champion). Convergent claim: the paper *must* enumerate all role-stacking explicitly in §7 (instrument designer + swarm orchestrator + governance-rule author + study subject + analyst + future paper author + 1-of-110 scorecards filled by an AI agent). The Gemini-CLI scorecard `2026-05-04-postwach-04` is the canonical exhibit.

### C3. The most-defensible second-order finding is the topology × rework × failure correlation.
Skeptic explicitly preserves this as one of three findings that survive his attack. Methodologist accepts it as GQM-defensible (rework_files and agent_failures are framework-grounded). Champion centers it. Reflexivist does not contest. **Specific defensible facts:**
- 8/10 failure-mode sessions are `star` topology.
- Rework-ratio variance differs across topologies in a structurally interpretable way (star has more shallow-fanout retries; hierarchical has fewer but heavier rework events; 8+ agent bin has lowest rework at 0.064).
- This is the dataset's strongest mechanism-level claim and should be the empirical core of the paper.

### C4. The maturation trajectory is real but is *one* trajectory, not a population effect.
All four accept the multi-axis March → April–May trajectory (median pph 2.55 → 3.12; agents/session 2.72 → 3.77; utilization 0.904 → 0.977; failure sessions 8 → 2). Skeptic notes this is a single operator's learning curve and could be METR-style perception correction (W0 → W2 trough). Reflexivist notes the trajectory is autocorrelated by `MEMORY.md` accretion. Methodologist accepts it as a defensible *learning-curve descriptive*. Champion centers it. Convergent claim: report the trajectory as a *single-operator learning curve in a co-evolving researcher-AI system*, not as evidence about AI-swarm productivity in general.

### C5. Environmental friction is a real, GQM-defensible bottleneck.
`blocked_minutes` and `blockers` text both survive Methodologist's audit. The Windows/OneDrive/ARM64 cluster (29% of blocked sessions) and the agent-coordination/timeout cluster (20%) are claims about the operating environment, not about the cognitive value of swarm augmentation. Champion accepts; Skeptic does not contest (these are environmental, not perception); Methodologist endorses; Reflexivist treats as defensible because it is externalized to system behavior.

### C6. Cost-comparison RQ2 is empirically unsupportable from this dataset.
99.1% of cards lack cost data (1 of 110 has any USD figure). All four agents converge: RQ2 must be removed, deferred, or reframed as "what would be required to answer RQ2 in Cycle 2." Methodologist is most explicit; Champion and Reflexivist do not contest; Skeptic uses the missingness as additional evidence for the measurement-methodology reframing.

### C7. The scorecard schema itself is the most defensible *artifact* contribution.
Even Skeptic and Reflexivist (the harshest lenses) leave the schema standing as a publishable research artifact. Methodologist judges that with stratified output fields, Pydantic enforcement, and failure-or-skip logging, the schema becomes a contribution-grade instrument. **Tag: currently (a) research artifact; with the Methodologist's hardening, becomes (b) demonstrated capability.**

### C8. Pages-as-construct collapses and must be replaced.
All four agents agree (Champion via Counterexample-hunter inheritance; Skeptic explicitly; Methodologist as primary recommendation; Reflexivist via the autocorrelation argument). Concrete failures: `2026-03-07-postwach-05` (950 pp = `pypdf` mechanical extraction), `2026-04-12-postwach-01` (67 pp = mostly Python LOC, Dockerfile, CI YAML, Turtle). Stratified counts (`ontology_triples`, `prose_words`, `code_loc`, `config_lines`, `slide_count`, `figure_count`) replace the single `pages_produced` field for Cycle 2.

### C9. The defensible authoring-equivalent rate is 5–12 pg/hr (1.5–3× baseline) for substantive research writing, conditional on the construct-stratification fix.
Champion's headline. Skeptic's strongest objection ("you're trimming outliers your subject flagged") is partially defused by the convergence rule: the claim is conditional on stratified counts (C8), which the Methodologist independently demands and the Reflexivist endorses. The 1.5–3× range survives because (i) it is bracketed below by the long-session collapse to 0.57–2.5 pg/hr (substantive research) and above by the 5–12 pg/hr authoring band (drafting + structured writing), and (ii) it does not cross the order-of-magnitude threshold that would itself be an extraordinary claim. **Caveat: report as a *single-operator authoring-equivalent throughput band*, not as a productivity multiplier.**

### C10. Within-dataset replication in two harder domains is a useful corroborating fact.
GI-JOE ontology work (n=13, median 5.23 pph) and MACQ NNSA proposals (n=2 — too small for inference but suggestive at 16.67) replicate the band C9. All four agents agree this is *secondary* evidence (small-n, same operator, cross-hive memory autocorrelation), not confirmatory replication. Report as "within-dataset corroboration" not "external replication."

---

<a id="5-divergence"></a>
## 5. Divergence: Open Tensions That Become Cycle 2 Inputs

These are the points where the four agents *genuinely* disagree — not where they emphasize differently. Each becomes a future-work or framing question.

### D1. Is the paper a productivity study or a measurement-methodology study?
**Champion:** primarily productivity, with measurement caveats.
**Skeptic:** primarily measurement-methodology; productivity numbers should not lead.
**Methodologist:** primarily framework-design and instrument-validation, with longitudinal action-research pilot.
**Reflexivist:** primarily a measurement-publication-coupled trajectory study; *both* productivity and measurement are inside one closed loop.

**Synthesis (see §7):** The paper should be **one** thing — an action-research Cycle-1 instrument-validation study with productivity descriptives as a secondary contribution — not a hedged compromise. This resolves the disagreement by adopting the Methodologist's framing as the *primary* spine and routing Champion's calibrated rate, Skeptic's measurement-methodology contributions, and Reflexivist's coupling concept to *sub-contributions* under that spine.

### D2. Is the 5–12 pg/hr band reportable as a number?
**Champion:** yes, with hedges.
**Skeptic:** no, because it comes from the contaminated apparatus.
**Methodologist:** yes, *if* stratified by artifact type (which the dataset does not yet support). Otherwise no.
**Reflexivist:** yes, but only as a property of the coupled trajectory, not as a population estimate.

**Open tension:** the band is conditional on the stratification fix that the dataset itself does not yet have. The honest position is to report the band with explicit conditional language ("under the assumption that authoring-relevant pages can be stratified out post-hoc, the operator-authoring-equivalent throughput is in the 5–12 pg/hr band; this estimate inherits all instrument-validity threats listed in §7"). Cycle 2 should *prospectively* stratify and re-estimate.

### D3. Is the Gemini-CLI scorecard a contamination, a curio, or a contribution?
**Champion:** curio — does not affect headline numbers.
**Skeptic:** contamination — proves the measurement instrument is not even reliably *species*-bounded.
**Methodologist:** instrument-failure exemplar — exactly the kind of polysemy the schema must rule out via Pydantic + author identity validation.
**Reflexivist:** contribution — it is the canonical exhibit that the loop is closed not just within Paul's mind but across the human-AI authorial boundary itself.

**Synthesis:** Adopt the Reflexivist reading: include the Gemini-CLI scorecard as a §7 case study illustrating measurement-publication coupling, then close the schema gap (per Methodologist) by adding an `instrument_author_identity` field in Cycle 2.

### D4. Should long-session-low-rate sessions be "workmode discrimination" or "perception-correction artifact"?
**Champion:** workmode discrimination — different tasks have different appropriate rates; long substantive-research sessions (0.57–2.5 pg/hr) are doing the harder work and the low rate is *correct*.
**Skeptic:** METR perception-correction — when the operator works longer, the gap between perceived and actual closes, and the rate drops because *the early-session rate was inflated*, not because the late-session task is harder.

These two readings make opposite predictions about Cycle 2 (Champion: stratifying by task type will resolve the U-shape; Skeptic: instrumented ground truth will show the early-session high rates were illusory). This is the sharpest open empirical question and is the natural pre-registration target for Cycle 2.

### D5. Is `MEMORY.md` autocorrelation a feature or a bug?
**Champion:** silent — does not directly contest.
**Skeptic:** confound — sessions are not i.i.d., so any aggregate statistic (medians included) is a property of the trajectory, not the operator-AI pair.
**Methodologist:** confound that the schema cannot fix at the per-session level; must be handled at the analysis level.
**Reflexivist:** *constitutive feature* of the system being studied — to remove autocorrelation would be to eliminate the very thing that makes a research-co-pilot useful.

**Open question:** is the unit of analysis the *session* (Skeptic, Methodologist) or the *trajectory* (Reflexivist, Champion implicitly)? Cycle 2 must decide. If trajectory, the right inferential machinery is time-series (state-space models, change-point detection on the multi-axis maturation trajectory), not session-level descriptives.

### D6. Should pass-only quality construction be patched or accepted?
**Champion:** patch (add fail logging) without re-doing existing data.
**Skeptic:** the existing data is uninterpretable on quality grounds; patching forward does not save the back catalog.
**Methodologist:** ban pass-only construction prospectively; treat back-catalog quality fields as advisory only.
**Reflexivist:** the pass-only construction is itself a finding about [R014]'s incentive structure (filling out a scorecard pre-publication selects for self-flattering gates).

**Synthesis:** Methodologist's prospective ban + Reflexivist's framing of the back-catalog gates as *evidence about the measurement loop, not about quality*. This means the paper reports `tests_passed` but does not report `first_pass_quality_pct` as a quality construct.

---

<a id="6-conclusions-per-rq"></a>
## 6. Conclusions per Research Question

### RQ1: What productivity dimensions are useful for AI-swarm-augmented research?
**Verdict: PARTIAL YES (descriptive only).**
The four-dimension scorecard (D1 Output, D2 AI Efficiency, D3 Quality, D4 Process) is itself the most defensible artifact contribution (per C7). The dataset can answer RQ1 *descriptively*: which fields fill, which fields are empty (cost: 99.1% missing per Stage 1), which fields exhibit construct-congruence failures (D1 `pages` per C8; D3 pass-only per D6), and which fields are GQM-defensible (D4 process, D2 agents/topology with polysemy fix). The dataset *cannot* answer RQ1 normatively (which dimensions matter most for outcome-grade productivity) without external review attached to artifact-stratified outputs. Cite Methodologist §3.3.

### RQ2: How does AI-swarm productivity compare to traditional research methods?
**Verdict: NO (empirically unsupportable from this dataset).**
99.1% of cards lack cost data; there are zero paired traditional-mode observations; subject-generated counterfactuals like "2-3 person-weeks" (`2026-03-07-gi-joe-02`) and "4-6 hours manual equivalent" (`2026-03-03-postwach-01`) are exactly the perception-not-instrumentation that METR (2025) showed swings 43 points. RQ2 must be removed from the CSER 2027 paper or reframed as "instrumentation requirements for answering RQ2 in Cycle 2." Cite Skeptic items 1, 6 + Methodologist §3.4 + Convergent finding C6.

### RQ3: What moderators affect AI-swarm productivity?
**Verdict: PARTIAL YES (medians and IQRs, no causal claims).**
The topology × rework × failure-mode correlation (C3) is the strongest moderator-style signal: 8/10 failure-mode sessions are star topology; 8+ agent bin has lowest rework (0.064). Agent-count median is monotonic into the 8+ bin. Session length exhibits a non-monotonic U-shape in pph that has two competing readings (D4). Hive type is confounded by sample asymmetry (PostWach 77.3%) and by autocorrelation through `MEMORY.md`, so cross-hive comparisons should be reported as "within-trajectory descriptives" not as moderator effects. Report medians and IQRs; do *not* fit regressions as if sessions were i.i.d. (D5). Cite Champion §3 + Skeptic survival items (a)(b) + Methodologist §3.5.

---

<a id="7-recommended-paper-framing"></a>
## 7. Recommended Paper Framing

The paper should be **one** thing, not a hedge of four positions.

### 7.1 Spine
**Action-research Cycle-1 instrument-validation study with descriptive trajectory analysis** (Staron 2020 framing; Methodologist's primary recommendation). This is the *primary* spine because it is the only frame under which the construct threats (Skeptic) become *contributions* rather than fatal flaws, and under which the role-stacking (Reflexivist) becomes *named methodology* rather than apologetic disclosure.

### 7.2 Title candidates
- "Measurement-Publication Coupling in Single-Operator AI-Swarm Productivity Studies: An Action-Research Cycle 1"
- "What Self-Reports Can and Cannot Tell Us About AI-Swarm-Augmented Research: A 110-Session Action Study"
- "Toward a Calibrated Productivity Instrument for AI-Swarm-Augmented Research: Cycle 1 Findings From a 14-Week Single-Operator Study"

The Reflexivist's coined term **"measurement-publication coupling"** is recommended for the abstract because it names what is novel about this study compared to prior single-operator productivity instruments and makes the role-stacking a contribution rather than a confession.

### 7.3 Contributions (in priority order)
1. **GQM-derived four-dimension productivity scorecard schema** as a research artifact (C7), with documented construct-validity threats and a specific Cycle-2 hardening plan (Methodologist §3.6).
2. **Descriptive trajectory of one researcher's AI-swarm-augmented work over 14 weeks** (C4), reported as a single trajectory through a co-evolving researcher-AI joint state (Reflexivist) — *not* as a population estimate.
3. **The topology × rework × failure-mode correlation** (C3) as the dataset's strongest mechanism-level finding.
4. **A taxonomy of self-report contamination modes specific to agent-coordinated work** (Skeptic's recommended contribution), including the Gemini-CLI case study (`2026-05-04-postwach-04`) as the canonical exhibit.
5. **The conceptual contribution of "measurement-publication coupling"** (Reflexivist) as a frame for future single-operator action studies of AI-augmented work.
6. **A calibrated authoring-equivalent throughput band of 5–12 pg/hr** (C9, Champion's headline) reported *conditionally* on stratified construct counts and explicitly *not* as a productivity multiplier.

### 7.4 What the paper does NOT claim
- It does not claim 41.35 pg/hr / 55× baseline (C1).
- It does not answer RQ2 (cost comparison) (§6 RQ2).
- It does not claim cross-hive moderator effects (§6 RQ3, D5).
- It does not generalize to "AI-swarm productivity in research" — only to "Paul + this stack + this 14-week trajectory" (Skeptic item 12).
- It does not report `first_pass_quality_pct` as a quality construct (D6).

### 7.5 Honest abstract (drafted)
> We report a 14-week longitudinal action study (N=110 sessions, 6 hives) in which one researcher used a self-designed four-dimension scorecard to record AI-swarm-augmented research work. The researcher is also the instrument designer, swarm orchestrator, governance-rule author, and intended analyst, and 1 of 110 sessions was scorecarded by an AI agent rather than by the researcher. The study therefore characterizes a *measurement-publication coupled* trajectory rather than a population effect. We contribute (i) the GQM-derived scorecard schema as a research artifact with documented construct-validity threats, (ii) a descriptive trajectory across artifact types showing a multi-axis March-to-May maturation (median throughput 2.55 → 3.12 pg/hr; agents/session 2.72 → 3.77; utilization 0.904 → 0.977; failure sessions 8 → 2), (iii) a topology × rework × failure-mode correlation in which 8 of 10 failure-mode sessions were star-topology and the 8+ agent bin had the lowest rework ratio (0.064), and (iv) a reflexive analysis of the closed loop between instrument and subject. A calibrated single-operator authoring-equivalent throughput band of 5–12 pg/hr is reported conditional on artifact-type stratification; the unfiltered raw mean of 41.35 pg/hr is shown to be driven by mechanical-conversion outliers and is not defensible as a productivity claim. We propose a Cycle 2 instrument hardening (Pydantic schema enforcement, artifact-stratified output fields, fail-or-skip gate logging, MCP-telemetry-driven cost capture, and an instrumented ground-truth comparator) and pre-register the open empirical question of whether long-session rate collapse reflects workmode discrimination or perception correction.

---

<a id="8-threats-to-validity"></a>
## 8. Threats to Validity (Consolidated)

### 8.1 Internal validity
- **Single-operator confound.** All findings are properties of one researcher-AI joint state; no within-study replication across operators.
- **`MEMORY.md` autocorrelation.** 350-line/43.3 KB project memory accretes across sessions; observations are not i.i.d. (Skeptic, Reflexivist).
- **Date-gap survivorship.** Visible gaps 03-13→03-16, 04-15→04-19, 04-23→04-28 represent silent denominators (Skeptic item 2).
- **Pass-only quality construction.** Survivorship-bias analog on D3 fields (Methodologist, D6).

### 8.2 External validity
- **Single environment.** Windows + OneDrive + ARM64 + Claude Code + claude-flow + a specific MCP stack. Findings about "agent coordination friction" do not generalize beyond this stack (Skeptic item 12).
- **Single domain composition.** 77.3% PostWach; cross-hive claims are not population-supported (Stage 1; Skeptic item 7).
- **Single operator's writing style + research portfolio.** Authoring rate is conditioned on the operator's pre-existing scaffolding (`MEMORY.md`, `docs/capability-index.md`, `docs/project-registry.md`).

### 8.3 Construct validity
- **D1 `pages_produced` collapses heterogeneous artifacts** (`2026-03-07-postwach-05` 950 pp pypdf vs `2026-04-12-postwach-01` 67 pp code-heavy vs ontology triples vs prose) (C8, Methodologist §3.3.1).
- **D2 `agents_spawned` polysemy** (Task subagents vs MCP hive agents vs swarm agents conflated) (Methodologist §3.3.2).
- **D2 `swarm_topology` default-or-unset ambiguity** (61 of 110 = "none"; cannot distinguish "no topology selected" from "topology field not filled").
- **D3 `first_pass_quality_pct`** is circular when the gates are pass-only.
- **D4 `rework_files` schema indiscipline** (int vs list across cards).

### 8.4 Conclusion validity
- **Heavy-tailed distributions on pph** (PostWach mean 47.19, median 2.50). Means are uninterpretable; medians and IQRs are the only legitimate aggregate statistics.
- **N=2 (MACQ) and n=1 (Roadmapping) are not inferentially usable**; report as anecdotal corroboration only.
- **Effect-size vocabulary is not licensed.** No causal claims; no regression-style moderator analysis (D5).

### 8.5 Reflexive validity (the fifth category, per Reflexivist)
- **Role stacking (six roles in one person).** Instrument designer, swarm orchestrator, governance-rule author ([R014] mandates the very data the paper analyzes), study subject, analyst, paper author. Must be enumerated (C2).
- **Measurement-publication coupling.** `perception_note` voice shifts log → story; "Most productive session... to date" appears verbatim implying running narrative ranking (Reflexivist §4).
- **AI-authored measurement event.** `2026-05-04-postwach-04` (Gemini CLI) is existence-proof that the measurement boundary is not species-bounded (Skeptic item 9, Reflexivist §2).
- **Meta-recursion.** This synthesis is the 111th measurement event; the corpus does not include analysis-of-corpus, leaving a hole at the meta-level (Reflexivist §3).
- **Hawthorne + publication.** Subject knows scorecards target publication; biases all metrics toward favorable narratives (Skeptic item 3, Reflexivist §4).

---

<a id="9-next-step-inputs"></a>
## 9. Next-Step Inputs (Cycle 2 — Future Work, Not Current Scope)

The user has scoped a follow-on analysis that incorporates **session archives, rule-change history, and hive-structure evolution**. Each adds answers to questions the current scorecard corpus cannot reach.

### 9.1 Session archives (`docs/session-archives/SESSION_ARCHIVE_*.md`)
**What they add:**
- Narrative-form session reports independent of the per-session YAML scorecard.
- Cross-references (which sessions handed off to which other sessions; which rules were created in which sessions).
- A second measurement channel that can be triangulated against the scorecard channel.

**Questions they answer:**
- Triangulation: where does `perception_note` (scorecard) diverge from session-archive prose? Divergences are direct evidence about the measurement-publication coupling (Reflexivist).
- Survivorship: do undocumented date-gap windows (Skeptic item 2) appear in archives but not scorecards, or vice versa?
- Counterfactual instrumentation: archives may contain better-grounded effort estimates than the scorecard `perception_note`.

### 9.2 Rule-change history (`CLAUDE.md` git history; `MEMORY.md` git history; `~/.claude/CLAUDE.md` history)
**What it adds:**
- A timeline of *governance evolution* (when each rule was added, modified, deleted) that is currently invisible to the scorecard analysis.
- Specifically, when [R014] (the scorecard mandate) was added, when [R016] (artifact integration status) was added, when [R017] / [R106] (MCP discipline) were added — each is a *regime change* that breaks the dataset into pre/post epochs.

**Questions it answers:**
- Did `perception_note` voice shift after [R014] was strengthened? (Reflexivist concern: §4.)
- Did `gates_run` content shift after [R016] was added? (Direct test: the `2026-03-26-postwach-02` card explicitly references "[R016] compliance on three-step assessment" and "[R016] self-check on initial asset inventory: fail" — i.e., rule-change-driven measurement.)
- Did the agent-coordination/timeout blocker rate shift after [R017]/[R106] MCP normalization? (Cross-cuts the W0→W2 trajectory question.)

### 9.3 Hive-structure evolution (`docs/project-registry.md` history; `docs/capability-index.md` history; hive directory creation timestamps)
**What it adds:**
- The dataset claims 6 hives, but the hives were not all live throughout the 14 weeks. Fort Wachs was created 2026-03-10. The Roadmapping hive is n=1. Hive structure is itself a moving target.

**Questions it answers:**
- Does the temporal maturation (C4) coincide with hive-structure stabilization (more hives live + memory accretion)?
- Are the GI-JOE n=13 sessions (Champion's "harder domain corroboration") concentrated in a specific architectural epoch?
- Does the topology × rework correlation (C3) hold within-hive-epoch as well as across the full dataset?

### 9.4 Instrumented ground truth (Skeptic's specific recommendation)
- Commit-graph (per-session `git log` + `git diff --shortstat`) as an automated pages/lines-changed measurement.
- LSP-derived authored-line attribution (which character ranges in committed files were last touched within the session window vs imported from prior sessions vs AI-generated vs human-typed).
- Blind external rater on a 10-session subset for D3 quality.

### 9.5 MCP-telemetry-driven cost capture (Methodologist's specific recommendation)
Hook `mcp__claude-flow__system_metrics`, `mcp__claude-flow__performance_metrics`, and the model-route hooks into automatic per-session cost extraction so D2 cost fields stop being 99.1% empty.

### 9.6 Multi-operator extension (the only path to RQ2 and out of single-operator confound)
The current dataset is structurally single-operator. Cycle 2 cannot answer RQ2 without recruiting at least one independent operator running a comparable scorecard. This is the largest external-validity gap and the most expensive Cycle-2 input.

---

<a id="10-operational-recommendations"></a>
## 10. Operational Recommendations

Concrete actions for the researcher between now and CSER 2027 / ESEM 2027 / EMSE submission.

### 10.1 Schema discipline (do before next session)
1. **Pydantic enforcement at scorecard creation time.** Block save on schema violations. Implement via the `auto-memory` hook so the [R014] write-event is gated.
2. **Stratify D1 output fields.** Replace single `pages_produced` with: `prose_words`, `ontology_triples`, `code_loc`, `config_loc`, `slide_count`, `figure_count`, `pdf_pages_authored`, `pdf_pages_mechanical`. Keep `pages_produced` as a derived/legacy field with deprecation note.
3. **Disambiguate D2 agent counts.** Replace `agents_spawned` with `task_subagents`, `mcp_hive_agents`, `swarm_agents` as separate fields; require `swarm_topology` to be one of `{none, star, hierarchical, mesh, hybrid, hierarchical-mesh, NOT_RECORDED}`.
4. **Ban pass-only quality construction.** D3 must include `gates_failed_or_skipped` with explicit reasons.
5. **Normalize `rework_files`** to always be a list (length-zero allowed).
6. **Add `instrument_author_identity`** field defaulting to operator name; allow the value to be an AI agent identifier with explicit `agent_authored: true` flag (per Gemini-CLI episode).

### 10.2 Analysis-script hardening
1. Drop the four parse-failed scorecards from the headline computation but report them in Appendix A.
2. Replace mean-pph with median-pph as the primary aggregate; report IQR instead of stdev.
3. Compute trajectory-aware statistics (rolling medians; change-point detection on the multi-axis maturation trajectory).
4. Stratify all aggregates by `swarm_topology` and `agents_spawned` bin (already partially done; make standard output).
5. Build a "headline-table" generator that explicitly separates **mechanical-conversion outliers**, **0-page sessions**, and **substantive-research sessions** (per Appendix B) before computing any rate.

### 10.3 Action-research cadence
1. Frame the current 14-week corpus as **Cycle 1: diagnose-act-evaluate**.
2. Pre-register the Cycle 2 study design before next session: stratified outputs, instrumented ground truth on a subset, fail-or-skip gates, MCP cost capture.
3. Plan Cycle 3 as the multi-operator extension that unlocks RQ2.

### 10.4 Reflexive discipline
1. Add a §7 to the manuscript draft *now* enumerating the six stacked roles; do not defer to revision.
2. Include the Gemini-CLI scorecard (`2026-05-04-postwach-04`) as a §7 case study, not as a footnote.
3. Treat this synthesis (the 111th measurement event) as a meta-level scorecard and either include it in the corpus or explicitly exclude it with rationale.
4. Audit `perception_note` text across the corpus for recurring framing phrases ("Most productive session... to date", "dramatically faster", "highly productive") and report the count as a finding about the measurement loop.

### 10.5 Threats-to-validity discipline
Add a fifth category — **Reflexive validity** — to the manuscript's threats-to-validity section, populated from §8.5 above. This is the Reflexivist's structural contribution and should not be hidden inside Internal validity.

### 10.6 R016 tagging in the manuscript
Following [R016], tag every contribution: scorecard schema is **(a) → (b)** (research artifact graduating to demonstrated capability under the Cycle-2 hardening); the trajectory descriptive is **(b) demonstrated capability** (works for one operator); the topology × rework correlation is **(b)** with a Cycle-3 path to **(c) integrated deliverable** if multi-operator replication holds.

---

<a id="appendix-a-data-quality-issues"></a>
## Appendix A: Data Quality Issues

### A.1 YAML parse failures (4 cards excluded from headline computation)
Per Stage 1 brief, 4 cards failed YAML parsing. **Two of those four are top-decile sessions per the counterexample-hunter** — meaning headline computations on the 110 valid cards are not just trimmed but biased toward the survivable middle. Specific filenames must be enumerated in the Cycle-2 audit.

### A.2 String-in-numeric violations (15 cards per Stage 1)
Examples include `lines: ~950`, `lines: ~3200`, `total_files_created: ~65`, `total_lines_written: ~10000` (`2026-04-12-postwach-01`). The tilde-prefix string in a numeric field is a Pydantic-blockable violation; under the current loose YAML parsing it produces silent type coercion or NaN substitution depending on analyzer version.

### A.3 Schema indiscipline
- `rework_files`: sometimes `int` (e.g., `rework_files: 2` in `2026-03-26-postwach-02`), sometimes `list` (e.g., `rework_files: []` in `2026-05-04-postwach-04`), sometimes `int` representing list length (e.g., `rework_files: 3` in `2026-04-12-postwach-01` while the prose describes 3 specific files).
- `start_time` / `end_time`: sometimes `"08:00"`, sometimes `"~09:00"`, sometimes empty string with a `wall_clock_hours_override` workaround (e.g., `2026-03-03-postwach-01`).
- `swarm_topology`: 61 of 110 = `"none"`; the field cannot distinguish "no topology selected" from "no swarm spawned at all" from "field not filled".

### A.4 Researcher-field anomaly
1 of 110 cards has `researcher: Gemini CLI` (`2026-05-04-postwach-04`). Not a typo; the card was produced by the Gemini CLI agent during a session in which it diagnosed and fixed the broken `claude` and `claude-flow` environment.

### A.5 Cost field missingness
99.1% (109 of 110) of cards have empty `total_cost_usd`. RQ2 is empirically unsupportable from this dataset (C6, §6 RQ2).

---

<a id="appendix-b-outliers"></a>
## Appendix B: Outliers Worth Excluding from Headline Computations

Headline computations (median pph, calibrated authoring-equivalent rate band) should explicitly partition the corpus into mechanical-conversion, 0-page, ultra-short, and substantive-research subsets. Each is excluded from the headline rate for a different reason; each must still appear in the threats-to-validity discussion.

### B.1 Mechanical-conversion sessions (exclude from authoring-rate; keep in trajectory and process)
| Session ID | pph (raw) | Reason |
|------------|-----------|--------|
| `2026-03-07-postwach-05` | very high (950 pp / 0.42 hr) | `pypdf` extraction of Zeigler TMS2018; `agent_failures: 7` (all agents blocked by content filter); pivot to programmatic conversion. Pages-produced is a `pypdf` artifact. |
| Counterexample-hunter top outlier (2280 pg/hr) | 2280 | Mechanical conversion / git-add of pre-existing material. Not authoring. |
| Counterexample-hunter (109 pg/hr) | 109 | Same class. |

### B.2 Zero-page sessions (exclude from rate; keep in process and quality)
- `2026-05-04-postwach-04` (Gemini CLI): `pages_produced: 0`; environment-fix session. Belongs in process-health and reflexive-validity discussion, not in authoring-rate computation.
- Stage 1 noted additional 0-page sessions; full enumeration belongs in Cycle 2 audit.

### B.3 Ultra-short sessions (<1 hour)
Stage 1: `<1hr=156 mean (artifact)`. Sub-hour sessions inflate `pages_produced/hour` because denominators are tiny and rounding errors dominate. Bin separately; do not aggregate with multi-hour sessions.

### B.4 Long substantive-research sessions (keep in authoring-rate floor; flag as workmode-discrimination vs perception-correction tension D4)
Long sessions (6–10 hr fatigue zone, 10+ hr deep-work) collapse to 0.57–2.5 pg/hr. Champion calls this workmode discrimination; Skeptic calls it METR-style perception correction. These sessions *must* be in the rate computation because they bound the band C9 from below; the open question (D4) is what the bound *means*.

### B.5 Code-heavy "pages" (stratify, don't exclude)
- `2026-04-12-postwach-01` (67 pp): Practitioner Guide v8 PDF *was* genuinely authored, but the same scorecard also reports ~10000 LOC of Streamlit + lib/ + tests + ontology + Docker/CI which are *not* pages. Under the current schema, both flow into the same `total_lines_written` and only the Practitioner Guide flows into `pages_produced`, but the heuristic is fragile and operator-dependent. Stratification (per §10.1.2) is the fix.

### B.6 Subject-generated counterfactuals (flag as Hawthorne/publication-coupling evidence, do not use as baseline)
- `2026-03-03-postwach-01`: "Estimated 4-6 hours manual equivalent compressed to ~1.5 hours."
- `2026-03-07-gi-joe-02`: "2-3 person-weeks of experienced ontology engineer + domain expert."
- `2026-03-09-gi-joe-01`: "6-12 person-weeks."
These are subject-generated speedup ratios with no instrumented baseline. Skeptic item 1. Use as content for the §7 measurement-publication-coupling case study, not as RQ2 evidence.

---

## Synthesis Closing Note (Aufhebung)

Hegelian sublation: *aufheben* simultaneously cancels, preserves, and elevates. Applied here:

- **Cancelled:** the 41.35 pg/hr / 55× academic-baseline headline (C1); RQ2 cost-comparison as currently scoped (C6); pass-only `first_pass_quality_pct` as a quality construct (D6); cross-hive moderator claims (D5); the framing of the Gemini-CLI scorecard as a curio (D3).

- **Preserved:** the calibrated 5–12 pg/hr authoring-equivalent band, conditional on stratification (C9); the topology × rework × failure correlation (C3); the multi-axis maturation trajectory (C4); the GQM-derived scorecard schema (C7); the Windows/OneDrive/ARM64 environmental friction finding (C5).

- **Elevated:** the recognition that this is not 110 i.i.d. observations but one trajectory through a co-evolving researcher-AI joint state (Reflexivist's *measurement-publication coupling*), which transforms the role-stacking from confession to methodology, the Gemini-CLI scorecard from curio to canonical exhibit, and the pass-only construction from quality-validity threat to evidence about the measurement loop itself.

The contradiction between the four positions was not split-the-difference averaging. The Methodologist's action-research framing supplies the spine under which the Champion's rate, the Skeptic's measurement contributions, and the Reflexivist's coupling concept become *non-rivalrous sub-contributions* — each preserved at its strongest, none averaged into a hedge.

---

*End of synthesis. Saved to: `Papers/AI_Swarm_Productivity/analyses/2026-05-05_swarm_debate.md`.*
