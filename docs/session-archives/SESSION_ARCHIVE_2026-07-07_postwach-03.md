# Session Archive — 2026-07-07 postwach-03

**Focus:** Fable 5 planning; the morphism-library research program (Target C); reference-corpus review; authoring and tri-model hardening of the Fable authoring prompts.
**Researcher:** Paul Wach
**Model:** Opus 4.8 (planning); 10 Opus-tier subagents; Codex (gpt-5.5) + Gemini red-teams.
**Working folder:** `00 Planning and Execution/Fable 5 planning/` (outside the PostWach repo, by principal direction).

## Summary
Began by reviewing a viral skill-capture repo (`tomicz/fable-5-train-opus-skills-after-it-retires`) and generalized it into (1) a reusable hive-of-hives skill-bootstrap procedure and (2) a plan to spend the Fable 5 window (model leaves the subscription ~July 12) on irreplaceable, low-verifiability work. The subject converged on the morphism library, and through a corpus review and extended debate produced a scoped flagship research target (Target C) plus a tri-model-hardened set of Fable authoring prompts. GI-JOE ontology work is deferred to after the cutoff. Full intellectual narrative in `SESSION_NOTES_2026-07-07_Fable5_and_Morphism_Library.md` (six core-contribution capsules).

## Artifacts produced (in `Fable 5 planning/`, unless noted)
- `Repo_Review_fable5-train-opus-skills_2026-07-07.md`
- `PROCEDURE_Skill_Library_Bootstrap_and_Handoff.md` (reusable, portfolio-wide)
- `PLAN_Discussion_Evolution.md`
- `Morphism_Library_Corpus_Inventory_v0.md` (Shadab/Salado/Rao Kannan review, Tier 1 + 2)
- `Target_C_Scope_Pedigree_Acceptability_Order_Morphism.md` (the live target spec)
- `Morphism_Library_Ontology_Schema_v0.md` (background agent; D-1..D-6 open typing questions)
- `SESSION_NOTES_2026-07-07_Fable5_and_Morphism_Library.md` (narrative + capsules)
- `Fable_Authoring_Prompts.md` (the hardened Fable run prompts)
- `AI_Second_Brain_MindStudio_Notes_2026-07-07.md` (tangent, parent folder)
- Memory: `project_fable5_morphism_library.md` + MEMORY.md Open-Threads pointer.

## Key decisions
- **Flagship = Target C**: does pedigree license a sound projection of acceptability from model to realized system (abstract-interpretation soundness at the reality boundary). Target A (nonlinear-from-partial) held as long-horizon crown jewel; Target B (interfaces-as-systems) is now constitutive of C via the federation.
- **Pedigree-primary (answer b)**: order models by pedigree; acceptability is a distributed validating property, not the frame. Rejected "order designs / verdict-preservation" (a) as presuming a single-SD verdict that does not exist.
- **Measure = D_s** (degree of homomorphism, a resolution measure). On the DEVS carrier structure = behavior, so D_b is subsumed; D_b re-emerges only off-carrier as a fidelity residual.
- **Terminology fixed**: fidelity = model↔reality; resolution = within-family; pedigree = cross-family (VM↔SD). "Projected fidelity" confirmed for the VM's anticipatory role. Do NOT use "projected vs measured" framing (principal correction).
- **SD is a functional reference (Wymore FSD) plus a buildable VM federation** coupled through interfaces. Cross-family + interfaces + DEVS carrier all follow from this. Cross-family pedigree = Wymore's functional↔buildable homomorphism (Salado-Kannan 2018 Def. 2); we extend Wymore.
- **Evidence tagging = TRAK two-axis stamp**: SOURCE {Established | Inferred | Synthetic} × LEVEL {0-5}. GRL (readiness) and the Bayesian posterior are verification-stage only, not authoring (overkill; portfolio already learned τ-as-gate false-negatives).
- **Authoring allocation**: Fable authors the judgment-dense research + skills; Opus does discovery, review, mechanical runbooks, prep.
- **PostWach vs GI-JOE split** (STOIC/TRAK precedent): PostWach authors the ontology specification (Fable typing spec); GI-JOE implements TBox/SHACL after July 12. GI-JOE is entirely post-cutoff.

## Tri-model prompt hardening
Codex (gpt-5.5) and Gemini red-teamed `Fable_Authoring_Prompts.md`; ~16 fixes adopted. Codex: over-scope split into hard-stop gates, evidence ledger, fail-fast BLOCKED, operational-skill quality gates, drop Prompt 4 parallelization, prose/anti-theater budget. Gemini: anti-confirmation-bias proof rule, read-predecessor-output rule, `<SKILLS_ROOT>` handling, LaTeX notation, milestone strictness. TTL production removed from Fable (deferred to GI-JOE) rather than "make Fable emit valid TTL." Gemini first run failed on sandbox scoping (target file outside its workspace); recovered by copying into its workspace.

## Plan to July 12 (all PostWach; GI-JOE after)
1. Finish prep: two launch confirmations pending (skill placement, default `.claude/skills`; run mechanism, capped Fable workflow vs interactive sessions); this archive + scorecard (done).
2. Run the Fable window (`model: fable`, fresh rate-limit block not overlapping the parallel validation session's Fable use, hard token cap): Prompt 1 (Target C research, hard-stop gates), Prompts 2-5 (skills incl. ontology typing spec). Optional second wave if budget remains.
3. Post-run review (Opus/cheaper): FACTUAL/DOCTRINE/USABILITY, test skill guards on Sonnet-class, cross-project-reviewer.
4. Handoff: PostWach→GI-JOE ticket carrying the typing spec.

## After July 12
GI-JOE implements the ontology (TTL/SHACL/OntoClean). Cheaper models: mechanical runbook skills, optional second-wave skills, cross-family (L5) / Target A frontier as it matures.

## Run outcome + principal correction (2026-07-08)
The Fable flagship workflow (`wf_4835e1a7-a3e`, 5 agents, ~21 min, ~709k subagent tokens, session model = Fable 5) completed overnight with no BLOCKED emissions. Outputs: `Fable 5 planning/research/TargetC_pedigree_acceptability_candidate.md` (27-row evidence ledger) + 4 skills in PostWach `.claude/skills/` (morphism-domain-reference incl. the D-1..D-6 typing spec for GI-JOE, morphism-research-frontier, morphism-verification-campaign, morphism-research-methodology). The anti-confirmation-bias hardening held (no forced proof).

**Principal correction (2026-07-08), reopening the flagship result:** Fable's Gate-1 claim "every witnessed morphism is a scoped isomorphism, D_s = 0" is an ARTIFACT of measuring D_s on the scoped reduction to a canonical 2-state on/off reference; the flashlight problem space is 2-state, so scoping flattens 3-, 2-, and 1-state models to a common 2-state core before degree is measured, forcing D_s = 0. A 2-state and a 3-state machine cannot be isomorphic. The **T1/T2/T5 degree-only refutation is WITHDRAWN** as a refutation of the conjecture (re-characterized as: this scoped metric is degenerate on this test bed). What stands: **T4a (monotonicity over the kernel-refinement order — the correct structural order, hence the conjecture is SUPPORTED-so-far), C1/C2 (scalar-D_s defects, feed the CSER 2026 metric line), L1-L3, L4'.** The enriched object pi = (morphism, descriptor, conditions) is the correctly-stated conjecture. **Corrected next step:** recompute D_s on structure-preserving morphisms (the SM 3->2->1 hierarchy or full-model maps, which have a real graded spectrum) and re-run T1/T2; better, use the federated multi-discipline test bed. The artifact carries a correction banner. This is the R016 candidate-fencing working as intended: the first adversarial reader caught the load-bearing flaw before propagation.

## Open threads / notes
- Missing federated multi-discipline test-bed example (flashlight is a single-SD toy).
- Blackboard-to-ticket merge (2026-07-01 CTO thread): the PostWach↔GI-JOE morphism-library co-build is logged as a validation case; ticket handoff suffices for now.
- Concurrency: a parallel session is validating the dissertation results; Target C uses only its settled outputs (120/120 identities), and references the open F1/F7 decisions as open.
- Provenance/governance: all research claims candidate until proven and refutation-tested (R016); references via reflookup/refverify (R019); ontology typing is GI-JOE-implemented.
