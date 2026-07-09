# AICB v0.6 — Phase-3 Backfill Report

**Manuscript:** `02 My Outreach/2026_SERC_AI4SE_SE4AI/AICB/Wach_Wallk_AICircuitBreaker_Abstract_v0.6.md`
**Gate:** `refcheck.py --include-pending --advisory`
**Run date:** 2026-06-04

## Counts

| Status | Count |
|--------|-------|
| Total bib entries | 6 |
| MATCH (approved.bib) | 2 |
| PENDING (in pending store, awaiting Byzantine verification) | 1 |
| MISS (in neither store; must be created from scratch) | 3 |

## MATCH (approved) — 2

| # | bibkey | Surname, Year |
|---|--------|---------------|
| 2 | `kamien2026mto` | Wach, 2026 (matched via Wach as first author; +1 candidate `wach2026meo`) |
| 6 | `mcdermott2020ai4se` | McDermott, 2020 |

## PENDING — 1 (priority for Byzantine verification)

| # | bibkey | Surname, Year | Notes |
|---|--------|---------------|-------|
| 1 | `wach2022formalizing` | Wach, 2022 (+2 candidates) | Intended target is `wach2022pairing` (INSIGHT 25(4):65-70); matcher picked first alphabetical. Promote `wach2022pairing` (and decide on the two siblings). |

Pending candidates clustered at (Wach, 2022): `wach2022formalizing`, `wach2022initial`, `wach2022pairing` (the cited paper).

## MISS — 3 (must be created from scratch)

| # | Bib entry preview | Line |
|---|-------------------|------|
| 3 | JCGM 100:2008, *Evaluation of measurement data — Guide to the expression of uncertainty in measurement (GUM)*, Joint Committee for Guides in Metrology, BIPM, 2008. | 112 |
| 4 | Montgomery, D.C., *Introduction to Statistical Quality Control*, 8th ed., Wiley, 2019. | 113 |
| 5 | National Security Agency, *Cybersecurity Information Sheet: Advancing Zero Trust Maturity Throughout the Visibility and Analytics Pillar*, May 2024. | 114 |

Note: pending store has `montgomery2017design` (Design and Analysis of Experiments, 2017), NOT the 2019 SPC text the manuscript cites. Genuine create-from-scratch.
