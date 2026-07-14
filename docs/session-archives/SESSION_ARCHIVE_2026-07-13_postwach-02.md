# Session Archive — 2026-07-13 postwach-02

> PROVENANCE: claude-opus-4-8[1m] (Anthropic, Claude Code CLI). Long continuous session on the WySE-Theory
> **decision-layer** research program (distinct from the concurrent 2026-07-13 postwach-01 RTSync SBIR
> session). Heavy multi-model orchestration via the Workflow tool and background Agents: Fable 5 for
> derivations, Codex (red) / Opus (white) / Sonnet (blue/apply) / Haiku (relays) for adversarial review,
> after a mid-session token-optimization shift. Repo: DocWach/WySE-Theory (local folder "Fable 5 planning"),
> committed + pushed throughout. Skills: wyse-model-generation (CREATED + exercised), reflookup, refverify,
> morphism-research-methodology, morphism-domain-reference.

**Hive:** PostWach (CTO / Chief Scientist). **Researcher:** Paul Wach. **Model:** Opus 4.8 [1m] main loop
(+ Fable 5 derivations; Sonnet/Haiku bulk; Codex red legs on ChatGPT sub, off the Claude weekly limit).
**Status:** CLOSED (major milestones; decision-layer thread substantially advanced; 3 of 7 candidates
hardened; adversarial iteration paused at a natural point).

**Headline:** Built and exercised the `wyse-model-generation` skill, then grounded and formally derived the
WySE **decision layer** — T3SD figures of merit + Kannan acceptability + Set-Based Design — as seven
witness-verified Fable candidates, identified and reorganized the WySE-Theory repo, and put the candidates
through **five rounds of RBW adversarial hardening**. The load-bearing finding: across all five rounds the
**mathematics never broke (zero refutations)** — every defect was *claim over-statement*, and the
**cross-vendor red leg proved essential** (it downgraded two prematurely-CLOSED candidates and caught
false-universals that a same-vendor 15,504-case machine scan had ratified).

## 1. wyse-model-generation skill (CREATE + exercise)
- CREATED `.claude/skills/wyse-model-generation/SKILL.md` (R020 CREATE): Phase-1 grounded generation via
  **propose → validate → measure**; a generated model is an R016 (a) hunch until a witness measures it.
- Exercised on the **DC-motor** (LA, linear; poles + steady state vs external ground truth) and the
  **nonlinear pendulum** (LA; elliptic-integral period vs small-angle — teeth against a linearization
  shortcut). Both witness-validated (SHA-stable), SME-adjudicated. Skill §8 updated each use.

## 2. Decision-layer research — the core
- **Grounding:** T3SD figures of merit / Wymore standard scoring functions (12 shapes from one SSF1
  generator + combining functions; source `04 Resource Library/Wymore/QuantitativeMethods.pdf` = Daniels-
  Werner-Bahill 2001; extraction log written). Kannan acceptability. **Set-Based Design** external lit
  review (Ward 1989 MIT thesis → 1995 "Second Toyota Paradox" → 1999 SBCE principles; the reviews find the
  *formal narrowing-under-uncertainty* treatment an open frontier — verified against Toche 2020 / Dullen 2021).
- **Seven Fable candidates** (all witness-verified, R016 (a)): **A** FoM-scalar vs Kannan-poset trichotomy;
  **B** confidence-weighted acceptability order; **C** SSF acceptance-region / down-set on the (D_s,D_b) plane;
  **D** shared-carrier coupling (closes the C9 fence); **E** Cody transfer-distance vs D_s (refuted-then-
  reframed: transfer distance is behavioral); **F17** set-based narrowing (integrate-by-intersection = the
  poset meet; CE-F17 negative: bound-tightening alone doesn't narrow); **F2** combiner classification
  (all-threshold veto = exactly annihilation; veto-preserving class = {product, weighted product, min,
  geometric mean}; product NOT forced — discharges C's PO-C3, corrects C's framing).
- **Plain-witness reproductions** confirmed we can implement T3SD (FoM = 0.605 exact) and Kannan (Def-2
  acceptability + monotonicity), off-Fable.
- **References:** promoted **11 Set-Based-Design refs** into approved.bib (8 DOI-verified via `refverify`,
  which CAUGHT two phantom-author / wrong-DOI errors the lit-review agent had asserted; 3 no-DOI magazines/
  thesis attested by paulwach@arizona.edu). approved.bib 361 → 373. Plus daniels2001quantitative,
  smith2007ameliorating earlier.

## 3. WySE-Theory repo (identified, un-staled, reorganized)
- Identified: the local folder **"Fable 5 planning" IS `github.com/DocWach/WySE-Theory`** (the "3-days-stale"
  GitHub state was 20 unpushed local commits) — resolved by pushing. README identity note added.
- **Reorganized by-topic**: 264 `git mv` renames (history preserved) into `docs/{planning,framework,
  positioning,session-notes,procedures,paper-ideas,fable-prompts,one-pager}`, `derivations/<topic>/` (29
  topics; this week's work under `decision-layer/`), `library/`, `logs/`.

## 4. RBW adversarial hardening (5 rounds) — the discipline story
- v1 RBW → all 6 REWORK. v2 rework → C, F17 CLOSED (2-leg, Codex timed out). v3 → **live Codex red
  DOWNGRADED C & F17** (found C's Kannan-weld overstatement + a cross-candidate inconsistency, F17's
  overclaim in a governance file), **E CLOSED**. v4 claim-calibration (global-sweep + uniform scoping) →
  **D CLOSED**; Codex caught **B's two false-universals a 15,504-case same-vendor scan had ratified**. v5
  systematic universal-hedging (check |X|≥4) → **B CLOSED**.
- **Genuinely CLOSED-HARDENED: E, D, B** (B owes a live cross-vendor red — Codex timed out its round).
  **REWORK:** A (one wording item: margin (3/8)(w1+w2) = 3/8 only on the normalized simplex), C (residual
  line items + adopt F2), F17 (finish the "formal foundation" sweep + 3 items).
- **KEY METHODOLOGY FINDINGS:** (1) never mark CLOSED without a **live cross-vendor red** — proven twice;
  (2) across 5 rounds the **math never broke (zero refutations)** — the entire failure surface is claim
  calibration (overclaims, universal quantifiers wider than the proof, summary-surface drift); (3)
  **token discipline** — apply→Sonnet, red→Codex (off Claude limit), Haiku relays, Opus for adjudication
  only; per-candidate line-fixing hits whack-a-mole, global-sweep + universal-hedging converges.

## 5. Tooling / ops
- **Gemini blue leg down:** `gemini` CLI 429 = API-key quota exhausted; the "new CLI" is **`agy`
  (Antigravity) v1.0.10** — installed with a headless `-p` mode + subscription auth (sidesteps the 429) but
  NOT signed in (models empty) → sign in interactively OR clear the API quota to restore a true 3rd vendor.
- **Killed a 3-day orphaned `codex` domain-critic shell** (PID 21236, hung since 7/10) — the "1 shell still
  running" indicator. Several stale `@claude-flow` MCP-server node processes noted for manual reaping.

## 6. Open / next
- Rework residuals (all prose/claim-calibration, no math): A PO-REWORK-14; C RW-C4 line items + fold in F2;
  F17 V4-R1 sweep + 3 items. **B, C, F17 owe a live cross-vendor red** (Codex-timeout-dependent).
- **refverify debt (R019, before ANY render):** Gordan 1873 (load-bearing for A), Fishburn, Keeney-Raiffa,
  Farkas/Motzkin, Szpilrajn, Arrow/Sen, McGarvey, Barthelemy-Monjardet, Moulin, Villani, Ben-David, Mansour,
  Davey-Priestley, Birkhoff, Klement-Mesiar-Pap, Grabisch, Baez-Courser, sun2026, micouin.
- Restore agy/Gemini for a true 3-vendor final confirm on E/D/B (and the eventually-closed A/C/F17).
- Deeper open Fable targets (scoped, not run): F1 (PO-A1 Farkas boundary), PO-F17-3 (is the single-gate class
  intersection-closed? non-closure ⇒ set-carrying is FORCED — the profound SBD question).

## 7. Commits (DocWach/WySE-Theory, all pushed)
Model-gen + A-E + backlog (b2d086c); E (4f45aff); reproductions (a0cde2d); reorg (0d5d518 + 2328274);
README identity (b77b2fb); F17 (6d23dd6); RBW v1 (1b81198); rework v2 (c5700fa); v3 (65a03f4); backlog fix
(c7f153c); v4 (65695df); scope doc (5493671); F2 (956e1f6); v5 (8812a70). Memory `research_decision_analysis_confidence_thread.md`
updated throughout.
