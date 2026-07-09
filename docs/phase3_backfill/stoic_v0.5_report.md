# STOIC v0.5 — Phase-3 Backfill Report

**Manuscript:** `02 My Outreach/2026_SERC_AI4SE_SE4AI/STOIC_HOS_ZynWorld/Wach_Philipbar_STOIC_HOS_ZynWorld_v0.5.md`
**Gate:** `refcheck.py --include-pending --advisory`
**Run date:** 2026-06-04

## Counts

| Status | Count |
|--------|-------|
| Total bib entries | 10 |
| MATCH (approved.bib) | 4 |
| PENDING (in pending store, awaiting Byzantine verification) | 0 |
| MISS (in neither store) | 6 |

STOIC is the densest MISS-rate manuscript: 6/10. The misses are mostly novel 2025-2026 AI-OS literature plus an unpublished INCOSE IS 2026 piece.

## MATCH (approved) — 4 (with caveats)

| # | Reported bibkey | Surname, Year | Caveat |
|---|-----------------|---------------|--------|
| 1 | `kamien2026mto` | Wach, 2026 (+1 candidate) | **FALSE POSITIVE.** Manuscript cites "P. Wach, A. Salado, B. Philipbar, *From Rules to Agentic Swarms*, INSIGHT 2026" — this is NOT `kamien2026mto`. The intended target is currently MISSING from approved.bib. Treat as MISS. |
| 6 | `wymore1993mbse` | Wymore, 1993 | Correct. |
| 7 | `zeigler2018tms` | Zeigler, 2018 | Correct. |
| 9 | `kamien2026mto` | Wach, 2026 (+1 candidate) | **MISMATCH.** Manuscript cites "P. Wach, B. Philipbar, J. Gregory, *Math-Based Data Structures...*, INCOSE Int. Symp., 2026". Correct bibkey is `wach2026meo`. Matcher returned the alphabetically-first Wach 2026 entry. |

**Net real MATCH:** 2 of 10 (#6, #7). After the alphabetical-tiebreaker false positive, the effective MATCH rate is 2/10, not 4/10.

## PENDING — 0

None of the missing STOIC references resolved against the EndNote-imported pending pool. (Wymore, Zeigler matched approved; the AI-OS literature is too new to be in the 2026-06-04 EndNote snapshot.)

## MISS — 6 (must be created from scratch, plus the two false-positive corrections)

| # | Bib entry preview | Line |
|---|-------------------|------|
| 1* | P. Wach, A. Salado, and B. Philipbar, "From Rules to Agentic Swarms: A Systems Engineering Journey Through the Evolution of AI," *INSIGHT*. 2026. | 62 |
| 2 | K. Mei, Z. Li, S. Xu, R. Ye, Y. Ge, and Y. Zhang, "AIOS: LLM Agent Operating System," in *Proc. Conf. on Language Modeling (COLM)*, 2025. arXiv:2403.16971. | 63 |
| 3 | Dell Technologies and Palantir Technologies, "Dell and Palantir Introduce an On-Premises AI Operating System," Dell Newsroom, May 2026. | 64 |
| 4 | NaasAI, "ABI: An Ontology-Grounded AI Operating System (BFO-Aligned)," GitHub repository, 2026. | 65 |
| 5 | Y. Kim, "OntoLoop OS: The Ontological Operating System for AI and Digital Civilization," SSRN Preprint, July 2025. | 66 |
| 8 | B. Philipbar and P. Wach, "DEVS-Based Agentic AI Swarms: System Entity Structure of Queens for Rapid Systems Development and Verification," in *Proc. INCOSE Int. Symp.*, 2026. | 69 |
| 10 | R. Cohen (rUv), "ruflo: The Leading Agent Meta-Harness for Claude," v3.7.0-alpha.14, GitHub, 2026. | 71 |

\* #1 is the false-positive from the MATCH table — gate let it through because of an unrelated `kamien2026mto` Wach-2026 entry. Treat as MISS for Phase-3 backfill purposes. Manuscript #10 likely intends approved entry `ruvnet2026ruflo` (rUv, 2026) but is cited as "R. Cohen (rUv)" — the matcher saw "Cohen 2026", missed. Re-cite as "rUv (R. Cohen)" or alias the bibkey under both surnames.
