# Fable / Research-Workflow Cost Ledger (running)

Companion to the R014 scorecards. Tracks the **running** token + cost total for the Fable research line,
which the per-session scorecards did not aggregate before 2026-07-16.

**Units.** Primary = **subagent output tokens** (the dominant cost driver; read from each workflow/agent
task-notification `usage` block). Dollars are **derived estimates** unless marked `measured` (from the CLI
`/cost`). Billing regime is noted per row because most Fable-line work ran on subscription + the toll-free
Fable window + Codex-on-ChatGPT-sub, so **actual marginal dollars have been ~0** beyond the flat subscription.

## Cumulative snapshot (as of 2026-07-16)
Two scopes — do not conflate:
- **Recent Fable research line (subset):** ~16.0M subagent tokens (this-conversation ~10.3M precise + prior ~6M est, ±2M).
- **FULL corpus backfill (all 258 scorecards, all hives, Feb 25–Jul 16):** **~74.6M subagent-output tokens**
  (band 62–91M; 16.65M measured + 57.9M modeled). R016: **(a) MODELED ESTIMATE ±30–50%**, not recovery.
  Method + per-session appendix: `cost_backfill_report_2026-07-16.md`; live rollups: `cost_dashboard_2026-07-16.md`.
- **actual_marginal_dollars:** ~0  (subscription + toll-free-Fable pre-Jul-19 + Codex external)
- **notional_per_token_dollars_est:** ~$970 corpus-wide (~$13/M output, blended 40/40/20 Opus/Sonnet/Fable; band $808–1,185).
- **measured_dollars:** NOT yet captured -- run `/cost` and record going forward. Auto-capture prototyped
  (transcript-parse; SessionEnd probe armed) — see `.claude/helpers/cost-capture-probe.mjs`.

## Backfill estimation (all 258 scorecards, 2026-07-16) — MODELED (a)
Calibration: 11 clean multi-agent measured points → **median 80k output tokens/agent**, IQR [63k, 103k].
Applied `agents_spawned × 80k` where tokens unrecorded; measured where present; 0-agent = ~0 subagent (main-loop out-of-unit).
All 258 typed by a 10-agent classifier sweep (reading scorecard + archive).

Every row is a MODELED ESTIMATE with a ±band (from the per-agent IQR), except the `measured` portion.
`mixed (Nm/Ne)` = N cards measured / N estimated. Auto-synced from `cost_backfill_report_2026-07-16.md`.

| Dimension | Cards | Est subagent tokens | Band | Flag |
|---|---|---|---|---|
| **TOTAL** | 258 (926 agents) | **74.6M** | 62.1M–91.2M | mixed (14m/244e) |
| hive: postwach | 213 | 66.1M | 55.5M–80.3M | mixed (13m/200e) |
| hive: gijoe | 21 | 4.6M | 3.6M–5.9M | estimated |
| hive: nnsa | 2 | 1.2M | 0.9M–1.6M | estimated |
| hive: sead | 6 | 0.9M | 0.7M–1.1M | estimated |
| hive: sysmlv2 | 7 | 0.4M | 0.3M–0.5M | mixed (1m/6e) |
| hive: lawsun/fort/roadmapping/finance/other | 9 | 1.4M | 1.1M–1.9M | estimated |
| type: derivation/Fable | 25 | 31.7M | 28.0M–36.5M | mixed (7m/18e) |
| type: paper/manuscript | 96 | 18.9M | 15.0M–24.1M | mixed (2m/94e) |
| type: ops/tooling | 87 | 14.8M | 11.6M–19.0M | estimated |
| type: review/refverify | 35 | 5.6M | 4.7M–7.0M | mixed (3m/32e) |
| type: governance | 15 | 3.6M | 2.9M–4.6M | mixed (2m/13e) |

## This conversation (precise, from task-notification usage blocks)
| Session | Scope | Subagent tokens | Regime |
|---|---|---|---|
| 2026-07-15-postwach-01 | data-fusion inventory + agnosticism + taxonomy | 322,898 | subscription |
| 2026-07-15-postwach-02 | F18/F19/F20 derive + RBW v1/v2/v3 | 2,369,013 | sub + toll-free-Fable + Codex |
| 2026-07-16-postwach-01 | data-fusion completion + consolidation + citation audit + closes + A/F17 | ~6,570,000 | sub + toll-free-Fable + Codex |
| 2026-07-16 (B) | B dual-lens investigation | RUNNING (est ~1.0M) | sub + toll-free-Fable + Codex |
| 2026-07-16-postwach-03 | cost-instrumentation (this session): B0 probe + dashboard + 258 backfill | 1,159,258 subagent (measured) + ~0.20M main-loop snapshot | subscription |

### 2026-07-16-postwach-03 (this session, dogfood — precise from usage blocks)
| Component | Tokens | Basis |
|---|---|---|
| claude-code-guide agent (SessionEnd schema) | 52,241 | measured (task usage) |
| classifier sweep (10 agents x 258 scorecards) | 1,107,017 | measured (workflow usage) |
| **subagent subtotal** | **1,159,258** | measured |
| main-loop output (snapshot mid-session) | ~202,764 | measured, still growing (out-of-unit) |

### 2026-07-16-postwach-01 per-workflow breakdown
| Workflow | Tokens |
|---|---|
| tier2 F21/F22/F23 derive+RBW | 1,041,317 |
| tier2 v2 | 841,865 |
| refverify (13, verify) | 118,814 |
| refverify (promote 14) | 171,363 |
| catalog | 106,430 |
| consolidation F10/F24/F25 + A/B/C/F17 | 1,787,738 |
| citation audit (8) | 567,945 |
| v2 rework C/F25/F10/F24 | 1,027,908 |
| final close F25/F10 | 333,790 |
| close A/F17 | 573,862 |
| **subtotal** | **~6,571,032** |

## Prior sessions (2026-07-12..07-14, before this conversation) — ESTIMATE
| Span | Scope | Subagent tokens (est) | Basis |
|---|---|---|---|
| 2026-07-12..14 | A-E, F2, F17 derivations + RBW rounds v1-v9 | ~6,000,000 (±2M) | memory (v2 ~1.38M, v3 ~1.05M, A-D batch 494k, plus v4/v5/v6-v9 + repros) |

## Fable-cliff note (Jul 19)
Only the **Fable-model derivation agents** (~15-20% of tokens) become pay-per-use tolls after the cliff.
Opus/Sonnet (subscription) and Codex (external sub) are unaffected. So the incremental *toll* on remaining
work is on ~15-20% of tokens only.

## TODO (deferred per principal 2026-07-16 — "not right now, but a useful measure")
1. **Reconstruct prior sessions precisely** from the prior session archives + workflow/agent logs (replace the
   ~6M estimate with summed usage blocks).
2. **Capture measured `/cost` dollars** per session going forward (the derived estimates above are a ceiling,
   not a bill).
3. Fold the B dual-lens tokens in on completion.
