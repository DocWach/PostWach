# Session Archive: Scoping Review — Search & Classification

**Date:** February 16, 2026
**Session:** Scoping Review Phase 2 (Database Search Execution)
**Protocol:** Scoping_Review_Protocol.md v1.0

---

## Session Summary

Executed the complete database search phase of the scoping review protocol in two passes:

1. **Preliminary pass** — Web searches covering S1-S6 plus thematic searches. Produced initial extraction table (34 primary papers) and classification matrix.

2. **Formal database search pass** — 6 parallel research agents executed formal database queries across IEEE Xplore, arXiv, Scopus, Google Scholar, DTIC, NATO STO, RAND, MITRE, JHU APL. Results consolidated into updated deliverables.

## Deliverables

1. **Scoping_Review_Extraction_Table.md** — Consolidated extraction table with 82 primary corpus papers (P01-P82), 30 secondary corpus entries, 17 defense-specific NeSy papers (non-GT), and 14 institutional sources. P01-P34 have full extraction forms; P35-P82 in condensed format pending Phase 4 full-text review.

2. **Scoping_Review_Classification_Matrix.md** — NeSy Type (6 rows) x GT Concept (9 columns, including new Hypergame category) gap map with paper counts, key citations, maturity assessments, change tracking from preliminary, and prioritized research opportunities.

## Key Findings (Phase 2 Final)

### Matrix Summary
- **54 total matrix cells** (6 types x 9 concepts): 4 GREEN (7.4%), 26 YELLOW (48.1%), 24 RED (44.4%)
- Compared to preliminary: +3 GREEN, +10 YELLOW, -7 RED

### Major Revisions from Preliminary
- **Type 3 (Compilation) is no longer a complete gap** — 7 papers found (STLGame, LOGAN, CICERO, Rational Verification, Bayesian Inverse Games)
- **Correlated Equilibrium is no longer empty** — 3 papers across 3 NeSy types (NES, Exp3-IXrl, PRISM-games)
- **Type 4 (Neural_{Symbolic}) is the largest cluster** — 20 papers (up from 5), dominated by differentiable equilibrium solvers
- **Hypergame added as 9th GT concept** — 3 papers; models misperception/deception natively
- **Nash Equilibrium** is GREEN in 4 of 6 NeSy types (32 total papers)
- **Type 2 is the only type covering all 9 GT concepts** (23 papers)

### Defense-Specific Findings
- **Triple intersection** (NeSy + GT + Defense) remains sparse: ~6 papers (Zhu group dominates)
- **No paper combines all four elements**: NeSy + formal GT + formal verification + defense/wargaming
- **LLM + ontology/KG is the dominant NeSy paradigm in defense** — not classical NeSy (LTN, DeepProbLog)
- **17 defense NeSy papers lack explicit GT** — opportunity to add game-theoretic foundations
- **DARPA ANSR** ($6.4M, multi-performer) is the core NeSy-defense program

### Confirmed Gap (Review Contribution)
- **No existing survey covers the NeSy + GT intersection**
- The scoping review's 6x9 classification matrix is a novel contribution

## Search Execution Log

### Pass 1: Preliminary Web Searches

| Search | Status | Papers Found | Notes |
|---|---|---|---|
| S1: NeSy + GT | Complete | ~31 | Kwiatkowska NS-CSG cluster, differentiable economics |
| S2: NeSy + Defense/SE | Complete | ~31 | DARPA programs, Tambe security games |
| S3: GT + AI + Defense | Complete | ~48 | Broad; many neural-only (secondary corpus) |
| S4-S6: Triple + targeted | Complete | ~27 | Triple intersection sparse; 4 core papers |
| Foundational neural game solvers | Complete | ~30 | Secondary corpus Category A |
| AI wargaming + defense | Complete | ~42 | Grey literature, institutional reports |
| Existing surveys | Complete | ~30 | Confirmed no NeSy+GT survey exists |
| NPS/DTIC/grey | Complete | ~55 | 17 institutional categories |

### Pass 2: Formal Database Search Agents

| Agent | Search | Status | New Papers | Key Findings |
|---|---|---|---|---|
| S1 formal | Block A AND B | Complete | 47 total | Type 4 largest cluster (13 papers); 6 NeSy types populated |
| S2 formal | Block A AND C | Complete | 39 total | LLM+KG dominant in defense; 17 NeSy papers without GT |
| S4-S6 formal | Triple + targeted + verification | Complete | 28 new | Triple intersection ~6 papers; Zhu group dominates |
| Citation tracking | Key paper forward/backward | Complete | 15 new primary | G-CTR, Consensus Game, CICERO promoted, Gestalt NE, hypergames |
| Type 3 + CE | Specific gap searches | Rate-limited | Partial | S1 agent covered these adequately |
| Type 4 differentiable | Targeted search | Rate-limited | Partial | S1 agent covered these adequately |
| Defense + grey lit | Targeted search | Rate-limited | Partial | S2 agent covered defense; grey lit from prior session |

## Protocol Phase Status

| Phase | Target Date | Status |
|---|---|---|
| 1. Protocol finalization | Feb 2026 | COMPLETE |
| 2. Database searches | Mar 2026 | COMPLETE (82 primary papers, 30 secondary, 17 defense NeSy, 14 institutional) |
| 3. Title/abstract screening | Mar-Apr 2026 | PENDING |
| 4. Full-text review | Apr-May 2026 | PENDING |
| 5. Taxonomy construction | May 2026 | PRELIMINARY (6x9 matrix populated; Hypergame addition needs protocol amendment) |
| 6. Synthesis and drafting | May-Jun 2026 | PENDING |
| 7. Internal review | Jun-Jul 2026 | PENDING |
| 8. Submission | Jul 2026 | PENDING |

## Protocol Amendment Required

**Amendment 1:** Add Hypergame as 9th GT concept in Section 10.2 (Dimension 2: Game-Theoretic Solution Concept). Rationale: Formal search identified 3 papers and an active research line (Trencsenyi group, Thomas & Saad) combining hypergame theory with AI/neural methods. Hypergames model misaligned perceptions and nested beliefs — relevant to fog-of-war in defense applications.

## Next Steps

1. **Protocol amendment**: Add Hypergame to Section 10.2; update Section 10.3 matrix dimensions
2. **Title/abstract screening**: Pilot test on 30 papers (target Cohen's kappa >= 0.80)
3. **Full extraction forms**: Create detailed forms for P35-P82 during full-text review
4. **Deduplication**: Cross-reference P35-P82 against each other and P01-P34 for duplicates
5. **Full-text retrieval**: Obtain PDFs for all 82 primary papers
6. **Refine classifications**: Some Type 2/4/6 boundaries need resolution during full-text review
7. **Begin thematic synthesis** (5 themes per protocol Section 11.2)
