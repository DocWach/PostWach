---
name: red-blue-white
description: >-
  Configure and run a Red-Blue-White (RBW) adversarial-verification protocol to stress-test a
  load-bearing CLAIM or DECISION before it is committed. RED tries to REFUTE the claim (find a
  counterexample/defeater); BLUE is the claim/decision on record (its author, not required to argue
  live); WHITE independently ADJUDICATES whether any RED finding actually defeats the claim or is a
  false alarm. Load when stress-testing a load-bearing claim or decision before committing it,
  especially reviewer-facing claims, claims that REVERSE a prior decision, or a subordinate/hive
  deliverable you are about to rely on. Do NOT load for trivial/low-stakes checks, a fact already
  verified by two independent objective sources, purely conversational turns, or when a single
  objective tool already settles it. Contrast with dialectical-synthesis (single-mind
  thesis/antithesis, NOT multi-agent adversarial).
---

# Red-Blue-White (RBW)

**Integration status (R016): (a) research artifact.** New skill, codifying a pattern the portfolio
has run repeatedly (the 2026-07-10/11 morphism RBW legs; a fixed 5-round RBW; the 2026-07-16 P1 claim
check). It is not yet reused THROUGH this codification. Promote to **(b) demonstrated capability**
after the first real run driven by this skill.

PROVENANCE: produced by Opus 4.8 (claude-opus-4-8[1m]), vendor Anthropic, access mode Claude Code CLI,
PostWach-principal-directed, 2026-07-16.

RBW is the concrete instantiation of the "attempt the refutation yourself, adversarially" step in
[[morphism-research-methodology]] Step 5, generalized to any load-bearing claim. Where that skill sets
the evidence bar, this one lays out the ROLES, the INDEPENDENCE topology, and the CONFIGURABLE variants.

## 1. What RBW is (and its non-negotiable invariants)

A multi-agent adversarial protocol to stress-test a load-bearing claim/decision before commit. Three
roles plus a backstop:

- **RED** — tries hard to REFUTE the claim: find a counterexample, a defeater, a construct that the
  claim says cannot exist. RED's job is to be adversarial, not fair.
- **BLUE** — the claim/decision ON RECORD (its author, or the standing position). BLUE does **not**
  need to argue live; the recorded claim is what RED attacks and WHITE judges.
- **WHITE** — INDEPENDENTLY ADJUDICATES each RED finding: does it actually defeat the claim, or is it
  a false alarm? WHITE rules, it does not advocate.
- **VALIDATION BACKSTOP** — an OBJECTIVE tool (parser, test, executable, solver) that settles a
  surviving candidate, distinct from anyone's opinion.

The point is **independence + evidence, not consensus.**

**Core invariants (never relax these):**

1. **INDEPENDENCE.** RED and WHITE must be independent of the claim's AUTHOR. If a hive/agent authored
   the claim, that hive is BLUE; it must NOT run the red team on its own work. No marking your own
   homework.
2. **EVIDENCE-OR-GAP.** Every RED finding and every WHITE ruling carries evidence or an explicit
   `GAP` / `[VERIFY]` marker. No bare assertion counts.
3. **VALIDATION BACKSTOP.** Any candidate that survives RED+WHITE is checked by an objective tool
   distinct from opinion BEFORE the claim is called broken or held.
4. **R016 TAGGING.** Label each ruling as **tool-run** (executed/verified) vs **spec-/reasoning-grounded**
   (judgment, `[VERIFY]`). Never present a judgment as a tool result.

## 2. When to load / when NOT to

**LOAD when** stress-testing a load-bearing claim or decision before committing it, especially:
- reviewer-facing claims (a negative/positive assertion a reviewer will attack);
- a claim or decision that REVERSES a prior decision;
- a subordinate's or another hive's deliverable you are about to rely on.

**Do NOT LOAD for:**
- trivial / low-stakes checks;
- a fact already verified by two independent objective sources;
- purely conversational turns;
- when a single objective tool already settles it (just run the tool).

**Contrast with [[dialectical-synthesis]]** (do not confuse them): dialectical-synthesis is a
SINGLE-MIND Hegelian thesis/antithesis/synthesis that seeks reconciliation. RBW is MULTI-AGENT
adversarial with enforced INDEPENDENCE and an objective backstop, and it seeks a VERDICT
(hold / hold-with-caveat / broken), not a synthesis of positions. Use dialectical-synthesis to develop
one mind's idea; use RBW to certify a claim against independent attack.

## 3. Configure the run (the variant axes)

RBW is a PATTERN, not a fixed shape. Pick a value on each axis; record the chosen config with the run.

### Axis 1 — MECHANISM (who plays the roles)
| Value | Independence strength | Cost | Pick when |
|---|---|---|---|
| **(a) In-session Workflow** — Claude multi-agent (the Workflow tool) | Role-independent, single model | low (default) | most claims; fast turnaround; the go-to |
| **(b) Cross-model tri-model** — Codex / Gemini as RED / WHITE (the [[project_tri_model_review]] pipeline) | MODEL-diverse: strongest against a single model's blind spot | heavy | high-stakes reviewer-facing claims; when a single model's prior might be the shared blind spot |
| **(c) Single-agent dialectical** — one agent role-plays RED then WHITE | weakest (no true independence) | minimal | quick sanity pass only; NOT sufficient for a shipped claim — contrast [[dialectical-synthesis]] |

### Axis 2 — RED COMPOSITION
- **N identical skeptics** — redundancy / voting; good when one failure mode dominates and you want
  robustness against a single skeptic missing it.
- **K DIVERSE LENSES** — each RED attacks a DIFFERENT failure mode / construct family. Use when the
  claim can fail multiple ways (the canonical case; see §5). Independence of lenses is itself an
  invariant: overlapping lenses do not count as independent attacks.

### Axis 3 — ROUNDS / CONVERGENCE
- **Single-pass** — one RED sweep, one WHITE adjudication. Cheapest.
- **Loop-until-dry** — repeat RED→WHITE; STOP after K consecutive rounds with NO new refutation.
- **Fixed N-round hardening** — a set number of rounds regardless of convergence (portfolio precedent:
  a **5-round RBW**). Use when you want a bounded, auditable hardening budget.
- **Verdict vocabulary:** `claim-holds` / `claim-holds-with-caveat` / `claim-broken`.

### Axis 4 — VERDICT AGGREGATION (how WHITE(s) decide)
- **White majority vote** — multiple whites, majority rules.
- **Synthesis-reconcile** — a reconciler resolves split whites into one verdict (used in §5).
- **Require-unanimous-red-fail (strict)** — claim is broken only if ALL reds+whites agree it fails;
  strongest bias toward preserving the claim; use for costly reversals.

### Axis 5 — INDEPENDENCE TOPOLOGY (name every role explicitly before starting)
State, for THIS run: who is BLUE (author / standing position), who is RED (independent attacker), who
is WHITE (independent adjudicator), and what is the VALIDATION BACKSTOP (tool).
- **Cross-hive variant:** BLUE = another hive's deliverable; RED = the REQUESTING hive; backstop = the
  AUTHORING hive's own tool, used ONLY as an objective validator (not as an advocate). This keeps the
  requester from grading itself while still exercising the author's tool as ground truth.

### Axis 6 — DOMAIN APPLICATION
- **(a) Load-bearing claim verification** — esp. reviewer-facing negative/positive claims.
- **(b) Design-decision selection** — among options; each option is a BLUE candidate, RED attacks each.
- **(c) Manuscript-claim reviewer-proofing** — pre-empt the reviewer who will try to refute your claim.
- **(d) Cross-hive deliverable check** — you are about to rely on another hive's output.

### Axis 7 — EVIDENCE / RIGOR
- Evidence-or-GAP on every finding and ruling (invariant 2).
- R016 tool-run vs reasoning-grounded on every ruling (invariant 4).
- Any surviving `[VERIFY]` item is ROUTED to the validation backstop (a tool) before the verdict is
  finalized; a claim is never called broken or held on an unresolved `[VERIFY]`.

## 4. Run procedure

1. **Freeze BLUE.** Write the claim/decision verbatim as it will ship. This is the target; do not let
   it drift mid-run (mirrors the pre-stated-hypothesis rule in [[morphism-research-methodology]]).
2. **Set the config.** Choose a value on each of the seven axes above; record it. Name the
   independence topology explicitly (Axis 5) — verify RED and WHITE are NOT the author.
3. **RED attacks.** Each RED (lens) independently tries to refute BLUE, producing candidate defeaters,
   each with evidence or a `GAP`/`[VERIFY]` marker.
4. **WHITE adjudicates.** For each candidate, WHITE rules genuine-defeater vs false-alarm, tagged
   tool-run vs reasoning-grounded. Split whites resolve per Axis 4.
5. **Backstop validates.** Any surviving candidate (and any `[VERIFY]`) goes to the objective tool
   before a verdict. RED SHOULD actually run the tool, not describe it.
6. **Verdict + caveat.** Emit `claim-holds` / `claim-holds-with-caveat` / `claim-broken`. If
   `-with-caveat`, state the exact narrowing (what part of the wording was over-broad).
7. **Record.** Config, every RED finding, every WHITE ruling with its R016 tag, the backstop result,
   and the verdict. This is the audit trail; the claim ships with it.

## 5. Worked example (canonical use case)

**2026-07-16 — P1 manuscript claim.** BLUE claim on record: *"SysML v2 has no native
verification-model-to-system-design fidelity link."* This reversed a prior recommendation, was
reviewer-facing, and both the author (PostWach) and the first independent check (the SysMLv2 hive) had
let it stand — exactly the load-bearing, decision-reversing case RBW exists for.

Config used:
- **Mechanism:** (a) in-session Workflow, 7 agents.
- **RED:** 4 DIVERSE LENSES — (1) KerML feature-level; (2) connections/interfaces; (3)
  allocation/dependency; (4) verification-framework semantics — each independently hunting a native
  construct relating a fidelity-differing verification model to the specific design.
- **BLUE:** the SysMLv2 hive's prior recommendation (on record, not arguing live).
- **WHITE:** 2 independent adjudicators, ruling each candidate genuine-fidelity vs trace/structural/invalid.
- **Synthesis:** 1 reconciler (Axis 4 = synthesis-reconcile).
- **Backstop:** the hive's SysML parser — RED actually RAN it (tool-run, not reasoning-grounded).

**Verdict: `claim-holds-with-caveat`.** The SUBSTANCE held — there is *no native BOUNDED /
degree-valued fidelity morphism*. But the LITERAL wording ("no native link at all") was OVER-BROAD: a
one-line `allocate` refutes it. The whites SPLIT on one candidate; the synthesis reconciler resolved it.

**Lesson:** RBW caught a reviewer-facing OVER-CLAIM that both the author and the first independent
check had missed. The fix was to narrow the wording, not drop the claim. This is the canonical trigger:
a load-bearing claim, reversing a prior decision, before it ships.

## 6. Failure modes RBW is built to stop

- **Marking your own homework.** The author runs its own red team, finds nothing, ships. RBW forbids
  it via the independence invariant; the cross-hive topology (Axis 5) is the structural fix when the
  claim is a deliverable.
- **Consensus-as-proof.** "Three agents agree" is not the bar — agreement without an objective backstop
  and without independence is shared blind spot, not verification (echoes
  [[morphism-research-methodology]] self-test 3).
- **Judgment dressed as measurement.** A WHITE ruling stated as if a tool produced it. Invariant 4
  (R016 tool-run vs reasoning-grounded) fences this; unresolved `[VERIFY]` routes to the backstop.
- **Over-broad literal wording.** The substance is right but the sentence claims more than the evidence
  (the §5 case). RBW's `claim-holds-with-caveat` verdict exists precisely to surface and narrow this.

## 7. Related skills / tools

- **the Workflow tool** — mechanism (a), in-session multi-agent RBW.
- **[[project_tri_model_review]]** (tri-model review pipeline) — mechanism (b), Codex/Gemini as
  RED/WHITE for genuine model-diversity independence.
- **[[dialectical-synthesis]]** — CONTRAST: single-mind dialectic, not multi-agent adversarial. Do not
  confuse.
- **[[verification-quality]]** — objective truth-scoring; a candidate validation backstop.
- **[[morphism-research-methodology]]** — the evidence bar and Step-5 refutation discipline RBW
  instantiates; use its rigor tags when stamping RBW rulings.
