# Cost Recovery — real four-component API usage (transcripts), as of 2026-07-16

**R016: (b) RECOVERED / MEASURED**, not modeled — parsed directly from the surviving session and
subagent transcript JSONL (`~/.claude/projects/<slug>/`), which carry the four components the API
meters: `input` (fresh), `cache_write` (1.25× in), `cache_read` (0.1× in), `output` (full out).
This is the ACCURATE cost basis — distinct from the legacy `subagent_tokens` proxy backfill, which
is a harness figure ~16× transcript output in the one checkable case (see the backfill report).

**Coverage caveat.** Transcripts survive only for **~2026-06-22 → 07-16** (main back to ~06-19).
Feb–mid-June has NO transcripts — not recoverable. Not every subagent transcript persists
(background / worktree-cleaned agents leave none), so subagent totals are a FLOOR. Dates are the
first in-transcript timestamp; dollars are NOTIONAL (blended rates; actual marginal ~0 on subscription).

## Totals (real API tokens)
| stream | files | input | cache_write | cache_read | output | notional $ |
|---|---|---|---|---|---|---|
| main | 39 | 8.42M | 216.68M | 7547.10M | 55.25M | $6,813 |
| subagent | 570 | 23.18M | 154.31M | 935.60M | 8.41M | $1,829 |
| **combined** | — | 31.60M | 370.99M | 8482.70M | 63.66M | **$8,642** |

## Cost by component (combined) — where the dollars actually are
| component | tokens | rate $/M | notional $ | % of $ |
|---|---|---|---|---|
| input | 31.60M | $5.20 | $164 | 2% |
| cache_write | 370.99M | $6.50 | $2,411 | 28% |
| cache_read | 8482.70M | $0.52 | $4,411 | 51% |
| output | 63.66M | $26.00 | $1,655 | 19% |

*Note the split: `cache_read` is the volume giant but cheap; `output` is small volume but the
cost driver. The output-only proxy saw neither the true volume nor the cache cost.*

## Per week — main
| week | files | input | cache_write | cache_read | output | notional $ |
|---|---|---|---|---|---|---|
| 2026-W28 | 12 | 3.37M | 112.33M | 3609.47M | 26.23M | $3,307 |
| 2026-W29 | 5 | 1.58M | 38.51M | 1184.95M | 9.71M | $1,127 |
| 2026-W27 | 11 | 1.54M | 36.43M | 1387.50M | 9.64M | $1,217 |
| 2026-W26 | 10 | 1.48M | 22.10M | 1118.79M | 8.24M | $947 |
| 2026-W25 | 1 | 0.45M | 7.31M | 246.38M | 1.42M | $215 |

## Per week — subagent
| week | files | input | cache_write | cache_read | output | notional $ |
|---|---|---|---|---|---|---|
| 2026-W28 | 209 | 9.22M | 72.59M | 427.05M | 4.54M | $860 |
| 2026-W29 | 301 | 11.27M | 62.49M | 399.59M | 3.14M | $754 |
| 2026-W27 | 36 | 1.83M | 11.60M | 72.63M | 0.50M | $136 |
| 2026-W26 | 24 | 0.86M | 7.64M | 36.33M | 0.24M | $79 |

