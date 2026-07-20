# SCOPING NOTE — F26: Neuromorphic Computing as a DEVS Homomorphism

**STATUS:** scoping seed, integration status **(a) research artifact / hunch** throughout (R016). This is
NOT a run. No derivation, no witness, no D_s or D_b is computed here; the note only shapes a future
dedicated session to the point where it can run F26. Every claim below is a hunch until a self-verifying
witness measures it.

**PROVENANCE (R018):** scoping by Opus 4.8 (claude-opus-4-8[1m]), Anthropic, Claude Code CLI,
principal-directed, 2026-07-16. Method: morphism-research-frontier discipline (Fable-shape verdict) +
wyse-model-generation framing (carrier = the quintuple; witness with teeth/decoy).

**FAMILY:** sibling of the data-fusion Fable family (F18–F25, `research/data-fusion-inventory/`). Ties out
to **F24** (Kennedy–O'Hagan coupling as readout comorphism), **candidate E** (Cody 2021 transfer distance),
and the **biomimetics-analyst** skill.

---

## The hook (folklore to cede)

**Spikes are events.** A spiking neural network (SNN) advances by discrete, timestamped spike events, which
is exactly what a Discrete Event System Specification (DEVS) formalizes. This makes "SNNs are event systems"
the ceded *folklore* — it is already known and used (event-driven SNN simulators exploit it). The Fable is
NOT that observation. The Fable is the measured statement: **a neuromorphic (spiking / event-driven /
analog) realization of a named target computation is a DEVS/WySE homomorphism with a measurable structural
degree D_s and a measurable behavioral distance D_b, and the energy–accuracy tradeoff is a curve on the
(D_s, D_b) plane.**

---

## 1. The WySE carrier (what must be pinned before any run)

The carrier is the single most under-determined thing here, and pinning it is the pre-run gate (Section 7).
The candidate carrier:

**Target computation `Z*` (the reference).** A named function realized as a WySE quintuple
`z* = (SZ*, IZ*, OZ*, NZ*, RZ*)` at a chosen stratification level (LO / LF / LA / LC). For a first run the
target should be a small, exactly-specified function whose ground truth is externally known (not a
learned/trained network — a *specified* computation, per the STRONG-grounding fence of
wyse-model-generation). Candidates: a leaky-integrate-and-fire (LIF) neuron realizing a *thresholded
temporal coincidence* (2-input AND-in-time), or a small SNN realizing a fixed linear filter / a rate-coded
adder.

**Neuromorphic realization `Z_snn` (the DEVS carrier).** The load-bearing decision: **is the SNN an ATOMIC
DEVS or a COUPLED DEVS?**
- A **single spiking neuron** (LIF) is naturally an **atomic DEVS**: the membrane potential is the
  continuous state `SZ` between events; the internal transition `NZ_int` fires a spike and resets when the
  potential crosses threshold (time-advance = time-to-threshold under the sub-threshold ODE); the external
  transition `NZ_ext` integrates arriving input spikes; `RZ` emits the output spike. This is the DEVS
  "quantized integrator" pattern — the sub-threshold dynamics are a continuous ODE wrapped by an
  event-driven threshold crossing. Level: LA (analog membrane) or LC if the neuron is itself decomposed.
- A **network of neurons** is a **coupled DEVS**: each neuron is an atomic-DEVS component; synapses are the
  DEVS couplings (output-port spike → input-port spike, with a synaptic weight and delay on the coupling).
  The network's I/O behavior is the closure-under-coupling of the atomic components. Level: LC (coupled).

**Signatures.** `IZ` = spike-event ports (input spike trains, each an event stream over an alphabet of
neuron indices or a real-valued current); `OZ` = output spike train(s) / decoded readout; the *behavior* is
the timed output event trajectory (a piecewise-constant / point-process signal on `[0,T]`).

**The two channels the run measures.**
- **D_s (structural):** the Wach–Salado degree-of-homomorphism of the map `h: Z_snn → Z*` (or the reduct
  the other way) — how much of the target's state/transition structure the SNN realization preserves. For an
  exact rate-coded realization D_s should be high; for an aggressive low-power (few-spike) realization D_s
  degrades.
- **D_b (behavioral):** a Lawvere `[0,∞]`-enriched distance on the timed output. Natural instantiation: a
  **spike-train / point-process metric** (van Rossum distance or Victor–Purpura spike-distance) between the
  SNN output train and the target's reference output, OR output decoding error (rate/latency-decoded value
  vs. the true function value). This is the neuromorphic analogue of the trajectory-error D_b used in the
  pendulum witness.

---

## 2. The crisp provable claim (what a Fable run would target)

Stated so a witness can forbid a mismatch:

> **F26 claim.** Let `Z*` be a named target computation as a WySE quintuple at level L, and let `Z_snn` be a
> spiking realization built as a (coupled) DEVS whose atomic components are LIF-DEVS neurons under a fixed
> encoding/decoding pair `(enc, dec)`. Then the map `h: Z_snn → Z*` induced by `dec ∘ (·) ∘ enc` is a WySE
> homomorphism with a measurable degree `D_s(Z_snn, Z*)` and a behavioral distance
> `D_b(Z_snn, Z*) = ρ(dec(out_snn), out_*)` (ρ a fixed spike-train / decoding metric). Moreover, as a
> spike-budget / energy parameter `E` (spike count, or threshold/refractory setting) is swept, the pair
> `(D_s, D_b)` traces a monotone-in-the-loose-sense frontier on the degree plane: **reducing the spike
> budget cannot decrease both D_s and D_b** (a no-free-lunch / Pareto statement).

The **minimal, most-witnessable version** to run first is the single-neuron version (drop the network):
*a LIF-DEVS neuron realizing a thresholded temporal-coincidence function is an atomic-DEVS homomorphism of
the target with D_b = 0 in the exact-encoding regime and D_b > 0 (bounded by encoding quantization) in the
low-spike regime.* The frontier claim is the stretch goal; the homomorphism-with-measured-(D_s, D_b) claim
is the floor.

---

## 3. Witness sketch (small, concrete, with teeth and a decoy)

**Target.** A 2-input temporal-AND (coincidence detector): output fires iff two input spikes arrive within
a window `Δ`. Ground truth is externally known (the truth table over spike-timing offsets), so the witness
measures transcription against an external reference, not integrator self-consistency (revelation 3 of
wyse-model-generation).

**SNN realization `Z_snn`.** One LIF-DEVS neuron: sub-threshold leak τ, threshold θ set so a *single* input
spike is sub-threshold but two within Δ cross θ. Encode the two logical inputs as spike times; decode
"output = 1" as "the neuron emitted a spike in `[0,T]`."

**What is measured.**
- **D_s:** degree-of-homomorphism of the LIF-DEVS → coincidence-function map (state = membrane potential
  collapses onto the boolean coincidence state; how faithfully the reset/threshold structure realizes the
  target's transition).
- **D_b:** spike-train distance (Victor–Purpura or van Rossum) between the neuron's output train and the
  target's reference output train across a sweep of input-timing offsets; and a rate/latency decode error.

**The teeth (a witness that cannot fail measures nothing).** Sweep the coincidence window: for offsets
`> Δ` the neuron MUST stay silent; for offsets `< Δ` it MUST fire. Assert both. Assert D_b = 0 (up to the
metric's timing tolerance) in the exact regime and assert D_b grows as θ is raised toward the low-spike
regime.

**The decoy (the linearization-shortcut analogue).** Include a **non-leaky integrator** decoy (τ → ∞, a
perfect accumulator) that *sums* the two inputs regardless of timing. It realizes logical-OR-ish /
rate-sum behavior, NOT temporal coincidence. Assert the decoy FAILS the coincidence truth table (fires on
widely separated inputs where the true LIF stays silent). This is the direct analogue of the pendulum's
linear-decoy: it proves the witness discriminates a genuine event-timing homomorphism from a
timing-blind accumulator. Without the leak (the DEVS time-advance), the map is not a homomorphism of the
*temporal* target — that is the finding the decoy protects.

**Carrier honesty (from the DC-motor/pendulum runs).** The sub-threshold membrane ODE is a
continuous/floating-point carrier, so the honest rigor ceiling is **SME-adjudicated**, not `proven`
(revelation 2). `proven` would require an exact-arithmetic / event-time-symbolic carrier — a candidate
witness upgrade, plausibly *easier* here than for the pendulum because the DEVS event times can be solved
in closed form for LIF (time-to-threshold is analytic), so an exact-timing witness is a real possibility
worth pinning in Section 7.

---

## 4. Prior art to cede — refverify gate ([PLACEHOLDER], no DOIs invented)

All entries are hunched-from-memory prior art and MUST clear the R019/R109 Byzantine–Bayesian gate
(`refcheck.py` / refverify) before any manuscript use. **No DOIs, pages, or volumes are asserted.**

- **[PLACEHOLDER] SNN theory / computational power of spiking neurons** — the canonical result that spiking
  (timing-based) neurons are a distinct/more-powerful computational model than rate/sigmoidal units.
  (Maass, "Networks of spiking neurons: the third generation of neural network models," *Neural Networks*,
  late 1990s — metadata UNVERIFIED.)
- **[PLACEHOLDER] neuromorphic-as-approximation / energy–accuracy tradeoff** — spiking realizations as
  approximate/low-power computation; the accuracy-vs-energy (spikes) frontier. (Candidate anchors: Merolla
  et al. TrueNorth *Science* 2014; Davies et al. Loihi *IEEE Micro* 2018; Roy, Jaiswal, Panda "Towards
  spike-based machine intelligence with neuromorphic computing," *Nature* 2019 — ALL metadata UNVERIFIED.)
  This is the literature that already owns the "energy–accuracy tradeoff curve"; F26 cedes the *existence*
  of the curve and claims only the *WySE recasting* (the curve is a (D_s, D_b) frontier).
- **[PLACEHOLDER] event-driven / exact SNN simulation** — event-driven simulation of spiking networks with
  analytic spike times (the exact-timing carrier that makes a `proven`-grade witness plausible). (Candidate
  anchors: Brette et al. "Simulation of networks of spiking neurons: a review," *J. Computational
  Neuroscience* 2007; Ros/Carrillo event-driven LUT schemes — metadata UNVERIFIED.)
- **[PLACEHOLDER] spike-train distance metrics** — the D_b instantiation. Victor & Purpura spike-distance;
  van Rossum "A novel spike distance," *Neural Computation* ~2001 — metadata UNVERIFIED. These are load-
  bearing (they DEFINE the behavioral metric), so verify FIRST.
- **[PLACEHOLDER] DEVS-of-SNN, if it exists** — the key literature-gap probe. Search for any published
  DEVS / Zeigler-formalism model of spiking neurons or neuromorphic hardware. **If it exists, F26 must cede
  the DEVS-modeling and claim only the (D_s, D_b)-measured-homomorphism-and-frontier layer** (the same
  posture the fusion family took toward Kennedy–O'Hagan). **If it does not exist**, the DEVS formalization
  of the SNN is itself a contribution (but a modeling contribution, not the theorem — do not conflate).
  Zeigler's DEVS quantized-integrator / DEVS&DESS hybrid formalism is the ceded substrate either way.

Already-approved refs likely reusable (confirm in approved.bib via reflookup): Girard & Pappas 2007
(behavioral distance → D_b), Wach & Salado 2024 (degree-of-homomorphism → D_s), Wach 2022 (WySE
foundations). Do NOT assume; run reflookup.

---

## 5. Dependencies + ties

- **F24 (Kennedy–O'Hagan coupling as readout comorphism).** Strongest structural sibling. The neuromorphic
  realization is a *low-fidelity, low-energy* surrogate for the exact target computation — precisely the
  multi-fidelity posture. The encode/decode pair `(enc, dec)` plays the role of KOH's readout comorphism ρ;
  the spike-budget sweep is the fidelity-level sweep. F26's (D_s, D_b) frontier is the neuromorphic instance
  of the multi-fidelity level-crossing that F24 formalizes. **Reuse F24's comorphism machinery; do not
  reinvent it.**
- **Candidate E (Cody 2021 Mesarovician transfer distance).** The energy–accuracy frontier is a distance in
  the same family as transfer distance. If the SNN is a *learned* realization (Phase-2 stretch, NOT the
  first run), the gap between the trained SNN and the target is literally a transfer distance. First run
  stays STRONG-grounded (specified target, not trained) to keep the wyse-model-generation fence intact.
- **biomimetics-analyst skill.** The biological neuron → engineered SNN correspondence is exactly a bio-eng
  morphism of the kind that skill catalogs. F26 is the *rigorous, measured* version of a biomimetics
  candidate: the skill's 7-step discovery protocol (biophysics-modeler → state-space → morphism
  classification) is the natural front-end for pinning `Z*` and `Z_snn`. Load biomimetics-analyst when
  formalizing the neuron; load wyse-model-generation when transcribing it into the validated quintuple.
- **wyse-model-generation skill.** The carrier (Section 1) is generated by this skill's
  propose → validate → measure loop. F26 would be its **third exercised object, and its first at level LC
  (coupled) and first event-timing carrier** — directly filling the skill's stated pre-(b) gap ("a second
  LEVEL not LA + a coupled LC system").
- **TMS +probability thread.** If spike generation is stochastic (Poisson neurons), D_b lifts to a
  Wasserstein / Giry-monad distance and F26 touches the +probability morphism (F7/F8 neighborhood). Keep
  the first run DETERMINISTIC (LIF, fixed threshold) to isolate the structural claim.

---

## 6. Fable-shape verdict

**Fable-worthy: YES, conditionally — Tier 2**, gated on pinning the carrier and on the DEVS-of-SNN prior-art
probe.

- **The delta vs. ceded folklore.** Folklore = "spikes are events, SNNs simulate on event-driven engines,
  and there is an energy–accuracy tradeoff." F26's NEW content = (i) the neuromorphic realization is a
  *WySE homomorphism* with a *measured* D_s (nobody in the neuromorphic literature measures structural
  degree-of-homomorphism — same gap the fusion inventory found for D_s), and (ii) the energy–accuracy
  tradeoff is a *(D_s, D_b) frontier on the degree plane*, giving the tradeoff a two-channel (structural +
  behavioral) decomposition it currently lacks. The homomorphism floor is near-certain and cheap; the
  frontier/no-free-lunch claim is the genuine theorem and the higher-risk contribution.
- **Main risk.** **Carrier under-determination + the "so what" risk.** If `Z*`, the level, and the
  encode/decode pair are not pinned to a single specified computation, the run degenerates into a
  narrative that spikes *are* events (folklore) rather than a measured homomorphism with teeth. Second-order
  risk: the frontier claim may be *true but loose* (the (D_s, D_b) monotonicity holds trivially), in which
  case F26 reduces to the homomorphism floor (still publishable, smaller). Third: DEVS-of-SNN may already
  exist (probe first) — if so, cede the modeling and keep only the measured-degree layer.
- **Ripeness.** High. It reuses the fully-built WySE spine (D_s, D_b, DEVS carrier, comorphism from F24) and
  the wyse-model-generation loop; the only new machinery is a spike-train metric for D_b (off-the-shelf,
  Victor–Purpura / van Rossum) and a LIF-DEVS transcription (analytic event times).

---

## 7. What must be PINNED before a run (the carrier)

Ordered gate — a run session does these first, in order, and STOPS if any cannot be pinned:

1. **Fix the target `Z*`.** One named, externally-specified computation (recommend: 2-input temporal-AND /
   coincidence detector). State it as a WySE quintuple at a stated level with a *purpose* justifying the
   level (wyse-model-generation Step 1). No trained network on the first run.
2. **Decide atomic vs. coupled.** First run = **atomic** LIF-DEVS single neuron (defer the coupled-DEVS
   network to a second wave). Pin `SZ, IZ, OZ, NZ_int, NZ_ext, RZ, ta` explicitly from the LIF equations +
   DEVS quantized-integrator pattern; mark every inferred component (Guard 1).
3. **Fix `(enc, dec)`.** The encode (logical input → spike times) and decode (output train → value) pair,
   held constant across the run. This is the F24-style readout comorphism; without it D_s and D_b are
   undefined.
4. **Fix the D_b metric.** Choose ONE spike-train distance (Victor–Purpura *or* van Rossum) and its timing
   parameter, and the decoding-error metric. Verify its reference FIRST (Section 4).
5. **Pre-declare the witness numbers (wyse-model-generation Step 3).** The coincidence truth table over the
   offset sweep, the exact-regime D_b = 0 assertion, the decoy-FAILS assertion, and the spike-budget sweep
   points — as specific numbers a mismatch would forbid, BEFORE running.
6. **Decide the rigor target.** Default ceiling is SME-adjudicated (floating-point membrane). Investigate
   whether the analytic LIF event-time (closed-form time-to-threshold) supports an **exact-timing carrier**
   for a `proven`-grade witness; if yes, pin that carrier instead.
7. **Run the DEVS-of-SNN prior-art probe (Section 4) and reflookup** before writing anything citable; stage
   gating refs to `pending/`, do NOT promote to approved.bib outside the run session.

---

*Scoping note only. No witness run, no D_s/D_b computed, no reference promoted. All (a). To be executed in a
distinct, dedicated session per the Fable cost/discipline convention.*
