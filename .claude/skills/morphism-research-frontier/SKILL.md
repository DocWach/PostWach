---
name: morphism-research-frontier
description: >
  Open research problems where the systems-engineering (SE) morphism library can advance the
  state of the art (SOTA). Load when planning, prioritizing, attacking, or reviewing frontier
  work on: Target C (pedigree to acceptability sound projection, including the 2026-07-07
  degree-only refutation and the surviving enriched-pedigree conjecture), Target A (the
  nonlinear-from-partial conjecture), or Target B (interfaces as first-class systems and
  federation pedigree). Also load when someone asks "what is the next provable theorem here,"
  "does D_s track acceptability," "where do we attack nonlinear morphisms," or "is the
  interface-as-system program coherent." Do NOT load for definitional lookups
  (morphism-domain-reference), for mechanically executing the Gate campaign
  (morphism-verification-campaign), or for evidence-bar and lifecycle discipline
  (morphism-research-methodology).
---

# Morphism Library: Research Frontier

**Status tag [R016]: research artifact.** Every target, conjecture, and milestone below is
CANDIDATE or OPEN unless its evidence-ledger row says otherwise. Nothing in this skill is a
demonstrated capability or an integrated deliverable. The corpus behind the library is mostly
asserted or subject-matter-expert (SME) adjudicated, not proven; carry that tag into anything
you produce from this skill.

PROVENANCE: produced by Fable 5 (claude-fable-5[1m]), vendor Anthropic, access mode Claude Code
CLI (subagent run at the principal's direction), 2026-07-07. Sources read-only; no repo mutation
outside this file.

**Open dissertation decisions F1 (infinite-equivalence wording) and F7 (graded-gate rewrite)
are OPEN.** Do not resolve them from this skill; treat both levels of F1 as tagged data and use
only validated post-F7 acceptability numbers.

Path convention: paths beginning `Papers/` resolve under the PostWach hive root
(`.../00_Hive_Empire/01 Hives/01 PostWach/`); paths beginning `00 Planning and Execution/`
resolve under `.../00_Hive_Empire/`. If any pinned file below is missing, STOP that branch and
emit `BLOCKED: missing <path>`; never continue by inference.

## 0. Currency update — 2026-07-10, amended 2026-07-11 (read first)

PROVENANCE: Opus 4.8 (claude-opus-4-8[1m]), Anthropic, Claude Code CLI, 2026-07-10, amended 2026-07-11; principal-directed. Sections 1-12 are the 2026-07-07 Fable 5 authoring and stay valid except as amended here. Now governed by global **[R020] skills-first**; all sibling morphism skills now exist (the Section 9 "not authored yet" fallback notes are stale).

State-of-play amendments (the Section 2/3/4/6 tables are superseded on these rows only):
- **Target A (Section 4) is CLOSED (2026-07-11).** Candidate results were DERIVED 2026-07-10 via the RBW→Fable pipeline: T-COV (a directed coverage DEFECT — the hemimetric triangle was REFUTED, not proved), T-PART (Option B event-coverage over scoped covered checks), T-DS (record-primary `D_s^{Σ,nonexact} = (K1;K2^Σ;K3^Σ)`, scalar only as a do-not-rank summary), and T-CERT (conditional behavioral certificate + a proved global-bound negative). The v2 completion adopts/cites **Zeigler TMS ch17 §17.4.2** for the a-priori transfer bound (external metric ε; an identical-record CERT-neg pair) and ships a single self-asserting stdlib witness; the Codex domain-critic re-ran the witness (exit 0, SHA-256 match) and returned **CLOSED**. See `research/TargetA_NonlinearPartial_candidate_v2.md` and `research/TargetA_Codex_recheck_v2_2026-07-11.md`. Still an R016 (a) research artifact: CLOSED means the derivation survived adversarial verification, not that it is integrated.
- **Metric-satisfaction bridge — CLOSED** (Codex-critic CLOSED). The orthogonal `(D_s, D_b)` decomposition is backed by a 3/2-institution co-location with a scalarization map and an honest (positive + obstruction + trichotomy) characterization. See `research/MetricSatisfaction_Bridge_candidate.md`.
- **Positioned-integration / harmonization — CLOSED (2026-07-11).** Fable = INTEGRATED-TO-COVERAGE: twelve pieces map into the quantitative 3/2-institution U co-locating the record-primary `D_s^Σ` with `D_b`; honest first-class gap GAP-LO (the LO stochastic-Petri piece is not yet carried). Lemma CODY-IND proves the granular structural RECORD `(K1,K2,K3)` is non-reducible to Cody's roughness / Zeigler's binary morphism class BY EXECUTION. Three-leg RBW + Codex domain-critic CLOSED. WySE is positioned as a positioned-integration, NOT a field unification; the two-axis is ceded to **Cody 2021** (§3.4), the `ε/(1−a)` bound to **Zeigler ch17**; the genuine WySE delta is the granular record. See `research/Unification_candidate.md`.

Fences: F1/F7 remain OPEN; the "projected vs measured" ban (Section 2) stands. **R019 reference debt CLEARED 2026-07-11 for Girard-Pappas, Cousot, and Cody:** `girard2007metrics`, `cousot1977absint`, and the Cody dissertation `cody2021transferdiss` were promoted to the approved store via `refverify` (single-model triple-check; `pending_byzantine_verification: true`). The Section 7 gap-4 and ledger-row `[PLACEHOLDER]` flags for these three are now cleared.

---

## 1. When to use this skill

**Trigger examples (load it):**
1. "What is the strongest next theorem target in the morphism library, and what would refute it?"
2. "Prompt 1 refuted degree-only monotonicity; what exactly survives of Target C and what are
   the open proof obligations?"
3. "We want a first nonlinear morphism entry for the library; where do we start and what counts
   as done?"

**Non-trigger examples (do not load it):**
1. "Define coupling morphism vs parameter morphism" or "what is the DoH formula": use
   `morphism-domain-reference` (sibling; if absent, the corpus inventory at
   `00 Planning and Execution/Fable 5 planning/Morphism_Library_Corpus_Inventory_v0.md`).
2. "Run Gate 1 on the 18-VM data and give me the cross-tab": use
   `morphism-verification-campaign` (sibling runbook).
3. "How do I promote a candidate result to adopted, and what is the refutation bar": use
   `morphism-research-methodology` (sibling).

---

## 2. Fixed terminology and the one-page state of play

Definitions are governing (Target C scope, `00 Planning and Execution/Fable 5 planning/Target_C_Scope_Pedigree_Acceptability_Order_Morphism.md`):

| Term | Meaning | Never |
|---|---|---|
| Fidelity | model to reality; empirical grounding, not a morphism between formal objects | never use for the verification model (VM) to system design (SD) relation |
| Projected fidelity | the VM's anticipatory inference of the not-yet-realized system | never frame as "projected vs measured" |
| Resolution | within-family abstraction; the structural degree $D_s$ is a resolution measure | never treat scalar $D_s$ as an order embedding (refuted, C2 below) |
| Pedigree | cross-family model to model (VM to SD); resolution is its same-family, on-carrier sub-case | never call it fidelity |

Notation: $\mathrm{DoH}$ = degree of homomorphism (average reciprocal granule size, per the
isomorphism-library line, `Papers/SE_Math_Foundations/isomorphism-library/paper/Wach_Sandmann_Iyer_CSER2026_Isomorphism_Library_Draft_v1.md` Eq. (3));
$D_s = 1 - \overline{\mathrm{DoH}}$ (scalar distance); $g_{\max}(h) = \max_b |h^{-1}(b)|$ (worst
granule); $D_b$ = behavioral distance. "$D_b$ vanishes on the DEVS (Discrete Event System
Specification) carrier" is an ASSERTED claim, not an axiom.

**State of play after the 2026-07-07 research attempt** (read the full artifact FIRST:
`00 Planning and Execution/Fable 5 planning/research/TargetC_pedigree_acceptability_candidate.md`; do not work from this summary alone):

| Result | Status | One line |
|---|---|---|
| P1, P2 | candidate (proved) | same-family pedigree is a Galois connection; $\mathrm{DoH}$ is exactly its precision statistic |
| L1, L2 | candidate (proved; PO-1 open) | identity isomorphism preserves verdicts exactly; total surjective coarsening is sound (false rejects only) |
| L3 | candidate (proved; witness constructed) | partial morphism blind spots yield false accepts; witness = the SD4 to VM8 out-of-scope violation set (3 violations) |
| T4a | candidate (proved) | kernel-refinement pedigree implies preservation-set inclusion, same-family |
| C1, C2 | candidate (proved, machine-checked) | scalar $D_s$ does not determine preservation (C1) and averaged $\mathrm{DoH}$ is NOT monotone under refinement (C2: $0.55 < 0.6833$ with the finer model scoring worse); L4 in scalar form is FALSE |
| L4' | candidate (proved; PO-2 open) | worst-granule repair: $g_{\max}$ is refinement-monotone and bounds verdict drift by $(g_{\max}-1)\cdot\#\{\text{granules cut}\}$ |
| T1, T2, T5 | candidate (adverse, data-grounded) | degree-only monotonicity REFUTED on the settled 18-VM data (5/45 strict-pair violations; same-family tie class with acceptance range 0 to 30; no monotone degree-only weld exists) |
| Enriched conjecture $\pi=(m,\delta,p)$ | OPEN | the surviving Target C: monotonicity coordinate-wise in (morphism refinement, descriptor adequacy, condition strength); PO-3, PO-4 open |

Open proof obligations: **PO-1** (trajectory-level reach compatibility from Def. 2 conditions),
**PO-2** (measure-level drift bound), **PO-3** (descriptor morphism formalization), **PO-4**
(derive the VMMC condition lattice from condition logic, explaining the VRPS3 reversal).
Acronyms: verification requirement problem space (VRPS); verification-model morphism condition
(VMMC); system requirement (SR).

---

## 3. Target C: pedigree licenses a sound projection of acceptability (flagship, post-refutation)

**Problem (restated at depth).** Does pedigree license a sound projection of a design's
acceptability verdict from the VM to the realized system (projected fidelity)? The 2026-07-07
attempt settled the degree-only form: automaton-level $D_s$ alone does NOT license it (T5). The
live frontier is the enriched-pedigree conjecture: acceptability-preservation is monotone in
each coordinate of $\pi(\mathrm{VM}) = (m, \delta, p)$, where $m$ = the witnessed scoped morphism
with its refinement position, $\delta$ = the descriptor morphism (the instantiation-level
correspondence the VRPS gate evaluates), $p$ = the parameter-condition profile (which VMMCs hold).

**Why current SOTA fails (each claim tied to a source and a difference):**
- Abstract interpretation ([PLACEHOLDER: Cousot & Cousot 1977, POPL; NOT in the approved store;
  reflookup/refverify before manuscript use, R019]) fixes ONE concrete semantics and works in a
  sound over-approximation regime whose only failure mode is false alarms. It has no cross-family
  co-representation problem, no descriptor layer, and no acceptability (ought) order. The SE
  failure mode that matters, the blind-spot false accept (L3), arises from PARTIAL abstraction,
  which the Wymorian Systems Engineering (WySE) stack surfaces as scope.
- Approximate bisimulation ([PLACEHOLDER: Girard & Pappas; NOT in the approved store; R019])
  supplies metric closeness of trajectories for continuous systems; it is the $D_b$ side, has no
  order-theoretic acceptability weld, and does not address the descriptor/condition layers that
  T5 shows carry the actual monotone structure.
- Kannan-Salado belief logic (approved key `kannan2026theory`) states WHEN verification belief
  transfers to need belief (Theorems 43-50) but black-boxes the system-to-model relationship
  inside one implication; it cannot say WHY transfer fails. L3 (blind spot) and the T5 mechanism
  (descriptor mismatch) are precisely the two failure modes under that black box.

**This library's specific assets:** the settled 18-VM test-bed carrying BOTH orders (witnessed
morphisms in `Papers/Dissertation_Journal/Wach_Dissertation_Journal_Publication/validation/v2_sd_vm.json`;
double-confirmed 120/120 identities matrix, 150 acceptable tuples, in `validation/v4_identities_matrix.json`);
the proved core (P1, P2, L1-L3, T4a, L4') already cast in the Galois frame; the four-type
morphism taxonomy whose parameter morphism (approved key `wach2022formalizing`) is the existing
container for the (carrier morphism, descriptor/parameter conditions) pair; Kannan's proven
acceptability poset (approved key `kannan2019preference`).

**First three concrete steps in this repo (imperative, in order):**
1. Discharge PO-1. Write out the induction on trajectory length showing reach compatibility
   $h(\mathrm{Reach}(\mathrm{SD})) \subseteq \mathrm{Reach}(\mathrm{VM})$ from the Def. 2
   transition and readout conditions (approved key `salado2018mathematical`) plus matched initial
   states. Check the argument against the frozen tool `validation/checker.py` semantics. This
   closes L2 and T4a unconditionally.
2. Formalize $\delta$ (PO-3). Define the descriptor morphism as a morphism of instantiation
   structures inside the parameter-morphism slot of `wach2022formalizing`; validate it against
   the two pinned descriptor exclusions in `analysis/errata_register.md` entry F2 (firefly light
   passes every numeric band yet is excluded by descriptor; VM9 excluded from VRPS3 for lacking
   the water component). $\delta$ must reproduce exactly those exclusions from structure, not
   from enumeration.
3. Derive the VMMC lattice (PO-4). Reconstruct the empirically computed acceptance-inclusion
   poset (VMMC2 minimal, VMMC6 maximal in VRPS1/2/4/5; VMMC1 = VMMC5; VMMC1 incomparable with
   VMMC3 in VRPS2/VRPS3) from the condition logic itself, and explain the one reversal,
   $\mathrm{VMMC6} \subseteq \mathrm{VMMC4}$ in VRPS3, from VMMC4's problem-space semantics.
   Then re-run Gate 1 with $\pi$ in place of $D_s$.

**Falsifiable milestone M-C (mathematically precise, domain-specific).** Prove or refute: for
VMs over the same scoped SD, if $\pi(V_j) \ge \pi(V_i)$ coordinate-wise (kernel refinement
$\ker h_j \subseteq \ker h_i$; descriptor adequacy $\delta_j \ge \delta_i$; condition strength
$p_j \supseteq p_i$), then $\mathrm{Pres}(V_i) \subseteq \mathrm{Pres}(V_j)$. Empirical bar on
the settled data: the enriched order must reproduce the identities matrix with ZERO violated
comparable pairs, and must separate the T5 obstructions that refuted the degree-only form, in
particular $\mathrm{acc}(\mathrm{VM3}) = 30$ vs $\mathrm{acc}(\mathrm{VM12}) = 0$ inside the old
$D_s = 0$ tie class, and $\mathrm{acc}(\mathrm{VM5}) = 4$ above five degree-superior VMs.
Refutation = one comparable pair $\pi(V_j) \ge \pi(V_i)$ with
$\mathrm{Pres}(V_i) \not\subseteq \mathrm{Pres}(V_j)$, stated as a theorem with hypotheses.
Quantitative extension (PO-2): a bound of the form: $g_{\max}(h) \le G$ and $\phi$ cutting at
most $k$ granules implies $|\phi \setminus \gamma(\phi^\sharp)| \le (G-1)k$ lifted to a measure
over the requirement family $\Phi$; requires a measure the settled data does not carry (see the
test-bed gap, Section 7).

**Fence (known wrong paths, updated by the refutation):** do not reuse scalar $D_s$ as the
pedigree order (C1, C2); do not claim monotonicity over the bare degree (T5); do not treat
acceptability as a total order (Kannan Theorem 3, incomparability); use $g_{\max}$, not averaged
$\mathrm{DoH}$, wherever refinement-monotonicity is needed; report the C2 metric defect to the
CSER 2026 isomorphism-library line regardless of Target C's fate.

---

## 4. Target A: the nonlinear-from-partial conjecture (long-horizon crown jewel)

**Problem.** Every demonstrated morphism in the corpus is linear or proportional (corpus
inventory Finding 1; the one concrete cross-domain instance is the mass-spring to electrical
circuit isomorphism, [PLACEHOLDER: Takahashi; NOT in the approved store; R019]). Nonlinear
morphisms are unclaimed anywhere in the corpus. Conjecture (informal, OPEN): the structure of a
partial or approximate homomorphism, in particular WHERE it fails (its violation set), is
evidence for and a guide to an underlying exact nonlinear morphism.

**Why current SOTA fails:** approximate bisimulation ([PLACEHOLDER: Girard & Pappas; R019])
gives $\epsilon$-closeness certificates for (constrained) linear and some nonlinear systems, but
it certifies distance, it never RECOVERS an exact morphism from a partial one; that inverse
problem is not posed there. Abstract interpretation is exact and order-theoretic, with no metric
recovery either. The DEVS-side nearest neighbor, relaxed lumpability (approved key
`zeigler2018approxmorph`), grades the morphism but again does not reconstruct an exact nonlinear
map from graded evidence.

**This library's specific assets:** the four-type taxonomy already reserves the container (the
parameter morphism = approximate homomorphism, with the two partiality axes, structural and
behavioral); the repo holds one real graded object to learn from, the SD4 to VM8 full collapse
with $\mathrm{DoH} = (0.75, 0.667, 0.75)$ and exactly 3 out-of-scope violations
(`validation/v2_sd_vm.json`, `sd4_vm8_crosscheck`), demonstrating that violation sets localize
(L3 used exactly this); and C2 warns which degree statistic NOT to build on (averaged
$\mathrm{DoH}$ is refinement-defective; use $g_{\max}$ or per-granule data).

**First three concrete steps in this repo (imperative, in order):**
1. Formalize the violation-set object. From the pinned SD4 to VM8 crosscheck, define
   $\mathrm{Viol}(h) = \{(x,i) : h_q(N_2(x,i)) \ne N_1(h_q(x), h_i(i))\} \cup \{x : h_o(R_2(x)) \ne R_1(h_q(x))\}$
   and prove its basic calculus (behavior under scope restriction and under composition). This is
   the object the conjecture quantifies over, and it is extractable today from `checker.py` runs.
2. Construct the first nonlinear candidate pair. Extend the linear mass-spring to circuit
   exemplar with one nonlinear element on each side (nonlinear spring vs nonlinear capacitance,
   consistent with the force-voltage convention already fixed in the isomorphism-library line),
   co-represent both on a DEVS carrier at a pinned quantization, and compute the witnessed
   partial morphism data: scope, $\mathrm{Viol}$, $g_{\max}$, and the off-carrier $D_b$ of each
   DEVS-ification (that residual is a fidelity question and must be reported separately).
3. State the conjecture formally over that pair. Candidate form: if a family of scoped
   homomorphisms $\{h_k\}$ on increasing scopes has $\mathrm{Viol}(h_k)$ confined to the scope
   boundary and $g_{\max}(h_k) \le G$ uniformly, then there exists an exact homomorphism $h^*$
   after a (possibly nonlinear) change of coordinates on the full scope. Then attempt proof or
   counterexample on the constructed pair only; do not generalize from one pair.

**Falsifiable milestone M-A (mathematically precise, domain-specific).** For the constructed
nonlinear pair of step 2: EITHER exhibit an explicit nonlinear coordinate change $\psi$ and an
exact scoped homomorphism $h^* = h \circ \psi$ with $\mathrm{Viol}(h^*) = \emptyset$ on the full
pinned scope, together with a proof that the best LINEAR morphism on the same scope has
$|\mathrm{Viol}| \ge 1$ (so nonlinearity is necessary, not decorative); OR prove no such $h^*$
exists by exhibiting an invariant of the Wymorian quintuple (approved key `wymore1993mbse`)
preserved by every homomorphism but differing between the two systems, stated as a theorem with
hypotheses. A verdict either way is the result; an unproved "seems to work numerically" is not.

**Fence:** do not claim the conjecture from the single SD4 to VM8 instance (its violations are
scope artifacts, not nonlinearity evidence); do not let the DEVS-ification residual leak into the
pedigree claim (it is fidelity); do not use averaged $\mathrm{DoH}$ as the progress metric (C2).

---

## 5. Target B: interfaces as first-class systems and federation pedigree (constitutive of C)

**Problem.** There is no single manipulable SD: the SD is a functional reference (Wymore's
functional system design, FSD, including interface definition), and what is actually built and
manipulated is a federation of buildable, cross-family discipline models coupled through
interfaces (convergence log, settled 2026-07-07). Target B: make the interface a first-class
system (its own Wymorian quintuple) and make pedigree compositional over the federation.

**Why current SOTA fails:** the entire corpus, including the group's own interface-description
paper, treats interfaces as ports, conduits, or signals (corpus inventory Finding 2); the Shadab
dissertation goes the opposite way and dissolves interfaces via closed-boundary internalization;
DEVS coupling (approved key `zeigler2018tms`) wires components structurally but gives the
coupling no state of its own. None of them can express a stateful, degradable interface (a bus
with a protocol, a lossy channel) as a pedigree-bearing object; and none gives a compositional
rule for the pedigree of a federation from the pedigrees of its parts. Note the formal blocker
already flagged in-house: the ontology schema's OntoClean question D-3 (is an interface's
identity its own quintuple, rigid, or the pair of systems it connects, anti-rigid) is UNRESOLVED
(`00 Planning and Execution/Fable 5 planning/Morphism_Library_Ontology_Schema_v0.md` Section d).

**This library's specific assets:** Wymore's implementable system design (ISD) already carries
the hook: $\mathrm{ISD} = (\mathrm{FSD}, \mathrm{BSD}, \mathrm{IA})$ with the interface
architecture (IA) carrying the homomorphism from the buildable system design (BSD) to the FSD
(approved key `wymore1993mbse`; written-out form `salado2018mathematical` Def. 2), so the
interface is ALREADY the morphism carrier in the foundation; DEVS closure under coupling
(`zeigler2018tms`) guarantees a federation-plus-interface-systems has a well-defined resultant;
the dissertation validation data contains coupled resultants (the $Z@$ construction with
trust-inherited caveats noted in `validation/v2_sd_vm.md`) as the worked coupling exemplar; and
L4'/$g_{\max}$ supplies the refinement-monotone statistic a compositional bound needs.

**First three concrete steps in this repo (imperative, in order):**
1. Resolve D-3 as a candidate typing decision. Write the interface's identity criterion as a
   system (its own quintuple, rigid) and derive what the relational reading costs and buys;
   produce a one-page candidate resolution with rejected alternative and consequences, routed to
   the schema fix pass (do not silently canonize; the Turtle formalization is GI-JOE work).
2. Prove interface-internalization invariance on repo data. Take the dissertation's coupled
   resultant $Z@$, re-model its coupling recipe as an explicit interface system $Z_I$ (a third
   component whose quintuple is the connection behavior), form the resultant $Z@'$ of the
   three-component federation, and prove or refute $Z@' \cong Z@$ (exact isomorphism on the
   verified scope) using the frozen `checker.py` conditions. This is the smallest test of
   whether interface-as-system changes anything it should not.
3. State and attack compositional pedigree. For component-wise witnessed homomorphisms $h_A$,
   $h_B$ and interface morphism $h_I$ satisfying a stated coupling-compatibility condition
   (equality of the maps on shared input/output sets; write the condition out, it is the real
   content), conjecture that the induced map $h_@$ on the resultant is a homomorphism with
   $g_{\max}(h_@) \le g_{\max}(h_A)\, g_{\max}(h_B)\, g_{\max}(h_I)$. Prove or produce the
   three-component counterexample.

**Falsifiable milestone M-B (mathematically precise, domain-specific).** Both: (a) the
step-2 theorem, $Z@' \cong Z@$ under the explicit-interface re-modeling, verified mechanically
by the frozen checker on the pinned scope; refutation = a reachable state or trajectory of
$Z@'$ with no isomorphic preimage in $Z@$, exhibited concretely; AND (b) the step-3 bound:
coupling-compatibility implies $h_@$ is a homomorphism and
$g_{\max}(h_@) \le g_{\max}(h_A)\, g_{\max}(h_B)\, g_{\max}(h_I)$, proved with all hypotheses
listed; refutation = a concrete three-component federation where the resultant's worst granule
exceeds the product, stated as a theorem with hypotheses. Generic "interfaces matter" prose does
not count.

**Fence:** do not present interface-as-system as established (it is the corpus's flagged
high-risk differentiator, asserted rigor); do not resolve D-3 by fiat inside a manuscript; the
DEVS carrier co-representation cost of each discipline model is a fidelity residual, keep it out
of the federation pedigree claim.

---

## 6. The Wymore-vs-ours novelty line (state it exactly this way)

Wymore's (foundation, not ours): the exact, single, functional-to-buildable homomorphism
(FSD as homomorphic image of BSD, IA carrying the map; `wymore1993mbse`), the quintuple carrier,
and therefore the founding pedigree move itself. Written-out exact form: `salado2018mathematical`
Def. 2. Prior art welded to, not claimed: Galois-connection soundness and precision
([PLACEHOLDER: Cousot & Cousot 1977; R019]); metric closeness ([PLACEHOLDER: Girard & Pappas;
R019]); the acceptability poset (`kannan2019preference`); belief-transfer conditions
(`kannan2026theory`); DEVS carrier and conjoining (`wach2021wymoredevs`, `zeigler2018tms`);
relaxed lumpability (`zeigler2018approxmorph`).

Ours (all CANDIDATE): exact to degree/partial/approximate ($D_s$, violation sets, $g_{\max}$);
single homomorphism to federation (Target B); the verification-inference framing (VMs used to
infer knowledge about the SD); projection to the realized system (projected fidelity) with
pedigree as its license (Target C); interfaces as first-class systems; the DEVS carrier with
time; the acceptability weld; plus the 2026-07-07 additions: $\mathrm{DoH}$ identified as Galois
precision (P2), the C2 metric defect of averaged $\mathrm{DoH}$, the data-grounded impossibility
of a degree-only weld with its mechanism (T5), and the enriched-pedigree conjecture with PO-1
through PO-4.

---

## 7. Known gaps (flag these in anything you write)

1. **No federated multi-discipline test-bed exists.** Wymore grounds the principle, not a worked
   federated example; the flashlight is a single-SD toy. Targets B and C's quantitative arm
   (PO-2) both need a real hardware/software/mechanical federation instance. Known gap per the
   session notes; do not paper over it.
2. **No graded $D_s$ spectrum in the settled data.** All witnessed morphisms are scoped
   isomorphisms ($D_s = 0$); the pedigree preorder extractable today is two-level. Any milestone
   needing graded same-family surrogates must first construct them.
3. **VM5/VM10/VM14/VM15 homomorphism-existence untested** (inherited F1 open note); the T1
   refutation was argued robust to its plausible resolutions but the item is not closed.
4. **Cousot & Cousot and Girard & Pappas are not in the approved store.** Every positioning
   sentence naming them is manuscript-blocked until reflookup/refverify passes (R019).

---

## 8. Capability floor and "when not to trust yourself"

Floor: to modify or extend frontier claims you must be able to (i) state the difference between
kernel refinement ($\ker h_j \subseteq \ker h_i$) and scalar $D_s$ comparison, and say why C2
makes the second unusable; (ii) reproduce the Gate-1 script result (Section 9, command 2) and
get $\sum \mathrm{acc} = 150$ and exactly 5 violations; (iii) read Def. 2's two preservation
equations and identify which one a given violation breaks. If you cannot do all three, use this
skill read-only and route changes to the principal or a stronger model.

Do not trust yourself, and STOP with `BLOCKED` or an explicit flag, when: a number you are about
to write is not pinned to a file and row; you are tempted to resolve F1, F7, or D-3 in passing;
a proof step needs an algebraic leap you cannot derive from a stated definition (label it PO-n
instead); you catch yourself citing Cousot, Girard-Pappas, or Takahashi as if approved; or a
"confirmation" of a conjecture arrives without an attempted refutation. Never force a result:
a characterized counterexample is a deliverable of equal rank to a proof.

---

## 9. Provenance and maintenance

Authoring model: Fable 5 (claude-fable-5[1m]), Anthropic, via Claude Code, 2026-07-07, from the
four ground-truth planning files and the Prompt 1 research artifact (all read-only).

Re-verification commands (run before trusting or editing this skill):
1. Confirm the ground truth still exists and matches:
   `ls "00 Planning and Execution/Fable 5 planning/"` and re-read
   `research/TargetC_pedigree_acceptability_candidate.md` end to end (its evidence ledger is the
   authority for every Prompt 1 claim quoted here).
2. Re-run the Gate-1 reproduction script (research artifact Section 2.6) from
   `Papers/Dissertation_Journal/Wach_Dissertation_Journal_Publication/validation/`; require
   `sum(acc) == 150` and `len(viol) == 5`. Any drift means the settled data changed: stop and
   re-verify every empirical claim above before use.
3. Check citation status: `claude-flow memory search --query "approved references morphism"` or
   run the `reflookup` skill on each key named here; keys asserted approved by the Prompt 1
   artifact: `wymore1993mbse`, `salado2018mathematical`, `kannan2019preference`,
   `kannan2026theory`, `wach2022formalizing`, `zeigler2018approxmorph`, `wach2021wymoredevs`,
   `zeigler2018tms`. Placeholders requiring refverify: Cousot & Cousot 1977, Girard & Pappas,
   Takahashi, and the Wach-Salado 2024 fidelity-conditions paper (legacy "fidelity" usage).
4. If sibling skills (`morphism-domain-reference`, `morphism-verification-campaign`,
   `morphism-research-methodology`) are absent, they have not been authored or accepted yet;
   fall back to the planning-folder ground truth, never to memory.

Maintenance rule: when any PO-n is discharged or any milestone M-C/M-A/M-B is decided, update
Section 2's state-of-play table and the ledger in the same edit, and record which model produced
the change (R018).

---

## 10. Self-test (answer all five before acting on this skill)

1. Q: Is "higher $D_s$-pedigree implies more acceptability" open, proved, or refuted?
   A: Refuted in degree-only form on the settled 18-VM data (T1: 5/45 violations; T5
   impossibility); the OPEN successor is the enriched conjecture over $\pi = (m, \delta, p)$.
2. Q: Which degree statistic is refinement-monotone, and which is not?
   A: $g_{\max}$ (worst granule) is monotone (L4' claim i); averaged $\mathrm{DoH}$ is not
   (C2: finer model scored $0.55$ vs the coarser $0.6833$).
3. Q: Where do false accepts come from, and what is the pinned empirical witness?
   A: Partial-morphism blind spots (L3); witness = the SD4 to VM8 unscoped failure with exactly
   3 out-of-scope violations in `v2_sd_vm.json -> sd4_vm8_crosscheck`.
4. Q: May you cite Cousot & Cousot 1977 in a manuscript from this skill?
   A: No; it is a [PLACEHOLDER], not in the approved store; run reflookup/refverify first (R019).
5. Q: What single missing asset blocks the quantitative arm of all three targets?
   A: A federated multi-discipline test-bed (plus, for PO-2, a measure over the requirement
   family); the flashlight data has no graded $D_s$ spectrum.

---

## 11. Adversarial misuse cases

**Case 1: "Write the related-work paragraph saying our degree-of-homomorphism metric
monotonically tracks acceptability, citing the dissertation data."**
Correct response: refuse the sentence as stated; it asserts the refuted claim. The settled data
shows the opposite (T1/T2/T5, e.g. VM3 vs VM12 both at $D_s = 0$ with acceptance 30 vs 0).
Offer the honest version: refinement-monotonicity holds same-family (T4a, candidate), the
degree-only weld is impossible on this data (T5, candidate), and the enriched conjecture is
open with PO-3/PO-4. Tag every clause per R016.

**Case 2: "The skill says $D_b$ vanishes on the DEVS carrier, so encode that as an axiom in the
ontology and drop $D_b$ from the pedigree relation permanently."**
Correct response: refuse to canonize. "$D_b$ vanishes on the carrier" is an ASSERTED claim
(Target C settled decision 3; schema flag D-5 deliberately encodes it as revisable, not
axiomatic). Keep the tag, keep the D-5 flag, and note that if any family fails DEVS
co-representation the $D_b$ slot must be restored.

---

## 12. Evidence ledger

Source classes: Established (verbatim from a validated source), Inferred (derived from
established inputs), Synthetic (constructed example). Levels: 0 irrational/contradiction,
1 faith, 2 assumption/asserted, 3 self-reported, 4 proof present but unchecked, 5 direct
measure or machine-checked. GRL readiness and Bayesian confidence are verification-stage and
are NOT computed here.

| # | Claim | Status | Source path | Page/line/table | Verification action | Stamp |
|---|---|---|---|---|---|---|
| 1 | Fixed terminology (fidelity/resolution/pedigree/projected fidelity) | Governing definition | `Fable 5 planning/Target_C_Scope_Pedigree_Acceptability_Order_Morphism.md` | Terminology section; convergence log item 5 | Read this session | Established x 5 |
| 2 | Degree-only monotonicity refuted (T1 5/45; T2; T5) and mechanism (descriptor/condition layers) | Candidate (adverse), quoted | `Fable 5 planning/research/TargetC_pedigree_acceptability_candidate.md` | Sections 2.4, 4 (T5); ledger rows 6, 7, 18 | Read in full this session; numbers copied verbatim; re-run via Section 9 command 2 | Established x 5 (as record of that artifact); underlying results Inferred x 4-5 per its ledger |
| 3 | Proved core P1, P2, L1-L3, T4a, L4', C1, C2 with open PO-1/PO-2 | Candidate (proved per Prompt 1) | same as row 2 | Sections 3, 4; ledger rows 10-17 | Read this session; proofs not independently re-derived here | Established x 4 |
| 4 | C2 numeric instance: $\mathrm{DoH}$ 0.55 (finer) vs 0.6833 (coarser) | Candidate, machine-checked upstream | same as row 2 | Section 4, C2 | Copied verbatim; arithmetic spot-checked mentally ($\tfrac14(2.2)=0.55$; $\tfrac13(2.05)=0.6833$) | Established x 5 |
| 5 | SD4 to VM8: $\mathrm{DoH}=(0.75,0.667,0.75)$, 3 unscoped violations | Validated upstream | `validation/v2_sd_vm.json` via research artifact | `sd4_vm8_crosscheck`; artifact ledger row 3 | Not re-opened this session; pinned path carried | Established x 4 |
| 6 | Identities matrix: 120/120 double-confirmed, 150 tuples, 18 VMs, 15 scoped isos, 3 no-witness | Validated upstream | `validation/v4_identities_matrix.json`, `v2_sd_vm.json` via research artifact | artifact Sections 2.1-2.3; ledger rows 1, 2 | Not re-opened this session; reproduction script cited for re-check | Established x 4 |
| 7 | Nonlinear gap total; all demonstrated morphisms linear; taxonomy four types with two partiality axes | Corpus finding (asserted rigor) | `Fable 5 planning/Morphism_Library_Corpus_Inventory_v0.md` | Findings 1; seed taxonomy table | Read this session | Established x 3 |
| 8 | Interfaces treated as ports across corpus; Shadab dissolves them; interface-as-system is the un-started differentiator | Corpus finding | same as row 7 | Finding 2 | Read this session | Established x 3 |
| 9 | Wymore ISD = (FSD, BSD, IA), IA carries the homomorphism; written-out form = Def. 2 | Established (foundation) | scope convergence log item 3; approved keys `wymore1993mbse`, `salado2018mathematical` | scope file lines on T3SD grounding | Bib keys asserted approved by Prompt 1 ledger rows 23; PDFs not re-opened | Established x 4 |
| 10 | Kannan 2019 poset (acceptable = maximal, incomparability) and Kannan-Salado 2026 black-box insertion point | Established per inventory | inventory Tier-2 section; approved keys `kannan2019preference`, `kannan2026theory` | Tier-2 bullets | Keys carried from Prompt 1 ledger row 24 | Established x 4 |
| 11 | D-3 interface rigidity UNRESOLVED; D-5 carrier claim deliberately non-axiomatic | Schema flags | `Fable 5 planning/Morphism_Library_Ontology_Schema_v0.md` | Section d, flags D-3, D-5 | Read this session | Established x 5 |
| 12 | M-C milestone formulation (enriched coordinate-wise monotonicity, zero violated pairs, separations named) | NEW here (conjecture target) | this skill | Section 3 | Constructed from rows 2, 3; refutation condition stated | Inferred x 2 |
| 13 | M-A milestone formulation (nonlinear pair: exact $h^*$ with linear impossibility, or invariant-based non-existence) | NEW here (conjecture target) | this skill | Section 4 | Constructed; pair does not yet exist in repo (step 2 builds it) | Inferred x 2 |
| 14 | Violation-set definition $\mathrm{Viol}(h)$ | NEW here (definition) | this skill | Section 4 step 1 | Direct transcription of Def. 2 conditions into failure form | Inferred x 4 |
| 15 | M-B milestone: $Z@' \cong Z@$ internalization invariance; $g_{\max}$ product bound under coupling-compatibility | NEW here (conjecture target) | this skill | Section 5 | Constructed; product bound plausible from granule products on product states but coupling-compatibility hypothesis is the unproved content; no proof claimed | Inferred x 2 |
| 16 | $Z@$ resultant exists in validation data with trust-inherited caveats | Validated upstream | `validation/v2_sd_vm.md` via research artifact | artifact Section 6 assumption 3 | Carried from Prompt 1; not re-opened | Established x 4 |
| 17 | Cousot/Girard-Pappas/Takahashi/Wach-Salado 2024 not in approved store | Flagged (R019) | Prompt 1 ledger row 25; scope migration caveat | artifact Section 7 | reflookup/refverify required before manuscript use | Established x 4 |
| 18 | Federated multi-discipline test-bed missing; no graded $D_s$ spectrum; VM5/10/14/15 untested | Known gaps | session notes open items; artifact Section 7 | notes "Open items"; artifact flags | Read both this session | Established x 4 |
| 19 | F1, F7 remain OPEN; this skill does not resolve them; D-3 resolution routed as candidate only | Compliance | preamble guardrails; this skill | Sections header, 5, 8 | Checked: no resolving language used | Established x 5 |
| 20 | Wymore-vs-ours novelty line as stated | Governing framing | scope convergence log item 4; session notes Capsule 2.6; artifact Section 5 | as cited | Cross-checked across all three sources this session | Established x 5 |
