# FROZEN SNAPSHOT — cited figure for the AI_Swarm_Productivity paper

**Do not regenerate this file.** It is the pinned, citeable corpus snapshot as of 2026-07-16
(260 scorecards, calibration median 82k output-tok/agent). The living `cost_dashboard.py` /
`cost_backfill_report_<date>.md` will drift as new sessions land; cite THIS file in the paper.

- **Cumulative subagent-output tokens (est):** 77.3M [64.4M – 93.9M]  (R016: (a) MODELED, ±30–50%)
- measured 17.8M + modeled 59.5M; 260 cards, 937 agents
- **Notional $ (output-only, $26/M blended):** $1,983 [$1,660 – $2,415]; actual marginal ~$0
- Frozen from: cost_backfill_report_2026-07-16.md (git-tracked)

---

# Cost Backfill Report — AI_Swarm_Productivity (261 scorecards)
*Generated 2026-07-16 by `cost_dashboard.py report`. Companion to `fable_cost_ledger.md`.*

**R016: (a) MODELED ESTIMATE — not recovery.** Raw per-session usage (task-notification
`usage` blocks, `/cost`) is ephemeral and gone for ~240 of 258 sessions. This report models
subagent output tokens from the fields the scorecards DO carry, calibrated on the 14 that
recorded tokens. Treat the aggregate as an order-of-magnitude (±30–50%), not accounting-grade.

## Method
1. **Unit:** subagent OUTPUT tokens (dominant cost driver; the ledger's unit).
2. **Calibrate:** on scorecards recording both `tokens_output` and `agents_spawned>=2`,
   compute output-tokens-per-agent. n=13 clean points; per-agent (k tokens): [26, 35, 46, 63, 65, 79, 80, 85, 100, 103, 105, 121, 131].
   → median **80k**/agent, IQR [63k, 103k].
3. **Classify:** all 258 sessions typed by a 10-agent classifier sweep reading each scorecard +
   matching archive (260/261 agent-labeled). Types: derivation/Fable, paper/manuscript,
   governance, ops/tooling, review/refverify.
4. **Apply:** measured where recorded; else `agents × median` with band `agents × [Q1,Q3]`;
   0-agent sessions → ~0 subagent tokens (main-loop-only; out of this unit).

## Aggregate
- **cumulative subagent-output tokens (est):** 76.27M  (band 63.85M–92.89M)
- measured (14 cards): 18.37M; modeled (244 cards): 57.91M
- total agents spawned: 949
- **notional $ (API-rate, $26/M out):** $1,983 (band $1,660–$2,415); **actual marginal $ ≈ 0**.

*Every token figure below is a MODELED ESTIMATE carrying a ±band (per-agent IQR), except rows
flagged `measured`; `mixed (Nm/Ne)` = N measured / N estimated cards in that row.*

### By hive
| hive | est tokens | band | flag | cards | agents |
|---|---|---|---|---|---|
| postwach | 67.79M | 57.16M–82.02M | mixed (15m/200e) | 215 | 841 |
| gijoe | 4.57M | 3.59M–5.88M | estimated | 21 | 57 |
| nnsa | 1.20M | 0.94M–1.55M | estimated | 2 | 15 |
| sead | 0.88M | 0.69M–1.14M | estimated | 6 | 11 |
| unknown | 0.72M | 0.57M–0.93M | estimated | 4 | 9 |
| fort | 0.40M | 0.32M–0.52M | estimated | 1 | 5 |
| sysmlv2 | 0.38M | 0.33M–0.45M | mixed (2m/6e) | 8 | 7 |
| lawsun | 0.32M | 0.25M–0.41M | estimated | 2 | 4 |
| roadmapping | 0.00M | — | estimated | 1 | 0 |
| finance | 0.00M | — | estimated | 1 | 0 |

### By session type
| type | est tokens | band | flag | cards | agents |
|---|---|---|---|---|---|
| derivation/Fable | 32.21M | 28.59M–37.07M | mixed (8m/18e) | 26 | 402 |
| paper/manuscript | 18.89M | 14.97M–24.14M | mixed (2m/94e) | 96 | 236 |
| ops/tooling | 15.92M | 12.75M–20.15M | mixed (1m/87e) | 88 | 195 |
| review/refverify | 5.64M | 4.66M–6.95M | mixed (4m/32e) | 36 | 71 |
| governance | 3.61M | 2.89M–4.58M | mixed (2m/13e) | 15 | 45 |

### By week
| week | est tokens | band | flag | cards | agents |
|---|---|---|---|---|---|
| 2026-W29 | 21.31M | 19.03M–24.38M | mixed (8m/9e) | 17 | 265 |
| 2026-W28 | 12.94M | 11.53M–14.83M | mixed (5m/22e) | 27 | 160 |
| 2026-W15 | 7.22M | 5.67M–9.29M | estimated | 14 | 90 |
| 2026-W14 | 4.57M | 3.59M–5.88M | estimated | 11 | 57 |
| 2026-W10 | 4.17M | 3.28M–5.37M | estimated | 17 | 52 |
| 2026-W13 | 3.13M | 2.46M–4.03M | estimated | 16 | 39 |
| 2026-W17 | 2.97M | 2.33M–3.82M | estimated | 15 | 37 |
| 2026-W27 | 2.69M | 2.24M–3.29M | mixed (2m/17e) | 19 | 34 |
| 2026-W11 | 2.57M | 2.02M–3.30M | estimated | 12 | 32 |
| 2026-W26 | 2.51M | 2.13M–3.01M | mixed (2m/15e) | 17 | 31 |
| 2026-W16 | 2.25M | 1.76M–2.89M | estimated | 8 | 28 |
| 2026-W21 | 1.92M | 1.51M–2.48M | estimated | 17 | 24 |
| 2026-W18 | 1.60M | 1.26M–2.06M | estimated | 5 | 20 |
| 2026-W23 | 1.44M | 1.13M–1.86M | estimated | 18 | 18 |
| 2026-W24 | 1.28M | 1.01M–1.65M | estimated | 15 | 16 |
| 2026-W22 | 1.04M | 0.82M–1.34M | estimated | 8 | 13 |
| 2026-W12 | 0.88M | 0.69M–1.14M | estimated | 6 | 11 |
| unknown | 0.72M | 0.57M–0.93M | estimated | 4 | 9 |
| 2026-W25 | 0.56M | 0.44M–0.72M | estimated | 5 | 7 |
| 2026-W09 | 0.40M | 0.32M–0.52M | estimated | 2 | 5 |
| 2026-W19 | 0.08M | 0.06M–0.10M | estimated | 8 | 1 |

## Fidelity / honest caveats
- All 14 calibration points are RECENT heavy sessions (Jun 23–Jul 16); early/lighter sessions
  (Feb–May) are extrapolated by agent-count and are the weakest rows. Aggregate ±30–50%.
- The per-agent median (80k) hides real variance (26k–131k). Small-N sessions dominated by one
  large agent, or many light agents, are individually unreliable; the AGGREGATE is the deliverable.
- 0-agent (main-loop-only) sessions contribute ~0 here. Their real main-loop tokens exist but are
  not in the scorecards; the cumulative is a SUBAGENT-token FLOOR for those sessions.
- Dollars are notional (subscription + toll-free-Fable + external Codex ⇒ ~0 actual marginal).

## Per-session appendix
| id | date | hive | type | agents | basis | est tokens | band |
|---|---|---|---|---|---|---|---|
| 2026-03-18-sysmlv2-01 | None | unknown | ops/tooling | 1 | E | 0.08M | 0.06M–0.10M |
| 2026-03-19-sysmlv2-01 | None | unknown | review/refverify | 0 | 0 | 0.00M | — |
| 2026-05-04-sysmlv2-01 | None | unknown | ops/tooling | 8 | E | 0.64M | 0.50M–0.83M |
| sysmlv2-debugging-retroactive | None | unknown | ops/tooling | 0 | 0 | 0.00M | — |
| 2026-02-25-postwach-01 | 2026-02-25 | postwach | ops/tooling | 4 | E | 0.32M | 0.25M–0.41M |
| 2026-02-25-postwach-02 | 2026-02-25 | postwach | ops/tooling | 1 | E | 0.08M | 0.06M–0.10M |
| 2026-03-02-nnsa-01 | 2026-03-02 | nnsa | paper/manuscript | 8 | E | 0.64M | 0.50M–0.83M |
| 2026-03-02-nnsa-02 | 2026-03-02 | nnsa | paper/manuscript | 7 | E | 0.56M | 0.44M–0.72M |
| 2026-03-03-postwach-01 | 2026-03-03 | postwach | governance | 7 | E | 0.56M | 0.44M–0.72M |
| 2026-03-03-postwach-02 | 2026-03-03 | postwach | ops/tooling | 3 | E | 0.24M | 0.19M–0.31M |
| 2026-03-04-postwach-01 | 2026-03-04 | postwach | ops/tooling | 0 | 0 | 0.00M | — |
| 2026-03-04-postwach-02 | 2026-03-04 | postwach | ops/tooling | 5 | E | 0.40M | 0.32M–0.52M |
| 2026-03-06-postwach-01 | 2026-03-06 | postwach | paper/manuscript | 0 | 0 | 0.00M | — |
| 2026-03-06-roadmapping-01 | 2026-03-06 | roadmapping | ops/tooling | 0 | 0 | 0.00M | — |
| 2026-03-07-gi-joe-01 | 2026-03-07 | gijoe | derivation/Fable | 0 | 0 | 0.00M | — |
| 2026-03-07-gi-joe-02 | 2026-03-07 | gijoe | paper/manuscript | 0 | 0 | 0.00M | — |
| 2026-03-07-postwach-01 | 2026-03-07 | postwach | paper/manuscript | 0 | 0 | 0.00M | — |
| 2026-03-07-postwach-02 | 2026-03-07 | postwach | ops/tooling | 0 | 0 | 0.00M | — |
| 2026-03-07-postwach-03 | 2026-03-07 | postwach | derivation/Fable | 3 | E | 0.24M | 0.19M–0.31M |
| 2026-03-07-postwach-04 | 2026-03-07 | postwach | paper/manuscript | 12 | E | 0.96M | 0.76M–1.24M |
| 2026-03-07-postwach-05 | 2026-03-07 | postwach | ops/tooling | 7 | E | 0.56M | 0.44M–0.72M |
| 2026-03-07-postwach-06 | 2026-03-07 | postwach | ops/tooling | 0 | 0 | 0.00M | — |
| 2026-03-07-postwach-07 | 2026-03-07 | postwach | paper/manuscript | 0 | 0 | 0.00M | — |
| 2026-03-09-gi-joe-01 | 2026-03-09 | gijoe | derivation/Fable | 8 | E | 0.64M | 0.50M–0.83M |
| 2026-03-09-postwach-02 | 2026-03-09 | postwach | paper/manuscript | 4 | E | 0.32M | 0.25M–0.41M |
| 2026-03-10-postwach-01 | 2026-03-10 | postwach | paper/manuscript | 0 | 0 | 0.00M | — |
| 2026-03-10-postwach-02 | 2026-03-10 | postwach | governance | 12 | E | 0.96M | 0.76M–1.24M |
| 2026-03-11-postwach-01 | 2026-03-11 | postwach | review/refverify | 0 | 0 | 0.00M | — |
| 2026-03-11-postwach-02 | 2026-03-11 | postwach | ops/tooling | 0 | 0 | 0.00M | — |
| 2026-03-12-postwach-02 | 2026-03-12 | postwach | review/refverify | 0 | 0 | 0.00M | — |
| 2026-03-12-postwach-03 | 2026-03-12 | postwach | ops/tooling | 4 | E | 0.32M | 0.25M–0.41M |
| 2026-03-13-postwach-01 | 2026-03-13 | postwach | paper/manuscript | 2 | E | 0.16M | 0.13M–0.21M |
| 2026-03-13-postwach-02 | 2026-03-13 | postwach | ops/tooling | 0 | 0 | 0.00M | — |
| 2026-03-13-postwach-03 | 2026-03-13 | postwach | ops/tooling | 0 | 0 | 0.00M | — |
| 2026-03-13-postwach-04 | 2026-03-13 | postwach | ops/tooling | 2 | E | 0.16M | 0.13M–0.21M |
| 2026-03-16-postwach-02 | 2026-03-16 | postwach | ops/tooling | 0 | 0 | 0.00M | — |
| 2026-03-17-gi-joe-01 | 2026-03-17 | gijoe | ops/tooling | 8 | E | 0.64M | 0.50M–0.83M |
| 2026-03-17-postwach-02 | 2026-03-17 | postwach | ops/tooling | 0 | 0 | 0.00M | — |
| 2026-03-17-postwach-03 | 2026-03-17 | postwach | ops/tooling | 1 | E | 0.08M | 0.06M–0.10M |
| 2026-03-17-postwach-04 | 2026-03-17 | postwach | ops/tooling | 1 | E | 0.08M | 0.06M–0.10M |
| 2026-03-20-postwach-01 | 2026-03-20 | postwach | ops/tooling | 1 | E | 0.08M | 0.06M–0.10M |
| 2026-03-23-postwach-01 | 2026-03-23 | postwach | paper/manuscript | 3 | E | 0.24M | 0.19M–0.31M |
| 2026-03-23-postwach-02 | 2026-03-23 | postwach | paper/manuscript | 4 | E | 0.32M | 0.25M–0.41M |
| 2026-03-24-postwach-01 | 2026-03-24 | postwach | paper/manuscript | 6 | E | 0.48M | 0.38M–0.62M |
| 2026-03-24-postwach-02 | 2026-03-24 | postwach | ops/tooling | 0 | 0 | 0.00M | — |
| 2026-03-24-postwach-03 | 2026-03-24 | postwach | ops/tooling | 0 | 0 | 0.00M | — |
| 2026-03-25-postwach-01 | 2026-03-25 | postwach | ops/tooling | 0 | 0 | 0.00M | — |
| 2026-03-25-postwach-02 | 2026-03-25 | postwach | review/refverify | 3 | E | 0.24M | 0.19M–0.31M |
| 2026-03-25-postwach-03 | 2026-03-25 | postwach | paper/manuscript | 0 | 0 | 0.00M | — |
| 2026-03-25-postwach-04 | 2026-03-25 | postwach | paper/manuscript | 0 | 0 | 0.00M | — |
| 2026-03-26-gi-joe-01 | 2026-03-26 | gijoe | ops/tooling | 0 | 0 | 0.00M | — |
| 2026-03-26-gi-joe-02 | 2026-03-26 | gijoe | review/refverify | 0 | 0 | 0.00M | — |
| 2026-03-26-postwach-01 | 2026-03-26 | postwach | governance | 4 | E | 0.32M | 0.25M–0.41M |
| 2026-03-26-postwach-02 | 2026-03-26 | postwach | governance | 8 | E | 0.64M | 0.50M–0.83M |
| 2026-03-27-gijoe-01 | 2026-03-27 | gijoe | paper/manuscript | 3 | E | 0.24M | 0.19M–0.31M |
| 2026-03-27-postwach-01 | 2026-03-27 | postwach | derivation/Fable | 4 | E | 0.32M | 0.25M–0.41M |
| 2026-03-27-postwach-02 | 2026-03-27 | postwach | derivation/Fable | 4 | E | 0.32M | 0.25M–0.41M |
| 2026-03-30-gijoe-01 | 2026-03-30 | gijoe | ops/tooling | 10 | E | 0.80M | 0.63M–1.03M |
| 2026-03-31-gi-joe-01 | 2026-03-31 | gijoe | ops/tooling | 5 | E | 0.40M | 0.32M–0.52M |
| 2026-03-31-gijoe-01 | 2026-03-31 | gijoe | ops/tooling | 1 | E | 0.08M | 0.06M–0.10M |
| 2026-03-31-postwach-01 | 2026-03-31 | postwach | paper/manuscript | 3 | E | 0.24M | 0.19M–0.31M |
| 2026-03-31-postwach-02 | 2026-03-31 | postwach | ops/tooling | 8 | E | 0.64M | 0.50M–0.83M |
| 2026-03-31-postwach-03 | 2026-03-31 | postwach | ops/tooling | 0 | 0 | 0.00M | — |
| 2026-03-31-postwach-04 | 2026-03-31 | postwach | paper/manuscript | 1 | E | 0.08M | 0.06M–0.10M |
| 2026-04-01-postwach-01 | 2026-04-01 | postwach | paper/manuscript | 1 | E | 0.08M | 0.06M–0.10M |
| 2026-04-02-postwach-02 | 2026-04-02 | postwach | ops/tooling | 3 | E | 0.24M | 0.19M–0.31M |
| 2026-04-03-postwach-02 | 2026-04-03 | postwach | derivation/Fable | 10 | E | 0.80M | 0.63M–1.03M |
| 2026-04-05-postwach-01 | 2026-04-05 | postwach | paper/manuscript | 15 | E | 1.20M | 0.94M–1.55M |
| 2026-04-06-postwach-01 | 2026-04-06 | postwach | review/refverify | 0 | 0 | 0.00M | — |
| 2026-04-07-postwach-01 | 2026-04-07 | postwach | paper/manuscript | 8 | E | 0.64M | 0.50M–0.83M |
| 2026-04-08-postwach-01 | 2026-04-08 | postwach | paper/manuscript | 0 | 0 | 0.00M | — |
| 2026-04-10-postwach-02 | 2026-04-10 | postwach | paper/manuscript | 7 | E | 0.56M | 0.44M–0.72M |
| 2026-04-10-postwach-03 | 2026-04-10 | postwach | ops/tooling | 10 | E | 0.80M | 0.63M–1.03M |
| 2026-04-10-sead-01 | 2026-04-10 | sead | ops/tooling | 3 | E | 0.24M | 0.19M–0.31M |
| 2026-04-11-postwach-01 | 2026-04-11 | postwach | ops/tooling | 3 | E | 0.24M | 0.19M–0.31M |
| 2026-04-11-postwach-02 | 2026-04-11 | postwach | paper/manuscript | 21 | E | 1.68M | 1.32M–2.17M |
| 2026-04-11-sead-01 | 2026-04-11 | sead | ops/tooling | 1 | E | 0.08M | 0.06M–0.10M |
| 2026-04-11-sead-02 | 2026-04-11 | sead | ops/tooling | 0 | 0 | 0.00M | — |
| 2026-04-12-gijoe-01 | 2026-04-12 | gijoe | ops/tooling | 8 | E | 0.64M | 0.50M–0.83M |
| 2026-04-12-postwach-01 | 2026-04-12 | postwach | ops/tooling | 24 | E | 1.92M | 1.51M–2.48M |
| 2026-04-12-postwach-02 | 2026-04-12 | postwach | paper/manuscript | 1 | E | 0.08M | 0.06M–0.10M |
| 2026-04-12-sead-01 | 2026-04-12 | sead | ops/tooling | 4 | E | 0.32M | 0.25M–0.41M |
| 2026-04-13-postwach-01 | 2026-04-13 | postwach | ops/tooling | 2 | E | 0.16M | 0.13M–0.21M |
| 2026-04-13-postwach-02 | 2026-04-13 | postwach | review/refverify | 0 | 0 | 0.00M | — |
| 2026-04-13-postwach-03 | 2026-04-13 | postwach | ops/tooling | 2 | E | 0.16M | 0.13M–0.21M |
| 2026-04-13-postwach-04 | 2026-04-13 | postwach | paper/manuscript | 11 | E | 0.88M | 0.69M–1.14M |
| 2026-04-14-postwach-01 | 2026-04-14 | postwach | ops/tooling | 4 | E | 0.32M | 0.25M–0.41M |
| 2026-04-14-postwach-02 | 2026-04-14 | postwach | paper/manuscript | 4 | E | 0.32M | 0.25M–0.41M |
| 2026-04-14-postwach-03 | 2026-04-14 | postwach | governance | 1 | E | 0.08M | 0.06M–0.10M |
| 2026-04-14-postwach-04 | 2026-04-14 | postwach | paper/manuscript | 4 | E | 0.32M | 0.25M–0.41M |
| 2026-04-20-postwach-01 | 2026-04-20 | postwach | ops/tooling | 0 | 0 | 0.00M | — |
| 2026-04-20-postwach-02 | 2026-04-20 | postwach | review/refverify | 15 | E | 1.20M | 0.94M–1.55M |
| 2026-04-21-postwach-01 | 2026-04-21 | postwach | review/refverify | 3 | E | 0.24M | 0.19M–0.31M |
| 2026-04-21-postwach-02 | 2026-04-21 | postwach | ops/tooling | 5 | E | 0.40M | 0.32M–0.52M |
| 2026-04-21-postwach-03 | 2026-04-21 | postwach | ops/tooling | 0 | 0 | 0.00M | — |
| 2026-04-21-postwach-04 | 2026-04-21 | postwach | paper/manuscript | 4 | E | 0.32M | 0.25M–0.41M |
| 2026-04-21-sead-01 | 2026-04-21 | sead | ops/tooling | 0 | 0 | 0.00M | — |
| 2026-04-22-postwach-01 | 2026-04-22 | postwach | paper/manuscript | 1 | E | 0.08M | 0.06M–0.10M |
| 2026-04-22-postwach-02 | 2026-04-22 | postwach | ops/tooling | 0 | 0 | 0.00M | — |
| 2026-04-22-postwach-03 | 2026-04-22 | postwach | review/refverify | 4 | E | 0.32M | 0.25M–0.41M |
| 2026-04-23-gi-joe-01 | 2026-04-23 | gijoe | ops/tooling | 0 | 0 | 0.00M | — |
| 2026-04-23-gi-joe-02 | 2026-04-23 | gijoe | review/refverify | 0 | 0 | 0.00M | — |
| 2026-04-23-postwach-01 | 2026-04-23 | postwach | ops/tooling | 1 | E | 0.08M | 0.06M–0.10M |
| 2026-04-23-postwach-02 | 2026-04-23 | postwach | governance | 0 | 0 | 0.00M | — |
| 2026-04-23-postwach-03 | 2026-04-23 | postwach | governance | 4 | E | 0.32M | 0.25M–0.41M |
| 2026-04-28-postwach-01 | 2026-04-28 | postwach | paper/manuscript | 0 | 0 | 0.00M | — |
| 2026-04-29-postwach-01 | 2026-04-29 | postwach | ops/tooling | 0 | 0 | 0.00M | — |
| 2026-04-29-postwach-02 | 2026-04-29 | postwach | review/refverify | 0 | 0 | 0.00M | — |
| 2026-04-29-postwach-03 | 2026-04-29 | postwach | ops/tooling | 0 | 0 | 0.00M | — |
| 2026-04-30-postwach-01 | 2026-04-30 | postwach | review/refverify | 20 | E | 1.60M | 1.26M–2.06M |
| 2026-05-04-postwach-01 | 2026-05-04 | postwach | paper/manuscript | 1 | E | 0.08M | 0.06M–0.10M |
| 2026-05-04-postwach-02 | 2026-05-04 | postwach | paper/manuscript | 0 | 0 | 0.00M | — |
| 2026-05-04-postwach-03 | 2026-05-04 | postwach | paper/manuscript | 0 | 0 | 0.00M | — |
| 2026-05-04-postwach-04 | 2026-05-04 | postwach | ops/tooling | 0 | 0 | 0.00M | — |
| 2026-05-05-postwach-01 | 2026-05-05 | postwach | paper/manuscript | 0 | 0 | 0.00M | — |
| 2026-05-06-postwach-01 | 2026-05-06 | postwach | paper/manuscript | 0 | 0 | 0.00M | — |
| 2026-05-07-postwach-01 | 2026-05-07 | postwach | paper/manuscript | 0 | 0 | 0.00M | — |
| 2026-05-08-sysmlv2-01 | 2026-05-08 | sysmlv2 | ops/tooling | 0 | 0 | 0.00M | — |
| 2026-05-18-postwach-01 | 2026-05-18 | postwach | paper/manuscript | 3 | E | 0.24M | 0.19M–0.31M |
| 2026-05-18-postwach-02 | 2026-05-18 | postwach | ops/tooling | 0 | 0 | 0.00M | — |
| 2026-05-18-postwach-03 | 2026-05-18 | postwach | ops/tooling | 0 | 0 | 0.00M | — |
| 2026-05-19-postwach-01 | 2026-05-19 | postwach | ops/tooling | 0 | 0 | 0.00M | — |
| 2026-05-19-postwach-02 | 2026-05-19 | postwach | review/refverify | 1 | E | 0.08M | 0.06M–0.10M |
| 2026-05-20-postwach-01 | 2026-05-20 | postwach | derivation/Fable | 11 | E | 0.88M | 0.69M–1.14M |
| 2026-05-21-gi-joe-01 | 2026-05-21 | gijoe | derivation/Fable | 0 | 0 | 0.00M | — |
| 2026-05-21-gi-joe-02 | 2026-05-21 | gijoe | governance | 0 | 0 | 0.00M | — |
| 2026-05-21-postwach-01 | 2026-05-21 | postwach | ops/tooling | 0 | 0 | 0.00M | — |
| 2026-05-21-postwach-02 | 2026-05-21 | postwach | ops/tooling | 0 | 0 | 0.00M | — |
| 2026-05-21-postwach-03 | 2026-05-21 | postwach | review/refverify | 0 | 0 | 0.00M | — |
| 2026-05-21-postwach-04 | 2026-05-21 | postwach | ops/tooling | 0 | 0 | 0.00M | — |
| 2026-05-21-postwach-05 | 2026-05-21 | postwach | ops/tooling | 4 | E | 0.32M | 0.25M–0.41M |
| 2026-05-22-postwach-01 | 2026-05-22 | postwach | paper/manuscript | 0 | 0 | 0.00M | — |
| 2026-05-23-gi-joe-01 | 2026-05-23 | gijoe | review/refverify | 4 | E | 0.32M | 0.25M–0.41M |
| 2026-05-23-postwach-01 | 2026-05-23 | postwach | paper/manuscript | 1 | E | 0.08M | 0.06M–0.10M |
| 2026-05-23-postwach-02 | 2026-05-23 | postwach | paper/manuscript | 0 | 0 | 0.00M | — |
| 2026-05-26-sead-01 | 2026-05-26 | sead | ops/tooling | 3 | E | 0.24M | 0.19M–0.31M |
| 2026-05-27-postwach-01 | 2026-05-27 | postwach | paper/manuscript | 0 | 0 | 0.00M | — |
| 2026-05-27-postwach-02 | 2026-05-27 | postwach | paper/manuscript | 0 | 0 | 0.00M | — |
| 2026-05-27-postwach-03 | 2026-05-27 | postwach | paper/manuscript | 2 | E | 0.16M | 0.13M–0.21M |
| 2026-05-27-postwach-04 | 2026-05-27 | postwach | ops/tooling | 5 | E | 0.40M | 0.32M–0.52M |
| 2026-05-28-postwach-01 | 2026-05-28 | postwach | paper/manuscript | 0 | 0 | 0.00M | — |
| 2026-05-28-postwach-02 | 2026-05-28 | postwach | review/refverify | 3 | E | 0.24M | 0.19M–0.31M |
| 2026-05-28-postwach-03 | 2026-05-28 | postwach | paper/manuscript | 0 | 0 | 0.00M | — |
| 2026-06-01-postwach-01 | 2026-06-01 | postwach | paper/manuscript | 0 | 0 | 0.00M | — |
| 2026-06-01-postwach-02 | 2026-06-01 | postwach | review/refverify | 1 | E | 0.08M | 0.06M–0.10M |
| 2026-06-01-postwach-03 | 2026-06-01 | postwach | ops/tooling | 3 | E | 0.24M | 0.19M–0.31M |
| 2026-06-01-postwach-04 | 2026-06-01 | postwach | paper/manuscript | 2 | E | 0.16M | 0.13M–0.21M |
| 2026-06-01-postwach-05 | 2026-06-01 | postwach | review/refverify | 0 | 0 | 0.00M | — |
| 2026-06-02-postwach-01 | 2026-06-02 | postwach | ops/tooling | 0 | 0 | 0.00M | — |
| 2026-06-02-postwach-02 | 2026-06-02 | postwach | review/refverify | 0 | 0 | 0.00M | — |
| 2026-06-02-postwach-03 | 2026-06-02 | postwach | paper/manuscript | 0 | 0 | 0.00M | — |
| 2026-06-02-postwach-04 | 2026-06-02 | postwach | paper/manuscript | 1 | E | 0.08M | 0.06M–0.10M |
| 2026-06-02-postwach-05 | 2026-06-02 | postwach | ops/tooling | 0 | 0 | 0.00M | — |
| 2026-06-03-postwach-02 | 2026-06-03 | postwach | ops/tooling | 3 | E | 0.24M | 0.19M–0.31M |
| 2026-06-04-postwach-01 | 2026-06-04 | postwach | paper/manuscript | 0 | 0 | 0.00M | — |
| 2026-06-04-postwach-02 | 2026-06-04 | postwach | paper/manuscript | 0 | 0 | 0.00M | — |
| 2026-06-04-postwach-03 | 2026-06-04 | postwach | review/refverify | 0 | 0 | 0.00M | — |
| 2026-06-04-postwach-04 | 2026-06-04 | postwach | paper/manuscript | 4 | E | 0.32M | 0.25M–0.41M |
| 2026-06-04-postwach-05 | 2026-06-04 | postwach | ops/tooling | 0 | 0 | 0.00M | — |
| 2026-06-05-postwach-01 | 2026-06-05 | postwach | paper/manuscript | 4 | E | 0.32M | 0.25M–0.41M |
| 2026-06-05-postwach-02 | 2026-06-05 | postwach | paper/manuscript | 0 | 0 | 0.00M | — |
| 2026-06-08-postwach-01 | 2026-06-08 | postwach | review/refverify | 0 | 0 | 0.00M | — |
| 2026-06-08-postwach-02 | 2026-06-08 | postwach | paper/manuscript | 0 | 0 | 0.00M | — |
| 2026-06-09-postwach-01 | 2026-06-09 | postwach | paper/manuscript | 0 | 0 | 0.00M | — |
| 2026-06-09-postwach-02 | 2026-06-09 | postwach | paper/manuscript | 5 | E | 0.40M | 0.32M–0.52M |
| 2026-06-09-postwach-03 | 2026-06-09 | postwach | paper/manuscript | 0 | 0 | 0.00M | — |
| 2026-06-09-postwach-04 | 2026-06-09 | postwach | paper/manuscript | 0 | 0 | 0.00M | — |
| 2026-06-10-postwach-01 | 2026-06-10 | postwach | paper/manuscript | 0 | 0 | 0.00M | — |
| 2026-06-10-postwach-02 | 2026-06-10 | postwach | ops/tooling | 0 | 0 | 0.00M | — |
| 2026-06-10-postwach-03 | 2026-06-10 | postwach | review/refverify | 0 | 0 | 0.00M | — |
| 2026-06-12-postwach-01 | 2026-06-12 | postwach | review/refverify | 0 | 0 | 0.00M | — |
| 2026-06-12-postwach-02 | 2026-06-12 | postwach | paper/manuscript | 1 | E | 0.08M | 0.06M–0.10M |
| 2026-06-13-postwach-01 | 2026-06-13 | postwach | paper/manuscript | 0 | 0 | 0.00M | — |
| 2026-06-13-postwach-02 | 2026-06-13 | postwach | paper/manuscript | 0 | 0 | 0.00M | — |
| 2026-06-13-postwach-03 | 2026-06-13 | postwach | paper/manuscript | 7 | E | 0.56M | 0.44M–0.72M |
| 2026-06-14-postwach-01 | 2026-06-14 | postwach | paper/manuscript | 3 | E | 0.24M | 0.19M–0.31M |
| 2026-06-15-postwach-01 | 2026-06-15 | postwach | paper/manuscript | 3 | E | 0.24M | 0.19M–0.31M |
| 2026-06-15-postwach-02 | 2026-06-15 | postwach | paper/manuscript | 4 | E | 0.32M | 0.25M–0.41M |
| 2026-06-16-postwach-01 | 2026-06-16 | postwach | paper/manuscript | 0 | 0 | 0.00M | — |
| 2026-06-16-postwach-02 | 2026-06-16 | postwach | paper/manuscript | 0 | 0 | 0.00M | — |
| 2026-06-20-postwach-01 | 2026-06-20 | postwach | paper/manuscript | 0 | 0 | 0.00M | — |
| 2026-06-22-finance-bro-01 | 2026-06-22 | finance | ops/tooling | 0 | 0 | 0.00M | — |
| 2026-06-22-postwach-01 | 2026-06-22 | postwach | paper/manuscript | 2 | E | 0.16M | 0.13M–0.21M |
| 2026-06-22-postwach-02 | 2026-06-22 | postwach | ops/tooling | 2 | E | 0.16M | 0.13M–0.21M |
| 2026-06-22-postwach-03 | 2026-06-22 | postwach | ops/tooling | 0 | 0 | 0.00M | — |
| 2026-06-22-postwach-04 | 2026-06-22 | postwach | paper/manuscript | 0 | 0 | 0.00M | — |
| 2026-06-22-postwach-05 | 2026-06-22 | postwach | paper/manuscript | 5 | E | 0.40M | 0.32M–0.52M |
| 2026-06-22-postwach-06 | 2026-06-22 | postwach | paper/manuscript | 1 | E | 0.08M | 0.06M–0.10M |
| 2026-06-23-postwach-02 | 2026-06-23 | postwach | paper/manuscript | 0 | 0 | 0.00M | — |
| 2026-06-23-postwach-03 | 2026-06-23 | postwach | paper/manuscript | 0 | 0 | 0.00M | — |
| 2026-06-23-sysmlv2-01 | 2026-06-23 | sysmlv2 | review/refverify | 4 | M | 0.14M | — |
| 2026-06-23-sysmlv2-02 | 2026-06-23 | sysmlv2 | ops/tooling | 0 | 0 | 0.00M | — |
| 2026-06-23-sysmlv2-03 | 2026-06-23 | sysmlv2 | governance | 0 | 0 | 0.00M | — |
| 2026-06-24-postwach-01 | 2026-06-24 | postwach | paper/manuscript | 0 | 0 | 0.00M | — |
| 2026-06-24-postwach-02 | 2026-06-24 | postwach | review/refverify | 0 | 0 | 0.00M | — |
| 2026-06-28-postwach-01 | 2026-06-28 | postwach | paper/manuscript | 2 | E | 0.16M | 0.13M–0.21M |
| 2026-06-28-postwach-02 | 2026-06-28 | postwach | paper/manuscript | 10 | E | 0.80M | 0.63M–1.03M |
| 2026-06-28-postwach-03 | 2026-06-28 | postwach | review/refverify | 5 | M | 0.60M | — |
| 2026-06-29-GI-JOE-01 | 2026-06-29 | gijoe | ops/tooling | 0 | 0 | 0.00M | — |
| 2026-06-29-GI-JOE-02 | 2026-06-29 | gijoe | review/refverify | 0 | 0 | 0.00M | — |
| 2026-06-29-postwach-01 | 2026-06-29 | postwach | ops/tooling | 0 | 0 | 0.00M | — |
| 2026-06-29-postwach-02 | 2026-06-29 | postwach | review/refverify | 0 | 0 | 0.00M | — |
| 2026-06-29-postwach-03 | 2026-06-29 | postwach | governance | 1 | E | 0.08M | 0.06M–0.10M |
| 2026-06-29-postwach-04 | 2026-06-29 | postwach | ops/tooling | 7 | E | 0.56M | 0.44M–0.72M |
| 2026-06-29-postwach-05 | 2026-06-29 | postwach | paper/manuscript | 10 | E | 0.80M | 0.63M–1.03M |
| 2026-06-29-postwach-06 | 2026-06-29 | postwach | review/refverify | 0 | 0 | 0.00M | — |
| 2026-06-29-postwach-07 | 2026-06-29 | postwach | ops/tooling | 0 | 0 | 0.00M | — |
| 2026-06-30-postwach-01 | 2026-06-30 | postwach | paper/manuscript | 7 | M | 0.44M | — |
| 2026-06-30-postwach-02 | 2026-06-30 | postwach | paper/manuscript | 1 | M | 0.17M | — |
| 2026-06-30-postwach-03 | 2026-06-30 | postwach | review/refverify | 0 | 0 | 0.00M | — |
| 2026-07-01-postwach-01 | 2026-07-01 | postwach | paper/manuscript | 0 | 0 | 0.00M | — |
| 2026-07-01-postwach-02 | 2026-07-01 | postwach | paper/manuscript | 2 | E | 0.16M | 0.13M–0.21M |
| 2026-07-01-sysmlv2-02 | 2026-07-01 | sysmlv2 | paper/manuscript | 0 | 0 | 0.00M | — |
| 2026-07-02-postwach-01 | 2026-07-02 | postwach | paper/manuscript | 0 | 0 | 0.00M | — |
| 2026-07-03-postwach-01 | 2026-07-03 | postwach | review/refverify | 3 | E | 0.24M | 0.19M–0.31M |
| 2026-07-03-postwach-02 | 2026-07-03 | postwach | paper/manuscript | 0 | 0 | 0.00M | — |
| 2026-07-03-sysmlv2-01 | 2026-07-03 | sysmlv2 | ops/tooling | 3 | E | 0.24M | 0.19M–0.31M |
| 2026-07-06-postwach-01 | 2026-07-06 | postwach | paper/manuscript | 1 | E | 0.08M | 0.06M–0.10M |
| 2026-07-07-postwach-01 | 2026-07-07 | postwach | review/refverify | 0 | 0 | 0.00M | — |
| 2026-07-07-postwach-03 | 2026-07-07 | postwach | derivation/Fable | 10 | E | 0.80M | 0.63M–1.03M |
| 2026-07-08-postwach-01 | 2026-07-08 | postwach | derivation/Fable | 2 | E | 0.16M | 0.13M–0.21M |
| 2026-07-08-postwach-02 | 2026-07-08 | postwach | derivation/Fable | 1 | M | 0.10M | — |
| 2026-07-08-postwach-03 | 2026-07-08 | postwach | derivation/Fable | 24 | M | 0.62M | — |
| 2026-07-08-postwach-04 | 2026-07-08 | postwach | derivation/Fable | 3 | E | 0.24M | 0.19M–0.31M |
| 2026-07-08-postwach-05 | 2026-07-08 | postwach | derivation/Fable | 4 | E | 0.32M | 0.25M–0.41M |
| 2026-07-09-postwach-01 | 2026-07-09 | postwach | derivation/Fable | 10 | E | 0.80M | 0.63M–1.03M |
| 2026-07-09-postwach-02 | 2026-07-09 | postwach | paper/manuscript | 8 | E | 0.64M | 0.50M–0.83M |
| 2026-07-09-postwach-03 | 2026-07-09 | postwach | review/refverify | 0 | 0 | 0.00M | — |
| 2026-07-09-postwach-04 | 2026-07-09 | postwach | derivation/Fable | 31 | M | 3.20M | — |
| 2026-07-10-fort-wachs-01 | 2026-07-10 | fort | governance | 5 | E | 0.40M | 0.32M–0.52M |
| 2026-07-10-gi-joe-01 | 2026-07-10 | gijoe | ops/tooling | 10 | E | 0.80M | 0.63M–1.03M |
| 2026-07-10-postwach-01 | 2026-07-10 | postwach | derivation/Fable | 14 | M | 1.40M | — |
| 2026-07-10-postwach-02 | 2026-07-10 | postwach | derivation/Fable | 8 | M | 1.05M | — |
| 2026-07-10-postwach-03 | 2026-07-10 | postwach | ops/tooling | 0 | 0 | 0.00M | — |
| 2026-07-10-postwach-04 | 2026-07-10 | postwach | paper/manuscript | 0 | 0 | 0.00M | — |
| 2026-07-10-postwach-05 | 2026-07-10 | postwach | governance | 0 | 0 | 0.00M | — |
| 2026-07-10-postwach-06 | 2026-07-10 | postwach | ops/tooling | 0 | 0 | 0.00M | — |
| 2026-07-10-postwach-07 | 2026-07-10 | postwach | ops/tooling | 0 | 0 | 0.00M | — |
| 2026-07-10-postwach-08 | 2026-07-10 | postwach | derivation/Fable | 0 | 0 | 0.00M | — |
| 2026-07-11-postwach-01 | 2026-07-11 | postwach | derivation/Fable | 11 | E | 0.88M | 0.69M–1.14M |
| 2026-07-11-postwach-02 | 2026-07-11 | postwach | ops/tooling | 0 | 0 | 0.00M | — |
| 2026-07-12-gijoe-01 | 2026-07-12 | gijoe | ops/tooling | 0 | 0 | 0.00M | — |
| 2026-07-12-postwach-01 | 2026-07-12 | postwach | derivation/Fable | 16 | E | 1.28M | 1.01M–1.65M |
| 2026-07-12-postwach-02 | 2026-07-12 | postwach | paper/manuscript | 2 | E | 0.16M | 0.13M–0.21M |
| 2026-07-13-lawsun-01 | 2026-07-13 | lawsun | governance | 0 | 0 | 0.00M | — |
| 2026-07-13-postwach-01 | 2026-07-13 | postwach | paper/manuscript | 10 | E | 0.80M | 0.63M–1.03M |
| 2026-07-13-postwach-02 | 2026-07-13 | postwach | derivation/Fable | 115 | E | 9.22M | 7.25M–11.87M |
| 2026-07-14-gijoe-01 | 2026-07-14 | gijoe | ops/tooling | 0 | 0 | 0.00M | — |
| 2026-07-14-lawsun-01 | 2026-07-14 | lawsun | ops/tooling | 4 | E | 0.32M | 0.25M–0.41M |
| 2026-07-14-postwach-02 | 2026-07-14 | postwach | derivation/Fable | 0 | 0 | 0.00M | — |
| 2026-07-14-postwach-03 | 2026-07-14 | postwach | governance | 3 | M | 0.24M | — |
| 2026-07-15-postwach-01 | 2026-07-15 | postwach | review/refverify | 5 | M | 0.32M | — |
| 2026-07-15-postwach-02 | 2026-07-15 | postwach | derivation/Fable | 30 | M | 2.37M | — |
| 2026-07-15-postwach-03 | 2026-07-15 | postwach | paper/manuscript | 4 | E | 0.32M | 0.25M–0.41M |
| 2026-07-15-postwach-04 | 2026-07-15 | postwach | paper/manuscript | 0 | 0 | 0.00M | — |
| 2026-07-15-sysmlv2-01 | 2026-07-15 | sysmlv2 | paper/manuscript | 0 | 0 | 0.00M | — |
| 2026-07-16-postwach-01 | 2026-07-16 | postwach | derivation/Fable | 71 | M | 6.00M | — |
| 2026-07-16-postwach-02 | 2026-07-16 | postwach | governance | 0 | M | 0.00M | — |
| 2026-07-16-postwach-03 | 2026-07-16 | postwach | ops/tooling | 11 | M | 1.16M | — |
| 2026-07-16-postwach-04 | 2026-07-16 | postwach | derivation/Fable | 12 | M | 0.56M | — |
| 2026-07-16-sysmlv2-01 | 2026-07-16 | sysmlv2 | review/refverify | 0 | M | 0.00M | — |

*basis: M=measured, E=estimated (agents×median), 0=zero-agent (main-loop only).*
