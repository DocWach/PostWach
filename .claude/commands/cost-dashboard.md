---
name: cost-dashboard
description: Run the AI_Swarm_Productivity cost dashboard / backfill estimator and summarize the result
---

# Cost Dashboard

Run the token/cost dashboard for the AI_Swarm_Productivity scorecard corpus.

## Steps
1. From the project root, run (use `python`, NOT `python3` — the latter hits the Windows Store shim here):

   ```bash
   python "Papers/AI_Swarm_Productivity/cost_dashboard.py" $ARGUMENTS
   ```

   `$ARGUMENTS` is the optional mode: `calibrate` (terminal only), `dashboard`, `report`, or empty/`both`
   (default: writes both the dashboard and the backfill report).

2. The script reads `Papers/AI_Swarm_Productivity/data/scorecards/*.yaml` and, if present,
   `data/scorecard_classifications_2026-07-16.json` (agent-derived type labels; falls back to the
   keyword heuristic if absent). Output files are dated by the newest scorecard:
   `data/cost_dashboard_<date>.md` and `data/cost_backfill_report_<date>.md`.

3. Report back the cumulative estimate with its band, the per-hive and per-session-type rollups, and the
   paths of any files written. Preserve the R016 (a) MODELED-ESTIMATE framing and the per-row bands /
   measured-vs-estimated flags; never present an estimated figure without its margin.

## Notes
- This is a backfill/reporting tool: it recomputes from the scorecards each run. It does NOT append new
  sessions to `data/research_token_ledger.md` — that is the separate B1 auto-capture hook
  (`.claude/helpers/cost-capture.mjs`, SessionEnd; appends a per-session row + prints a confirmation).
- Dollars are notional (subscription + toll-free-Fable + external Codex ⇒ ~0 actual marginal); state that.
