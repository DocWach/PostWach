# Section 2: Background and Foundations

**Target length:** ~1,200 words
**Status:** Draft v0.1

---

## 2. Background and Foundations

This section establishes the foundational concepts underlying multi-agent AI systems for systems engineering, tracing the evolution of relevant research areas and defining the intersection that motivates this survey.

### 2.1 Multi-Agent Systems: Historical Development

Multi-agent systems (MAS) emerged as a distinct research area in the 1980s and 1990s, drawing from distributed artificial intelligence, object-oriented programming, and concurrent systems [1, 2]. Wooldridge and Jennings [3] provided influential definitions, characterizing agents as computer systems capable of autonomous action in some environment to meet design objectives. Key properties include autonomy (operating without direct intervention), social ability (interacting with other agents), reactivity (perceiving and responding to environment), and proactivity (taking initiative toward goals).

Early MAS research addressed fundamental questions: How should agents be designed internally? How should agents communicate and coordinate? How do collective behaviors emerge from individual actions? Foundational work established agent communication languages (KQML, FIPA-ACL), coordination mechanisms (contract net, organizational structures), and agent architectures (reactive, deliberative, hybrid) [4, 5, 6].

By the 2000s, MAS had found applications across domains including manufacturing, logistics, e-commerce, and simulation. However, the symbolic AI approaches underlying most MAS work faced limitations in handling uncertainty, learning from experience, and processing unstructured information—limitations that constrained applicability to complex real-world problems.

### 2.2 Swarm Intelligence: Principles and Paradigms

Swarm intelligence emerged from study of collective behavior in biological systems—ant colonies, bird flocks, fish schools—where simple individuals following local rules produce sophisticated collective behavior [7, 8]. Bonabeau, Dorigo, and Théraulaz [9] formalized swarm intelligence principles and demonstrated applications to optimization problems.

Key swarm intelligence paradigms include:

**Ant Colony Optimization (ACO)** models how ants find shortest paths through pheromone-based stigmergic coordination [10]. Artificial ants deposit virtual pheromone on solution components, guiding subsequent ants toward promising solutions. ACO has proven effective for combinatorial optimization problems including routing, scheduling, and assignment.

**Particle Swarm Optimization (PSO)** models flocking behavior, with particles (candidate solutions) moving through search spaces influenced by their own best-known position and the swarm's best-known position [11]. PSO has found wide application in continuous optimization.

**Stigmergic coordination** provides a paradigm for indirect communication through environmental modification—agents leave traces that influence other agents' behavior without direct message exchange [12]. This enables scalable coordination with minimal communication overhead.

Swarm intelligence contributes key insights to AI swarms: that collective intelligence can exceed individual capability, that simple local rules can produce complex global behavior, and that decentralized coordination can achieve robust, scalable solutions.

### 2.3 Large Language Models and Agentic AI

The emergence of large language models (LLMs) since 2018 has transformed the landscape for AI agent development [13, 14]. Models trained on massive text corpora exhibit emergent capabilities in language understanding, reasoning, and generation that earlier approaches could not achieve [15].

The transition from LLMs to agentic AI involves augmenting language models with capabilities for autonomous action:

**Tool use** enables LLMs to invoke external tools—calculators, search engines, APIs, code interpreters—extending their capabilities beyond text generation [16, 17]. Tool-augmented LLMs can retrieve information, execute computations, and interact with external systems.

**Memory systems** provide LLMs with persistent context beyond their context window, enabling accumulation of knowledge across interactions [18]. Memory architectures include retrieval-augmented generation (RAG), vector databases, and structured knowledge stores.

**Planning and reasoning** approaches enable LLMs to decompose complex tasks, reason about action sequences, and pursue goals over extended interactions [19, 20]. Techniques include chain-of-thought prompting, ReAct (reasoning + acting), and tree-of-thought exploration.

**Multi-agent LLM systems** extend agentic AI to multiple coordinated agents, each potentially with specialized roles, capabilities, or perspectives [21, 22, 23]. Recent frameworks including AutoGPT, MetaGPT, CrewAI, and others demonstrate multi-agent architectures where LLM-based agents collaborate on complex tasks.

### 2.4 Systems Engineering Process Framework

Systems engineering provides the disciplined processes for managing complex system development across the lifecycle [24, 25]. ISO/IEC/IEEE 15288:2023 [26] defines the standard framework of system lifecycle processes, organized into:

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

The INCOSE Systems Engineering Handbook [27] and NASA Systems Engineering Handbook [28] provide guidance on applying these processes across domains. Systems engineering applies to any complex system—aerospace, defense, healthcare, energy, transportation, infrastructure—making it inherently domain-agnostic while requiring domain-specific knowledge for application.

### 2.5 Intersection: Why Multi-Agent AI for Systems Engineering?

The convergence of multi-agent systems, swarm intelligence, and LLM-based agentic AI creates new possibilities for systems engineering support. Several characteristics of systems engineering motivate multi-agent approaches:

**Multi-disciplinary nature.** Systems engineering integrates contributions from diverse disciplines—mechanical, electrical, software, human factors, logistics. No single agent can embody expertise across all disciplines; multi-agent architectures enable discipline specialization with cross-discipline coordination.

**Collaborative practice.** Systems engineering is inherently collaborative, involving teams of engineers, stakeholders, and organizations. Multi-agent systems mirror this collaborative structure, with agents representing different perspectives, roles, or organizational entities.

**Artifact complexity.** Systems engineering produces complex, interrelated artifacts—requirements, architectures, designs, test cases—with consistency and traceability requirements across thousands of elements. Agent swarms can achieve comprehensive coverage that individual analysis cannot.

**Lifecycle span.** Systems engineering spans extended lifecycles from concept through disposal. Persistent agent systems can maintain continuity, accumulating knowledge and adapting to evolving system states.

**Quality through diversity.** Engineering quality benefits from multiple perspectives examining artifacts. Agent swarms provide perspective diversity—different specializations, different analysis approaches—that surface issues single-point analysis misses.

This intersection defines the scope of this survey: multi-agent AI systems, drawing on classical MAS foundations, swarm intelligence principles, and modern LLM-based agentic AI capabilities, applied to support systems engineering processes.

---

**Word count:** ~1,050 words
**Subsections:** 5
**References cited:** [1]-[28]

---

## Revision Notes

- [ ] Expand LLM-based agents section with more recent frameworks
- [ ] Add specific examples for each swarm intelligence paradigm
- [ ] Consider adding timeline figure

