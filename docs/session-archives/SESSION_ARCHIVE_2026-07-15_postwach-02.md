# Session Archive — 2026-07-15 postwach-02

**Hive:** PostWach (CTO / Chief Scientist)
**Topic:** Data-fusion Fable EXECUTION wave (F18 + F20 + F19) — derivation, witness verification, cross-vendor RBW
**PROVENANCE:** Opus 4.8 (claude-opus-4-8[1m]) orchestrated; derivations by Fable 5 (claude-fable-5); RBW red by
Codex (gpt-5.5, OpenAI, live cross-vendor); blue by Sonnet 4.6; white by Opus 4.8. Anthropic + OpenAI, Claude
Code CLI, principal-directed.
**Status:** CLOSED. The distinct execution session reserved by postwach-01 (same day). Autonomous to completion
per principal directive ("set up a workflow and execute to completion; do not wait on me").

## Charge

Execute the data-fusion Tier-1 Fable wave documented by postwach-01: derive F18 + F20 + F19, verify witnesses,
harden via cross-vendor RBW. Mid-session the principal directed a Workflow run to completion without checkpoints.

## What happened

Warmed ruflo (v3.29.0); re-grounded on the launch package (synthesis plan, backlog F18-F25, pending refs) and
the existing Fable candidate/witness/RBW file conventions in `derivations/decision-layer/`.

1. **Derivation (3 Fable-5 background agents).** F18 (order-theorist lens), F20 (real-analyst), F19
   (probabilist). Each produced `Fable_F<ID>_*_candidate.md` + `_witness.py` and self-verified.
   - **All three witnesses PASSED and were INDEPENDENTLY RE-RUN by PostWach** (exit 0, SHAs reproduced
     byte-identically): F18 `286ad384`, F20 `6d1d2ccf`, F19 `d49d751c`.
   - F20's witness CORRECTED the tasking: the squared-distance decoy is convex, so it does NOT violate the
     bound; the genuine non-convex-but-metric decoy sqrt(L1) violates. Failure axis = CONVEXITY, not metricity.
     (measure-not-assume working; the witness had real teeth.)

2. **RBW hardening (Workflow `rbw-datafusion-hardening`, 9 agents, ~649k subagent tokens).** Pipeline per
   candidate: Codex red (LIVE cross-vendor, gpt-5.5) -> Sonnet blue -> Opus white; adjudicator barred
   CLOSED-HARDENED without a live Codex red. **codexLive = true for all three.**
   - **Verdicts: F18 REWORK, F20 REWORK, F19 REWORK.** None refuted, none closed. Every core theorem survived
     and every witness reproduced; all surviving defects are claim-calibration + prior-art, repairable in
     prose/scope (BLUE drafted the fixes).
   - Codex prior-art catches: F18 = Dushnik-Miller order dimension (1941), closer than Szpilrajn, plus an
     illusory `preserved_incomparability` teeth (tautologically unreachable over Q); F20 = the bound is finite
     Jensen (1906) + a 0*inf well-formedness gap; F19 = "is EXACTLY a credal set" is a category error (an order
     is representable-by, not identical-to, a credal set) + two false prose claims (D3 E-admissibility, §4
     sub-polytope) + T4 needs its Omega-growth hypothesis stated + exactness witnessed on 1 dim-2 instance only.

## Key result

**F19 dissolves the totalize-vs-poset tension on the merits.** T4 ({credal-dominance orders} = {finite posets},
constructive) is TRUE; T3 (singleton credal set = the |M|=1 totalizing endpoint) is correct; the credal set is
confirmed as the carrier for "a distribution over the poset that refuses to collapse incomparable
alternatives." F19 fills the F3 slot. Remaining work is v2 calibration + refverify, not new mathematics.

## Decisions / status

- F18, F20, F19 = candidate (a), witness-verified + PostWach-reproduced; RBW = 3x REWORK (characterized
  results, first-class). None promoted to adopted/(b).
- Reference debt stands: walley1991 staged-not-approved; Troffaes 2007, Dushnik-Miller 1941, Szpilrajn 1930,
  Stanley 1986 pending. No manuscript rendered; R019 not triggered.

## Artifacts produced (in `Fable 5 planning/derivations/decision-layer/`)

- `Fable_F18_logop_kannan_noncollapse_{candidate.md,witness.py}`
- `Fable_F20_db_convexity_mixtures_{candidate.md,witness.py}`
- `Fable_F19_credal_set_poset_{candidate.md,witness.py}`
- `RBW_F18_2026-07-15.md`, `RBW_F20_2026-07-15.md`, `RBW_F19_2026-07-15.md`
- Backlog `Fable_Run_Backlog_2026-07-13.md` (RUN OUTCOME note in the data-fusion wave)
- Memory: `research_data_fusion_fable_family.md`, `research_decision_analysis_confidence_thread.md`, `MEMORY.md`

## Open items / next

- **v2 calibration pass** on all three (all prose/scope; BLUE's fixes drafted in the RBW files): F18 re-scope
  LogOP framing + strike illusory teeth + add Dushnik-Miller; F20 move the bound to cedes as finite-Jensen +
  fix 0*inf + scope the witness; F19 retitle off the identity overclaim + state T4 Omega-hypothesis + fix D3/§4
  + honest witness-scope. Then a live cross-vendor re-adjudication for CLOSED-HARDENED.
- **refverify** the pending/placeholder refs before any (b)/manuscript.
- F19's PO-F19-3 (grading layer over incomparabilities) is the Axis-B open object.

## Session hygiene

12 subagents total (3 Fable derivation + 9 RBW workflow), ALL completed; none orphaned. No claude-flow swarm /
hive-mind. Live Codex red succeeded on all three (contrast prior rounds' Gemini-down substitutions). No commits.

## UPDATE — continued to completion (v2 + v3): 3x CLOSED-HARDENED

The session did not end at REWORK; per the principal directive to execute to completion, two further rounds ran:
- **RBW v2** (Workflow, Sonnet apply / live Codex red / Opus white, 9 agents, ~719k tok): still 3x REWORK.
  Overclaims fixed, but the apply edits introduced minor internal-consistency defects (lemma renumbering broke
  cross-refs; incomplete sweeps missed the WITNESS DOCSTRINGS) plus one substantive F19 error (a false
  "minimum-realizer complexity is open" claim; order dimension is NP-complete for k>=3, Yannakakis 1982).
- **RBW v3** (Workflow, Opus apply of the exact fixes incl. witness-docstring sweeps + the Yannakakis correction /
  live Codex red / Opus white, 9 agents, ~704k tok): **F18 / F20 / F19 = CLOSED-HARDENED.** codexLive true on all;
  witness SHAs stable. A residual cosmetic "total order"->"total preorder" on F19 (missed by the v3 sweep) was
  closed BY HAND (3 SHA-preserving edits) and PostWach re-reproduced d49d751c.

**Final status: F18, F20, F19 all CLOSED-HARDENED; (a) eligible for (b) pending refverify** of the placeholders
(walley1991 staged; yannakakis1982 NEW; Szpilrajn 1930, Dushnik-Miller 1941, Stanley 1986, Troffaes 2007, Berger).
F19 is the credal-set carrier that HARDENS the totalize-vs-poset tension-closer. Reviews:
`RBW_F{18,20,19}_{v2,v3}_2026-07-15.md`.

**Loop discipline:** stopped at v3 (the committed bound). The v1->v2->v3 arc matched the known decision-layer
pattern (math sound throughout; whack-a-mole on prose); switching the v3 apply from Sonnet to Opus + exact edit
lists + explicit witness-docstring sweeps is what closed it. Wave cost ~2.37M subagent tokens across 3 workflows
(30 subagents, all completed, none orphaned); live Codex red on all three rounds.

## Scorecard

`Papers/AI_Swarm_Productivity/data/scorecards/2026-07-15-postwach-02.yaml`.
