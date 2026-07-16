# Session Archive: Cost Instrumentation (R014 backfill + auto-capture + dashboard)
**Date:** 2026-07-16
**Hive:** PostWach (CTO / Chief Scientist)
**Type:** Ops / tooling (capability build)
**Session id:** 2026-07-16-postwach-03

## Objective
Execute `Papers/AI_Swarm_Productivity/cost_instrumentation_spec_2026-07-16.md`: (B0) probe whether a
SessionEnd hook exposes token/cost, (B2) build a dashboard, (A) backfill-estimate token/cost across all
past scorecards. Deliverable framing: a defensible order-of-magnitude, R016 (a) MODELED ESTIMATE, NOT
accounting-grade recovery (raw usage is ephemeral and gone for ~240 of the sessions).

## What was done (in spec order)
- **B0 (gating probe).** Found: a Claude Code `SessionEnd` hook stdin carries only
  `{session_id, hook_event_name, reason, cwd}` — NO token/cost; no hook event exposes `/cost` dollars.
  BUT the session transcript JSONL sits at a deterministic path
  (`~/.claude/projects/<slug>/<session_id>.jsonl`) with per-turn `message.usage` blocks. Proved the parse
  on the live transcript (1,317 turns summed). ⇒ **auto-capture is feasible by transcript-parse**, not the
  semi-manual `/cost` fallback. Built `.claude/helpers/cost-capture-probe.mjs` (probe + B1 prototype),
  wired into settings.json SessionEnd (armed; writes `.claude-flow/data/sessionend-probe.json` at session end).
  Caveat carried forward: workflow SUBAGENT tokens are `<usage>subagent_tokens:N</usage>` annotations, not
  `message.usage` — B1 must scan both.
- **B2 (dashboard).** `Papers/AI_Swarm_Productivity/cost_dashboard.py` (stdlib only): calibrate / dashboard /
  report modes. Regex extraction tolerant of 3 schema versions + inline comments.
- **Part A (backfill).** Calibrated on scorecards recording tokens AND agents≥2 → **median ~82k output
  tokens/agent, IQR [65k,105k]**. Classified all sessions by a **10-agent Workflow sweep** (each agent read
  scorecard + matching archive), correcting the keyword heuristic (which mislabeled 96 paper/manuscript
  sessions as 31). Applied `agents × median`; measured where present; 0-agent = ~0 subagent (main-loop out-of-unit).
- Populated `data/fable_cost_ledger.md` (measured vs estimated flags + per-row bands), wrote
  `data/cost_backfill_report_2026-07-16.md` and `data/cost_dashboard_2026-07-16.md`, dogfooded this session,
  drafted the Alpha Empress governance handoff, added a `/cost-dashboard` slash-command wrapper.

## Headline result (R016: (a) MODELED ESTIMATE, ±30–50%, not recovery)
Full corpus (260 scorecards as of session end, Feb 25–Jul 16, all hives): **~77.3M subagent-output tokens
[64–94M]** (17.8M measured + 59.5M modeled); **~$1,005 notional / ~$0 actual** (subscription + toll-free-Fable
+ external Codex). Heaviest type: derivation/Fable 32.1M/390 agents. Living figure — recomputed each run.

## Principal steers honored
- **Every published figure carries an estimate flag AND a ±band per row** (not just the top line). Mid-session
  gate: "are all additions marked as estimates with margin? This is important for publication." → added `band`
  + `measured/estimated/mixed(Nm/Ne)` columns to every rollup; audited: zero bandless tables remain.
- Kept the recent-Fable-line running total (~16M) SEPARATE from the corpus-wide backfill (~77M) — do not conflate.

## Honest caveats / flags
- **R020 gap:** the spec named `update-config` + `hooks-automation` skills; neither was invoked (settings.json
  edited by hand). Logged in the scorecard. Repeats the "re-enact ad hoc" pattern the rule targets.
- **Calibration is recent-heavy:** all 12 points are Jun 23–Jul 16 heavy sessions; early (Feb–May) rows are the
  weakest, extrapolated by agent-count only.
- **Living-figure drift:** two cards landed mid-session (this dogfood + a concurrent `2026-07-16-sysmlv2-01`
  from the SysMLv2 hive submitting into the shared OneDrive store — NOT deleted, per the INCIDENT-001 discipline).
  The token headline was stable across the drift (77.3M); only agent/measured counters moved ±2.
- **Sweep value:** the aggregate was already fixed by measured agent-counts; the ~1.1M-token sweep bought
  corrected TYPE labels, not a different headline.

## Deliverables (all committed)
- `.claude/helpers/cost-capture-probe.mjs`, `.claude/settings.json` (SessionEnd probe), `.claude/commands/cost-dashboard.md`
- `Papers/AI_Swarm_Productivity/cost_dashboard.py`
- `data/fable_cost_ledger.md` (populated), `data/cost_backfill_report_2026-07-16.md`, `data/cost_dashboard_2026-07-16.md`,
  `data/scorecard_classifications_2026-07-16.json`
- `docs/governance_handoff_cost_instrumentation_2026-07-16.md`
- Scorecard `data/scorecards/2026-07-16-postwach-03.yaml`; memory `project_cost_instrumentation.md`

## Cost of this session (dogfood)
~1.16M subagent output tokens (measured: claude-code-guide 52,241 + classifier sweep 1,107,017), ~11 agents,
~$15 notional / ~$0 actual (subscription). Main-loop additional (out-of-unit).

## Next (deferred, not blocking)
1. B1 full auto-capture: sum subagent `<usage>` annotations, not just main-loop `message.usage`.
2. Inspect `.claude-flow/data/sessionend-probe.json` next session to confirm the empirical SessionEnd payload.
3. Alpha Empress: register template v1.2 + hook/dashboard for cross-hive R014 consistency.
4. Decide whether to FREEZE the paper's number at a pinned corpus snapshot vs let it live.
