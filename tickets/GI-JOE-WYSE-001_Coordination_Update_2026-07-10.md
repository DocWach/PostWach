# GI-JOE → PostWach Coordination Handoff: STOIC-WySE Ontology

**Ticket:** GI-JOE-WYSE-001
**From:** GI-JOE (ontology engineering platform)
**To:** PostWach (CTO; SE-morphism domain authority; holder of the two in-flight dissertation-based publications)
**Date:** 2026-07-10
**Status:** DELIVERED to PostWach 2026-07-10 — updated handoff (supersedes the draft PostWach already reviewed); awaiting response on the three asks in §5
**Subject:** Independent formalization of the WySE verification metamodel — coordination, updated-tables request, and an independent-check offer

---

## 0. Update note (2026-07-10)

This is the **updated** handoff, superseding the earlier ticket PostWach already reviewed. Since that review, `stoic-wyse` v0.1.0 is **complete**: all four validation layers pass (reasoner, SHACL, 7 CQs), the **camera-ready pass is done** (OntoClean — no backbone violations; OQuaRE ≈ 4.3/5; OOPS! — no critical/important pitfalls), polish is applied (CC-BY-4.0 license, sibling disjointness for SR/VRPS and the two activities), and the files are **synced to GI-JOE** `ontologies/{domain,shapes,queries}/`. **Nothing in the metamodel changed** from what you reviewed — this update reports completion and reiterates the three asks in §5, which now gate **only** the parked acceptance layer.

## 1. Summary

GI-JOE has independently formalized the **WySE (Wymorian Systems Engineering) verification metamodel** as `stoic-wyse` v0.1.0, derived **solely from the dissertation §4 characterization** (Wach 2022, "Study of Equivalence in Systems Engineering within the Frame of Verification") and its Appendix A.1 glossary — **independently of the two in-flight publication drafts**.

The TBox, SHACL shapes, competency queries, and a structural worked-example ABox are complete and validate **GREEN across all layers**; OntoClean / OQuaRE / OOPS! all pass. Per R016 this is an **(a) research artifact**.

Because it was built independently of the live publications, it can serve as a **cross-check** on them. This ticket (a) reports what was built, (b) requests the current instance-table data needed to complete it, and (c) offers the ontology as a formal independent check.

---

## 2. What was built — and the modeling decisions PostWach should sanity-check

**Architecture:** BFO-only, consistent with `stoic-t3sd` / `stoic-devs`. All artifacts are GDC subclasses of `obo:BFO_0000031` (DD-01). **No CCO layer, no BFO roles** — the role framing was deliberately dropped in favour of the family's relational pattern (see decision log below).

**The seven artifacts:**
- `wyse:PSF` (Problem Space of Functions) and `wyse:SM` (System Model) — the two foundational rigid kinds, each with a `formalTuple`.
- `wyse:SR`, `wyse:VRPS` — subclasses of PSF (problem-space artifacts).
- `wyse:SD` = **defined class**: an SM that **adheres to SR** (§4.6, adherence-defined).
- `wyse:VM` = **defined class**: an SM **used in a verification activity** (§4.10, use-defined).
- `wyse:VMMC` — the morphic conditions on the SD–VM morphism.

**Key design decisions (please confirm these match the publications):**
1. **SM `represents` an EngineeredSystem** — a model is always a model *of* something (aboutness).
2. **SD is defined by adherence to SR; VM by use in a verification activity** — the design/verification distinction is relational, not a different kind.
3. **Design-as-VM works with no disjointness** — one SM (flashlight design ZA) is inferred as *both* an SD and a VM; the reasoner confirms this.
4. **VMMC and acceptability are defined over a reified SD–VM morphism.**
5. **Acceptance criterion (§4.11)** encoded as: a VM is acceptable iff **bound by a VRPS ∧ morphic to the SD ∧ adherent to the VMMC** (necessary conditions in OWL; the "within one verification activity" coupling is a SHACL shape).

## 3. Validation status (all GREEN)

- **Reasoner (OWL-RL):** consistent; design-as-VM entailment holds.
- **SHACL:** 0 violations (aboutness + morphism-structure shapes active on the ABox; acceptance shape dormant pending §5).
- **Competency queries (7):** all return their expected oracle counts, including CQ-W06 = 3 (the acceptance criterion).
- **OntoClean:** no backbone/rigidity violations.
- **OQuaRE:** ≈ 4.3 / 5.0.
- **OOPS!:** no critical/important pitfalls (minor advisories only).

## 4. The independent-check offer

The strongest form of the check: **feed our independently-built metamodel PostWach's current SD/VRPS/VMMC/morphism facts, let the acceptance shape *derive* the acceptable-VM set, and diff that against what the publications *assert*.** Agreement is strong cross-validation of the papers; disagreement localizes either a paper error or an ontology error. This independence is the asset — GI-JOE deliberately did **not** build from the live drafts.

## 5. What GI-JOE needs from PostWach (the asks)

1. **Definitional confirmation.** The principal's stated understanding is that **only the tables changed** (instance-level), with no definitional drift. Please confirm from the publication side that no *definitions* (the artifacts, the nine relationships, or the acceptance criterion) changed. If any did, it affects the TBox (Part 2), not just the parked ABox.
2. **Updated tables / canonical source.** Which is authoritative now — the dissertation-of-record or the updated publication tables? Please provide the current, **errata-clean** instance data for the parked facts:
   - VM→VMMC adherence (§4.10),
   - VM→VRPS binding (§4.11),
   - the VRPS+VMMC+SD combination / acceptability results (§4.11; status of the Tables 81–117 reconciliation flagged `[GATED]` in the §4 markdown).
3. **Independent-check form.** Do you want the ontology used as a formal check, and in what form — CQ results, a derived-vs-asserted acceptability diff, or a discrepancy report?

## 6. On response, GI-JOE will

- Unpark the acceptance-determining ABox facts (currently commented in `stoic-wyse.ttl`, Part VIII).
- Run the acceptance SHACL shape to derive the acceptable-VM set and produce the **derived-vs-asserted diff**.
- Elevate the artifact from R016 **(a) research artifact → (b) demonstrated capability** once the acceptance battery passes on reconciled data.

## 7. Artifacts (source of truth = STOIC repo)

- Ontology: `STOIC/ontologies/stoic-wyse.ttl` (TBox + structural ABox; acceptance facts parked in Part VIII)
- Shapes: `STOIC/shapes/stoic-wyse.shapes.ttl`
- Queries: `STOIC/queries/stoic-wyse/CQ-W01…W07.rq`
- Validation harness: `STOIC/scripts/validate-ontology.py`

---

## Decision log (why BFO-only, no roles/CCO)

- Initial framing "a VM is an SM with a role of VM" created a BFO tension (roles need an independent-continuant bearer; a model is a GDC). CCO's ICE layer resolved it, but `stoic-t3sd` demonstrates the family models designs/requirements/models/morphisms as **plain GDC subclasses with no roles and no CCO** — so the tension was framing-induced, not domain-required. WySE adopts the T3SD-consistent BFO-only pattern; CCO remains a deliberate future family-wide option if a downstream requirement (FM-provenance, SysML grounding) needs the ICE distinctions.

**PROVENANCE:** Drafted by Claude (Anthropic, Opus 4.8) under principal (Paul Wach) direction, 2026-07-10, per R018.
