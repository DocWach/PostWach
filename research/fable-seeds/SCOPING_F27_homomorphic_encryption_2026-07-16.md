# SCOPING NOTE — F27: Homomorphic Encryption on the (D_s, D_b) Plane

**STATUS:** scoping note ONLY. Integration status **(a) research artifact / hunch** throughout (R016).
Nothing here is derived, witnessed, or run; execution is reserved for a distinct session. This note
scopes the seed to the point where a future session can run it. Do NOT read any claim below as
established — everything is CANDIDATE / OPEN.

**PROVENANCE (R018):** authored by Opus 4.8 (claude-opus-4-8[1m]), vendor Anthropic, access mode
Claude Code CLI, principal-directed research subagent, 2026-07-16. Sources read-only; the only repo
mutation is this file.

**FRAME:** WySE = Wymorian systems theory. A system z = (SZ, IZ, OZ, NZ, RZ) carries a signature Σ
and a behavior (trajectory set). A homomorphism h: z_A -> z_B is a signature morphism plus a
state/carrier map making the structure- and behavior-preservation diagrams commute. Each candidate
morphism carries **D_s** (degree of structural homomorphism — how much of the algebraic structure is
preserved, the record (K1, K2, K3)) and **D_b** (a Lawvere [0,∞]-enriched behavioral distance — how
far the behavior diverges). Bridge pattern **candidate E**: an established technique instantiates the
underlying morphism structure; the run either proves the correspondence or proves failure off a
restriction.

**R019 NOTE:** every bibliographic entry below is [PLACEHOLDER] and is NOT in the approved-references
store. None may be cited in a manuscript until it passes the Byzantine-Bayesian protocol (refverify).
DOIs are deliberately NOT drafted (no hallucinated identifiers).

---

## 0. The hook (why this is a seed at all)

Homomorphic encryption (HE) is **literally an algebraic homomorphism**: an HE scheme provides an
encryption map Enc such that for a supported operation `op`,

```
    Dec( Enc(a)  op*  Enc(b) )  =  a  op  b
```

where `op*` is the corresponding ciphertext-space operation. This is the definition of a
(ring / group) homomorphism between a plaintext algebra and a ciphertext algebra — it is not a WySE
invention and must be ceded as definitional prior art (Section 4).

The WySE **delta is not inventing HE**; it is **READING HE in the (D_s, D_b) frame** and observing
that two quantities the HE literature already tracks are exactly D_s and D_b of one WySE object:

- **D_s = which operations are preserved.** The homomorphism is partial: it graduates
  partially-homomorphic (PHE, only `+` OR only `×`) -> somewhat/leveled (SHE/LHE, all operations but
  bounded multiplicative depth) -> fully homomorphic (FHE, all operations, unbounded). This is a
  monotone ladder of *how much of the plaintext ring structure the ciphertext map preserves* — a
  structural-homomorphism degree.
- **D_b = noise growth.** In lattice-based schemes each ciphertext carries a noise term that grows
  with each homomorphic operation; when noise exceeds a threshold, decryption fails. Noise-vs-depth is
  a genuine **behavioral defect** measured against operation depth — a [0,∞]-valued behavioral
  divergence that is 0 while decryption is still correct and diverges (or jumps to ∞ = "wrong plaintext")
  past the noise ceiling.
- **Bootstrapping = a morphism-REPAIR operation.** Gentry's bootstrapping homomorphically evaluates the
  decryption circuit to produce a fresh low-noise ciphertext of the same plaintext — a **noise reset**.
  In WySE terms it is an endomorphism-repair that resets D_b to (near) its floor without changing D_s,
  which is exactly what turns a leveled scheme (bounded depth) into a fully homomorphic one (unbounded).

One WySE object captures **both** the somewhat-vs-fully distinction (its D_s ladder) **and** the
correctness margin (its D_b-vs-depth profile), with bootstrapping as the operation that manipulates D_b.

---

## 1. The precise WySE carrier

Cast HE as a graded homomorphism between two WySE systems.

**Plaintext system z_P.** The system whose "behavior" is arithmetic over a plaintext algebra.
- Carrier / state SZ_P: the plaintext ring elements (e.g. Z_t for BGV/BFV, or the message space Z_N for
  Paillier's additive group).
- Structure: the ring operations (+, ×) — or, for PHE, the single supported group operation.
- IZ_P / OZ_P: operands in, result out.
- NZ_P / RZ_P: applying an arithmetic-circuit gate is a next-state step; the readout is the plaintext value.
- A **circuit** C over z_P is a WySE trajectory: a sequence of gate applications. z_P's behavior is
  exact arithmetic (no noise, no failure).

**Ciphertext system z_C.** The system whose behavior is homomorphic evaluation over ciphertexts.
- Carrier / state SZ_C: ciphertexts (lattice elements), each carrying a hidden **noise** component e.
- Structure: the ciphertext operations `op*` (ciphertext add, ciphertext multiply, and, in leveled
  schemes, key-switching / modulus-switching / relinearization as bookkeeping steps).
- NZ_C: applying a ciphertext gate — which also **transforms the noise** (add: noise adds; multiply:
  noise multiplies/blows up).
- RZ_C: Dec (decryption). RZ_C is **correct only while noise < threshold**; past threshold, RZ_C returns
  the wrong plaintext.

**The morphism h: z_P -> z_C (via Enc, with Dec as the section).**
- Enc is the carrier map; Dec ∘ Enc = id on plaintexts (a retraction), so structurally Enc embeds z_P
  into z_C.
- **D_s(h) = the operation-preservation record.** h preserves gate g iff `Dec(Enc(a) g* Enc(b)) = a g b`
  for all a, b. The set of preserved gates is the structural record:
  - PHE: D_s preserves exactly one of {+, ×} (a single-operation subgroup homomorphism).
  - SHE / leveled: D_s preserves {+, ×} but only up to a bounded multiplicative depth L (a bounded-degree
    ring homomorphism — preserves the ring structure on the sub-algebra of circuits of depth ≤ L).
  - FHE: D_s preserves {+, ×} on all circuits (full ring homomorphism).
  So D_s is *graded by which/how-much of the plaintext ring structure survives* — the WySE structural
  degree, read as (K1 = sorts/carrier map Enc, K2 = which operations commute, K3 = the depth bound L).
- **D_b(h) at circuit C = the noise-induced behavioral divergence.** Define
  D_b(h; C) = Lawvere distance between the readout of z_C after evaluating C homomorphically and the
  readout of z_P after evaluating C. While noise(C) < threshold, Dec is correct and D_b = 0; at the
  first depth where noise(C) ≥ threshold, D_b jumps to a positive value (or to ∞, "decryption fails").
  Noise grows monotonically along the circuit (add: additively; multiply: multiplicatively), so D_b is
  monotone non-decreasing in circuit depth up to the ceiling.
- **Bootstrapping = a repair endomorphism r: z_C -> z_C** with Dec ∘ r = Dec (semantics-preserving) and
  noise(r(ct)) ≈ floor (resets the behavioral margin). r changes D_b (resets it) without changing D_s
  (the preserved-operation set is unchanged); iterating r is what lifts D_s's depth bound L from finite
  (leveled) to unbounded (FHE).

**Summary of role assignments:**

| WySE role | HE object |
|-----------|-----------|
| plaintext system z_P | the plaintext ring (Z_t / Z_N) with exact +, × |
| ciphertext system z_C | ciphertexts (lattice elements) with noisy op*, threshold-gated Dec |
| morphism h | Enc (carrier map), with Dec as retraction |
| **D_s(h)** | the operation-preservation record: {+} or {×} (PHE) ⊂ {+,× up to depth L} (SHE) ⊂ {+,×} (FHE) |
| **D_b(h; C)** | noise-vs-depth: 0 while Dec correct, jumps past the noise ceiling |
| bootstrapping | repair endomorphism r resetting D_b; lifts D_s's depth bound to ∞ |

---

## 2. The crisp provable claim

The theorem a Fable run would target, stated witnessably:

> **Claim F27.** For a WySE homomorphism h = Enc: z_P -> z_C of a homomorphic-encryption scheme,
> (i) **D_s graduates the HE hierarchy exactly**: the operation-preservation record D_s(h) is a
> partial order in which PHE (single operation) ⊏ SHE/leveled (both operations, bounded depth L) ⊏
> FHE (both operations, unbounded), and this order is *strict and exhaustive* — every scheme sits at
> exactly one rung, determined by its preserved-operation record; and
> (ii) **D_b is monotone non-decreasing in circuit multiplicative depth**: for a fixed scheme,
> D_b(h; C) = 0 for all circuits C of depth ≤ L (the leveled bound) and becomes positive (decryption
> incorrect) for some circuit of depth L+1; and
> (iii) **bootstrapping is a D_b-reset that preserves D_s**: there is an endomorphism r on z_C with
> Dec ∘ r = Dec and D_b(h; r(·)) reset to the noise floor, and *iterating r removes the depth bound in
> (ii)* — i.e., the composite scheme (base leveled scheme + bootstrapping) attains the FHE rung of the
> D_s order in (i).

Witnessable form: (i) is a finite-enumeration check over a fixed set of gates on a concrete toy scheme
(does `Dec(Enc(a) op* Enc(b)) = a op b` hold for op ∈ {+, ×}, over sampled a, b?); (ii) is a monotone
numeric sweep of a measured noise magnitude and a correctness indicator against depth, with a
**teeth** point where correctness flips at L+1; (iii) is a check that a repair step restores correctness
at a depth that failed without it. All three are SHA-stable numeric/enumeration witnesses with a
tolerance/threshold check, exactly the shape of the data-fusion FC-family witnesses.

**Scoping caveat (Axis-A rigor, per morphism-research-methodology).** As with every floating-/
finite-carrier WySE witness, F27 will be **SME-adjudicated over sampled inputs**, not `proven`: the
`Dec(Enc(a) op Enc(b)) = a op b` check is over a sampled finite subset of plaintexts, not a closed-form
proof of the scheme's homomorphic identity (that identity is the ceded prior art — see Section 4). The
NEW, witnessable object is the **(D_s, D_b) reading**, not the correctness of HE.

---

## 3. Witness sketch (TOY scheme, teeth included)

A future run should NOT reach for a production library. Two toy carriers, cheap and self-verifying:

**Carrier A — Paillier (additive PHE), for D_s = {+} only and the teeth against multiplicativity.**
- Implement textbook Paillier keygen / Enc / Dec in pure Python (integers, `pow`, modular inverse; no
  external crypto lib needed for a toy).
- Verify the **additive** homomorphism: `Dec(Enc(a) * Enc(b) mod n^2) = (a + b) mod n` over sampled a, b.
  (Paillier's ciphertext-multiply realizes plaintext-add.)
- **Teeth 1 (D_s ladder):** show there is **no** ciphertext operation realizing plaintext multiply for
  Paillier — Paillier occupies the PHE rung with D_s = {+} only. The decoy is "treat Paillier as SHE":
  attempt a ×-witness and show it fails, pinning Paillier strictly below the SHE rung.
- D_b for Paillier is trivially 0 (no noise; RSA-style modular arithmetic is exact) — this is the
  **contrast carrier** that isolates the D_s ladder from the D_b/noise axis. Useful precisely because it
  shows a scheme where D_s < full but D_b ≡ 0.

**Carrier B — a small BGV/BFV-like leveled scheme (or a toy "approximate-GCD" / DGHV-style integer
scheme), for the D_b noise-vs-depth profile, the correctness ceiling, and the bootstrapping reset.**
- Implement a minimal ring-LWE-flavored (or integer DGHV-flavored) leveled scheme with a **small,
  explicitly tracked noise term** and a modest modulus, sized so that the noise ceiling is reachable in a
  handful of multiplications (the point is to *hit* the failure, not to be secure).
- Verify both `+` and `×` homomorphisms at depth 0–1 (D_s = {+, ×} up to L).
- **Measure D_b:** sweep circuit multiplicative depth d = 0, 1, 2, ...; at each depth record (a) the
  measured noise magnitude and (b) a correctness indicator `Dec(eval) == plaintext-eval`. Expect D_b = 0
  (correct) up to depth L, then D_b > 0 (incorrect) at L+1.
- **Teeth 2 (D_b monotonicity + ceiling):** the correctness indicator MUST flip from 1 to 0 at a
  specific depth L+1, and noise MUST be monotone non-decreasing — a scheme/parameterization where
  correctness *did not* fail (ceiling never reached) would be a null witness; the run must pick
  parameters that make the ceiling bite.
- **Teeth 3 (bootstrapping reset):** insert a noise-reset step (for a toy, a modulus-switch / re-encrypt
  proxy standing in for full bootstrapping) before depth L+1 and show the circuit that *failed* now
  *succeeds*, with measured noise dropped back toward the floor and D_s unchanged. This is the
  morphism-REPAIR witness. (A faithful bootstrapping — homomorphically evaluating Dec — is heavy; the
  run should scope this as a **modulus-switch/re-encrypt proxy** and flag that the full-bootstrap
  version is a follow-on, R016 (a).)

**Overall teeth (the non-homomorphic decoy).** Include at least one map that is **NOT** a homomorphism
— e.g., a deterministic block cipher's Enc, or a naive "encrypt each digit" scheme — and show
`Dec(Enc(a) op* Enc(b)) ≠ a op b`: D_s = ∅ (no operation preserved). This proves the witness has teeth
(it can tell a homomorphism from a non-homomorphism) rather than rubber-stamping any Enc.

**Cost profile.** Pure-Python integer arithmetic; both carriers are small. Estimated a single
foreground session with no subagent fan-out; no GPU, no external crypto dependency for the toy scale.

---

## 4. Prior art to cede ([PLACEHOLDER] — refverify before any manuscript)

The run **cedes** essentially all of the mathematics; the WySE contribution is only the (D_s, D_b)
reading. Do NOT invent DOIs; the entries below are candidate metadata from prior knowledge only.

```
[PLACEHOLDER: gentry2009fhe]
  Author: Gentry, C.
  Title: Fully homomorphic encryption using ideal lattices
  Venue: STOC 2009 (ACM Symposium on Theory of Computing)
  Year: 2009
  Note: First FHE scheme + bootstrapping. Bootstrapping-as-noise-reset is Gentry's, not ours.
        DOI/pages unverified.

[PLACEHOLDER: paillier1999public]
  Author: Paillier, P.
  Title: Public-key cryptosystems based on composite degree residuosity classes
  Venue: EUROCRYPT 1999
  Year: 1999
  Note: Additive PHE toy carrier A. DOI/pages unverified.

[PLACEHOLDER: rivest1978homomorphisms]
  Author: Rivest, R.L., Adleman, L., Dertouzos, M.L.
  Title: On data banks and privacy homomorphisms
  Year: 1978
  Note: Original "privacy homomorphism" framing — HE-as-homomorphism is DEFINITIONAL and predates us
        by decades. This is the load-bearing cede: the homomorphism reading is not novel.
        Venue/pages unverified.

[PLACEHOLDER: brakerski2014bgv]
  Author: Brakerski, Z., Gentry, C., Vaikuntanathan, V.
  Title: (Leveled) fully homomorphic encryption without bootstrapping
  Venue: ACM TOCT / ITCS 2012
  Year: 2012/2014
  Note: BGV leveled scheme; "leveled" = the bounded-depth D_s rung. DOI/venue/year unverified.

[PLACEHOLDER: fan2012bfv]
  Author: Fan, J., Vercauteren, F.
  Title: Somewhat practical fully homomorphic encryption
  Year: 2012
  Note: BFV scheme (toy carrier B family). Venue/pages unverified.

[PLACEHOLDER: cheon2017ckks]
  Author: Cheon, J.H., Kim, A., Kim, M., Song, Y.
  Title: Homomorphic encryption for arithmetic of approximate numbers
  Venue: ASIACRYPT 2017
  Year: 2017
  Note: CKKS (approximate/real HE) — relevant if the run extends D_b to an approximate-arithmetic
        Lawvere distance. DOI/pages unverified.

[PLACEHOLDER: vandijk2010dghv]
  Author: van Dijk, M., Gentry, C., Halevi, S., Vaikuntanathan, V.
  Title: Fully homomorphic encryption over the integers
  Venue: EUROCRYPT 2010
  Year: 2010
  Note: DGHV integer scheme — candidate toy carrier B (approximate-GCD, easiest to implement in
        pure-Python integers). DOI/pages unverified.
```

**What is ceded (be explicit):** (1) HE-is-a-homomorphism — definitional, Rivest-Adleman-Dertouzos 1978;
(2) the PHE/SHE/FHE taxonomy — standard cryptographic vocabulary; (3) noise growth and the correctness
threshold — every lattice-HE paper; (4) bootstrapping-as-noise-reset — Gentry 2009. The run must NOT
present any of these as WySE findings (R016).

---

## 5. Dependencies and ties

- **The morphism library / D_s (structural degree) machinery.** F27 reuses the structural record
  (K1, K2, K3) as the *operation-preservation record*. Tie: `morphism-domain-reference` for the D_s
  record definition; the Lemma CODY-IND granular-record result (2026-07-12 trunk) is the closest kin —
  F27's D_s is another instance of "a granular record separates what a scalar rung label conflates"
  (PHE/SHE/FHE is a coarse scalar; the preserved-operation record is the granular object).
- **The D_b (Lawvere [0,∞]-enriched behavioral distance) machinery.** F27's noise-vs-depth profile is a
  D_b instance where the interesting structure is a *threshold jump* (0 -> positive at the ceiling),
  distinct from the smooth D_b of the fusion family. Tie: the metric-satisfaction bridge
  (`research/MetricSatisfaction_Bridge_candidate.md`) for the orthogonal (D_s, D_b) decomposition — F27
  is a clean case where D_s (which ops) and D_b (noise margin) are manifestly *independent* axes
  (Paillier: D_s < full, D_b ≡ 0; leveled scheme: D_s = full-up-to-L, D_b climbs).
- **Bootstrapping as repair** has no current sibling in the library — this is F27's most novel structural
  contribution (a D_b-reset endomorphism that lifts a D_s depth bound). Candidate GAP/new-machinery note.
- **+probability / approximate thread (F7/F8, Giry).** Only if the run extends to CKKS (approximate
  arithmetic), where D_b becomes a genuine real-valued approximation error rather than a binary
  correct/fail — links the Lawvere-metric D_b to the approximate-morphism family. Scope this as a
  follow-on, not the base run.
- **No new external tooling.** Pure-Python integer arithmetic; no approved.bib entries yet (Section 4 all
  [PLACEHOLDER]); a Tier-1 run needs at least gentry2009fhe + paillier1999public + rivest1978homomorphisms
  promoted before any manuscript.

---

## 6. Fable-shape verdict

**F27 is likely the MORE directly Fable-shaped of the two seeds.** Why:

1. **The homomorphism is not analogical — it is the literal object.** Unlike most library candidates
   where "system X is *like* a homomorphism," HE *is* a ring/group homomorphism by construction
   (Rivest 1978). There is no bridging argument to defend; the (D_s, D_b) reading attaches to an object
   already known to be a homomorphism. That removes the single most common failure mode of a Fable run
   (the correspondence itself being contested).

2. **Both degrees are pre-quantified by the domain.** D_s (which operations preserved) and D_b (noise
   margin) are quantities the HE literature *already measures independently*. The run does not have to
   invent the metrics; it has to *identify* them with D_s and D_b and show the identification is faithful.
   Finite-enumeration + monotone-sweep witnesses, both cheap.

3. **Clean teeth are available and unavoidable.** A non-homomorphic decoy (block cipher) gives D_s = ∅;
   a depth-L+1 circuit gives the D_b ceiling; Paillier-as-SHE fails the ×-witness. The witness can
   distinguish, so it is not a rubber stamp.

4. **The bootstrapping-as-repair reading is genuinely new machinery**, not just a relabel (see the delta
   analysis below).

**The delta versus the ceded HE literature (state it precisely).** NEW in the WySE reading, none of it
claiming credit for HE itself:
- (a) **Identifying the PHE/SHE/FHE taxonomy with a D_s partial order** — reading a crypto taxonomy as a
  *structural-homomorphism-degree order*, connecting it to the library's D_s record (K1,K2,K3) and to
  Lemma CODY-IND (granular record vs scalar rung).
- (b) **Reading noise-vs-depth as a Lawvere [0,∞]-enriched D_b with a threshold jump** — placing the
  correctness margin on the same behavioral-distance axis the library uses for fusion / lumping,
  exhibiting a *threshold-jump* D_b (a new D_b shape for the library).
- (c) **Bootstrapping as a D_b-reset endomorphism that lifts a D_s depth bound** — the structurally
  richest piece: a repair operation that moves along the D_b axis without moving along D_s, and whose
  iteration changes the D_s rung (leveled -> FHE). No current library entry has a "repair endomorphism"
  of this kind.
- (d) **The manifest orthogonality demonstration**: Paillier (D_s partial, D_b ≡ 0) vs leveled scheme
  (D_s full-to-L, D_b climbing) is a crisp two-point demonstration that D_s and D_b are independent axes
  — a clean witness for the orthogonal-decomposition claim the metric-satisfaction bridge asserts.

**Main risk (name it plainly): "just relabeling known HE facts."** The failure mode is that (a) and (b)
reduce to *renaming* the crypto taxonomy and the noise budget in WySE vocabulary with no new theorem.
Guardrails for the run:
- The run must make the D_s/D_b reading **do work the crypto framing does not already do** — the load
  bearer is (c) and (d): the bootstrapping-repair-endomorphism and the orthogonality demonstration are
  the parts that are *not* a relabel, because the library gains a new morphism-repair primitive and a
  clean two-axis-independence witness. If the run cannot make (c)/(d) carry, it is relabeling and should
  be retired, not shipped.
- Cede (a)/(b) explicitly as *readings* (R016), and target the theorem at the *composite* statement
  F27(iii): base-leveled + bootstrapping attains the FHE D_s rung — that composite is a WySE statement
  about how a D_b-repair moves a scheme along the D_s order, which is not a bare HE fact.
- Watch **goal-first**: the objective is the library's (D_s, D_b) machinery earning a new domain and a
  new repair primitive, NOT explaining HE. If the run drifts into "here is how FHE works," it has lost
  the thread.

**Fable-worthy checklist (against the standing criteria):**
- Genuine delta: YES, but concentrated in (c)/(d); (a)/(b) are readings. Conditional PASS.
- Finite witness: YES (enumeration + monotone sweep + repair check, SHA-stable). PASS.
- Isolable prior art: YES, cleanly ceded (Section 4). PASS.
- RBW-hardenable: YES (a cross-vendor red leg can attack the "just relabeling" risk directly — the
  standing lesson: never mark CLOSED on a 2-leg review; the red leg's job here is to argue relabel).
- Goal-first: PASS with the guardrail above.
- Ripe: see Section 7.

---

## 7. Is it ripe to run now?

**Ripe to run as a Tier-1/2 candidate — with two light preconditions, neither blocking scoping.**

- **Machinery readiness: YES.** D_s (record) and D_b (Lawvere distance) machinery exist and are exercised
  (fusion family, the record-separation trunk). The witness is pure-Python integer arithmetic, cheap, no
  subagent fan-out, no GPU, no external crypto dependency at toy scale. The pendulum/DC-motor witness
  discipline transfers directly.
- **Reference debt: NOT blocking the run, blocking the manuscript.** Section 4 is all [PLACEHOLDER]. A
  Tier-1 manuscript needs gentry2009fhe + paillier1999public + rivest1978homomorphisms (and, if used,
  the leveled-scheme refs) promoted via refverify BEFORE any render (R019/R109). The *derivation and
  witness* can run without them; the *write-up* cannot render until they are approved.
- **Scope discipline (the real precondition): decide the bootstrapping fidelity up front.** Full
  bootstrapping (homomorphically evaluating Dec) is heavy; the run should commit to the **modulus-switch /
  re-encrypt proxy** for teeth 3 and declare the full-bootstrap version a follow-on R016 (a). Without
  that decision the run risks over-scoping into a real FHE implementation, which is off-thread.
- **Recommended run shape:** single foreground session. Carrier A (Paillier, ~1 short witness: additive
  homomorphism + the ×-decoy teeth) then Carrier B (leveled/DGHV toy: +/× homomorphism, noise-vs-depth
  sweep with the correctness ceiling, and the re-encrypt-proxy repair). RBW-harden with a LIVE cross-
  vendor red leg whose explicit charge is the "just relabeling known HE facts" objection — if the red leg
  cannot be answered by (c)/(d), retire rather than ship.

**Verdict:** ripe, cheap, and the most directly Fable-shaped of the two seeds — provided the run keeps
the delta on the bootstrapping-repair endomorphism (c) and the two-axis-orthogonality demonstration (d),
and cedes the HE-is-a-homomorphism reading (a)/(b) as prior art.

---

*Document status: R016 (a) research artifact / hunch. Scoping note only — not derived, not witnessed,
not run. All references [PLACEHOLDER], none in approved.bib. Provenance: Opus 4.8 (claude-opus-4-8[1m]),
Anthropic, Claude Code CLI, principal-directed, 2026-07-16.*
