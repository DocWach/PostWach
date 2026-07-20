# Hive Empire Governance Revector — Requirements Traceability Matrix (RTM)

**Status:** v1.0 (baseline; SN ratified, SR INCOSE GtWR-conformant, lifecycle on ISO/IEC/IEEE 15288, DR-01/DR-02 closed, DR-03 deferred; 2026-07-14). See companion `decision-log.md`. R016 tag: **(a) research artifact / design spec** — not a demonstrated capability, not an integrated deliverable.
**Locus:** interim home in PostWach (CTO design role). Migrates into the canonical `hive-empire-governance` store once the apex exists.
**PROVENANCE:** produced by Opus 4.8 (claude-opus-4-8[1m]), vendor Anthropic, access mode Claude Code CLI, 2026-07-14, at the principal's direction (PostWach governance-revector session).

---

## 1. Purpose

Apply WySE (our own method) to the governance revector itself, so that every design decision, and later every V&V test, is traceable to a stated stakeholder need and therefore defensible. This is dogfooding: the governance system is the "system," and this document is its problem-space specification plus the traceability spine down to architecture and verification.

## 2. Nomenclature (ratified 2026-07-14)

| Tier | Outcomes side | Functions side |
|---|---|---|
| **Level** | LO | LF |
| **Specification type** (problem space) | PSO | PSF |
| **SE-domain subtype** (translation) | **SN** (stakeholder needs) | **SR** (system requirements) |

A level sets abstraction; a specification type is the problem-space construct at that level; the SE-domain subtype is that construct translated into systems-engineering practice. RTM rows carry SN / SR. `PSO` retained as the outcomes-side spec type (not renamed to PSN).

## 3. WySE grounding and discipline (source: `morphism-domain-reference` §6.1; rigor: asserted, corpus)

- **PSO** (problem space of outcomes): an outcome mapping `O: M × F → D`; outcomes are *needs*, the consequences of interactions, closed-system, not directly producible.
- **PSF** (problem space of functions): an unordered set of input/output-trajectory conditions, i.e. requirements, open-system.
- **Different in kind, not inter-derivable.** "A function cannot be decomposed into outcomes" (Salado 2021). Therefore **SR is NOT a decomposition of SN.** The SN→SR link is the ought-weld (Kannan acceptability): a requirement is listed because it is *necessary for a need to be acceptably met*, not because the need contains it.
- **Level stratification:** LO (outcomes) → LF (functions) → LA (architecture) → LC (coupled realization). Most decisions taken so far are LA/LC; this document back-fills LO/LF so that architecture is grounded rather than asserted.

## 4. LO / PSO — Stakeholder Needs (SN)

Grounded in principal statements during the 2026-07-14 session. Status `draft-grounded` = traced to a principal statement, pending explicit line-by-line ratification.

| ID | Stakeholder need (solution-free outcome) | Source (session) | Status |
|---|---|---|---|
| SN-1 | The governance corpus stays coherent as it grows; it does not accrete into contradiction or duplicate rules | opening "revector, not bolt-on"; revector seed | draft-grounded |
| SN-2 | Any governance fact is authoritative in exactly one place; no divergent copies to reconcile | seed (SSOT), ratified | draft-grounded |
| SN-3 | The status of any governed item is unambiguous to whoever meets it (active / retired / proposed) | seed (lifecycle) | draft-grounded |
| SN-4 | Governing the empire costs the principal little; no heavyweight ritual to do or review governance | "start-up and execution too burdensome" | draft-grounded |
| SN-5 | The principal stays the final authority; any decision can be set aside by him | "I should maintain override" | draft-grounded |
| SN-6 | Tailoring governance or capability to a hive does not spawn drifting copies | Lawsun transfer example | draft-grounded |
| SN-7 | Rules, ontology, and capabilities are governed as one coherent whole | "governance should not just be rules" | draft-grounded |
| SN-8 | Obsolete artifacts do not accumulate indefinitely; records preserved, waste collectable | "digital waste" | draft-grounded |
| SN-9 | Every governance decision, design, and V&V result is traceable to the need it serves | this session | draft-grounded |
| SN-10 | The governance approach is externalizable as an evidence-backed publishable artifact | harness-survey directive | draft-grounded |
| SN-11 | The empire is operable as a coherent whole from a single locus | the VS Code empty-folder story | draft-grounded |
| SN-12 | Relevant perspectives (security, governance) reach decisions by default; departures are visible | authority-model debate | draft-grounded |

## 5. LF / PSF — System Requirements (SR)

Scope: INCOSE GtWR applies to **SR only** (principal, 2026-07-14); SN remain WySE PSO and are not rewritten. Each SR is singular and in boilerplate form; singularity splits carry sub-IDs. Source ontology: `INCOSE_GtWR_requirements_ontology_extract.md`.

**Defined terms:** *governance item* = a rule, an ontology class, or a capability descriptor; *canonical governance store* = the single authoritative repository of governance items; *governance system* = the tooling operating over the store; *hive view* = a hive-local rendering generated from the store; *transfer* = a stored mapping of a governance item to a target perspective; *review lens* = a perspective (security, governance, ontology) applied to a transition; *dispensation* = a recorded sovereign override; *retention class* is one of append-only-record, durable, ephemeral, generated-rebuildable.

| ID | System requirement | Serves | Owner |
|---|---|---|---|
| SR-1 | The canonical governance store shall store each governance item with a lifecycle-status attribute. | SN-2,3,7 | PostWach / GI-JOE (ontology) |
| SR-2a | The governance system shall represent each governance item's lifecycle status as the set of ISO/IEC/IEEE 15288 stages the item currently occupies. | SN-3 | Alpha Empress |
| SR-2b | The governance system shall return a governance item's current lifecycle status when that item is read. | SN-3 | Alpha Empress |
| SR-2c | The governance system shall permit a governance item to re-enter a previously occupied stage. | SN-3 | Alpha Empress |
| SR-3a | The governance system shall generate each hive view by applying the registered transfers to the canonical governance items. | SN-2,6 | PostWach |
| SR-3b | The governance system shall reject any governance item authored in a hive view independently of the canonical governance store. | SN-2,6 | PostWach |
| SR-4a | The canonical governance store shall store each transfer with a source item, a target perspective, and a mapping. | SN-6 | GI-JOE (schema) |
| SR-4b | The governance system shall determine each transfer's mapping mechanism from the class of its source item. | SN-6 | PostWach (semantics) |
| SR-5 | When a governance transition is tagged security or governance, the governance system shall apply the corresponding review lens within the active session. | SN-4,12 | Fort Wachs / Alpha Empress |
| SR-6a | The governance system shall allow the principal to record a dispensation, with a reason, on any governance item. | SN-5,12 | PostWach |
| SR-6b | The governance system shall report the dispensation rate and the lens-skip rate. | SN-12 | PostWach |
| SR-7a | The governance system shall assign a retention class to each artifact. | SN-8 | PostWach |
| SR-7b | The governance system shall make each artifact of retention class ephemeral or generated-rebuildable available for collection. | SN-8 | PostWach |
| SR-7c | The governance system shall preserve each artifact of retention class append-only-record. | SN-8 | PostWach |
| SR-8a | The governance system shall record, for each decision, design element, and test, a traceability link to the stakeholder need or system requirement it serves. | SN-9 | PostWach |
| SR-8b | The governance system shall return the set of traceability links on query. | SN-9 | PostWach |
| SR-9 | The governance system shall load the canonical governance store when a session is opened at the apex locus. | SN-11 | PostWach |
| SR-10 | The governance system shall report each detected instance of the following: rule contradictions; orphaned items; ungated transitions. | SN-1 | Alpha Empress |
| SR-11 | The governance system shall export the governance model and its operational evidence in a citable form. | SN-10 | PostWach |

INCOSE conformance notes: singularity splits produced the sub-IDs (SR-2/4/6/7/8); combinators and parentheticals were removed via the defined term *governance item*; the former "without spinning up a separate hive" (old SR-5) is demoted to design rationale as an unverifiable negative. Ownership: ontology content of SR-1 and schema of SR-4a are **GI-JOE**-owned.

## 6. LA — Architecture decisions and traceability

Decisions taken in the 2026-07-14 session, each traced through SR to SN. `ratified` = principal-accepted this session; `open` = pending principal decision.

| LA ID | Architecture decision | Realizes | Serves | Status |
|---|---|---|---|---|
| LA-1 | Single canonical governance store: `hive-empire-governance` | SR-1 | SN-2,3,7 | ratified (locus); repo not yet created |
| LA-2 | Lifecycle = ISO/IEC/IEEE 15288 stages (Concept, Development, Production, Utilization, Support, Retirement), tailored to a governance item. NON-LINEAR: an item may occupy multiple stages at once and iterate/recurse (DevOps/Agile loop, e.g. Utilization to Development for revision to Production), not waterfall. ISO 10007 CM discipline wraps transitions; Blanchard & Fabrycky cited for designing retirement in. Former "mirrored" removed (a relationship, now a transfer edge LA-4) | SR-2a,2b,2c | SN-3 | ratified (DR-01) |
| LA-3 | Hive CLAUDE.md and capability sets are **generated views** over canonical | SR-3 | SN-2,6 | ratified |
| LA-4 | **Transfer** = one operator that moves a node along the Perspective axis, class-dispatched mechanism (Rule = constraint intersection; Skill = reframing; Agent = parameter binding) | SR-4 | SN-6 | ratified |
| LA-5 | Role-hives (Fort Wachs, Alpha Empress, GI-JOE) are **Perspectives / lenses** invoked in-session, not hives you spin up | SR-5 | SN-4,12 | ratified |
| LA-6 | **Authority model:** Sovereign (principal) + required in-session lens + dispensation-logged override; advisory-now, bindable-later (single edge parameter). Override = deontic dispensation over deny-monotone composition | SR-6 | SN-5,12 | ratified |
| LA-7 | Retention classes {append-only-record, durable, ephemeral, generated-rebuildable}; digital waste = ephemeral/rebuildable never collected. Policy in revector; sweep is a downstream task under the policy | SR-7 | SN-8 | ratified (policy) / sweep open |
| LA-8 | This RTM + the SN→SR→LA→LC→V&V chain | SR-8 | SN-9 | in progress |
| LA-9 | **Apex node:** empire-root folder made operable (thin `.claude/` + CLAUDE.md loading canonical) so a whole-empire session has something to stand on | SR-9 | SN-11 | design ratified; bootstrap order OPEN |
| LA-10 | Drift/incoherence reporting: contradictions, orphans, ungated-transition rate | SR-10 | SN-1 | open |
| LA-11 | Publishable systematic survey / taxonomy of AI harnesses; Hive Empire positioned against it | SR-11 | SN-10 | in progress (2 background scans complete, in `research/harness-survey/`) |
| LA-12 | GI-JOE dual role: authors the ontology INTO the canonical store (SSOT preserved) AND is the ontology + V&V review lens; sovereign-overridable via dispensation (same pattern as LA-5/LA-6). V&V-independence caveat (author = reviewer): compensate with an independent adversarial pass (cross-vendor two-red RBW) on high-risk items | SR-1,4,8 | SN-7,9,5 | ratified (role); independence control open |

**Defensibility check (2026-07-14):** every LA decision traces to an SR and an SN; no orphan decisions, and no SN is currently uncovered by an SR. Result is **provisional** until the SN set is ratified by the principal.

## 7. LC — Coupled realization (not yet specified)

Deferred. Will hold the concrete repo/coupling structure (canonical repo layout, generation/sync mechanism, in-session lens invocation, retention GC step). Gated on the ontology-locus and bootstrap-order decisions (Section 9).

## 8. V&V (not yet defined)

Each SR needs a verification method (SR-1…SR-11). Deliberately empty pending SR ratification; populating it is the next WySE step (the LF→verification support function). Placeholder so the gap is visible, not silently skipped.

## 9. Open items (as of 2026-07-14)

1. SN ratification — **DONE 2026-07-14** (SN-1…SN-12 ratified as good-enough working baseline). The "no orphan decisions" check is now on ratified needs.
2. **Ontology locus** — RESOLVED toward single apex repo: GI-JOE authors the ontology INTO the canonical store, sovereign-overridable (LA-12). Federated option retired unless principal reopens.
3. **Bootstrap order** — thin apex skeleton now vs finish schema first vs design-doc-only.
4. **V&V methods** — Section 8; each SR needs a verification method. Owner: GI-JOE (V&V lens), sovereign-overridable.
5. **LC realization** — Section 7.
6. **Cleanup sweep** — execute under the LA-7 retention policy once defined (`project_repo_cleanup_todo`).
7. **INCOSE GtWR ontology** — EXTRACTED 2026-07-14 (source: principal's own WRT-2516 BFO-grounded formalization of GtWR V4, 2023; `docs/governance-revector/INCOSE_GtWR_requirements_ontology_extract.md`; 9 entities, C1-C15 characteristics, 42 rules / 14 categories). Reuse-not-rebuild; GI-JOE inherits the BFO requirements ontology. RESOLVED 2026-07-14: (a) INCOSE scoped to SR only, SN remain WySE PSO (no Need class added); (b) SR-1…SR-11 rewritten into singular INCOSE-conformant boilerplate (Section 5, v0.2). REMAINING: (c) `refverify` the primary GtWR citation (Ryan and Wheatcraft, INCOSE-TP-2010-006-04) before any manuscript use.
8. **LO/LF mathematical formalization** — DEFERRED to next round (DR-03). The prose LO/LF spec (Sections 4-5) stands as good-enough for now; next round adds the PSO outcome-mapping math `(D, ⪯ betterness poset, D_acc)` and the PSF I/O-trajectory-condition math `{c_k}`. Poset-plus-confidence shape ties to the decision-analysis / confidence-distribution thread.
9. **V&V independence control** — scope/trigger for the compensating adversarial pass (cross-vendor two-red RBW) given GI-JOE author = reviewer (LA-12).

## 10. Maintenance

Update on: SN ratification; each open item in Section 9 closing; migration into the canonical store; any new SN/SR the principal states. Governance registration (Alpha Empress) and the ontology formalization (GI-JOE) are downstream owners per Section 5.
