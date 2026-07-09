# STIDS MTO (2026-05-23 revision) — Phase-3 Backfill Report

**Manuscript:** `02 My Outreach/2026 STIDS/Authoring_Mission_Threads_MTO_STIDS_Revised_2026-05-23.md`
**Gate:** `refcheck.py --include-pending --advisory`
**Run date:** 2026-06-04

## Counts

| Status | Count |
|--------|-------|
| Total bib entries | 24 |
| MATCH (approved.bib) | 22 |
| PENDING (in pending store, awaiting Byzantine verification) | 0 |
| MISS (in neither store) | 2 |

This manuscript drove the 2026-06-03 backfill of 20 STIDS-MTO entries into `approved.bib`, so MATCH coverage is near-complete by construction.

## MATCH (approved) — 22

| # | bibkey | Surname, Year |
|---|--------|---------------|
| 1 | `arp2015bfo` | Arp, 2015 |
| 2 | `beery2019mbseme` | Beery, 2019 |
| 3 | `brown2023setcovering` | Brown, 2023 |
| 4 | `ceusters2012iao` | Ceusters, 2012 |
| 5 | `dod2020meg` | Department, 2020 |
| 6 | `giles2019swarm` | Giles, 2019 |
| 8 | `omg2022uaf` | Object, 2022 |
| 9 | `raz2024mefoundations` | Raz, 2024 |
| 10 | `rudnicki2019cco` | Rudnicki, 2019 |
| 11 | `w3c2013provo` | W3C, 2013 |
| 12 | `shacl2017` | W3C, 2017 |
| 13 | `w3c2009skos` | W3C, 2009 |
| 14 | `allen1983temporal` | Allen, 1983 |
| 15 | `dachowicz2021mission` | Dachowicz, 2021 |
| 17 | `moreau2013provdm` | Moreau, 2013 |
| 18 | `odni2015icd203` | ODNI, 2015 |
| 19 | `maier1998sos` | Maier, 1998 |
| 20 | `singer2009sbd` | Singer, 2009 |
| 21 | `salmen2011stids` | Salmen, 2011 |
| 22 | `smith2013iaointel` | Smith, 2013 |
| 23 | `ruvnet2026ruflo` | rUv, 2026 |
| 24 | `w3c2012owl2syntax` | W3C, 2012 |

## PENDING — 0

(No PENDING-only matches; approved.bib already covers everything that has a pending counterpart.)

## MISS — 2 (must be created from scratch)

| # | Bib entry preview | Line |
|---|-------------------|------|
| 7 | International Organization for Standardization. (2020). *ISO/IEC 21838-2: Information technology, Top-level ontologies (TLO), Part 2: Basic Formal Ontology (BFO).* | 357 |
| 16 | Miles, A. & Bechhofer, S. (2009). *SKOS Reference.* W3C Recommendation. | 366 |

Note: approved.bib HAS `iso21838part2_2021` (the 2021 ISO BFO standard). The manuscript cites it under the 2020 draft year by ISO, with corporate-author "International Organization for Standardization." The matcher tries the (international, 2020) key, finds nothing. Either re-cite as 2021 with bibkey `iso21838part2_2021`, or add a (corporate-author = ISO, year = 2020) variant. Approved also has `w3c2009skos` (W3C as corporate author). Manuscript ref #16 cites "Miles, A. & Bechhofer, S. (2009)" — same document, different attribution style. Re-cite as W3C or alias.
