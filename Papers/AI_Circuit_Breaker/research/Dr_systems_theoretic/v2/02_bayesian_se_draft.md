# Extraction: Bayesian-Morphism Framework in the Bayesian SE for AI Draft

**Purpose.** Extract, verbatim where possible, the formal treatment of context, V&V confidence propagation, and the Bayesian-morphism framework from Paul Wach's most current draft article on Bayesian systems theory for AI. The prior synthesis (`Papers/AI_Circuit_Breaker/research/Dr_systems_theoretic/synthesis_debate.md`, dated 2026-05-20) was constructed without this material in hand and proposed a five-layer stack for D_r. This document tests each layer of that recommendation against the actual draft.

**Date.** 2026-05-20.

**Primary source.** `C:\Users\pfwac\OneDrive - University of Arizona\Documents\02 My Outreach\2026 - Bayesian_DEVS\revision\main.tex` (full file, lines 1-493). The article is a revision being prepared for a Wiley/INCOSE journal venue (the Systems Engineering journal). Authors: Wach, Krometis, Sonanis, Panchal, Beling, Freeman. Title: "Systems Engineering for AI-based Systems Enabled Through Bayesian and Systems Theoretic Methods."

**Supporting sources.**
- `revision/notation.tex` (symbol definitions, lines 1-39).
- `revision/lbs_diagram.tex` (block diagram of an LBS in its closed context, lines 1-53).
- `revision/network_simple.tex`, `network_full_broken.tex`, `network_full_connected.tex`, `network_latent.tex`, `network_yolo.tex` (the four Bayesian network figures).
- `revision/references.bib` (cited works: wymore1967mathematical, wach2021conjoining, wach2026isomorphism, zeigler2018theory, zeigler2019theory, zeigler2023extending, shadab2021shifting, salado2018a, pearl2009causality).

**Scope discipline.** This is an extraction. Section 1 through Section 4 stay inside Wach's own framework and vocabulary. Section 5 (comparison) and Section 7 (gaps) are the only places where the synthesis-debate vocabulary is reintroduced.

---

## 1. The Bayesian-morphism framework as stated

### 1.1 Symbols and the LBS object

The draft defines a learning-based system (LBS) and its associated objects in `notation.tex` and at lines 135-148 of `main.tex`.

| Symbol | Meaning |
|---|---|
| `S` (`\sys`) | The full LBS under development, hardware plus learning algorithm |
| `S_1, S_2, S_3, ...` | Iterations of the LBS across the lifecycle, e.g., digital model, prototype, fielded system |
| `C` (`\env`) | A closed context |
| `C_1, C_2, ...` | Distinct closed contexts, e.g., digital model context, early prototype context, real operational context |
| `X` (`\st`) | Inputs (positions, target type, lighting, weather, etc.) |
| `O(X)` (`\obs(\st)`) | Observation of input X (camera, sensor, hardware-mediated) |
| `Y` (`\oc`) | Output of a given system in a given context |
| `F` (`\ocf`) | The function inherent in the LA |
| `sigma` (`\structpres`) | Structural preservation, the degree of homomorphism |
| `D` (`\behavpres`) | Behavioral preservation, output distance |

The bullet list at lines 137-143 establishes that the LBS, the closed context, the inputs, the observations, and the outputs are all named first-class objects.

### 1.2 The output equation: explicit dependence on both system and context

Equation (1) of the draft (line 145, `\eqref{eq:la}`) is the load-bearing definitional equation for the framework. Verbatim:

> Y = F_S ( O_{C, S} (X) )

with the prose at line 148: "where the subscripts S and C denote dependence on the system and context, respectively."

This single equation already commits the framework to the position that **outputs depend on both system and context**, not just on system. The notation `F_S` carries the system index, and `O_{C, S}` carries both the context index and the system index. The input X is exogenous to both. This makes the role of context explicit at the object level: a different C with the same S can produce a different Y, because the observation pipeline is different.

This is item (6) of the brief's preliminary read confirmed.

### 1.3 The hierarchy of system specifications

Section 4.1 (`sec:se:theory`, lines 159-202) introduces the formal apparatus. The draft positions itself in the Wymorian Systems Engineering (WySE) Metamodel lineage and treats system morphisms as the central mathematical mechanism (line 161).

Two levels of the hierarchy are pulled out:

**The level of least knowledge (line 167-173).** Equation (2), `\eqref{eq:io}`:

> IO = (T, X, Y)

where IO is the Input/Output Observation Frame, T is the time base, X is the input values set, and Y is the output values set. The associated I/O Observation Frame Morphism relates two systems IO = (T, X, Y) and IO' = (T', X', Y') via functions g and k: g maps input segments from the primed system to input segments of the unprimed, and k maps output segments onto the primed output space.

**The level of most knowledge (line 175-185).** Equation (3), `\eqref{eq:N}`:

> N = (T, X_N, Y_N, D, {M_d}, {I_d}, {Z_d})

where N is a coupled system (network of systems), with external inputs, external outputs, component reference set D, component I/O systems M_d, influencer sets I_d, and interface maps Z_d. The associated Coupling Morphism, equation (4), `\eqref{eq:coord}`:

> < coord, k_d', g_d', h_d' >

satisfying coupling preservation, state-transition preservation, and input/output preservation. The component map `coord` is onto.

The prose at line 187 acknowledges that "the approximate morphism enables a realistic search for neighborhoods of morphisms: an error that does not grow may generally be perceived as acceptable." Cited to Zeigler 2018. This is item (5) of the brief's preliminary read confirmed: morphisms in this framework are not exact correspondences; they are neighborhoods of approximation. The citation lineage is Zeigler 2018 with extension to the hierarchy via Zeigler 2023.

### 1.4 The two-axis degradation framework: (sigma, D)

Section 4.1.1 (`sec:se:twoaxis`, lines 189-198) is the formal definition of the two-axis framework. Verbatim:

> 1. **Structural preservation** sigma (degree of homomorphism): the average reciprocal mapping cardinality across states, inputs, and outputs. For an isomorphism, sigma = 1; as abstraction increases (many-to-one mappings), sigma < 1.
> 2. **Behavioral preservation** D (output distance): D = max_t |Y_1(t) - Y_2(t)|. For an isomorphism, D = 0; discretization or approximation increases D.

The prose at lines 197-198 emphasizes orthogonality:

> These axes are orthogonal: a morphism may have perfect structural preservation (sigma = 1) but poor behavioral preservation (D >> 0), or vice versa. Both must be specified to fully characterize a morphic relationship. An isomorphism is the special case (sigma = 1, D = 0); all other morphisms are approximate equivalences with quantified degradation.

This is the structural/behavioral pair as defined in the draft. The notation maps cleanly: `\structpres = sigma` and `\behavpres = D`. The lineage citation is Wach and Sandman 2026 (CSER 2026 isomorphism library paper).

### 1.5 Three structural facts about the hierarchy

Line 200 contains three claims about the relationship between the IO and N levels that are load-bearing for what follows:

> First, the relationship between the IO observation frame and coupled systems is one-to-many: one IO specification can lead to many N specifications. Second, a morphism at the IO level does not guarantee a morphism at the N level. Third, a morphism at the N level implies a morphism at the IO level.

These three facts establish that the two levels are not coextensive: IO is a strictly weaker fiber over the system specification space than N is. This matters for the morphic chain (Section 1.6 below).

### 1.6 The morphic chain

Line 202, verbatim:

> The systems theoretic framing effectively forms a morphic chain enabled through mathematical characterization of equivalence. Within each link of the morphic chain is a pair of IO (e.g., development context and operational context), a pair of N (e.g., prototype and final product), and a pair of IO with N. Each link carries its own (sigma, D) characterization of morphism quality.

This is the central architectural claim. A single link of the morphic chain contains:

- A pair of IO observation frames, i.e., a pair of contexts.
- A pair of N coupled systems, i.e., a pair of systems.
- A pair of (IO, N) bindings, i.e., the system-context coupling on each side.

Each of these pairs is mediated by a morphism, and each morphism carries its own (sigma, D). The chain is built by concatenating such links across the lifecycle.

### 1.7 The quad relationship

Section 4.2 (`sec:se:lbs`, lines 204-219) names the quad explicitly. Lines 206-208, verbatim:

> Consider the following example: a real operational context and its surrogate development context could both be specified based on (1), with the IO observation frame morphism used to characterize equivalence in the exogenous conditions. The final product and surrogate system model could be specified based on (3), with the network of systems morphism used to characterize equivalence. The mathematical mechanisms form the quad relationship shown in Figure 2, which serves as the basis for the dynamic morphic chain-link.

The caption of Figure 2 (`fig:morphisms`, lines 210-215) is the most concise statement of the quad. Verbatim:

> Metamodel of systems theoretic framing for learning-based systems. The quad relationship maps to the two-axis framework: context morphisms (top) are characterized by (sigma_C, D_C) and system morphisms (bottom) by (sigma_S, D_S).

This is item (1) of the brief's preliminary read confirmed, verbatim, in the published figure caption. The framework distinguishes:

- **Context morphisms (top of the quad)** characterized by **(sigma_env, D_env)** in the brief's notation. The LaTeX writes these as `(\structpres_\env, \behavpres_\env)` which renders as (sigma_C, D_C) given the macro `\env = C`.
- **System morphisms (bottom of the quad)** characterized by **(sigma_sys, D_sys)** in the brief's notation. The LaTeX writes these as `(\structpres_\sys, \behavpres_\sys)` which renders as (sigma_S, D_S).

Line 217, verbatim continuation:

> In Figure 2, we show the real mission (top left) and preservation of equivalence to surrogate context (top right). We show the fielded system (bottom left) and preservation of equivalence to surrogate models (bottom right). Each arrow in the quad now carries a (sigma, D) pair that quantifies the morphism quality for that link. These values directly parameterize the conditional probabilities in the Bayesian network described in Section 5: higher morphism quality (larger sigma, smaller D) implies stronger correlation between system outputs, while degraded morphisms (smaller sigma, larger D) increase uncertainty.

The quad has four arrows in the figure (one per corner-to-corner edge). The text at line 217 says "each arrow in the quad now carries a (sigma, D) pair," not "the quad carries two (sigma, D) pairs total." The figure caption is the cleaner statement: top context-morphism arrows are (sigma_env, D_env), bottom system-morphism arrows are (sigma_sys, D_sys). Both readings are present in the source.

### 1.8 Where the Bayesian network meets the morphism chain

Section 5 (`sec:bayes`, lines 224-281) lifts the morphic chain to a Bayesian network. Line 228:

> A natural approach to modeling correlation between confidence in models across the morphisms described in the previous section is via Bayesian networks (Salado 2018a; Xu 2023). A Bayesian network is a directed acyclic graph (DAG) model that describes the relationship between nodes representing random variables via conditional probabilities (the graph edges).

The construction (line 236):

> To apply the Bayesian network to the WySE Metamodel, we use nodes to represent system states at different points in the morphic chain. Figure 4 provides an example with three alternate systems, representing, e.g., a simulation model, a hardware prototype, and the fielded system, each related to the Context.

This is item (3) of the brief's preliminary read confirmed: Bayesian network with nodes for system states; edges parameterized by morphism quality. Section 5.3 (Prediction via Bayesian Network, lines 269-281) makes the parameterization explicit. Verbatim, line 279:

> The conditional probability Prob(Y_j | Y_i, C) is parameterized by the morphism quality (sigma, D) between systems i and j. Higher morphism quality (larger sigma, smaller D) implies that the conditional probability concentrates near the identity mapping (outputs are highly correlated), while lower morphism quality spreads the conditional probability (outputs are less predictable from one another).

### 1.9 The framework as a single picture

Putting the pieces together, the draft commits to the following architecture:

1. The output of an LBS is a function of both system and context, equation (1).
2. The system has two levels of specification: IO (least knowledge) and N (most knowledge), equations (2) and (3).
3. Equivalences at each level are characterized by morphisms, with the I/O Observation Frame Morphism at the IO level and the Coupling Morphism at the N level (equation (4)).
4. Each morphism is characterized by a structural-behavioral pair (sigma, D).
5. The morphism universe contains two kinds of morphism that are categorically distinct: I/O observation frame morphisms (context morphisms) and N coupling morphisms (system morphisms). They live at different levels of the hierarchy and one-way implication holds (N-morphism implies IO-morphism, not vice versa, line 200).
6. A single link of the morphic chain contains a context-morphism pair (sigma_env, D_env) and a system-morphism pair (sigma_sys, D_sys); these two pairs together quantify equivalence of the development-stage diagram to the next-stage diagram (line 202).
7. The morphic chain composes such links across the lifecycle (development -> prototype -> fielded).
8. A Bayesian network is layered on top, with system states as nodes and edges parameterized by the (sigma, D) of the corresponding morphism (line 279).
9. The Bayesian network supports prediction, via marginalization, of higher-fidelity performance from lower-fidelity test data (equation (8), `\eqref{eq:predict}`, line 273).

---

## 2. Formal context treatment in the draft

This section answers the brief's question 2: what does the draft already say about context, formally?

### 2.1 Context is a closed observation frame

Section 3 (`sec:lbs`, lines 127-152) introduces context as a first-class object. Line 138:

> Closed contexts are denoted by C_1, C_2, ... For example, C_1 might be a purely digital model context, C_2 might be an early prototype context, and C_3 might be a real (e.g., live-fire) operational context.

The block diagram (`lbs_diagram.tex`, line 38) renders C as a box surrounding the input X, the hardware-LA system S, and the output Y, labeled "Closed Context C." The draft's notion of context is that of a closed observation frame: the boundary of the box defines what is in-context, and the inputs X are themselves derived from variables internal to the context (positions, target type, lighting, weather).

The closed-context construction is what the draft means by "context." It is not a parameter; it is a structured object that contains the system and the inputs the system sees. This already encodes the key claim that context is a diagram, not a parameter.

### 2.2 The IO observation frame is the formal home of context

The IO specification, equation (2):

> IO = (T, X, Y)

is the formal home of context. The text at line 167 calls this "the level of least knowledge, in which we only have knowledge of external interactions." This is the formal specification of what the LBS sees from the outside, time base plus input alphabet plus output alphabet.

Section 4.2, line 206, makes the binding explicit:

> a real operational context and its surrogate development context could both be specified based on (1), with the IO observation frame morphism used to characterize equivalence in the exogenous conditions.

The IO observation frame is the context, in the formal sense the draft uses. Two contexts are compared by an IO observation frame morphism. This is item (1) of the preliminary brief confirmed at the formalism level: I/O observation frame morphisms are context morphisms.

### 2.3 The pair of mapping functions for an IO morphism

At line 173, the I/O observation frame morphism is given concretely:

> we relate two systems IO = (T, X, Y) and IO' = (T', X', Y') by defining functions: g : (X', T') -> (X, T) derives a segment over X given a segment over X', and k : (Y, T) -> onto (Y', T') derives an output segment over Y' given an output segment over Y.

This is the set-theoretic content of an IO morphism. g pulls inputs back; k pushes outputs forward. The morphism is onto on the output side. This morphism is what carries the context-morphism quality pair (sigma_env, D_env): structural preservation is computed by the average reciprocal mapping cardinality of g and k, behavioral preservation is computed by the max-time output distance on Y.

### 2.4 Context morphism vs system morphism: the categorical distinction

The draft does not use the word "categorical" but it does maintain a strict separation between two kinds of morphism. Line 202 lists the contents of a single morphic chain link:

> a pair of IO (e.g., development context and operational context), a pair of N (e.g., prototype and final product), and a pair of IO with N.

The "pair of IO" is the context-morphism part of the link. The "pair of N" is the system-morphism part of the link. The "pair of IO with N" is the system-in-context binding on each side. The link is thus a 4-tuple of pairs, and the link's quality is characterized by the (sigma, D) of each constituent morphism.

The implication asymmetry (line 200, third bullet) is the key categorical fact: a morphism at the N level implies a morphism at the IO level, but not vice versa. This means context morphisms are weaker than system morphisms in the technical sense. A pair of systems can have valid IO morphism (matching exogenous conditions) without having a valid N morphism (matching internal coupling). The converse fails. Operationally: changing context affects what input segments are seen, but does not by itself constrain the internal-coupling story of the system.

### 2.5 The morphic chain across development, prototype, fielded

The lifecycle reading is given at lines 137-138, the bullet list of `S_1, S_2, S_3` and `C_1, C_2, C_3`, and at line 236, where the Bayesian network is described as having "three alternate systems, representing, e.g., a simulation model, a hardware prototype, and the fielded system, each related to the Context."

The chain across the lifecycle is:

- Link 1: (C_1, S_1) -> (C_2, S_2). Context morphism IO_1 -> IO_2 carries (sigma_env^{12}, D_env^{12}). System morphism N_1 -> N_2 carries (sigma_sys^{12}, D_sys^{12}).
- Link 2: (C_2, S_2) -> (C_3, S_3). Context morphism IO_2 -> IO_3 carries (sigma_env^{23}, D_env^{23}). System morphism N_2 -> N_3 carries (sigma_sys^{23}, D_sys^{23}).

Each link is a quad with its own four (sigma, D) pairs (one per arrow in the quad). The morphic chain is built by composition of links.

The draft does not formally state a chain composition law for context-morphism quality. The system-morphism chain composition is implied by composition of homomorphisms; the context-morphism chain composition is parallel but not explicit. This is a gap (Section 7).

### 2.6 Bayesian propagation of confidence

Section 5.3 (lines 269-281) gives the prediction equation. Equation (8), `\eqref{eq:predict}`:

> Prob(Y_j = Y | C) = sum over Y' of Prob(Y_j = Y | Y_i = Y', C) * Prob(Y_i = Y' | C)

This is the marginalization identity for the joint over (Y_i, Y_j | C). It propagates the marginal distribution of system i (estimated from lower-fidelity testing) to the marginal distribution of system j (predicted for higher-fidelity performance) via the conditional Prob(Y_j | Y_i, C). The conditional is parameterized by the morphism quality (sigma, D) between systems i and j (line 279).

In the morphic-chain reading, propagation along a chain of two links chains the prediction equation:

> Prob(Y_3 | C) = sum_{Y_2, Y_1} Prob(Y_3 | Y_2, C) Prob(Y_2 | Y_1, C) Prob(Y_1 | C)

This is the inferential mechanism that turns morphism-quality numbers into a confidence-propagation calculation. The draft demonstrates this for one link (YOLO clear -> YOLO blurred) in Section 6.

### 2.7 d-separation handling of full and partial context

Section 5.2 (`sec:bayes:ci`, lines 238-258) is the most rigorous part of the draft. It is explicitly grounded in Pearl 2009 d-separation theory.

**Full context (lines 242-247).** Verbatim:

> When the context variable C includes all variables affecting system outputs, target type, position, orientation, lighting, weather, camera angle, scene complexity, and so forth, then for any two systems i and j in the network, knowledge of C renders Y_i and Y_j conditionally independent: Y_i perp Y_j | C_full. This follows from d-separation: in the DAG, all paths between Y_i and Y_j pass through C_full; conditioning on C_full blocks every such path.

Equation (6), `\eqref{eq:ci}`: `Y_i perp Y_j | C_full`.

**Partial context (lines 249-258).** Verbatim:

> In practice, only a subset of context variables are observed. Let C_obs denote the observed context (e.g., target presence/absence) and let E denote the unobserved shared variables (e.g., lighting, weather, camera angle, scene complexity). Marginalizing over E induces conditional dependence between system outputs: Y_i not-perp Y_j | C_obs. This is because the path Y_i <- E -> Y_j remains active when E is unobserved.

Equation (7), `\eqref{eq:cd}`: `Y_i not-perp Y_j | C_obs`.

The latent-variable DAG figure (`network_latent.tex`) gives the explicit ancestral graph: a node `C_obs` (observed context) and a separate dashed node `E` (latent context variables). Both `C_obs` and `E` have arrows into both system outputs `Y_1` and `Y_2`. The dashed-box convention for E follows the ancestral graph framework of Richardson and Spirtes (cited in the text).

The draft's diagnostic claim at line 258 is load-bearing:

> We argue that this is the typical and more realistic model for practical V&V, because controlling for all variables affecting system output is rarely feasible. We should expect, due to similar hardware, software, or algorithmic components, the outputs for different system iterations to be correlated. All references to the Context that follow should be understood as partial context.

This is item (4) of the brief's preliminary read confirmed in full rigor. The draft treats partial context as the default operational case, not as a limiting case.

### 2.8 Explicit treatment of "context change" or "deployment context shift"

Section 3 (line 152) and Section 6 (Section 6.1) explicitly motivate the framework by deployment shift:

> It is therefore essential to characterize the differences between the data that the LA is trained on and the data that it will see in the full mission context. For example, differences between the training data context and a physical context might include time of day, time of year, and weather. Differences between training and physical systems might include image resolution and image angle.

The framework's name for the deployment-shift quantity is the (sigma_env, D_env) on the context morphism between the training context and the operational context. The draft does not introduce a separate name (no "D_r," no "shift" symbol); the existing context-morphism quality pair is the deployment-shift measurement.

The YOLO example operationalizes one slice of this: the clear-image context vs the blurred-image context is a context shift. The conditional probabilities `Prob(Y_B | Y_C, C)` are the empirical realization of the link quality between the two contexts. The morphism-quality language in Section 4 is the theoretical scaffolding; the conditional-probability table in Section 6 is its empirical instantiation.

### 2.9 Summary of the formal context construct

The draft's formal definition of context, distilled:

> Context is the IO observation frame `IO = (T, X, Y)` over which a system is specified. Two contexts are compared by an IO observation frame morphism, with maps g (input pullback) and k (output pushforward), characterized by a structural-behavioral quality pair (sigma_env, D_env). The closed context `C` is the visual rendering of the IO frame plus the system situated inside it. In the Bayesian network, context appears as a node `C` (full or observed) on which all system-output nodes are conditioned; the d-separation status of `C` determines whether system outputs are conditionally independent (full context) or conditionally dependent (partial context). The partial-context case is the default for practical V&V.

This is what the draft already does. It is a substantial construct.

---

## 3. Quad relationship and morphic chain

The brief asks for explicit extraction of the quad and the chain. They were sketched in Section 1 above. This section is a dedicated formal restatement.

### 3.1 The quad as a four-arrow diagram

Figure 2 of the draft (`fig:morphisms`) shows a square diagram with four corners and four arrows. The four corners are:

- **Top-left:** Real mission context, denoted `C_real` or `C_1`. Specified at the IO level: `IO_real = (T, X_real, Y_real)`.
- **Top-right:** Surrogate development context, denoted `C_dev`. Specified at the IO level: `IO_dev = (T, X_dev, Y_dev)`.
- **Bottom-left:** Fielded system, denoted `S_real` or `S_fielded`. Specified at the N level: `N_real`.
- **Bottom-right:** Surrogate system model, denoted `S_dev`. Specified at the N level: `N_dev`.

The four arrows are:

- **Top arrow** (C_real <-> C_dev): IO observation frame morphism, the context morphism. Quality pair: (sigma_env, D_env).
- **Bottom arrow** (S_real <-> S_dev): Coupling morphism, the system morphism. Quality pair: (sigma_sys, D_sys).
- **Left arrow** (C_real -> S_real): The binding of the fielded system into the real mission context.
- **Right arrow** (C_dev -> S_dev): The binding of the surrogate system into the surrogate development context.

The two horizontal arrows are the morphism pair the framework cares about for V&V. The two vertical arrows are the system-in-context bindings. Together, the four arrows form a commuting square in the sense that the diagram's commutativity is what is being characterized; the (sigma, D) quality pairs are the degradation of commutativity.

### 3.2 Why "quad" and not "pair"

The draft's wording at line 202 is precise:

> Within each link of the morphic chain is a pair of IO (e.g., development context and operational context), a pair of N (e.g., prototype and final product), and a pair of IO with N.

A pair of IO + a pair of N + a pair of (IO, N) bindings = three pairs = six items, arranged as a quad (4 corners, 4 arrows). The morphism universe inside one link contains two morphisms: the context morphism (top) and the system morphism (bottom). Each carries its own (sigma, D). The link is fully characterized by these two (sigma, D) pairs together with the diagram structure that places them in relation.

This is materially the bifunctor reading the categorical investigator in the synthesis-debate document arrived at independently (synthesis debate, Section 4 Disagreement 2, on the bifunctor character of the contextual gap). The draft expresses it set-theoretically rather than via fibrations, but the structural claim is the same: the contextual gap is a property of a diagram with two distinguished morphisms, not of a single arrow.

### 3.3 The chain as composition of quads

The morphic chain across the lifecycle is built by composing quads. Define link `L_k` as the quad at lifecycle stage transition `k -> k+1`:

- Top arrow of `L_k`: context morphism from `IO_k` to `IO_{k+1}`, quality (sigma_env^{k,k+1}, D_env^{k,k+1}).
- Bottom arrow of `L_k`: system morphism from `N_k` to `N_{k+1}`, quality (sigma_sys^{k,k+1}, D_sys^{k,k+1}).
- Left arrow: system-in-context binding at stage k.
- Right arrow: system-in-context binding at stage k+1.

The chain `L_1 ; L_2 ; ... ; L_{n-1}` is the composition of these quads, with the right edge of `L_k` glued to the left edge of `L_{k+1}`. The endpoints of the chain are `(C_1, S_1)` and `(C_n, S_n)`.

The draft does not give a chain-composition formula for (sigma, D). It says the chain "carries" the per-link pairs (line 202) and that the conditional probabilities propagate via equation (8) (line 273). Chain composition of the (sigma, D) numbers themselves is implicit in the inheritance of homomorphism composition properties but is not stated. This is the closest the draft comes to a gap on the chain side (Section 7).

### 3.4 Relationship of the quad to the Bayesian network

Section 5 lifts the quad to the Bayesian network as follows. The four corners of the quad become network nodes (with the two contexts collapsed into a single `C` node in the typical drawing, and the two systems as separate `Y_i` nodes). The two horizontal morphisms become network edges with conditional probabilities parameterized by their (sigma, D) pairs. The two vertical bindings are encoded by the conditioning relation `Prob(Y_i | C)` on each side.

Concretely (cf. `network_yolo.tex`):

- A context node `C` (Context, partial in the typical case).
- A system-state node `Y_C` (Clear).
- A system-state node `Y_B` (Blur).
- Edge from C to Y_C carrying `Prob(Y_C | C)`.
- Edge from C to Y_B carrying `Prob(Y_B | C)`.
- Edge from Y_C to Y_B carrying `Prob(Y_B | Y_C, C)`.

The third edge (Y_C -> Y_B) is the system-morphism edge: it is parameterized by the system-morphism quality (sigma_sys, D_sys). The other two edges (C to Y_C and C to Y_B) are the binding edges: they encode `Prob(Y_i | C)` from the partial-context d-separation analysis of Section 2.7. There is no edge in the Bayesian network corresponding to the context morphism itself, because in this drawing both Y_C and Y_B share the same `C` node (the context-pair has been collapsed by conditioning on a single observed context).

In a richer drawing with two contexts (training context vs operational context), there would be edges between context nodes parameterized by the context morphism's (sigma_env, D_env). The draft's typical figure simplifies by collapsing to one context, but the underlying quad has two contexts.

### 3.5 Quad implications for V&V

The two-axis quad gives a vocabulary for V&V trade-offs:

- A simulation model with high system-morphism quality (high sigma_sys, low D_sys) but low context-morphism quality (low sigma_env, high D_env) is a faithful model of an irrelevant context. Most "lab vs operational" failures live here.
- A scenario test with high context-morphism quality (real operational data) but low system-morphism quality (different hardware coupling) is a relevant test of a wrong system. Most "wrong-prototype" failures live here.
- The Bayesian network's predictive accuracy depends on both pairs being faithfully characterized.

The draft does not break out this two-by-two diagnostic explicitly. It is implicit in the figure-2 caption ("higher morphism quality implies stronger correlation; degraded morphisms increase uncertainty"). This is a productive elaboration the draft enables but does not fully develop (Section 7).

---

## 4. Bayesian network and d-separation for partial context

This section restates the d-separation treatment formally and notes what it does and does not commit to.

### 4.1 The two cases formally

**Case A (full context).** All variables affecting `Y_i` and `Y_j` are observed and included in the context variable `C`. The DAG has:

- A single context node `C` (full).
- System-state nodes `Y_i` for each system in the chain.
- Arrows from `C` to each `Y_i`.
- No arrows between `Y_i` and `Y_j`.

d-separation result: `Y_i perp Y_j | C` for any i, j. Equation (6).

**Case B (partial context).** Only a subset `C_obs` is observed; latent variables `E` (lighting, weather, camera angle, scene complexity) are unobserved. The DAG has:

- An observed context node `C_obs`.
- An unobserved (dashed) latent node `E`.
- System-state nodes `Y_i`.
- Arrows from both `C_obs` and `E` to each `Y_i`.

d-separation result: `Y_i not-perp Y_j | C_obs`. Equation (7). The path `Y_i <- E -> Y_j` is active because E is not in the conditioning set.

The latent-variable DAG figure (`network_latent.tex`) shows two systems Y_1 and Y_2 with both `C_obs` (solid) and `E` (dashed) as parents. The figure annotation at line 33-36 makes the active path explicit.

### 4.2 Operational consequence

The draft commits to the partial-context model as default (line 258). The Bayesian network for V&V therefore has edges between system-state nodes; these edges encode the conditional dependence induced by shared latent context. The edges are NOT artifacts of d-separation failure; they are the correct model for the realistic case where context cannot be fully observed.

The right-hand panel of Figure 4 (`network_full_connected.tex`) is the operational form of the network: a partial-context root, three system-state nodes Y_1, Y_2, Y_3, all conditioned on the context, plus inter-system edges Y_1 -> Y_2 and Y_2 -> Y_3. The chain edges Y_1 -> Y_2 -> Y_3 are the morphism-quality edges.

### 4.3 The role of (sigma, D) in the conditional probability

Line 279, verbatim:

> Higher morphism quality (larger sigma, smaller D) implies that the conditional probability concentrates near the identity mapping (outputs are highly correlated), while lower morphism quality spreads the conditional probability (outputs are less predictable from one another).

The draft does not specify the functional form. It does not say `Prob(Y_j = y | Y_i = y', C) = f(sigma, D, y, y')` for a specified f. It commits only to a monotonic relationship: higher quality means more concentration near the identity. Producing a specific functional form (e.g., a Gaussian with variance set by D and concentration parameter set by sigma) is outstanding work.

The YOLO example treats the conditional probabilities as empirically estimated counts (Tables 1-3) rather than as derived from (sigma, D) values. The morphism-quality language and the empirical-probability language are formally separate in the current draft.

### 4.4 What the d-separation treatment commits to

The d-separation treatment:

1. Names the full-vs-partial-context distinction as a formal property of the DAG.
2. Identifies partial context as the realistic default.
3. Identifies shared unobserved latent variables (lighting, weather, camera angle, scene complexity) as the mechanism by which system outputs become conditionally dependent.
4. Endorses the connected-systems Bayesian network (right panel of Figure 4) as the appropriate model for practical V&V.

It does not:

1. Specify what variables go into `E` for a given application beyond illustrative examples.
2. Provide a procedure for elevating variables from `E` to `C_obs` as more is observed.
3. Quantify the strength of the induced dependence (the conditional dependence is qualitative, not quantitative).
4. Connect the latent-variable structure to the morphism-quality (sigma, D) construct.

The fourth point is the most important gap: the d-separation analysis lives at the Bayesian-network level, and the (sigma, D) construct lives at the morphism level, and the draft does not formally bind them. The conditional probability `Prob(Y_j | Y_i, C)` carries the (sigma, D) parameterization, but the latent-variable structure that induces this conditional probability in the first place is left as a generic Pearl-style construction.

---

## 5. Comparison to the prior synthesis (layer by layer)

The brief asks for an explicit per-layer comparison. The prior synthesis (synthesis_debate.md, Section 5) proposed a five-layer stack. Each is tested against the draft.

### 5.1 Layer 1: Wymore-A, declared assertion domain `Dom(h)`

**Synthesis-debate claim.** Every certified morphism `h` carries an explicit declaration of `Dom(h_cert) = (Q_cert, I_cert', O_cert')`. Set-theoretic. Out-of-context is a Boolean precondition violation.

**Status in the draft.** Implicitly present, not explicitly named.

The IO observation frame `IO = (T, X, Y)` (equation 2) is functionally identical to a declared assertion domain on the input side: T and X are exactly the time base and input set over which the morphism is asserted, which is the IO-side analog of `(Q_cert, I_cert')`. The N-level specification (equation 3) adds the state-space and coupling structure analogous to `Q_cert`. Together, the IO and N specifications carry the declared-domain information.

The draft does NOT make this a separate certification-artifact declaration. The IO and N specifications are the system specifications themselves, not separate artifacts attached to the morphism. The Wymore-A move of distinguishing `Dom(h)` from `h` is not present.

The Wymore-A predicate `q in Dom(h_cert)` is also not present as a runtime check. The draft frames operational deployment as a Bayesian inference problem over a partial-context graph, not as a domain-membership test followed by a metric-degradation measurement. The Wymore-A precondition logic is a different operational mode than the Bayesian-marginalization logic of the draft.

**Verdict.** Wymore-A is **partially present in different vocabulary.** The IO/N specifications carry the same set-theoretic content as `Dom(h)`. The artifact-level distinction Wymore-A makes (`Dom(h)` is a separate declared artifact) and the Boolean precondition test (`q in Dom(h)`) are not in the draft. **Adding Wymore-A on top of the draft would require declaring `IO_cert` and `N_cert` as separate certification artifacts and instituting a runtime domain-membership test.** This is additional engineering, not new mathematics.

### 5.2 Layer 2: DEVS/Experimental Frame decomposition (G, A, T)

**Synthesis-debate claim.** Context decomposes operationally into the EF triple `E = (G(E), A(E), T(E))`: generator, acceptor, transducer. Context distance is `d_EF = (d_G, d_A, d_T)`. The continuous-coverage indicator `C_env` is the graded acceptor `A_graded`.

**Status in the draft.** Subsumed by the IO observation frame at the formal level, **not decomposed** at the operational level.

The IO observation frame `IO = (T, X, Y)` is the Wymorian-level analog of the EF. The DEVS investigator argued (synthesis debate, Section 3) that an EF is itself a Wymore system; the Wach-Zeigler-Salado 2021 bridge gives the formal link. Wach 2021 is `wach2021conjoining` in the draft's bibliography; the draft cites it as the Wymore-DEVS bridge (line 161, line 165). The draft sits in this bridged tradition.

The EF triple's three components (G, A, T) are NOT broken out in the draft. The draft has:

- The input set X (in `IO = (T, X, Y)`). This is the analog of G (the admissible-input generator).
- The output set Y. This is the carrier on which T (the transducer) operates; the draft does not compute statistics on Y as a transducer would.
- No acceptor. The draft has no predicate over observed trajectories that maps to "in-frame" vs "out-of-frame."

The d_G / d_A / d_T decomposition of context distance into three orthogonal components is not in the draft. The draft uses the two-axis (sigma_env, D_env) on the IO morphism, which is structurally one component (sigma_env on the maps g and k, behaviorally D_env on the output space Y). The structural/behavioral decomposition is orthogonal to the G/A/T decomposition.

The graded-acceptor `A_graded` (continuous coverage) construction is not present.

**Verdict.** Layer 2 is **partially subsumed and partially absent.** The IO frame is the EF at the level of Wymore vocabulary; the bridge to DEVS is acknowledged. The G/A/T decomposition into three context-distance components is not present and would be additional construct work. Whether this work is worth doing depends on whether the (sigma_env, D_env) pair on the IO morphism captures enough of what G/A/T would capture; the draft does not address this question.

### 5.3 Layer 3: Wymore-B, parameter family / inter-fiber morphism

**Synthesis-debate claim.** The certified system is one fiber `Z_real(c_cert)` of a family `{ Z_real(c) | c in C }`. Deployment failure is captured by an inter-fiber morphism `g: Z_real(c_cert) -> Z_real(c_op)`, measured by `(D_s(g), D_b(g))` using the existing two-axis machinery. The "third quantity" is the same first two quantities applied to a second arrow.

**Status in the draft.** **Present in essentially this form, expressed set-theoretically with closed contexts rather than fibers.**

The draft's closed-context family `{C_1, C_2, C_3, ...}` indexed by lifecycle stage is functionally a fiber family. The context morphism between IO_i and IO_j is the inter-fiber morphism. The (sigma_env, D_env) quality pair on this context morphism is exactly the "first two quantities applied to a second arrow."

The draft's morphic chain link contains both the inter-fiber context morphism (top of the quad) and the within-fiber system morphism (bottom of the quad). The synthesis debate's Layer 3 considered only the inter-fiber direction. The draft is more general: it has both directions in one link.

Where the synthesis debate is set-theoretic (parameter family) and the categorical version is fibered, the draft is closed-context-set-theoretic. These three vocabularies describe the same construction; the draft's choice is the closest to the categorical investigator's recommendation for the design spec ("keep the operational construct set-theoretic," synthesis debate Section 4 Disagreement 4 adjudication).

**Verdict.** Layer 3 is **already present in the draft in the form of the context morphism (top of the quad).** The (sigma_env, D_env) is exactly the "first two quantities applied to a different arrow." The draft is more general than Layer 3 by also carrying the within-fiber system morphism explicitly.

This is the most important finding. Layer 3 of the synthesis debate, which was identified as the operationally adequate construct for the AI Circuit Breaker design spec, is already in the draft.

### 5.4 Layer 4: Friston / Markov blanket, distributional axis

**Synthesis-debate claim.** Add a distributional axis `sigma_dist` (Friston-style free energy or distributional divergence) orthogonal to the structural axis `sigma_struct`. Together they form a two-axis context-match construct `Sigma_ctx = (sigma_struct, sigma_dist)`.

**Status in the draft.** **Absent. The distributional axis is genuinely not in the draft.**

The draft's two axes are structural and behavioral (sigma, D). Both are about morphism-level preservation: sigma is structural preservation of mappings (cardinality of preimages), D is behavioral preservation of outputs (max-time output distance). Neither is distributional in the sense of measuring divergence between input distributions.

The Bayesian network does carry distributional content via the conditional probabilities `Prob(Y_j | Y_i, C)` and the marginals `Prob(Y_i | C)`. But these are at the network level, not as a property of the morphism. The morphism-quality pair (sigma, D) does not include a measure of how `Prob(X | C_op)` differs from `Prob(X | C_cert)`.

The latent-variable construction (`E` in Section 5.2 of the draft) does carry implicit distributional content: the partial-context dependence between `Y_i` and `Y_j` is mediated by the distribution of `E`. But the draft does not extract a distributional quantity from this; it leaves the latent variables qualitative.

**Verdict.** Layer 4 is **absent.** Adding a distributional context-match coordinate to the existing structural-behavioral pair would be new construct work. The draft's Bayesian layer already has distributions; what is missing is a morphism-level distributional invariant.

The synthesis debate identified this as the "genuinely new construct work, not a re-presentation of existing mathematics" (Section 4 Disagreement 3 adjudication). The draft confirms the diagnosis.

### 5.5 Layer 5: Rosen modeling relation, diagrammatic lineage

**Synthesis-debate claim.** Acknowledge that the (D_s, D_b) construct sits on a Rosen-shaped modeling-relation diagram; the degree-of-homomorphism is a commutation defect in Rosen's sense. Cross-disciplinary lineage acknowledgment with no new mathematics.

**Status in the draft.** **Absent at the explicit citation level.**

The draft does not cite Rosen. The lineage citations in Section 4 are Wymore (wymore1967mathematical, wymore1993modelbased), Zeigler (zeigler2018theory, zeigler2019theory, zeigler2023extending), and Wach (wach2021conjoining, wach2026isomorphism, wach2025slr). The von Bertalanffy citation (`von1974general`) opens Section 4 at the general-systems-theory level.

The Rosen modeling-relation diagram (encoding, decoding, natural causation, formal inference, commutation condition) is structurally present in the WySE Metamodel formalism but is not named as such. The system-morphism diagram between `S` and a surrogate `S'` is a Rosen-style commuting square in everything but vocabulary.

**Verdict.** Layer 5 is **absent at the citation level**, structurally implicit. Adding it is a small lineage-acknowledgment move with no mathematical content, consistent with the synthesis debate's framing.

### 5.6 Synthesis-debate summary table, reframed

| Layer | Synthesis claim | Status in draft |
|---|---|---|
| 1 (Wymore-A) | Declare `Dom(h)` as certification artifact; Boolean precondition test | Partially present in different vocabulary (IO/N specs carry the set-theoretic content; artifact-level distinction and precondition test not present) |
| 2 (DEVS/EF) | Decompose context distance into `(d_G, d_A, d_T)` | Subsumed at Wymore level (IO frame = EF at that level), not decomposed; graded acceptor absent |
| 3 (Wymore-B / categorical) | Inter-fiber morphism with `(D_s, D_b)` | **Present.** Context morphism (top of the quad) with `(sigma_env, D_env)`. Draft is more general (includes within-fiber system morphism too) |
| 4 (Friston) | Distributional axis `sigma_dist` orthogonal to structural | **Absent.** Morphism-level distributional invariant not present |
| 5 (Rosen / Pattee) | Diagrammatic lineage acknowledgment | Absent at citation level, structurally implicit |

---

## 6. Headline finding

The brief asked for the strongest single claim about how this draft reshapes the D_r question.

**The headline finding.** Paul's already-in-revision Bayesian SE for AI draft already carries a two-kind morphism universe inside the WySE Metamodel hierarchy:

- **IO observation frame morphisms**, characterized by **(sigma_env, D_env)**, which formally compare two closed contexts. These are context morphisms.
- **N coupling morphisms**, characterized by **(sigma_sys, D_sys)**, which formally compare two coupled systems. These are system morphisms.

These two kinds of morphism are categorically distinct (line 200: N-morphism implies IO-morphism, not vice versa), live at different levels of the Wymorian hierarchy of system specifications, and form a quad relationship inside a single morphic chain link (line 202, line 213 figure caption). The (sigma, D) two-axis quality pair is applied to each, giving a four-(sigma, D)-pair link.

**Consequence for the D_r question.** D_r, the contextual-gap construct the synthesis debate was scoped to deliver, **already exists in the draft as (sigma_env, D_env) on the IO observation frame morphism.** The synthesis debate's Layer 3 ("the third quantity is the first two quantities applied to a different arrow") is exactly what the draft already does, expressed in the draft's set-theoretic closed-context vocabulary rather than in fibered-category vocabulary.

Therefore the D_r question, as scoped, reduces to a notational-and-architectural integration question:

- **Notational:** decide whether to use the draft's notation `(sigma_env, D_env)` for the context-morphism quality, or to introduce a new symbol (the synthesis debate's `D_r`, the categorical investigator's `D_ctx`, etc.). The draft's notation has provenance in a published paper line (CSER 2025 sigma, CSER 2026 sigma + D, current Wiley/INCOSE revision sigma_env + D_env). Introducing a new symbol breaks this lineage.

- **Architectural:** decide whether the AI Circuit Breaker design spec should adopt the draft's quad-and-chain construction wholesale, or whether some part of the synthesis debate's five-layer stack adds value the draft does not already deliver. The per-layer comparison (Section 5) shows that Layer 3 is present, Layer 1 is partially present, Layer 2 is subsumed at the Wymore level, Layer 5 is a citation-only addition, and **only Layer 4 (distributional axis) is genuinely new construct work** that the draft does not carry.

**The construct-development question therefore largely closes.** What remains is integration into the AI Circuit Breaker design spec and a possible distributional-axis extension. The five investigations the synthesis debate worked from were correct in their diagnoses; the draft already operationalizes the strongest of those diagnoses (Layer 3) in published-paper form.

---

## 7. Gaps and updated recommendation direction

### 7.1 What the draft leaves unfinished on context

Six items the draft does not deliver, in descending order of importance for an AI Circuit Breaker context formalization:

**Gap 1: Distributional axis.** The morphism-quality pair (sigma, D) is structural and behavioral. It does not include a distributional invariant of the input distribution. A context morphism whose maps g, k preserve cardinalities exactly (sigma_env = 1) and whose output behavior is identical (D_env = 0) could still represent a deployment context with a different input distribution than the certified context, and the framework would not register the difference.

This is exactly the gap the synthesis debate's Layer 4 identifies. Closing it requires a distributional invariant attached to the morphism. Candidates: KL divergence on `Prob(X | C)`, total variation, a Friston free-energy reading, conformal-prediction coverage. The draft's bibliography includes `angelopoulos2023conformal`; the discussion section (line 447) names conformal prediction as a "promising direction" for future integration. The conformal-prediction reading is closer to the draft's existing vocabulary than the Friston reading.

**Gap 2: Chain composition law for (sigma, D).** The draft asserts that each link of the morphic chain carries its own (sigma, D) pair (line 202) and that conditional probabilities propagate via marginalization (equation 8), but does not give an explicit composition formula for how (sigma, D) on link `L_1` and (sigma, D) on link `L_2` combine to give (sigma, D) on the composed link `L_1 ; L_2`. The synthesis debate's DEVS section (Section 2.2) sketched a chain-bound theorem with worst-case for d_G, additive for d_A under 1-Lipschitz, worst-case for d_T. The analog for (sigma, D) is the "W26 chain bound theorem" mentioned in the synthesis debate; the draft does not state this bound explicitly. A clear chain-composition law is needed for multi-stage propagation.

**Gap 3: Binding of (sigma, D) to conditional probability functional form.** The draft commits to a monotonic relationship between morphism quality and conditional-probability concentration (line 279). It does not specify the functional form. The YOLO example sidesteps this by estimating conditional probabilities empirically from counts. For the framework to be predictive (rather than self-consistent on existing data), the (sigma, D) values need to determine the conditional probability up to identification. This is a research question, not a definitional gap, but it is open.

**Gap 4: Wymore-A artifact-level declaration and runtime precondition test.** The draft has the set-theoretic content of `Dom(h)` inside its IO and N specifications, but does not separate `Dom(h)` as a certification artifact distinct from `h`, and does not institute a runtime predicate `q in Dom(h_cert)`. For an AI Circuit Breaker design spec, the runtime predicate is exactly the Boolean precondition the breaker would trip on. The draft's framework does not natively support this precondition test; it supports continuous (sigma, D) measurement instead. An AI Circuit Breaker that combines a Wymore-A precondition with a continuous (sigma, D) sensor is a richer instrument than the draft's framework alone delivers.

**Gap 5: Specification of the latent-variable structure E.** The d-separation treatment names latent variables (lighting, weather, camera angle, scene complexity) as the mechanism for partial-context conditional dependence. It does not specify how to identify these for a given application, how to escalate variables from `E` to `C_obs` as more is observed, or how the latent-variable structure connects to the morphism-quality (sigma, D) construct. The connection is conceptually clear (latent E induces conditional dependence between Y_i and Y_j, which raises the off-diagonal of the conditional probability matrix, which corresponds to lower morphism quality), but it is not made formal.

**Gap 6: Two-by-two diagnostic on (sigma_env, D_env) vs (sigma_sys, D_sys).** Section 3.5 above sketches a two-by-two of "faithful model of irrelevant context" vs "wrong system in real context" vs "right system in right context" vs "wrong system in irrelevant context." The framework supports this diagnostic but the draft does not develop it. For practitioners, this is the most immediately usable elaboration the framework enables.

### 7.2 What is in scope for the AI Circuit Breaker context formalization that the draft does not supply

Three additions the AI Circuit Breaker design spec would need on top of the draft:

1. **A precondition test (Wymore-A precondition).** A Boolean predicate `q in Dom(h_cert)` on the live input trajectory, with the breaker tripping on violation. The draft's continuous (sigma_env, D_env) measurement is the "how far outside" quantity; the breaker also needs the "in or out" quantity.

2. **A distributional sensor (Layer 4 distributional axis).** A distributional invariant of the deployment context against the certified context. Candidates include conformal-prediction coverage (closest to the draft's existing vocabulary), KL divergence on input distributions, or free-energy increase (Friston). This is the gap that closes the structural-only character of (sigma, D).

3. **A chain-composition rule.** A formal rule for how `(sigma, D)` on a chain of morphisms combines, so the breaker can read out an aggregate quality across the chain rather than a per-link quality. This is a theorem to prove, not just a definition to adopt; the synthesis debate identifies it as the W26 chain-bound theorem.

Items beyond these (categorical fibration apparatus, Rosen lineage citations, EF G/A/T decomposition) are not strictly required for the design spec; they are theoretical-paper extensions.

### 7.3 Updated recommendation direction

The synthesis debate's five-layer stack should be reorganized in light of this extraction. A sketch of the direction (not the full updated recommendation):

**Reorganization principle.** Use the draft's (sigma_env, D_env) on the IO observation frame morphism as the operational context-morphism quality construct. Drop Layer 3 from the synthesis-debate stack as "already delivered by the draft." Drop Layer 5 to a citation footnote. Reframe Layer 1 as a "precondition wrapper" added on top of the draft. Reframe Layer 2 as a possible operational refinement not strictly required. Promote Layer 4 (distributional axis) to "the genuine new construct work," with a conformal-prediction reading proposed as the closest-to-draft option.

**Resulting structure (sketch).**

- **Core construct (from the draft, not new):** Each morphic chain link carries two kinds of morphism. Context morphisms (IO level) are quantified by (sigma_env, D_env). System morphisms (N level) are quantified by (sigma_sys, D_sys). The Bayesian network on top propagates V&V confidence via the marginalization equation (equation 8 of the draft).
- **Wrapper additions for the AI Circuit Breaker design spec:**
  - (a) Wymore-A precondition predicate `q in Dom(h_cert)`, instantiated using IO_cert and N_cert from the draft's specification.
  - (b) Distributional-axis sensor on context match, with conformal-prediction coverage as the recommended starting point (already in draft's bibliography and discussion as a future direction).
  - (c) Chain-composition theorem for (sigma, D), formalizing the worst-case / additive composition that the draft implies but does not state.
- **Optional theoretical-paper extensions:**
  - (d) Categorical fibration formulation as a journal-paper restatement of the draft's set-theoretic closed-context construction, for the ACT / Compositionality audience.
  - (e) Rosen / Pattee lineage acknowledgment as a one-paragraph cross-disciplinary positioning move.
  - (f) DEVS G/A/T decomposition as an alternative operational refinement of the draft's IO frame, if a paper venue calls for it.

**The headline change to the prior recommendation.** Layers 1, 2, 3, 5 of the prior recommendation are now seen as either present-in-the-draft, partially-present, or low-priority additions. Layer 4 (distributional axis) is the surviving genuine new-construct claim. The AI Circuit Breaker design spec should be written on top of the draft's framework, not in parallel to it; the three wrapper additions above are the design-spec-specific deliverables.

### 7.4 What this extraction does not settle

This extraction is a faithful read of the draft. It does not settle:

- Whether the draft's framework is the *right* framework for the AI Circuit Breaker design spec. It only establishes that the draft already carries most of what the synthesis debate proposed.
- Whether the (sigma_env, D_env) pair is sufficient as a context-morphism quality, or whether one of the candidate distributional invariants should be added.
- Whether the draft's notation should be carried wholesale into the AI Circuit Breaker design spec, or whether a translation layer is needed.
- The priority and sequencing of the three wrapper additions above.

These are decisions for the synthesis step. This document supplies the material for those decisions.

---

## Appendix A: Source line-number index

For traceability, the key passages in the draft and their LaTeX source locations.

| Construct | Source file | Line(s) |
|---|---|---|
| LBS output equation `Y = F_S(O_{C,S}(X))` | `main.tex` | 145 |
| Closed-context definition `C_1, C_2, ...` | `main.tex` | 138 |
| Theoretical background, WySE Metamodel introduction | `main.tex` | 159-165 |
| IO observation frame `IO = (T, X, Y)` (eq 2) | `main.tex` | 167-171 |
| IO observation frame morphism, maps g and k | `main.tex` | 173 |
| Coupled system `N = (T, X_N, Y_N, D, {M_d}, {I_d}, {Z_d})` (eq 3) | `main.tex` | 175-179 |
| Coupling morphism `<coord, k_d', g_d', h_d'>` (eq 4) | `main.tex` | 181-185 |
| Approximate morphism / neighborhoods | `main.tex` | 187 |
| Two-axis degradation framework (sigma, D) definitions | `main.tex` | 189-198 |
| Three structural facts about IO vs N levels | `main.tex` | 200 |
| Morphic chain definition | `main.tex` | 202 |
| Quad relationship introduction | `main.tex` | 206-208 |
| Figure 2 caption (quad maps to two-axis: context (sigma_env, D_env), system (sigma_sys, D_sys)) | `main.tex` | 210-215 |
| Bayesian networks for system confidence | `main.tex` | 224-236 |
| Marginal computation (eq 5) | `main.tex` | 228-232 |
| Full context conditional independence (eq 6) | `main.tex` | 242-247 |
| Partial context conditional dependence (eq 7) | `main.tex` | 249-258 |
| Partial context as default for V&V | `main.tex` | 258 |
| Prediction equation (eq 8) | `main.tex` | 271-275 |
| (sigma, D) parameterization of conditional probability | `main.tex` | 279 |
| Latent variable DAG figure | `network_latent.tex` | 1-41 |
| YOLO Bayesian network figure | `network_yolo.tex` | 1-29 |
| LBS block diagram with closed context | `lbs_diagram.tex` | 1-53 |
| YOLO example, predictive validation | `main.tex` | 386-426 |
| Conclusion, four-contribution summary | `main.tex` | 458-465 |

## Appendix B: Symbol mapping between draft, synthesis-debate, and brief

| Concept | Draft notation | Synthesis-debate notation | Brief notation |
|---|---|---|---|
| Closed context | `C` (`\env`) | `c_cert`, `c_op` | env_1, env_2 |
| Context family | `{C_1, C_2, ...}` | `{ Z_real(c) | c in C }` | family of envs |
| Context morphism (IO level) | IO observation frame morphism | inter-fiber morphism `g` (Wymore-B) or `k` (categorical) | io observation frame morphism |
| Context morphism quality | (sigma_env, D_env) | (D_s(g), D_b(g)) | (sigma_env, D_env) |
| System | `S` (`\sys`), `N` (`\ns`) | `Z_ai`, `Z_real` | sys |
| System morphism | Coupling morphism | `h_cert` | NS coupled system morphism |
| System morphism quality | (sigma_sys, D_sys) | (D_s(h), D_b(h)) | (sigma_sys, D_sys) |
| Quad relationship | the quad in Figure 2 | Layer 3 inter-fiber + within-fiber | quad relationship |
| Morphic chain | the morphic chain | composition of inter-fiber morphisms | morphic chain |
| Full context | `C_full` | (implicit) | full context |
| Partial context | `C_obs` | (implicit) | partial context |
| Latent variables | `E` | (implicit, ancestral graph) | latent context variables |
| Distributional axis | (absent) | `sigma_dist`, free energy, Sigma_ctx | (absent in draft) |
| Precondition test | (absent) | `q in Dom(h_cert)` (Wymore-A) | (absent in draft) |
| Chain composition rule | (implicit) | W26 chain bound | (open) |
