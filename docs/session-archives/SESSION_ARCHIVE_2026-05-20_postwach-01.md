# Session Archive — 2026-05-20 postwach-01

**Hive:** PostWach
**Scope:** Warm up ruflo, review AI Circuit Breaker work and Jeffrey Wallk's proposed SERC AI4SE/SE4AI Workshop 2026 abstract draft (deadline Jun 5, 2026), then pivot to systems-theoretic investigation of the D_r (context relevancy) construct across two swarms with materials Paul added mid-session (WySE Metamodel, Bayesian SE draft, SES). Session continues into formal-ontology framing of problem spaces, level / role distinctions, EF unbundling, and morphic chain reformulation.
**Platform:** Ruflo v3.7.0-alpha.14, claude-opus-4-7 (1M context), Windows 11.
**Outcome:** Two swarms (4 + 4 agents) and one targeted swarm (3 agents) produced a substantive systems-theoretic body of analysis on D_r. Net result: D_r as a third coordinate of the morphism distance metric is retired; the construct is at a different architectural level; Paul's already-in-revision Bayesian SE for AI draft already supplies the (sigma_env, D_env) context-morphism quality pair on the IO observation frame morphism; Wymore's foundational TTSD machinery carries the cross-problem-space morphism that the construct ultimately rests on. The corpus is more unified than the initial v1 swarm read. Conversational alignment converged on problem-space-at-Levels-0-2 vs system-specification-at-Levels-3-4 framing, EF unbundling (G + T as problem-space-like, A as reference system specification), and closed-system framing as itself a homomorphism degradation. WySE Metamodel ontology development logged as candidate GI-JOE ticket.

---

## 1. Entry state

Session opened with Paul asking to warm up ruflo and review AI Circuit Breaker work, flagging an abstract deadline "in a couple of weeks." Target identified as SERC AI4SE/SE4AI Workshop 2026 (Jun 5, 2026 deadline). Current consensus draft was Wach_Wallk_AICircuitBreaker_Abstract_v0.5.md (Apr 23, 2026). Paul then shared a new draft from Jeffrey Wallk (`AICB_SERCabstract_2026-05-07.pdf`) with the framing that it appeared "obviously written by an LLM with limited human adjustment" and that he disagreed with the updates. He requested a swarm review and a separate swarm to assess how to correctly capture the intent of D_r.

---

## 2. Method

### 2.1 First swarm (4 background agents in parallel)

Spawned for Jeffrey's draft review and D_r assessment:
- Red team (skeptical-challenger): adversarial review of Jeffrey's draft against v0.5 baseline.
- Blue team (rationalist-synthesizer): steelman each Jeffrey addition; verdict per item.
- D_r literature scout (literature-reviewer): adjacent literatures (ODD, OOD, concept drift, applicability domain, V&V envelope, assume-guarantee contracts, ASME V&V 40, distributional robustness, coverage, Wymore-on-scope).
- D_r construct analysis (algebraic-logician): metric-axiom critique of D_r-as-third-axis; alternative formulations F1-F4.

### 2.2 White synthesis and D_r recommendation memo

After all four returned, produced:
- `white_synthesis_jeffrey_draft_v0.1.md`: RBW adjudication with 15 action items for v0.6.
- `Dr_recommendation_v0.1.md`: pick `C_env(q) + A(q)` at Layer 1 plus Layer 3 SPC chart; retire "D_r" name and the false CSER 2026 extension claim; add Sahigara 2012 (QSAR Williams plot), ASME V&V 40, Tibshirani 2019 (conformal under covariate shift), Benveniste 2018 (contracts), Wymore 1993 as citations.

### 2.3 User redirect: pure construct exploration

Paul redirected: "back away from the SERC abstract." Asked for a swarm exploring D_r systems-theoretically, building on his Wymore / degree-of-homomorphism / iso-degradation lineage, with debate and recommendation.

### 2.4 Second swarm (4 background agents in parallel)

- Wymore-native investigator (general-purpose): how does context show up inside Wymore's 5-tuple? Three formulations (A = morphism domain Dom(h); B = parameter family Z_real(c) with inter-fiber morphism g; C = coupling to environment system Z_env). Recommended A as foundation, B as extension, C as physical specialization. Key technical claim: "out of context" is non-assertion, not bad-assertion (D_s, D_b undefined off-domain, not high).
- DEVS / Experimental Frame investigator (general-purpose): EF as the canonical systems-theoretic notion of context. d_EF triple (d_G, d_A, d_T) decomposing into generator / acceptor / transducer distances. Verified Wach-Zeigler-Salado 2021 as *Applied Sciences* 11(11):4936. Key finding: (D_s, D_b) were always EF-conditional.
- Broader systems theory scout (researcher): 10 traditions mapped (Mesarovic, Klir, Bunge, Maturana, Pattee, Rosen, GST, Cybernetics, Salthe, SSM, Friston). Top 3 for direct integration: Friston (Markov blanket), Klir (source system), Rosen (modeling relation). Headline gap: no tradition jointly delivers structural-and-distributional context match.
- Category-theoretic investigator (category-theorist): Grothendieck fibration `p : Sys -> Ctx` with in-fiber morphism `k : F(u)(Z_real(cert)) -> Z_real(op)`. Same construct as Wymore-B expressed categorically. Three dead ends called out (Cartmell contextual categories, topos theory, third-axis framing).

### 2.5 Synthesis debate (synthesis_debate.md)

Staged the four perspectives, identified strong convergence (all four diagnose D_r-as-third-axis as a category error; Wymore-B + DEVS-EF morphism + Categorical fibration are the same construction in different vocabularies). Independent recommendation: five-layer stack with Wymore-A foundation, DEVS/EF operational decomposition, Wymore-B / categorical theoretical extension, Friston-style distributional axis, Rosen lineage acknowledgment. Single sharpest claim: "context is the data that determines which Wymore diagram a certified morphism is supposed to inhabit; 'out of context' is when the diagram has changed underneath the morphism while the morphism itself has stayed the same."

### 2.6 User requested deeper context: WySE Metamodel, Bayesian SE draft, SES

Paul shared three new sources to incorporate. Spawned third swarm (3 background agents in parallel):
- WySE Metamodel deep reader (general-purpose): read `Papers/AIOS_WySE/paper/sections/part4_formal_foundations.md` (783 lines). Reconciled S_a/C_r vs D_s/D_b notation (sign-flipped equivalents). Found AIOS-WySE Part IV has no first-class operational context construct; Omega is closest WySE-native object but treated as part of Z, not h.
- Bayesian SE draft analyst (general-purpose): read full `02 My Outreach/2026 - Bayesian_DEVS/revision/main.tex` (493 lines). Verified Figure 2 caption (line 213) reads verbatim: "context morphisms (top) are characterized by (sigma_env, D_env) and system morphisms (bottom) by (sigma_sys, D_sys)." Quad relationship and morphic chain explicit. d-separation handling of partial vs full context.
- SES specialist (researcher): full SES treatment from ZPK00 / Z23 / ZKZ24 / FPDZ22 / RZ85. Verified Z23 as *Information* vol 14 issue 1 art 22, ZKZ24 as *Simulation* 100(12) pp 1181-1196. Five candidate context encodings; recommended pattern (e) = designated context-specialization axis. Self-similar two-axis at SES level: d_SES + d_EF.

### 2.7 Synthesis v2 (synthesis_v2.md)

Major reorganization: D_r question largely closes because Bayesian SE draft already supplies the construct. Layer 3 of prior synthesis is "already done." Layer 4 (distributional axis) is the surviving genuinely new construct work. Self-similar two-axis decomposition across levels: morphism, context, family.

### 2.8 User correction on WySE

Paul corrected: WySE foundational TTSD machinery does carry the context morphism, as the morphism between the system requirement problem space and the verification requirement problem space. The v2 reader missed this by reading AIOS-WySE Part IV in isolation. The CB Spec v4 §2.6 "Z_ai as the runtime analog of a verification model" was the breadcrumb.

Updated synthesis_v2.md with seven targeted edits: header revision note, new Section 1.1 ("Correction: WySE carries the construct at the design-time problem-space layer"), Section 2.1 finding revised, Section 2.1 recommendation contribution recast, new convergence point C6 (design-time and runtime are the same construct at two lifecycle moments), Section 4.1 "Design-time lineage" subsection, W1 wrapper recast, Section 4.5 sharpest claim revised, Section 5 row L1 updated, Section 8 verdict revised.

### 2.9 Conversational alignment on problem spaces

Paul opened a deeper conversation: he had been getting drift from statements, convergence from leading questions. Logged this as a behavioral feedback memory (`memory/feedback_questions_vs_statements.md`).

Paul's leading question: "What is the overlap and distinction between the DEVS EF, SES, etc. and the intent of the WySE Metamodel?"

Worked through: WySE intent is design-theoretic (Wymore's MBSE chain from stakeholder need to verified system); DEVS EF intent is execution-theoretic; DEVS SES intent is knowledge-representation-theoretic. They meet at the morphism. WySE goes above into design and verification problem spaces; DEVS goes below into simulator semantics and family of model structures.

### 2.10 Conversational alignment on problem spaces in detail

Paul restated the baseline: WySE Metamodel as informal top-level ontology that needs to be formalized. Problem spaces in WySE: system requirement problem space, verification requirement problem space (both at I/O function level), with proposed extension to stakeholder need and validation problem spaces (at outcome level). Asked: is IOFO a problem space? Is EF a problem space? Is SES a problem space?

Responded: IOFO is an element (one specific function); EF is composite (G is the input half, T is the output half, A is the reference system specification); SES is a constructive declaration of a problem space (the set declared is what is the problem space). Layer cutoff: problem spaces at Levels 0-2 of the SSH; system specifications at Levels 3-4. The "I/O System" is at Level 3 and is the first level where the problem becomes a system. Paul confirmed the cutoff.

Paul corrected the EF reading: G provides inputs only, T captures outputs and computes statistics, A is closer to a system model under test (or to the reference system specification encoded by the predicate). Agreed and retracted "G is a problem space" in favor of "G is the input half of a problem-space-like pair (G, T); A is a Level-3-or-4 reference system specification."

### 2.11 Conversational alignment on related themes

- Two SESes can declare the same problem space (different decomposition orders, decomposition vs Cartesian product, different MB couplings producing equivalent executable models). Analogous to multiple regex / DFA declarations of the same regular language.
- EF as closed-system framing: G + T together substitute for the external system; the closure is a lossy abstraction; the lossiness is itself a candidate axis of D_r (point 4 of Paul's earlier seven-point statement).
- Validation model may include Level 3-4 model of test units (electrical impulse generator emulating power supply; pendulum emulating shock/vibration). This goes beyond G/T as bare inputs/outputs.
- Interfaces are missing from the discussion. In DEVS, interfaces are simulation ports. In SE/WySE, interfaces are larger constructs that bundle sets of I/O. Parameterization differs between WySE and DEVS.

### 2.12a Late-session corrections on the morphic chain debate

After I produced the eight-point debate sketch for the morphic chain, Paul corrected several framing errors:

- **Morphic chain mechanism is what matters, not the prototype-to-fielded instance.** I had framed the chain as digital model → prototype → fielded system. That is one instance. The mechanism is more general: a morphic chain exists wherever multiple linked specifications relate by morphisms. Other valid instances: dynamic interaction between system requirements ↔ system design ↔ V&V across the full lifecycle from concept to retirement; old system to new system; design alternatives; within a product line. The mechanism is the load-bearing piece for the WySE ontology; specific instances are examples.
- **Dynamic interaction, not stage-dependent role presence.** I had asked whether all four WySE roles are always present at every development stage. Wrong framing. The dynamic interaction between system requirements, system design, and V&V exists from system concept through some point in operation and sustainment when the decision to retire the system is made. All four roles (extended: stakeholder need, system requirement, verification requirement, validation) are present throughout, in dynamic interaction. The "stage-dependent presence" question was misposed.
- **Chain is across role-sets, not within them.** I had described the chain as stakeholder need → system requirement → verification requirement (within one role-instantiation). Wrong. Paul's meaning of chain is from one complete set of needs+requirements+verification+validation TO a second set (or infinite sets). The chain is between different instantiations of the full WySE role complement, not a sequence within one instantiation.
- **Bounds, not morphism, between Levels 0-2 and Levels 3-4.** I had described a "design step morphism" from problem space (Levels 0-2) to system specification (Levels 3-4). Wrong. The relationship is bounds, not morphism. The problem space bounds what designs are admissible: a design's I/O projection (its behavior taken down to Levels 0-2) must be an element of the problem space's admissible set. This is set-membership / constraint, not a structure-preserving map between two systems of the same type. Morphisms relate two systems of the same kind; problem-space-to-system-specification is a different kind of relation entirely (an admissibility constraint).
- **Validation problem space type signature postponed.** Per Paul's direction, hold off on formalizing the validation problem space until the problem spaces of functions (system requirements and verification) are completed.
- **Chain composition (sigma, D) algebra still open.** Acknowledged unresolved; needs working out per kind of morphism.

### 2.12 Side note filing

`side_note_wyse_ontology_to_gijoe.md` filed as candidate GI-JOE ticket for WySE Metamodel ontology development. Status: candidate, not yet filed. Updated with item on alternative declarations of problem space (Rao Kannan at UAH flagged as citation lead) and noted SES equivalence as algorithmic-efficiency exploration item.

---

## 3. Deliverables

### Files created (chronological)

**SERC abstract review:**
- `Papers/AI_Circuit_Breaker/reviews/red_team_jeffrey_draft_v0.1.md`
- `Papers/AI_Circuit_Breaker/reviews/blue_team_jeffrey_draft_v0.1.md`
- `Papers/AI_Circuit_Breaker/reviews/white_synthesis_jeffrey_draft_v0.1.md`

**D_r first investigation:**
- `Papers/AI_Circuit_Breaker/reviews/Dr_literature_scoping_v0.1.md`
- `Papers/AI_Circuit_Breaker/reviews/Dr_construct_analysis_v0.1.md`
- `Papers/AI_Circuit_Breaker/reviews/Dr_recommendation_v0.1.md`

**D_r systems-theoretic second swarm:**
- `Papers/AI_Circuit_Breaker/research/Dr_systems_theoretic/01_wymore_native.md`
- `Papers/AI_Circuit_Breaker/research/Dr_systems_theoretic/02_devs_experimental_frame.md`
- `Papers/AI_Circuit_Breaker/research/Dr_systems_theoretic/03_broader_systems_theory.md`
- `Papers/AI_Circuit_Breaker/research/Dr_systems_theoretic/04_categorical_synthesis.md`
- `Papers/AI_Circuit_Breaker/research/Dr_systems_theoretic/synthesis_debate.md`

**D_r third swarm with new materials:**
- `Papers/AI_Circuit_Breaker/research/Dr_systems_theoretic/v2/01_wyse_metamodel.md`
- `Papers/AI_Circuit_Breaker/research/Dr_systems_theoretic/v2/02_bayesian_se_draft.md`
- `Papers/AI_Circuit_Breaker/research/Dr_systems_theoretic/v2/03_ses.md`
- `Papers/AI_Circuit_Breaker/research/Dr_systems_theoretic/v2/synthesis_v2.md`
- `Papers/AI_Circuit_Breaker/research/Dr_systems_theoretic/v2/side_note_wyse_ontology_to_gijoe.md`

**Memory:**
- `memory/feedback_questions_vs_statements.md`
- Updated `memory/MEMORY.md` with the new feedback entry.

### Files NOT modified

- `Papers/AI_Circuit_Breaker/AI_Circuit_Breaker_Design_Spec_v4.md` (read for context; no changes).
- `02 My Outreach/2026_SERC_AI4SE_SE4AI/Wach_Wallk_AICircuitBreaker_Abstract_v0.5.md` (current consensus SERC abstract; no v0.6 produced this session).
- `02 My Outreach/2026 - Bayesian_DEVS/revision/main.tex` (Bayesian SE draft; read for context; no changes).
- `Papers/AIOS_WySE/paper/sections/part4_formal_foundations.md` (read for context; no changes).

---

## 4. Decisions (durable)

- **D1.** Jeffrey Wallk's 2026-05-07 PDF draft of the SERC abstract is not adopted as written. Reasons captured in red_team / blue_team / white_synthesis. Specifically blocking: D_r as third axis of morphism distance (Fatal), three unsupported "to our knowledge first" claims (regression on prior white-synthesis directive), holonic immune system as novelty (prior art Koestler 1967, Van Brussel et al. 1998 PROSA), Phase III scope flip (cost-estimate to executed instantiation), 6-page render vs 3-page cap.
- **D2.** D_r as a third coordinate of the morphism distance metric is retired. The construct is at a different architectural level (independently arrived at by all four agents of the second swarm).
- **D3.** The Bayesian SE for AI draft (Wach, Krometis, Sonanis, Panchal, Beling, Freeman; in revision for Wiley/INCOSE) already supplies the context-morphism construct as (sigma_env, D_env) on the IO observation frame morphism, parallel to (sigma_sys, D_sys) on the NS coupled-system morphism, in a quad relationship across the morphic chain. The "D_r question" as initially scoped largely closes.
- **D4.** Wymore foundational TTSD machinery carries the context morphism as the morphism between the system requirement problem space and the verification requirement problem space. AIOS-WySE Part IV does not surface this construct; CB Spec v4 §2.6 has it implicitly via "verification model" language. The corpus (Wymore TTSD, AIOS-WySE, CB Spec v4, Bayesian SE draft) is more unified than initial v2 swarm read.
- **D5.** The two-axis (D_s, D_b) decomposition is self-similar across levels: morphism level (CSER 2025 / 2026), context level (Bayesian SE draft), family level (SES + EF combined). Same structural-behavioral pairing logic applied to different objects at different levels.
- **D6.** WySE problem spaces sit at Levels 0-2 of the DEVS System Specification Hierarchy (Observation Frame, I/O Behavior, I/O Function). Level 3 onward (state-transition, coupled-component) is system specification, not problem specification. The "IO System" is at Level 3.
- **D6a (correction to my earlier framing).** The relationship between problem space (Levels 0-2) and system specification (Levels 3-4) is **bounds**, not morphism. The problem space bounds what designs are admissible: the design's I/O projection must be an element of the problem space's admissible set. This is set-membership / constraint, not a structure-preserving map. Morphisms relate two systems of the same kind; problem-space-to-system-specification is an admissibility relation, a different kind of relation entirely. Calling it a "design step morphism" was wrong.
- **D7.** Problem spaces in WySE: at minimum, system requirement problem space and verification requirement problem space (problem spaces of input/output functions). Proposed extension: stakeholder need problem space and validation problem space (problem spaces of outcomes). The two new roles are at the outcome level, not the I/O function level. A specific problem space is a (level, role) cell.
- **D8.** EF unbundles into: G (input side, structurally part of a problem-space-like pair), T (output side, structurally part of a problem-space-like pair), A (reference system specification at Levels 3-4, or equivalently the predicate that encodes correctness against that reference). The EF triple does not have a clean "problem space" type; it bundles input-side problem space, output-side problem space, and reference system specification.
- **D9.** SES is the constructive declaration of a problem space at a chosen level / role. Multiple SESes can declare the same problem space (analogous to multiple regex / DFA for the same regular language).
- **D10.** EF is a closed-system framing of the external system. G + T together substitute for what the open external environment would provide; the closure is a lossy abstraction (a candidate axis of D_r per Paul's earlier point 4).
- **D11.** WySE Metamodel ontology development is a candidate GI-JOE ticket. Side note filed at `Papers/AI_Circuit_Breaker/research/Dr_systems_theoretic/v2/side_note_wyse_ontology_to_gijoe.md`. Ticket not yet filed.
- **D12.** Behavioral feedback memory: when Paul provides statements I tend to drift (add scaffolding, propose next steps); when he asks leading questions I converge. Memory entry at `memory/feedback_questions_vs_statements.md` and pointer in `MEMORY.md` Critical Behavioral Rules.
- **D13.** The morphic chain is a mechanism, not a specific instance. The prototype-to-fielded sequence is one instance. Other valid instances: dynamic interaction between system requirements, system design, and V&V across the full lifecycle from concept to retirement decision; old system to new system; design alternatives; within a product line. The mechanism is the load-bearing piece for ontology work; specific instances are examples.
- **D14.** Dynamic interaction exists from system concept through some point in operation and sustainment when the decision to retire is made. All WySE roles (stakeholder need, system requirement, verification requirement, validation, design) are present throughout in dynamic interaction; the "stage-dependent role presence" question was misposed.
- **D15.** Chain semantics: Paul's "chain" is between different instantiations of the full WySE role complement (one complete set of needs + requirements + verification + validation TO a second set, possibly infinite sets), not a sequence within one instantiation. The within-instantiation relations (needs to requirements to verification) are role-relations, not chain links.
- **D16.** Validation problem space type signature work is postponed until problem spaces of functions (system requirements and verification) are completed.
- **D17.** Chain composition (sigma, D) algebra remains open. Needs working out per kind of morphism.

---

## 5. Open items the user must address

1. **SERC AI4SE/SE4AI v0.6 abstract.** Deadline Jun 5, 2026 (16 days from session). v0.5 exists; v0.6 not produced. The white_synthesis_jeffrey_draft_v0.1.md gives 15 action items for v0.6; the Dr_recommendation_v0.1.md gives the C_env + A treatment; the v2 synthesis recommends building the abstract on the Bayesian SE quad with (sigma_env, D_env). Decision needed: produce v0.6 in next session, or hold until further D_r alignment.
2. **Distributional axis selection.** Conformal-prediction coverage (already in Bayesian draft bibliography as Angelopoulos 2023) is the closest-to-draft candidate. Alternatives: KL divergence on input distributions, total variation, Friston free-energy. User preference unresolved.
3. **SES adoption scope.** Bayesian SE paper, AI Circuit Breaker design spec, or separate methodology paper. Unresolved.
4. **WySE Metamodel ontology ticket to GI-JOE.** Side note filed; ticket not yet filed. Confirm timing.
5. **Wymore 1993 TTSD direct read.** Not done in either swarm. The Wach-Salado 2019 "Can Wymore's Mathematical Framework Underpin SysML?" is the closest published bridge; the AIOS-WySE Part IV is a partial restatement. A direct read of Wymore 1993 chapters on TTSD is on the table as the next investigation.
6. **Salado validation papers.** Salado 2018a and Salado 2021 on systems-theoretic verification and validation. Paul flagged he is not convinced Salado has it right. Direct read pending.
7. **STPA / STAMP / SCRE / FORREST exploration.** On hold per Paul's direction.
8. **Stochastic morphism formalization.** Open construct question. Current sigma is set-theoretic; stochastic generalization (Markov kernels, measure-theoretic preservation) needs working out.
9. **Closed-vs-open system framing as a homomorphism degradation.** Working hypothesis: the closure operation is itself a D_h-quantifiable move. Not formalized.
10. **Outcome and validation as semantic constructs.** What is an "outcome" systems-theoretically? Validation problem space proposed but formal definition pending. Connects to Salado work (open item 6).
11. **Rao Kannan at UAH.** Citation lead for alternative problem-space declarations. Pull citation before formal literature review.
12. **Interfaces in DEVS vs WySE.** DEVS interfaces are ports; WySE interfaces bundle I/O with parameterization. Semantic distinction important for ontology. Parameterization mechanism in DEVS less clear; needs investigation.
13. **External system modeling.** Validation models may include Level 3-4 specifications of test units (impulse generators, pendulums) that emulate parts of the open environment. This is richer than EF's G + T closure. How does this fit the level / role framing?
14. **Morphic chain in dissertation reformulated.** Paul flagged this as the convergence target. Sketch produced; needs more debate and detail before formal commitment.

---

## 6. Out-of-scope items not pursued

- DARPA DSO BAA Executive Summary compression (Attachment A format, 4 Heilmeier Qs, 1 page).
- PM routing email to HR001125S0013@darpa.mil (drafted Apr 1, not sent).
- Terminology reconciliation with Jeffrey (SAS/CRI/VDC/SCS/ASAR vs S_a/C_r/D_s/D_b). Flagged at session start; not addressed.
- v0.6 SERC abstract draft itself.
- Direct read of Wymore 1993 TTSD chapters.
- Direct read of Salado 2018a and Salado 2021.
- STPA / STAMP / SCRE / FORREST literature.
- Rao Kannan UAH citation pull.
- The four reasoning bullets at the end of the session conversation on validation model, interfaces, external system modeling, and morphic chain detail. Engaged conversationally; not investigated in depth.

---

## 7. Next session entry hints

- **Pickup file.** `Papers/AI_Circuit_Breaker/research/Dr_systems_theoretic/v2/synthesis_v2.md` is the current recommendation state. The four follow-up points from end-of-session conversation are open: A vs system design vs verification model vs validation model; problem-space bounding in WySE vs DEVS; morphic chain debate before formalization (with the corrections in D13-D17 captured); external system detail (test units, interfaces).
- **Critical pickup distinctions from late-session corrections.** When resuming the morphic chain work: (a) chain is mechanism, not the prototype-to-fielded instance; (b) all WySE roles are present throughout the lifecycle in dynamic interaction; (c) chain is across role-set instantiations, not within one instantiation; (d) Levels 0-2 to Levels 3-4 is bounds, not morphism; (e) postpone validation problem-space type signature until system requirement and verification requirement problem spaces are completed; (f) chain composition algebra still open.
- **Side note to track.** `Papers/AI_Circuit_Breaker/research/Dr_systems_theoretic/v2/side_note_wyse_ontology_to_gijoe.md` is the candidate GI-JOE ticket. Two future-exploration items added: alternative problem-space declarations (Rao Kannan lead), SES equivalence as algorithmic-efficiency move.
- **Conversational pattern note.** `memory/feedback_questions_vs_statements.md`: Paul gets convergence from leading questions, drift from statements. When Paul provides statements, do not add path-forward scaffolding or "what's new" framing. Mirror Paul's framing words; answer the actual question.
- **Reusable patterns.**
  - Three-swarm pattern (4 + 4 + 3 background agents in parallel, with synthesis at each stage) is the right cadence for a deep construct-development session. Each swarm closed under ~10 minutes with substantive 400-700 line deliverables.
  - The (level, role) cell framing for problem spaces is the right axis pair for WySE-DEVS ontology work.
  - "Out of context is non-assertion, not bad-assertion" (D_s, D_b undefined off-domain) is the formal pivot that retires D_r as a third axis.
- **Cited verified during session:**
  - Wach, Zeigler, Salado (2021), *Applied Sciences* 11(11):4936, DOI 10.3390/app11114936.
  - Zeigler (2023), "Extending the Hierarchy of System Specifications and Morphisms with SES Abstraction," *Information* 14(1) art 22, DOI 10.3390/info14010022.
  - Zeigler, Koertje, Zanni (2024), "The utility of homomorphism concepts in simulation: building families of models from base-lumped model pairs," *Simulation* 100(12) pp 1181-1196, DOI 10.1177/00375497241264834.
- **Render command (working on this system):** `pandoc input.md -o output.pdf --pdf-engine=xelatex -V mainfont="Calibri" -V geometry:margin=0.75in -V fontsize=10pt`. Not used this session; flagged from 2026-05-19 archive.
- **MEMORY.md update needed.** Add an Open Threads entry for "D_r systems-theoretic investigation" pointing at `Papers/AI_Circuit_Breaker/research/Dr_systems_theoretic/v2/synthesis_v2.md` so future sessions can pick up.
- **Productivity scorecard.** Per [R014], scorecard to be filed at `Papers/AI_Swarm_Productivity/data/scorecards/2026-05-20-postwach-01.yaml`.
