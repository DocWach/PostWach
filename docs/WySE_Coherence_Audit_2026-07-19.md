# WySE Coherence Audit -- 2026-07-19 (Synthesis)

**Status:** (a) research artifact -- internal audit record; no manuscript or engine wiring is claimed here.

## PROVENANCE (R018)

- **Synthesis author:** Anthropic Claude, model `claude-opus-4-8[1m]` (Opus 4.8), Claude Code CLI, access mode: interactive subagent, 2026-07-19.
- **Upstream auditors (inputs to this synthesis):** two independent auditor passes delivered as structured JSON --
  - Auditor A ("dependency"): Fable dependency-graph + F2 witness re-run (Anthropic Claude, Opus/Sonnet class, Claude Code CLI).
  - Auditor B ("capstone"): CT-capstone + central-claim pass (Anthropic Claude, Opus/Sonnet class, Claude Code CLI).
- **Delegation note:** the F2 witness execution (`Fable_F2_combiner_classification_witness.py`, exit 0, 267 assertions, canonical SHA `70d70ddc...`) was run by Auditor A and is recorded here on Auditor A's attestation. This synthesis did NOT independently re-run the witness: the Fable candidate/witness/RBW files named below are not present in the PostWach working tree at synthesis time (glob confirmed empty for `Fable_*`, `RBW_F2*`, `RBW_C_v2*`, `F9D*`, `F9FE*`, `combiner_classification*`, `acceptance_region*`). This audit therefore rests on the two auditor attestations as evidence; the recommendation names which claims are attestation-backed vs. disk-verified.

---

## 1. Coherence Verdict: **coherent-with-gaps**

The Fable result graph is internally honest but not yet fully coherent. Of 21 CLOSED-HARDENED rows, exactly **two** carry a load-bearing dependency on a non-CLOSED node, and both point at the **same** node: **F2** (`Fable_F2_combiner_classification`, ledger verdict DERIVED-NO-RBW). That is a genuine coherence break (a CLOSED node resting on a non-CLOSED node), but it is **honestly fenced, not hidden**: `RBW_C_v2_2026-07-16` reached its CLOSED verdict precisely by rewording "DISCHARGED by F2" to "discharged MODULO the F2 candidate ... conditional on F2's promotion," and states outright that it does NOT promote F2. So the break is disclosed and conditionalized, which is why the verdict is *coherent-with-gaps* rather than *incoherent*.

The other standing gap is the **CT capstone**: there is a coherent CT thread but **no CLOSED-HARDENED unified/capstone object** -- all three capstone candidates (F9, F9FE, F9D) sit at REWORK. This is a gap, not an incoherence, because nothing CLOSED-HARDENED depends on the capstone (critically, the flagship does not -- see Section 3).

---

## 2. Dependency-Graph Findings + F2 Resolution (Auditor A)

**Graph shape.** 21 CLOSED-HARDENED rows (B, C, CPOSET-r2, D, E, F18, F19, F23, F24, F25, F29, F30R, F31, F32, F32GP-r2, F34-STRESS, F36, F38, F39, F39G, M1). Exactly two load-bearing edges cross from CLOSED into non-CLOSED, both into F2:

- **C depends on F2 heavily.** C's PO-C3 is "discharged MODULO the F2 candidate"; PO-C4 is "characterized by the F2 candidate ... not a closure"; and C's self-adversarial load-bearing delta item (1) ("the product is not thereby forced ... veto-preserving class is exactly {product, weighted product, min, geometric mean}") imports F2's T-F2-1/T-F2-3/T-F2-5 wholesale (Remark R1). This break is **MANAGED, not resolved**: `RBW_C_v2_2026-07-16` (CLOSED-HARDENED) explicitly does not promote F2 and closed by conditionalizing the discharge language. C's own witness passed (SHA `77892ea4...` intact); the fix is upstream at F2, not a C re-derive.
- **F18 depends on F2 narrowly.** F18 self-labels "Extends F2"; its headline instantiation T-F18-3 quantifies over F2's veto-preserving class. But F18's own core theorems T-F18-1/T-F18-2 (any scalarization into a total codomain collapses every genuine incomparability) are elementary and self-contained and **survive F2 being wrong**; only F18's sharp instantiation/framing rides on F2.

**F2 resolution (the pivot of the whole audit).** F2's candidate + witness are both on disk (per Auditor A); **no `RBW_F2` file exists** (glob confirmed). Auditor A ran `Fable_F2_combiner_classification_witness.py`:

- exit 0; **all 267 assertions pass**;
- canonical SHA `70d70ddcfd8fcedf9b54c20cd7cb0b921fc0a6ea935619a03c99c4adcd463a34` **byte-matches the ledger row**;
- the witness has real teeth: counterexamples CE-1..CE-6 separate the veto class exactly (e.g. CE-1 separates prod/min/geo at (1/2,1/8); CE-4 rejects SPROD(1,1)=1/2 at theta=3/4; CE-6 veto window shrinks in p), the transport lemma L-F2-2 verified on all 25 grid points, non-associativity of geomean / non-commutativity of wprod confirmed.

Therefore **F2 is SOUND and reproducible.** It does not need a Fable re-derive; it needs a **Red-Blue-White round** to convert DERIVED-NO-RBW into a real verdict. **Closing F2's RBW removes BOTH coherence breaks at once.**

**Cleared as non-breaks (checked and dismissed by Auditor A):**

- The F34-STRESS -> F39 -> F39G chain reuses F34-BENCH (REFUTED honest-negative) machinery/scenario/op-accounting verbatim but **not** its refuted WySE-win claim (F34-STRESS itself reports WIN=False, consistent with the negative). No CLOSED node depends on a refuted claim.
- F25/F24/F23/F29 "T-F2x" hits are **internal theorem numbering**, not F2-candidate dependencies.
- F29's "F10 style" reference is a not-started future-work PO, **not** a dependency on the REWORK F10.

---

## 3. CT-Capstone + Central-Claim Findings (Auditor B)

**Capstone (Q1): GAP -- no CLOSED-HARDENED unified object.** All three capstone candidates are REWORK:

- **F9** (`RBW_F9_2026-07-16`): four sustained majors (Boolean-not-V-valued, GB Set/Cat unreconciled, rhetorical D_s).
- **F9FE** (`RBW_F9FE_2026-07-19`, REWORK): axiom-1 relabels Diaconescu L-institutions; D2 no formal V-CAT typing; D3 sentence-leg enrichment atom-restricted while stated over all sentences; PO-F9FE-5 prior-art gate unpaid.
- **F9D** (`RBW_F9D_2026-07-19`, REWORK): the narrow salvage survives -- (D_s,D_b) as an enrichment with the independent weld D_b <= 2 D_s and a measured negation obstruction -- but delta item 1 is not non-owned and the base is mislabeled V-Cat where the witness's own base is the product quantale V x V.

The genuine, WHITE-verified contribution across F9FE/F9D is the **independent Lipschitz weld plus the negation obstruction**, witnessed only on a **finite positive-fragment Moore-machine / trajectory-footprint instance**, not the integrated general object. Every capstone candidate is (a) research artifact, unwired to engine/decision layer/manuscript.

**Two forms of the capstone, distinguished.**

- The **positioned-integration capstone as PROSE** ("harness Diaconescu + contribute the weld") **IS establishable** via the F9D rewording: both F9D and F9FE RBWs state the fixes (relabel axiom-1 as ceded instantiation; correct V-Cat -> V x V; restrict the atom-level claim) are **wording, not re-derivation**, over a sound witness. **BUT** the prose carry is **conditional on the unpaid prior-art survey (PO-F9D-4 / PO-F9FE-5)**, which is manuscript-blocking -- until refverify settles whether Diaconescu I(L) / Mardare-Panangaden-Plotkin / Bacci / Kurz already contain the bigraded weld or the (V x V)-Cat typing, the novelty claim is only conditional.
- A **WITNESSED CLOSED-HARDENED derivation of the INTEGRATED object** (compound sentences, full Wymorian z-tuple, general theorem rather than a finite instance) **does NOT yet exist** and requires a further Fable derive.

**Central claim (Q2): FULLY DISCHARGED, and independent of the capstone.** The flagship claim -- the record captures distinctions scalars conflate at a thermodynamic cost -- makes **no reference to F9*/enriched institution/capstone object**; it is built entirely on the record-vs-scalar spine, so the capstone GAP does not touch it. Every load-bearing lemma is CLOSED-HARDENED: F29 (Thm 2.1), F31 (Thm 2.2), F32 (Thm 2.3, via the round-3 correction `RBW_F32_correction_2026-07-17`; flagship states the corrected claim and names A0 as load-bearing), F36-r2 (Thm 3.4), F38-r2 (cost ledger), F39 (Result 4.1), F34-STRESS (Result 5.2). The REFUTED results (F34-BENCH delivered-win, M2/MOR, M3/transfer) are used **honestly as characterized negatives**; the delivered-win is explicitly not claimed. The F29 one-shot-vs-Shannon pigeonhole wording (RBW D2) is a MINOR item the flagship already discloses and scopes (Section 2.2).

---

## 4. Contradiction / Staleness Findings

- **No live contradiction** between the two auditors. They agree that F2 is the single root of the graph breaks (Auditor A) and that the flagship does not touch the capstone (Auditor B); the two gaps are orthogonal (F2 -> C/F18; capstone -> nothing CLOSED).
- **Managed-not-resolved staleness at C.** `RBW_C_v2_2026-07-16`'s CLOSED verdict is honest but leans on a still-unpromoted F2. This is stale relative to the fact that F2's witness now demonstrably passes; the RBW conditionalization predates a completed F2 adjudication. Not a defect, but the honest fence should be retired by closing F2, not left standing.
- **Disk/attestation gap (synthesis-level).** The Fable working files are not in the PostWach tree at synthesis time; this synthesis relies on auditor attestation for the witness run and SHA match. Flagged so the F2 RBW round can re-confirm the SHA against the live ledger as its first act.
- **Standing R019 reference debt (flagship).** Many `[PLACEHOLDER]` cites remain; the manuscript itself gates on this. It blocks **render**, not the mathematics -- distinct from the capstone prior-art survey, which blocks the **novelty claim**.

---

## 5. Definitive Split: Fable-Needed vs. Non-Fable

**Do NOT manufacture a Fable need to justify the cliff.** The honest answer for tonight: **zero Fable derives are required to bank the two current coherence breaks.** F2 is sound-and-witnessed (needs RBW, not derive); C and F18 need nothing (upstream fix). The only item that genuinely requires a *future* Fable derive is the integrated capstone OBJECT -- and that is **not on tonight's critical path**, because nothing CLOSED (including the flagship) depends on it.

### fableNeededItems (genuinely require a Fable DERIVE)

- **CAP-integrated-object** -- A witnessed CLOSED-HARDENED derivation of the *integrated* (D_s,D_b) capstone object (compound sentences, full Wymorian z-tuple, general theorem) does not exist; the surviving weld+obstruction is witnessed only on a finite positive-fragment instance. This is the only true Fable-derive need in the audit. **It is NOT required before the cliff** -- defer it.

### nonFableItems (resolvable by RBW / prose / refverify)

- **F2** -- RBW. Witness passes (exit 0, 267 assertions, SHA match, real CEs); needs a Red-Blue-White round to convert DERIVED-NO-RBW -> verdict. Removes both graph breaks.
- **C coherence break** -- RBW (upstream). Resolved automatically by closing F2's RBW; no C re-derive (C witness passed, SHA `77892ea4...`).
- **F18 coherence break** -- RBW (upstream). Same F2 RBW closes the framing dependency; F18's core survives regardless.
- **CT capstone as positioned-integration PROSE** -- prose + refverify. F9D/F9FE rewording (relabel axiom-1, V-Cat -> V x V, restrict atom-level claim) is wording over a sound witness; carry is conditional on the prior-art survey PO-F9D-4 / PO-F9FE-5 (refverify).
- **F9FE/F9D formal-typing defects** -- prose. Presentation/typing fixes over sound witnesses (V-CAT typing, atom-vs-all-sentences scope, V x V base label).
- **Flagship R019 reference debt** -- refverify. `[PLACEHOLDER]` cites block render, not math; manuscript already gates.

---

## 6. Recommendation

**Bank tonight (before the cliff):**

1. **Run the F2 Red-Blue-White round and close it.** This is the single highest-leverage move: it converts F2 from DERIVED-NO-RBW to a real verdict on an already-witnessed, SHA-matched, teeth-having result, and **removes BOTH coherence breaks (C and F18) at once**. RED should attack the veto-class boundary (CE-4/CE-6 windows) and the transport lemma; the witness already supplies the separating counterexamples, so this is an adjudication round, not new mathematics. First act of the round: re-confirm SHA `70d70ddc...` against the live ledger (closes the synthesis-level disk/attestation gap).
2. **After F2 closes, retire the honest fence at C.** Update the C discharge language from "MODULO the F2 candidate / conditional on F2's promotion" back to a plain discharge, and drop F18's conditional framing. The graph then reaches full coherence (0 CLOSED nodes resting on non-CLOSED nodes).

**Defer (NOT tonight):**

3. **The integrated CT-capstone Fable derive.** It is a real Fable need but off the critical path -- nothing CLOSED, including the flagship, depends on it. Do not force it into the cliff.
4. **The capstone positioned-integration prose + prior-art survey.** The prose carry exists via the F9D rewording, but do not assert the novelty claim until refverify pays PO-F9D-4 / PO-F9FE-5. Until then it is conditional; state it as (a) with the harness/weld framing, not as an established contribution.
5. **Flagship R019 reference debt** -- clear via refverify before render; it does not gate the mathematics tonight.

**Net:** the flagship central claim is fully discharged and untouched by both gaps; one RBW round tonight (F2) closes the entire coherence break; and no Fable derive is required before the cliff. The single genuine Fable-derive need (the integrated capstone object) is honestly deferred.

---

*R016 tag: this document and every artifact it references are (a) research artifacts unless a specific wiring is named. The flagship manuscript remains render-blocked by R019 reference debt; no integrated deliverable (c) is claimed.*
