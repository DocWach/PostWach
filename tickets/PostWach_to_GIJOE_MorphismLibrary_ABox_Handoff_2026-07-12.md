# PostWach -> GI-JOE Handoff: Morphism Library Catalog ABox Formalization (Wave 1+2, C1-C12)

**Document type:** Hive-to-hive handoff ticket  
**From:** PostWach (CTO / Chief Scientist) — adjudication authority  
**To:** GI-JOE — ontology ABox owner (`ml:` namespace, `http://morphlib.ontology/library#`)  
**Date:** 2026-07-12  
**Status:** Awaiting GI-JOE formalization; PostWach adjudication COMPLETE  
**R108 routing:** PostWach adjudicated; GI-JOE formalizes ABox + runs the ontology gate; SEAD only if an external deliverable surfaces.

PROVENANCE: This handoff document was authored by Opus 4.8 (claude-opus-4-8[1m]), vendor Anthropic, access mode Claude Code CLI subagent, 2026-07-12; compiled and written by a Sonnet 4.6 (claude-sonnet-4-6) compilation subagent at the principal's direction, 2026-07-12. Delegation: PostWach coordinator agent (Sonnet 4.6) compiled from Fable 5 (claude-fable-5[1m]) source candidate entries; PostWach CTO (principal Paul Wach) adjudicated rigorLevel assignments. Attribution per R018.

---

## 1. Background

The Morphism Library catalog now contains 12 new adjudicated candidate entries (C1-C12), extending the prior wave-1 catalog (E1-E7 + E8). These entries were produced by Fable 5 (claude-fable-5[1m]) on 2026-07-12, each with a self-asserting Python witness (exit code 0, SHA-256 recorded per entry). The entries apply CLOSED machinery from the Target A v2, Target B, StochMorph, GIRY, SMDP, and OT-DC candidate documents; none pushes a new theorem.

This handoff provides everything GI-JOE needs to formalize the 12 entries as `ml:` ABox individuals in the content-frozen schema `Morphism_Library_Ontology_Schema_v1.1.md`. It does NOT contain TTL; PostWach is prose-first per the D-C default. GI-JOE writes the TTL.

The schema GI-JOE engineers against: `Morphism_Library_Ontology_Schema_v1.1.md` (content-frozen 2026-07-10; applies principal decisions D-3, D-4, D-7 to v1). Namespace: `ml:` = `http://morphlib.ontology/library#`.

---

## 2. ABox-Ready Catalog Table (C1-C12)

Each row is one individual. C3 and C8 each decompose into two sub-entries at the exact/nonexact corner; those sub-entries are listed separately as they become distinct `ml:Morphism` / `ml:Resolution` or `ml:Pedigree` individuals.

### 2.1 Row notation

- **entry_id**: the `ml:` individual name (snake_case IRI local part)
- **systems**: source -> target (families)
- **relationType**: `ml:Resolution` (within-family) or `ml:Pedigree` (cross-family); Resolution is subClassOf Pedigree per v1.1 D-6, so BOTH tags apply to every Resolution entry
- **cardinality**: iso / homo / coupling / partial
- **level**: LA / LC->LA (per entry)
- **linearity**: linear / nonlinear / n/a (stochastic)
- **exactness**: exact / partial / approximate
- **D_s profile**: K1/K2/K3 summary + DoH + g_max (do-not-rank scalars)
- **D_b**: structural predictor + measured/bounded value
- **witness SHA-256**: from the executed self-asserting Python witness
- **rigorLevel**: PRINCIPAL-ADJUDICATED (use exactly as given)

---

### Wave 1 (C1-C5)

**C1: `pendulum__vdp__LA-ode-nonlinear`**

| Field | Value |
|---|---|
| entry_id | `pendulum__vdp__LA-ode-nonlinear` |
| systems | Damped pendulum (rotational-mechanical) -> Van der Pol oscillator (nonlinear electrical/auto-oscillator); branch mu=-1/2 ONLY; mu>0 REFUSED (Finding C1-F2, trace obstruction) |
| relationType | `ml:Pedigree` (cross-family; no resolution content) |
| cardinality | partial (non-total, non-surjective); direction pendulum -> VdP |
| level | LA (atomic core); D_b at LF2 |
| linearity | nonlinear |
| exactness | partial / approximate: T-COV fires (c_S^dom=1/2, c_S^cod=1/3), K3 exact on covered scope (v_N=v_R=[], part_B=1); external epsilon=1/24 on covered ODE |
| D_s profile | K1: partial, anchor=pendulum Z_P, scope={p0,p1}x I x{o0,o1}; K2: P_S={v0:[p0],v1:[p1]}, u_dom_S={p2,p3}, u_dom_O={o2,o3}; K3: 4 N-events + 2 R-checks checked, 4 charged to coverage, v_N=[], v_R=[]; DoH^cov=1 (do-not-rank), g_max=1, D_s^max=0 on covered scope |
| D_b | Inside (Zeigler ch17 attenuation, a=3/4, eps=1/24): D_b <= 1/6, exact rational; Outside: CERT-NEG fires (a=5/4 -> unbounded) |
| witness SHA | `e91874ab37e6c265781921d4af22705d931c3b247a4f8193ba992fa7a79fbc96` |
| rigorLevel | **proven** (scoped/machine-checked; caveat: SME review before manuscript; generality beyond the pinned mu=-1/2 instance is a declared GAP-C1-DB/GAP-C1-CERT) |

---

**C2: `pendulum__joJunction__LA-ode-nonlinear`**

| Field | Value |
|---|---|
| entry_id | `pendulum__joJunction__LA-ode-nonlinear` |
| systems | Driven damped pendulum (rotational-mechanical) -> Josephson junction phase dynamics, RCSJ model (superconducting-electrical); pinned alpha_P^2=alpha_J^2=1/4 instance; mismatched branch REFUSED |
| relationType | `ml:Pedigree` (cross-family: rotational-mechanical vs superconducting-electrical) |
| cardinality | isomorphism (bijective, total on full nonlinear state space) |
| level | LA; D_b at LF2 |
| linearity | nonlinear (shared sin form; S-UNIFORM intertwining) |
| exactness | exact (empty violation sets total scope; no linearization; D_b=0 exactness-forced) |
| D_s profile | K1: bijective, anchor=pendulum, scope=total (full cylinder); K2: all-singleton, u_dom=u_cod={} on all carriers; K3: coefficient tuple identity S-UNIFORM, v_N=[], v_R=[], T-PART=1 (7/7); DoH=1 (do-not-rank), g_max=1, D_s^max=0 |
| D_b | D_b=0 exactness-forced (identical transported fields -> identical trajectories via Picard-Lindelof); NUMERICAL float-sin RK4 confirms 0.000000e+00; large-angle regime exercised (max|q|=1.239 rad) |
| witness SHA | `0e47bae9aa3991575e61ed91baa718cac955814f3aef7b275c7ea85d7772b2d0` |
| rigorLevel | **proven** (machine-checked bijection + S-uniform intertwining in exact rationals; Josephson [PLACEHOLDER] refs must refverify before manuscript) |

---

**C3a: `MSD__MSD__resolution-stochastic_exact`** (sub-entry: exact corner)

| Field | Value |
|---|---|
| entry_id | `MSD__MSD__resolution-stochastic_exact` |
| systems | Fine 4-state MSD-analog PTS -> 2-state lumped PTS (same mechanical family); lumping h: s0->B0, s1/s2/s3->B1 |
| relationType | `ml:Resolution` (within-family, same system; also Pedigree by nesting) |
| cardinality | abstraction (surjective, many-to-one); direction fine -> coarse |
| level | LA; D_b at LF2 |
| linearity | n/a (stochastic) |
| exactness | exact (LumpVar=0, K3 violation set={}, D_b=0 exactness-forced) |
| D_s profile | K1: abstraction, anchor=fine PTS, scope=total; K2^Sigma: P_S={B0:[s0],B1:[s1,s2,s3]}, profile (1,3), u=empty; K3^Sigma: r_s=0 all s, violation set={}; DoH=2/3 (do-not-rank), g_max=3, D_s^max=2/3; LumpVar=0, LumpSTD=0, Kr=0, Kp=0 |
| D_b | D_b=0 (Thm 22.2 exact corner; block-sum lumpable) |
| witness SHA | `0894017d9b212d99d82d0ec329495a4f4294fd329a2ffb03cbbd182d3bdc3244` (shared with C3b) |
| rigorLevel | **proven** (exhaustive-rational finite carrier; machine-checked) |

---

**C3b: `MSD__MSD__resolution-stochastic_nonexact`** (sub-entry: nonexact corner)

| Field | Value |
|---|---|
| entry_id | `MSD__MSD__resolution-stochastic_nonexact` |
| systems | Same fine-to-coarse MSD-analog PTS pair; s3 row perturbed (m_s3(B0)=1/2 instead of 1/4) |
| relationType | `ml:Resolution` (within-family; also Pedigree) |
| cardinality | abstraction (surjective); direction fine -> coarse |
| level | LA; D_b at LF2 |
| linearity | n/a (stochastic) |
| exactness | non-exact / approximate (LumpVar=1/72>0; K3 violation set={s1,s2,s3}; D_b<=1/5 by ceded ch17 bound) |
| D_s profile | K1: identical to C3a; K2^Sigma: identical to C3a (profile (1,3), u=empty); K3^Sigma: r_s(B0)={s0:0,s1:-1/12,s2:-1/12,s3:+1/6}, violation set={s1,s2,s3}; DoH=2/3, g_max=3, D_s^max=2/3; LumpVar=1/72, LumpSTD=sqrt(1/72), Kr=0, Kp=1/6 |
| D_b | D_b<=1/5 (Dobrushin a=1/6, eps_P=1/6; ceded Zeigler ch17 attenuation bound; accumulated e_200<1/5 exact) |
| witness SHA | `0894017d9b212d99d82d0ec329495a4f4294fd329a2ffb03cbbd182d3bdc3244` |
| rigorLevel | **proven** (exhaustive-rational finite carrier; machine-checked) |

---

**C4: `DCMotor__LA-mono__couplingRecord`**

| Field | Value |
|---|---|
| entry_id | `DCMotor__LA-mono__couplingRecord` |
| systems | Armature-controlled DC motor: LC_R2 (coupled, with gyrator interface) -> LA_mono (interface-erased monolithic resultant); ONE physical system at two interface-visibility granularities |
| relationType | `ml:Resolution` (within-family coarsening; interface-visibility granularity; also Pedigree) |
| cardinality | abstraction: bijective on sigma_Z sorts (identity witness); empty partial maps on all interface carriers |
| level | LC->LA; D_b at LF2 |
| linearity | linear |
| exactness | over sigma_Z: exact (v_N=[], v_R=[], T-PART=1); over sigma_W: interface carriers entirely in u_dom (total erasure); FIRST catalog entry with live sigma_W record |
| D_s profile | sigma_Z: K1 bijective anchor=LC_R2 scope=total; K2 all-singleton; K3 empty violations T-PART=1(20/20); g_max=1, D_s^max=0. sigma_W coupling record: P_X={} on all five carriers (IoX,Ch,IF,E,A); u_dom_X=full carrier identities; u_cod_X={}; T-COV c_dom=1.0 on all five; v_P={}; warning=(blind T, viol F, conc F) |
| D_b | D_b=0 (discrete: 1360 trajectories, 0 mismatches; continuous: exact matrix identity forces D_b=0) |
| witness SHA | `a112cd0b41253cb76b442dab1a1222afab6e2a2cdcd008c8b93a64843a1d70b3` |
| rigorLevel | **proven** (machine-checked; caveat: SME review before manuscript; sigma_W record requires v1.1 D-3 Interface-as-conduit decision) |

---

**C5: `MSD4__seriesRLC3__partialMorphism`**

| Field | Value |
|---|---|
| entry_id | `MSD4__seriesRLC3__partialMorphism` |
| systems | MSD Z4 (four-state regime-refined) -> partial series-RLC Z3' (three-state; critically-damped regime NOT declared in target) |
| relationType | `ml:Resolution` (within-family partial resolution; also Pedigree; partiality lives in the within-family factor f:MSD Z4->MSD Z3; cross-family factor g is exact iso) |
| cardinality | partial (non-total): u_dom_S={s2}, injective on domain, surjective onto declared target |
| level | LA; D_b at LF2 |
| linearity | linear (partiality isolated, not nonlinearity) |
| exactness | partial / non-exact: T-COV fires (c_S^dom=c_O^dom=1/4); K3 exact on covered events (v_N=v_R=[], T-PART=1 on all 26 checked events); one event excluded (zeta=1: (s0,i1) charged to u_dom) |
| D_s profile | K1: partial, anchor=MSD Z4, scope={s0,s1,s3}xIx{o0,o1,o3}; K2: P_S singleton covered, u_dom_S={s2}, u_dom_O={o2}, all u_cod={}; K3: 26 events checked (6,5,6 per zeta-variant), 1 excluded, v_N=v_R=[] all; part_B=1 all; g_max=1, D_s^max=0, DoH^cov=1 |
| D_b | D_b(covered-scope)=0 exactness-forced; D_b(default extension)=1 (318 of 378 zeta=1 trajectories escape scope; escape fraction=53/63) |
| witness SHA | `7af541312eb523372a231896d866fefeed120154f14ba902b8cf51fe53e262db` |
| rigorLevel | **proven** (machine-checked; caveat: SME review before manuscript; GAP-CONT for measure-theoretic c_dom on infinite carriers) |

---

### Wave 2 (C6-C12)

**C6: `neuron__RC__LA-ode-bioeng`**

| Field | Value |
|---|---|
| entry_id | `neuron__RC__LA-ode-bioeng` |
| systems | Linearized Hodgkin-Huxley neuron (subthreshold; biological excitable-membrane family) -> passive RC circuit (electrical-circuit family); FIRST bio-to-engineered catalog entry |
| relationType | `ml:Pedigree` (cross-family: biological-neural vs electrical-circuit) |
| cardinality | isomorphism on declared subthreshold scope ({h0,h1}); full HH state space carries directed domain blind spot (suprathreshold spike block) |
| level | LA; D_b at LF2 |
| linearity | nonlinear (source is nonlinear HH; scoped to subthreshold linearization; nonlinearity captured as T-COV defect + CERT-NEG) |
| exactness | exact ON covered scope (empty violation sets, singleton granules, D_b=0); c_S^dom=3/5 (directed, domain-only); CERT-NEG outside; DIRECTED defect pattern (c_S^cod=0) |
| D_s profile | K1: iso on subthreshold scope, anchor=Z_HH; K2: P_S={r0:[h0],r1:[h1]}, u_dom_S={h2,h3,h4}, u_cod_S={}, u_dom_O={y2,y3,y4}, u_cod_O={}; K3: 4 N-events + 2 R-checks, 6 suprathreshold charged to coverage, v_N=[], v_R=[], part_B=1; DoH^cov=1, g_max=1 |
| D_b | Inside covered scope: D_b=0 exact (linearized-HH and RC ODEs identical; Euler byte-identical); Outside: CERT-NEG (a=5/4, eps=1/12 -> e_50>10^4, unbounded) |
| witness SHA | `e51d9d83410c08e1d52cd72fad9263e5a27b42013d7fa4984d475fd9ffd870e3` |
| rigorLevel | **SME-adjudicated** (machine-checked on declared rational stand-ins; HH canonical parameters are [PLACEHOLDER] pending refverify -- must run refverify on HH 1952 source before promoting to proven) |

---

**C7: `heat1D__RC-ladder__LA-pde-thermal`**

| Field | Value |
|---|---|
| entry_id | `heat1D__RC-ladder__LA-pde-thermal` |
| systems | 4-node FD discretization of 1D heat equation (thermal/diffusion family) <-> 4-node RC-ladder chain (electrical family); ALSO within-family N-node coarsening ladder (4->2 non-exact, 4->1 exact); ALSO partial pedigree (missing inductance, T-COV codomain defect) |
| relationType | `ml:Pedigree` (cross-family thermal<->electrical) as primary; `ml:Resolution` for N-node coarsening ladder |
| cardinality | Pedigree N=4: isomorphism; Resolution 4->2: abstraction (surjective, block-average); Resolution 4->1: abstraction (grand mean, exact) |
| level | LA; D_b at LF2 |
| linearity | linear |
| exactness | Pedigree N=4: exact; Resolution 4->2: non-exact (K3 FIRES, non-congruence partition, D_b>0); Resolution 4->1: exact (grand mean conserved mode, K3 exact, D_b=0 despite g_max=4); Partial pedigree: c_S^cod=1/2 (missing inductance, codomain blind spot) |
| D_s profile | N=4 pedigree: all-singleton, g_max=1, D_s^max=0, v_N=v_R=[]; 4->2: fibers [[T1,T2],[T3,T4]], g_max=2, DoH_S=1/2, D_s^max=1/2, K3 FIRES (lumping residual L nonzero); 4->1: g_max=4, DoH_S=1/4, D_s^max=3/4, K3 exact (1^T A4=0); partial pedigree: u_cod={iL1,iL2,iL3,iL4}, c_S^cod=1/2, c_S^dom=0; Finding C7-F1: coarsening depth does NOT order D_b (monotone reading refuted) |
| D_b | N=4 pedigree: D_b=0 sound; 4->2: D_b=1204.../4835...~0.249 (onset 1/64 at step 2); 4->1: D_b=0 (heat conservation); partial pedigree: no D_b claim on uncovered inductive regime |
| witness SHA | `20cd1b66dedc87b89498675a8f97b3be5c5ef67a22369cc710cbb2076480f184` |
| rigorLevel | **proven** (machine-checked; caveat: SME review before manuscript; D_b 4->2 is Euler dt=1/4 T=10 measurement not analytic steady-state) |

---

**C8a: `MDP__MDP__RL-homomorphism_exact`** (sub-entry: exact corner)

| Field | Value |
|---|---|
| entry_id | `MDP__MDP__RL-homomorphism_exact` |
| systems | 6-state grid-world MDP (uniform goal-reach) -> 2-state abstract MDP (goal/non-goal lumping); FIRST RL/MDP-homomorphism catalog entry |
| relationType | `ml:Resolution` (within-family stochastic abstraction; also Pedigree) |
| cardinality | abstraction (surjective, 5-to-1 non-goal block); direction fine -> coarse |
| level | LA; D_b at LF2 |
| linearity | n/a (stochastic) |
| exactness | exact (LumpVar=0, K3 violation set={}, D_b=0; exact MDP homomorphism, value preserved) |
| D_s profile | K1: abstraction, anchor=fine MDP, scope=total; K2^Sigma: P_S={B1:[c0..c4],B2:[c5]}, profile (1,5), u=empty; K3^Sigma: r_s=0 all s, violation set={}; DoH=3/5, g_max=5, D_s^max=4/5; LumpVar=0, Kr=0, Kp=0 |
| D_b | D_b=0 (value-function gap; V=(2/5,...,2), V'=(2/5,2); exact homomorphism) |
| witness SHA | `26581f097feae06eaace259beadbe9c10bb67d17022cbf548a1acdbd44e3c72e` (shared with C8b) |
| rigorLevel | **proven** (exhaustive-rational; RL references [PLACEHOLDER] must refverify before manuscript) |

---

**C8b: `MDP__MDP__RL-homomorphism_nonexact`** (sub-entry: nonexact corner)

| Field | Value |
|---|---|
| entry_id | `MDP__MDP__RL-homomorphism_nonexact` |
| systems | Same goal-lumping, goal-drift grid (cells adjacent to goal reach it with prob 1/2; interior cells reach goal with prob 0) |
| relationType | `ml:Resolution` (within-family; also Pedigree) |
| cardinality | abstraction (surjective); direction fine -> coarse |
| level | LA; D_b at LF2 |
| linearity | n/a (stochastic) |
| exactness | non-exact (LumpVar=3/50>0; K3 violation set={c0..c4}; D_b=5/21 measured value gap) |
| D_s profile | K1: identical to C8a; K2^Sigma: identical to C8a (profile (1,5), u=empty); K3^Sigma: r(B2)={c0:-1/5,c1:-1/5,c2:+3/10,c3:-1/5,c4:+3/10,c5:0}, violation set={c0,c1,c2,c3,c4}; DoH=3/5, g_max=5, D_s^max=4/5; LumpVar=3/50, Kr=0, Kp=3/10. T-STOCH-DS separation (Part B): K2 profile (2,4) vs (3,3) separates two MDPs equal on ENTIRE Ravindran-Barto/Ferns tuple |
| D_b | D_b=5/21 (measured value-function gap; |V(c2)-V'(B1)|=|4/7-1/3|=5/21 at goal-adjacent cells) |
| witness SHA | `26581f097feae06eaace259beadbe9c10bb67d17022cbf548a1acdbd44e3c72e` |
| rigorLevel | **proven** (exhaustive-rational; RL references [PLACEHOLDER] must refverify before manuscript) |

---

**C9: `threebody__coupling__LC-multi`**

| Field | Value |
|---|---|
| entry_id | `threebody__coupling__LC-multi` |
| systems | Linear three-body spring chain: LC (3 MSD subsystems + 2 interface systems I_AB, I_BC) -> LA_mono (6-state monolithic resultant); FIRST sigma_W record over TWO interfaces simultaneously |
| relationType | `ml:Resolution` (within-family, interface-visibility granularity; also Pedigree) |
| cardinality | abstraction: bijective on sigma_Z sorts (identity witness); empty partial maps on all interface carriers of BOTH interfaces |
| level | LC->LA; D_b at LF2 |
| linearity | linear |
| exactness | sigma_Z: exact (v_N=[], v_R=[], T-PART=1); sigma_W: BOTH interface systems entirely in u_dom (total erasure); joint warning fires on blind-spot component of BOTH I_AB and I_BC |
| D_s profile | sigma_Z: K1 bijective anchor=LC scope=total; K2 all-singleton S(8),I(4),O(2); K3 empty violations T-PART=1(40/40); g_max=1, D_s^max=0. sigma_W: per-interface records identical in kind to C4; P_X={} on all five carriers for EACH interface; u_dom_X=full carrier identities per interface; T-COV c_dom=1.0 all carriers both interfaces; v_P={} (scope=0) both; disjoint-carrier factorisation holds (benign; no laxator claimed per OT-DC) |
| D_b | D_b=0 (discrete: 2720 trajectories, 0 mismatches; continuous: 0.0 exact) |
| witness SHA | `df69e67eae8f8933efc9c7b978686a3a382c8bd9d634218b99aad794a8851854` |
| rigorLevel | **proven** (machine-checked; sigma_W record requires v1.1 D-3; GAP-MULTI probed but not closed) |

---

**C10: `noncompositionality__sigma_W__concreteChain`**

| Field | Value |
|---|---|
| entry_id | `noncompositionality__sigma_W__concreteChain` |
| systems | DC motor (E8/C4 family) at three interface-visibility granularities: LC_R2 -> LC_R3 (channel rename) -> LA_mono (total erasure) / LA_semi (partial single-lane erasure); NEGATIVE / non-compositionality demonstrator |
| relationType | `ml:Resolution` chain (interface-visibility coarsening; also Pedigree); entry KIND = NEGATIVE demonstrator (OT-DC instantiation) |
| cardinality | sigma_Z identity witness at every node (bijective); interface components: h1/h1' are renaming isomorphisms, h2 total erasure, h2_p partial injection |
| level | LC->LC->LA; D_b consumed from C4 |
| linearity | linear |
| exactness | sigma_Z: exact at every chain node; sigma_W: OT-DC demonstrated: equal step records + same h2_p map -> UNEQUAL composite records (g_A: u_dom_Ch={ch_emf}, g_B: u_dom_Ch={ch_torque}); Lemma ABS: total erasure absorbs alignment; WARNING/T-COV/scalar defect all EQUAL across chains (invisible to behavioral axis); only record identity content separates |
| D_s profile | Headline chain (LC_R2->LC_R3->LA_mono): both composites = C4 one-step record (Lemma ABS; total erasure). Non-functionality witness (partial erasure via h2_p): sigma_W(h1)=sigma_W(h1') as FULL records; composite g_A and g_B differ in P_Ch and u_dom_Ch (torque vs emf lane); warning (T,F,F) equal; T-COV c_dom=(1/2,1/2,1/2,1/2,0) equal; scalar defect=0 both. Verdict-transfer: phi_t={ch_torque} in T(g_A) but gap in T(g_B) (and vice versa for phi_e). Catalog rule: recompute sigma_W at composite level from maps; never predict from step records |
| D_b | No new D_b; consumes C4 D_b=0; D_b, warning, T-COV, scalar defect all equal across both chains (confirmed invisible to the structural separation) |
| witness SHA | `23b751d8de4c78364b6083556aa3202f9f4c65e908c40e1dcccc4814c33b3020` |
| rigorLevel | **proven** (machine-checked; sigma_W requires v1.1 D-3; Fong decorated-cospan machinery ceded [PLACEHOLDER] must refverify before manuscript) |

---

**C11: `continuousMeasure__Giry__stochastic`**

| Field | Value |
|---|---|
| entry_id | `continuousMeasure__Giry__stochastic` |
| systems | Continuous [0,1]-state identity-kernel Markov system M_cont -> finite quotient M_disc over Y={0,1}; TWO lumping maps compared: q_A (threshold at 1/2) and q_B (quarter-interleave); FIRST continuous-measure stochastic entry |
| relationType | `ml:Resolution` (same system, coarser measurable observation; also Pedigree) |
| cardinality | abstraction (surjective measurable lumping); direction continuous fine -> finite coarse |
| level | LA (atomic stochastic, Giry-monad carrier); D_b at LF2 |
| linearity | n/a (stochastic) |
| exactness | exact (both maps: PushW1=Kp^c=LumpVar^c=BisimIntra^c=0; kernel congruences; D_b=0 exactness-forced); SEPARATION at exact corner: K2^c sub-sigma-algebras F_A != F_B null-robustly (min symdiff=1/2), K3^c disintegrations differ (TV=1/2, W1=1/8 per fiber); verdict-transfer differs both directions |
| D_s profile | K1^c: abstraction, anchor=M_cont, scope=total, measurable, mod-null, std-Borel; K2^c: F_A={emptyset,[0,1/2),[1/2,1],X} vs F_B={emptyset,[0,1/4)u[1/2,3/4),[1/4,1/2)u[3/4,1],X}; K3^c: disintegration mu^A_y = 2.Leb on ONE interval vs mu^B_y = 2.Leb on TWO intervals; fiber-width scalar 2^h2=1/2 collapses (=, do-not-rank); profile (1,1) vs (2,2) |
| D_b | D_b=0 for BOTH q_A and q_B (exactness-forced; trivial dynamics; no contraction certificate needed) |
| witness SHA | `eb9b68f59dcf2f4a4799a5426518d61794faa39fc6a7124b2c1d501fed109042` |
| rigorLevel | **SME-adjudicated** (machine-checked on exact rational symbolic realization; GAP-KS-CONT: continuous Kemeny-Snell citation is [PLACEHOLDER]; disintegration existence theorem is classical [PLACEHOLDER] -- continuous generality on ceded measure theory; refverify before manuscript) |

---

**C12: `SMDP__semicontinuous__timed`**

| Field | Value |
|---|---|
| entry_id | `SMDP__semicontinuous__timed` |
| systems | Machine-degradation/maintenance semi-Markov system M (states N/W/D/F/X, Erlang(2) non-exponential holding times) -> 3-block abstract semi-Markov M' (blocks U={N,W,D}, R={F}, X={X}); FIRST timed catalog entry (off the untimed fence) |
| relationType | `ml:Resolution` (semi-Markov lumping: same system, coarser state granularity; also Pedigree) |
| cardinality | surjection (abstraction, total; granule sizes (3,1,1)) |
| level | LA (timed-stochastic semi-Markov carrier); D_b at LF2 |
| linearity | n/a (stochastic) |
| exactness | approximate on BOTH axes: PTS not lumpable (LumpVar=19/288>0, Kp=1/3, Kr=1; K3 violators {N,W,D} on N-side, {N,D} on R-side); TTS not exact-timing (Thm 22.1 cond-2 fails, LumpSTD_ta=4>0); four-coordinate record DR^smdp=(K1;K2^Sigma;K3^Sigma;K_ta^Sigma) fully exercised; separation against three scalar-equal morphisms (m1/m2/m2') at BOTH WT1 and WT2 corners |
| D_s profile | K1: abstraction, anchor=M, scope=total, abstract-TTS=block-uniform mixture (explicit K1 datum per GAP-COUPLE); K2^Sigma: blocks {U:[N,W,D],R:[F],X:[X]}, granule sizes (3,1,1), g_max=3, D_s^max=2/3; K3^Sigma: LumpVar=19/288, Kp=1/3, Kr=1, violator sets as above; K_ta^Sigma: per-(B,B') state-indexed conditional CDF families (Erlang(2) scale); (U,U)=(U,R) fibers = (N,W,D); spread_ta(U,U)=4 for m1; LumpSTD_ta=4; exact-timing flag=False; GAP-COUPLE exhibited: occupancy-weighted U-means pairwise distinct (96/17,338/51,108/17) |
| D_b | D_b(m1)=1935/416; D_b(m2)=635/416; D_b(m2')=999/416 (pairwise distinct; scalar-equal morphisms split THREE WAYS on the timed D_b axis; metric=|E_M'[T-to-scrap from U]-E_M[T-to-scrap from N]|) |
| witness SHA | `24e62ca754a9ac5900912f3991f7bf54cf20e9c4c6414e94eafce4743f81ca12` |
| rigorLevel | **SME-adjudicated** (machine-checked on Erlang(2) scale family; GAP-COUPLE: 4th-coordinate independence is construction-relative -- abstract-TTS construction carried as explicit K1 frame datum; SME review of GAP-COUPLE boundary before promoting to proven) |

---

## 3. SHACL / CQ Implications for GI-JOE

GI-JOE should expect these 12 individuals (14 `ml:Morphism`/`ml:Pedigree`/`ml:Resolution` individuals counting C3a/C3b and C8a/C8b as separate) to exercise the following schema constraints and CQ obligations from the portfolio ontology gate (`GI-JOE/.claude/helpers/ontology-gate.sh`):

**(a) Disjoint relation kinds (v1 D-6).** The schema asserts `ml:Resolution rdfs:subClassOf ml:Pedigree` (Resolution implies Pedigree, NOT disjoint). Every C3/C5/C7/C8/C9/C10/C11/C12 RESOLUTION entry is ALSO a PEDIGREE individual. GI-JOE must NOT assert `owl:AllDisjointClasses` over Resolution/Pedigree (that was v0; v1/v1.1 corrects it). The SHACL shape for `ml:Pedigree` must permit `ml:Resolution` individuals as instances without violation.

**(b) rigorLevel enumeration.** The v1.1 schema tags `ml:rigorLevel` as an annotation property with value set `{proven, SME-adjudicated, asserted}`. The 12 entries span all three values. SHACL shapes that constrain `ml:rigorLevel` must permit all three. No entry in this handoff carries `asserted` post-adjudication; GI-JOE should confirm the enumeration constraint does not include `asserted` as a blocking violation for the 9 `proven` entries and 3 `SME-adjudicated` entries.

**(c) D_s and D_b as SEPARATE properties, not one scalar.** Per v1 Design Commitment 3 and D-5, `ml:PredictedBehavior` (D_b) is a predicted artifact linked via `ml:predictsBehavior`, NOT a coordinate of `ml:DegreeOfHomomorphism` (D_s). The ABox must never encode D_b as a field of the D_s triple. Each entry's D_b (behavioral bound or measured value) goes on a distinct `ml:PredictedBehavior` individual linked by `ml:predictsBehavior`. GI-JOE should check that SHACL shapes on `ml:DegreeOfHomomorphism` do NOT expect a `ml:dbValue` property (which belongs on `ml:PredictedBehavior`).

**(d) sigma_W entries (C4, C9, C10).** Three entries carry live sigma_W coupling records. These require the v1.1 D-3 Interface-as-conduit decision: interfaces are conduits (NOT first-class systems with their own quintuples). The sigma_W carrier set (IoX, Ch, IF, E, A) must be modeled as annotation content on the morphism individual, not as `ml:Interface` subclass instances, per D-3. GI-JOE should confirm the ml:Interface class is in scope for this annotation before formalizing C4/C9/C10.

**(e) Stochastic entries (C3, C8, C11, C12).** The K2^Sigma field is a sub-sigma-algebra (C11) or finite kernel partition (C3, C8) rather than a scalar partition-index. GI-JOE should confirm whether v1.1 has a datatype property for the K2 profile (fiber sizes) or whether this is annotation-only for the current ABox milestone.

**(f) Timed entry (C12).** C12 is the first entry exercising the fourth record coordinate K_ta^Sigma. If the v1.1 TBox does not yet include `ml:TimingCoordinate` or a `ml:K_ta` component, GI-JOE should stub it as an annotation pending the schema extension ticket (the consumed SMDP_candidate.md defines the field; whether it is in v1.1 is a GI-JOE schema question).

**(g) CQ coverage.** The portfolio ontology CQs (20 queries in `GI-JOE/queries/portfolio/`) are over `http://joe-g.ontology/portfolio#`, not over `ml:`. The morphism library ontology is INDEPENDENT of the portfolio ontology per v1.1 (no import, no alignment). GI-JOE should confirm whether the 12 individuals belong in the morphism-library ABox only, or whether any cross-ontology bridge triples are expected. PostWach's guidance: morphism-library ABox only for this handoff; bridge triples are a future ticket.

---

## 4. R019 Caveat List

The following reference gaps MUST be resolved before any of these entries are cited in a manuscript or external deliverable:

**C6 (HH parameters):** The Hodgkin-Huxley canonical squid-axon parameters and rest-state gating values (n_0=8/25, m_0=1/20, h_0=3/5 are declared rational stand-ins; the 1952 source is [PLACEHOLDER: Hodgkin-Huxley 1952 squid-axon parameters]) must pass refverify before promoting to `proven`.

**All RL/MDP references (C3b, C8a/b):** Ravindran and Barto 2004 approximate MDP homomorphisms (Kr/Kp); Ferns, Panangaden, Precup 2004/2011 bisimulation metrics; Taylor, Precup, Panangaden 2008; Kemeny and Snell (if cited directly); Givan, Dean, Greig 2003 -- ALL are visible [PLACEHOLDER] in the source entries. Must refverify before manuscript.

**C7 distributed-parameter sources:** heat-conduction / RC electrical-thermal analogy source; RLC transmission-line / distributed-parameter ladder source -- [PLACEHOLDER].

**C10 decorated cospan machinery:** Fong 2015 decorated cospans (`fong2015decoratedcospans`) is grep-confirmed in approved.bib; no additional refverify needed for C10, but the result should be confirmed at formalization.

**C11 continuous measure theory:** Continuous Kemeny-Snell strong-lumpability form (definitional analog, [PLACEHOLDER]); disintegration / regular-conditional-probability theorem on standard Borel spaces (classical, [PLACEHOLDER]).

**C12 SMDP sources:** Ravindran and Barto 2003 SMDP homomorphisms; standard semi-Markov strong-lumpability text; Kemeny and Snell (direct cite); phase-type approximation source; timed-bisimulation source -- ALL [PLACEHOLDER].

**OneDrive store-sync lag note:** Several wave-2 entries (C7, C8, C11) note that the approved-references store (`04 Resource Library/00 Verified References/approved.bib`) was not locally resolvable during the run (OneDrive sync lag). GI-JOE MUST re-grep the store at the time of ABox formalization for all reference keys before considering the R019 obligation satisfied. The keys `wymore1993mbse`, `zeigler2018tms`, `zeigler2018approxmorph`, `girard2007metrics`, `salado2018mathematical`, `benveniste2018contracts`, `cody2021transferdiss` were grep-confirmed by C1/C2/C4/C5 runs where the store WAS present; carry-forward from C7/C8/C11 should be re-confirmed.

---

## 5. R108 Routing

| Stage | Owner | Action |
|---|---|---|
| Adjudication (COMPLETE) | PostWach (CTO, Paul Wach) | rigorLevel assignments per Section 2 of this document; FINAL |
| ABox formalization | GI-JOE | Write TTL individuals into `ml:` namespace per v1.1 schema; one individual per catalog entry (C3 and C8 get two each) |
| Ontology gate | GI-JOE | Run `GI-JOE/.claude/helpers/ontology-gate.sh` (full mode: syntax+SHACL+CQs); gate must PASS |
| SEAD routing | SEAD | Only if an external deliverable (manuscript draft, rendered PDF) requiring the ABox is in scope; PostWach routes the handoff to SEAD at that time |

PostWach does NOT write TTL. GI-JOE does NOT need PostWach re-approval for purely syntactic / OWL-encoding decisions within the v1.1 schema. If a schema gap is discovered (e.g., K_ta^Sigma not in TBox), GI-JOE opens a schema extension ticket and blocks the relevant individual (C12) until resolved.

---

## 6. Source Candidate File Paths

### Wave 1 (C1-C5)

- C1: `C:\Users\pfwac\OneDrive - University of Arizona\Documents\03 Projects\00_Hive_Empire\00 Planning and Execution\Fable 5 planning\research\LibEntry_C1_candidate.md`
- C2: `C:\Users\pfwac\OneDrive - University of Arizona\Documents\03 Projects\00_Hive_Empire\00 Planning and Execution\Fable 5 planning\research\LibEntry_C2_candidate.md`
- C3: `C:\Users\pfwac\OneDrive - University of Arizona\Documents\03 Projects\00_Hive_Empire\00 Planning and Execution\Fable 5 planning\research\LibEntry_C3_candidate.md`
- C4: `C:\Users\pfwac\OneDrive - University of Arizona\Documents\03 Projects\00_Hive_Empire\00 Planning and Execution\Fable 5 planning\research\LibEntry_C4_candidate.md`
- C5: `C:\Users\pfwac\OneDrive - University of Arizona\Documents\03 Projects\00_Hive_Empire\00 Planning and Execution\Fable 5 planning\research\LibEntry_C5_candidate.md`

### Wave 2 (C6-C12)

- C6: `C:\Users\pfwac\OneDrive - University of Arizona\Documents\03 Projects\00_Hive_Empire\00 Planning and Execution\Fable 5 planning\research\LibEntry_C6_candidate.md`
- C7: `C:\Users\pfwac\OneDrive - University of Arizona\Documents\03 Projects\00_Hive_Empire\00 Planning and Execution\Fable 5 planning\research\LibEntry_C7_candidate.md`
- C8: `C:\Users\pfwac\OneDrive - University of Arizona\Documents\03 Projects\00_Hive_Empire\00 Planning and Execution\Fable 5 planning\research\LibEntry_C8_candidate.md`
- C9: `C:\Users\pfwac\OneDrive - University of Arizona\Documents\03 Projects\00_Hive_Empire\00 Planning and Execution\Fable 5 planning\research\LibEntry_C9_candidate.md`
- C10: `C:\Users\pfwac\OneDrive - University of Arizona\Documents\03 Projects\00_Hive_Empire\00 Planning and Execution\Fable 5 planning\research\LibEntry_C10_candidate.md`
- C11: `C:\Users\pfwac\OneDrive - University of Arizona\Documents\03 Projects\00_Hive_Empire\00 Planning and Execution\Fable 5 planning\research\LibEntry_C11_candidate.md`
- C12: `C:\Users\pfwac\OneDrive - University of Arizona\Documents\03 Projects\00_Hive_Empire\00 Planning and Execution\Fable 5 planning\research\LibEntry_C12_candidate.md`

### Schema

- GI-JOE engineers against: `C:\Users\pfwac\OneDrive - University of Arizona\Documents\03 Projects\00_Hive_Empire\00 Planning and Execution\Fable 5 planning\Morphism_Library_Ontology_Schema_v1.1.md` (content-frozen)
- Reference: `C:\Users\pfwac\OneDrive - University of Arizona\Documents\03 Projects\00_Hive_Empire\00 Planning and Execution\Fable 5 planning\Morphism_Library_Ontology_Schema_v1.md` (superseded by v1.1)

---

END OF HANDOFF. Awaiting GI-JOE ABox formalization and ontology gate run.
