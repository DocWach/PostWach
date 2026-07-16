# Governance Handoff — Cost Instrumentation (PostWach → Alpha Empress), 2026-07-16

**From:** PostWach (CTO / Chief Scientist)  **To:** Alpha Empress (COO, governance registration)
**Re:** R014 cost-instrumentation build. PostWach BUILT the capability; Alpha Empress REGISTERS it
for cross-hive consistency (per `cost_instrumentation_spec_2026-07-16.md`, "Governance / skills").

## What was built (this session)
1. **Scorecard template v1.2** (`Papers/AI_Swarm_Productivity/scorecard-template.yaml`).
   Bumps the D2 block: `tokens_output` now REQUIRED; adds structured `tokens_by_workflow`,
   `cost{total_cost_usd, measured, cost_estimate_usd, cost_method, billing_regime}`, and a
   `cumulative_ledger` pointer. **Cross-hive impact:** every hive's end-of-session R014 scorecard
   must now fill the cost block. This is the item needing formal registration for consistency.
2. **Auto-capture hook + prototype** (`.claude/helpers/cost-capture-probe.mjs`, wired in
   `.claude/settings.json` SessionEnd). B0 finding: SessionEnd stdin exposes NO token/cost, but the
   session transcript JSONL (deterministic path, per-turn `usage` blocks) does — so auto-capture is
   feasible by transcript-parse. The probe is armed to confirm the exact SessionEnd payload empirically.
   Construct class = **HOOK + SCRIPT**, not an MCP-server plugin (right-sized per the taxonomy note).
3. **Dashboard + backfill estimator** (`Papers/AI_Swarm_Productivity/cost_dashboard.py`, stdlib-only).
   Renders cumulative / per-hive / per-type / per-week rollups; produces the dashboard and the
   backfill report.

## Deliverables produced
- `data/fable_cost_ledger.md` — populated with the corpus-wide backfill (measured vs estimated flags).
- `data/cost_backfill_report_2026-07-16.md` — method + aggregate + per-session appendix, all banded.
- `data/cost_dashboard_2026-07-16.md` — live rollups.
- `data/scorecard_classifications_2026-07-16.json` — 258 sessions typed (10-agent sweep).

## Headline result (R016: (a) MODELED ESTIMATE, ±30–50%, NOT recovery)
Full corpus (260 scorecards as of 2026-07-16, Feb 25–Jul 16, all hives): **~77.3M subagent-output tokens
[64–94M]**, 17.8M measured + 59.5M modeled; ~$1,005 notional (API-rate), **~$0 actual** (subscription/toll-free/Codex).
Living figure (recomputed per run). Every published figure carries an estimate flag AND a ±band per row.

## Registration asks of Alpha Empress
1. **Register template v1.2** as the cross-hive R014 standard; notify hives the cost block is required.
2. **Register the hook + dashboard** as the approved cost-capture mechanism (HOOK+SCRIPT class).
3. Confirm the **R016 fencing convention** (every backfilled number flagged (a) + banded) as the
   house standard for the AI_Swarm_Productivity paper's cost figures.

## Open (deferred, not blocking)
- B1 auto-capture must also sum subagent `<usage>` annotations, not just main-loop `message.usage`.
- Empirical SessionEnd payload confirmation lands at this session's end (`.claude-flow/data/sessionend-probe.json`).
- Early (Feb–May) rows are the weakest; all 14 calibration points are recent heavy sessions.
