---
name: morphism-research-methodology
description: >-
  The research discipline for the systems-engineering (SE) morphism library: how a hunch about a
  morphism, a degree metric, an order relation, or a cross-domain correspondence becomes an accepted
  result or a documented retirement. Load when you are about to test a conjecture against data,
  decide whether a candidate result can be promoted or must be retired, state a hypothesis before an
  empirical run, react to an adverse or refuting result, or tag the rigor level of a library entry
  (proven / SME-adjudicated / asserted). Covers the evidence bar, predict-numbers-before-running,
  the candidate lifecycle, R016 fencing, TRAK two-axis evidence stamps, and the recompute-do-not-narrate
  rule with the F7 false-narrative catch as the worked example. Do NOT load for domain definitions
  (use morphism-domain-reference), for the Target C gate sequence (use morphism-verification-campaign),
  for open-problem selection or state-of-the-art positioning (use morphism-research-frontier), or for
  citation verification (use reflookup / refverify).
---

# Morphism Research Methodology

**Status tag [R016]: research artifact.** This skill encodes a working method, validated on one
research line (the dissertation validation campaign and the Target C attempt, both 2026-07-07). It is
not a demonstrated capability on any other line, and nothing in it converts a candidate result into a
proven one by itself.

PROVENANCE: produced by Fable 5 (claude-fable-5[1m]), vendor Anthropic, access mode Claude Code CLI
(subagent run at the principal's direction), 2026-07-07. Sources: the Fable 5 planning ground-truth
set (`Target_C_Scope_Pedigree_Acceptability_Order_Morphism.md`, `Morphism_Library_Corpus_Inventory_v0.md`,
`SESSION_NOTES_2026-07-07_Fable5_and_Morphism_Library.md`, `Morphism_Library_Ontology_Schema_v0.md`),
the Prompt 1 research output (`research/TargetC_pedigree_acceptability_candidate.md`), and the
dissertation errata register (`Papers/Dissertation_Journal/Wach_Dissertation_Journal_Publication/analysis/errata_register.md`),
all read-only.

Open dissertation decisions **F1 (infinite-equivalence wording) and F7 (graded-gate rewrite) are OPEN**.
This skill cites the F7 *catch* as a historical event (it happened and is registered); it does not
resolve the F7 manuscript rewrite or the F1 wording, and no step below may be read as resolving them.

## 0. Currency update — 2026-07-10, amended 2026-07-11 (read first)

PROVENANCE: Opus 4.8 (claude-opus-4-8[1m]), Anthropic, Claude Code CLI, 2026-07-10, amended 2026-07-11; principal-directed. Sections 1-13 are the 2026-07-07 Fable 5 authoring and stay valid except as amended here. Now governed by global **[R020] skills-first**; all sibling morphism skills now exist (the Section 2 "domain-reference not yet present" note and ledger row 13 are stale).

Amendments:
- **RBW (red/blue/white) is the concrete instantiation of Step 5 (adversarial refutation).** The 2026-07-10/11 runs hardened the prompt, ran three independent adversarial legs — red = Codex, blue = Gemini, white = Opus — adjudicated, derived with Fable, then ran a Codex domain-critic before promotion. Read Step 5's "vary every convention / search for the minimal counterexample" as: use independent multi-model legs where available. A leg returning REWORK / FIX-THEN-READY is the process working (the bridge and Target A both returned honest REWORK and were reframed, not forced).
- **The lifecycle has now been exercised end-to-end.** The bridge, **Target A** (nonlinear-from-partial), and the **positioned-integration / harmonization** all reached CLOSED (Codex domain-critic CLOSED, 2026-07-11) — derivation campaigns where Gate 1's empirical cross-tab is replaced by a finite self-asserting executable witness with predicted-numbers-before-running. Interface-first (Target B) remains un-exercised.
- **Proof-status category** (new tagging concept, research seed): beyond the entry-level rigor tags of Section 3, a drawn ontology relationship carries a proof-status — drawn/unproven | proven-to-degree (carries its `(D_s, D_b)` as proof strength + R018) | refuted. The relationship-level analogue of the R016 fence, and the promotion gate applied to ontology edges.

Fences: F1/F7 remain OPEN; "recompute, do not narrate" (Section 4) and the never-force rule (Step 5) are unchanged and were honored. **R019 update: the standing Girard-Pappas and Cousot `[PLACEHOLDER]` flags are CLEARED (2026-07-11)** — `girard2007metrics`, `cousot1977absint`, and the Cody dissertation `cody2021transferdiss` were promoted to the approved store via `refverify` (single-model triple-check; `pending_byzantine_verification: true`).

---

## 1. Purpose

One sentence: this skill is the promotion gate between "I noticed something" and "the library asserts
something," for the morphism library and its research targets (Targets A, B, C).

The corpus this library grows from is mostly *asserted*, not proven: the four-type morphism taxonomy,
the metamodel, the cross-domain analogies, and the problem-space-formalization (PSF) infeasibility
claim all defer their formal conditions (corpus inventory, Rigor section). The one canonical exact
definition (Salado-Kannan 2018 Definition 2, approved reference key `salado2018mathematical`) was
itself found only on a second, deeper corpus pass. A library built by language models on such a corpus
will silently promote assertion to fact unless the methodology forbids it structurally. This skill is
that prohibition, written as an executable discipline.

## 2. When to load this skill

**Trigger examples (load it):**
1. "I think the partial/approximate homomorphism structure of this pair hints at an underlying
   nonlinear morphism. How do I test that without fooling myself?" (Target A shaped hunch entering
   the lifecycle.)
2. "The Gate-1 run refuted the monotonicity conjecture. What is the correct next move: patch the
   conjecture, blame the data, or write the counterexample up?" (Adverse-result handling.)
3. "Can this D_s result go into the paper as a result, or is it still a candidate? What rigor tag
   does the library entry get?" (Promotion / tagging decision.)

**Non-trigger examples (do not load it; use the named sibling):**
1. "What is the degree-of-homomorphism formula, and which of $D_s$ and $D_b$ applies on the Discrete
   Event System Specification (DEVS) carrier?" Definitions and taxonomy live in
   `morphism-domain-reference`.
2. "Run the pedigree-vs-acceptability campaign on the 18-VM data." The gate-by-gate runbook is
   `morphism-verification-campaign`.
3. "Which open problem should the next research window attack, and how does it position against
   abstract interpretation?" Target selection and positioning live in `morphism-research-frontier`.
   (Citation existence checks are `reflookup` / `refverify`; the render gate is `refcheck`.)

Sibling note: at authoring time (2026-07-07, verified by directory listing),
`morphism-research-frontier` and `morphism-verification-campaign` exist under `.claude/skills/`;
`morphism-domain-reference` (Prompt 2 of the same authoring plan) was not yet present. If a routed
sibling is missing when you need it, emit `BLOCKED: missing <skill>` rather than improvising its
content here.

## 3. Governing definitions

Define once; every later step uses these terms exactly.

**Hunch.** An untagged observation or analogy with no operational test attached. Hunches are free;
they carry no rights.

**Hypothesis (admissible).** A statement that *predicts numbers before running*: it names, in advance,
(i) the exact computation, (ii) the exact inputs pinned to files/rows, and (iii) the numeric or
set-valued outcome it forbids. A statement that cannot forbid an outcome is not admissible as a
hypothesis; send it back to hunch status.

**Evidence bar (the acceptance criterion).** A candidate result is accepted only when a *single
stated mechanism* explains *all* observations in scope, including the negatives and the anomalies,
and has *survived adversarial refutation* (Section 5, step 5). Partial explanations that fit the
positives but wave at the negatives do not pass. This is the bar the validation campaign actually
enforced: the F7 catch (Section 7) is what happens when a narrative fits the story but not the grids.

**Rigor levels (library entry tags, from the corpus inventory).**

| Tag | Meaning | Examples in this line |
|---|---|---|
| `proven` | In-framework proof written out; every hypothesis listed; steps derived or discharged | Kannan 2019's seven order-theoretic theorems (`kannan2019preference`); Shadab closed-systems Props 1-2 + Thm 1 (corpus inventory, Rigor section) |
| `SME-adjudicated` | Verdict rests on subject-matter-expert (SME) judgment plus partial tool validation | The dissertation morphism proofs (MS4 Me / DEVS), incl. pizza-VM to flashlight-SD (corpus inventory) |
| `asserted` | Stated in a source with the formal conditions deferred | The four-type taxonomy; the metamodel; the PSF infeasibility claim; all cross-domain analogies; "$D_b$ vanishes on the DEVS carrier" (ontology schema flag D-5) |

**TRAK two-axis evidence stamp (claim-level, finer than the entry-level rigor tag).** Stamp every
non-trivial claim with a SOURCE class {Established | Inferred | Synthetic} AND an evidence LEVEL
{0 Irrational | 1 Faith | 2 Assumption | 3 Self-reported | 4 Indirect measure | 5 Direct measure}.
For mathematical claims read the level as: 5 = independently or machine-checked proof, 4 = proof
present but unchecked, 2 = asserted, 0 = contradiction. Mapping to the entry tags: `proven` requires
level 4-5 on the load-bearing claims; `SME-adjudicated` is level 3-4; `asserted` is level 2. GRL
readiness and Bayesian confidence are verification-stage instruments; do NOT compute them during
research authoring.

**Candidate lifecycle (the only legal states).**

| State | Entry condition | Exit condition | Illegal shortcut this state exists to block |
|---|---|---|---|
| 1. Hunch | Free | Operationalized into an admissible hypothesis, or dropped | Citing a hunch in prose as if tested |
| 2. Experiment-flagged hypothesis | Predicts numbers; inputs pinned; forbidden outcome stated | Run executed exactly as pre-stated | Moving the goalposts after seeing data |
| 3. Candidate result (fenced per R016) | Run complete; outcome recorded, favorable or adverse | Passes the evidence bar AND the refutation attempt | Presenting a candidate as a result in any external artifact |
| 4a. Adopted result | Survived step 5 refutation; mechanism explains all observations incl. negatives; ledger row at level 4-5 | Only by later refutation (results are permanently refutable) | Adopting on repetition ("three sessions agree") instead of refutation |
| 4b. Documented retirement | Refuted, or evidence bar unreachable with available data | None; retirements are permanent records, not deletions | Silent deletion of a failed idea (loses the negative, invites re-derivation) |

An adverse outcome at state 3 is not a failure of the process; it is the process working. The Target C
attempt ended in state 4b for the degree-only conjecture and produced two NEW machine-checked
counterexamples (C1, C2) worth more than a weak confirmation would have been
(`research/TargetC_pedigree_acceptability_candidate.md` §4).

## 4. The core rule: recompute, do not narrate

State it as an imperative pair.

1. **Never source a load-bearing number, verdict, or adherence pattern from a summary artifact**
   (a summary markdown, a figure-generator dict, a prior session's prose, your own memory of the
   result). Summaries describe; base specifications and validated grids define.
2. **Recompute from the pinned base source through a frozen or version-pinned tool, or emit
   `BLOCKED: missing <path/id>` and stop that branch.** Never continue by inference. A wrong number
   with a confident narrative is strictly worse than a `BLOCKED`.

Corollaries:
- If two artifacts disagree, neither wins by seniority; the one that recomputes from base
  specifications wins, and the disagreement gets an errata-register entry.
- If a defect is found, trace its propagation forward (prose, tables, figures, theorem witnesses)
  before fixing anything; the F7 chain (Section 7) contaminated four artifact types from one file.
- "Documented-immaterial" is a legal disposition (errata register F6): show the anomaly cannot reach
  the result (e.g., E10 touches zero matrix cells) and record it so no future reader chases it.

## 5. The runbook: hunch to accepted result

Execute in order. Each step has a hard exit criterion; do not proceed past a failed criterion.

**Step 0. Tag the inputs before trusting them.** List every source the hunch rests on and its rigor
tag (`proven` / `SME-adjudicated` / `asserted`). If a load-bearing input is `asserted` (for example
"$D_b$ vanishes on the carrier," Target C settled decision 3), you may use it to *scope* the work but
never as a *premise of a proof*; record that restriction explicitly. Exit criterion: an input table
with tags, no untagged input.

**Step 1. Operationalize: make the hypothesis predict numbers.** Write down, before touching data:
the exact statistic or test, the exact codomain, and the outcome the hypothesis forbids. Worked
instance (the model to copy): before the Gate-1 run, the monotonicity conjecture was operationalized
as test T1, "for every strictly ordered pair $V_j \succ_{\mathrm{ped}} V_i$, require
$\mathrm{acc}(V_j) \ge \mathrm{acc}(V_i)$," with $\mathrm{acc}$ defined as the acceptable-tuple count
and the prediction "zero violations among the 45 strict pairs." The run found 5 violations; because
the test was pre-stated, that was a refutation, not a negotiation
(`TargetC_pedigree_acceptability_candidate.md` §2.1, §2.4). Exit criterion: a written test that a
hostile reader could run without asking you anything.

**Step 2. Pin every operational definition to a file and row.** For each quantity in the test, name
the extraction rule and the exact source location (file, key, line, table). The Gate-1 pin table
(four pins: the $D_s$ extraction rule, the family-label source, the acceptability-verdict source, the
exact monotonicity test, each with file/row) is the template. If any pin cannot land, emit
`BLOCKED: missing <path/definition>` and stop. Also run the known-defect screen: check the errata
register for entries touching your pinned inputs before using them. Exit criterion: a pin table with
zero unpinned rows, plus a defect-screen line.

**Step 3. Run, and make the run reproducible.** Recompute (Section 4); never transcribe. Ship the
minimal script that regenerates every table from the pinned read-only inputs, with at least one
self-checking assertion (the Gate-1 script asserts $\sum \mathrm{acc} = 150$ and the violation count).
Distinguish observed data from constructed witnesses: a counterexample you build is stamped Synthetic
and labeled "constructed, not observed." Exit criterion: script runs from the pinned files alone;
assertions pass; every table in the write-up regenerates.

**Step 4. Apply the evidence bar.** Ask: does ONE stated mechanism explain every observation in
scope, including the negatives and the anomalies? Enumerate the observations the mechanism must
cover, negatives first. If the mechanism explains the confirmations but needs a second story for the
anomalies, you do not have a result; you have two hunches. Worked instance: the T5 characterization
did not stop at "5 violating pairs exist"; it named the mechanism (the acceptability gate is
descriptor- and condition-aware while automaton-level $D_s$ is descriptor-blind and degenerately
zero) and showed the same mechanism covers the same-family tie-class failure, the cross-family
pizza tie, AND the descriptor-exclusion facts F2 already established upstream
(`TargetC_..._candidate.md` §4 T5; errata register F2). Exit criterion: a mechanism paragraph plus an
observation checklist with no uncovered row.

**Step 5. Attempt the refutation yourself, adversarially.** Before anyone else sees the candidate:
- Vary every convention the result might secretly depend on (the T1 refutation was re-run under both
  $\bot$ conventions for unwitnessed morphisms and survived both; §2.4 robustness).
- Search for the minimal counterexample to your own claim; machine-check it (C1 and C2 in the Target C
  attempt are refutations of a metric's implied claims, found and machine-checked in-session).
- For a proof: list all hypotheses; every step is either derived from a stated definition or labeled
  a numbered proof obligation (PO-n). "No theorem unless all hypotheses are listed." Never force a
  step; a failed step becomes a formally characterized counterexample or a PO, not an algebraic leap.
- For an empirical claim: state the load-bearing assumptions in their own section (the Target C
  attempt carries six, §6), including proxy assumptions (acceptance breadth proxying
  acceptability-preservation is assumption 1 there, and it is flagged as reopening-relevant).
Exit criterion: a written refutation attempt with its outcome; open obligations numbered; assumptions
sectioned.

**Step 6. Promote or retire, and stamp.**
- Survived step 5 with all load-bearing claims at level 4-5: promote to *adopted result*; rigor tag
  per Section 3; ledger rows for every non-trivial claim.
- Refuted: write the refutation up as a first-class object (a characterized counterexample stated as
  a theorem with hypotheses is a RESULT; T5 is the exemplar), record the retirement, and extract the
  surviving successor conjecture honestly labeled as open (the enriched-pedigree conjecture
  $\pi = (m, \delta, p)$ with PO-3/PO-4 is the exemplar; it is explicitly "not claimed as a result").
- Neither: the candidate stays fenced at state 3 with its blocking obligation named, or retires as
  "evidence bar unreachable with available data" (the L4' drift bound retired to PO-2 status because
  the settled data has no graded $D_s$ spectrum; §2.2, §7 of the Prompt 1 output).
- Every output ends with the evidence ledger: [claim | status | source path | page/line/table |
  verification action | stamp]. External use additionally requires R019: citations exist in the
  approved store or carry a visible `[PLACEHOLDER]`; never draft a plausible-from-memory citation.

## 6. R016 fencing (what may be said where)

| Artifact | May state | Must not state |
|---|---|---|
| Library entry | Anything, with the correct rigor tag and stamp | An `asserted` entry phrased as established fact |
| Internal research note | Candidates, refutations, hunches, all fenced | An unfenced candidate (someone will quote it) |
| Skill / runbook | Method plus tagged examples | A candidate result baked in as a step's premise |
| Manuscript | Adopted results; candidates only if visibly labeled candidate/open | Any bibliography entry not in the approved store (R019); any resolution of OPEN decisions (F1, F7) |

Integration-status fencing (R016 proper): every asset referenced is (a) research artifact,
(b) demonstrated capability, or (c) integrated deliverable; never present (a) as (b) or (c). The
morphism library content is, at this writing, (a) nearly everywhere.

## 7. Worked example: the F7 catch, or why recompute-don't-narrate is the load-bearing rule

The facts, pinned to the errata register (read-only; entries E5, E6, F7):

1. A derived summary file, `analysis/morphism_summary.md` §5, was systemically corrupted relative to
   the base adherence Tables 82-87: rows dropped, adherence invented, true adherence erased (entry E5).
2. From that corrupted summary, a clean, satisfying *narrative* was built: "the blue models (VM8/VM9)
   adhere to NO verification-model morphism condition (VMMC); the VRPS4 acceptable set is EMPTY,"
   an over-constraint finding (D22). The narrative propagated into the manuscript prose, a worked-example
   table (`tab:combined-worked`), a figure-generator dict (`article_figures.py` VMMC_TO_VM, entry E6),
   and a theorem's necessity witness. Four artifact types contaminated from one unrecomputed file.
3. The independent recompute wave (V3-VMMC re-derivation, 430/432 base cells; V4 identities matrix,
   120/120 double-confirmed) caught it: VM8/VM9 in fact ADHERE to VMMC3 (SD3, SD4) and VMMC6 (all
   system designs) and are acceptable in those contexts. The "empty acceptable set" finding was
   RETRACTED for VRPS4 (register entry F7). The correct story is conditional admission under the
   homomorphism-level conditions and exclusion under the stricter isomorphism-level ones.
4. The manuscript rewrite that follows from this (the graded-gate rewrite) is decision F7 and is
   **OPEN**; the register itself says "do NOT silently reconstruct." This skill takes no position on it.

Read the mechanism, not just the moral. The false narrative was *internally coherent*, *stylistically
strong*, and *wrong at 100% of its load-bearing cells for VM8/VM9's admissible conditions*. No amount
of narrative review could have caught it, because every reviewer downstream of the corrupted summary
saw a consistent story. Only recomputation from base specifications through frozen tools could, and
did. Hence the rule's exact form: the prohibition is on *narrating from derived artifacts*, not on
narration as such. And note what the catch cost: the recompute wave was independent, double-entry
(sweep-derived vs recompute-derived, 120/120 agreement), and cheap relative to one shipped false
claim. Every step-3 "make the run reproducible" requirement above is this lesson, operationalized.

## 8. Where good ideas historically came from in this line

Seven recurring generators, each pinned to an instance. Use them as prompts when hunting, not as
guarantees.

| # | Generator | Instance (pinned) |
|---|---|---|
| 1 | **Split a conflated term.** When one word carries three concepts, separate them and give each a formal home | "Fidelity" split into fidelity (model to reality), resolution (within-family), pedigree (cross-family model to model); verification/validation alignment fell out immediately (session notes Capsule 2.2; Target C scope, Terminology) |
| 2 | **Find the gap at the intersection of proven results.** Two rigorous bodies that do not cross are a theorem-shaped hole | Target C itself: Kannan 2019 has the acceptability order but no maps between ordered structures; Salado-Kannan 2018 has the exact morphism but no order; Kannan-Salado 2026 black-boxes the system-model relation inside one implication. The monotone weld between them was unclaimed (corpus inventory, Tier-2 findings) |
| 3 | **Honor the negative result; it usually contains the next object.** | Infinite equivalence (raw automaton-level pedigree is non-discriminating) motivated degree-pedigree, i.e., Target C's real question (Target C scope, Motivation); the T5 refutation yielded the enriched-pedigree object $\pi = (m, \delta, p)$; the C2 counterexample is a NEW metric defect feeding back to the CSER 2026 line (Prompt 1 output §4) |
| 4 | **Look for the one premise that unifies separate bets.** | "There is no single SD; reality is a buildable federation" made cross-family pedigree, interfaces-as-first-class, and the DEVS carrier consequences of one premise instead of three risks (session notes Capsule 2.5) |
| 5 | **Relocate the hardness rather than fight it.** | The DEVS-carrier move relocates cross-family difficulty from the metric to the construction (DEVS-ification), whose residual is a fidelity question, keeping pedigree clean (Target C scope, settled decision 4). Caveat from the attempt: the strong form failed on the settled data because the carrier is descriptor-blind; the relocation survives, the strong bet did not (Prompt 1 output §2.5) |
| 6 | **Ask what the object is FOR.** Purpose questions expose the deepest framing | "Pedigree's whole purpose is to license projected fidelity" reframed Target C from a metric exercise to a soundness-of-projection question (session notes Capsule 2.4) |
| 7 | **Check the foundations before claiming novelty.** A deeper corpus pass often finds the founding move already made | Tier 2 found Salado-Kannan 2018 Def. 2 (correcting "conditions are deferred throughout") and Wymore's functional-to-buildable homomorphism as the founding pedigree move; the honest novelty line is "extend, not invent" (corpus inventory Tier-2 correction; session notes Capsule 2.6) |

## 9. Capability floor and guard ("when not to trust yourself")

**Floor.** Executing this skill requires: (i) writing and running short verification scripts (Python)
against pinned JSON/markdown sources in-session; (ii) holding a multi-step order-theoretic or
algebraic argument without dropping hypotheses; (iii) distinguishing your recollection of a result
from a recomputation of it. A model or session that cannot do all three is below floor for
promotion decisions (steps 3-6). Below floor, you may still do steps 0-2 (tagging, operationalizing,
pinning), then hand off with the pin table and STOP.

**Guards. Stop and either recompute or emit `BLOCKED` when any of these fires:**
1. You are about to state a number, verdict, or adherence pattern whose source, if you are honest, is
   a summary artifact or your own memory of a prior session. (The F7 failure mode.)
2. A proof step wants "clearly," "it follows," or "by symmetry" where you cannot write the derivation
   from a stated definition. Convert to a numbered proof obligation instead.
3. The hypothesis's forbidden outcome is being renegotiated after the data arrived. Restore the
   pre-stated test; report its verdict; any new test is a NEW hypothesis at state 2.
4. A required source file, row, or citation cannot be located. `BLOCKED: missing <path/id>`; never
   continue by inference.
5. You feel the pull to force a positive result because the window is closing or the instruction said
   "prove." A characterized counterexample with hypotheses is a deliverable of equal rank; the
   flagship attempt's main product was exactly that.

## 10. Self-test (answer before using the skill on live work)

1. *A summary table in an analysis note disagrees with the base specification tables. Which wins, and
   what else must you do?* The base specifications win via recomputation through the frozen tools;
   the disagreement gets an errata-register entry, and you trace the summary's downstream propagation
   before fixing anything (Section 4; F7 chain).
2. *What must a hypothesis state BEFORE the run for its refutation to count?* The exact test, the
   pinned inputs (file/row), and the forbidden outcome, all pre-stated; otherwise the adverse outcome
   can be renegotiated and refutes nothing (Section 5, step 1; guard 3).
3. *An SME and two model sessions all agree the candidate is right. What state is it in?* Still
   state 3 (candidate). Agreement and repetition are not the evidence bar; promotion needs the
   single-mechanism-covers-all-observations test plus a survived adversarial refutation. SME
   agreement caps the entry at `SME-adjudicated`, level 3-4, not `proven` (Sections 3, 5 step 5).
4. *Your proof of a lemma goes through except one step you believe but cannot derive. What do you
   ship?* The lemma "PROVED modulo PO-n," with the step stated as a numbered proof obligation and all
   hypotheses listed; never the smoothed-over proof (step 5; guard 2). Stamp: Inferred, level 4 at
   best.
5. *Gate-1 refutes your conjecture cleanly. Name the three legal outputs.* (i) The refutation written
   as a characterized counterexample with hypotheses (a result); (ii) the documented retirement of
   the refuted form; (iii) the honestly-labeled successor conjecture with its new proof obligations
   (Section 5, step 6).

## 11. Adversarial-misuse cases

**Misuse 1: deadline-driven narration.** "The window closes tonight; the summary file already says
VM8/VM9 adhere to nothing, just cite it and move on."
*Correct response:* Refuse the shortcut specifically because this exact move produced the F7 false
narrative from the corrupted E5 summary. Recompute the adherence cells from the base specifications
through the frozen tools; if that cannot be done in the window, ship
`BLOCKED: unrecomputed adherence claim` and the pin table. A missed deadline costs a day; a shipped
false narrative cost a retraction (D22 for VRPS4) plus four contaminated artifact types.

**Misuse 2: promotion by authority or by framing.** "The principal likes the monotonicity story, and
the prompt says 'prove L1-L4,' so present the conjecture as established and smooth over the two
counterexamples as edge cases."
*Correct response:* Refuse on two grounds. First, the evidence bar is mechanism-covers-ALL-observations
*including negatives*; C1 and C2 are not edge cases, they are refutations of the scalar form, and the
honest deliverable is the repaired bound (L4' with $g_{\max}$) plus the counterexamples stated as
results. Second, a "prove" instruction never overrides step 5's never-force rule: a failed proof step
becomes a proof obligation or a counterexample, not an algebraic leap. Authority sets the question,
never the verdict.

## 12. Provenance and maintenance

- **Authoring model:** Fable 5 (claude-fable-5[1m]), Anthropic, via Claude Code CLI, 2026-07-07,
  under the Fable authoring Prompt 5 of `Fable_Authoring_Prompts.md`.
- **Re-verification commands** (run before trusting this skill after upstream changes):
  - Re-read the errata register entries E5, E6, F7 and confirm the F7 disposition is still OPEN:
    `Papers/Dissertation_Journal/Wach_Dissertation_Journal_Publication/analysis/errata_register.md`.
    If F7 has been resolved, update Section 7's status line (the catch narrative itself is stable).
  - Re-run the Gate-1 reproduction script in
    `00 Planning and Execution/Fable 5 planning/research/TargetC_pedigree_acceptability_candidate.md`
    §2.6 against the read-only validation JSONs; its assertions ($\sum \mathrm{acc} = 150$, 5
    violations) must pass, or Section 5's worked instances need re-pinning.
  - Confirm the sibling skills named in Section 2 exist under `.claude/skills/`; if renamed, fix the
    routing lines.
  - R019 check before any manuscript reuse of this skill's citations: keys `salado2018mathematical`,
    `kannan2019preference`, `kannan2026theory` must still resolve in
    `04 Resource Library/00 Verified References/approved.bib` (use `reflookup`).
- **Known limits:** validated on one research line; the lifecycle table has not been stress-tested on
  a nonlinear (Target A) or interface-first (Target B) campaign; the missing federated
  multi-discipline test-bed limits every empirical step to the single-SD flashlight toy (known gap,
  session notes Open items).

## 13. Evidence ledger

Source classes: Established (verbatim from a validated/ground-truth source), Inferred (derived here
from established inputs), Synthetic (constructed here). Levels: 0 irrational, 1 faith, 2 assumption/
asserted, 3 self-reported, 4 indirect measure / proof present but unchecked, 5 direct measure /
machine-checked. GRL readiness and Bayesian confidence are verification-stage only and are not
computed here.

| # | Claim | Status | Source path | Page/line/table | Verification action | Stamp |
|---|---|---|---|---|---|---|
| 1 | Corpus is mostly asserted or SME-adjudicated, rarely proven; rigor triple {proven, SME-adjudicated, asserted} | Established | `Morphism_Library_Corpus_Inventory_v0.md` | Rigor levels section | Re-read this session | Established x 5 |
| 2 | Salado-Kannan 2018 Def. 2 found on the Tier-2 pass, correcting "conditions deferred throughout" | Established | same file | Tier-2 correction to Finding 4 | Re-read this session | Established x 5 |
| 3 | E5: `morphism_summary.md` §5 systemically corrupted vs base Tables 82-87 | Established | `analysis/errata_register.md` | entry E5 | Re-read this session | Established x 5 |
| 4 | F7: "blue models adhere to no condition / VRPS4 empty" narrative FALSE, from E5; VM8/VM9 adhere VMMC3 (SD3,SD4) + VMMC6 (all); D22 retracted for VRPS4; rewrite decision OPEN, "do NOT silently reconstruct" | Established | same file | entry F7 | Re-read this session; quoted conservatively | Established x 5 |
| 5 | E6: figure dict corrupt both directions, matching E5 pattern; four artifact types contaminated (prose, table, figure dict, theorem witness) | Established | same file | entries E6, F7 | Re-read; artifact-type count tallied from E5/E6/F7 text | Established x 5 |
| 6 | Recompute wave: V3-VMMC 430/432; V4 identities matrix 120/120 double-confirmed; caught F7 | Established | same file; `validation/v4_identities_reconciliation.md` (per Prompt 1 output row 1) | F5, F7, V4 lines | Register re-read; matrix numbers cross-match Prompt 1 output ledger row 1 | Established x 5 |
| 7 | Gate-1 pin-table method, T1 pre-stated test, 5/45 violations, robustness to $\bot$ convention | Established | `research/TargetC_pedigree_acceptability_candidate.md` | §2.1, §2.4, §2.6 | Read this session; script and assertions quoted, not re-run here | Established x 4 |
| 8 | C1/C2 machine-checked counterexamples; T5 refutation with descriptor/condition mechanism; enriched conjecture $\pi=(m,\delta,p)$ open; L4' retired to PO-2 on this data | Established | same file | §4, §2.2, §7 | Read this session (their internal stamps: Synthetic/Inferred x 4-5) | Established x 4 |
| 9 | F1 and F7 are OPEN; this skill does not resolve them | Established | `errata_register.md`; Prompt 1 output header | F1, F7 entries; header | Both re-read; skill text checked for accidental resolution | Established x 5 |
| 10 | Idea-generator instances (term split, gap-at-intersection, negative-result, federation premise, hardness relocation, purpose question, foundations check) | Established | `SESSION_NOTES_2026-07-07...md`; Target C scope; corpus inventory | Capsules 2.2-2.6; Motivation; Tier-2 | Each row of §8 pinned to its capsule/section this session | Established x 4 |
| 11 | "$D_b$ vanishes on carrier" is asserted, not an axiom; usable for scoping only | Established | Target C scope; `Morphism_Library_Ontology_Schema_v0.md` | settled decision 3; flag D-5 | Re-read both | Established x 2 (the claim itself is an assumption; its *status as asserted* is x 5) |
| 12 | Lifecycle table, evidence bar, floor/guards as stated | Method (this skill) | this file | §3, §5, §9 | Synthesized from prompts-file hardening rules + observed campaign practice; not independently validated beyond the one line (§12 known limits) | Synthetic x 3 |
| 13 | Sibling status at authoring time: frontier and campaign skills present; domain-reference not yet present | Established | skills root directory listing | `morphism-research-frontier/`, `morphism-verification-campaign/` exist; no `morphism-domain-reference/` | Listed this session (parallel authoring runs landed mid-session); routing fenced with a BLOCKED instruction | Established x 5 |
| 14 | Approved-store keys `salado2018mathematical`, `kannan2019preference`, `kannan2026theory` exist | Inherited | Prompt 1 output ledger rows 23-24 | §1, §5 there | Not independently re-opened this session; re-verify via `reflookup` before manuscript use (R019) | Established x 4 |
