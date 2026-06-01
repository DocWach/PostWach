# Session Archive: 2026-03-13 PostWach-01

## Session Focus
DARPA CLARA (DARPA-PA-25-07-02) full proposal development: strategic alignment, domain selection, and proposal outline refinement.

## Key Decisions

1. **Option B framing adopted:** Morphism theory as the AR *foundation* for ML (AR built into ML), not a monitoring overlay. The Circuit Breaker emerges as a natural byproduct of the composition framework.

2. **Application domain: AI-enabled medical devices (FDA-regulated)**
   - Phase 1: ECG arrhythmia classification + clinical guideline alerting
   - Dataset: PTB-XL (21,837 ECGs, open-access) + MIT-BIH (secondary)
   - SOA baseline: FDA-cleared ECG algorithms (published sensitivity/specificity)
   - Key insight: FDA 510(k) "substantial equivalence" is literally a morphism question

3. **Phase 2 second domain: Telecom network management** (PI domain expertise, generalization demo)

4. **Amendment 01 (Mar 11, 2026):**
   - Proposal deadline extended to **April 17, 2026** (was Apr 10)
   - Program start: June 22, 2026 (was Jun 15)
   - "Bayesian LP-based Machine Learning" highlighted in ML kinds (validates ProbLog2 direction)

5. **Terminology:** "WySE ontology stack" is now **STOIC** ontology family

## Files Created
- `Papers/AI_Circuit_Breaker/proposals/01_darpa_clara/clara_abstract_v2.md` -- Option B reframed abstract
- `Papers/AI_Circuit_Breaker/proposals/01_darpa_clara/clara_proposal_outline.md` -- Full 10-section proposal outline

## Files Modified
- `Papers/AI_Circuit_Breaker/proposals/01_darpa_clara/clara_proposal_outline.md` -- Updated with medical device domain, Amendment 01 deadline, risk register, schedule, software stack, open items
- `memory/circuit-breaker-details.md` -- Updated deadline (Apr 17), program start (Jun 22), Bayesian LP highlight, STOIC terminology, next steps

## 6 Alignment Gaps Identified (from CLARA solicitation analysis)
1. Monitor vs Built-in (HIGH) -- resolved via Option B
2. Logical Explainability style (MED-HIGH) -- natural deduction, <=10 unfolding
3. Multiplicity tightness (MED) -- 2 AR kinds + 1 ML kind in Phase 1
4. Polynomial tractability for OWL DL (MED) -- EL++ profile constraint
5. SOA Benchmark (MED) -- resolved via medical device domain
6. AR-based ML Training (HIGH for Ph2) -- AR in the loss function, not just output filter

## Remaining Open Items
1. ProbLog2 integration feasibility prototype
2. EL++ profile verification for STOIC/CBTO
3. Budget detail (UA rates, subcontract, compute)
4. Parent PA formatting requirements (Section 5 from SAM.gov)
5. BAA portal registration (user handling)
6. ACA clause review
7. DARPA-SN-26-28 check
8. UA Sponsored Projects engagement (user handling)
9. Second ML kind decision (Bayesian methods vs. RL)

## SOA Benchmark Options Evaluated
| Option | Verdict |
|--------|---------|
| Telecom (synthetic) | Strong PI fit, weak benchmark infrastructure |
| Medical/Clinical (MIMIC) | Best benchmarks, domain mismatch |
| Medical Devices (FDA) | **Selected.** Strong benchmarks + regulatory alignment + "substantial equivalence as morphism" |
| Drug Discovery (MoleculeNet/TDC) | Best benchmark infrastructure overall, too far from PI background |
| Autonomous Systems Simulation | Too competitive, too far from PI |
| Hybrid (telecom primary + medical secondary) | Good but weaker than medical-primary |

## Timeline
- 35 days to deadline (Apr 17, 2026)
- Next priorities: begin prose drafting (Sections 2.1, 3.1, 3.2), ProbLog2 feasibility, budget
