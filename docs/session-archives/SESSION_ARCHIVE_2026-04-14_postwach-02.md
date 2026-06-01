# Session Archive: 2026-04-14 PostWach-02

**Hive:** PostWach
**Project:** AI Circuit Breaker — SERC AI4SE/SE4AI 2026 workshop abstract
**Date:** 2026-04-14
**Duration:** ~3 hours
**Focus:** Draft workshop abstract for AI Circuit Breaker; run parallel red/blue/white + lit-review; debate testbed options

---

## Session Summary

Warmed ruflo (v3.5.7) and inventoried the AI Circuit Breaker project. Recorded the decision not to pursue DARPA CLARA. Pivoted the session to the SERC AI4SE/SE4AI 2026 workshop abstract (SE4AI track, 3-page paper presentation, deadline June 5 2026). Reviewed CFP and two 2025 SERC AI workshop abstracts (GenGroves, STcP) for structural template. Confirmed authors (Wach + Wallk) and working-location policy.

Drafted abstract v0.1 mirroring the STcP structure, then integrated CSER 2026 isomorphism-library content (isomorphic-degradation framework, correct Sandmann co-authorship, exact-surjective scope limitation) for v0.2. User challenged the opening "SE cannot currently measure" claim; agreed to run a comprehensive red/blue/white review plus a scoping lit review across specified SE venues.

Extracted a 40-claim ledger from v0.2, then launched three background agents in parallel:
- **Red team** (skeptical-challenger) attacked claims, flagging C31/C32 (GUM/AI novelty) as **Fatal** due to prior Martin 2024 *Measurement* and Nanomanufacturing & Metrology 2025; C15 composition-theorem bound is wrong in general; C34/C40 conflate CISA ZTMM with DoD ZT RA.
- **Blue team** (literature-reviewer) verified NIST AI RMF 1.0, ISO/IEC 42001:2023, EU Reg 2024/1689, Wymore 1993, JCGM 100:2008, Montgomery SQC, Page 1954 CUSUM, Wagner PTB-XL 2020, Moody & Mark 2001, 2023 ACC/AHA AF Guideline, Wach/Zeigler/Salado 2021, NSA CSI May 2024 (Visibility and Analytics Pillar).
- **Lit-review** scoping across Wiley SE journal, INSIGHT, INCOSE IS, IEEE OJSE, NPS ARS, NDIA, CSER, SERC AI4SE. Fifty-entry inventory, concept-map matrix, 10-author community inventory, ranked 15 citations for the abstract + ~32 extensions for the journal paper. **Key finding:** SPC column is empty across all eight SE venues — strongest defensibility argument. Morphism column has only Wach-lineage work; none applied to AI trust.

Wrote `white_synthesis_v0.1.md` adjudicating the 40 claims and produced abstract v0.3 with the following corrections: narrowed C1 opening to acknowledge prior work; hedged C31/C32 novelty with "to our knowledge" and Martin 2024 adjacent citation; stated composition theorem as proposition with explicit 1-Lipschitz assumption; replaced ZT Pillar 7 language with NSA CSI May 2024 "Visibility and Analytics capability"; PTB-XL count corrected to 21,837 records only; MIT-BIH to ~110,000 reference annotations; added Hannun 2019 *Nature Medicine* external ECG anchor; added McDermott 2020, Freeman 2020, Zeller 2023, Schierman 2020 nearest-neighbor citations. References grew 10 → 23.

User flagged the CBTO claims as R016 violation: CBTO is fully specified inline in the v4 design spec (Appendix E, lines 1101-1902) with confirmed counts (25 classes, 20 object properties, 12 data properties, 6 SHACL shapes, 10 SPARQL queries) but has no `.ttl`/`.owl` file, no triple-store instantiation, no pyshacl/SPARQL engine validation. Status: research artifact (a), not demonstrated (b) or integrated (c). Corrective language not yet applied; deferred to v0.4.

User requested a CPS security testbed alternative to ECG to match SERC/DoD audience. Debated SWaT, EPIC, TEP, ORNL Power System Attack Dataset. Recommended SWaT as primary with ORNL secondary and TEP as UQ calibration bench. User flagged SWaT licensing concern; verification confirmed iTrust requires a Google Form access request (not a legal DUA, ~3 business days, free, no redistribution). Extended debate on how each dataset would actually be used and what distinctive outcome each enables:
- SWaT → 6-link morphism chain (composition-theorem validation)
- EPIC → cyclic-load allostatic regulation (bio-inspired Pillar 3)
- TEP → Type A + Type B uncertainty budget validation against ground truth
- ORNL → SPC common-cause/special-cause dichotomy is the native statistical formulation

User observed the layered framing is really a long-term research program, not a single-abstract scope. Recommended moving the four-dataset testbed strategy into a planning document. User then asked the meta-question: should the abstract reference a dataset at all? Debated Option A (no dataset), B (domain-level only), C (one illustrative). Recommended Option B: replace Phase I/II/III dataset-specific prose with domain-level language ("transmission-line protection," "multi-stage process control"), move the layered plan to `Papers/AI_Circuit_Breaker/planning/testbed_strategy.md`, recover ~400 words of abstract budget for deeper framework contribution prose. User agreed conceptually; v0.4 and planning document creation deferred to next session.

## Key Decisions

- **D1.** Not pursuing DARPA CLARA. Artifacts in `proposals/01_darpa_clara/` retained as reference.
- **D2.** SERC AI4SE/SE4AI 2026 is the current outreach priority for the AI Circuit Breaker line. Submission type: 3-page paper presentation. Track: SE4AI.
- **D3.** Jeffrey Wallk (VEG Managing Partner) stays as co-author through the CPS pivot.
- **D4.** Canonical outreach folder is `Documents\02 My Outreach\`, not `Documents\03 Projects\02 My Outreach\`. Folder consolidation deferred to inter-hive policy session. Logged in `memory/project_outreach_folder_canonical.md`.
- **D5.** CSER 2026 paper authors are **Wach, Sandmann, Iyer** (not Salado). Reference corrected in v0.2 and carried forward.
- **D6.** Abstract opening narrowed from "SE cannot currently measure" to "SE is being asked to underwrite AI systems with less metrological rigor than it applies to other safety-critical subsystems." Prior-art acknowledged: NIST AI RMF, ISO/IEC 42001, EU AI Act, AMLAS, runtime assurance, Abdar 2021 UQ survey.
- **D7.** SPC-for-AI-trust in SE venues is the single strongest novelty claim. Grounded in the lit-review scoping finding (empty SPC column across all eight venues reviewed).
- **D8.** Composition theorem stated as a proposition we establish; 1-Lipschitz assumption explicit; Lipschitz-weighted multiplicative bound acknowledged for the general case.
- **D9.** NSA CSI *Advancing Zero Trust Maturity Throughout the Visibility and Analytics Pillar* (May 2024) replaces the prior composite "NSA/CISA Zero Trust Maturity Model Pillar 7" citation. "Pillar 7" phrasing dropped because it conflates CISA ZTMM (5 pillars + 3 cross-cutting) with DoD ZT RA (7 pillars).
- **D10.** CBTO is currently R016 status (a) research artifact: specified in v4 design spec, not built. Abstract language must acknowledge this. Decision on Option A (soften counts) vs Option B (drop counts) deferred to v0.4.
- **D11.** Pivot from ECG-only testbed to CPS-security-primary testbed framing. SERC/DoD audience resonance is the driver.
- **D12.** Four candidate CPS testbeds evaluated: SWaT (primary if iTrust form is acceptable), ORNL Power System Attack (primary if form is a blocker), TEP (simulator-based UQ calibration bench), EPIC (Phase II cyclic-load allostatic story). Full matrix in next-session planning document.
- **D13.** Layered testbed strategy is a long-term research program artifact, not a single-abstract item. Moving to `Papers/AI_Circuit_Breaker/planning/testbed_strategy.md`.
- **D14.** Abstract direction for v0.4: Option B, domain-level language only, no dataset names. Recovers ~400 words of budget. Execution deferred to next session.

## Open Items for Next Session

1. Create `Papers/AI_Circuit_Breaker/planning/testbed_strategy.md` with the four-dataset layered plan, distinction matrix, and access-status details.
2. Write abstract v0.4: apply R016 CBTO correction (Option A: soften counts), apply D14 (dataset-free Phase I/II/III prose), carry over all D1-D13 decisions.
3. Verify CBTO counts against the live spec Appendix E (they matched on this pass: 25 classes, 20 object properties, 12 data properties, 6 SHACL shapes, 10 SPARQL queries).
4. Obtain Jeffrey's bio links and VEG affiliation string for the author-bio section.
5. Obtain Paul's Google Scholar / ResearchGate / LinkedIn URLs (currently `[PLACEHOLDER]`).
6. Decide whether to file the iTrust SWaT access form now (3-day SLA) or defer.
7. Lit-review next actions (from `lit_review_scoping_v0.1.md` §8): UA library Wiley verification pass; CSER 2023/2024 Springer chapter enumeration; NPS ARP archive pass.

## Files Created / Modified

### Abstract drafts (created)
- `02 My Outreach/2026_SERC_AI4SE_SE4AI/Wach_Wallk_AICircuitBreaker_Abstract_v0.1.md` + `.pdf`
- `02 My Outreach/2026_SERC_AI4SE_SE4AI/Wach_Wallk_AICircuitBreaker_Abstract_v0.2.md` + `.pdf`
- `02 My Outreach/2026_SERC_AI4SE_SE4AI/Wach_Wallk_AICircuitBreaker_Abstract_v0.3.md` + `.pdf`

### Review artifacts (created)
- `Papers/AI_Circuit_Breaker/reviews/claim_ledger_v0.2.md` (40 claims)
- `Papers/AI_Circuit_Breaker/reviews/red_team_v0.2.md` (agent-produced)
- `Papers/AI_Circuit_Breaker/reviews/blue_team_v0.2.md` (agent-produced)
- `Papers/AI_Circuit_Breaker/reviews/lit_review_scoping_v0.1.md` (agent-produced)
- `Papers/AI_Circuit_Breaker/reviews/white_synthesis_v0.1.md`

### Memory notes (created)
- `memory/project_ai_circuit_breaker_clara_declined.md`
- `memory/project_ai_circuit_breaker_collaborator.md`
- `memory/project_outreach_folder_canonical.md`

### MEMORY.md (modified)
- Added pointers for three new memory notes above.

## Agents Used

- 3 background parallel agents: skeptical-challenger (Red team), literature-reviewer x2 (Blue team, Lit scoping). All converged on overlapping fix list for claims C1, C15, C22, C31/C32, C34/C40.
- 1 foreground verification agent: general-purpose (SWaT/WADI/EPIC/BATADAL access terms).
- Total tool uses across agents: ~103.

## Session State at Termination

- v0.3 abstract + PDF is the current working artifact.
- v0.4 direction agreed (dataset-free, R016 CBTO correction) but not executed.
- No active background agents.
- No uncommitted external actions (no git commits, no pushes, no external submissions).

## Productivity Scorecard

See `Papers/AI_Swarm_Productivity/data/scorecards/2026-04-14-postwach-02.yaml`.
