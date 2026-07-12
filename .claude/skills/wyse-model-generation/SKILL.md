---
name: wyse-model-generation
description: >
  Generate a VALIDATED WySE system model z=(SZ,IZ,OZ,NZ,RZ) at a chosen stratification level from
  GROUNDED input (spec / governing equations / DEVS or SysML model / dataset), via a
  propose -> validate -> measure loop. NEVER assert a model from prior knowledge. Load when
  transcribing a specified system into a formal WySE model for the morphism engine, when choosing a
  model's resolution level (LO/LF/LA/LC), or when validating that a generated model reproduces
  ground-truth behavior. Phase-1 (STRONG-grounding) scope ONLY; cross-level generation and
  weak-grounding inference ("point at a car") are declared FUTURE, not built. Do NOT load for computing
  morphisms between EXISTING models (use morphism-domain-reference + the witness discipline), for
  research-target selection (morphism-research-frontier), or for the rigor bar itself
  (morphism-research-methodology).
---

# WySE Model Generation (Phase 1: grounded)

**Status tag [R016]: (a) research artifact -- NOT yet exercised end-to-end.** Authored 2026-07-12. This
skill encodes a METHOD, not a demonstrated capability; it has been run on ZERO real generations.
Everything it produces is an (a) HUNCH-MODEL until its validation witness passes. Promote toward (b)
demonstrated ONLY after the first end-to-end grounded generation validates the loop against real ground
truth. See "Where this stands" (Section 8). Continuous improvement is expected and required.

PROVENANCE (R018): Opus 4.8 (claude-opus-4-8[1m]), Anthropic, Claude Code CLI, 2026-07-12,
principal-directed CREATE (R020; no prior skill existed -- confirmed by search of the skills tree and
the 2026-07-11 file-history). Grounded in [[research_equivalence_convention]],
[[feedback_measure_not_assume_llm_intuition]], the morphism-research-methodology lifecycle, and the
closed morphism library. Governance registration PENDING with Alpha Empress (COO).

---

## 0. The one rule (why this skill exists)
A model GENERATED from prior knowledge is an ASSUMPTION. WySE exists to MEASURE, not assume
([[feedback_measure_not_assume_llm_intuition]]). So a generated model is a **hunch-model (lifecycle
state 1) with no rights** until a **validation witness MEASURES** that its behavior reproduces the
system's GROUND-TRUTH behavior. This skill is that discipline for model generation -- the upstream
analogue of the library's "recompute, do not narrate" rule. The equivalence the engine ultimately
measures is graded `D_s` ([[research_equivalence_convention]]); a wrong (unvalidated) model poisons
that measurement at the source.

## 1. What "a model" is, and what "generation" produces
A WySE system model is the Wymorian quintuple `z=(SZ, IZ, OZ, NZ, RZ)` -- state set, input set, output
set, transition `NZ`, readout `RZ` (see morphism-domain-reference). Generation produces a candidate `z`
AT A LEVEL of the stratification (LO / LF1-3 / LA / LC) PLUS a validation witness. The SAME system has
DIFFERENT `z` at different levels; the level is chosen by PURPOSE (the resolution the use-case needs),
never by default. Choosing the level is itself a recorded decision.

## 2. Grounding regimes (honest scope fence)
- **Phase 1 (THIS skill): STRONG grounding.** A formal spec / governing equations / a DEVS or SysML
  model EXISTS. Generation is TRANSCRIPTION into the quintuple + a validation witness. Lowest
  assumption. Real-ground-truth examples: the DC-motor, the pendulum, Patsy.
- **Phase 2 (FUTURE, not built): cross-level generation.** Generate the same system at multiple levels;
  relate them by the already-closed resolution/coupling morphisms (each pair is a catalog entry).
- **Phase 3 (FUTURE, not built): weak-grounding inference.** Only observations, no spec. Highest
  assumption; the validation bar is everything and is currently UNSPECIFIED. Flagged, not built.

## 3. Runbook: propose -> validate -> measure (Phase 1)
- **Step 0 -- GROUND the input.** Name the exact source (spec file, equation set, dataset) and its rigor
  tag. If the only "source" is prior knowledge, STOP: emit `BLOCKED: ungrounded generation` (Guard 1).
- **Step 1 -- CHOOSE the level.** State the target level and WHY the purpose needs that resolution.
- **Step 2 -- PROPOSE the quintuple.** Transcribe `SZ,IZ,OZ,NZ,RZ` from the grounded source. Every
  component traces to a source line/equation; nothing invented. Mark any inferred component explicitly.
- **Step 3 -- PREDICT the validation numbers BEFORE running.** State the ground-truth behavior the model
  must reproduce (trajectories / I/O / invariants) as specific numbers or sets that a mismatch would
  FORBID. A validation that cannot forbid a mismatch is not a validation.
- **Step 4 -- VALIDATE with a self-asserting witness.** Recompute the model's behavior and compare to
  ground truth in a script that asserts the match and prints a SHA-256; predicted numbers must match on
  the first run (recompute, do not narrate).
- **Step 5 -- TAG + hand off.** On PASS: a validated (a) artifact, rigor level {proven if machine-checked
  exactly on a finite/exact carrier | SME-adjudicated | asserted} per morphism-research-methodology. On
  FAIL: a documented retirement or a revised hunch (never a smoothed-over "close enough"). The validated
  model is the INPUT to the morphism engine (compute `D_s` vs another validated model -> measured GRADED
  equivalence, [[research_equivalence_convention]]).

## 4. Guards (measure-not-assume; stop and ground or emit BLOCKED)
1. Never PROPOSE a component from prior knowledge without a grounded source. `BLOCKED` beats confabulated.
2. Never present an unvalidated model AS a model; it is a hunch-model until the witness passes (R016 (a)).
3. The level is a decision with a stated purpose, not a default resolution.
4. A witness that "confirms" without recomputing behavior against ground truth is theater; recompute.
5. If the spec is incomplete, transcribe what is grounded and emit `BLOCKED: <missing component>` for the
   rest -- do not fill the gap from memory.

## 5. Where this sits in the engine
`generate` -> [validated model] -> morphism engine (`D_s` record + witness) -> measured GRADED
equivalence ([[research_equivalence_convention]]) -> optimization / model-SELECTION on the `(D_s, D_b)`
plane welded to the Kannan acceptability poset (FUTURE; parallel to generate but cannot conclude until
generate yields candidates). Model generation is the FIRST brick; everything downstream consumes it.

## 6. When to use / not use
Use: transcribing a specified system into a validated WySE model; choosing a model's resolution level;
validating a generated model against ground truth. Do NOT use: computing morphisms between EXISTING
models (morphism-domain-reference + the witness discipline); picking research targets
(morphism-research-frontier); setting the rigor bar (morphism-research-methodology); weak-grounding
inference (Phase 3, not built) -- if asked, say so and stop.

## 7. Related
[[research_equivalence_convention]] (equivalence = graded `D_s`, the measured goal),
[[feedback_measure_not_assume_llm_intuition]] (the one rule), [[project_stakeholder_elicitation_capability]]
(the need->outcome-space front-end that scopes the level), [[project_home_lab_assistant]] (Patsy = the
worked WySE-model-generation example), morphism-research-methodology (lifecycle + rigor tags),
morphism-domain-reference (the quintuple + typing).

## 8. Where this stands + continuous improvement (READ FIRST; be honest)
- **Integration status:** (a) research artifact, authored 2026-07-12, **exercised on ZERO real
  generations.** Do NOT present it as demonstrated (b) or integrated (c).
- **Validated scope:** NONE yet. The propose->validate->measure loop is a DESIGN; its first real test is
  pending. Recommended first anchor: the DC-motor (exact ground truth already in the library).
- **Improvement backlog (known gaps):** (i) Phase 2 cross-level and Phase 3 weak-grounding inference
  unbuilt; (ii) no elicitation front-end wired in (level-choice is manual); (iii) no optimization /
  selection back-end; (iv) the validation-witness bar for weak grounding is UNSPECIFIED; (v) this is a
  METHODOLOGY, not a repeatable tool.
- **Promotion path:** (a)->(b) after the first end-to-end grounded generation + validation on a real
  ground-truth object; (b)->(c) when wired to the elicitation front-end + the morphism engine + the
  selection back-end as one coherent flow.
- **Discipline:** every use MUST update this section with what broke and what the next version needs.
  This skill is expected to change fast; a stale "where this stands" is a bug.

## 9. Provenance / maintenance
Authored 2026-07-12 (Opus 4.8), CREATE per R020. REGISTER with Alpha Empress (COO) for governance
compliance. Re-verify after the first grounded generation: update Section 8 (exercised? validated
scope?) and the top-line integration status. Confirm sibling skills named in Section 6 still exist.
