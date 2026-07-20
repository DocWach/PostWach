# Decision-Layer Evidence / Opinion Fusion: Inventory for WySE Mapping

**Date:** 2026-07-15
**Author / agent:** Literature Reviewer (claude-sonnet-4-6, Anthropic, Claude Code CLI)
**R016 status:** Everything catalogued here is **(a) research artifact** prior art. Nothing is built,
connected, or integrated in this repository. The WySE decision layer is itself (a).
**R018 provenance:** claude-sonnet-4-6, Anthropic, Claude Code CLI, 2026-07-15; principal-directed
scoping task; writes to `research/data-fusion-inventory/` only.
**R019 gate:** All cited keys are drawn from `approved.bib` or flagged [PLACEHOLDER]. No invented
DOIs or page numbers. Run `scripts/refcheck.py` before any manuscript use.

---

## Scope

This inventory covers **evidence, opinion, and decision fusion** as distinct from sensor fusion
(raw signal integration) and multi-model ensemble fusion (model averaging in ML). The boundary
criterion: the combiner operates on **already-reduced summaries of evidence** -- scores,
probabilities, belief masses, utility ratings -- rather than on raw observations. This matches the
WySE decision layer, which receives structured model-adequacy assessments and must produce an
acceptability verdict or a confidence-weighted ordering.

The WySE decision-layer frame (from context, not re-derived here):

- **T3SD lineage** (Daniels, Werner, Bahill 2001; approved key `daniels2001quantitative`): sixteen
  scalar scoring functions (SSF1-16) paired with six combining functions: linear, product,
  exponential, sum-minus-product, compromise, and certainty-factor.
- **Kannan acceptability lineage** (approved key `kannan2019preference`; approved key
  `kannan2026theory`): a preference partial order (poset) over the solution space; acceptable =
  maximal elements; incomparability is structurally allowed (Theorem 3 of `kannan2019preference`).
- **Bayesian/TRAK posterior lineage**: a posterior probability over model adequacy; scalar.
- **Candidate F2 result** (as cited in task context): among the six T3SD combiners, exactly
  {product, weighted-product, min, geometric-mean} preserve the veto / annihilation property
  (a zero input drives the aggregate to zero). The linear combiner and the compromise combiner do
  NOT have this property.
- **Open research object**: a "confidence-weighted acceptability ORDER" -- a distribution over the
  Kannan poset, not over a scalar -- that respects incomparability rather than collapsing it.

The inventory maps each fusion family to these three lineages and assesses Fable-shape potential.

---

## Method Families Table

### F1. Linear Opinion Pooling (LOP)

| Attribute | Detail |
|---|---|
| **Operator** | $C_{\mathrm{LOP}}(p_1,\ldots,p_n) = \sum_i w_i p_i$, with $w_i \ge 0$, $\sum_i w_i = 1$; output is a probability distribution |
| **Idempotent?** | Yes (equal inputs, uniform weights) |
| **Associative?** | Yes (weighted average is associative over groupings with renormalized weights) |
| **Annihilator / veto?** | No. A zero probability from one expert does NOT drive the aggregate to zero unless $w_i = 1$. |
| **Monotone?** | Yes: stochastically (each $p_i \le q_i$ pointwise implies $C_{\mathrm{LOP}}(\mathbf{p}) \le C_{\mathrm{LOP}}(\mathbf{q})$) |
| **Totalizes?** | Yes: outputs a probability distribution, imposing a total order via expected value |
| **Canonical reference** | [PLACEHOLDER: Genest, C. and Zidek, J.V. (1986). "Combining probability distributions: A critique and annotated bibliography," *Statistical Science*. Verify journal, volume, pages via external source before manuscript use.] |
| **SE-domain grounding** | `stephen2024formal` (Kannan, Salado, Stephen 2024) formally identifies LOP as one of the "expertise aggregation techniques" used in SE teams and proves formal inconsistencies when aggregating preference rankings |

### F2. Logarithmic Opinion Pooling (LogOP)

| Attribute | Detail |
|---|---|
| **Operator** | $C_{\mathrm{LogOP}}(p_1,\ldots,p_n) \propto \prod_i p_i^{w_i}$; output is a normalized geometric mean of probability distributions |
| **Idempotent?** | Yes |
| **Associative?** | Yes (with weight renormalization) |
| **Annihilator / veto?** | Yes. If any $p_i(\omega) = 0$ for outcome $\omega$, the aggregate assigns probability 0 to $\omega$ for any positive $w_i$ (veto by zero). This matches the {product, geometric-mean} class in F2. |
| **Monotone?** | Yes (pointwise over log space) |
| **Totalizes?** | Yes: outputs a probability distribution |
| **Key property** | Satisfies "external Bayesianity" (updating then pooling = pooling then updating) -- LOP does not |
| **Canonical reference** | [PLACEHOLDER: Genest, C. (1984). "A characterization theorem for externally Bayesian groups," *Annals of Statistics*. Verify before manuscript use.] |
| **Note on SSF combiners** | The T3SD "product" combiner ($\prod_i s_i$) is the score-domain analogue of LogOP; the T3SD "exponential" combiner ($\prod_i s_i^{w_i}$) is the weighted-exponent variant. Both carry the veto. F2's classification is thus a score-domain instance of the LOP/LogOP distinction. |

### F3. Bayesian Evidence Combination / Bayes Factors

| Attribute | Detail |
|---|---|
| **Operator** | Sequential update: $P(H \mid E_1,\ldots,E_n) \propto P(H) \prod_i P(E_i \mid H)$ (assuming conditional independence of evidence given $H$); equivalently $K = \prod_i B_i$ where $B_i = P(E_i \mid H_1)/P(E_i \mid H_0)$ |
| **Idempotent?** | No: adding a second copy of evidence $E_i$ doubles its log-weight |
| **Associative?** | Yes: sequential Bayesian updating is order-invariant under conditional independence |
| **Annihilator / veto?** | Yes, in the log-odds form: $B_i = 0$ (evidence $E_i$ is impossible under $H_1$) drives posterior to zero. This is structural veto. |
| **Monotone?** | Yes in log-odds: positive Bayes factors increase posterior log-odds monotonically |
| **Totalizes?** | Yes: posterior probability is a scalar, yielding a total order over hypotheses |
| **Known pathology** | Naive product assumes conditional independence of evidence; violation produces overconfident posteriors (known as "double counting" or "washing" in sensor fusion) |
| **Canonical reference** | [PLACEHOLDER: Kass, R.E. and Raftery, A.E. (1995). "Bayes Factors," *Journal of the American Statistical Association*, vol. 90, no. 430. Verify pages before manuscript use.] |
| **WySE connection** | The Bayesian/TRAK posterior lineage in the WySE decision layer is exactly this operator applied to model-adequacy hypotheses. The T3SD "certainty-factor" combiner is a heuristic approximation of log-odds update (without a proper prior). |

### F4. Dempster-Shafer (DS) Belief Function Combination

| Attribute | Detail |
|---|---|
| **Operator** | Dempster's orthogonal sum: $m_1 \oplus m_2(A) = \frac{\sum_{B \cap C = A} m_1(B) m_2(C)}{1 - K}$ where $K = \sum_{B \cap C = \emptyset} m_1(B) m_2(C)$ is the conflict mass; the denominator renormalizes |
| **Idempotent?** | No (combining a source with itself doubles its evidential weight) |
| **Associative?** | Yes (Dempster's rule is associative over belief functions on the same frame) |
| **Annihilator / veto?** | Partial: a focal element assigned mass 1 by one source can concentrate the aggregate; under total conflict ($K = 1$) the rule is undefined -- the notorious Zadeh counterexample (see below) |
| **Monotone?** | Not in general: adding evidence can decrease belief in a hypothesis |
| **Totalizes?** | No: belief and plausibility are lower and upper bounds; the interval $[\mathrm{Bel}(A), \mathrm{Pl}(A)]$ represents evidential ignorance, preserving a form of incomparability for subsets |
| **Zadeh's counterexample** | Two experts assign near-total mass to disjoint hypotheses ($H_1$ and $H_2$ say) with a small overlap on $H_3$; Dempster's rule yields near-total mass on $H_3$ despite both experts considering it negligible. The renormalization step moves all conflict mass onto the intersection, an intuitively counterintuitive result. |
| **Conflict pathology** | High-conflict situations ($K$ near 1) produce brittle, unstable aggregates. Many modified rules exist (Yager's rule, Smets' non-normalized TBM, Dezert-Smarandache theory) to address this. |
| **Key property** | Represents imprecision (ignorance) explicitly, not as a uniform distribution over unknowns -- closer in spirit to the Kannan poset's preservation of incomparability than scalar combiners |
| **Canonical reference** | [PLACEHOLDER: Shafer, G. (1976). *A Mathematical Theory of Evidence*. Princeton University Press. Verify before manuscript use.] |
| **SE-domain grounding** | `salado2026survey` (Salado 2026) surveys evidence aggregation for architectural ilities decisions and includes DS-family methods as a candidate family; `xu2022expert` (Xu, Cho, Salado 2022) applies subjective logic (a Bayesian extension of DS theory) to expert opinion fusion for fault diagnosis |

### F5. Possibility Theory and Fuzzy Aggregation

| Attribute | Detail |
|---|---|
| **Operator family** | t-norms (for conjunction / AND): $T(a,b)$ with $T(1,b)=b$, $T(0,b)=0$; t-conorms (for disjunction / OR): $S(a,b)$ with $S(0,b)=b$, $S(1,b)=1$; standard examples: min/max (Godel), product/$1-(1-a)(1-b)$ (probabilistic), Lukasiewicz |
| **Idempotent?** | min and max are idempotent; product and Lukasiewicz are not |
| **Associative?** | All standard t-norms and t-conorms are associative |
| **Annihilator / veto?** | Every t-norm has annihilator at 0: $T(a,0)=0$ for all $a$. Every t-conorm has annihilator at 1: $S(a,1)=1$ for all $a$. The min t-norm is the strongest veto (minimum score governs). |
| **Monotone?** | Yes: all t-norms are monotone non-decreasing in each argument |
| **Totalizes?** | Not necessarily: possibility distributions assign $\Pi(A)$ and necessity $N(A) = 1-\Pi(\neg A)$; $[\Pi(A), N(A)]$ can be non-degenerate, preserving uncertainty |
| **OWA (Ordered Weighted Averaging) operators (Yager 1988)** | $\mathrm{OWA}_\mathbf{w}(a_1,\ldots,a_n) = \sum_i w_i b_i$ where $b_i$ is the $i$-th largest value. Special cases: $\mathbf{w}=(1,0,\ldots,0)$ = max; $\mathbf{w}=(0,\ldots,0,1)$ = min; uniform $\mathbf{w}$ = arithmetic mean. OWA interpolates between optimism (max) and pessimism (min). |
| **OWA annihilator?** | Only the min-weight vector produces a pure veto; intermediate vectors smooth the veto. |
| **Canonical references** | [PLACEHOLDER: Dubois, D. and Prade, H. (1988). *Possibility Theory*. Plenum Press. Verify before manuscript use.] [PLACEHOLDER: Yager, R.R. (1988). "On ordered weighted averaging aggregation operators in multicriteria decision-making," *IEEE Transactions on Systems, Man, and Cybernetics*. Verify volume, pages.] |
| **SE grounding** | The T3SD "compromise" combiner is a weighted sum of the score and the best-minus-worst penalty -- structurally related to the OWA family. It does not have an annihilator at 0, consistent with its exclusion from the F2 veto class. |

### F6. Multi-Criteria Aggregation: Choquet and Sugeno Integrals

| Attribute | Detail |
|---|---|
| **Choquet integral** | $C_\mu(f) = \int_0^\infty \mu(\{i : f(i) \ge t\}) \, dt$ where $\mu$ is a non-additive (fuzzy) measure / capacity; generalizes weighted average by allowing the weight of a coalition of criteria to be non-additive (interactions: $\mu(A \cup B) \ne \mu(A) + \mu(B)$) |
| **Sugeno integral** | $S_\mu(f) = \max_{A \subseteq N} \min(\mu(A), \min_{i \in A} f(i))$; a max-min dual to Choquet; ordinal scale only |
| **Idempotent?** | Yes for both (constant inputs return that constant) |
| **Associative?** | Not in general (capacity interactions break simple chaining) |
| **Annihilator / veto?** | Choquet: yes if $\mu(\{i\}) = 0$ for some criterion $i$ and the capacity is not subadditive enough to compensate; in general, a criterion with zero individual importance in $\mu$ can still be compensated by coalitions. Min-interaction capacity recovers the t-norm (min) veto. Sugeno: the min in the inner term creates a veto: any criterion achieving min drives the integrand. |
| **Monotone?** | Yes for both (monotone capacity + monotone integrand implies monotone integral) |
| **Totalizes?** | Yes for Choquet (scalar output); Sugeno outputs a lattice value (ordinal), still total on a linearly ordered scale |
| **Key property** | The capacity $\mu$ encodes dependencies among criteria (synergy, redundancy) -- no other scalar aggregator in common use does this without additional assumptions |
| **Canonical reference** | [PLACEHOLDER: Grabisch, M., Marichal, J.-L., Mesiar, R., and Pap, E. (2009). *Aggregation Functions*. Cambridge University Press. Verify before manuscript use.] |
| **WySE connection** | When model-adequacy criteria are known to interact (e.g., two coverage metrics are partially redundant), a Choquet integral over them is a principled aggregator. The Kannan poset does not encode interactions directly; a Choquet capacity could function as an interaction model over the requirements space. |

### F7. Imprecise Probability / Credal Set Fusion

| Attribute | Detail |
|---|---|
| **Framework** | A credal set $\mathcal{K}$ is a convex set of probability distributions; a lower probability $\underline{P}(A) = \min_{P \in \mathcal{K}} P(A)$ and an upper probability $\overline{P}(A) = \max_{P \in \mathcal{K}} P(A)$ are the extremes. Imprecise probabilities generalize both DS theory (credal sets from capacity structures) and classical Bayesian analysis (singleton $\mathcal{K}$). |
| **Fusion operator** | Natural extension: the set of all probability distributions consistent with the credal sets of individual sources; the result is the intersection of credal sets (most cautious rule, no pooling loss) or the convex hull of their union (least-cautious / conjunctive) |
| **Idempotent?** | Yes (intersecting a set with itself returns itself) |
| **Associative?** | Yes |
| **Annihilator / veto?** | Under intersection: if any source credal set places lower probability 0 on $A$, the aggregate preserves $\underline{P}(A) = 0$. This is a weak veto (it survives as a lower bound, not as certainty of exclusion). |
| **Monotone?** | Yes under the natural order on credal sets (containment) |
| **Totalizes?** | No: incomparability between distributions in $\mathcal{K}$ is preserved; two events $A$ and $B$ may be incomparable under $\underline{P}$ (neither $\underline{P}(A) \ge \underline{P}(B)$ nor vice versa in all distributions) |
| **Key property** | This is the framework that most directly models a "distribution over incomparable outcomes." The credal set is a set of probability measures; the poset ordering of hypotheses is encoded in the envelope structure. This is the closest existing framework to the open WySE research object (a "confidence distribution over the Kannan poset"). |
| **Canonical reference** | [PLACEHOLDER: Walley, P. (1991). *Statistical Reasoning with Imprecise Probabilities*. Chapman and Hall. Verify before manuscript use.] |
| **SE-domain grounding** | `xu2026set` (Xu, Salado 2026): set-based verification planning under knowable uncertainty uses a family-of-distributions framing structurally related to credal sets; `salado2026survey` discusses imprecise-probability approaches as a candidate family for ilities aggregation. |

### F8. Subjective Logic (Jøsang)

| Attribute | Detail |
|---|---|
| **Framework** | A subjective opinion is a triple $\omega = (b, d, u)$ with $b + d + u = 1$; $b$ = belief, $d$ = disbelief, $u$ = uncertainty mass; a base-rate $a$ maps to a projected probability $P = b + au$. Subjective logic is a formalized version of DS theory with a Bayesian projection. |
| **Fusion operator** | Cumulative fusion (Jøsang): $\omega_1 \oplus \omega_2$ defined to share evidence; averaging fusion (consensus): $\omega_1 \underline{\oplus} \omega_2$ for independent sources on the same topic |
| **Annihilator / veto?** | Under cumulative fusion, $b_1 = 0$ does not veto (uncertainty absorbs); under a product-based operator, yes |
| **Totalizes?** | No: subjective opinions retain an uncertainty mass $u > 0$ representing ignorance, which preserves a form of incomparability |
| **Canonical reference** | [PLACEHOLDER: Jøsang, A. (2016). *Subjective Logic: A Formalism for Reasoning Under Uncertainty*. Springer. Verify before manuscript use.] |
| **SE-domain grounding** | `xu2022expert` (Xu, Cho, Salado 2022): applies subjective logic to expert opinion fusion for fault diagnosis in SE context; directly adjacent to the WySE decision layer |

---

## WySE Decision-Layer Mapping

| Fusion family | Annihilator / veto? | Preserves incomparability? | Totalizes? | Closest WySE lineage | Key tension |
|---|---|---|---|---|---|
| F1 Linear Opinion Pool | No | No | Yes | T3SD linear combiner (exact match) | Cannot represent expert disagreement as a structural incomparability |
| F2 Logarithmic Opinion Pool | Yes (zero-veto) | No | Yes | T3SD product/geometric-mean combiners (F2 classification) | Veto is structurally correct but still totalizes |
| F3 Bayesian / Bayes Factors | Yes (structural veto) | No | Yes | Bayesian/TRAK posterior lineage (exact) | Conditional independence assumption often violated in SE evidence |
| F4 Dempster-Shafer | Partial (conflict-sensitive) | Partially (Bel/Pl interval) | No (interval) | No current WySE lineage; adjacent to uncertainty representation in Kannan | Zadeh pathology; renormalization destroys the preservation of incomparability under conflict |
| F5 t-norms / OWA | Yes (min = strongest veto) | No (scalar output) | Yes | T3SD "compromise" combiner family; OWA spans linear to min | min-OWA is the scalar projection of the Kannan max-element (most pessimistic acceptable); not the same as the poset |
| F6 Choquet / Sugeno | Yes (for appropriately zero-weighted criteria; Sugeno min) | No (scalar) | Yes (Choquet); ordinal (Sugeno) | No direct WySE lineage; addresses criterion-interaction gap | Interaction model (capacity) requires elicitation; capacity space exponential in criteria count |
| F7 Imprecise Probability / Credal | Weak (lower bound zero) | Yes (envelope preserves it) | No | Open WySE research object ("distribution over poset"): this is the closest prior art | Computationally demanding; credal set intersection is intractable at scale |
| F8 Subjective Logic | Partial | Partially ($u > 0$) | No | Adjacent to Bayesian/TRAK + DS interface | Formalism matures quickly; `xu2022expert` is an approved anchor |

**Key structural observation.** The Kannan acceptability poset (approved key `kannan2019preference`)
preserves incomparability by design: Theorem 3 proves that no total order exists over the solution
space in the general case. Every standard scalar combiner (F1-F3, F5, F6) totalizes, collapsing
incomparable alternatives into a linear ranking. Only F4 (DS Bel/Pl interval), F7 (credal set),
and F8 (subjective logic with $u > 0$) preserve a non-degenerate notion of incomparability. F7 is
the most principled framework for the open research object.

**Key veto observation.** F2's classification (product/geometric-mean/min/weighted-product carry
the veto; linear/compromise do not) is a score-domain instance of a general algebraic property
that applies uniformly across F1-F7: operators that "zero-out" at the boundary are exactly the
multiplicative / min-based ones. This is well-known in aggregation theory (t-norm boundary
condition). The F2 result is therefore not a new observation for aggregation theorists, but it
*is* a new theorem at the WySE score-domain level where the six T3SD combiners are the specific
objects of study. That specificity is the Fable-shape value.

---

## Fable-Shape Candidates

Ranked by estimated payoff and feasibility. Each entry states a crisp provable claim, a witness
sketch, and its relationship to existing candidates A-E, F2, F17.

---

### FC-1 (HIGH PRIORITY): LogOP-to-Kannan non-collapse theorem

**Provable claim:** For any finite set of alternatives containing at least one incomparable pair
under the Kannan acceptability order (Def. 2 of `kannan2019preference`), every weighted
logarithmic opinion pool (equivalently: every combiner in the T3SD {product, geometric-mean} veto
class) applied to their score vectors induces a total order on the alternatives, collapsing the
incomparable pair to a strict preference.

**Why this is crisp:** The Kannan poset has at least one incomparable pair on any non-trivial
requirement space (Kannan 2019 Theorem 3). A LogOP output is a scalar, hence total. The claim is
that the collapse is universal (no weighting scheme recovers incomparability), not just common.

**Witness sketch:** Construct a 3-alternative, 2-criterion instance where alternatives $A_1$ and
$A_2$ are incomparable under the Kannan order (each satisfies criteria the other violates). Assign
score vectors. Enumerate all weight vectors $\mathbf{w}$ in $\Delta^2$ (the 2-simplex). Show that
$\sum_j w_j \ln s_{1j} \ne \sum_j w_j \ln s_{2j}$ for all $\mathbf{w}$ (generically) -- i.e.,
the weighted log-sum always produces a strict ranking. Then show by structure that any
counterexample would require $\ln s_{1j} = \ln s_{2j}$ for all $j$, which contradicts the
Kannan incomparability premise. A finite exhaustive check on rational score instances is
machine-checkable and emits a stable hash.

**Relation to existing work:** Extends F2 (the veto classification) by adding the order
consequence. Adjacent to Target C (pedigree--acceptability morphism) but operates at the
combiner level, one layer below. Genuinely new Fable target; not a sub-case of any named
candidate A-E, F2, F17.

---

### FC-2 (HIGH PRIORITY): Credal-set envelope as the canonical "distribution over poset"

**Provable claim:** The open WySE research object -- a "confidence-weighted acceptability order"
-- is exactly a credal set over probability distributions on the Kannan solution space, where the
lower envelope $\underline{P}$ maps to the necessity measure $N$ and the upper envelope
$\overline{P}$ maps to the possibility measure $\Pi$ of the Kannan acceptability test. The
credal set preserves incomparability (two alternatives $x, y$ are incomparable in the poset if
and only if there exists $P \in \mathcal{K}$ with $P(x \succ y) > P(y \succ x)$ and
$P' \in \mathcal{K}$ with the reverse, i.e., neither dominates in all distributions).

**Why this is crisp:** The Kannan poset is defined over a finite solution space with the
requirement satisfaction structure from `kannan2019preference`. A credal set over a finite sample
space has a finite-dimensional representation. The claimed equivalence is a structural
correspondence, not an approximation. Its key checkable consequence is the preservation theorem:
incomparable pairs in the poset correspond to non-dominated pairs in the credal set.

**Witness sketch:** Instantiate a small requirement space (3 alternatives, 2 requirements) with
an incomparable pair established by the Kannan Def. 2 conditions. Construct the minimal credal
set consistent with the scoring data. Enumerate all $P \in \mathcal{K}$ (finitely many extreme
points) and verify the bidirectional ordering claim for each pair.

**Relation to existing work:** This is the key "new Fable target" at the intersection of F7
(imprecise probability) and the Kannan lineage. It would be the first candidate that does not
totalize while maintaining a computational witness. Adjacent to Target C (the enriched pedigree
conjecture) but operates on the output side of the decision layer, not the pedigree input side.
Genuinely new.

---

### FC-3 (MEDIUM PRIORITY): DS conflict mass as a structural analogue of Kannan incomparability

**Provable claim:** The DS conflict mass $K = \sum_{B \cap C = \emptyset} m_1(B) m_2(C)$ between
two experts is strictly positive if and only if their focal elements are non-nested, and the
post-combination Bel/Pl interval is strictly wider than for a single expert. Specifically: $K > 0$
implies $\mathrm{Pl}(A) - \mathrm{Bel}(A) > 0$ for at least one focal subset $A$, preserving an
interval of evidential ignorance that cannot be collapsed by Dempster's rule without additional
information.

**Why this is crisp:** This is a purely algebraic property of the DS combination rule with
specific focal-set structures. It can be checked exhaustively on small frames.

**Witness sketch:** 3-hypothesis frame; two experts with disjoint focal elements (conflict case).
Compute $K$, then $\mathrm{Bel}(H_i)$ and $\mathrm{Pl}(H_i)$ for each $H_i$. Verify that the
Bel/Pl gap is non-zero. Contrast with the Bayesian posterior (always a singleton distribution,
gap = 0). The witness encodes Zadeh's counterexample as a boundary case where the renormalization
pathology is most visible.

**Limitation:** DS combination under high conflict ($K$ near 1) is the Zadeh pathology, which
makes this result load-bearing for the "when NOT to use Dempster's rule" argument but potentially
not for the positive "use this" argument. A companion witness should demonstrate the pathology
explicitly.

**Relation to existing work:** No current WySE candidate addresses DS theory. This would be a new
entry, with `salado2026survey` and `xu2022expert` as approved SE anchors.

---

### FC-4 (MEDIUM PRIORITY): Choquet integral as capacity-encoded T3SD generalization

**Provable claim:** The T3SD linear combiner (weighted average of scoring functions) is exactly
the Choquet integral with an additive capacity (i.e., $\mu(A) = \sum_{i \in A} w_i$). The T3SD
product combiner is the Choquet integral with the capacity defined by the geometric-mean, which
is a specific non-additive capacity. Therefore, the six T3SD combining functions span only a
strict sub-class of all possible Choquet integrals, and the F2 veto-preservation result is a
special case of the Choquet boundary condition (where zero on any focal element drives the
integral to zero for multiplicative capacities).

**Why this is crisp:** The Choquet integral with additive capacity is the weighted average; this
is a standard result in aggregation theory. Checking that the T3SD product combiner corresponds
to a specific non-additive capacity is a finite algebraic verification.

**Witness sketch:** Enumerate the six T3SD combiners. For each, identify the capacity $\mu$ (or
show it is not a Choquet integral in the standard sense). Compute the Choquet integral for each
and verify the formula. This is a definitional check, checkable by symbolic computation.

**Value:** If proved, the Choquet framing generalizes the T3SD combiner algebra beyond six options
to the full space of non-additive capacities, enabling criterion-interaction modeling that the
original T3SD did not contemplate.

**Relation to existing work:** Extends F2 by embedding the six combiners into the Choquet
lattice. Genuinely new at the WySE level; not a sub-case of candidates A-E, F2, F17.

---

### FC-5 (LOWER PRIORITY): OWA orness / andness as a formalizable uncertainty-pessimism dial

**Provable claim:** The OWA operator family parameterized by weight vector $\mathbf{w}$ induces a
monotone map from the "orness" measure $\alpha(\mathbf{w}) = \sum_i w_i (n-i)/(n-1) \in [0,1]$
to the resulting aggregate score. Specifically: (a) orness 1 = maximum = most optimistic =
no veto; (b) orness 0 = minimum = most pessimistic = full veto; (c) for any incomparable pair
under the Kannan order, there exists a threshold orness $\alpha^*$ below which the OWA aggregate
ranks $A_2 \succ A_1$ and above which $A_1 \succ A_2$, implying that the OWA operator cannot
preserve the incomparability -- it always resolves it, but the resolution direction is
orness-dependent.

**Why this is crisp:** The orness--aggregate monotonicity is a known result ([PLACEHOLDER: Yager
1988]). The Kannan incomparability threshold is a finite computation. Claim (c) is checkable on
the same 3-alternative instance as FC-1.

**Relation to existing work:** Related to FC-1 but uses the OWA family instead of LogOP. Lower
priority than FC-1 and FC-2 because OWA is less directly connected to the T3SD six-combiner
taxonomy.

---

### FC-6 (LOWEST PRIORITY / LONGER HORIZON): Enriched poset as an imprecise-probability
       acceptability structure

**Provable claim:** The enriched pedigree conjecture from Target C ($\pi = (m, \delta, p)$ with
coordinate-wise monotonicity) is representable as a credal set over the Kannan solution space,
where the pedigree coordinate $m$ bounds the structural coverage (lower probability on
unverified regions), the descriptor coordinate $\delta$ refines the credal set (tightens the
envelope as descriptor adequacy increases), and the condition profile $p$ adds further constraints
(each VMMC condition that holds removes probability mass from failure scenarios).

**Why this is longer horizon:** Requires Target C's PO-3 and PO-4 to be discharged first. The
credal set framing is a proposed representation, not yet grounded in the specific VMMC data.

**Value:** This would bridge the pedigree/acceptability side (Target C) with the decision-layer
confidence-distribution object, completing a loop from model generation through morphism
measurement to decision. The most impactful long-range Fable target.

**Relation to existing work:** Extends Target C into the F7 (credal set) framework. The bridge
between the enriched pedigree and the Kannan poset is already the "weld" problem (Section 7.3
of `morphism-domain-reference`); FC-6 proposes that the weld IS the credal-set construction.

---

## Refs-to-Verify

Items flagged [PLACEHOLDER] in the table above. None are currently in `approved.bib`. All require
Byzantine-Bayesian verification per R019 before manuscript use.

| Placeholder label | Claim | Priority for verification |
|---|---|---|
| Genest & Zidek 1986 | Canonical LOP bibliography and critique | FC-1, FC-2: high |
| Genest 1984 | External Bayesianity characterization of LogOP | FC-2: high |
| Kass & Raftery 1995 | Bayes factors canonical reference | FC-3 anchor: medium |
| Shafer 1976 | DS theory foundational monograph | FC-3: high if DS work proceeds |
| Dubois & Prade 1988 | Possibility theory monograph | FC-5: medium |
| Yager 1988 | OWA operators original paper | FC-5: high if OWA work proceeds |
| Grabisch et al. 2009 | *Aggregation Functions* monograph | FC-4: high if Choquet work proceeds |
| Walley 1991 | Imprecise probabilities monograph | FC-2: highest priority |
| Jøsang 2016 | Subjective logic monograph | adjacent; medium |

**Already in `approved.bib` and immediately usable:**

| Key | Entry | Role |
|---|---|---|
| `daniels2001quantitative` | Daniels, Werner, Bahill 2001 | T3SD grounding for all candidates |
| `kannan2019preference` | Kannan et al. 2019 | Kannan poset; incomparability theorem |
| `kannan2026theory` | Kannan-Salado 2026 | Bayesian/belief-transfer layer |
| `stephen2024formal` | Stephen, Kannan, Salado 2024 | Formal inconsistencies in SE aggregation |
| `xu2022expert` | Xu, Cho, Salado 2022 | Subjective logic in SE opinion fusion |
| `salado2026survey` | Salado 2026 | Survey of evidence aggregation for ilities |

---

## Gaps

1. **No SE-grounded treatment of the LOP/LogOP distinction** exists in the approved store. The
   `stephen2024formal` paper proves formal inconsistencies in SE aggregation but does not classify
   the six T3SD combiners into LOP vs LogOP families. FC-1 fills this gap.

2. **No credal-set / imprecise-probability paper** is in the approved store for the WySE decision
   layer. The open research object (distribution over the Kannan poset) lacks a prior-art anchor
   beyond Walley 1991 [PLACEHOLDER]. This is the highest-priority gap for the FC-2 research
   thread.

3. **Criterion-interaction modeling is absent** from both the Kannan poset and the T3SD framework.
   The Kannan poset is defined over an ordered set of requirements but does not model synergy or
   redundancy among requirements. Choquet integrals (FC-4) would address this but require an
   approved monograph anchor (Grabisch et al. 2009 [PLACEHOLDER]).

4. **The DS/Kannan interface is unexplored.** The DS Bel/Pl interval is structurally analogous to
   the Kannan poset's incomparability structure (neither collapses to a scalar), but no paper in
   the approved store draws this connection. FC-3 is the first attempt.

5. **Conditional independence is assumed throughout** the Bayesian/TRAK lineage. In SE, evidence
   from two verification models often depends on shared physical properties (e.g., both test the
   same failure mode). The approved store has no treatment of evidence correlation in the
   Bayesian/SE context.

6. **The T3SD scoring functions (SSF1-16) are not mapped to the Choquet/OWA taxonomy.** The six
   combining functions are classified (F2 result), but the sixteen scoring functions -- which
   operate on raw criteria before combination -- are not mapped to any standard aggregation
   framework. This is a downstream gap after FC-4.
