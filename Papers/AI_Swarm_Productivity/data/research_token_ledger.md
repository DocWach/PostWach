# Research Token Ledger (running)

*Renamed 2026-07-16 from `fable_cost_ledger.md` — this tracks ALL research token use across every hive,
not just the Fable derivation line.*

Companion to the R014 scorecards. Tracks the **running** token + cost total for the research portfolio,
which the per-session scorecards did not aggregate before 2026-07-16.

**Units — IMPORTANT (2026-07-16 finding).** The **backfill** unit is `subagent_tokens`, the harness figure
each scorecard recorded from task-notification `<usage>` blocks. Investigating whether it could be split,
we found it is **NOT verified to equal API output tokens**: in the one case checkable against a surviving
subagent transcript, the annotation (52,241) was **~16× the transcript's actual output (3,269)**, and the
ratio is not constant (search/context-heavy agents inflate it). So `subagent_tokens` is a **harness cost-
proxy, not output tokens** — the earlier "subagent output tokens" label was wrong; the magnitudes are
internally consistent but the unit is unverified. **The backfill therefore cannot be cleanly "split" into
components** — the four API components (`input` / `cache_write` 1.25× / `cache_read` 0.1×, huge volume /
`output`) live in the session/subagent **transcripts**, a DIFFERENT (and cleaner) measurement that only
survives for ~Jun 22–Jul 16. **Going-forward B1 auto-capture** (`.claude/helpers/cost-capture.mjs`) reads
those four real components from the transcript — that is the accurate path; the scorecard `subagent_tokens`
is a legacy proxy. Rates (per 1M): Opus 4.x $5/$25 in/out, Sonnet 4.6 $3/$15, Fable 5 $10/$50, Haiku 4.5 $1/$5.
Dollars are **notional** unless marked `measured` (CLI `/cost`); most work ran on subscription +
toll-free-Fable + Codex-on-sub, so **actual marginal dollars have been ~0**.

## Cumulative snapshot (as of 2026-07-16)
Two scopes — do not conflate:
- **Recent Fable research line (subset):** ~16.0M subagent tokens (this-conversation ~10.3M precise + prior ~6M est, ±2M).
- **FULL corpus backfill (all 260 scorecards as of 2026-07-16, all hives, Feb 25–Jul 16):**
  **~77.3M subagent-output tokens** (band 64–94M; 17.8M measured + 59.5M modeled). R016: **(a) MODELED
  ESTIMATE ±30–50%**, not recovery. LIVING figure — recomputed per run; shifts as new measured sessions
  accrue (this session's dogfood is now the 12th calibration point, nudging the per-agent median 80k→82k).
  Method + per-session appendix: `cost_backfill_report_2026-07-16.md`; live rollups: `cost_dashboard_2026-07-16.md`.
- **actual_marginal_dollars:** ~0  (subscription + toll-free-Fable pre-Jul-19 + Codex external)
- **notional_per_token_dollars_est:** ~$1,983 corpus-wide (**output-only**, ~$26/M blended 40/40/20
  Opus/Sonnet/Fable at corrected rates; band $1,660–2,415). NOTE: corrected 2026-07-16 from an earlier
  ~$1,005 that used $13/M — it understated Opus output at $15 instead of $25. Adding input+cache would
  raise this further (cache-read volume is large), but the backfill is output-only.
- **measured_dollars:** NOT yet captured -- run `/cost` and record going forward. **B1 auto-capture is LIVE**
  (SessionEnd → `.claude/helpers/cost-capture.mjs` parses the transcript, appends a per-session row with
  all four token components + subagent output, prints a visible confirmation).

## Recovered real cost (transcripts, ~2026-06-22 → 07-16) — (b) MEASURED
The **accurate** cost basis: real four-component API tokens parsed from 39 main + 570 subagent
transcripts (`cost_dashboard.py recovery` → `cost_recovery_report_2026-07-16.md`). Distinct from the
`subagent_tokens` proxy backfill below.

| stream | input | cache_write | cache_read | output | notional $ |
|---|---|---|---|---|---|
| main | 8.4M | 216.7M | 7,547.1M | 55.3M | $6,813 |
| subagent | 23.2M | 154.3M | 935.6M | 8.4M | $1,829 |
| **combined** | 31.6M | 371.0M | **8,482.7M** | 63.7M | **$8,642** |

**Where the dollars are:** cache_read 51% + cache_write 28% = **79% cache**, output only 19%, input 2%.
The output-only view saw ~$1,655 of a real ~$8,642. **Coverage:** transcripts survive ONLY ~Jun22–Jul16
(Feb–mid-June unrecoverable); subagent totals are a FLOOR (not every subagent transcript persists).
Actual marginal $ still ~0 (subscription + toll-free-Fable + Codex). Going-forward B1 captures this per session.

## Backfill estimation (all 258 scorecards, 2026-07-16) — MODELED (a), proxy unit
Calibration: 12 clean multi-agent measured points → **median 82k output tokens/agent**, IQR [65k, 105k].
Applied `agents_spawned × 82k` where tokens unrecorded; measured where present; 0-agent = ~0 subagent (main-loop out-of-unit).
All 260 typed by a 10-agent classifier sweep (reading scorecard + archive) + 2 late-arriving cards.

Every row is a MODELED ESTIMATE with a ±band (from the per-agent IQR), except the `measured` portion.
`mixed (Nm/Ne)` = N cards measured / N estimated. Auto-synced from `cost_backfill_report_2026-07-16.md` (as of 260 cards).

| Dimension | Cards | Est subagent tokens | Band | Flag |
|---|---|---|---|---|
| **TOTAL** | 260 (935 agents) | **77.3M** | 64.4M–93.9M | mixed (15m/245e) |
| hive: postwach | 214 | 68.6M | 57.6M–82.8M | mixed (14m/200e) |
| hive: gijoe | 21 | 4.7M | 3.7M–6.0M | estimated |
| hive: nnsa | 2 | 1.2M | 1.0M–1.6M | estimated |
| hive: sead | 6 | 0.9M | 0.7M–1.2M | estimated |
| hive: sysmlv2 | 8 | 0.4M | 0.3M–0.5M | mixed (2m/6e) |
| hive: lawsun/fort/roadmapping/finance/other | 9 | 1.5M | 1.2M–1.9M | estimated |
| type: derivation/Fable | 25 | 32.1M | 28.4M–37.0M | mixed (7m/18e) |
| type: paper/manuscript | 96 | 19.4M | 15.3M–24.6M | mixed (2m/94e) |
| type: ops/tooling | 88 | 16.3M | 13.0M–20.6M | mixed (1m/87e) |
| type: review/refverify | 36 | 5.8M | 4.8M–7.1M | mixed (4m/32e) |
| type: governance | 15 | 3.7M | 3.0M–4.7M | mixed (2m/13e) |

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


## Auto-captured sessions (B1, going-forward) <!-- AUTOCAPTURE:B1 -->
All four API-metered token components + subagent output, per session, parsed from the
session transcript at SessionEnd. `$` is NOTIONAL (blended rates; actual marginal ~0 on
subscription). input=fresh uncached, cache_write=1.25x in, cache_read=0.1x in, output=full out.

| session | date | input | cache_write | cache_read | output | subagent_out | notional $ |
|---|---|---|---|---|---|---|---|
| 65c8ff32 | session-end | 651443 | 23444924 | 780234759 | 6236091 | 1794251 | $770.29 |
