# Claude Flow User Manual

**Version:** 3.1.0-alpha.3
**Platform:** Windows 11 (bash/Unix syntax in Claude Code shell)
**Audience:** Researchers who have completed the Getting Started Guide
**Estimated reading time:** 45--60 minutes
**Last updated:** 2026-03-03

---

**Prerequisites.** This manual assumes you have completed the Getting Started Guide
and can run `claude-flow --version` successfully. If not, start there first. The
Quick-Start Cheat Sheet provides a condensed command reference for daily use.

---

## Table of Contents

1. [Architecture Overview](#1-architecture-overview)
2. [Swarms -- Multi-Agent Coordination](#2-swarms----multi-agent-coordination)
3. [Agents -- The Workers](#3-agents----the-workers)
4. [Memory -- Persistent Knowledge](#4-memory----persistent-knowledge)
5. [Hooks -- Intelligent Automation](#5-hooks----intelligent-automation)
6. [Tasks and Sessions](#6-tasks-and-sessions)
7. [Hive-Mind -- Distributed Consensus](#7-hive-mind----distributed-consensus)
8. [Governance and Configuration](#8-governance-and-configuration)
9. [Research Team Workflows](#9-research-team-workflows)
10. [Troubleshooting and FAQ](#10-troubleshooting-and-faq)
- [Appendix A: Full Command Reference](#appendix-a-full-command-reference)
- [Appendix B: Agent Type Catalog](#appendix-b-agent-type-catalog)

---

## 1. Architecture Overview

### 1.1 How Claude Flow Relates to Claude Code

Claude Code is Anthropic's CLI for interacting with Claude. It provides a single
conversational agent that can read files, run commands, and edit code. Claude Flow
extends Claude Code by adding **multi-agent orchestration** -- the ability to spawn,
coordinate, and manage multiple Claude Code agents working in parallel on different
parts of a problem.

Think of it this way:

- **Claude Code** = one researcher at a desk.
- **Claude Flow** = a research team with a coordinator assigning tasks to specialists.

Claude Flow is installed globally via npm and invoked with the `claude-flow` command.
It runs alongside Claude Code, not instead of it. Your normal Claude Code workflow
remains unchanged; Claude Flow adds capabilities on top.

```
+------------------------------------------------------------------+
|  Your Terminal / Claude Code Session                             |
|                                                                  |
|  claude-flow  ------>  Agent Orchestrator                        |
|                           |                                      |
|            +--------------+--------------+                       |
|            |              |              |                        |
|         Agent 1       Agent 2       Agent 3                      |
|       (researcher)    (coder)     (reviewer)                     |
|            |              |              |                        |
|            +---------- Memory ----------+                        |
|                    (shared state)                                 |
+------------------------------------------------------------------+
```

### 1.2 The Agent Orchestration Model

Claude Flow follows a **coordinator-to-specialists** pattern. When you initialize a
swarm, a coordinator agent is created first. The coordinator:

1. Receives the overall task or objective.
2. Decomposes it into subtasks.
3. Spawns specialist agents (coder, reviewer, tester, researcher, etc.).
4. Assigns subtasks to the appropriate specialists.
5. Monitors progress and handles failures.
6. Merges results and delivers the final output.

This pattern scales from 2 agents (coordinator + 1 worker) to 15+ agents for complex
multi-chapter reports or large codebase operations.

### 1.3 Key Abstractions

| Abstraction | What It Is | Analogy |
|-------------|-----------|---------|
| **Agent** | A single Claude Code instance with a role | A team member |
| **Swarm** | A group of agents with a topology and strategy | The team |
| **Memory** | Shared persistent key-value + vector store | The team's shared notebook |
| **Hook** | An event-driven callback (pre/post actions) | A quality gate or trigger |
| **Skill** | A reusable, documented capability (stored in `.claude/skills/`) | A standard operating procedure |
| **Session** | A stateful conversation with persistence | A work session |
| **Task** | A tracked unit of work with status | A ticket |

These abstractions compose together. A swarm contains agents. Agents read and write
memory. Hooks fire at lifecycle boundaries. Skills encode reusable patterns that
agents can follow.

### 1.4 The Command Surface

Claude Flow organizes its CLI into four tiers:

| Tier | Commands | Purpose |
|------|----------|---------|
| **Primary** | `init`, `start`, `status`, `agent`, `swarm`, `memory`, `task`, `session`, `mcp`, `hooks` | Daily operations |
| **Advanced** | `neural`, `security`, `performance`, `embeddings`, `hive-mind`, `ruvector`, `guidance` | Specialized capabilities |
| **Utility** | `config`, `doctor`, `daemon`, `completions`, `migrate`, `workflow` | Setup and maintenance |
| **Analysis** | `analyze`, `route`, `progress` | Introspection and routing |

You will spend most of your time with the Primary commands. The Advanced commands
become relevant for large-scale projects or when optimizing agent performance.

---

## 2. Swarms -- Multi-Agent Coordination

### 2.1 What Is a Swarm?

A swarm is a group of coordinated agents working together on a shared objective. Unlike
spawning individual agents manually, a swarm provides:

- **Topology** -- a communication structure that determines how agents interact.
- **Strategy** -- a work-distribution policy that determines how tasks are assigned.
- **Lifecycle management** -- automatic scaling, health monitoring, and shutdown.
- **Shared memory** -- a common knowledge base all agents can read and write.

You should use a swarm whenever a task benefits from parallel work, diverse expertise,
or when the output is too large for a single agent to produce in one session.

### 2.2 Topologies

The topology defines the communication graph between agents. Choose based on your
task structure.

#### Hierarchical

```
         [Coordinator]
        /      |      \
   [Worker]  [Worker]  [Worker]
```

The coordinator delegates tasks downward. Workers report results upward. No
worker-to-worker communication. This is the **default and most commonly used**
topology.

**Best for:** Structured tasks with clear subtask decomposition -- writing a report
with independent chapters, running parallel literature searches, executing a test
suite.

```bash
claude-flow swarm init --topology hierarchical --max-agents 8 --strategy specialized
```

#### Mesh

```
   [Agent] ---- [Agent]
      |    \  /    |
      |     \/     |
      |     /\     |
      |    /  \    |
   [Agent] ---- [Agent]
```

All agents can communicate with all other agents. Fully connected graph.

**Best for:** Brainstorming, peer review, consensus-building where every perspective
needs to see every other perspective.

```bash
claude-flow swarm init --topology mesh --max-agents 6 --strategy balanced
```

**Caution:** Communication overhead grows quadratically with agent count. Keep mesh
swarms small (4--6 agents).

#### Star

```
              [Hub]
            / | | | \
   [Spoke] [Spoke] [Spoke] [Spoke] [Spoke]
```

A central hub distributes independent tasks to spokes. Spokes do not communicate
with each other. Results flow back to the hub.

**Best for:** Embarrassingly parallel tasks -- searching multiple databases
simultaneously, processing independent files, running the same analysis on
different datasets.

```bash
claude-flow swarm init --topology star --max-agents 10 --strategy balanced
```

#### Ring

```
   [Agent 1] --> [Agent 2] --> [Agent 3] --> [Agent 4]
       ^                                        |
       |                                        |
       +----------------------------------------+
```

Each agent receives input from its predecessor and passes output to its successor.
A sequential pipeline.

**Best for:** Multi-stage processing pipelines -- draft then review then edit then
format. Each stage adds value to the previous stage's output.

```bash
claude-flow swarm init --topology ring --max-agents 4 --strategy specialized
```

#### Hierarchical-Mesh (Hybrid)

```
         [Coordinator]
        /             \
   [Sub-team A]    [Sub-team B]
   (mesh of 3)     (mesh of 3)
```

A coordinator manages sub-teams, where within each sub-team agents communicate
freely (mesh). Combines hierarchical delegation with peer collaboration.

**Best for:** Large complex projects where sub-teams need internal collaboration
but the overall effort needs top-down coordination.

```bash
claude-flow swarm init --topology hierarchical-mesh --max-agents 15 --strategy specialized
```

### 2.3 Strategies

The strategy determines how work is distributed across agents within the swarm.

| Strategy | Behavior | When to Use |
|----------|----------|-------------|
| `specialized` | Agents are assigned tasks matching their declared expertise (coder gets code tasks, reviewer gets review tasks). | Most of the time. This is the default. |
| `balanced` | Tasks are distributed evenly regardless of agent type, aiming for equal load. | When all agents have similar capabilities or when you want even utilization. |
| `byzantine` | Byzantine fault-tolerant consensus. Multiple agents independently produce results; majority vote determines the answer. | High-stakes decisions where correctness matters more than speed. |
| `raft` | Leader-election consensus (Raft protocol). One agent leads, others replicate. | Stateful operations requiring strong consistency. |
| `gossip` | Agents propagate information peer-to-peer, eventually converging. | Large swarms where eventual consistency is acceptable. |
| `crdt` | Conflict-free replicated data types. Agents work independently; conflicts resolve automatically via mathematical properties. | Concurrent writes to shared state. |
| `quorum` | Requires a quorum (majority) of agents to agree before proceeding. | When you need consensus without full Byzantine tolerance. |

For most research workflows, `specialized` is the right choice. Use `balanced` for
homogeneous tasks. The consensus strategies (`byzantine`, `raft`, `quorum`) are
relevant when using the Hive-Mind system (Section 7).

### 2.4 Swarm Lifecycle

A swarm follows this lifecycle:

```
  init  -->  start  -->  [monitor]  -->  [scale]  -->  stop
   |           |             |              |            |
   |           |             |              |            |
 Define    Launch       Check status    Add/remove    Shut down
 topology   agents      and health      agents        cleanly
```

**Initialize.** Define the swarm's topology, maximum agent count, and strategy.
This creates the configuration but does not launch any agents.

```bash
claude-flow swarm init --topology hierarchical --max-agents 8 --strategy specialized
```

**Start.** Launch the swarm. The coordinator agent is created first, then workers
are spawned as needed.

```bash
claude-flow swarm start
```

**Monitor.** Check on running agents, their status, and task progress.

```bash
claude-flow swarm status
```

**Scale.** Add or remove agents dynamically as workload changes.

```bash
claude-flow swarm scale --add 2
claude-flow swarm scale --remove 1
```

**Coordinate.** Send directives to the swarm coordinator.

```bash
claude-flow swarm coordinate --directive "Prioritize Section 3"
```

**Stop.** Gracefully shut down all agents and persist state.

```bash
claude-flow swarm stop
```

### 2.5 Examples

#### Example: Research Literature Review Swarm

Goal: Search 5 databases for papers on "agentic AI in systems engineering," filter
by relevance, and produce an annotated bibliography.

```bash
# Initialize a star topology (parallel independent searches)
claude-flow swarm init --topology star --max-agents 7 --strategy specialized

# Start the swarm
claude-flow swarm start

# The coordinator (hub) spawns 5 researcher agents, each assigned a database.
# A 6th agent aggregates and deduplicates results.
# Results are stored in shared memory under the "literature" namespace.

# Monitor progress
claude-flow swarm status

# When complete
claude-flow swarm stop
```

#### Example: Code Review Swarm

Goal: Review a 2,000-line pull request for correctness, security, and style.

```bash
# Mesh topology so reviewers can see each other's comments
claude-flow swarm init --topology mesh --max-agents 4 --strategy specialized

# Spawn specialized reviewers
claude-flow agent spawn --type reviewer --name "correctness-reviewer"
claude-flow agent spawn --type security-architect --name "security-reviewer"
claude-flow agent spawn --type performance-engineer --name "perf-reviewer"

claude-flow swarm start
claude-flow swarm status
claude-flow swarm stop
```

#### Example: Report Writing Swarm (Real-World Case)

The WRT-2516 technical report (167 pages, 13 chapters, 3 appendices) was produced
using Claude Flow with 4 sequential waves of agents, approximately 16 agents total:

| Wave | Agents | Chapters | Duration |
|------|--------|----------|----------|
| 1 | 5 | Ch 2--7, App A--B | ~45 min |
| 2 | 3 | Ch 8--9 | ~30 min |
| 3 | 3 | Ch 10--12 | ~30 min |
| 4 | 3 | Ch 1, Ch 13, App C | ~20 min |
| Figures + Refs | 2 | TikZ diagrams, bibliography | ~15 min |

Each wave used a hierarchical topology with specialized strategy. Agents within a
wave worked in parallel on independent chapters. Waves were sequenced because later
chapters depended on earlier ones.

```bash
# Wave 1: Foundation chapters (independent, parallelizable)
claude-flow swarm init --topology hierarchical --max-agents 6 --strategy specialized
claude-flow swarm start
# ... agents write Ch 2-7, Appendices A-B ...
claude-flow swarm stop

# Wave 2: Methodology chapters (depend on Wave 1 outputs)
claude-flow swarm init --topology hierarchical --max-agents 4 --strategy specialized
claude-flow swarm start
# ... agents write Ch 8-9, reading Wave 1 outputs from memory ...
claude-flow swarm stop

# Repeat for Waves 3 and 4
```

**Key lesson:** Not everything should be parallelized. When chapters have
dependencies, use sequential waves. Within each wave, parallelize independent work.

---

## 3. Agents -- The Workers

### 3.1 Agent Types

Claude Flow provides over 60 agent types organized into categories. Each type carries
default behaviors, prompts, and capabilities appropriate to its role.

#### Core Development

| Type | Role |
|------|------|
| `coder` | Writes and modifies source code |
| `reviewer` | Reviews code for correctness, style, and best practices |
| `tester` | Writes and runs tests |
| `planner` | Decomposes tasks and creates implementation plans |
| `researcher` | Investigates topics, reads documentation, gathers information |

#### V3 Specialized

| Type | Role |
|------|------|
| `security-architect` | Designs security architecture and threat models |
| `security-auditor` | Audits code and configuration for vulnerabilities |
| `memory-specialist` | Manages shared memory, namespaces, and data flow |
| `performance-engineer` | Profiles, benchmarks, and optimizes performance |

#### Swarm Coordination

| Type | Role |
|------|------|
| `hierarchical-coordinator` | Manages a hierarchical swarm |
| `mesh-coordinator` | Manages a mesh swarm |
| `adaptive-coordinator` | Dynamically adjusts coordination strategy |
| `collective-intelligence-coordinator` | Merges insights from multiple agents |
| `swarm-memory-manager` | Handles memory synchronization across agents |

See [Appendix B](#appendix-b-agent-type-catalog) for the complete catalog of all 60+
agent types.

### 3.2 Spawning Agents

Agents can be spawned individually or as part of a swarm.

**Spawn a single agent:**

```bash
claude-flow agent spawn --type researcher --name "lit-reviewer"
```

**Spawn with a specific task:**

```bash
claude-flow agent spawn --type coder --name "api-builder" \
  --task "Implement the REST API endpoints defined in api-spec.yaml"
```

**Spawn multiple agents:**

```bash
claude-flow agent spawn --type researcher --name "db-searcher-1"
claude-flow agent spawn --type researcher --name "db-searcher-2"
claude-flow agent spawn --type reviewer --name "quality-check"
```

### 3.3 Agent Lifecycle

An agent follows this lifecycle:

```
  spawn  -->  active  -->  [metrics]  -->  stop
    |           |              |             |
    |           |              |             |
  Created    Working       Check         Graceful
  with role  on tasks      performance   shutdown
```

**Spawn.** The agent is created with a type, name, and optionally a task.

**Active.** The agent processes tasks, reads/writes memory, and communicates with
other agents according to the swarm topology.

**Metrics.** At any time, you can check an agent's performance.

```bash
claude-flow agent metrics --name "lit-reviewer"
```

**Health.** Check whether an agent is responsive.

```bash
claude-flow agent health --name "lit-reviewer"
```

**Logs.** View an agent's output history.

```bash
claude-flow agent logs --name "lit-reviewer"
```

**List.** See all running agents.

```bash
claude-flow agent list
```

**Stop.** Gracefully shut down an agent.

```bash
claude-flow agent stop --name "lit-reviewer"
```

### 3.4 Agent Routing

When a task arrives, Claude Flow must decide which agent type should handle it. This
is done by the **routing system**, which considers:

1. **Task description** -- keywords and intent.
2. **Agent capabilities** -- what each type is designed to do.
3. **Current load** -- which agents are idle vs. busy.
4. **Historical performance** -- which agent types have succeeded at similar tasks.

The default routing table maps task categories to agent compositions:

| Task Type | Agent Team |
|-----------|-----------|
| Bug Fix | coordinator, researcher, coder, tester |
| Feature | coordinator, architect, coder, tester, reviewer |
| Refactor | coordinator, architect, coder, reviewer |
| Performance | coordinator, performance-engineer, coder |
| Security | coordinator, security-architect, auditor |
| Documentation | researcher, api-docs |

You can invoke routing explicitly:

```bash
# Ask the router which agents to use for a task
claude-flow hooks route --task "Add SHACL validation to the ontology pipeline"

# Get an explanation of why a routing decision was made
claude-flow hooks explain --topic "Why was security-architect selected?"
```

### 3.5 The 3-Tier Model

Claude Flow uses a 3-tier model routing system to optimize cost and latency. Not
every task needs the most powerful (and expensive) model.

| Tier | Handler | Latency | Cost | Use Cases |
|------|---------|---------|------|-----------|
| **1** | Agent Booster | <1ms | $0 | Simple transforms: rename variables, add type annotations, remove console.log statements |
| **2** | Haiku | ~500ms | ~$0.0002 | Simple tasks, straightforward bug fixes, low-complexity edits |
| **3** | Sonnet / Opus | 2--5s | $0.003--$0.015 | Architecture decisions, security analysis, complex multi-step reasoning |

The model router selects the tier automatically based on task complexity. You can
also influence routing:

```bash
# View model routing decisions
claude-flow hooks model-route --task "Fix the typo in line 42"
# Result: Tier 1 (Agent Booster)

claude-flow hooks model-route --task "Design a zero-trust authentication architecture"
# Result: Tier 3 (Opus)
```

**Cost implication:** For a research team running 50+ agent-hours per month, proper
tier routing can reduce costs by 60--80% compared to routing everything through
Tier 3.

---

## 4. Memory -- Persistent Knowledge

### 4.1 Why Memory Matters

Without memory, each agent starts with a blank slate. Memory provides:

- **Persistence** -- knowledge survives across sessions and agent restarts.
- **Sharing** -- agents in a swarm can read each other's findings.
- **Search** -- semantic (vector) search lets agents find relevant prior work.
- **Coordination** -- agents use memory to signal status, claim tasks, and avoid
  duplicating effort.

Memory is the shared notebook that turns independent agents into a coordinated team.

### 4.2 Core Operations

#### Store

Write a key-value pair to memory, optionally in a namespace.

```bash
claude-flow memory store --key "finding-001" \
  --value "NIST SP 800-207 defines zero trust as..." \
  --namespace "literature"
```

#### Retrieve

Fetch a specific key.

```bash
claude-flow memory retrieve --key "finding-001" --namespace "literature"
```

#### Search

Find entries by semantic similarity (vector search) or keyword.

```bash
claude-flow memory search --query "zero trust architecture" --namespace "literature"
```

#### List

List all keys in a namespace.

```bash
claude-flow memory list --namespace "literature"
```

#### Delete

Remove an entry.

```bash
claude-flow memory delete --key "finding-001" --namespace "literature"
```

### 4.3 Namespaces

Namespaces partition memory into logical compartments. Use them to keep different
types of knowledge separate and searchable.

Common namespace conventions:

| Namespace | Purpose |
|-----------|---------|
| `coordination` | Agent status, task assignments, progress tracking |
| `patterns` | Learned code patterns, reusable solutions |
| `literature` | References, citations, findings from literature review |
| `decisions` | Architecture decisions, rationale, ADRs |
| `metrics` | Performance data, cost tracking, quality scores |

```bash
# Store in a namespace
claude-flow memory store --key "decision-001" \
  --value "Use OWL 2 DL for the trust ontology because..." \
  --namespace "decisions"

# Search within a namespace
claude-flow memory search --query "ontology format" --namespace "decisions"

# List all entries in a namespace
claude-flow memory list --namespace "decisions"
```

### 4.4 Vector Search

Claude Flow's memory system supports vector embeddings, enabling semantic similarity
search. This means you can search by meaning, not just by exact keyword match.

```bash
# Initialize the embedding system
claude-flow embeddings init

# Store with embeddings (automatic if embeddings are enabled)
claude-flow memory store --key "paper-42" \
  --value "This paper proposes a bio-inspired circuit breaker for AI trust..."

# Semantic search finds this even with different wording
claude-flow memory search --query "biological mechanisms for controlling AI behavior"
```

The embeddings system uses HNSW (Hierarchical Navigable Small World) indexing,
providing 150x to 12,500x faster search compared to brute-force comparison.

### 4.5 Memory Lifecycle

Memory accumulates over time. These commands help manage it.

**Initialize.** Set up the memory backend.

```bash
claude-flow memory init --force --verbose
```

**Configure.** Adjust memory settings.

```bash
claude-flow memory configure
```

**Statistics.** View memory usage.

```bash
claude-flow memory stats
```

**Cleanup.** Remove stale or orphaned entries.

```bash
claude-flow memory cleanup
```

**Compress.** Reduce storage by compressing old entries.

```bash
claude-flow memory compress
```

**Export.** Save memory to a portable format.

```bash
claude-flow memory export --output memory-backup.json
```

**Import.** Load memory from a backup or another project.

```bash
claude-flow memory import --input memory-backup.json
```

### 4.6 Cross-Session Persistence

Memory persists across Claude Code sessions by default. When you close a session
and start a new one, your stored knowledge is still available. This is critical for
multi-day research projects.

The persistence path is controlled by the environment variable:

```bash
CLAUDE_FLOW_MEMORY_PATH=./data/memory
```

To share memory between projects, export from one and import to another:

```bash
# In project A
claude-flow memory export --output /tmp/shared-findings.json

# In project B
claude-flow memory import --input /tmp/shared-findings.json
```

### 4.7 Example: Building a Research Knowledge Base

Scenario: You are conducting a scoping review on neuro-symbolic AI for wargaming.

```bash
# Step 1: Initialize memory with a dedicated namespace
claude-flow memory init

# Step 2: Store reference metadata as you find papers
claude-flow memory store --key "ref-001" \
  --value '{"authors":"Smith et al.","year":2024,"title":"Hybrid Neural-Symbolic Reasoning","relevance":"high","notes":"Proposes a neural-symbolic architecture for tactical decision support"}' \
  --namespace "scoping-review"

claude-flow memory store --key "ref-002" \
  --value '{"authors":"Chen and Wang","year":2023,"title":"Knowledge Graphs for Military Planning","relevance":"medium","notes":"Uses OWL ontologies but no neural component"}' \
  --namespace "scoping-review"

# Step 3: Search semantically
claude-flow memory search --query "ontology-based military decision making" \
  --namespace "scoping-review"

# Step 4: Export for archival
claude-flow memory export --output scoping-review-memory.json
```

Over time, this builds a searchable knowledge base that any agent in any future
session can query. This is especially valuable for longitudinal research projects
spanning weeks or months.

---

## 5. Hooks -- Intelligent Automation

### 5.1 What Are Hooks?

Hooks are event-driven callbacks that fire at specific points in the Claude Flow
lifecycle. They enable:

- **Quality gates** -- validate code before it is committed.
- **Automated learning** -- record what worked and what did not.
- **Intelligent routing** -- direct tasks to the best-suited agent.
- **Background workers** -- run maintenance tasks without blocking your workflow.

Hooks are Claude Flow's mechanism for encoding institutional knowledge and enforcing
standards automatically.

### 5.2 Lifecycle Hooks

These fire at boundaries of edits, commands, tasks, and sessions.

| Hook | When It Fires | Purpose |
|------|---------------|---------|
| `pre-edit` | Before a file is modified | Gather context, check permissions, validate preconditions |
| `post-edit` | After a file is modified | Record the change, train patterns, verify quality |
| `pre-command` | Before a shell command runs | Assess risk, validate safety, check authorization |
| `post-command` | After a shell command runs | Record outcome, track metrics, detect failures |
| `pre-task` | Before a task begins | Log start time, suggest agents, coordinate swarm |
| `post-task` | After a task completes | Record results, update metrics, store learnings |
| `session-end` | When a session closes | Persist state, generate summary, export metrics |
| `session-restore` | When a session resumes | Reload state, restore context, re-establish agents |

**Example: pre-edit hook invocation**

```bash
claude-flow hooks pre-edit --file "src/parser.py" --operation "modify"
```

**Example: post-task hook with learning**

```bash
claude-flow hooks post-task --task-id "task-42" --success true --store-results
```

### 5.3 Routing Hooks

These determine where tasks and code changes should be directed.

| Hook | Purpose | Key Options |
|------|---------|-------------|
| `route` | Route a task to the optimal agent type | `--task`, `--context`, `--top-k` |
| `explain` | Explain why a routing decision was made | `--topic`, `--detailed` |
| `coverage-route` | Route based on test coverage gaps | `--task`, `--path` |
| `coverage-suggest` | Suggest test coverage improvements | `--path` |
| `coverage-gaps` | List coverage gaps with priorities | `--format`, `--limit` |
| `model-route` | Select the optimal model tier for a task | `--task` |
| `model-outcome` | Record model routing outcomes for learning | (automatic) |

**Example: Routing a task**

```bash
claude-flow hooks route --task "Refactor the memory module for thread safety" --top-k 3
```

This returns the top 3 agent types most suited to the task, ranked by predicted
effectiveness.

### 5.4 Learning Hooks

These enable Claude Flow to improve over time by learning from past work.

| Hook | Purpose | Key Options |
|------|---------|-------------|
| `pretrain` | Bootstrap intelligence by analyzing the existing repository | `--model-type`, `--epochs` |
| `build-agents` | Generate optimized agent configurations based on project patterns | `--agent-types`, `--focus` |
| `metrics` | View the learning metrics dashboard | `--v3-dashboard`, `--format` |
| `transfer` | Transfer learned patterns to/from a registry | `store`, `from-project` |
| `intelligence` | Access the RuVector intelligence system | `trajectory-*`, `pattern-*`, `stats` |

**Example: Pretraining on your repository**

```bash
# Analyze the repo to learn code patterns, naming conventions, and architecture
claude-flow hooks pretrain --model-type neural --epochs 3
```

After pretraining, the routing system and agent configurations are tuned to your
project's specific patterns.

**Example: Viewing metrics**

```bash
claude-flow hooks metrics --v3-dashboard --format table
```

### 5.5 Background Workers

Claude Flow can run 12 background workers that perform maintenance and analysis
tasks without blocking your primary workflow. Workers run via the daemon and can be
dispatched on demand.

| Worker | Priority | Description |
|--------|----------|-------------|
| `ultralearn` | normal | Deep knowledge acquisition from codebase and documentation |
| `optimize` | high | Identifies and suggests performance optimizations |
| `consolidate` | low | Consolidates memory, merges duplicates, compresses old entries |
| `predict` | normal | Predictive preloading of likely-needed resources |
| `audit` | critical | Security analysis -- scans for vulnerabilities, secrets, misconfigurations |
| `map` | normal | Codebase mapping -- builds structural understanding of the project |
| `preload` | low | Preloads resources expected to be needed soon |
| `deepdive` | normal | Deep code analysis -- complex pattern detection and anti-patterns |
| `document` | normal | Auto-generates documentation for undocumented code |
| `refactor` | normal | Identifies and suggests refactoring opportunities |
| `benchmark` | normal | Performance benchmarking against baselines |
| `testgaps` | normal | Identifies gaps in test coverage and suggests tests |

**Managing workers:**

```bash
# List available workers and their status
claude-flow hooks worker list

# Dispatch a specific worker
claude-flow hooks worker dispatch --type audit

# Check worker status
claude-flow hooks worker status --type audit

# Detect which workers should run based on recent changes
claude-flow hooks worker detect
```

### 5.6 Example: Setting Up a Pre-Edit Quality Gate

Scenario: You want to ensure that no file in the `ontologies/` directory is modified
without passing SHACL validation.

```bash
# Register a pre-edit hook that runs SHACL validation
claude-flow hooks pre-edit --file "ontologies/*.ttl" --operation "modify"
```

In practice, quality gates are often implemented through the CLAUDE.md governance
rules (see Section 8) and skills that encode the validation logic. The hook
mechanism ensures these gates fire automatically rather than relying on manual
invocation.

---

## 6. Tasks and Sessions

### 6.1 Task Management

Tasks are tracked units of work with status, assignment, and lifecycle management.

**Create a task:**

```bash
claude-flow task create --title "Write Chapter 5" \
  --description "Draft the assessment methodology chapter, ~20 pages" \
  --assignee "coder-1"
```

**List tasks:**

```bash
claude-flow task list
```

**Update task status:**

```bash
claude-flow task update --id "task-5" --status "in-progress"
claude-flow task update --id "task-5" --status "complete"
```

**Assign a task:**

```bash
claude-flow task assign --id "task-5" --agent "researcher-2"
```

Tasks integrate with the swarm system. When a swarm is running, the coordinator
creates and assigns tasks automatically. You can also create tasks manually for
tracking purposes.

### 6.2 Session Management

Sessions provide continuity across work periods. A session captures:

- Active agents and their state.
- Memory contents.
- Task progress.
- Hook configurations.

**Start a session:**

```bash
claude-flow session start --id "lit-review-2026-03"
```

**Check session status:**

```bash
claude-flow session status
```

**End a session (persists state):**

```bash
claude-flow session end --generate-summary --export-metrics
```

**Restore a previous session:**

```bash
# Restore a specific session
claude-flow session restore --session-id "lit-review-2026-03"

# Restore the most recent session
claude-flow session restore --latest
```

Session restore is particularly valuable for multi-day research efforts. You can
close your laptop on Friday, and on Monday `session restore --latest` brings you
back to exactly where you left off -- with all agents, memory, and task state intact.

---

## 7. Hive-Mind -- Distributed Consensus

### 7.1 When to Use Hive-Mind

The Hive-Mind system is for situations where multiple agents must reach agreement
on a decision, and you need guarantees about the quality of that agreement. Use it
when:

- A decision has significant consequences (architecture choices, security policies).
- You want multiple independent opinions and a structured way to merge them.
- You need fault tolerance -- the system should produce a correct result even if
  some agents fail or produce bad output.

For most day-to-day work, the standard swarm topologies (Section 2.2) are sufficient.
Hive-Mind adds overhead and is best reserved for high-stakes decisions.

### 7.2 Queen-Led Consensus

The Hive-Mind follows a queen-led model:

1. The **queen** (coordinator) poses a question or decision to the swarm.
2. Each agent independently produces its assessment.
3. The queen collects all assessments.
4. A consensus protocol determines the final answer.
5. The queen announces the result.

```bash
# Initialize hive-mind
claude-flow hive-mind init --topology hierarchical

# Start consensus process
claude-flow hive-mind start

# Check consensus status
claude-flow hive-mind status

# Stop hive-mind
claude-flow hive-mind stop
```

### 7.3 Byzantine Fault Tolerance

Byzantine fault tolerance (BFT) handles the case where some agents produce incorrect
or adversarial outputs. The system can tolerate up to f faulty agents out of 3f + 1
total agents.

| Total Agents | Faulty Agents Tolerated | Required Agreement |
|-------------|------------------------|-------------------|
| 4 | 1 | 3 of 4 |
| 7 | 2 | 5 of 7 |
| 10 | 3 | 7 of 10 |

```bash
claude-flow swarm init --topology hierarchical --max-agents 7 --strategy byzantine
```

In a research context, "faulty" does not mean malicious -- it means an agent that
produces a low-quality or irrelevant response due to hallucination, context loss,
or misunderstanding the task. BFT ensures one bad agent response does not corrupt
the final output.

### 7.4 Example: Multi-Agent Decision Making

Scenario: Decide whether to use OWL 2 DL or OWL 2 Full for a new ontology, given
trade-offs in expressivity, decidability, and tool support.

```bash
# Initialize with byzantine consensus (tolerates 1 bad answer out of 4)
claude-flow swarm init --topology mesh --max-agents 4 --strategy byzantine

# Spawn domain-specific agents
claude-flow agent spawn --type researcher --name "ontology-expert" \
  --task "Evaluate OWL 2 DL vs OWL 2 Full for expressivity"
claude-flow agent spawn --type researcher --name "tooling-expert" \
  --task "Evaluate OWL 2 DL vs OWL 2 Full for reasoner support"
claude-flow agent spawn --type security-architect --name "safety-expert" \
  --task "Evaluate OWL 2 DL vs OWL 2 Full for decidability guarantees"
claude-flow agent spawn --type planner --name "pragmatist" \
  --task "Evaluate OWL 2 DL vs OWL 2 Full for development velocity"

# Start consensus
claude-flow hive-mind start

# Each agent independently researches and votes
# Byzantine consensus ensures the answer is robust even if one agent hallucinates

claude-flow hive-mind status
claude-flow hive-mind stop
```

---

## 8. Governance and Configuration

### 8.1 CLAUDE.md -- Project Instructions

Every project has a `CLAUDE.md` file at its root that contains behavioral
instructions for Claude Code and Claude Flow. This file is automatically loaded at
session start and governs all agent behavior.

A typical CLAUDE.md includes:

- **Rules** with unique IDs and risk annotations.
- **File organization** conventions.
- **Build and test** commands.
- **Architecture** context.

Example structure:

```markdown
# Project Instructions

## Rules
- [R001] Do what has been asked; nothing more, nothing less. @quality [all] risk:high
- [R002] NEVER create files unless absolutely necessary. @quality [edit] risk:medium
- [R005] NEVER commit .env or API keys. @security [bash,edit] risk:critical

## File Organization
- /src - Source code
- /tests - Test files
- /Papers - Research manuscripts

## Build & Test
- Run tests: python -m pytest tests/
```

### 8.2 V3 Rule Annotations

V3 governance uses a structured annotation format for rules:

```
[RULE-ID] Description. @category [scope] risk:level
```

| Component | Purpose | Examples |
|-----------|---------|---------|
| `[RULE-ID]` | Unique identifier | `[R001]`, `[G003]`, `[S002]` |
| `@category` | Classification tag | `@quality`, `@security`, `@research` |
| `[scope]` | Which tool types it applies to | `[all]`, `[edit]`, `[bash]`, `[bash,edit]` |
| `risk:level` | Severity if violated | `risk:low`, `risk:medium`, `risk:high`, `risk:critical` |

This structure enables automated governance auditing. An agent (such as the Alpha
Empress COO governance agent) can parse these annotations to verify compliance
across projects.

### 8.3 Configuration Management

Claude Flow stores configuration in `claude-flow.config.json` at the project root,
or in the location specified by the `CLAUDE_FLOW_CONFIG` environment variable.

```bash
# View current configuration
claude-flow config list

# Set a configuration value
claude-flow config set --key "memory.backend" --value "hybrid"

# Get a configuration value
claude-flow config get --key "memory.backend"
```

Key environment variables:

| Variable | Default | Purpose |
|----------|---------|---------|
| `CLAUDE_FLOW_CONFIG` | `./claude-flow.config.json` | Config file location |
| `CLAUDE_FLOW_LOG_LEVEL` | `info` | Logging verbosity |
| `ANTHROPIC_API_KEY` | (none) | API authentication |
| `CLAUDE_FLOW_MCP_PORT` | `3000` | MCP server port |
| `CLAUDE_FLOW_MCP_TRANSPORT` | `stdio` | MCP transport mode |
| `CLAUDE_FLOW_MEMORY_BACKEND` | `hybrid` | Memory storage backend |
| `CLAUDE_FLOW_MEMORY_PATH` | `./data/memory` | Memory storage directory |

---

## 9. Research Team Workflows

This section documents workflows specific to the University of Arizona research
environment. These patterns have been tested in production across multiple research
projects.

### 9.1 Paper Writing with Swarms

**When to use swarms for writing:** When a paper has 4+ independent sections,
multiple co-authors need drafts fast, or the paper requires synthesis from diverse
sources.

**When NOT to use swarms:** For short papers (<10 pages), single-author think
pieces, or when the argument must develop linearly from a single perspective.

**Recommended pattern: Wave-based hierarchical**

```bash
# Wave 1: Independent sections (parallelize)
claude-flow swarm init --topology hierarchical --max-agents 6 --strategy specialized

# Agent assignments via memory
claude-flow memory store --key "swarm/assignments" --namespace "coordination" \
  --value '{"agent-1":"Section 2: Related Work","agent-2":"Section 3: Methodology","agent-3":"Section 4: Results"}'

claude-flow swarm start
# ... wait for completion ...
claude-flow swarm stop

# Wave 2: Dependent sections (use Wave 1 outputs)
claude-flow swarm init --topology hierarchical --max-agents 3 --strategy specialized
claude-flow swarm start
# ... agents read Wave 1 outputs from memory to write Introduction and Discussion ...
claude-flow swarm stop
```

**Post-swarm integration.** After all waves complete, a single reviewer agent (or
the human author) integrates the sections, ensures consistent voice, and resolves
cross-references.

### 9.2 Literature Review Automation

Claude Flow agents can accelerate systematic and scoping reviews by parallelizing
the search and screening stages.

**Recommended pattern: Star topology with researcher agents**

```bash
# Spawn 5 researchers, one per database
claude-flow swarm init --topology star --max-agents 6 --strategy specialized

# Each spoke searches a different source
# Hub agent deduplicates and applies inclusion/exclusion criteria

# Store results in structured memory
claude-flow memory store --key "screening/paper-001" --namespace "lit-review" \
  --value '{"title":"...","source":"IEEE Xplore","include":true,"reason":"Meets criteria C1, C3"}'
```

**Important limitations.** Claude Flow agents cannot directly access paywalled
databases (IEEE Xplore, ACM DL, Scopus). The agents work with exported citation
files, PDFs you provide, or open-access sources. The value is in the screening,
synthesis, and annotation -- not the database querying itself.

### 9.3 Ontology Development and Validation

For ontology-heavy projects (OWL, SHACL, SPARQL), Claude Flow supports a
development-validation cycle.

**Pattern: Build then validate**

1. A `coder` agent writes or modifies `.ttl` files.
2. A pre-edit hook or quality gate runs syntax checking.
3. A `tester` agent runs SHACL validation (via pyshacl).
4. A `tester` agent runs SPARQL competency queries.
5. Results are stored in memory and reported.

```bash
# Store validation results
claude-flow memory store --key "validation/shacl-run-001" \
  --namespace "ontology" \
  --value '{"status":"pass","shapes":8,"violations":0,"timestamp":"2026-03-03T14:30:00"}'

# Search for past validation failures
claude-flow memory search --query "SHACL violation" --namespace "ontology"
```

This pattern was used extensively in the Portfolio Governance Ontology project
(119 individuals, 778 triples, 8 SHACL shapes, 20 SPARQL competency queries).

### 9.4 Cross-Project Coordination

The PostWach research portfolio spans 8+ hives (projects with V3 governance). Claude
Flow's memory system enables cross-project coordination.

**Pattern: Shared memory namespaces**

```bash
# Store a cross-project finding
claude-flow memory store --key "xproject/finding-001" \
  --namespace "coordination" \
  --value '{"from":"GI-JOE","to":"PostWach","type":"ontology-update","details":"Added 3 new classes to portfolio TBox"}'

# Search across projects
claude-flow memory search --query "ontology changes" --namespace "coordination"
```

**Memory export/import for handoff:**

```bash
# GI-JOE exports its ontology findings
claude-flow memory export --output ontology-findings.json --namespace "ontology"

# PostWach imports them for the meta-analysis
claude-flow memory import --input ontology-findings.json
```

### 9.5 Productivity Scorecards

The AI Swarm Productivity project tracks research session metrics using a
standardized scorecard format (see `Papers/AI_Swarm_Productivity/scorecard-template.yaml`).

A scorecard captures four dimensions:

| Dimension | What It Measures |
|-----------|-----------------|
| **D1: Output Volume** | Files created/modified, lines written, pages produced |
| **D2: AI Efficiency** | Agents spawned, topology, model, tokens, cost |
| **D3: Quality Gates** | Tests passed/failed, gates run, first-pass quality |
| **D4: Process Health** | Agent failures, retries, rework, blocked time |

**After each significant session, create a scorecard:**

1. Copy `scorecard-template.yaml` to `data/scorecards/<session-id>.yaml`.
2. Fill in the required fields from your session.
3. Leave the `derived` section blank (computed by the analysis script).

```bash
# Example: check your session metrics
claude-flow hooks metrics --v3-dashboard --format table
```

Scorecards enable longitudinal analysis of research productivity, comparing
swarm-assisted vs. manual work sessions, and identifying bottlenecks.

---

## 10. Troubleshooting and FAQ

### Common Errors

**"claude-flow: command not found"**

The CLI is not installed globally or not on your PATH.

```bash
# Check installation
npm list -g @claude-flow/cli

# Reinstall if needed
npm install -g @claude-flow/cli
```

**"No agents running"**

You initialized a swarm but did not start it, or all agents have been stopped.

```bash
# Check status
claude-flow swarm status
claude-flow agent list

# Start the swarm
claude-flow swarm start
```

**"Memory backend not initialized"**

Run memory init before using store/search/retrieve.

```bash
claude-flow memory init --force --verbose
```

**Agent appears stuck or unresponsive**

Check agent health and logs. If unresponsive, stop and respawn.

```bash
claude-flow agent health --name "stuck-agent"
claude-flow agent logs --name "stuck-agent"

# If truly stuck
claude-flow agent stop --name "stuck-agent"
claude-flow agent spawn --type coder --name "replacement-agent"
```

**Session restore fails**

The session file may be corrupted or the session ID may be incorrect.

```bash
# List available sessions
claude-flow session list

# Try restoring the latest
claude-flow session restore --latest
```

### System Diagnostics

When something is not working, run the doctor:

```bash
claude-flow doctor --fix
```

This checks:

- CLI version and installation integrity.
- Configuration file validity.
- Memory backend connectivity.
- Daemon status.
- MCP server status.

### Performance Tips

1. **Start the daemon.** Background workers and hooks perform better when the daemon
   is running.

   ```bash
   claude-flow daemon start
   ```

2. **Keep swarms small.** 4--8 agents is the sweet spot for most tasks. Beyond 10,
   coordination overhead can exceed the parallel speedup.

3. **Use the right topology.** Mesh with 15 agents is almost always wrong. Use
   hierarchical or hierarchical-mesh for large teams.

4. **Use namespaces.** Searching all of memory is slower than searching a specific
   namespace. Organize early.

5. **Clean up memory periodically.** Old entries slow down vector search.

   ```bash
   claude-flow memory cleanup
   claude-flow memory compress
   ```

6. **Stop idle agents.** Agents consume resources even when idle. Stop them when
   their work is complete.

   ```bash
   claude-flow agent stop --name "done-agent"
   ```

### When NOT to Use Swarms

Swarms add overhead. They are not appropriate for every task.

| Task | Use Swarm? | Why |
|------|-----------|-----|
| Fix a typo | No | Single edit, no parallelism needed |
| Rename a variable across files | No | Simple find-and-replace |
| Write a 2-page memo | No | One agent, one voice |
| Review a 50-line PR | No | One reviewer is sufficient |
| Write a 100-page report | **Yes** | Parallel chapters, diverse expertise |
| Screen 200 papers | **Yes** | Embarrassingly parallel |
| Security audit of 10 services | **Yes** | Parallel independent audits |
| Multi-perspective design review | **Yes** | Diverse opinions needed |

**Rule of thumb:** If the task can be decomposed into 3+ independent subtasks that
benefit from parallelism or diverse expertise, use a swarm. Otherwise, use a single
agent or plain Claude Code.

---

## Appendix A: Full Command Reference

### Primary Commands

| Command | Subcommands | Description |
|---------|-------------|-------------|
| `init` | `wizard`, `presets`, `skills`, `hooks` | Project initialization |
| `start` | -- | Start Claude Flow |
| `status` | `agents`, `memory`, `system` | System status monitoring |
| `agent` | `spawn`, `list`, `status`, `stop`, `metrics`, `pool`, `health`, `logs` | Agent lifecycle management |
| `swarm` | `init`, `start`, `status`, `stop`, `scale`, `coordinate` | Multi-agent swarm coordination |
| `memory` | `init`, `store`, `retrieve`, `search`, `list`, `delete`, `stats`, `configure`, `cleanup`, `compress`, `export`, `import` | Persistent knowledge management |
| `task` | `create`, `list`, `update`, `assign`, `status`, `delete` | Task tracking and assignment |
| `session` | `start`, `end`, `status`, `restore`, `list`, `export`, `import` | Session state management |
| `mcp` | `add`, `remove`, `list`, `start`, `stop`, `status`, `tools`, `execute`, `config` | MCP server management |
| `hooks` | (see below) | Intelligent automation and learning |

### Hooks Subcommands

| Subcommand | Description |
|------------|-------------|
| `pre-edit` | Context gathering before file edits |
| `post-edit` | Record editing outcomes for learning |
| `pre-command` | Risk assessment before shell commands |
| `post-command` | Record command execution outcomes |
| `pre-task` | Task start recording, agent suggestions |
| `post-task` | Task completion recording and learning |
| `session-end` | Session end with state persistence |
| `session-restore` | Restore a previous session |
| `route` | Route task to optimal agent |
| `explain` | Explain routing decisions |
| `pretrain` | Bootstrap intelligence from repository |
| `build-agents` | Generate optimized agent configurations |
| `metrics` | View learning metrics dashboard |
| `transfer` | Transfer patterns via registry |
| `list` | List all registered hooks |
| `intelligence` | RuVector intelligence system access |
| `worker` | Background worker management |
| `progress` | Track hook progress |
| `coverage-route` | Route based on test coverage gaps |
| `coverage-suggest` | Suggest coverage improvements |
| `coverage-gaps` | List coverage gaps with priorities |
| `token-optimize` | Optimize token usage |
| `model-route` | Select optimal model tier |
| `model-outcome` | Record model routing outcomes |

### Advanced Commands

| Command | Subcommands | Description |
|---------|-------------|-------------|
| `neural` | `train`, `predict`, `status`, `export`, `import` | Neural pattern training |
| `security` | `scan`, `audit`, `report`, `policy`, `secrets`, `compliance` | Security scanning and auditing |
| `performance` | `profile`, `benchmark`, `report`, `optimize`, `baseline` | Performance profiling |
| `embeddings` | `init`, `index`, `search`, `status` | Vector embedding management |
| `hive-mind` | `init`, `start`, `status`, `stop`, `vote`, `results` | Distributed consensus |
| `ruvector` | (intelligence system) | Self-optimizing neural architecture |
| `guidance` | (advisory system) | Guided decision support |

### Utility Commands

| Command | Subcommands | Description |
|---------|-------------|-------------|
| `config` | `list`, `get`, `set`, `reset`, `validate`, `export`, `import` | Configuration management |
| `doctor` | `--fix` | System diagnostics and repair |
| `daemon` | `start`, `stop`, `status`, `restart`, `logs` | Background worker daemon |
| `completions` | `bash`, `zsh`, `fish`, `powershell` | Shell completion scripts |
| `migrate` | `check`, `plan`, `run`, `rollback`, `status` | V2 to V3 migration |
| `workflow` | `run`, `list`, `create`, `status`, `stop`, `template` | Workflow execution |

### Analysis Commands

| Command | Description |
|---------|-------------|
| `analyze` | Analyze codebase or project structure |
| `route` | Route a task description to the optimal agent |
| `progress` | View overall progress across tasks and agents |

---

## Appendix B: Agent Type Catalog

### Core Development (5 types)

| Type | Description |
|------|-------------|
| `coder` | General-purpose code writer and editor. Handles implementation tasks across languages. |
| `reviewer` | Reviews code for correctness, maintainability, and adherence to project standards. |
| `tester` | Writes unit tests, integration tests, and runs test suites. Reports coverage. |
| `planner` | Decomposes complex tasks into ordered subtasks. Creates implementation plans. |
| `researcher` | Investigates topics, reads documentation, searches for information, and synthesizes findings. |

### V3 Specialized (4 types)

| Type | Description |
|------|-------------|
| `security-architect` | Designs security architectures, threat models, and trust boundaries. |
| `security-auditor` | Audits existing code and configuration for vulnerabilities and compliance gaps. |
| `memory-specialist` | Manages shared memory systems, namespace design, and data flow between agents. |
| `performance-engineer` | Profiles code, identifies bottlenecks, runs benchmarks, and suggests optimizations. |

### Swarm Coordination (5 types)

| Type | Description |
|------|-------------|
| `hierarchical-coordinator` | Manages hierarchical swarms. Delegates tasks downward, aggregates results upward. |
| `mesh-coordinator` | Manages mesh swarms. Facilitates peer-to-peer communication between all agents. |
| `adaptive-coordinator` | Dynamically adjusts coordination strategy based on runtime conditions. |
| `collective-intelligence-coordinator` | Merges diverse agent insights into a unified analysis or decision. |
| `swarm-memory-manager` | Handles memory synchronization, conflict resolution, and consistency across agents. |

### Consensus and Distributed (7 types)

| Type | Description |
|------|-------------|
| `byzantine-coordinator` | Manages Byzantine fault-tolerant consensus across agents. |
| `raft-manager` | Implements Raft consensus protocol for leader election and log replication. |
| `gossip-coordinator` | Manages gossip-based information propagation for eventual consistency. |
| `consensus-builder` | General-purpose consensus builder for multi-agent decision making. |
| `crdt-synchronizer` | Manages conflict-free replicated data types for concurrent state updates. |
| `quorum-manager` | Enforces quorum-based agreement before decisions are finalized. |
| `security-manager` | Manages security policies and access control across the agent swarm. |

### Performance and Optimization (5 types)

| Type | Description |
|------|-------------|
| `perf-analyzer` | Analyzes code and system performance, identifies hotspots. |
| `performance-benchmarker` | Runs standardized benchmarks and compares against baselines. |
| `task-orchestrator` | Orchestrates complex multi-step task sequences across agents. |
| `memory-coordinator` | Coordinates memory access patterns to minimize contention. |
| `smart-agent` | Self-optimizing agent that adapts its behavior based on task outcomes. |

### GitHub and Repository (9 types)

| Type | Description |
|------|-------------|
| `github-modes` | General GitHub workflow automation. |
| `pr-manager` | Creates, reviews, and manages pull requests. |
| `code-review-swarm` | Coordinates multi-agent code review on pull requests. |
| `issue-tracker` | Manages GitHub issues -- creation, triage, labeling, and closure. |
| `release-manager` | Manages release processes -- changelogs, version bumping, tagging. |
| `workflow-automation` | Creates and manages GitHub Actions workflows. |
| `project-board-sync` | Synchronizes project boards with issue and PR states. |
| `repo-architect` | Analyzes and recommends repository structure improvements. |
| `multi-repo-swarm` | Coordinates work across multiple repositories simultaneously. |

### SPARC Methodology (6 types)

| Type | Description |
|------|-------------|
| `sparc-coord` | Coordinates the SPARC methodology (Specification, Pseudocode, Architecture, Refinement, Completion). |
| `sparc-coder` | Implements code following SPARC methodology principles. |
| `specification` | Writes formal specifications and requirements documents. |
| `pseudocode` | Develops pseudocode representations of algorithms and logic. |
| `architecture` | Designs system architecture, component diagrams, and interfaces. |
| `refinement` | Iteratively refines implementations against specifications. |

### Specialized Development (8 types)

| Type | Description |
|------|-------------|
| `backend-dev` | Specializes in backend services, APIs, databases, and server-side logic. |
| `mobile-dev` | Specializes in mobile application development (iOS, Android, cross-platform). |
| `ml-developer` | Specializes in machine learning model development, training, and evaluation. |
| `cicd-engineer` | Designs and implements CI/CD pipelines, build systems, and deployment automation. |
| `api-docs` | Writes API documentation, endpoint specifications, and usage examples. |
| `system-architect` | Designs large-scale system architectures with scalability and reliability. |
| `code-analyzer` | Performs static analysis, code quality assessment, and complexity metrics. |
| `base-template-generator` | Generates boilerplate code and project templates from specifications. |

### Testing and Validation (2 types)

| Type | Description |
|------|-------------|
| `tdd-london-swarm` | Implements London-school TDD (mockist) with outside-in development. |
| `production-validator` | Validates production readiness -- checks health endpoints, monitoring, logging. |

---

## Glossary

| Term | Definition |
|------|-----------|
| **Agent** | A single Claude Code instance with an assigned role and task. |
| **AgentDB** | The memory/knowledge database system used by Claude Flow agents. |
| **BFT** | Byzantine Fault Tolerance -- consensus that works even if some agents produce bad output. |
| **Coordinator** | The lead agent in a hierarchical swarm that delegates work to specialists. |
| **CRDT** | Conflict-free Replicated Data Type -- a data structure that allows concurrent updates without conflicts. |
| **Daemon** | A background process that runs workers and monitors agent health. |
| **Hive** | A project with agent orchestration, skills, governance (CLAUDE.md), and V3 rules. |
| **HNSW** | Hierarchical Navigable Small World -- the algorithm used for fast vector similarity search. |
| **Hook** | An event-driven callback that fires at lifecycle boundaries. |
| **MCP** | Model Context Protocol -- the protocol used for communication between Claude and tools. |
| **Namespace** | A logical partition within memory for organizing entries by topic. |
| **Output** | An artifact produced by one or more hives. No agents, no orchestration. |
| **Queen** | The lead agent in a Hive-Mind consensus process. |
| **RuVector** | The self-optimizing neural intelligence system within Claude Flow. |
| **Skill** | A reusable, documented capability stored in `.claude/skills/`. |
| **SONA** | Self-Optimizing Neural Architecture -- adaptive routing within RuVector. |
| **Swarm** | A group of coordinated agents with a topology and strategy. |
| **Topology** | The communication graph structure between agents in a swarm. |
| **V3** | Version 3 of Claude Flow's governance system with rule annotations. |
| **Worker** | A background process that performs maintenance or analysis tasks. |

---

*This manual covers Claude Flow v3.1.0-alpha.3. For the condensed command reference,
see the Quick-Start Cheat Sheet. For installation and first-run instructions, see
the Getting Started Guide. For the raw CLI reference, see `docs/claude-flow-reference.md`.*

*Documentation maintained by the PostWach research group, University of Arizona.*
