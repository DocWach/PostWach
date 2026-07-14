# Session Archive — 2026-07-14 postwach-02

> PROVENANCE: claude-opus-4-8[1m] (Anthropic, Claude Code CLI). WySE-Theory decision-layer thread,
> continued. Heavy multi-model orchestration: Codex (OpenAI gpt-5.5) + Gemini 3.1 Pro (via `agy`/
> Antigravity) as adversarial red/blue legs, Opus as white/adjudicator/apply. Distinct from the
> concurrent 2026-07-14 governance-revector session (postwach-01). Repo: DocWach/WySE-Theory (local
> folder "Fable 5 planning").

**Hive:** PostWach (CTO / Chief Scientist). **Researcher:** Paul Wach. **Model:** Opus 4.8 [1m]
(+ Codex red legs on ChatGPT sub, Gemini legs on agy subscription -- both off the Claude weekly limit).
**Status:** CLOSED. Original scope fully accomplished; session then expanded into a new consolidation/
reachability phase (handed to a distillation session).

**Headline:** Restored Gemini as a review leg (via `agy`), ran a two-red / two-blue RBW harness, and
**closed all seven decision-layer candidates (A, B, C, D, E, F17, F2) CLOSED-HARDENED**. The harness
earned its keep hard: the cross-vendor / owed red caught **four real defects that same-vendor or
WHITE-substitute checks had ratified, including TWO premature closures** (A's ill-posed preorder fence;
B's entire prior v5 closure). The session then paused Fable and opened a consolidation phase (a single
"reachable" visual + audience-spectrum write-up), building the (D_s, D_b) decision-plane anchor and
reframing toward a three-subimage DEF-style stratified composite.

## 1. Gemini restored (the original item 2)
- `gemini` CLI = 429 quota-exhausted (hard cap, did not self-clear). The working Gemini path is **`agy`
  (Antigravity)** headless: `agy --dangerously-skip-permissions --model "Gemini 3.1 Pro (High)" -p "..."`
  (flags FIRST; `-p` takes the prompt as its value). Corrected the stale "agy is interactive-only" and
  "~20/day" notes in `memory/project_gemini_cli_migration.md`: agy has a working `--print` mode, and its
  quota is a HARDER cap on a ~weekly reset ("Individual quota reached ... Resets in 149h" hit mid-session
  2026-07-14, so Gemini is out ~6 days).

## 2. The RBW harness + per-candidate outcomes (the original item 1)
Design (your steer): **two reds (Codex + Gemini) + two blues (Codex + Gemini) + Opus white/adjudicator**;
Codex `codex exec --dangerously-bypass-approvals-and-sandbox`, Gemini via `agy`. All witnesses self-
asserting (predict-first, SHA-pinned); SHAs stable across every round (zero math refutations, all session).
- **A** (FoM-scalar vs Kannan-poset): CLOSED-HARDENED at **v10** after a tri-vendor round. Gemini caught
  the "read on the quotient" preorder fence as ILL-POSED (F=w.s does not descend to the quotient since s
  is not constant on ~_K classes) -- a fence 5 prior rounds + Codex + both blues had endorsed. My fix
  OVER-corrected twice (a false "no weak extension" universal), caught same-round by both reds; final form
  = definite-sign / product-comparable class-difference condition. Delta T-A2(iii) machine-checked
  (SHA f7951c2f). Records: `RBW_A_v6_2026-07-14.md`, `RBW_A_v9_2026-07-14.md`.
- **C** (SSF acceptance-region): CLOSED-HARDENED at **v7**. Gemini caught a STRUCTURAL contradiction Codex
  passed: the T-C3 scope banner globally forced the labeling to be antitone-through-plane, contradicting
  T-C3(ii)'s premise; scoped the hypothesis to the positive result. SHA 77892ea4. Record: `RBW_C_v6_2026-07-14.md`.
- **F17** (set-based narrowing): CLOSED-HARDENED at **v7**. Applied RBW_F17_v5 checklist (V5-R1 foundation
  overclaim, V5-R2 false "H-DOM necessary is open" subclaim, V5-R3 H-6 for LIMIT(iii)); Codex then caught a
  sibling omission (H-DOM missing from the transfer surfaces); v7 added it; Codex confirm clean. SHA bc17d82.
  Record: `RBW_F17_v6_2026-07-14.md`.
- **B** (confidence-weighted acceptability): CLOSED-HARDENED at **v7** -- but **the owed Codex red revealed
  B had been PREMATURELY closed in v5** (that closure used WHITE-substituted machine checks because Codex
  had timed out). The real red found 3 issues (RW-13 still a false universal without a STRICT cycle;
  "exact characterization" overclaim; theta-minimality). Fixed v6; the v6 confirm caught my (c)-bullet
  false universal; v7 corrected it (theta>1/2 = guaranteed-not-necessary antisymmetry). SHA 34af0765.
  Targeted re-confirm timed out (Codex tooling); white-verified. Record: `RBW_B_v6_2026-07-14.md`.
- **D, E, F2**: closed in the prior session; unchanged.

**OWED:** a **Gemini second-red on B, C, F17** when agy's quota resets (~6 days). Everything else is fully
cross-vendor confirmed.

## 3. Methodology finding (the point of the session)
The **cross-vendor / owed red is load-bearing** -- demonstrated FOUR times this session, on separate
candidates: A (ill-posed fence), A (my over-correction), C (structural contradiction), B (whole premature
closure). A single-vendor red, or a WHITE-substituted red, ships all four. Also: **the apply/white leg's
own fixes must be adversarially checked** -- I introduced 2+ overclaims while fixing, each caught same
round. Feeds `[[project_governance_revector]]` item 4 (codify cross-vendor red as standard practice).

## 4. Consolidation / reachability phase (the divergence)
After F17, you paused Fable to "review what we have": build ONE reachable visual that decomposes across an
audience spectrum (labrador L1 -> Einstein L5); the test = if it cannot reduce to a single graspable
picture, we do not understand it / WySE is not reachable. Honest-reporting agreed: report the break, do
not force a seam.
- **Built the phase-1 anchor:** `docs/writeup/figures/WySE_decision_plane_anchor_L2_2026-07-14.png` (+ the
  `plane_anchor.py` script) -- the (D_s, D_b) plane with the down-set acceptance region, frontier antichain,
  accepted/rejected models, origin = exact. Deterministic matplotlib render (NO generative image model).
- **Honest finding:** the plane cleanly carries C (down-set + frontier), A (scalar projection picks a
  rejected winner), F17 (nested narrowing), and rests on D (shared carrier). It does NOT carry B or the
  adequacy dimension -- those are ORTHOGONAL to (D_s, D_b) (uncertainty over WHICH acceptability order /
  whether the model is adequate). So the honest single visual is **"plane + an orthogonal acceptability/
  confidence axis" (2.5D)**, not flat 2D. A drafted `plane_plus_confidence_axis.py` (2.5D) is HELD, not
  rendered -- superseded by your reframe below.
- **Your reframe (end of session, key input for distillation):** "one image" = a COMBO of ~3 subimages;
  keep the plane, define two more, the D_h isomorphism quad an OPTION; arrange it like the **UofA Digital
  Engineering Factory (DEF)** -- **stratification layers with a decision-framing box on the left going up
  the stratification**. My proposal (OPEN for the distillation session): strata bottom->top = D_h morphism/
  isomorphism quad (foundation: how "alike" is defined) -> (D_s,D_b) plane (measure) -> acceptability/
  confidence (decide); left spine = the decision loop (need -> generate -> measure -> good enough? -> select).
  OPEN STEER: (a) bottom panel = isomorphism quad vs needs/purpose layer; (b) strata = decision loop vs the
  WySE level scheme (LO/LF/LA/LC); (c) reuse the existing quad from `[[project_two_axis_quadrant_figure_reuse]]`.

## 5. Tooling / ops
- **agy/Gemini quota-exhausted ~6 days** (not a timeout -- a hard cap). `gemini` CLI 429. **paperbanana
  likely also down** (same GOOGLE_API_KEY). **Deterministic rendering (matplotlib 3.10.8 / Mermaid) is the
  reliable path** for precise technical visuals and is BETTER than any generative image model for labeled
  geometry (a ChatGPT/Gemini image garbles axes/labels -- a broken link under the reachability bar).
- Logged capability-backlog: make paperbanana backend-pluggable (VLM critic first) -- see
  `[[project_paperbanana]]` item 3. Defensible infra, not a blocker, does NOT fix the technical-diagram limit.
- **Orphaned processes:** two `codex` PIDs (13832 ~2:04pm, 45868 ~3:32pm) lingering from timed-out reds;
  NOT killed (name-based kill could hit the concurrent governance session). Reap manually if desired.

## 6. Commits
- **DocWach/WySE-Theory:** A + C closures pushed at **e15f860** (mid-session). B, F17, all five 2026-07-14
  RBW records, the candidate CLOSED-HARDENED stamps, and the phase-1 figure + scripts committed at
  end-of-session (see git log). Decision-layer commit/push was your authorized scope.
- **Hive (this repo):** this archive + the R014 scorecard + the distillation seed + memory updates committed
  (NOT pushed -- hive push not in scope).

## 7. Open / next (-> the distillation session)
- **Distillation session** (your next): build the DEF-stratified 3-subimage composite + the audience-spectrum
  write-up. Entry point = `[[project_wyse_distillation]]`; detailed notes = THIS archive; anchor figure +
  scripts under `docs/writeup/figures/`. Resolve the three OPEN STEER questions in §4.
- **Owed Gemini second-red on B, C, F17** when agy resets (~2026-07-20).
- **R019 reference debt** (before ANY render of the write-up): the `[PLACEHOLDER]` refs across A (Gordan
  load-bearing, Fishburn, Keeney-Raiffa, Farkas/Motzkin, Szpilrajn, Arrow/Sen), C (Davey-Priestley, Birkhoff,
  Klement-Mesiar-Pap, Grabisch), B (Fishburn, McGarvey, Sen, Barthelemy-Monjardet, Moulin), F17 (Davey-
  Priestley, Sun 2026, Micouin 2008) must pass refverify. None drafted from memory.
- Reap the two orphaned codex processes.
