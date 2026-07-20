# SCOPING NOTE — F28: Homomorphic-Encryption Noise as a Genuinely Non-Vanishing D_b

**STATUS:** scoping note ONLY. Integration status **(a) research artifact / hunch** throughout (R016).
Nothing here is derived, witnessed, or run. This note scopes the seed to the point where a future
session could run it. Do NOT read any claim below as established — everything is CANDIDATE / OPEN.
This is **item 2 spun out of the F27 debate as its own, cleaner entry** — see Section 7 for the split.

**PROVENANCE (R018):** authored by Opus 4.8 (claude-opus-4-8[1m]), vendor Anthropic, access mode
Claude Code CLI, principal-directed research subagent, 2026-07-16. Sources read-only; the only repo
mutation is this file.

**FRAME:** WySE = Wymorian systems theory. `D_b` is a Lawvere `[0,∞]`-enriched **behavioral** distance
between two systems' behaviors. The morphism library carries a **LOAD-BEARING but ASSERTED** claim
(`morphism-domain-reference` §4.4 / D-5; Target C settled decision 3; rigor: **asserted, not axiom**):

> "On a DEVS carrier the structure exactly generates the behavior, so there is no discretization gap,
> `D_b` vanishes, and `D_s` alone is the pedigree measure; `D_b` re-emerges only **off-carrier**, as
> the fidelity of a DEVS-ification."

The claim is deliberately encoded as **REVISABLE** (D-5 keeps `D_b` an optional slot precisely so the
schema stays honest "if the carrier bet fails"). F28 is a candidate **witness/test** of this assertion.

**R019 NOTE:** every bibliographic entry below is [PLACEHOLDER], NOT in the approved-references store.
None may be cited in a manuscript until it passes refverify. DOIs are deliberately NOT drafted.

---

## 0. The hook (why this is a SEPARATE seed from F27)

F27 already read HE noise as a `D_b` instance — but as a **threshold-jump** correctness margin: `D_b = 0`
while `Dec` is correct, then jumps to `∞` ("wrong plaintext") past the noise ceiling. That reading is a
*fidelity residual* shape (it measures whether the ciphertext system still reproduces plaintext behavior),
and it is compatible with the §4.4 assertion: the jump is exactly a DEVS-ification-fidelity failure.

F28 makes a **sharper, cleaner move**. In lattice HE the ciphertext noise does not merely sit below an
opaque threshold — it lives under the **canonical embedding** `σ: R = Z[x]/(x^n+1) → C^n` (evaluate the
ring element at the `2n`-th roots of unity), where it has a **real geometric norm** `||σ(e)||`. That norm
is:

- **intrinsic** to the ciphertext (it is a property of the carrier element itself, not of any comparison
  to "the actual thing"),
- **non-vanishing** (nonzero for any nontrivial ciphertext — fresh ciphertexts already carry noise), and
- **monotone growing** with homomorphic operations (adds under `+`, multiplies under `×`), and
- **a provable metric** — `d_σ(ct_1, ct_2) = ||σ(e_1) − σ(e_2)||` is a genuine metric (a Euclidean norm
  pulled back through a ring embedding), hence a Lawvere `[0,∞]`-enriched distance.

So HE offers a **well-defined system where a Lawvere `D_b` is intrinsic, non-zero, and provably a metric**
— a candidate **counter-instance** to the unqualified "`D_b` vanishes on the carrier" assertion. The F28
delta is therefore **not** "HE is a homomorphism" (that is F27's ceded prior art) and not the
threshold-jump reading (that is F27's `D_b` shape). It is a contribution to **WySE's OWN D_b theory**:
does the canonical-embedding noise metric fall under "off-carrier fidelity," or is it an on-carrier,
intrinsic, non-vanishing `D_b` the assertion does not cover — thereby **sharpening D-5**.

---

## 1. The precise WySE carrier — what system does this D_b measure?

The subtle question the seed must pin down first: **which system, and is HE on or off the DEVS carrier?**

**The system z_C (ciphertext system).** Carrier `SZ_C` = ciphertexts (elements of `R_q^k`, lattice
elements), each carrying a hidden noise term `e ∈ R`. `NZ_C` = ciphertext gates (`+`, `×`, key-switch,
mod-switch), each of which **also transforms `e`**. `RZ_C` = decryption `Dec`, correct only while the
noise is small.

**The behavior D_b measures — two candidate readings, and F28 chooses the SECOND:**

- **Reading (I), the F27/fidelity reading (ceded to F27):** the behavior is the **decrypt-correctness**
  trajectory — does `z_C` reproduce `z_P`'s plaintext arithmetic? `D_b` = divergence of `Dec(eval_C)` from
  `plaintext-eval`. This is a *fidelity of the DEVS-ification* (ciphertext system vs. the plaintext "actual
  thing"), which is exactly the case §4.4 says is legitimately off-carrier. F27 owns this.

- **Reading (II), the F28 intrinsic-metric reading (the NEW object):** the behavior is the **noise
  trajectory itself** — the sequence `σ(e_0), σ(e_1), …` of canonical-embedding images as the circuit runs.
  `D_b` = the `||σ(·)||` geometric distance between two ciphertexts (or between a ciphertext and a
  noise-free reference `σ(e)=0`). This is a distance defined **on the carrier elements**, evaluated by the
  ring embedding, with NO reference to "the actual thing" — it is intrinsic. **This is the seed's object.**

**On/off the DEVS carrier — the load-bearing scoping distinction.** Two sub-cases the run must separate:

1. **The ciphertext ring as its OWN carrier.** If we take `z_C` at face value — a discrete-event system
   whose states are lattice elements and whose transitions are ciphertext gates — then the noise metric
   `d_σ` is an **on-carrier, intrinsic** distance between states of a single system. Under this framing the
   assertion "`D_b` vanishes on the carrier" is directly challenged: here is an on-carrier system carrying a
   non-vanishing, provable Lawvere metric between its own trajectories. **This is the sharp counter-instance.**

2. **The plaintext ring as the carrier, ciphertext as a DEVS-ification of it.** If instead `z_P` (exact
   plaintext arithmetic) is "the carrier" and `z_C` is a *lattice DEVS-ification* of it, then the assertion's
   escape clause applies: the noise IS the fidelity residual of the DEVS-ification, legitimately off-carrier,
   and F28 collapses back into F27. **The run must show sub-case (1) is a faithful, non-degenerate framing**
   — i.e. that the ciphertext system is a system in its own right whose *own behavior* (noise trajectory)
   carries the metric, not merely a lossy shadow of `z_P`. The whole bite of F28 hinges on defending (1)
   over (2). If (1) cannot be defended, F28 is not distinct from F27 and should be folded back.

**Working position (candidate).** The defensible claim is the **narrow** one: the canonical-embedding
noise functional is a genuine Lawvere metric on the ciphertext carrier, so **the unqualified assertion
"`D_b` vanishes on the DEVS carrier" is FALSE as stated** — it holds only under the additional premise that
the carrier's structure exactly generates a *noise-free* behavior. HE exhibits a carrier whose structure
generates behavior that is **exact yet non-vanishing in `D_b`** (the ciphertext arithmetic is exact; the
noise metric is still nonzero). That premise-exposure is the D-5 sharpening, not a refutation of the whole
carrier program.

---

## 2. The crisp provable claim

> **Claim F28.** Let `σ: R = Z[x]/(x^n+1) → C^n` be the canonical embedding of a cyclotomic ring, and for
> ciphertexts `ct_i` with noise `e_i` define `d_σ(ct_1, ct_2) = ||σ(e_1) − σ(e_2)||_2`. Then:
>
> (i) **`d_σ` is a genuine Lawvere `[0,∞]` metric** — identity `d_σ(ct,ct)=0`, symmetry, and the triangle
> inequality `d_σ(a,c) ≤ d_σ(a,b) + d_σ(b,c)` all hold (they descend from the Euclidean norm on `C^n`
> because `σ` is a ring homomorphism, hence additive: `σ(e_a − e_c) = σ(e_a − e_b) + σ(e_b − e_c)`); and
>
> (ii) **`d_σ` is NON-VANISHING on the carrier** — for any fresh nontrivial ciphertext `||σ(e)|| > 0`, so
> the noise-to-reference distance `d_σ(ct, ct_clean)` is strictly positive on a system whose ciphertext
> arithmetic is exact; and
>
> (iii) **`d_σ` is MONOTONE in circuit multiplicative depth** — `||σ(e)||` grows (additively under `+`,
> multiplicatively under `×`) along any circuit, so `d_σ(ct_d, ct_clean)` is non-decreasing in depth `d`;
>
> **Therefore** the ciphertext system is an **on-carrier, structure-generates-behavior** system carrying a
> non-vanishing, monotone, provable Lawvere `D_b`. This is a **counter-instance to the unqualified §4.4/D-5
> assertion "`D_b` vanishes on the carrier"**: the assertion holds only under the unstated premise that the
> carrier's exact structure also yields *noise-free* behavior. F28 makes that premise explicit — **the
> sharpening of D-5.**

**Witnessable form.** (i) is a metric-axiom check over sampled ciphertext triples (compute `||σ(·)||`, verify
the triangle numerically at machine tolerance). (ii) is a strict-positivity check on fresh ciphertexts.
(iii) is a monotone numeric sweep of `||σ(e_d)||` vs depth. All three are SHA-stable numeric witnesses with
tolerance checks — the same discipline as the DC-motor / pendulum witnesses.

**Axis-A rigor caveat (per morphism-research-methodology).** The metric-axiom witness runs on a
**floating-point carrier** (`σ` maps into `C^n`; the norm is floating-point). Per the standing rule
(floating-point ⇒ NOT `proven`), (i) is **SME-adjudicated over sampled triples**, not `proven` — UNLESS the
run pushes the triangle inequality to a **closed-form proof** (it descends cleanly from `σ` additive + the
Euclidean triangle inequality, which is a genuine candidate for an Axis-A `proven` result, independent of
the numeric witness). **Flag both:** the closed-form metric proof (Axis-A high) is the more valuable target
than the numeric check; state which one the run claims.

---

## 3. Witness sketch (TOY scheme, teeth included)

A future run should NOT reach for a production library. Pure-Python toy is sufficient.

**Carrier — a small Ring-LWE / BFV-flavored scheme over `R = Z[x]/(x^n+1)`, small `n` (e.g. n=4 or 8).**
- Implement keygen / Enc / Dec with an **explicitly tracked** noise polynomial `e` per ciphertext (pure
  Python; NumPy for the FFT/roots-of-unity evaluation is acceptable).
- Implement `σ`: evaluate a ring element at the primitive `2n`-th roots of unity (an FFT / Vandermonde
  evaluation) to get its `C^n` image; `||σ(e)||_2` is the canonical-embedding noise norm.

**Witness steps:**
1. **Metric axioms (Claim i):** sample ciphertext triples `(a,b,c)`; compute `d_σ` pairwise; verify
   `d_σ(a,a)=0`, symmetry, and the **triangle inequality** at machine tolerance. Additionally, carry the
   **closed-form** argument (`σ` additive ⇒ triangle descends from Euclidean triangle) as the Axis-A target.
2. **Non-vanishing (Claim ii):** over many fresh ciphertexts, confirm `||σ(e)|| > 0` strictly (fresh noise
   is never zero) — the intrinsic, on-carrier non-vanishing.
3. **Monotonicity (Claim iii):** sweep multiplicative depth `d = 0,1,2,…`; record `||σ(e_d)||`; confirm
   non-decreasing (multiplicative blow-up under `×`, additive under `+`).

**Teeth (the load-bearing decoy) — a NON-METRIC noise functional that VIOLATES the triangle.**
Define a plausible-but-wrong "noise size" functional and show it is **not** a Lawvere metric, so the witness
can tell a genuine metric from a fake:
- **Candidate decoy:** the **coefficient-embedding `∞`-norm composed non-linearly**, e.g.
  `f(e) = ||e||_∞^2` (squared max-coefficient), or the **coefficient-vector norm WITHOUT the canonical
  embedding** used as if it were the geometric noise (the coefficient norm and canonical norm differ by the
  ring's condition number; treating the raw coefficient norm as the geometric distance mis-measures noise
  growth under `×`). Squaring breaks the triangle: `f(a,c) = ||e_a−e_c||^2 > ||e_a−e_b||^2 + ||e_b−e_c||^2`
  for a collinear triple — an explicit triangle **violation**. Exhibiting one such triple is the teeth: the
  witness distinguishes the true canonical-embedding metric (triangle holds) from a squared/mis-embedded
  functional (triangle fails). Without this, the witness would rubber-stamp any "noise number" as a metric.

**Teeth interpretation.** The decoy matters for the D-5 sharpening: it shows the counter-instance is a
metric BECAUSE of the canonical embedding's linearity, not a generic property of "any noise number." The
sharpened D-5 statement is thus precise — *the canonical-embedding norm* is the non-vanishing Lawvere `D_b`,
and a naive noise size is not even a metric.

**Cost profile.** Pure-Python + NumPy FFT; small `n`; single foreground session, no subagent fan-out,
no GPU, no external crypto dependency.

---

## 4. Prior art to cede ([PLACEHOLDER] — refverify before any manuscript)

The run **cedes** the canonical-embedding machinery and all HE constructions; the WySE contribution is only
what the non-vanishing metric says about the D-5 assertion. Do NOT invent DOIs.

```
[PLACEHOLDER: lyubashevsky2013ideal]
  Author: Lyubashevsky, V., Peikert, C., Regev, O.
  Title: On ideal lattices and learning with errors over rings
  Venue: EUROCRYPT 2010 / J. ACM 2013
  Year: 2013 (journal; 2010 conference)
  Note: THE canonical-embedding + Ring-LWE noise-analysis reference. The canonical embedding as the
        right geometry for noise, the "expansion factor," and noise growth under ring ops are THEIRS,
        not ours. This is the load-bearing cede for F28. DOI/venue/pages unverified.

[PLACEHOLDER: fan2012bfv]
  Author: Fan, J., Vercauteren, F.
  Title: Somewhat practical fully homomorphic encryption
  Year: 2012
  Note: BFV toy carrier. Venue/pages unverified.

[PLACEHOLDER: gentry2009fhe]
  Author: Gentry, C.
  Title: Fully homomorphic encryption using ideal lattices
  Venue: STOC 2009
  Year: 2009
  Note: Noise growth + bootstrapping context. DOI/pages unverified.

[PLACEHOLDER: cheon2017ckks]
  Author: Cheon, J.H., Kim, A., Kim, M., Song, Y.
  Title: Homomorphic encryption for arithmetic of approximate numbers
  Venue: ASIACRYPT 2017
  Year: 2017
  Note: CKKS leans hardest on the canonical embedding as the operative geometry — relevant if F28
        extends the metric to approximate arithmetic. DOI/pages unverified.
```

**What is ceded (be explicit):** (1) the canonical embedding and that noise should be measured under it —
Lyubashevsky-Peikert-Regev; (2) noise growth under homomorphic ops — every lattice-HE paper; (3) all HE
constructions. The run must NOT present any of these as WySE findings (R016). **NEW to WySE:** only that
this established norm is a Lawvere `D_b` counter-instance to §4.4/D-5.

---

## 5. The key value — this is a contribution to WySE's OWN D_b theory

**Not "HE is a homomorphism" (relabeling), and not F27's threshold-jump reading.** F28's entire value is
what it says about the library's asserted D-5 carrier claim:

- **It tests a REVISABLE assertion with a hard instance.** §4.4/D-5 flags "`D_b` vanishes on the carrier"
  as asserted-not-axiom and deliberately keeps `D_b` an optional slot "if the carrier bet fails." F28
  supplies a concrete, provable-metric system where an on-carrier `D_b` is **intrinsic and non-vanishing**,
  forcing the assertion to expose its unstated premise (structure generates *noise-free* behavior).

- **The delta lives in what it says about WySE, not about HE.** The HE facts are all ceded (Section 4). The
  contribution is a **sharpening of D-5**: replace the unqualified "`D_b` vanishes on the carrier" with a
  premise-explicit version, and register a **new `D_b` shape** for the library — an *intrinsic
  carrier-element metric* (the canonical-embedding norm), distinct from both the smooth fidelity-residual
  `D_b` of the fusion family and F27's threshold-jump `D_b`.

- **It connects to the metric-satisfaction bridge (F10) at the theory level.** The bridge is CLOSED and
  co-locates `(D_s, D_b)` as a `3/2`-institution with a Lawvere `[0,∞]`-enriched `D_b`. F28 supplies a
  clean, provable member of that enriched category — a case where `D_b` is a *bona fide* Lawvere metric with
  a closed-form triangle proof, useful as a worked instance underneath the bridge's abstract claim.

**Main risk (name it plainly): the escape clause swallows it.** If the run cannot defend sub-case (1) of
Section 1 (ciphertext ring as its own carrier), the assertion's "off-carrier fidelity" clause absorbs the
noise metric and F28 collapses into F27. **Guardrail:** the run must (a) commit up front to the
ciphertext-ring-as-own-carrier framing and argue it is non-degenerate (the ciphertext arithmetic is *exact*,
so the system genuinely generates its own behavior on the carrier, yet `D_b ≠ 0`), and (b) target the
**closed-form triangle proof** (Axis-A) so the contribution is a proved metric, not a numeric coincidence.
If neither carries, retire / fold into F27, do not ship.

---

## 6. Fable-shape verdict

**F28 is Fable-shaped, and unusually clean on the metric-axiom axis — but narrower and more theory-facing
than F27.**

1. **The metric is provable, not analogical.** The canonical-embedding norm is a Euclidean norm through a
   ring embedding; the metric axioms descend from a one-line argument (`σ` additive + Euclidean triangle).
   This is a genuine candidate for an Axis-A **`proven`** result (rare in this library, most witnesses being
   floating-point SME-adjudicated). That closed-form-proof availability is F28's distinctive strength.

2. **The contribution is a live theory-test, not a domain tour.** F28 attacks a specifically flagged
   revisable assertion (D-5) and would sharpen it — a direct contribution to WySE's `D_b` axiomatics, which
   is higher-value-per-word than adding another domain instance.

3. **Teeth are available and sharp** (the non-metric squared/mis-embedded decoy that violates the triangle),
   so the witness is not a rubber stamp.

**The delta versus F27 and versus the ceded HE literature (state it precisely):**
- NEW: (a) reading the canonical-embedding noise norm as an **intrinsic, non-vanishing, on-carrier Lawvere
  `D_b`** (distinct from F27's threshold-jump correctness `D_b`); (b) the **counter-instance / D-5
  sharpening** — exposing the unstated noise-free premise in "`D_b` vanishes on the carrier"; (c) a
  candidate **closed-form triangle proof** giving an Axis-A `proven` member of the metric-satisfaction
  bridge's enriched category.
- CEDED: the canonical embedding, noise geometry, all HE (Section 4).

**Main risk restated:** the on-carrier framing is contestable (Section 1 sub-case 1 vs 2). If the escape
clause wins, F28 is not distinct from F27. The run lives or dies on defending the ciphertext-ring-as-own-
carrier reading + landing the closed-form proof.

**Fable-worthy checklist:**
- Genuine delta: YES, concentrated in the D-5 sharpening + the closed-form metric. PASS.
- Finite witness: YES (metric-axiom check + monotone sweep + non-metric decoy; SHA-stable); PLUS a candidate
  closed-form Axis-A proof. PASS (strong).
- Isolable prior art: YES, cleanly ceded (Section 4, LPR13 load-bearing). PASS.
- RBW-hardenable: YES — the red leg's explicit charge is "the off-carrier fidelity clause swallows this"
  (sub-case 2). Never mark CLOSED on a 2-leg review.
- Goal-first: PASS — the objective is WySE's `D_b` theory (D-5), NOT explaining HE noise.
- Ripe: see Section 7.

---

## 7. Relation to F27 and F10; ripeness

**Relation to F27 (the modulus-ladder / (D_s,D_b)-plane redirect).** F27 reads HE on the **(D_s, D_b)
plane**: `D_s` = the PHE/SHE/FHE operation-preservation ladder, `D_b` = the **threshold-jump** correctness
margin, bootstrapping = a `D_b`-reset endomorphism. F28 keeps ONLY the `D_b` axis and sharpens it: the same
noise, read not as a correctness threshold but as an **intrinsic canonical-embedding geometric metric**, and
aimed not at the `(D_s,D_b)` reading but at the **D-5 carrier assertion**. **Split rationale:** F27's `D_b`
is a fidelity residual (compatible with §4.4's off-carrier clause); F28's `D_b` is an *on-carrier intrinsic
metric* that challenges the clause. Keeping them separate stops F27's broad `(D_s,D_b)` scope from muddying
F28's single sharp claim. F28 can share F27's toy Ring-LWE carrier (Carrier B) but adds the `σ` evaluation
and the metric-axiom witness. **If sub-case (2) wins, F28 folds back into F27.**

**Relation to F10 (D_b as a Lawvere-enriched category / the metric-satisfaction bridge).** F10 established
`D_b` as a Lawvere `[0,∞]`-enriched behavioral distance inside the CLOSED metric-satisfaction bridge
(`3/2`-institution co-locating `(D_s,D_b)`). F28 is a **concrete, provable member** of that enriched
category — a case with a closed-form triangle proof — and it stress-tests one asserted boundary condition
(D-5) of the same bridge. F28 is downstream of F10's abstraction: it does not rebuild the enrichment, it
populates it with a hard instance and probes an assumption.

**Ripeness — ripe to run as a Tier-2 candidate, with one framing precondition.**
- **Machinery readiness: YES.** `D_b` (Lawvere) machinery exists (F10/bridge CLOSED). Witness is pure-Python
  + NumPy FFT, cheap, no fan-out, no GPU, no external crypto dependency.
- **The real precondition (framing, not tooling): commit up front to the ciphertext-ring-as-own-carrier
  reading (Section 1 sub-case 1) and argue it is non-degenerate.** Without that decision the run risks the
  escape clause collapsing F28 into F27. Second sub-precondition: **decide whether the target is the
  closed-form triangle proof (Axis-A `proven`) or the numeric metric-axiom witness (SME-adjudicated)** —
  prefer the former; it is F28's distinctive value.
- **Reference debt: NOT blocking the run, blocking the manuscript.** Section 4 all [PLACEHOLDER]; a Tier-1
  manuscript needs lyubashevsky2013ideal (load-bearing) + fan2012bfv promoted via refverify before render
  (R019/R109).
- **Recommended run shape:** single foreground session sharing F27's Carrier B; add `σ` evaluation; run the
  three metric witnesses + the non-metric decoy; attempt the closed-form triangle proof; RBW-harden with a
  LIVE cross-vendor red leg charged with the "off-carrier fidelity clause swallows this" objection.

**Verdict:** ripe, cheap, and cleaner-than-F27 on the metric axis (a candidate Axis-A `proven` result), but
**narrower and framing-contingent** — its whole bite depends on defending the on-carrier reading against the
§4.4 escape clause. Best run AFTER or alongside F27 (shared carrier), kept as a separate, single-claim entry.

---

*Document status: R016 (a) research artifact / hunch. Scoping note only — not derived, not witnessed, not
run. Tests a REVISABLE asserted claim (D-5); no assertion here is itself established. All references
[PLACEHOLDER], none in approved.bib. Provenance: Opus 4.8 (claude-opus-4-8[1m]), Anthropic, Claude Code CLI,
principal-directed, 2026-07-16.*
