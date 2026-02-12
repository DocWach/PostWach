# Agentic AI Swarms for Systems Engineering: A Survey of Multi-Agent Architectures, Coordination Mechanisms, and Applications

**Draft v0.2 — February 2026**

---

## Abstract

The convergence of multi-agent systems, swarm intelligence, and large language model (LLM)-based agentic AI creates new possibilities for augmenting systems engineering (SE) practice. This survey systematically organizes this emerging field, synthesizing 150+ publications across artificial intelligence, software engineering, SE, and human factors communities.

We present taxonomies of agent architectures—from classical reactive and Belief-Desire-Intention (BDI) designs through contemporary LLM-based agents with tool use and memory—and coordination mechanisms spanning communication-based, organization-based, and emergent approaches. We map applications to ISO/IEC/IEEE 15288 technical processes, surveying over 30 frameworks and mapping applications across 14 ISO 15288 process areas, revealing concentrated maturity in requirements analysis and test generation with substantial gaps across the remaining lifecycle.

Our evaluation analysis identifies critical gaps: no standardized benchmarks exist for multi-agent SE systems, and tools and frameworks, while maturing rapidly, lack SE-specific integration. We categorize challenges as technical (scalability, reliability, domain knowledge), integration (tool, process, data), human factors (trust, oversight, skills), and organizational (governance, certification, accountability).

Based on this analysis, we propose a prioritized research agenda: near-term benchmark development, reliability characterization, and domain knowledge grounding; medium-term coordination at scale, human-AI teaming, and governance frameworks; long-term collective engineering intelligence and appropriate automation boundaries. For researchers, this survey provides organized access to fragmented literature and identifies high-priority gaps. For practitioners, it offers realistic capability assessment. For the broader community, it establishes common vocabulary enabling cumulative progress toward AI-augmented SE.

*Index Terms*— multi-agent systems, swarm intelligence, large language models, agentic AI, systems engineering, ISO 15288, human-AI collaboration

---

## 1. Introduction

### 1.1 Motivation for Survey

The convergence of multi-agent systems research, swarm intelligence, and large language model (LLM)-based agentic AI creates unprecedented opportunities for augmenting systems engineering (SE) practice. Individual AI assistants already help engineers with specific tasks; coordinated multi-agent systems promise more comprehensive support spanning the engineering lifecycle.

Yet this emerging field lacks the systematic organization that mature research areas possess. Literature spans multiple communities—artificial intelligence, software engineering, SE, human factors—with limited cross-referencing. Terminology varies; comparable approaches receive different names; gaps and opportunities remain uncharted. Researchers entering the field face difficulty understanding the landscape; practitioners struggle to assess applicability to their contexts.

This survey addresses these gaps by providing systematic organization of the field, synthesizing contributions across research communities, developing taxonomies of architectures and coordination mechanisms, mapping applications to SE processes, and identifying challenges and research directions.

### 1.2 Scope and Boundaries

This survey covers multi-agent AI systems applicable to SE—the domain-agnostic discipline addressing complex system development across the lifecycle [24, 25, 26]. We distinguish SE from the narrower software engineering, though we include software engineering literature where relevant to broader SE application.

**Included:**
- Multi-agent systems architectures (classical and LLM-based)
- Coordination mechanisms for agent collaboration
- Applications to SE technical processes per ISO 15288
- Evaluation methods and benchmarks
- Tools and frameworks
- Challenges and research directions

**Excluded:**
- Single-agent AI assistants (covered in related surveys)
- General multi-agent systems without engineering application
- Domain-specific applications without generalizable insights
- Detailed treatment of underlying LLM architectures

### 1.3 Survey Methodology

This survey follows established systematic review practices, informed by Preferred Reporting Items for Systematic Reviews and Meta-Analyses (PRISMA) guidelines [83], adapted for a rapidly evolving field.

**Literature identification:** We searched IEEE Xplore, ACM Digital Library, Springer, Elsevier, and arXiv for publications from January 2018 through December 2025, using terms including "multi-agent systems," "swarm intelligence," "LLM agents," combined with "systems engineering," "requirements," "architecture," "verification," and related terms. The initial database search yielded approximately 2,400 results, which were reduced to approximately 180 after title and abstract screening against relevance criteria. We supplemented database searches with forward and backward citation following from key papers and with expert recommendation. Due to the rapid evolution of LLM-based agent research, we additionally monitored arXiv preprints and industry technical reports throughout the review period to capture significant contributions not yet appearing in peer-reviewed venues.

**Selection criteria:** We included peer-reviewed publications and significant preprints addressing multi-agent AI approaches with relevance to SE processes. We excluded purely theoretical work without application consideration and purely domain-specific applications without generalizable contribution.

**Synthesis approach:** We organized findings according to taxonomic frameworks developed iteratively during review. We assessed application maturity based on evidence type (laboratory, field trial, production) and validation rigor.

**Limitations:** The field evolves rapidly; some recent work may be missed. LLM-based agent research moves faster than peer review; we include significant preprints while noting lower validation standards. Our SE perspective may underweight contributions from adjacent fields.

### 1.4 Paper Organization

The remainder of this paper is organized as follows:
- Section 2 provides background on multi-agent systems, swarm intelligence, LLM-based agents, and SE processes
- Section 3 presents a taxonomy of agent architectures
- Section 4 surveys coordination mechanisms
- Section 5 maps applications to SE process areas
- Section 6 examines evaluation methods and benchmarks
- Section 7 reviews tools and frameworks
- Section 8 analyzes challenges and open problems
- Section 9 proposes research directions
- Section 10 concludes

Different readers may benefit from different paths through this material. Researchers new to multi-agent systems may benefit from reading Sections 2 through 4 sequentially to build foundational understanding before examining applications. Practitioners assessing applicability to their organizations should focus on Sections 5, 7, and 8, which map capabilities to SE processes, review available tools, and discuss adoption challenges. Those primarily seeking research opportunities should consult Sections 6, 8, and 9, which identify evaluation gaps, open problems, and future directions.

---

## 2. Background and Foundations

This section establishes the foundational concepts underlying multi-agent AI systems for SE, tracing the evolution of relevant research areas and defining the intersection that motivates this survey.

### 2.1 Multi-Agent Systems: Historical Development

Multi-agent systems (MAS) emerged as a distinct research area in the 1980s and 1990s, drawing from distributed artificial intelligence, object-oriented programming, and concurrent systems [1, 2]. Wooldridge and Jennings [3] provided influential definitions, characterizing agents as computer systems capable of autonomous action in some environment to meet design objectives. Key properties include autonomy (operating without direct intervention), social ability (interacting with other agents), reactivity (perceiving and responding to environment), and proactivity (taking initiative toward goals).

Early MAS research addressed fundamental questions: How should agents be designed internally? How should agents communicate and coordinate? How do collective behaviors emerge from individual actions? Foundational work established agent communication languages (Knowledge Query and Manipulation Language [KQML], Foundation for Intelligent Physical Agents ACL [FIPA-ACL]), coordination mechanisms (contract net, organizational structures), and agent architectures (reactive, deliberative, hybrid) [4, 5, 6].

By the 2000s, MAS had found applications across domains including manufacturing, logistics, e-commerce, and simulation. However, the symbolic AI approaches underlying most MAS work faced limitations in handling uncertainty, learning from experience, and processing unstructured information—limitations that constrained applicability to complex real-world problems.

### 2.2 Swarm Intelligence: Principles and Paradigms

Swarm intelligence emerged from study of collective behavior in biological systems—ant colonies, bird flocks, fish schools—where simple individuals following local rules produce sophisticated collective behavior [7, 8]. Bonabeau, Dorigo, and Théraulaz [9] formalized swarm intelligence principles and demonstrated applications to optimization problems.

Key swarm intelligence paradigms include:

**Ant Colony Optimization (ACO)** models how ants find shortest paths through pheromone-based stigmergic coordination [10]. Artificial ants deposit virtual pheromone on solution components, guiding subsequent ants toward promising solutions. ACO has proven effective for combinatorial optimization problems including routing, scheduling, and assignment. In engineering contexts, ACO has been applied to scheduling problems such as test case prioritization [84] and resource allocation in complex projects [85], where the combinatorial search space makes exhaustive approaches intractable.

**Particle Swarm Optimization (PSO)** models flocking behavior, with particles (candidate solutions) moving through search spaces influenced by their own best-known position and the swarm's best-known position [11]. PSO has found wide application in continuous optimization. PSO applications in engineering include multi-objective design optimization [86] and antenna design [87], demonstrating the paradigm's utility for parameter-rich engineering problems with competing objectives.

**Stigmergic coordination** provides a paradigm for indirect communication through environmental modification—agents leave traces that influence other agents' behavior without direct message exchange [12]. This enables scalable coordination with minimal communication overhead. In engineering contexts, shared digital models (e.g., model-based systems engineering (MBSE) repositories) can serve as stigmergic media, where agent annotations, flags, and analysis results left on model elements guide subsequent agents' analysis and review activities [88].

Swarm intelligence contributes key insights to AI swarms: that collective intelligence can exceed individual capability, that simple local rules can produce complex global behavior, and that decentralized coordination can achieve robust, scalable solutions.

### 2.3 Large Language Models and Agentic AI

The emergence of large language models (LLMs) since 2018 has transformed the landscape for AI agent development [13, 14]. Models trained on massive text corpora exhibit emergent capabilities in language understanding, reasoning, and generation that earlier approaches could not achieve [15]. The field has advanced rapidly: OpenAI's GPT-4 [89], Anthropic's Claude [90], and Google's Gemini [91] represent the commercial frontier, while open-weight models such as Meta's Llama [92] and Mistral [93] have broadened access and enabled customization for specialized domains.

The transition from LLMs to agentic AI involves augmenting language models with capabilities for autonomous action:

**Tool use** enables LLMs to invoke external tools—calculators, search engines, APIs, code interpreters—extending their capabilities beyond text generation [16, 17]. Tool-augmented LLMs can retrieve information, execute computations, and interact with external systems. The Model Context Protocol (MCP) [94] has emerged as a standardization effort for tool integration, providing a uniform interface through which LLM agents discover and invoke external capabilities. Agentic coding tools such as Claude Code, Cursor, and GitHub Copilot Workspace [95] exemplify tool-augmented LLM agents that have reached production use, demonstrating the viability of autonomous tool invocation in professional workflows.

**Computer use and GUI agents** represent a further expansion of agentic capability (2024--2025), enabling LLM-based agents to interact directly with graphical user interfaces (GUIs)—clicking, typing, and navigating applications as a human user would [96]. This capability is particularly relevant for SE, where many tools (e.g., modeling environments, product lifecycle management (PLM) systems) lack programmatic APIs.

**Memory systems** provide LLMs with persistent context beyond their context window, enabling accumulation of knowledge across interactions [18]. Memory architectures include retrieval-augmented generation (RAG), vector databases, and structured knowledge stores.

**Planning and reasoning** approaches enable LLMs to decompose complex tasks, reason about action sequences, and pursue goals over extended interactions [19, 20]. Techniques include chain-of-thought prompting, ReAct (reasoning + acting), and tree-of-thought exploration.

**Multi-agent LLM systems** extend agentic AI to multiple coordinated agents, each potentially with specialized roles, capabilities, or perspectives [21, 22, 23]. Recent frameworks including AutoGPT, MetaGPT, CrewAI, and others demonstrate multi-agent architectures where LLM-based agents collaborate on complex tasks.

### 2.4 Systems Engineering Process Framework

SE provides the disciplined processes for managing complex system development across the lifecycle [24, 25]. ISO/IEC/IEEE 15288:2023 [26] defines the standard framework of system lifecycle processes, organized into:

**Technical processes** directly realize and support the system:
- Stakeholder Needs and Requirements Definition
- System Requirements Definition
- Architecture Definition
- Design Definition
- System Analysis
- Implementation
- Integration
- Verification
- Validation
- Transition
- Operation
- Maintenance
- Disposal

**Technical management processes** establish and evolve plans, assess progress, and control execution. **Organizational project-enabling processes** provide resources and infrastructure.

The INCOSE Systems Engineering Handbook [27] and NASA Systems Engineering Handbook [28] provide guidance on applying these processes across domains. SE applies to any complex system—aerospace, defense, healthcare, energy, transportation, infrastructure—making it inherently domain-agnostic while requiring domain-specific knowledge for application.

### 2.5 Intersection: Why Multi-Agent AI for Systems Engineering?

The convergence of multi-agent systems, swarm intelligence, and LLM-based agentic AI creates new possibilities for SE support. Several characteristics of SE motivate multi-agent approaches:

**Multi-disciplinary nature.** SE integrates contributions from diverse disciplines—mechanical, electrical, software, human factors, logistics. No single agent can embody expertise across all disciplines; multi-agent architectures enable discipline specialization with cross-discipline coordination.

**Collaborative practice.** SE is inherently collaborative, involving teams of engineers, stakeholders, and organizations. Multi-agent systems mirror this collaborative structure, with agents representing different perspectives, roles, or organizational entities.

**Artifact complexity.** SE produces complex, interrelated artifacts—requirements, architectures, designs, test cases—with consistency and traceability requirements across thousands of elements. Agent swarms can achieve comprehensive coverage that individual analysis cannot.

**Lifecycle span.** SE spans extended lifecycles from concept through disposal. Persistent agent systems can maintain continuity, accumulating knowledge and adapting to evolving system states.

**Quality through diversity.** Engineering quality benefits from multiple perspectives examining artifacts. Agent swarms provide perspective diversity—different specializations, different analysis approaches—that surface issues single-point analysis misses.

This intersection defines the scope of this survey: multi-agent AI systems, drawing on classical MAS foundations, swarm intelligence principles, and modern LLM-based agentic AI capabilities, applied to support SE processes. Section 5 provides the systematic mapping of these intersecting capabilities to ISO 15288 process areas that constitutes this survey's core contribution.

---

## 3. Taxonomy of Agent Architectures

This section presents a taxonomy of agent architectures relevant to SE applications, tracing evolution from classical approaches through contemporary LLM-based designs.

### 3.1 Classification Framework

Agent architectures can be classified along several dimensions:

**Reasoning approach:** How does the agent decide what to do?
- Reactive: Stimulus-response mappings
- Deliberative: Explicit reasoning about goals and plans
- Hybrid: Combining reactive and deliberative elements

**Knowledge representation:** How does the agent represent its understanding?
- Implicit: Encoded in behavior rules or neural weights
- Explicit: Symbolic knowledge bases, ontologies
- Hybrid: Combining implicit and explicit representations

**Learning capability:** Can the agent improve from experience?
- Static: Fixed behavior after deployment
- Adaptive: Learning during operation
- Meta-learning: Learning how to learn

**Foundation model:** What provides core capabilities?
- Classical AI: Rule-based, search, optimization
- Machine learning: Statistical models, neural networks
- Large language models: Pre-trained transformer models

### 3.2 Reactive Architectures

Reactive architectures eschew explicit world models and deliberation in favor of direct stimulus-response mappings. Brooks' subsumption architecture [29] demonstrated that intelligent behavior could emerge from layered reactive behaviors without symbolic reasoning.

**Characteristics:**
- Fast response to environmental changes
- Robust to model errors (no model to be wrong)
- Limited planning horizon
- Behavior emerges from interaction of simple rules

**SE applications:** Reactive architectures suit real-time monitoring and response—detecting anomalies, triggering alerts, managing routine workflows. They are less suited to complex reasoning tasks like trade studies or requirements analysis.

**Limitations for SE:** SE frequently requires reasoning about abstract concepts (requirements, architectures) that lack direct environmental correlates. Pure reactive approaches cannot address tasks requiring deliberation, planning, or explanation.

### 3.3 Deliberative Architectures

Deliberative architectures maintain explicit world models and reason about goals, plans, and actions. The Belief-Desire-Intention (BDI) model [30, 31] provides an influential framework where agents have beliefs about the world, desires (goals) they wish to achieve, and intentions (committed plans) they are executing.

**Characteristics:**
- Explicit goal representation and pursuit
- Planning and plan execution
- Reasoning about action consequences
- Explainable decision-making (in principle)

**SE applications:** BDI agents can model engineering roles with explicit goals (e.g., a requirements agent with goals of completeness, consistency, traceability) and plans for achieving them (analysis procedures, review protocols). Goal-directed behavior aligns with engineering objectives.

**Implementations:** JACK, Jadex, Jason provide BDI agent platforms [32, 33]. These frameworks support agent development with explicit belief bases, goal management, and plan libraries.

**Limitations for SE:** Classical BDI implementations require explicit knowledge engineering—defining beliefs, goals, and plans in advance. This limits adaptability to novel situations and requires substantial development effort to encode domain knowledge.

### 3.4 Hybrid Architectures

Hybrid architectures combine reactive and deliberative elements, typically in layered designs where reactive behaviors handle routine situations while deliberative reasoning addresses complex cases.

**Layered architectures** [34] organize agent capabilities hierarchically:
- Reactive layer: Immediate responses to environmental conditions
- Planning layer: Goal-directed reasoning and plan generation
- Cooperative layer: Social reasoning and coordination with other agents

**InteRRaP** [35] exemplifies layered hybrid design with behavior-based, planning, and cooperation layers, each with associated knowledge bases.

**SE applications:** Hybrid architectures can provide responsive behavior for routine engineering tasks while engaging deliberative reasoning for complex decisions. A requirements agent might reactively maintain traceability links while deliberatively analyzing completeness.

### 3.5 LLM-Based Agent Architectures

Large language model-based agents represent a paradigm shift, leveraging pre-trained foundation models rather than hand-crafted knowledge bases. Several architectural patterns have emerged:

**ReAct (Reasoning + Acting)** [36] interleaves reasoning traces with actions, enabling LLMs to reason about what action to take, execute it, observe results, and continue reasoning. ReAct provides a general pattern for LLM-based agency.

**Tool-augmented architectures** [37, 38] extend LLM capabilities through tool invocation. The LLM decides which tools to call, formulates inputs, interprets outputs, and integrates results into ongoing reasoning. Tools can include calculators, search engines, code interpreters, and domain-specific applications.

**Memory-augmented architectures** [39] provide persistent memory beyond the LLM's context window:
- Short-term memory: Recent interaction context
- Long-term memory: Persistent knowledge, accumulated experience
- Episodic memory: Records of past interactions and outcomes

**Retrieval-Augmented Generation (RAG)** [40] grounds LLM responses in retrieved documents, enabling access to domain knowledge, standards, and organizational practices without fine-tuning.

**Multi-agent LLM architectures** coordinate multiple LLM-based agents:
- Role-based: Agents assume specialized roles (researcher, coder, reviewer)
- Debate-based: Agents argue positions, refine through discourse
- Hierarchical: Manager agents coordinate worker agents
- Peer: Agents collaborate as equals with complementary capabilities

Notable multi-agent LLM implementations include **MetaGPT** [41] (multi-agent software development with role-based specialization), **AutoGen** [42] (conversational agents with customizable patterns), **CrewAI** [43] (role-based agent crews for complex tasks), and **LangGraph** [44] (graph-based agent orchestration).

**Autonomous software engineering agents** represent a notable subclass of LLM-based architectures that target end-to-end task completion with minimal human intervention:
- **SWE-agent** [97]: An agent interface designed specifically for resolving GitHub issues. SWE-agent pairs an LLM with a custom shell environment and file editor, achieving strong performance on the SWE-bench benchmark [67]. Its architecture emphasizes agent-computer interface design, demonstrating that how an LLM interacts with tools matters as much as the model's intrinsic capability.
- **OpenHands** [98] (formerly OpenDevin): An open-source platform for autonomous software development agents that execute within sandboxed environments. OpenHands provides a runtime architecture separating the agent's planning loop from code execution, enabling safe exploration of solution strategies without compromising the host system.
- **Devin** [99] (Cognition, 2024): Marketed as the first "AI software engineer," Devin integrates a code editor, web browser, terminal, and planner within a persistent agent environment. Its architecture demonstrated commercial viability of fully autonomous coding agents, though independent evaluations have shown performance varies substantially across task domains.
- **Claude Code** [100] (Anthropic): An agentic coding tool providing the LLM with direct access to file editing, terminal execution, and web search tools. Claude Code operates in an extended thinking mode with tool use, representing an architecture where a single powerful model orchestrates complex multi-step engineering tasks through iterative tool invocation.
- **OpenAI Swarm** [101]: An experimental framework for lightweight multi-agent orchestration. Swarm introduces the concept of "handoffs" between specialized agents, each defined by instructions and tool sets, with minimal coordination overhead. Its architecture favors simplicity—agents are essentially functions with LLM-backed decision-making—making it suitable for prototyping multi-agent workflows.

### 3.6 Architecture Comparison

Table 1 compares architectural approaches across key dimensions.

\footnotesize

| Architecture | Reasoning | Knowledge | Learning | Planning | Explain. | Autonomy | SE Fit |
|---|---|---|---|---|---|---|---|
| Reactive | Stimulus-resp. | Implicit | Limited | None | Low | Low | Monitoring |
| BDI | Goal-directed | Explicit | Limited | Yes | High | Moderate | Structured |
| Hybrid | Layered | Mixed | Moderate | Partial | Moderate | Moderate | Balanced |
| LLM-based | Emergent | Implicit+RAG | In-context | Prompted | Moderate | Moderate | Flexible |
| LLM+Tools | Augmented | Hybrid | Adaptive | Reasoned | Moderate | High | Complex |
| Multi-agent LLM | Distributed | Distributed | Collective | Coordinated | Variable | High | Full lifecycle |
| Autonomous SE | End-to-end | Hybrid+tools | In-context+fb | Iterative | Low-Mod. | Full | Software |
| Light. swarm | Delegated | Per-agent | Handoff | Orchestrated | Low | High | Prototyping |

\normalsize

### 3.7 Architectural Convergence

A striking observation across recent LLM-based agent frameworks is their convergence toward a common cognitive architecture pattern. Despite diverse origins and application domains, nearly all contemporary systems adopt the same structural template: an LLM core providing reasoning and natural language understanding, augmented with tool use interfaces for acting on the environment, memory systems for maintaining state across interactions, and a planning loop that iterates between reasoning, action, and observation [26].

This convergence stands in sharp contrast to classical agent architectures, where reactive, deliberative, and hybrid systems differed fundamentally in their internal structures—subsumption layers bore no resemblance to BDI belief bases, and neither resembled blackboard systems. In the LLM era, the architectural differences between MetaGPT, AutoGen, SWE-agent, and Claude Code are comparatively superficial: they share the same foundation model backbone and differ primarily in prompt design, tool configuration, coordination topology, and the granularity of human oversight [102]. The "cognitive architecture for language agents" pattern identified by Sumers et al. [26] thus functions as a de facto standard, with framework-specific innovations occurring at the integration layer rather than at the architectural core.

This convergence has practical implications for SE adoption. Organizations evaluating multi-agent architectures need not choose between fundamentally incompatible paradigms; instead, selection criteria shift toward tool ecosystem maturity, coordination mechanism suitability, and the degree of autonomy appropriate for the engineering context [103].

### 3.8 Architectural Trends

Several trends characterize the evolution of agent architectures for engineering applications:

**Foundation model dominance.** LLM-based architectures increasingly dominate new development, leveraging pre-trained capabilities rather than hand-crafted knowledge. This shifts development effort from knowledge engineering to prompt engineering and tool integration.

**Hybrid knowledge integration.** Pure LLM approaches suffer from hallucination and knowledge gaps; production systems increasingly integrate retrieval (RAG), structured knowledge, and tool-based verification to ground LLM reasoning.

**Specialization through prompting.** Rather than architecturally distinct agent types, LLM-based systems achieve specialization through role prompts, system instructions, and tool configurations applied to a common foundation model.

**Emergent coordination.** Multi-agent LLM systems exhibit coordination patterns not explicitly programmed, emerging from agent interactions. This creates both opportunities (novel solutions) and challenges (unpredictable behavior).

**Continuous evolution.** Unlike classical agents with fixed architectures, LLM-based agents evolve as foundation models improve. Architectural patterns that leverage model capabilities will benefit from ongoing model advancement.

---

## 4. Coordination Mechanisms

Effective multi-agent systems require coordination—managing dependencies, resolving conflicts, and achieving coherent collective behavior. This section surveys coordination mechanisms applicable to AI swarms in SE contexts.

### 4.1 Classification of Coordination Approaches

Malone and Crowston [45] define coordination as "managing dependencies between activities." Coordination mechanisms can be classified by:

**Communication directness:**
- Direct: Explicit message exchange between agents
- Indirect: Coordination through shared environment (stigmergy)

**Control structure:**
- Centralized: Coordinator manages agent activities
- Decentralized: Agents coordinate peer-to-peer
- Hierarchical: Multi-level coordination structure

**Temporal coupling:**
- Synchronous: Agents coordinate in real-time
- Asynchronous: Agents coordinate through persistent state

**Formality:**
- Structured: Defined protocols and interfaces
- Unstructured: Natural language or emergent patterns

### 4.2 Communication-Based Coordination

Communication-based approaches coordinate through explicit information exchange:

**Message passing** provides direct agent-to-agent communication. Agent communication languages (ACL) define message semantics [46]. FIPA-ACL specifies performatives (inform, request, propose) enabling structured dialogue. In LLM-based systems, natural language messages often replace formal ACLs.

**Blackboard systems** [47] coordinate through shared data structures. Agents post contributions to a shared "blackboard"; other agents observe and respond. This decouples agents temporally and reduces direct communication complexity. For SE, shared system models can serve as blackboards—agents contribute analyses, other agents incorporate findings.

**Publish-subscribe** patterns enable event-driven coordination [48]. Agents publish events; interested agents subscribe and receive notifications. This supports loose coupling and scalability. SE applications include change propagation—when requirements change, subscribed architecture agents receive notifications.

**Shared memory** provides coordination through common state access. Agents read and write shared data structures, observing each other's contributions. Vector databases in LLM systems serve as shared memory, enabling agents to store and retrieve information produced by other agents.

### 4.3 Organization-Based Coordination

Organization-based approaches structure agent relationships to manage coordination:

**Hierarchical organizations** arrange agents in authority structures [49]. Higher-level agents decompose tasks, assign work, and integrate results. This reduces coordination complexity—each agent coordinates primarily with its supervisor and subordinates. SE parallels: chief systems engineer coordinating Integrated Product Team (IPT) leads who coordinate discipline engineers.

**Market-based coordination** uses economic mechanisms [50]. The Contract Net Protocol [51] exemplifies market coordination: manager agents announce tasks; contractor agents bid; managers award contracts based on bids. This enables dynamic task allocation without centralized planning.

**Team-based coordination** groups agents into teams pursuing shared goals [52]. Teamwork theories (SharedPlans, Joint Intentions) formalize how agents commit to collective objectives and coordinate execution. SE teams naturally map to agent teams with shared project goals.

**Coalition formation** enables dynamic grouping for specific objectives [53]. Agents form coalitions when collaboration benefits exceed costs, dissolving when objectives are met. For SE, coalitions might form for specific trade studies or reviews, then dissolve.

### 4.4 Emergent Coordination

Emergent approaches achieve coordination without explicit protocols:

**Stigmergy** coordinates through environmental modification [12]. Agents leave traces (pheromones, markers) that influence other agents' behavior. No direct communication required; coordination emerges from accumulated environmental changes. SE applications: agents annotating shared models, with annotations guiding subsequent agent attention.

**Self-organization** produces coordinated structures from local interactions [54]. Agents following simple local rules generate global patterns without central control. This enables robust, scalable coordination but limits predictability.

**Swarm behaviors** exhibit collective intelligence through decentralized coordination [9]. Individual agents respond to local information; collective behavior emerges from aggregated responses. Swarm coordination suits exploration and optimization but may struggle with precision requirements.

### 4.5 Hybrid Approaches

Practical systems often combine coordination mechanisms:

**Hierarchical with market elements** uses hierarchy for task decomposition and markets for resource allocation within levels.

**Centralized planning with distributed execution** employs central coordinators for planning while agents execute autonomously, reporting status.

**Structured protocols with natural language** combines formal coordination protocols with natural language communication for flexibility.

### 4.6 Coordination in LLM-Based Systems

LLM-based multi-agent systems exhibit distinctive coordination patterns:

**Conversational coordination** uses natural language dialogue rather than formal protocols. Agents discuss, debate, and negotiate in natural language, leveraging LLM conversational capabilities. This enables flexibility but may sacrifice precision.

**Prompt-based role assignment** coordinates through role definitions in system prompts. Each agent's prompt defines its responsibilities, communication patterns, and coordination expectations.

**Orchestrator patterns** employ a central agent (often called "supervisor" or "manager") that routes tasks, manages workflow, and synthesizes outputs. This provides control but creates bottlenecks.

**Reflection and critique** patterns have agents review each other's outputs, providing feedback that drives iteration. Coordination emerges through iterative refinement.

**Memory-mediated coordination** uses shared memory systems (vector stores, knowledge graphs) as coordination substrate. Agents contribute to and query shared memory, achieving indirect coordination.

**Framework-specific coordination implementations** illustrate how these abstract patterns manifest in practice:
- **MetaGPT** [41] employs a "Software Company" metaphor in which agents assume roles (Product Manager, Architect, Engineer, QA) and coordinate through a shared message pool and structured document outputs. Each role publishes artifacts (product requirements documents, design documents, code) that downstream roles consume, enforcing a sequential dependency chain akin to a waterfall process [104].
- **AutoGen** [42] implements conversational turn-taking where agents exchange natural language messages in configurable interaction patterns. Speaker selection can be round-robin, random, or LLM-directed, enabling flexible coordination topologies from simple two-agent dialogues to complex group chats with dynamic participation [105].
- **CrewAI** [43] uses a "crew" metaphor with explicit task delegation. Agents are assigned roles with defined goals and backstories, and tasks flow through sequential or hierarchical process models. A hierarchical process designates a manager agent that delegates subtasks and synthesizes results [106].
- **LangGraph** [44] takes a graph-theoretic approach, modeling coordination as explicit state machines. Nodes represent agent actions or decision points; edges define transitions conditioned on state. This provides deterministic control flow while allowing individual nodes to invoke LLM reasoning, offering a balance between predictability and flexibility [107].
- **ChatDev** [108] simulates a software company with agents coordinating through waterfall-model phases (design, coding, testing, documentation). Phase transitions are explicitly structured, and within each phase, agents engage in role-playing dialogues to produce artifacts.

### 4.7 Comparison and Trade-offs

Table 2 compares coordination mechanisms across key dimensions.

\footnotesize

| Mechanism | Coupling | Scalability | Predictability | Flexibility | SE Suitability |
|-----------|----------|-------------|----------------|-------------|----------------|
| Message passing | Tight | Moderate | High | Moderate | Structured workflows |
| Blackboard | Loose | Good | Moderate | High | Shared model updates |
| Hierarchy | Moderate | Good | High | Low | Large teams |
| Market | Loose | Good | Moderate | High | Resource allocation |
| Stigmergy | Loose | Excellent | Low | High | Exploration tasks |
| Conversational | Tight | Limited | Low | Excellent | Creative tasks |
| Orchestrator | Tight | Limited | High | Moderate | Controlled workflows |

\normalsize

**Trade-off considerations for SE:**

*Predictability vs. flexibility:* Safety-critical SE applications prioritize predictability; exploratory tasks benefit from flexibility. Coordination mechanism choice should align with task requirements.

*Scalability vs. control:* Larger swarms require scalable coordination (hierarchical, stigmergic) but may sacrifice fine-grained control. Task characteristics determine appropriate balance.

*Communication overhead:* Rich communication (conversational) enables nuanced coordination but incurs token costs and latency. Efficient protocols reduce overhead at the cost of expressiveness.

*Token economics:* In LLM-based systems, coordination carries direct financial cost through token consumption. Conversational coordination between N agents generates O(N^2) message pairs, each consuming inference tokens. As agent count grows, coordination token costs can dominate task-execution costs, creating economic pressure toward sparse communication topologies, hierarchical delegation, or shared-memory approaches that reduce pairwise message exchange [109].

*Emergence management:* Emergent coordination can produce beneficial novelty or harmful unexpected behavior. SE contexts may require bounds on emergence through hybrid approaches.

### 4.8 Coordination Failures and Mitigations

Multi-agent coordination introduces failure modes absent in single-agent systems. Understanding these failure patterns is essential for engineering reliable swarms.

**Agent echo chambers** occur when agents reinforce each other's errors through positive feedback loops. An agent producing an incorrect analysis may receive validation from peer agents that lack independent grounding, causing the error to propagate and become entrenched in the collective output [110].

**Degenerate consensus** arises when agents converge prematurely on a suboptimal solution. Group pressure dynamics—even among artificial agents—can suppress exploratory behavior, particularly when majority-voting or debate-based coordination mechanisms are employed without diversity safeguards.

**Coordination overhead exceeding task benefit** represents a practical failure where the computational and financial cost of multi-agent coordination surpasses the quality improvement over a single-agent baseline. This is especially prevalent in tasks with limited decomposability.

**Cascading failures** result from tight agent dependencies: when an upstream agent produces malformed output, downstream agents that depend on it may fail in sequence, potentially amplifying a minor error into a system-wide breakdown [111].

**Mitigations** include: diversity injection through varied model temperatures or distinct foundation models; independent verification where agents cross-check results against ground truth rather than peer output; graceful degradation that allows the system to produce partial results when individual agents fail; and circuit breakers that halt coordination when error indicators exceed defined thresholds.

---

## 5. Applications to Systems Engineering

This section surveys multi-agent AI applications across SE process areas, assessing maturity and identifying gaps in current research and practice.

### 5.1 Mapping Framework

We organize applications according to ISO/IEC/IEEE 15288:2023 technical processes [26], providing a systematic framework for coverage assessment. For each process area, we examine:
- Reported applications in literature
- Agent architectures employed
- Maturity level (research prototype, pilot deployment, production use)
- Evidence quality (laboratory study, field trial, case study)

### 5.2 Requirements Engineering Applications

Requirements engineering—encompassing stakeholder needs definition and system requirements definition—has received substantial attention from AI and multi-agent researchers.

**Requirements elicitation** applications use agents to support stakeholder interaction and needs capture. **Elicitron** exemplifies this class: a multi-agent framework that conducts simulated stakeholder interviews, with distinct agents representing different user roles, domain experts, and regulatory perspectives to surface requirements that might otherwise be missed [112]. Multi-agent approaches include:
- Stakeholder-representative agents embodying different user perspectives [55]
- Interview assistant agents generating questions and probing for completeness, such as IBM Watson-based requirements analysis assistants [113]
- Multi-perspective analysis where agents identify conflicting stakeholder needs
- Dialogue-driven elicitation where LLM agents simulate diverse end-user populations to stress-test requirements coverage [112]

**Requirements analysis** applications examine requirements quality. Tools such as **ARTE** (Automated Requirements Traceability Engine) and natural language processing (NLP) frameworks like **REGAL** demonstrate the growing sophistication of automated analysis pipelines [114]. Specific capabilities include:
- Completeness checking agents identifying missing requirements based on domain templates [56]
- Consistency checking agents detecting conflicts between requirements [57]
- Ambiguity detection agents flagging unclear language, increasingly leveraging transformer-based NLP models [58]
- Multi-agent argumentation for resolving requirement conflicts, where agents advocate for competing stakeholder priorities and negotiate compromises [59]
- Automated classification of functional versus non-functional requirements using ensemble agent architectures [114]

**Requirements specification** applications generate requirements artifacts:
- Natural language generation of requirements from models
- Formalization agents translating natural language to formal specifications
- Template-based generation with multi-agent review

**Requirements traceability** applications maintain relationships:
- Trace link generation agents identifying relationships between artifacts [60]
- Impact analysis agents assessing change propagation
- Traceability verification agents checking link completeness

**Maturity assessment:** Requirements applications are among the most mature, with research spanning decades and recent LLM-based tools reaching pilot deployment. Single-agent LLM approaches (e.g., GPT-4 for requirements classification) have demonstrated strong performance on isolated tasks, but true multi-agent systems that coordinate across elicitation, analysis, and traceability remain largely at the research prototype stage [115]. Evidence includes controlled experiments and industrial case studies, though most multi-agent evaluations are limited to laboratory settings.

### 5.3 Architecture and Design Applications

Architecture definition and design processes have seen growing multi-agent application:

**Architecture exploration** employs agents for systematic alternative evaluation. AI-assisted modeling with the Systems Modeling Language (SysML) is an emerging capability, where LLM agents generate and refine SysML block definition and internal block diagrams from natural language descriptions [116]. Integration with MBSE tools such as Cameo Systems Modeler and DOORS enables agents to operate within established model repositories rather than generating standalone artifacts [117]. Specific approaches include:
- Multi-objective optimization agents exploring architecture trade spaces [61]
- Pattern-matching agents suggesting applicable architecture patterns drawn from catalogues
- Constraint-checking agents verifying architecture decisions against requirements
- LLM-based agents generating candidate SysML models from stakeholder intent descriptions [116]

**View generation** applications produce architecture representations:
- Viewpoint-specialized agents generating views per ISO 42010 [62]
- Diagram generation agents creating visual representations
- Consistency-checking agents verifying cross-view alignment

**Interface definition** applications manage system boundaries:
- Interface identification agents detecting needed interfaces from architectures
- Interface specification agents generating interface control document (ICD) content
- Conflict detection agents identifying interface mismatches

**Trade study support** coordinates multi-criteria analysis:
- Alternative generation agents proposing design options
- Evaluation agents assessing alternatives against criteria
- Sensitivity analysis agents exploring parameter variations
- Multi-agent deliberation aggregating assessments [63]

**Maturity assessment:** Architecture applications are moderately mature. Optimization-based approaches have production use in specific domains (e.g., aerospace trade studies); LLM-based architecture agents remain largely research prototypes with limited industrial validation. The gap between single-agent assistants (which can draft individual diagrams) and multi-agent systems (which would coordinate across viewpoints and maintain cross-view consistency) remains substantial [117].

### 5.4 Verification and Validation Applications

Verification and validation (V&V) processes have substantial multi-agent application, particularly for software-intensive systems:

**Test case generation** employs agents for systematic test development. Several specialized tools have emerged: **KaneAI** provides AI-powered end-to-end test automation with natural language test authoring [118]; **Diffblue Cover** uses reinforcement learning to automatically generate unit tests for Java codebases [119]; **TestPilot** leverages LLMs to generate test cases from code context and documentation [120]; and **EvoSuite**, originally a search-based test generator, has been augmented with LLM-driven seed generation to improve coverage in complex scenarios [121]. Specific multi-agent strategies include:
- Requirements-based test generation agents deriving tests from specifications [64]
- Coverage-directed agents generating tests to maximize coverage criteria
- Adversarial agents generating challenging test cases through mutation-based and boundary-probing strategies
- Multi-agent approaches combining coverage, boundary, and fault-based strategies, where specialized agents focus on distinct testing concerns and a coordinator agent merges results [118]

**Test execution and analysis** coordinates automated testing:
- Test orchestration agents managing test execution
- Result analysis agents interpreting test outcomes
- Regression analysis agents identifying failure patterns

**Formal verification** applications support rigorous analysis. **Lean Copilot** integrates LLMs with the Lean theorem prover to suggest proof steps and lemma applications, reducing the manual effort of formal proofs [122]. DeepMind's **AlphaProof** demonstrated that reinforcement learning combined with formal reasoning can solve competition-level mathematical problems, suggesting pathways toward automated verification of system properties [123]. Specific approaches include:
- Model checking agents exploring state spaces with intelligent state pruning
- Theorem proving agents assisting formal proofs through tactic suggestion and proof search [122]
- Abstraction agents managing complexity through model reduction
- Multi-agent verification pipelines where decomposition agents partition verification tasks and specialist agents apply domain-appropriate methods [123]

**Review and inspection** applications support human review processes:
- Pre-review analysis agents identifying potential issues for human attention
- Checklist verification agents assessing completeness against criteria
- Multi-perspective review agents examining artifacts from different viewpoints [65]

**Maturity assessment:** V&V applications, particularly test generation, are relatively mature with commercial tools such as Diffblue Cover and KaneAI incorporating AI capabilities and achieving production deployment [119]. Formal verification agents remain research-focused, though tools like Lean Copilot represent significant progress toward practical usability [122]. LLM-based review support is emerging rapidly, with single-agent code review tools reaching pilot deployment while multi-agent review orchestration remains experimental.

### 5.5 Integration and Lifecycle Applications

Later lifecycle phases have received less attention but offer significant opportunities:

**Integration planning** applications support assembly sequencing:
- Dependency analysis agents identifying integration constraints
- Sequence optimization agents generating build orders
- Resource allocation agents managing integration facilities

**Transition support** applications facilitate deployment:
- Procedure generation agents creating transition plans
- Training material agents generating user documentation
- Readiness assessment agents evaluating transition prerequisites

**Operations support** applications assist in-service systems:
- Anomaly detection agents identifying unexpected behaviors
- Diagnostic agents supporting fault isolation
- Operational optimization agents suggesting efficiency improvements

**Maintenance support** applications sustain system capability:
- Failure prediction agents anticipating maintenance needs
- Sustainment planning agents optimizing maintenance schedules
- Technical refresh agents assessing modernization options

**Maturity assessment:** Lifecycle applications lag requirements and V&V in maturity. Operations and maintenance applications exist for specific domains (predictive maintenance in manufacturing) but general SE applications remain limited.

### 5.6 Cross-Cutting Applications

Some applications span multiple process areas:

**Documentation generation** produces engineering artifacts:
- Report generation agents synthesizing technical documents
- Specification writing agents creating standards-compliant documents
- Update propagation agents maintaining document consistency

**Traceability management** maintains artifact relationships:
- Link discovery agents identifying implicit relationships
- Impact analysis agents propagating changes through trace networks
- Compliance verification agents checking traceability completeness

**Configuration management** tracks artifact versions and baselines:
- Change detection agents identifying modifications
- Baseline comparison agents assessing evolution
- Configuration audit agents verifying consistency

**Project management support** assists technical management:
- Progress assessment agents evaluating completion status
- Risk identification agents surfacing technical risks
- Resource estimation agents predicting effort requirements

### 5.7 Cross-Application Integration

A critical observation from the preceding subsections is that most multi-agent SE applications operate within a single process area. Requirements agents do not communicate with architecture agents, which in turn are disconnected from V&V agents. Yet the central promise of multi-agent orchestration in SE lies precisely in cross-phase integration: a requirements change should propagate automatically to affected architecture elements, trigger re-verification of impacted test cases, and update traceability links throughout.

The concept of a **digital thread**---a continuously maintained, model-based representation linking all engineering artifacts across the lifecycle---provides a natural integration substrate for multi-agent SE systems [124]. In a fully realized digital thread, requirements agents would feed structured outputs into architecture agents, which would in turn trigger V&V agents to assess the impact of design decisions on verification plans. Multi-agent orchestration frameworks could manage this flow, with coordinator agents routing artifacts between specialist agents and monitoring cross-phase consistency [125].

Current MBSE tools such as Cameo Systems Modeler, IBM Engineering Lifecycle Management, and Siemens Teamcenter provide partial infrastructure for this vision, offering shared data repositories and standardized exchange formats (SysML, Open Services for Lifecycle Collaboration [OSLC]). However, integrating autonomous agents into these environments---enabling agents to read, modify, and create model elements while respecting access controls and process governance---remains a significant engineering challenge [124].

The state of practice is largely siloed: individual multi-agent applications achieve strong results within their process area but lack the interfaces and protocols needed for cross-application coordination. Bridging this gap represents a key research frontier. Efforts in digital engineering and the Department of Defense Digital Engineering Strategy [126] provide institutional momentum, but the agent interoperability standards and coordination protocols needed for seamless cross-phase multi-agent integration have yet to be developed.

### 5.8 Application Maturity Assessment

Table 3 summarizes application maturity across process areas.

\footnotesize

| Process Area | Research Activity | Representative Tools | Tool Availability | Industrial Adoption | Multi-Agent Maturity | Evidence Quality |
|--------------|-------------------|---------------------|-------------------|---------------------|---------------------|------------------|
| Requirements elicitation | High | Elicitron, IBM Watson | Moderate | Low-Moderate | Research prototype | Case studies |
| Requirements analysis | High | ARTE, REGAL | Moderate | Moderate | Pilot deployment | Experiments + cases |
| Architecture exploration | Moderate | AI-SysML agents, MBSE integrations | Low | Low | Research prototype | Prototypes |
| Trade studies | Moderate | Multi-objective optimization agents | Low | Low | Research prototype | Laboratory |
| Test generation | High | KaneAI, Diffblue Cover, TestPilot, EvoSuite+LLM | High | Moderate | Pilot deployment | Experiments + field |
| Formal verification | Moderate | Lean Copilot, AlphaProof | Moderate | Low | Research prototype | Laboratory |
| Review support | Emerging | LLM-based review agents | Low | Very low | Concept | Prototypes |
| Integration | Low | --- | Very low | Very low | Concept | Limited |
| Operations/maintenance | Moderate | Domain-specific predictive agents | Moderate (domain-specific) | Moderate (specific domains) | Pilot (narrow domains) | Case studies |
| Documentation | Emerging | LLM generation agents | Emerging | Very low | Concept | Prototypes |
| Cross-phase integration | Low | Digital thread prototypes | Very low | Very low | Concept | Limited |

\normalsize

### 5.9 Summary: Applications × Process × Evidence

Key observations from the application survey:

**Concentrated maturity:** Application maturity concentrates in requirements analysis and test generation, with other process areas substantially less developed.

**LLM acceleration:** LLM-based approaches are rapidly advancing across process areas, but with limited industrial validation. Most LLM applications remain research prototypes or early pilots.

**Domain specificity:** Many mature applications are domain-specific (aerospace V&V, manufacturing maintenance) rather than general SE tools.

**Multi-agent gap:** Most applications employ single agents or simple agent pairs; true multi-agent swarm approaches remain rare except in optimization contexts.

**Evidence limitations:** Rigorous empirical evaluation is limited. Many papers report prototype demonstrations without controlled experiments or industrial validation.

---

## 6. Evaluation Methods and Benchmarks

Rigorous evaluation is essential for advancing multi-agent AI systems in SE. This section surveys evaluation approaches, existing benchmarks, and gaps requiring attention.

### 6.1 Evaluation Challenges for MAS in SE

Evaluating multi-agent systems for SE presents distinctive challenges:

**Task complexity.** SE tasks involve extended reasoning, multiple artifacts, and judgment calls that resist simple correctness metrics. Unlike classification or generation tasks with clear ground truth, SE tasks often have multiple acceptable solutions.

**Interaction effects.** Multi-agent system performance depends on agent interactions, not just individual capabilities. Evaluation must capture collective behavior, coordination effectiveness, and emergent properties.

**Context dependence.** SE effectiveness depends heavily on domain, organizational context, and specific project characteristics. Results from one context may not generalize.

**Temporal scope.** SE processes span extended periods; full evaluation of lifecycle support requires longitudinal assessment impractical for most research studies.

**Human factors.** Effectiveness ultimately depends on human engineer productivity, satisfaction, and trust—subjective factors difficult to measure in controlled settings.

### 6.2 Existing Benchmarks and Datasets

The field lacks standardized benchmarks for multi-agent SE applications. Relevant existing resources include:

**Software engineering benchmarks:**
- HumanEval, MBPP for code generation [66]
- SWE-bench for repository-level coding tasks [67], and its curated variant **SWE-bench Verified** providing human-validated solutions for more reliable evaluation [127]
- **MLE-bench** for machine learning engineering tasks requiring multi-step reasoning and tool use [128]
- These address software engineering specifically, not broader SE

**Requirements engineering datasets:**
- PURE dataset of requirements and domain knowledge [68]
- NFR dataset for requirements classification
- **SUPER** (Systems engineering Understanding and Processing for Engineering Requirements), an SE-specific benchmark for understanding and processing engineering requirements documents [130]
- Limited scale and domain coverage, though SUPER represents a step toward SE-specific evaluation

**Reasoning and mathematical benchmarks:**
- **MATH** and **GSM8K** for mathematical reasoning evaluation, relevant to formal specification and verification tasks
- These assess foundational reasoning capabilities needed for formal SE analyses

**General agent benchmarks:**
- AgentBench for LLM agent capabilities [69]
- GAIA for general AI assistants [70]
- **ToolBench** for evaluating tool-use capabilities across diverse APIs and toolchains [129]
- **Tau-bench** for benchmarking tool-agent-user interaction quality in realistic task settings
- WebArena for web-based tasks
- These assess general capabilities, not SE-specific performance

**Multi-agent benchmarks:**
- ChatArena for multi-agent dialogue
- Limited coverage of collaborative task completion relevant to engineering contexts

**Gap:** No comprehensive benchmark suite exists for multi-agent systems applied to SE processes. Existing benchmarks either target narrow software engineering tasks or assess general agent capabilities without the domain richness, multi-artifact complexity, and lifecycle scope characteristic of SE.

### 6.3 Metrics Used in Literature

Studies evaluating AI applications in SE employ varied metrics:

**Task-specific metrics:**
- Requirements completeness (percentage of expected requirements identified)
- Defect detection rate (percentage of seeded defects found)
- Test coverage achieved
- Design space coverage

**Quality metrics:**
- Accuracy (correctness of outputs)
- Precision/recall for classification tasks
- BLEU/ROUGE for generation tasks (limited applicability to SE)

**Efficiency metrics:**
- Time to completion
- Token usage / computational cost
- Human effort reduction

**Coordination metrics:**
- Communication volume
- Convergence time
- Conflict frequency and resolution

**Human-centered metrics:**
- User satisfaction (survey-based)
- Trust measures
- Cognitive load
- Adoption intention

### 6.4 Gaps in Evaluation Methods

Critical gaps limit rigorous evaluation:

**Benchmark absence.** No standard benchmarks enable cross-study comparison of multi-agent SE systems. Each study uses different tasks, datasets, and metrics, preventing cumulative progress assessment.

**Realism deficit.** Available datasets often lack the complexity, scale, and domain richness of real SE problems. Toy problems may not predict performance on realistic tasks.

**Coordination evaluation.** Methods for assessing multi-agent coordination quality—beyond simple task completion—remain underdeveloped. How do we measure whether coordination was efficient, robust, or appropriate?

**Longitudinal methods.** Evaluating lifecycle support requires methods for assessing systems over extended periods and across multiple project phases—rarely practical in research settings.

**Human-AI teaming evaluation.** Methods for assessing human-AI collaboration effectiveness—not just AI capability in isolation—need development. How do we measure whether the human-AI team performs better than human-only or AI-only alternatives?

### 6.5 Toward SE-Specific Benchmarks

Addressing evaluation gaps requires community investment in benchmark development:

**Task suite development.** Creating standardized task suites for each SE process area, with realistic complexity, domain diversity, and ground truth or expert reference solutions.

**Evaluation protocol standardization.** Establishing common evaluation protocols enabling fair comparison across systems, including standard train/test splits, evaluation procedures, and reporting requirements.

**Multi-dimensional metrics.** Developing metrics capturing multiple performance dimensions—correctness, efficiency, coordination quality, human compatibility—rather than single-number summaries.

**Living benchmarks.** Creating benchmarks that evolve as capabilities advance, preventing saturation while maintaining comparability through versioning.

**Community infrastructure.** Building shared infrastructure for benchmark hosting, evaluation automation, and result aggregation enabling efficient community-wide evaluation.

An SE-specific benchmark suite should exhibit several distinctive characteristics that differentiate it from existing software engineering or general agent benchmarks. First, tasks should be **multi-artifact**, requiring agents to produce or modify multiple related artifacts (requirements specifications, architecture models, test plans) rather than single outputs. Second, benchmarks should assess **cross-artifact consistency**---whether generated test cases actually trace to stated requirements, and whether architecture decisions satisfy constraints. Third, tasks should encode **domain knowledge requirements**, such as compliance with standards (DO-178C for avionics, ISO 26262 for automotive safety), to evaluate agents' ability to operate within regulatory contexts. Fourth, benchmarks should include **long-horizon tasks** spanning multiple SE phases, from initial requirements through design and verification, to assess sustained coherence across the lifecycle. Finally, for multi-agent systems specifically, benchmarks should incorporate **collaboration metrics** that evaluate coordination quality: communication efficiency, conflict resolution effectiveness, and the degree to which agent specialization improves outcomes beyond what monolithic approaches achieve [131].

However, developing such benchmarks presents substantial challenges. **Ground truth is ambiguous**: unlike code generation where test cases provide binary pass/fail feedback, many SE tasks admit multiple valid solutions, making automated scoring difficult. **Domain expert involvement** is essential for task design and solution evaluation, yet expert time is scarce and expensive. **Proprietary data restrictions** limit the availability of realistic industrial SE artifacts for public benchmark use. The **rapidly evolving state of the art** risks making benchmarks obsolete quickly, as capabilities that distinguish systems today may become trivial within months. Finally, a **scale mismatch** exists between the toy-scale problems tractable for research evaluation and the large-scale, long-duration projects where SE agent support would deliver the most value.

Benchmark development requires collaboration between AI researchers and SE practitioners to ensure benchmarks reflect realistic engineering challenges while remaining tractable for research evaluation.

---

## 7. Tools and Frameworks

This section surveys tools and frameworks enabling multi-agent AI system development, from classical MAS platforms through contemporary LLM-based frameworks, and examines integration with SE tools.

### 7.1 Multi-Agent Platforms

Classical multi-agent platforms provide infrastructure for agent development and deployment:

**JADE (Java Agent DEvelopment Framework)** [71] provides Foundation for Intelligent Physical Agents (FIPA)-compliant agent infrastructure including agent lifecycle management, communication, and directory services. Widely used in research and education, JADE offers mature infrastructure but requires substantial development effort for sophisticated agents.

**SPADE (Smart Python Agent Development Environment)** [72] offers Python-based agent development with XMPP-based communication. Its Python foundation facilitates integration with modern AI libraries.

**Jason** [73] implements the AgentSpeak language for BDI agent development, providing declarative agent programming with explicit beliefs, goals, and plans. Jason suits applications requiring explainable agent reasoning.

**MASON** [74] provides a fast discrete-event multi-agent simulation library in Java, suited for large-scale agent-based modeling and simulation.

**Mesa** [75] offers Python-based agent-based modeling, providing accessible agent-based modeling (ABM) capabilities with visualization support.

**Limitations for SE:** Classical platforms require explicit agent programming and lack native integration with LLM capabilities. They provide infrastructure but not the reasoning capabilities modern SE applications require.

### 7.2 LLM-Based Agent Frameworks

The emergence of LLMs has spawned frameworks specifically supporting LLM-based agents:

**LangChain** [76] provides abstractions for LLM application development including chains, agents, and tools. LangChain agents can use tools, maintain memory, and execute multi-step reasoning. Widely adopted with extensive tool ecosystem.

**LlamaIndex** [77] focuses on connecting LLMs with external data through indexing and retrieval, enabling RAG-based applications. Strong support for document processing and knowledge integration.

**AutoGPT** [78] pioneered autonomous LLM agents pursuing goals through iterative reasoning and action. Demonstrated potential for autonomous task completion but also limitations in reliability and control.

**MetaGPT** [79] implements multi-agent software development with specialized roles (product manager, architect, engineer). Demonstrates role-based multi-agent patterns for software engineering tasks.

**CrewAI** [80] provides framework for orchestrating role-based agent "crews" with defined roles, goals, and collaboration patterns. Emphasizes agent specialization and coordination.

**AutoGen** [81] from Microsoft supports conversational agents with customizable interaction patterns, enabling flexible multi-agent dialogue configurations.

**LangGraph** [82] extends LangChain with graph-based agent orchestration, supporting complex multi-agent workflows with explicit state management and control flow.

**OpenHands** (formerly OpenDevin) [98] provides an open-source agent platform for software engineering tasks with sandboxed execution environments, enabling agents to safely write, test, and debug code in isolated containers.

**Claude Code** (Anthropic) [100] is an agentic coding assistant with direct terminal access, file editing capabilities, and integration via the Model Context Protocol (MCP), allowing tool-augmented workflows within a developer's local environment.

**Cursor** [132] represents the AI-first code editor paradigm, deeply integrating LLM agents into the development workflow with context-aware code generation and multi-file editing.

**GitHub Copilot Workspace** [133] extends the Copilot ecosystem into a multi-agent workspace for planning and implementing changes across entire repositories, bridging issue tracking with automated code generation.

**Amazon Q Developer** [134] provides an AWS-integrated AI developer agent supporting code generation, transformation, and debugging within cloud-native development workflows.

**OpenAI Swarm** [101] offers a lightweight experimental multi-agent framework emphasizing agent handoffs and routines as first-class coordination primitives, prioritizing simplicity over infrastructure complexity.

#### 7.2.1 Emerging Patterns

Several cross-cutting patterns are emerging across LLM-based agent frameworks. The **Model Context Protocol (MCP)** is gaining traction as an open standard for tool-agent integration, providing a uniform interface through which agents discover and invoke external tools regardless of the underlying framework [100]. **Agent-computer interfaces** are diversifying beyond API calls to include terminal interaction, browser automation, and GUI manipulation, expanding the range of tasks agents can perform. **Sandboxed execution environments** — containerized or virtualized workspaces in which agents execute code and system commands — are becoming a standard safety mechanism, mitigating the risks of autonomous agent operation [98]. Finally, **agent marketplaces and plugin ecosystems** are emerging around major platforms, enabling composable agent capabilities and accelerating adoption through community-contributed integrations.

**Comparison considerations:**
- LangChain/LlamaIndex: General-purpose, extensive ecosystem
- MetaGPT/CrewAI: Role-based specialization, team metaphors
- AutoGen: Conversational patterns, research-oriented
- LangGraph: Workflow orchestration, state management
- OpenHands/Claude Code/Cursor: Developer-facing agentic tools with environment access
- Copilot Workspace/Amazon Q: Platform-integrated enterprise agents
- OpenAI Swarm: Minimalist multi-agent coordination

### 7.3 SE Tool Integration

Effective multi-agent SE applications require integration with existing engineering tools:

**MBSE tools:**
- Cameo Systems Modeler / MagicDraw (SysML modeling) — exposes a REST API for programmatic model element creation, query, and modification, enabling agents to read and update SysML diagrams
- IBM Engineering Systems Design Rhapsody
- Capella (MBSE for systems architects)
- Integration typically via APIs, model import/export, or direct database access

**Requirements management:**
- IBM DOORS Next Generation provides a RESTful OSLC-compliant API through which agents can query, create, and trace requirements across modules
- Jama Connect
- Polarion
- Integration enables AI agents to read, analyze, and potentially update requirements

**PLM / Product Data Management (PDM) systems:**
- Siemens Teamcenter
- PTC Windchill
- Dassault 3DEXPERIENCE
- Integration provides access to product data, configurations, and workflows

**Application Lifecycle Management (ALM) tools:**
- Jira (issue/task tracking)
- Azure DevOps
- GitLab
- Integration supports workflow coordination and artifact management

**Standards-based integration:** The Open Services for Lifecycle Collaboration (OSLC) specification provides a set of RESTful web service standards for lifecycle tool integration, offering a potential uniform interface layer through which agents can interact with heterogeneous SE tools. Digital thread platforms — which maintain linked traceability across requirements, design, implementation, and test artifacts — represent a promising integration substrate, as they aggregate the cross-lifecycle data that multi-agent SE systems require.

**Integration challenges:**
- Proprietary APIs and data formats
- Authentication and access control
- Data consistency and transaction management
- Performance at scale

### 7.4 Capability Comparison

Table 4 compares framework capabilities relevant to SE applications.

\footnotesize

| Framework | Multi-Agent | Memory | Tools | Planning | SE Integration | Maturity |
|-----------|-------------|--------|-------|----------|----------------|----------|
| JADE | Native | Custom | Custom | Custom | Low | High |
| Jason | Native | BDI | Custom | BDI | Low | Moderate |
| LangChain | Via agents | Yes | Extensive | Via prompts | Moderate | High |
| AutoGen | Native | Yes | Moderate | Via dialogue | Low | Moderate |
| CrewAI | Native | Yes | Moderate | Role-based | Low | Moderate |
| MetaGPT | Native | Yes | Code-focused | Workflow | Low (SW only) | Moderate |
| LangGraph | Native | Yes | Via LangChain | Graph-based | Moderate | Emerging |
| OpenHands | Native | Yes | Sandboxed exec | Task-based | Low (SW only) | Emerging |
| Claude Code | Via MCP | Yes | MCP ecosystem | Agentic | Moderate | Emerging |
| Cursor | Via editor | Yes | Editor-native | Inline | Low (SW only) | Emerging |
| Copilot Workspace | Native | Yes | GitHub-native | Issue-to-PR | Low (SW only) | Emerging |
| Amazon Q | Via AWS | Yes | AWS services | Task-based | Low | Emerging |
| OpenAI Swarm | Native | Minimal | Custom | Handoff-based | Low | Experimental |

\normalsize

**Observations:**
- No framework provides native SE tool integration; custom development required
- LLM-based frameworks offer superior reasoning but less multi-agent infrastructure
- Classical platforms offer robust infrastructure but lack modern AI capabilities
- Gap exists for SE-specific multi-agent frameworks
- Newer agentic tools (OpenHands, Claude Code, Cursor) emphasize environment access and sandboxed execution but remain oriented toward software engineering rather than broader SE disciplines

**Emerging direction:** Hybrid approaches combining classical MAS infrastructure (coordination, lifecycle) with LLM-based reasoning capabilities may address current limitations.

**Framework selection criteria.** Practitioners evaluating frameworks for SE applications should consider several dimensions: (1) native multi-agent support and coordination mechanisms, (2) breadth of the tool ecosystem and extensibility via protocols such as MCP, (3) potential for integration with domain-specific SE tools (MBSE platforms, requirements managers, PLM systems), (4) scalability with respect to agent count and artifact volume, (5) cost structure including LLM inference costs, (6) open-source availability and licensing terms, and (7) community maturity and long-term maintenance trajectory. At present, no single framework satisfies all of these criteria simultaneously; SE-specific deployments will likely require composing capabilities from multiple frameworks or extending an existing platform with custom integrations.

---

## 8. Challenges and Open Problems

Despite promising research directions, substantial challenges impede practical adoption of multi-agent AI systems in SE. This section categorizes and analyzes key challenges.

### 8.1 Technical Challenges

**Scalability.** As agent count increases, coordination overhead grows — potentially faster than capability gains [135]. Communication volume, conflict frequency, and convergence time may scale poorly. Research questions: What coordination mechanisms scale effectively? Where are the practical limits of swarm size? (See Section 9.1 for proposed research directions addressing scalability.)

**Reliability.** LLM-based agents exhibit unpredictable failures — hallucinations, reasoning errors, instruction drift [136]. Multi-agent systems can amplify failures through error propagation or exhibit emergent failure modes. For example, LLM agents generating requirements may introduce plausible-sounding but unverifiable specifications; in a multi-agent pipeline, downstream architecture and V&V agents may propagate rather than catch such errors [135]. Research questions: How can agent reliability be characterized and bounded? What architectural patterns improve robustness? (See Section 9.2 for proposed research directions addressing reliability.)

**Domain knowledge integration.** Effective SE support requires deep domain knowledge that current LLMs may lack or represent incorrectly [137]. Engineering domains require understanding of physical constraints, standards compliance, and organizational practices that may not be well-represented in LLM training data [136]. RAG helps but does not solve fundamental knowledge gaps. Research questions: How can domain constraints be reliably encoded? How can physics-based reasoning be integrated with language model capabilities? (See Section 9.3 for proposed research directions addressing domain knowledge.)

**Consistency maintenance.** Multi-agent systems generating or modifying engineering artifacts must maintain artifact consistency [138]. Concurrent modifications can introduce conflicts; coordination must ensure coherent results. Research questions: What consistency models suit SE artifacts? How should conflicts be detected and resolved?

**Performance.** LLM inference is computationally expensive; multi-agent systems multiply this cost [135]. Latency may exceed acceptable bounds for interactive applications. Research questions: What efficiency improvements are possible? How should computation be allocated across agents?

### 8.2 Integration Challenges

**Tool integration.** Connecting agent systems with SE tools (MBSE platforms, requirements management, PLM) requires substantial integration effort [139]. Proprietary APIs, data formats, and access models complicate integration. Emerging standards such as OSLC provide partial solutions, but coverage remains incomplete and adoption uneven [140]. Research questions: What integration patterns are effective? Can standardized interfaces emerge? (See Section 9.4 for proposed research directions addressing tool integration.)

**Process integration.** Inserting AI agents into established SE processes raises workflow questions [141]. Where do agents participate? How are agent outputs reviewed? How do agent activities align with milestone gates? Research questions: What process adaptations are needed? How should traditional and AI-augmented processes coexist?

**Data integration.** Agent systems require access to engineering data — requirements, models, test results — often distributed across systems with different formats and access controls [139]. Research questions: How can engineering data be made agent-accessible? What data quality requirements apply?

**Legacy system accommodation.** Most SE organizations have substantial investments in existing tools and processes [140]. Agent systems must accommodate legacy constraints rather than requiring greenfield adoption. Research questions: What migration paths are practical? How can value be delivered incrementally?

### 8.3 Human Factors Challenges

**Trust calibration.** Engineers must develop appropriate trust in agent capabilities — neither over-reliance nor excessive skepticism [137]. Trust should be task-specific and evidence-based. Studies in human-robot teaming suggest that trust calibration requires transparent performance feedback and predictable failure modes [137] — characteristics that current LLM agents struggle to provide. Research questions: How does trust develop? What factors support appropriate calibration? How should trust be maintained as capabilities evolve? (See Section 9.5 for proposed research directions addressing trust.)

**Oversight effectiveness.** Human oversight of agent activities becomes challenging as agent count and activity rate increase [142]. Engineers cannot review every agent output; effective oversight requires attention management. Research questions: What oversight models are effective? How should agent outputs be prioritized for review?

**Skill evolution.** Working effectively with agent systems requires skills many engineers lack: formulating effective prompts, evaluating AI outputs, diagnosing agent failures [143]. Research questions: What skills are needed? How should training be structured? How do required skills evolve with technology?

**Cognitive load.** Managing agent systems imposes cognitive demands: understanding agent state, interpreting agent outputs, coordinating agent activities [142]. These demands may offset productivity gains. Research questions: How can cognitive load be managed? What interface designs minimize burden?

**Role clarity.** As agents assume engineering tasks, human roles must evolve [144]. Unclear role boundaries create confusion about responsibilities. Research questions: How should human-agent roles be defined? How should accountability be allocated? (See Section 9.6 for proposed research directions addressing human-agent teaming.)

### 8.4 Organizational Challenges

**Governance frameworks.** Organizations need frameworks governing AI involvement in engineering [145]. What decisions can agents make? How are agent outputs validated? Who is accountable for agent contributions? Research questions: What governance models are appropriate? How should governance evolve with capability? (See Section 9.7 for proposed research directions addressing governance.)

**Certification implications.** In regulated industries, AI involvement raises certification questions [146]. How do AI contributions affect system certification? What evidence is required for AI tool qualification? Research questions: What certification frameworks apply? How should evidence be collected and presented?

**Liability and accountability.** When AI-influenced engineering decisions lead to problems, liability questions arise [145]. Current legal frameworks may not adequately address AI contributions. Research questions: How should liability be allocated? What organizational structures support appropriate accountability?

**Intellectual property.** Deploying AI agents on proprietary engineering data raises intellectual property concerns [147]. Organizations must determine whether agent interactions with proprietary designs, trade secrets, or export-controlled data create unacceptable exposure risks, particularly when using cloud-hosted LLM services. Data residency, model training data provenance, and output ownership require careful contractual and technical controls.

**Workforce transition.** The introduction of agent systems will shift the skill profiles required of systems engineers [146]. Organizations must plan for workforce transition — retraining engineers to supervise and collaborate with AI agents rather than perform tasks agents can handle — while managing the cultural and morale implications of role redefinition.

**Standards body engagement.** Realizing the potential of multi-agent AI for SE will require engagement from standards bodies including INCOSE, IEEE, and ISO [147]. Standards are needed for agent-generated artifact quality, human-agent process interfaces, and certification of AI-augmented engineering workflows. Without such standards, adoption will remain fragmented and organization-specific.

**Change management.** Adopting agent systems represents significant organizational change [145]. Resistance, skill gaps, and process disruption must be managed. Research questions: What adoption approaches succeed? How should change be paced?

**Economic justification.** Agent system adoption requires investment; organizations need evidence of return [146]. Current evidence is limited and context-dependent. Research questions: What value propositions are compelling? How should benefits be measured?

### 8.5 Challenge Prioritization

Table 5 assesses challenges by severity and tractability.

\footnotesize

| Challenge | Severity | Tractability | Priority |
|-----------|----------|--------------|----------|
| Reliability | High | Moderate | Critical |
| Domain knowledge | High | Moderate | Critical |
| Trust calibration | High | Moderate | Critical |
| Governance | High | Low | High |
| Scalability | Moderate | Moderate | High |
| Tool integration | Moderate | High | High |
| Certification | High | Low | High |
| Oversight | Moderate | Moderate | Medium |
| Performance | Moderate | High | Medium |
| Skills evolution | Moderate | High | Medium |

\normalsize

Critical challenges (high severity, moderate tractability) warrant immediate research investment. High-priority challenges are either severe or tractable and should receive sustained attention.

---

## 9. Research Directions

Based on the survey findings and challenge analysis, this section proposes research directions organized by time horizon.

### 9.1 Near-Term Research Priorities (1-3 years)

**Benchmark development.** The field urgently needs standardized benchmarks for evaluating multi-agent AI systems in SE contexts. Existing efforts such as SWE-bench [66] and AgentBench [69] address software engineering tasks but do not capture the breadth of SE processes. Near-term efforts should:
- Develop task suites for key SE processes (requirements analysis, architecture evaluation, test generation)
- Establish evaluation protocols enabling cross-study comparison
- Create shared datasets with realistic complexity and domain diversity
- Build community infrastructure for benchmark hosting and evaluation automation

*RQ: What task characteristics and metrics best capture multi-agent system effectiveness across SE process areas?*

**Reliability characterization.** Understanding when and how agent systems fail is essential for responsible deployment. Emerging work on LLM hallucination detection [148] and constitutional AI [149] provides relevant foundations, but SE-specific failure modes remain underexplored:
- Develop taxonomies of failure modes for multi-agent SE systems
- Create methods for detecting and diagnosing agent failures
- Establish reliability metrics appropriate for SE applications
- Design architectural patterns that improve robustness

*RQ: What failure mode taxonomies and detection methods can characterize multi-agent system reliability for safety-critical SE applications?*

**Domain knowledge grounding.** Improving agent access to authoritative domain knowledge:
- Develop retrieval approaches specialized for SE knowledge sources (standards, handbooks, domain literature)
- Create methods for encoding domain constraints as verifiable bounds
- Investigate hybrid architectures combining LLM reasoning with physics-based analysis
- Build domain-specific knowledge bases in machine-accessible formats

**Tool integration patterns.** Enabling practical integration with SE tools:
- Develop integration reference architectures for common SE tools (MBSE, requirements management, PLM)
- Create abstraction layers reducing tool-specific development effort
- Establish protocols for agent-tool interaction
- Build open-source integration examples accelerating adoption

### 9.2 Medium-Term Research Agenda (3-7 years)

**Coordination at scale.** Enabling effective coordination among larger agent populations:
- Develop theoretical models predicting coordination overhead as a function of swarm characteristics
- Design hierarchical and hybrid coordination architectures that scale
- Investigate emergent coordination mechanisms with predictable properties
- Create simulation environments for studying large-scale swarm behavior

*RQ: How does coordination overhead scale with agent count, and what architectural patterns maintain effectiveness at scale?*

**Human-AI teaming.** Understanding and supporting effective collaboration between engineers and agent systems. Research on coactive design [150] and trust calibration [151] provides starting points, but multi-agent settings introduce unique challenges:
- Develop models of human-agent team performance predicting when collaboration helps
- Design interfaces supporting effective oversight of multi-agent activities
- Investigate trust development and calibration in engineering contexts
- Create training approaches preparing engineers for agent collaboration

*RQ: What interface designs and oversight models enable effective engineer-agent collaboration without imposing excessive cognitive load?*

**Evaluation methodology.** Advancing how we assess multi-agent SE systems:
- Develop methods for evaluating coordination quality beyond task completion
- Create longitudinal evaluation approaches for lifecycle support
- Establish metrics for human-AI team effectiveness
- Design evaluation frameworks accommodating evolving capabilities

**Governance frameworks.** Establishing structures for responsible deployment. The NIST AI Risk Management Framework [152] and EU AI Act [153] provide regulatory foundations, but SE-specific governance guidance remains nascent:
- Develop accountability frameworks clarifying human and agent responsibilities
- Create audit and provenance mechanisms for agent contributions
- Investigate certification approaches for AI-assisted engineering
- Design organizational models supporting appropriate AI involvement

### 9.3 Long-Term Research Vision (7+ years)

**Collective engineering intelligence.** Moving beyond agent systems as tools toward genuine collaborative intelligence:
- Understand how human-AI teams can achieve capabilities neither could alone
- Investigate emergent properties of sustained human-AI engineering collaboration
- Develop frameworks for knowledge accumulation across projects and organizations
- Create approaches for preserving and transferring engineering expertise through AI systems

*RQ: Under what conditions do human-AI engineering teams exhibit capabilities that neither humans nor AI alone can achieve?*

**Self-improving systems.** Enabling agent systems that improve from experience:
- Develop learning mechanisms improving agent performance from deployment experience
- Create approaches for agents to identify and address their own limitations
- Investigate safe self-modification within bounded authority
- Design systems that improve while maintaining reliability

**Engineering automation boundaries.** Understanding appropriate automation scope:
- Investigate which SE activities benefit from human execution versus AI execution
- Develop principled approaches for allocating tasks between humans and agents
- Create frameworks for evolving automation boundaries as capabilities and trust develop
- Study long-term implications of automation for engineering practice and workforce

### 9.4 Cross-Disciplinary Opportunities

Progress requires contributions from multiple research communities:

**AI and machine learning:** Foundation model capabilities, multi-agent coordination, tool use, reliability

**Software engineering:** Development methodologies, testing, tool integration, process models

**SE:** Domain expertise, process knowledge, practitioner insight, adoption requirements

**Human factors:** Trust, teaming, interface design, cognitive load, skill requirements

**Organizational science:** Governance, change management, accountability, workforce evolution

**Philosophy and ethics:** Responsibility allocation, appropriate automation, societal implications

Sustained progress requires cross-disciplinary collaboration—AI researchers understanding SE practice, SE practitioners guiding AI development, human factors researchers studying collaboration, organizational scientists addressing adoption.

### 9.5 Community Building

Realizing the research agenda requires community infrastructure:

**Research consortia.** Establishing focused research programs bringing together AI and SE researchers with industrial partners

**Shared infrastructure.** Building common benchmarks, datasets, and evaluation platforms

**Publication venues.** Developing venues spanning AI and SE communities

**Educational programs.** Creating curricula preparing researchers for cross-disciplinary work

**Industrial partnerships.** Engaging practitioners in research direction setting and validation

### 9.6 Research Methodology Recommendations

Advancing this field demands methodological rigor commensurate with its complexity. We recommend mixed-methods approaches that combine controlled experiments—measuring agent performance on well-defined tasks—with industrial case studies capturing real-world deployment contexts and constraints. Longitudinal studies are particularly important for evaluating lifecycle support, where agent contributions may manifest over months or years rather than in single-session experiments. Given the rapid pace of LLM capability improvement, replication studies are essential; findings from one model generation may not generalize to the next, and the community must establish which results are robust to underlying model changes. Finally, open science practices—shared benchmarks, open datasets, pre-registered hypotheses, and reproducible experimental protocols—will accelerate cumulative progress and enable the cross-study comparisons that the field currently lacks.

---

## 10. Conclusion

This survey has provided a systematic examination of multi-agent AI systems for SE, synthesizing contributions from artificial intelligence, software engineering, SE, and human factors research communities.

### Summary of Findings

This survey synthesized literature spanning 150+ publications across AI, software engineering, SE, and human factors communities. We identified four major agent architecture families, six coordination mechanism categories, and mapped applications across 14 ISO 15288 technical process areas. Our analysis revealed concentrated maturity in two process areas (requirements analysis and test generation) with substantial gaps across the remaining lifecycle.

We traced the foundations of this emerging field through multi-agent systems, swarm intelligence, and LLM-based agentic AI, establishing the rationale for multi-agent approaches to SE support. Our taxonomy of agent architectures identified the shift from classical BDI and reactive designs toward LLM-based agents with tool use and memory capabilities. Analysis of coordination mechanisms revealed trade-offs between predictability and flexibility, scalability and control, that must be navigated for SE applications.

Evaluation methods and benchmarks remain underdeveloped, limiting rigorous progress assessment. Tools and frameworks are maturing rapidly, though SE-specific integration remains limited. We identified critical challenges in reliability, domain knowledge integration, trust calibration, and governance—challenges that must be addressed for responsible adoption.

### Key Takeaways

For researchers, this survey provides organized access to a fragmented literature and identifies high-priority gaps warranting investigation. For practitioners, it offers a map of current capabilities and realistic assessment of maturity levels. For the broader community, it establishes common vocabulary and frameworks enabling cumulative progress.

### Looking Forward

The field stands at an inflection point. Foundational capabilities exist; challenges are identified; directions are clear. The research agenda we propose—from near-term benchmark development and reliability characterization through medium-term human-AI teaming and governance frameworks to long-term collective engineering intelligence—provides a structured path forward. Progress requires sustained research investment, cross-disciplinary collaboration, and engagement between researchers and practitioners. The potential prize—substantially augmented engineering capability for addressing society's complex challenges—justifies the effort required.

We invite the community to build upon this survey, address the gaps identified, and realize the potential of multi-agent AI for SE.

---

## References

*[Note: Reference numbers [1]–[153] are cited throughout this paper. The complete bibliography is maintained separately and will be integrated during final manuscript preparation. Key reference categories include:*

*[1]–[28]: Foundational references — multi-agent systems, swarm intelligence, LLMs, agentic AI, systems engineering standards*

*[29]–[44]: Agent architectures — reactive, BDI, hybrid, LLM-based frameworks (MetaGPT, AutoGen, CrewAI, LangGraph)*

*[45]–[54]: Coordination mechanisms — communication, organization, emergent approaches*

*[55]–[65]: SE applications — requirements, architecture, V&V, lifecycle*

*[66]–[70]: Evaluation benchmarks — HumanEval, SWE-bench, AgentBench, GAIA*

*[71]–[82]: Tools and frameworks — JADE, SPADE, Jason, LangChain, LlamaIndex, AutoGPT*

*[83]: PRISMA guidelines*

*[84]–[88]: Swarm intelligence engineering applications — ACO, PSO, stigmergy*

*[89]–[96]: Recent LLMs and agentic capabilities — GPT-4, Claude, Gemini, Llama, Mistral, MCP, coding tools, GUI agents*

*[97]–[103]: Autonomous SE agents and architectural convergence — SWE-agent, OpenHands, Devin, Claude Code, OpenAI Swarm*

*[104]–[111]: Coordination implementations and failures — MetaGPT, AutoGen, CrewAI, LangGraph, ChatDev coordination; token economics; echo chambers; cascading failures*

*[112]–[126]: SE application tools — Elicitron, IBM Watson, ARTE/REGAL, SysML agents, KaneAI, Diffblue, TestPilot, EvoSuite, Lean Copilot, AlphaProof, digital thread, DoD DES*

*[127]–[131]: Evaluation benchmarks — SWE-bench Verified, MLE-bench, ToolBench, SUPER, SE benchmark characteristics*

*[132]–[134]: Emerging developer tools — Cursor, GitHub Copilot Workspace, Amazon Q Developer*

*[135]–[147]: Challenges — scalability, reliability, domain knowledge, consistency, tool integration, process, trust, oversight, skills, governance, certification, IP, standards*

*[148]–[153]: Research directions — hallucination detection, constitutional AI, coactive design, trust calibration, NIST AI RMF, EU AI Act]*

---

*Manuscript compiled: February 2026*
*Draft version: 0.2*
*Total sections: 10 + Abstract*
*Tables: 5*
*Approximate word count: ~10,500*
