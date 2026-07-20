# Data Fusion as a WySE Fable Family — Synthesis and Run Plan (2026-07-15)

**STATUS:** scoping review, integration status **(a) research artifact** throughout (R016). Nothing here is
launched; execution is reserved for a distinct/dedicated session (principal directive 2026-07-15).
**PROVENANCE (R018):** inventory produced by four Sonnet 4.6 subagents (Anthropic, Claude Code CLI),
synthesis by Opus 4.8 (claude-opus-4-8[1m]), principal-directed. **Method:** systematic-literature-review
skill, scoping-review mode (landscape map + Fable-shape verdict per sense), PRISMA-inspired but not a full
campaign.

Companion slice files (the detail): `01_decision_layer_evidence_fusion_*`,
`02_multi_model_multi_fidelity_fusion_*`, `03_classical_sensor_fusion_as_morphism_*`,
`04_organizational_architecture_fusion_*` (all 2026-07-15, this folder).

## 1. Objective

Inventory the full spectrum of "data fusion" as candidate WySE / systems-morphism Fable-run targets, then
plan which senses are Fable-shaped (carry a crisp mathematical claim provable by a self-verifying witness,
RBW-hardenable). Four senses were scoped in parallel: (1) decision-layer evidence fusion, (2)
multi-model / multi-fidelity fusion, (3) classical sensor/estimation fusion recast as a morphism, (4)
organizational / architectural fusion.

## 2. Strategic finding

"Data fusion" is not one run; it is a coherent FAMILY that reuses the WySE spine already built (institutions,
the homomorphism degrees D_s and D_b, the Giry monad / category of stochastic maps, the Kannan acceptability
poset). Three convergences recur across the four senses:

- **Institutions / colimits.** Organizational ontology-merge (a pushout of logical theories) and the
  decision layer both land on machinery WySE already uses (F9 neighborhood).
- **Homomorphism / comorphism on (D_s, D_b).** Kalman fusion, reduced-order models, and Kennedy-O'Hagan
  multi-fidelity coupling are all candidate-D / candidate-E adjacencies.
- **Giry / stochastic maps / Kleisli.** Bayesian fusion, Wasserstein behavioral distance, and mixture-of-
  experts all touch the +probability thread (F7, F8).

**The crown, and a dedup.** The decision-layer slice's top candidate (credal set = a distribution over the
Kannan poset, via Walley's imprecise-probability framework) is the concrete mathematical carrier for the
ALREADY-PRIORITIZED Tier-1 target **F3** (the confidence-weighted acceptability frontier). It does not
duplicate F3; it names its machinery and would, if proven, close the standing totalize-versus-poset tension
that has run since Target C (see `research_decision_analysis_confidence_thread`). This is the single
highest-leverage result the inventory surfaced, and it is a naming of an object we were already circling.

## 3. Fable-shape verdicts by sense

Full per-candidate detail (provable claim, witness sketch, refs) is in the four slice files. Summary:

- **Decision-layer (slice 01):** FC-1 LogOP-to-Kannan non-collapse (crisp, finite-enumeration witness,
  extends F2); FC-2 credal set = distribution over the poset (crown, carrier for F3, needs Walley 1991);
  medium: Dempster-Shafer conflict as incomparability, Choquet integral generalizing the six T3SD
  combiners, ordered-weighted-averaging (OWA) orness as a pessimism dial.
- **Multi-model / multi-fidelity (slice 02):** F-MF-01 reduced-order model as a Wymore homomorphism
  (witness runs on the pendulum already exercised); F-MF-02 D_b convexity for same-level mixtures (simplest
  claim, five witness points on existing infrastructure); F-MF-03 Kennedy-O'Hagan coupling as a readout
  comorphism; moderate: Wasserstein D_b inheritance (ties candidate E), multilevel Monte Carlo variance
  decomposition (a computational tool, not a theorem); speculative: mixture-of-experts as a Kleisli colimit.
  No existing fusion paper expresses level-crossing in Wymore-tuple / (D_s, D_b) terms, so the strong three
  are genuine new contributions, not translations.
- **Classical sensor fusion (slice 03):** FC1 Kalman information-form fusion = the categorical product of
  linear-Gaussian observation models (unique behavior-preserving homomorphism, D_b = 0; numpy-sweep
  witness); FC4 covariance intersection as a lax morphism that separates a safety invariant from optimality
  on the degree plane (structurally novel); FC3 Bayesian fusion in the category of stochastic maps
  (independence failure gives D_s = conditional mutual information; ties the Giry thread); plus EKF
  approximate morphism and Dempster-Shafer frame-coarsening naturality.
- **Organizational / architectural (slice 04):** ontology alignment/merging = pushout in the institution of
  theories is the one strongly Fable-shaped sub-area (description-logic reasoner checks it). Conway
  mirroring, knowledge-graph entity resolution, and enterprise schema integration reduce to constrained D_s
  measurements. JDL Levels 2-4, common-operating-picture, and hard+soft fusion are correctly NOT
  Fable-shaped (interpretive/doctrinal, no canonical algebra); do not chase them as theorems.

## 4. Net-new backlog additions (F18-F25)

Curated from ~24 raw candidates to eight Fable-worthy runs (the decision criteria in
`Fable_Run_Backlog_2026-07-13.md`). The rest fold into existing entries (Bayesian/Stoch -> F8; Wasserstein
-> F14; Dempster-Shafer/Choquet/OWA -> the F2/F18 combiner family; multilevel Monte Carlo = an off-Fable
computational tool). Entries mirrored into the canonical backlog this session.

| ID | Title | Delta (the new theorem) | Ties / cedes | Tier |
|----|-------|-------------------------|--------------|------|
| F18 | LogOP -> Kannan non-collapse | Every scalar combiner in the {product, geometric-mean} veto class induces a total order, unconditionally collapsing any Kannan-incomparable pair; the order-theoretic consequence of F2 | extends F2; Walley/pooling refs | 1 |
| F19 | Credal set = distribution over the Kannan poset | A confidence-weighted acceptability order is exactly a credal set (Walley imprecise probability); lower/upper envelope = Kannan necessity/possibility; closes totalize-vs-poset | IS the carrier for F3; needs walley1991 | 1 |
| F20 | D_b convexity for same-level mixtures | Bayesian model averaging / linear pooling satisfy D_b_fused <= convex-weighted sum of parent D_b by convexity of the Lawvere metric | new; cheapest witness | 1 |
| F21 | Reduced-order model as Wymore homomorphism | POD-Galerkin projection Pi is Wymore's surjection h_q; D_s = degree-of-homomorphism of Pi; D_b bounded by tail singular-value sum | carve-out vs candidate D; witness on pendulum | 2 |
| F22 | Kalman info-form = categorical product | Kalman information-form fusion is the unique behavior-preserving homomorphism from the product sensor system into the minimum-variance estimator (D_b = 0) | candidate-E pattern; sensor-fusion refs | 2 |
| F23 | Covariance intersection = safety/optimality split | Covariance intersection is a lax morphism preserving a consistency invariant (D=0) while accepting D_b > 0; first degree-plane separation of a safety from an optimality property | new; structurally novel | 2 |
| F24 | Kennedy-O'Hagan coupling as readout comorphism | The multi-fidelity scaling factor rho is the readout-layer comorphism between stratification levels; D_b bounded by GP posterior standard deviation | candidate D; needs kennedy2000 | 3 |
| F25 | Ontology merge = pushout of theories | The merge of two ontologies over a common sub-ontology is the pushout in the institution of logical theories; DL-reasoner-checkable | F9 enriched-institution; ontology-alignment refs | 3 |

## 5. Blocking reference debt (R019)

No approved.bib coverage exists for the fusion domain; every slice's citations are [PLACEHOLDER]. Gating
refs for a Tier-1 run staged to `.../00 Verified References/pending/data_fusion_gating_2026-07-15.bib`
this session (verification background agent; NOT promoted to the shared approved store, which stays gated):
walley1991 (F19), kennedy2000 (F24), giles2008 (multilevel Monte Carlo tool), dasarathy1997 and
steinberg1999 (JDL/taxonomy anchors). Promotion to approved.bib and the render gate (refcheck) belong to
the run session.

## 6. Recommended distinct-session plan

1. Promote the staged gating refs (refcheck / refverify) into approved.bib with provenance.
2. Tier-1 wave, inside the Fable toll-free window if still relevant: **F18 + F20 + F19** (two low-risk wins
   plus the crown). F18 and F20 are finite-enumeration / existing-infrastructure and near-certain; F19 is
   the strategic equivalence theorem and should follow Walley promotion. Note F19 supersedes running F3
   from scratch (it provides F3's carrier); reconcile the two in that session.
3. Tier-2 (F21, F22, F23) as a second wave; F21 requires an explicit carve-out from candidate D.
4. RBW-harden with a LIVE cross-vendor red leg (the standing lesson: never mark CLOSED on a 2-leg review).

## 7. Cost

Inventory: ~254k subagent tokens, four Sonnet agents (no Opus on the sweep; Fable cost discipline held).
Verification agent: one Sonnet, background. Log to AI_Swarm_Productivity scorecard D2 (ai_efficiency) at
session end per R014.
