---
name: morphism-verification-campaign
description: Decision-gated campaign runbook for testing whether a morphism-based pedigree order tracks an acceptability order (Target C shape) on settled validation data. Load when running or resuming a pedigree-vs-acceptability campaign, re-running Gate 1 on new data, attacking the enriched-pedigree conjecture (PO-3/PO-4), or triaging a monotonicity violation. Do not load for concept lookups (use morphism-domain-reference), for picking a research target (use morphism-research-frontier), or for general evidence discipline outside a campaign (use morphism-research-methodology).
---

# Morphism Verification Campaign Runbook

**Integration status [R016]: (a) research artifact.** This runbook operationalizes the Target C campaign structure. Every mathematical claim it carries is CANDIDATE unless its evidence-ledger row says otherwise. The degree-only monotonicity conjecture it was originally built to test is **REFUTED on the settled 18-VM data** (2026-07-07 run); the runbook is retained and generalized because the campaign shape is reusable: new data, the enriched-pedigree conjecture, and future pedigree-vs-acceptability welds all run through the same gates.

PROVENANCE: produced by Fable 5 (claude-fable-5[1m]), vendor Anthropic, access mode Claude Code CLI (subagent run at principal's direction), 2026-07-07. Sources read-only; no mutation of the dissertation repo or validation data.

Open dissertation decisions F1 (infinite-equivalence wording) and F7 (graded-gate rewrite) are **OPEN**. This runbook uses only validated post-F7 acceptability values and treats both F1 levels as tagged data; it does not resolve either decision, and neither may any campaign run under it.

---

## 1. Purpose and objects (definitions first)

A **campaign** here is a four-gate, decision-gated research attempt on one falsifiable target of the form: does an order on verification models induced by a morphism measure monotonically track an acceptability structure on the same models or their designs?

Fixed terminology (non-negotiable; see the known-wrong-paths fence, §9):

- **Fidelity** = model to reality. **Projected fidelity** = the verification model's anticipatory inference of the not-yet-realized system. **Resolution** = within-family abstraction; the structural degree $D_s$ is a resolution measure. **Pedigree** = cross-family model to model, verification model (VM) to system design (SD). Never write "fidelity" for the VM-to-SD relation. Never use "projected vs measured" framing.
- **System**: Wymorian quintuple $Z = (S, I, O, N, R)$.
- **Exact homomorphism** (canonical baseline): Salado-Kannan 2018 Definition 2 (approved store key `salado2018mathematical`): surjections $h_q, h_i, h_o$ with transition preservation $h_q(N_2(x,i)) = N_1(h_q(x), h_i(i))$ and readout preservation $h_o(R_2(x)) = R_1(h_q(x))$. Direction: SD concrete, VM abstract; witnessed map runs $\mathrm{SD} \to \mathrm{VM}$.
- **Degree of homomorphism (DoH)** for $h: A \to B$: $\mathrm{DoH} = \frac{1}{|B|} \sum_{b \in B} \frac{1}{|h^{-1}(b)|}$, per state/input/output component; scalar distance $D_s = 1 - \overline{\mathrm{DoH}}$. Notation caveat: the CSER 2026 (Conference on Systems Engineering Research) draft uses $D_s$ for the DoH tuple itself; the Target C lineage uses $D_s = 1 - \mathrm{DoH}$. Write $\mathrm{DoH}$ for the ratio and $D_s$ for the distance in every campaign artifact so no claim depends on the collision.
- **Refinement pedigree order** (the correct same-family order): $V_j \trianglerighteq V_i$ iff $\ker h_j \subseteq \ker h_i$ (kernel refinement). Proved order-compatible with preservation (T4a). The scalar $D_s$ is NOT an order embedding (counterexamples C1, C2, §8).
- **Acceptability** (Kannan, approved key `kannan2019preference`): betterness poset; acceptable = maximal elements; incomparability allowed.
- **Artifact stack**: system requirement (SR); verification requirement problem space (VRPS); verification-model morphism condition (VMMC); per the WySE (Wymorian Systems Engineering) metamodel.
- **DEVS** = Discrete Event System Specification, the common carrier for cross-family co-representation. "$D_b$ vanishes on the carrier" is an **asserted claim**, not an axiom; use it only as scope justification, never as a proof premise.

Sibling skills (same authoring wave; if a sibling is not yet present in `.claude/skills/`, treat its function as unassigned and do not improvise it): `morphism-domain-reference` (concepts and taxonomy), `morphism-research-frontier` (target selection), `morphism-research-methodology` (evidence discipline and candidate lifecycle).

---

## 2. Campaign state ledger (instantiate before Phase 0)

Create one campaign file (in the campaign's own working folder, never the repo root) with these fields. A campaign without a filled ledger MUST NOT proceed past Phase 0.

| Field | Content |
|---|---|
| Target | One-line falsifiable statement (conjecture to confirm or refute) |
| Orders | The two orders: domain order (pedigree; state WHICH order: kernel refinement, enriched $\pi$, or other) and codomain structure (acceptability; state the exact operationalization and whether it is a proxy) |
| Data | Exact read-only source files, with the four pins of §4.1 |
| Milestone | The measurable success criterion (§10); numbers, not adjectives |
| Fallback | The pre-committed fallback if the load-bearing bet fails (for Target C: same-family core if the DEVS-carrier move fails) |
| Provenance | R018 line: foundation model, vendor, access mode; delegation if any |
| Open decisions | Upstream decisions the campaign must not resolve (currently F1, F7) |

---

## 3. Phase 0: preconditions (fail-fast; all steps mandatory)

1. Verify every source file in the ledger exists and is readable. On any miss, emit `BLOCKED: missing <path>` and STOP that branch. Never continue by inference.
2. Confirm read-only discipline: the dissertation manuscript repo and its `validation/` and `analysis/` data are READ-ONLY. Write only to the campaign's own output path.
3. Run the known-defect screen: read `analysis/errata_register.md` end to end; list every erratum that touches a pinned input; classify each as material or documented-immaterial WITH the register's own evidence (for the 2026-07-07 run: E2 and E10 immaterial to the identities matrix, 0 cells).
4. Confirm no race with open upstream decisions: use only settled, double-confirmed data (for the flashlight test-bed: the 120/120 sweep-vs-recompute identities matrix). If the needed value is under an open decision, `BLOCKED: open decision <id>`.
5. Stamp provenance (R018) in the campaign file header.
6. Pre-register the tests: write the exact monotonicity criteria (§4.4) and the milestone numbers BEFORE computing anything. Hypothesis predicts numbers before running.

Expected observation: all six steps pass in minutes. If step 1 or 4 fails, the campaign does not start; there is no partial-credit start.

---

## 4. Phase 1, Gate 1: empirical cross-tabulation (HARD STOP)

Gate 1 exists to make the conjecture confront the data before any formal work. Do NOT proceed to Gate 2 unless (a) the cross-tab is reproducible by script with passing asserts and (b) the monotonicity criterion is explicitly stated.

### 4.1 Step 1: pin the four operational definitions

Fill this table; every row must name a file and a row/key inside it. Any unpinnable row: `BLOCKED: missing <definition>` and STOP.

| Pin | Must specify | 2026-07-07 pinning (calibration example) |
|---|---|---|
| $D_s$ extraction rule | Formula source + which mapping tables | DoH Eq. (3) of `Papers/SE_Math_Foundations/isomorphism-library/paper/Wach_Sandmann_Iyer_CSER2026_Isomorphism_Library_Draft_v1.md`; maps from `validation/v2_sd_vm.json` (`vm_reductions[].collapse_h/g/k`, `sd4_vm8_crosscheck`) |
| Family labels | The field that decides same- vs cross-family, values verbatim | `v2_sd_vm.json -> vm_reductions[].semantic_class`; same-family = "on/off light" (10 VMs); cross-family = pizza, RGB pen, conduits; edge = symbolic, radio |
| Acceptability-verdict source | The validated cell rule, with its composition rule quoted | `validation/v4_identities_matrix.json` (`matrix`, `membership`, `composition_rule`); verdict AGREE per `v4_identities_reconciliation.md` §3, §5 |
| Monotonicity test, exact | T1 and T2 as in §4.4, with codomain choice stated and justified | Acceptance-breadth proxy $\mathrm{acc}(V)$ = count of acceptable tuples containing $V$; the weakest conjecture-charitable codomain |

### 4.2 Step 2: build the cross-tab, split by family

Produce one table: VM | family label (pinned) | witnessed morphism | $D_s$ | acceptability value | accepting contexts. Same-family block first, then cross-family and edge cases. Totals must cross-check against the pinned matrix (for the flashlight data: $\sum \mathrm{acc} = 150$; membership vectors reproduce `membership` exactly).

**Reproducibility requirement (measurable, never by eye):** ship a script of at most one page that regenerates the table from ONLY the pinned files and ends in `assert` statements on the totals and the violation count. The gate passes only if the asserts pass on a fresh run. The 2026-07-07 reference script lives in `00 Planning and Execution/Fable 5 planning/research/TargetC_pedigree_acceptability_candidate.md` §2.6 (asserts: $\sum = 150$, violations $= 5$).

### 4.3 Step 3: DEVS-carrier early-validation subgate (with fallback)

Run this BEFORE investing in cross-family formalization. Test, on the cross-family cases already in the data, both halves of the carrier bet:

1. **Co-representation** (mechanical): do the cross-family models reduce to the common carrier? Expected: yes cheaply, or the bet dies immediately.
2. **Discrimination** (the real bet): does carrier-level $D_s$ separate cross-family models with different acceptability?

Branch table:

| Observation | Branch |
|---|---|
| Both halves pass | Proceed with cross-family as the objective (L5 theorem track) |
| Co-representation passes, discrimination fails | Take the pre-committed fallback: same-family core. Record the mechanism of the failure (where the discriminating information actually lives) |
| Co-representation fails | Fallback immediately; log which family is not co-representable, as a characterized gap |

Calibration record (2026-07-07): co-representation succeeded (pizza VM11 and RGB-pen VM10 reduce token-wise, `structural_reduces: true`); discrimination FAILED (carrier-level $D_s = 0$ for the pizza; the discriminating information lives in instantiation descriptors, which the VRPS membership gate sees and the automaton-level morphism cannot). Fallback taken. Any rerun on this same data must not re-litigate this subgate; new data may.

### 4.4 Step 4: run the exact monotonicity tests

- **T1 (order test):** for every strictly ordered pair $V_j \succ_{\mathrm{ped}} V_i$, require the acceptability value of $V_j$ to be $\ge$ that of $V_i$. Enumerate ALL strict pairs; report violations as an exact count and list.
- **T2 (discrimination test):** within each pedigree tie class, is the acceptability value constant? A tie class with a wide acceptability range means the order carries no information there even if T1 is vacuously satisfied.

Run both tests SEPARATELY for the same-family (resolution) block and the cross-family block. Carry every unpinned convention explicitly (for example: unwitnessed VMs as bottom element vs incomparable) and show the verdict under each convention; a refutation that hinges on a convention choice is not a refutation.

### 4.5 Gate-1 decision table (expected observations and branches)

| If you see | It means | Branch to |
|---|---|---|
| T1 and T2 pass in both splits | Conjecture survives contact with data | Gate 2, theorem track |
| T1 violation(s) | Either data error or genuine counterexample | Triage first: recheck violations against the double-confirmed inputs and the errata register. Data error: fix upstream, rerun Gate 1. Genuine (inputs validated): Gate 3 receives the counterexample track; Gate 2 still runs for the formal core |
| T1 vacuous (no strict pairs) but T2 fails | The extracted order is degenerate on this data; the conjecture is untestable in its graded form here, and the order carries no acceptability information | Record which sub-lemmas become empirically untestable (flag, do not silently drop); continue with the formal core; add "graded test-bed" to the known-gaps list |
| Only a two-level order (all witnessed morphisms exact, rest unwitnessed) | No graded $D_s$ spectrum exists in the data | Same as above; do NOT manufacture a spectrum by re-deriving degrees from unvalidated maps |
| Totals fail the assert | Your extraction is wrong, not the data | Fix the script; never hand-adjust a table to make totals match |

Calibration record (2026-07-07): T1 REFUTED, 5 of 45 strict-pair violations, all against VM5; robust to the bottom-element convention. T2 FAILED in both splits (same-family tie class at $D_s = 0$ spans acceptability values 0 to 30; pizza ties every flashlight VM). The pedigree order extractable from the data is two-level. Triage confirmed both inputs double-confirmed; genuine counterexample; Gate 3 took the counterexample track. Secondary finding to reuse: the monotone structure that DOES exist lives in the VMMC inclusion poset per VRPS and the descriptor-based VRPS membership gate, not in the automaton-level degree.

---

## 5. Phase 2, Gate 2: formalization

Entry condition: Gate 1 verdict recorded (pass, counterexample, or degenerate-order flag). Steps:

1. **Fix the frame.** Same-family core: commit to the abstract interpretation / Galois-connection frame ($\alpha(X) = h(X)$, $\gamma(Y) = h^{-1}(Y)$ on powersets; SD concrete, VM abstract). Cross-family: first principles; do not force the Galois frame across families.
2. **Fix verdict semantics explicitly** and state the choice as an assumption (for example the sound under-approximation $\phi^\sharp = \{b : \gamma(\{b\}) \subseteq \phi\}$). Other verdict rules move which side carries the false accepts; theorems are checkable only against a stated choice.
3. **Define acceptability-preservation** as a formal object (for the 2026-07-07 run: $\mathrm{Pres}(\mathrm{VM}) = \{\phi : \mathrm{vd}_{\mathrm{VM}}(\phi) = \mathrm{vd}_{\mathrm{SD}}(\phi)\}$, ordered by inclusion). If the empirical layer used a proxy (acceptance breadth), say so in a load-bearing-assumptions section; the formal layer is exact, the empirical layer tests the proxy.
4. **State the monotonicity theorem target with hypotheses, over the correct order.** Use kernel refinement $\trianglerighteq$, not scalar $D_s$ (see C1, C2, §8). Every hypothesis listed; every unproved step labeled a proof obligation `PO-n`.
5. **Isolate the cross-family gap** as a named object: what exactly the same-family frame cannot express (2026-07-07 finding: the gap is semantic, not metric; the instantiation-descriptor layer carried by VRPS and VMMC).

Expected observation: the frame reproduces the Gate-1 verdict qualitatively. If the formalization PREDICTS the opposite of what Gate 1 measured, one of the two is wrong; stop and find which before writing any theorem.

---

## 6. Phase 3, Gate 3: proof or characterized counterexample

Two tracks; Gate 1's verdict decides which is primary. Both tracks obey: no theorem unless all hypotheses are listed and every step is either derived from a stated definition or labeled a proof obligation. Never force a result; a failed proof step becomes a formally characterized counterexample or `BLOCKED`, never an algebraic leap.

### 6.1 Theorem track (conjecture survived Gate 1)

Prove the sub-lemma ladder in order; each lemma cites its hypotheses and its empirical instance in the pinned data:

- L1 soundness baseline (identity isomorphism preserves verdicts exactly).
- L2 coarsening is one-sided (sound; false rejects only), with the reach-compatibility induction as an explicit obligation if not written out.
- L3 blind-spot false accept (partial morphism; the load-bearing negative), with a witness pinned to data where one exists.
- L4-class degradation bound, stated over an order-compatible statistic (see the C2 repair below), with any measure-level bound left as an obligation if the data carries no measure.
- L5 cross-family extension, ONLY if the carrier subgate passed.

Machine-check every finite computation (saturation tests, DoH arithmetic, order enumerations) and say so in the ledger; "proof written, unchecked" is evidence level 4, not 5.

### 6.2 Counterexample track (Gate 1 refuted the conjecture; the 2026-07-07 path)

A counterexample is a RESULT only when characterized: stated as a theorem with hypotheses, with the mechanism identified, not just the instance. Requirements:

1. State the impossibility as a theorem whose hypotheses are exactly the pinned data facts (each machine-recomputed), for example: tie-class obstruction plus strict-pair obstruction plus the cross-family instance (T5 in the candidate document).
2. Prove robustness to every carried convention (bottom vs incomparable; proxy vs exact codomain).
3. Extract the mechanism: WHY the map fails (2026-07-07: the acceptability gate is descriptor-, structure-, and condition-aware; automaton-level $D_s$ is descriptor-invariant and degenerately zero on the data).
4. Write the honest successor conjecture with its own proof obligations, tagged CANDIDATE, never claimed (2026-07-07: the enriched pedigree object $\pi = (m, \delta, p)$, morphism plus descriptor morphism plus condition profile, with PO-3 formalize $\delta$, PO-4 derive the VMMC lattice from condition logic including the VRPS3 reversal).
5. Feed metric defects back to their owning line (2026-07-07: C2, the averaged DoH is non-monotone under refinement, goes back to the CSER 2026 isomorphism-library line regardless of Target C).

### 6.3 Gate-3 branch table

| If you see | Branch |
|---|---|
| A lemma proof needs a hypothesis the data cannot support | Label `PO-n`, keep the lemma conditional; do not weaken the claim silently |
| A synthetic counterexample kills a lemma as stated | Repair the statement over a different statistic or order (worst-granule $g_{\max}$ repaired L4); prove order-compatibility of the repair before using it |
| The counterexample dissolves under a convention change | It is not a counterexample; report the convention-dependence instead |
| Cross-family extension needs machinery that does not exist | Stop; log it as the frontier handoff (partial/approximate morphism machinery, Target A), do not improvise |

---

## 7. Phase 4, Gate 4: positioning and fencing

1. Position against, at minimum: abstract interpretation (Cousot and Cousot), approximate bisimulation (Girard and Pappas), and the Kannan-Salado belief logic (`kannan2026theory`). Anti-theater rule: every positioning claim ties to a named source AND a specific difference claim; no free-floating background.
2. R019: any citation not in the approved store gets a visible `[PLACEHOLDER]` and a reflookup/refverify action item; never a plausible-from-memory citation. (Standing items from the 2026-07-07 run: Cousot & Cousot 1977 and Girard & Pappas are `[PLACEHOLDER]`, not yet in the approved store.)
3. State the three-way split plainly: what is Wymore's (the functional-to-buildable homomorphism, the quintuple carrier), what is prior art (Galois soundness and precision; order-theoretic acceptability; belief-transfer conditions; DEVS conjoining and relaxed lumpability), what is new and CANDIDATE.
4. Tag every novelty claim that rests on "not in the literature to my knowledge" as Inferred with a literature-check action, never Established.
5. Restate the deepest framing without overclaim: whether pedigree licenses a sound projection of acceptability from model to realized system (projected fidelity); the reality-side residual is a fidelity question by definition and is not claimable from model-side data.

---

## 8. Phase 5: promotion protocol (candidate to result or retirement)

Every claim moves through this lifecycle; no claim skips a stage. Success at each stage is measurable, never judged by eye.

| Stage | Entry | Exit criterion (measurable) |
|---|---|---|
| 1. Candidate | Claim stated with hypotheses, R016-fenced, evidence-stamped | Written statement + stamp exist |
| 2. Refutation bar | Adversarial attempt to kill it: convention flips, synthetic counterexample search over small finite structures, recompute-don't-narrate on every number | All attacks enumerated and survived, OR a kill is found and the claim moves to stage 4b |
| 3. Independent check | Proof machine-checked or independently re-derived; empirical claims re-run from pinned files by a fresh session | Asserts pass on fresh run; stamp upgraded to level 5 |
| 4a. Documented result | Stages 2-3 passed | Entered in the library with rigor tag `proven` (or `SME-adjudicated` where the check is human), provenance, and its evidence-ledger row |
| 4b. Documented retirement | Killed at any stage | The kill is written up as a characterized counterexample or convention-dependence note, with the mechanism; retired claims are records, not deletions |

Standing calibration examples: the degree-only monotonicity conjecture reached 4b (T5, characterized, mechanism extracted); T4a (refinement monotonicity) sits at stage 3 pending independent check (currently level 4); C1 and C2 are machine-checked synthetic counterexamples at level 5; the enriched-pedigree conjecture $\pi = (m, \delta, p)$ is at stage 1 with PO-3/PO-4 open.

---

## 9. Known-wrong-paths fence (updated with the 2026-07-07 kills)

Refuse each of these on sight; cite the fence row when you do.

1. Using "fidelity" for the VM-to-SD relation. That is pedigree; fidelity is model to reality.
2. Collapsing the pedigree order to scalar $D_s$ and treating it as an order embedding. Killed twice: C1 (equal scalar, different preservation) and C2 (averaged DoH strictly non-monotone under kernel refinement: granules $\{1,1,10,10\}$ give $\mathrm{DoH} = 0.55$ while the strictly coarser $\{1,1,20\}$ gives $0.6833$). Use kernel refinement $\trianglerighteq$, or the worst-granule statistic $g_{\max}$, for anything order-theoretic.
3. Assuming acceptability is a total order (Kannan: incomparability is real).
4. Assuming degree of homomorphism extends across families automatically. On the settled data the carrier-level degree is descriptor-blind and degenerately zero; the discrimination lives in the VRPS/VMMC layers.
5. Claiming novelty without positioning against abstract interpretation / Galois connections.
6. Re-running the refuted degree-only conjecture on the settled 18-VM data. It is refuted there (T5); the live successors are the enriched object $\pi$ on the same data (PO-3/PO-4) or the original conjecture on NEW graded data.
7. Using "$D_b$ vanishes on the carrier" as a proof premise. It is an asserted scope justification only.
8. Treating acceptance breadth as if it were per-predicate verdict agreement without stating the proxy assumption.
9. Narrating instead of recomputing: no number enters a table unless the script computed it in this run.
10. Resolving F1 or F7 in passing. They are upstream OPEN decisions.

---

## 10. Measurable success criteria (the milestone template)

A campaign of this shape has a result when ALL of the following hold, each checkable by script or by written theorem, none by eye:

- (a) The conjecture is confirmed-or-refuted on the pinned data, separately per family split, with the violation count exact and the counterexample listed if refuted.
- (b) Either a proof (hypotheses listed, obligations labeled) that the chosen order-compatible statistic bounds verdict drift, OR a characterized counterexample stated as a theorem with hypotheses.
- (c) A stated position on whether ANY pedigree measure tracks acceptability across families, with the mechanism.
- (d) The evidence ledger is complete: every non-trivial claim has a row with source path, verification action, and a TRAK two-axis stamp.

---

## 11. Trigger examples (load this skill when)

1. "Re-run Gate 1 of the pedigree-acceptability campaign against the new federated test-bed data" (new data, same campaign shape; start at Phase 0).
2. "Attack PO-3: formalize the descriptor morphism $\delta$ and test whether the enriched pedigree object restores monotonicity" (successor conjecture; counterexample track history required).
3. "We found a monotonicity violation in the cross-tab; is it a data error or a counterexample?" (Gate-1 triage branch, §4.5).

## 12. Non-trigger examples (do NOT load this skill when)

1. "What is the difference between resolution and pedigree?" Use `morphism-domain-reference`; this runbook assumes the taxonomy.
2. "Which open problem should we attack next quarter?" Use `morphism-research-frontier`; this runbook executes a chosen target, it does not choose.
3. "Draft the related-work section of the CSER paper." Manuscript authoring is not a campaign; only Gate 4's positioning rules transfer, via the research output document, not via loading this skill.

## 13. Self-test (answer before running a campaign; answers below)

1. What are the two entry conditions for leaving Gate 1?
2. Which order do you use for the same-family monotonicity theorem, and why not scalar $D_s$?
3. The DEVS-carrier discrimination test fails on your data. What do you do?
4. Your T1 refutation disappears when unwitnessed models are treated as incomparable instead of bottom. What is the verdict?
5. What does a claim need before it may be called a documented result?

Answers: (1) the cross-tab regenerates by script with passing asserts, and the monotonicity criterion is explicitly pre-stated; (2) kernel refinement $\trianglerighteq$; scalar $D_s$ is killed by C1 (equal scalar, different preservation) and C2 (non-monotone under refinement); (3) take the pre-committed fallback (same-family core), record the failure mechanism, do not burn the window on the cross-family theorem; (4) no refutation; report convention-dependence and check whether a discrimination-test failure survives (in the 2026-07-07 run T2 still refuted tracking); (5) survival of the refutation bar plus an independent or machine check, then a library entry with rigor tag, provenance, and ledger row.

## 14. Adversarial-misuse cases (with the correct response)

**Misuse 1: "The conjecture is basically confirmed same-family; just say monotone and move on."** The same-family split of the settled data has NO strict pedigree pairs (one tie class at $D_s = 0$) and T2 fails inside it; "monotone" there is vacuous truth plus zero discrimination. Correct response: refuse the claim; report T1 as vacuous and T2 as failed, cite §4.5 row 3, and state that the graded form is untestable on this data.

**Misuse 2: "Backfill $D_s$ values for the unwitnessed VMs from their state counts so we get a graded spectrum."** That manufactures pedigree data with no witnessed morphism, violating pin 1 and fence 9, and it silently resolves an open item (homomorphism-existence for VM5/10/14/15 is untested, an F1-adjacent open note). Correct response: refuse; either exhibit and validate an actual coarser homomorphism first, or carry $\bot$ under both conventions as §4.4 requires.

## 15. Capability floor and when not to trust yourself

Floor: running this campaign requires (i) reading and hand-verifying order-theoretic proofs at the level of the partition/Galois arguments in the candidate document, (ii) writing short verification scripts with asserts, and (iii) holding the fidelity/resolution/pedigree distinction under paraphrase pressure. If you cannot re-derive why C2's arithmetic makes the averaged DoH non-monotone ($\frac{1}{4}(1+1+\frac{1}{10}+\frac{1}{10}) = 0.55 < \frac{1}{3}(1+1+\frac{1}{20}) = 0.6833$) without looking it up, you are below floor for the proof phases: still run Phases 0-1 (they are script-gated) but STOP at Gate 2 and hand off, stating "below floor for formalization."

Do not trust yourself when: a proof step feels obvious but you cannot name the definition it uses (label it `PO-n`); a number in your table did not come from this run's script (recompute); you are tempted to summarize the data's verdict from memory of a previous session (re-read the pinned files); the result you are writing is the one you hoped for (run the refutation bar twice).

## 16. Provenance and maintenance

- Authoring model: Fable 5 (claude-fable-5[1m]), Anthropic, via Claude Code, 2026-07-07; based on the Target C scope, the corpus inventory, the session notes, the ontology schema v0, and the Prompt 1 research output (all read this session, paths in the ledger below).
- Re-verify the empirical calibration record at any time (read-only, from `Papers/Dissertation_Journal/Wach_Dissertation_Journal_Publication/validation/`): run the §2.6 script of `00 Planning and Execution/Fable 5 planning/research/TargetC_pedigree_acceptability_candidate.md`; expected: asserts pass, $\sum \mathrm{acc} = 150$, T1 violations $= 5$.
- Re-verify source existence: `Test-Path` (PowerShell) on every path in the evidence ledger.
- Update triggers: new validation data (revisit §4.3 and fence 6); F1 or F7 closing upstream (revisit every row that carries their tag); PO-1..PO-4 closing (move the affected lemmas up the promotion table); the approved store gaining the Cousot or Girard-Pappas entries (clear the two `[PLACEHOLDER]` flags).
- R019 standing flags: Cousot & Cousot 1977 `[PLACEHOLDER]`; Girard & Pappas `[PLACEHOLDER]`. Run reflookup/refverify before any manuscript use.

## 17. Evidence ledger

SOURCE class {Established, Inferred, Synthetic}; LEVEL {0 irrational, 1 faith, 2 assumption/asserted, 3 self-reported, 4 proof present but unchecked, 5 direct measure / machine-checked}. Readiness and Bayesian confidence are verification-stage measures and are not computed here. Paths under `00 Planning and Execution/Fable 5 planning/` abbreviated `FP/`; under `Papers/Dissertation_Journal/Wach_Dissertation_Journal_Publication/` abbreviated `WD/`.

| # | Claim | Status | Source path | Page/line/table | Verification action | Stamp |
|---|---|---|---|---|---|---|
| 1 | Four-gate campaign structure, fallback rule, known wrong paths (original five) | Established (scope) | `FP/Target_C_Scope_Pedigree_Acceptability_Order_Morphism.md` | "Decision-gated campaign structure"; "Known wrong paths"; settled decision 4 | Read this session | Established x5 |
| 2 | Degree-only monotonicity conjecture REFUTED on settled data: T1 5/45 violations (all vs VM5), T2 failed both splits, robust to $\bot$ convention | Candidate (adverse result, reproducible) | `FP/research/TargetC_pedigree_acceptability_candidate.md` | §2.4; §2.6 script | Read this session; script + asserts specified there; not re-executed in this authoring session | Inferred x4 |
| 3 | Pedigree order on settled data is two-level (15 scoped isomorphisms at $D_s=0$; VM5/14/15 unwitnessed) | Candidate (per Prompt 1) | `FP/research/TargetC_...candidate.md`; underlying `WD/validation/v2_sd_vm.json` | §2.2; json `vm_reductions[].scoped_isomorphism` | Read candidate doc; underlying json existence verified (Glob) this session | Inferred x4 |
| 4 | DEVS-carrier subgate outcome: co-representation passed, discrimination failed, fallback taken | Candidate (gate decision) | `FP/research/TargetC_...candidate.md` | §2.5 | Read this session | Inferred x4 |
| 5 | C1, C2 counterexamples (scalar $D_s$ not an order embedding; averaged DoH non-monotone, 0.55 vs 0.6833); L4 scalar form false | Candidate (machine-checked per source) | `FP/research/TargetC_...candidate.md` | §4, C1/C2; ledger rows 15-16 | Read this session; C2 arithmetic re-verified by hand here | Synthetic x5 |
| 6 | T4a refinement monotonicity proved over kernel refinement; L4' worst-granule repair; PO-1..PO-4 open | Candidate (proved modulo obligations, per source) | `FP/research/TargetC_...candidate.md` | §3.3, §4; ledger rows 14, 17 | Read this session; proofs not independently rechecked here | Inferred x4 |
| 7 | Mechanism of failure: acceptability gate is descriptor/condition-aware; monotone structure lives in VMMC inclusion poset + VRPS membership | Candidate | `FP/research/TargetC_...candidate.md` | §2.4 (secondary), §3.4, T5 characterization | Read this session | Inferred x4 |
| 8 | Enriched-pedigree successor conjecture $\pi = (m, \delta, p)$, stage-1 candidate | Conjecture (open) | `FP/research/TargetC_...candidate.md` | §4 end | Read this session; carried as CANDIDATE only | Inferred x2 |
| 9 | Identities matrix double-confirmed 120/120; 150 acceptable tuples; errata E2/E10 immaterial | Validated (upstream) | `WD/validation/v4_identities_reconciliation.md`; `WD/analysis/errata_register.md` | per candidate doc rows 1, 21 | File existence verified (Glob) this session; contents relied on via Prompt 1's ledger, not re-read here | Established x4 |
| 10 | DoH formula and $D_s$ convention caveat | Established (definition) | `Papers/SE_Math_Foundations/isomorphism-library/paper/Wach_Sandmann_Iyer_CSER2026_Isomorphism_Library_Draft_v1.md` | Eq. (3), per candidate doc row 22 | File existence verified (Glob); formula transcribed from candidate doc | Established x4 |
| 11 | Terminology (fidelity/resolution/pedigree/projected fidelity); "$D_b$ vanishes on carrier" is asserted, not axiom | Established (governing) | `FP/Target_C_Scope_...md`; `FP/SESSION_NOTES_2026-07-07_...md`; `FP/Morphism_Library_Ontology_Schema_v0.md` | Terminology section; Capsules 2.2-2.4; flag D-5 | Read all three this session | Established x5 |
| 12 | Rigor tags (proven / SME-adjudicated / asserted); most corpus content asserted | Established | `FP/Morphism_Library_Corpus_Inventory_v0.md` | Rigor levels section | Read this session | Established x5 |
| 13 | Approved-store keys used (`salado2018mathematical`, `kannan2019preference`, `kannan2026theory`); Cousot and Girard-Pappas NOT in store | Flagged | candidate doc ledger rows 23-25; `04 Resource Library/00 Verified References/approved.bib` | §5, §7 | Keys taken from candidate doc; store not independently re-opened here; reflookup/refverify before manuscript use (R019) | Established x3 |
| 14 | F1 and F7 are OPEN; this skill and its campaigns must not resolve them | Compliance | `FP/Fable_Authoring_Prompts.md` (guardrail); candidate doc row 27 | GUARDRAILS; §7 | Read both this session | Established x5 |
| 15 | Sibling skills not yet present in `.claude/skills/` at authoring time | Observation | skills root glob | this session | Glob returned no `morphism-*` matches | Established x5 |
