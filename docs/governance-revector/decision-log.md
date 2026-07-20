# Hive Empire Governance Revector — Decision Log (ADR-lite)

**Status:** v1.0, 2026-07-14. Companion to `governance-revector-RTM.md`. R016 tag: **(a) research artifact / design record**.
**PROVENANCE:** produced by Opus 4.8 (claude-opus-4-8[1m]), vendor Anthropic, access mode Claude Code CLI, 2026-07-14, at the principal's direction (PostWach governance-revector session).

Each record: Context / Decision / Alternatives rejected / Rationale / Consequences / Traces / Status. DR-01 to DR-03 are the decisions worked through explicitly at session end; DR-04 to DR-12 were ratified earlier in the same session and are recorded here for completeness.

---

## DR-01 — Governance-item lifecycle on ISO/IEC/IEEE 15288 (non-linear)

- **Context:** the working lifecycle was a bespoke {proposed, active, mirrored, retired}; "mirrored" read wrong and the set was not standard.
- **Decision:** adopt the ISO/IEC/IEEE 15288 life-cycle stages that the INCOSE SE Handbook uses (Concept, Development, Production, Utilization, Support, Retirement), tailored to a governance item. The lifecycle is NON-LINEAR: an item may occupy several stages at once and may iterate/recurse (DevOps/Agile loop), not waterfall; status is the set of occupied stages, and re-entry is allowed. Wrap transitions in ISO 10007 CM discipline (baseline = Utilization/in-force, change control = the lens gates, status accounting = this log + RTM, audit = SR-10). Cite Blanchard & Fabrycky for designing retirement in. Remove "mirrored"; tightening/specialization is a transfer edge (DR-06), not a state.
- **Alternatives rejected:** keep bespoke {proposed, active, retired} (less defensible than a standard); Draft/Active/Deprecated/Retired deprecation convention (not the SE standard the shop uses); full Blanchard & Fabrycky stages (over-granular on design for a rule-item); ISO 10007 as a *state* source (it defines CM process, not states); keep "mirrored" (a relationship masquerading as a state).
- **Rationale:** SE-standard grounding and defensibility, consistent with adopting INCOSE for SR; the stages map cleanly (Production = generation-to-hive-views, SR-3a); real systems occupy multiple phases and iterate.
- **Consequences:** RTM LA-2, SR-2a/2b/2c updated; status is a set, re-entry permitted; ISO 10007 and 15288 citations need `refverify` before manuscript use.
- **Traces:** SN-3; SR-2a/2b/2c; LA-2, LA-4.
- **Status:** RATIFIED 2026-07-14.

## DR-02 — Ontology locus: single canonical repo, GI-JOE authors in

- **Context:** fork between a single apex repo and a federated store keyed by owner.
- **Decision:** the ontology lives in the single canonical `hive-empire-governance` store; GI-JOE is its author and its ontology + V&V review lens; sovereign-overridable via dispensation.
- **Alternatives rejected:** federated (ontology stays in GI-JOE's repo, canonical references it) — breaks SN-2 single-source-of-truth. Ownership is not locus: GI-JOE owns and authors, canonical hosts.
- **Rationale:** SN-2; a single authoritative location is the whole point of the revector.
- **Consequences:** GI-JOE commits across a repo boundary; author = reviewer independence gap, compensated by the cross-vendor two-red RBW control (open item 9).
- **Traces:** SN-2,7,9; SR-1, SR-4a; LA-1, LA-12.
- **Status:** RATIFIED 2026-07-14.

## DR-03 — LO/LF mathematical formalization (deferred)

- **Context:** the LO/LF problem spaces were drafted in prose plus a sketch of the math.
- **Decision:** DEFER the mathematical formalism to a next round; the prose LO/LF spec stands as good-enough for now. Next round adds the PSO outcome-mapping math (outcome space `D`, betterness poset `⪯`, acceptance down-set, antichain frontier, no scalar governance score) and the PSF I/O-trajectory-condition math `{c_k}`, with the necessity-plus-confidence weld.
- **Rationale:** the prose is sufficient to carry the design decisions now; the math is a rigor upgrade, not a blocker.
- **Consequences:** RTM open item 8 marked deferred; the WySE decision-plane figure already depicts the intended acceptability structure.
- **Traces:** all SN via `D_acc`; all SR via `∩ c_k`.
- **Status:** DEFERRED 2026-07-14.

## DR-04 — Lead formalism: separate authority from behavior-envelope

- **Decision:** the revector's engineering runs on the authority/decision-rights formalism (claims lattice, ruflo ADR-010); WySE / behavior-envelope stays the research thread for proving composition properties. The two reconverge only at the transfer primitive, watched so WySE does not slip onto the critical path.
- **Alternatives rejected:** WySE/envelope leads now (unproven for governance, expensive); authority-only with envelope shelved (loses the research line).
- **Traces:** LA-4, LA-6. **Status:** RATIFIED.

## DR-05 — Hive rulebooks are generated views

- **Decision:** the canonical store is the only authored source; each hive CLAUDE.md and capability set is generated from it (global items plus that hive's transfers). Hand-editing a hive rulebook is disallowed.
- **Alternatives rejected:** authored + mirror-map (drift persists); canonical-only via MCP with no local rulebooks (loses human-readable local view).
- **Traces:** SN-2,6; SR-3a/3b; LA-3. **Status:** RATIFIED.

## DR-06 — Transfer operator (one operator, class-dispatched)

- **Decision:** specialization to a hive is a single `transfer` operator that moves a governed node along the Perspective axis; the mechanism is dispatched by the source class (Rule = constraint intersection; Skill = reframing; Agent = parameter/persona binding). Composition-by-transfer replaces duplication everywhere (rules, skills, agents), which also reduces storage waste.
- **Alternatives rejected:** a typed family of unrelated operators (misses the scale-invariance); per-hive forking (the accretion/dilution disease).
- **Traces:** SN-6; SR-4a/4b; LA-4. **Status:** RATIFIED. R016 note: the transfer pattern is demonstrated once (Lawsun legal), a design bet not proven infrastructure.

## DR-07 — Authority model: sovereign + in-session lens + dispensation

- **Decision:** the principal is sovereign; role-hives (Fort Wachs security, Alpha Empress governance, GI-JOE ontology/V&V) are required in-session review lenses on tagged transitions, not separate hives to spin up. Override is legal and logged as a dispensation; enforcement strength is one edge parameter (advisory-now, bindable-later). Formally: deny-monotone composition plus a sovereign dispensation (a deontic contrary-to-duty operator), which also fills the surveyed GAP-1.
- **Alternatives rejected:** binding delegation / true separation of duties (contradicts single-principal reality and how the principal works); sovereign-only advisory-optional (decays to zero use, loses the drift signal). The chosen model inverts the default so review is automatic and free while override is the deliberate, recorded act.
- **Traces:** SN-4,5,12; SR-5, SR-6a/6b; LA-5, LA-6. **Status:** RATIFIED.

## DR-08 — Retention classes and digital-waste collection

- **Decision:** every artifact carries a retention class {append-only-record, durable, ephemeral, generated-rebuildable}. Digital waste = ephemeral/rebuildable items never collected. The retention POLICY is part of the revector; the actual cleanup SWEEP is a downstream task executed under the policy. Records (e.g. scorecards, session archives under R014) are preserved.
- **Alternatives rejected:** treat cleanup as a separate ad hoc effort (recreates the accretion problem); eyeball-delete by file (risks destroying provenance records).
- **Traces:** SN-8; SR-7a/7b/7c; LA-7. **Status:** RATIFIED (policy); sweep is open item 6.

## DR-09 — Apex node (operable empire root)

- **Decision:** the empire-root folder becomes a governed node with a thin `.claude/` + CLAUDE.md that loads the canonical governance ontology, so a session opened there operates as the sovereign over the whole empire (fixing the empty-folder / invented-scaffolding problem). Hives remain generated views below it.
- **Alternatives rejected:** keep the empire root a bare folder (the failure mode observed); governance reachable only via MCP from within hives (no whole-empire locus).
- **Traces:** SN-11; SR-9; LA-9. **Status:** design RATIFIED; bootstrap order and build are open (parked to a build session).

## DR-10 — Governance is an ontology, not just rules

- **Decision:** governance is a class hierarchy of governed nodes (Rule, Capability{Skill,Agent,SwarmConfig}, Artifact, StructuralNode{Hive,Custodian,Perspective}, Transfer) under an abstract `GovernedNode` that carries lifecycle, retention, authority-owner, scope, and provenance as inherited properties. Skills classify on multiple axes (Function, Provenance, Perspective), not a single tree.
- **Alternatives rejected:** governance-as-rules-only (the original too-narrow frame); a single-inheritance tree for skills (does not fit the multi-axis reality).
- **Traces:** SN-7; SR-1, SR-4a; LA-1, LA-12. **Status:** RATIFIED (frame); GI-JOE formalizes (DR-02).

## DR-11 — INCOSE GtWR scoped to SR only

- **Decision:** the INCOSE Guide for Writing Requirements governs SR (system requirements) only; SN (stakeholder needs) remain WySE PSO and are not rewritten in INCOSE form. No Need class is added to the INCOSE ontology.
- **Alternatives rejected:** extend INCOSE with a Need class; map SN onto INCOSE applicability levels (would erase the WySE different-in-kind distinction).
- **Rationale:** needs and requirements are different in kind (PSO vs PSF), so different ontologies is correct.
- **Traces:** SN vs SR split; Section 5. **Status:** RATIFIED. Source: principal's own WRT-2516 BFO formalization of GtWR V4; primary citation needs `refverify`.

## DR-12 — Nomenclature (levels / spec types / SE subtypes)

- **Decision:** three tiers. Level: LO / LF. Specification type (problem space): PSO / PSF. SE-domain subtype (translation): SN (stakeholder needs) / SR (system requirements). PSO retained as the outcomes-side spec type (not renamed PSN). RTM rows carry SN / SR.
- **Traces:** Sections 2, 4, 5. **Status:** RATIFIED.
