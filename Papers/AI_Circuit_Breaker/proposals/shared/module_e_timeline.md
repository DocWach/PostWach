# Module E --- Base Milestone Template

**Shared module for all proposals. Updated 2026-03-23 for ECG-only phasing.**

---

## Base Timeline (24-Month Period of Performance)

| Phase | Months | Milestone | Deliverable |
|-------|--------|-----------|-------------|
| 1 | 1--4 | Theory + ECG ontology | Composition theorem formalized; cardiac domain ontology (impossible states, AHA/AAMI constraints) in OWL; ProbLog2 pipeline prototyped; STOIC alignment verified in EL++ |
| 2 | 4--8 | Single-task AR+ML prototype | Transformer encoder on PTB-XL; AR constraints in loss function; morphism quality instruments (D_s, D_b, d_cos) operational |
| 3 | 8--12 | Composition experiments | Two-task composition (classification + guideline compliance); composition theorem validated empirically; hallucination injection; SPC baseline |
| 4 | 12--15 | Phase 1 closeout | Full experimental results; Phase 1 paper; software + documentation |
| 5 | 16--21 | Phase 2: Deepened ECG pipeline | Second ML kind (Bayesian); AR-constrained training; three-task composition; domain-transfer cost analysis |
| 6 | 21--24 | Phase 2 closeout | Open-source release; final report; integration paper |

## Deliverable Summary

- **Publications:** 3--4 peer-reviewed papers (1 foundational theory, 1 ECG testbed validation, 1 composition + AR-constrained training, 1 integration capstone)
- **Software:** Open-source circuit breaker reference implementation with CBTO ontology, SHACL shapes, SPARQL CQ catalog, and ECG domain ontology
- **Data:** Annotated ECG testbed results with morphism quality labels (D_s, D_b, d_cos) for community benchmarking
- **Ontology:** CBTO v2.0 + ECG cardiac domain ontology, published as reusable semantic artifacts

## Key Decision Points

| Month | Decision | Criteria |
|-------|----------|----------|
| 4 | Proceed to prototype build | CBTO TBox passes OWL consistency check; ECG ontology impossible states encoded; ProbLog2 feasibility confirmed |
| 12 | Phase 1 graduation | Composition theorem validated (D_s_total >= max(D_s_i)); AUROC >= FDA-cleared SOA; d_cos hallucination detection TPR > 95% at 5% FPR |
| 21 | Phase 2 closeout prep | Three-task composition validated; AR-constrained training demonstrated; sample complexity < unconstrained SOA |

---

*Adjust total duration, budget allocation, and milestone timing per specific solicitation requirements. For 15-month Phase 1 programs (e.g., DARPA CLARA), Phases 1--4 map to Phase 1; Phases 5--6 map to Phase 2.*
