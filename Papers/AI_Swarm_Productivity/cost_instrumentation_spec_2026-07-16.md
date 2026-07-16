# Cost-Instrumentation Session — Spec / Design Note (2026-07-16)

Purpose: a self-contained plan for a SEPARATE session that (A) backfill-ESTIMATES token/cost across all past
scorecards, and (B) builds going-forward auto-capture + a dashboard. Written so that session starts with a plan,
not a blank page. Author: PostWach (Opus 4.8), principal-directed. R016: this is a DESIGN NOTE (a); nothing built.

## Grounding facts (measured this session)
- **257 scorecards**, all centralized in `01 PostWach/Papers/AI_Swarm_Productivity/data/scorecards/` (the other
  hives submit here; empire-wide scan found no separate hive stores). Cross-hive: 212 postwach, 45 across
  gi-joe, sead, sysmlv2, nnsa, lawsun, fort-wachs, roadmapping, finance-bro, ignite. Span Feb 25 -> Jul 16 (~5 mo).
- **197 session archives** in `docs/session-archives/`.
- **Only 13 scorecards carry a `tokens_output` value; 71 archives mention tokens/cost at all** (mostly
  qualitative). Raw usage (task-notification `usage` blocks, `/cost`) is EPHEMERAL and GONE for past sessions.
- Therefore: for ~240 of 257, precise recovery is IMPOSSIBLE. This is an **ESTIMATION** problem, not recovery.
- Existing assets: running ledger `data/fable_cost_ledger.md`; scorecard template bumped to **v1.2** (token/cost
  now REQUIRED + structured; ledger pointer added).

## Part A — Backfill estimation (feeds the AI_Swarm_Productivity paper)
A1. **Calibrate** a per-session-TYPE token model on the 13 known-token scorecards + the 71 partial-signal
    archives. Session types (from archives): `derivation/Fable`, `paper/manuscript`, `governance`, `ops/tooling`,
    `review/refverify`. Model = median tokens per type x size-proxy multiplier (agent-count if recorded, else
    artifact volume / duration bucket).
A2. **Classify all 257** via a parallel-classifier workflow (~10 agents x ~26 sessions; each reads the matching
    archive + scorecard and emits `{id, hive, date, type, size_proxy, agents_if_recorded, tokens_if_recorded}`).
A3. **Apply** the model -> per-session estimate + error band; **aggregate** per-hive, per-week, per-type,
    cumulative. Write into the ledger (mark each row `measured` vs `estimated`). Produce a short backfill report
    with fidelity (expect **aggregate +/-30-50%**; worse for early lighter sessions since all 13 calibration
    points are recent heavy sessions -- state this honestly).
    Deliverable: populated ledger + `data/cost_backfill_report_<date>.md`. R016: (a) MODELED ESTIMATE, fenced.

## Part B — Auto-capture + dashboard (right-sized: hook + script, NOT an MCP-server plugin)
B0. **FEASIBILITY PROBE FIRST (gates B1).** Write a trivial `SessionEnd` hook (settings.json) that logs whatever
    session metadata the harness passes it; run one session; inspect. QUESTION: does a SessionEnd hook receive
    token/cost, or must it read `/cost`? (The ruflo SessionStart hook proves hooks get SOME context; usage figures
    are the unknown.) Use the `update-config` + `hooks-automation` skills.
B1. **Auto-capture.** If usage is exposed -> hook appends a ledger row per session automatically. If NOT ->
    semi-manual fallback: the hook writes a stub row + reminds the session to paste `/cost`, or parses `/cost`
    output if reachable. Be honest about which regime you land in.
B2. **Dashboard.** A stdlib Python script that reads the ledger + all 257 scorecards and renders: cumulative
    tokens/$, per-hive, per-week, per-session-type, Fable-toll projection (only ~15-20% Fable-derivation tokens
    tolled post-Jul-19), plus D3/D4 rollups (first_pass_quality, rework_ratio) if useful. Output: a markdown
    dashboard (+ optional matplotlib/mermaid plot). Optionally a `/cost-dashboard` slash-command wrapper.
    R016: (b) demonstrated once it runs on real data.

## Effort / cost
~3-5M subagent tokens, half a day wall-clock. Part A ~2-4M (the 257-classify is the bulk); Part B ~1M + the probe.
At subscription/toll-free terms, ~0 marginal $. Log this session's own tokens into the new ledger (dogfood).

## Governance / skills (R020, cross-hive)
- Cross-hive R014 instrumentation: PostWach BUILDS the capability; **Alpha Empress REGISTERS** the template v1.2
  bump + the hook/dashboard for cross-hive consistency.
- Skills to use: `update-config` (settings.json hook), `hooks-automation`, `systematic-literature-review`-style
  classification for the 257 sweep, `research-portfolio-optimizer` not needed here.
- Construct-taxonomy note: this is a HOOK + SCRIPT (+ optional slash-command), not a "plugin" (MCP server) --
  see `reference_construct_taxonomy` memory; a plugin proper would be over-engineering.

## Risks / notes
- Ephemeral data -> accept ESTIMATION; do not overclaim precision.
- Hook may not expose usage -> the B0 probe decides the design; do not build B1 before probing.
- settings.json lives in a OneDrive-synced `.claude/`; commit promptly; do not run two sessions on the same
  `.claude/` (INCIDENT-001 hazard).
- Use a FRESH session (`/clear`) to shed this conversation's large context before starting.

## Deliverables checklist
[ ] B0 probe result (what SessionEnd exposes)  [ ] auto-capture hook (or documented fallback)
[ ] dashboard script + rendered dashboard  [ ] calibrated cost model  [ ] 257-session classification
[ ] populated ledger (measured vs estimated flags)  [ ] backfill report w/ error bars
[ ] Alpha Empress governance-registration note
