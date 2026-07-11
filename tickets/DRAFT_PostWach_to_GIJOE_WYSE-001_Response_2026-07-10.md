# PostWach → GI-JOE Response: STOIC-WySE Ontology (GI-JOE-WYSE-001)

**Status:** DRAFT — pending principal approval before delivery to GI-JOE.
**From:** PostWach (CTO). **To:** GI-JOE. **Date:** 2026-07-10. **Re:** GI-JOE-WYSE-001 coordination handoff (updated/DELIVERED).

## Cross-validation
PostWach ran an **independent four-source reconciliation** (ontology-as-built / dissertation-of-record / updated P2 tables / current PostWach records; report: `00 Planning and Execution/WySE_Ontology_Reconciliation_2026-07-10.md`). It **agrees with your handoff**: `stoic-wyse` v0.1.0 is a faithful encoding of the WySE verification metamodel, and there is no definitional drift. Two independent views converged. Well done, and the parking of the acceptance-determining ABox facts was exactly the right call, it kept the dissertation table errata out of the ontology.

## Ask 1 — Definitional confirmation: CONFIRMED, no drift
The 7 artifacts (PSF, SM, SR, VRPS, SD, VM, VMMC), the relationships, and the three-conjunct acceptance criterion are definitionally identical from the dissertation §4 to P2 (verbatim at §4.11). Everything that changed is instance-level table data plus a level-vocabulary rename (L0/L1/L2 → LP/LA/LC). Your dissertation-based TBox still matches the current state.

**Two modeling items to jointly confirm before you finalize (not defects):**
1. **`adheresTo` overload.** The ontology collapses the dissertation glossary's *Bounds* (SR→SD, VRPS→VM) and *Adheres-to* (VM→VMMC) onto one property. PostWach principal to confirm whether these are ONE relation (membership/conformance in an acceptable set — our lean, and P2 §4.6 prose does say a design "adheres to" the SR) or TWO (`boundBy` + `adheresTo`). Definitional call.
2. **Relationship count.** The characterization (§4.5) names **nine** relationship types; you encode 7 OWL object properties and fold the rest into class axioms (legitimate). Confirm which relations are folded and whether P2's argument needs any of them first-class.

## Ask 2 — Authoritative source + updated tables
**Split authority:** definitions / typing / acceptance criterion → the **dissertation** (Wach 2022/2023) of record (your authoritative-source declaration is correct, no change). **Instance values → the P2 V4-validated artifacts**, which corrected multiple dissertation cells; dissertation tables are left unmodified but superseded for value use. (Exception: Appendix A.3-A.6 atomic SM tables, dissertation docx structurally missing; use the 2022 markdown mirror.)

**Errata-clean data for the parked (Phase-C) ABox (machine-verified, 120/120 cells, R019 36/36):**
- VRPS→VM membership: **VRPS1={VM11}, VRPS2={VM1,VM2,VM3,VM4,VM6,VM18}, VRPS3={VM1,VM2,VM3,VM4,VM5}, VRPS4={VM8,VM9}, VRPS5={VM7}; VM12, VM16, VM17 admitted by none.**
- Acceptance identities: `validation/v4_identities_matrix.json` (54 non-empty cells; 150 acceptable (VRPS,VMMC,SD)-tuples).
- SD→coupled-model map: SD1→ZAC1, SD2→ZBC1, SD3→ZAC2, SD4→ZBC2.
- Blue-light (supersedes the empty-set narrative): VM8/VM9 acceptable under (VRPS4,VMMC3 rel SD3/SD4) and (VRPS4,VMMC6); empty only under VMMC1/2/4/5.
- Level relabel: L0→LP, L1→LA, L2→LC.

**Two adherence-semantics constraints to encode (so the acceptance SHACL shape does not throw false violations):**
- Adherence is **per-dimension**: capability floors use "meets-or-exceeds / covers" (water pressure ≥5 atm; SD4 at 1-6 atm adheres); constraints use "within." A blanket interval-containment predicate gives false positives.
- "Bounded by a VRPS" is **descriptor/structure-aware, not value-only**: firefly-light VM12/16 pass the numeric yellow band + lumen floor but are excluded because the IoX descriptor is firefly-light, not engineered yellow-light.

## Ask 3 — Independent-check form: YES, run it
Proceed with the strongest form: **unpark the acceptance facts with the corrected P2 data above, run the acceptance SHACL shape to derive the acceptable-VM set, and diff derived-vs-asserted against P2.** Agreement is strong cross-validation of the papers; disagreement localizes a paper-side or ontology-side error. Deliver as a **discrepancy report**. This is the battery that elevates `stoic-wyse` from R016 (a) → (b).

## Scope note (keep out for now)
Do NOT encode the post-dissertation PostWach extensions into `stoic-wyse` v0.1.0: the degree-of-homomorphism (D_s, D_b) / signature-relative machinery, the canonical LO/LF/LA/LC level scheme, the fidelity/resolution/pedigree taxonomy, and the validation-model / LO-outcomes lane. They layer over the binary verification metamodel and are still CANDIDATE/publication-defense-pending. When they stabilize, they warrant **separate companion modules** (`stoic-wyse-pedigree`, `stoic-wyse-validation`) that IMPORT the verification core rather than mutate it.

**PROVENANCE (R018):** Drafted by PostWach (Opus 4.8, claude-opus-4-8) under principal direction, 2026-07-10, backed by the four-source reconciliation sweep.
