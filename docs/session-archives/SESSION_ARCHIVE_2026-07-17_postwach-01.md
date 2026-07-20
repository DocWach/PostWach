# Session Archive: Scorecard v1.3 -- Capability Utilization (RBW + GQM) + Capability-Capture Daemon Spec
**Date:** 2026-07-17
**Hive:** PostWach (CTO / Chief Scientist)
**Type:** Research-instrument design + adversarial verification + problem formulation
**Provenance (R018):** claude-opus-4-8[1m], Anthropic, Claude Code CLI, principal-directed.

## Objective
Resume the Hive Empire update with one logged item: "Update scorecard to reflect skills, agents, swarms,
and tools used." Interrogate the intent (not just the literal four categories), decide the right instrument,
and ship it -- without shipping a flawed measurement into a research dataset.

## What was done

### 1. Intent interrogation (address-intent, not literal phrasing)
The literal ask named four capabilities (skills / agents / swarms / tools). Principal directed a broader
read: what about plugins and hooks? Established that the four are all *actively-invoked* capabilities and
that the harness surface also includes ambient infrastructure (plugins/MCP, hooks, memory). Principal also
directed splitting **workflows** out from **swarms** (the Workflow tool vs claude-flow `swarm_init` are
different mechanisms) -- making the ask really five invoked categories + an ambient trio.

### 2. RBW adversarial review BEFORE execution (principal-directed gate)
Loaded the `red-blue-white` skill (R020: invoke, don't re-enact). Config: in-session Workflow, 4 diverse
RED lenses (construct-validity / fabrication-burden / completeness-redundancy / analytic-utility) -> objective
BACKSTOP (retro-apply the draft schema to the real 2026-07-16-postwach-04 card) -> 2 WHITE adjudicators ->
synthesis-reconcile. **8 agents. Verdict: `claim-holds-with-caveat`.** RED (tool-verified against the live
corpus) killed the naive "invoked/ambient, all-required, human-filled" draft:
- the invoked/ambient split was **not a partition** (mixed an agency axis with a variance axis);
- a slash command **IS a skill** in this harness, so one act triple-counted across fields (no de-dup rule);
- new fields **duplicated the one metric** `analyze_scorecards.py` consumes (`agents_spawned`), risking drift;
- **nothing downstream consumes** the fields, so "all-required" was burden with no estimator;
- "all-required" over unobservable-at-fill-time fields = **fabrication pressure**.
It also caught a live data bug: 5 cards' `cumulative_ledger` still pointed at the pre-rename `fable_cost_ledger.md`.

### 3. GQM problem formulation (principal nudge: "are you using a problem-formulation skill?")
This was the miss -- I had solutioned (drafted fields) before formulating. Engaged the `problem-framer`
agent to produce a Goal-Question-Metric formulation. It corrected two of my premises against source
(`agent_failures` lives in D4, not D2; the consumer reads more than one field) and produced the architectural
fix that dissolved every RBW defeater at once: **stop asking a human to attest capability use; extract it with
a daemon.** Metric catalog M1-M12 typed presence/count/dose x capture-channel (transcript / hooklog / config /
human), each reconciled to an authoritative field, GAPs marked honestly. Resolved workflow-vs-swarm
**objectively**: keyed on which orchestration tool actually fired (`Workflow` -> workflow; `swarm_init`/
`hive-mind` -> swarm; both -> hybrid; Task-only -> agent-fanout; none -> single-agent; `unknown` ONLY when no
capture). Presence != frequency: "which plugin" is categorical identity, not a count.

### 4. Shipped (template now; daemon deferred)
- **`scorecard-template.yaml` -> v1.3.** D2b reframed *Skills Utilization* -> **CAPABILITY UTILIZATION**.
  Locked rules: PLACEMENT = agency (not variance); DE-DUP = classify by the tool that fired; SINGLE SOURCE OF
  TRUTH (D2b never restates `agents_spawned`/`tool_calls`/`swarm_topology`); `not_captured` a valid value
  (never fabricate); ambient config demoted to record-once. Added `coordination_style` to D2.
- **`capability_capture_spec_2026-07-17.md`** -- daemon that extends `cost-capture.mjs` to machine-source D2b
  from the transcript. R016 (a) design note. **Deferred to a quiescent point** (shared `.claude/` SessionEnd
  hook; INCIDENT-001 concurrency hazard) -- template ships first.
- **`2026-07-17-postwach-01.yaml`** -- this session's scorecard, dogfooding every new v1.3 field on real data.
- **Fixed the stale pointer** in 5 cards (`fable_cost_ledger.md` -> `research_token_ledger.md`).
- **Committed** `c017ed6` on `main` (8 files; no ruvnet trailer). Not pushed.

## Key decisions
- **RBW before execution on a load-bearing instrument decision.** The schema governs a research dataset going
  forward and reverses/extends the existing D2b -- exactly the RBW trigger. It paid for itself: zero files were
  written on the defeated first design.
- **Formulate before solutioning.** The `problem-framer`/GQM step reframed "add YAML fields" into "build a
  capture daemon" -- the correct instrument. Skills-first applies to formulation, not just execution.
- **Daemon architecture over human attestation.** Machine-extraction is the single move that makes the catalog
  objective, zero-burden, drift-free, and fabrication-proof.
- **Sequencing = template now, daemon at quiescence.** The template is an ordinary `Papers/` file (safe anytime);
  the daemon edits a shared live hook and must wait for no-other-sessions + prompt commit.
- **Ownership = cost-instrumentation thread.** The daemon extends the same `cost-capture.mjs`; Alpha Empress
  registers v1.3 (same handoff as the B1 cost hook).

## Artifacts
- `Papers/AI_Swarm_Productivity/scorecard-template.yaml` (modified -> v1.3).
- `Papers/AI_Swarm_Productivity/capability_capture_spec_2026-07-17.md` (created; daemon spec).
- `Papers/AI_Swarm_Productivity/data/scorecards/2026-07-17-postwach-01.yaml` (created; dogfood card).
- 5 cards repointed (`2026-07-16-postwach-01/02/03/04`, `2026-07-16-sysmlv2-01`).
- RBW workflow script `rbw-scorecard-v13-schema-wf_28a0816a-6f5.js` (session workflows dir).
- Memory `project_cost_instrumentation` updated with the capability-capture increment.
- Commit `c017ed6` (main, unpushed).

## Next steps (for pick-up)
1. **Implement the capability-capture daemon** at the next quiescent point (no other live sessions), per
   `capability_capture_spec_2026-07-17.md`; verify on one real transcript via manual mode (R016 -> (b)).
2. **Alpha Empress:** register the v1.3 template + the capability-capture increment for cross-hive consistency.
3. Consider a committed estimator/RQ in the GQM outline that actually consumes the D2b fields (RBW's L4-F5 point
   -- until one exists, the moderation questions are unanswerable at current N; D2b is covariate accumulation).
4. Optional: `git push` `c017ed6`.

## Memory-worthy
- Written: capability-capture increment folded into `project_cost_instrumentation`.
- Reinforced live: [[feedback_address_intent_not_literal]] (four categories -> full surface + plugins/hooks),
  [[feedback_skills_first]] (formulate before solutioning; RBW invoked, problem-framer engaged),
  [[feedback_measure_not_assume_llm_intuition]] (daemon = measure; fabrication designed out).
