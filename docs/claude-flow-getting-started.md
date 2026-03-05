# Getting Started with Claude Flow

**Audience:** University of Arizona researchers new to Claude Code and claude-flow
**Version:** claude-flow v3.1.0-alpha.3
**Platform:** Windows 11 (commands use bash/Unix syntax)
**Estimated reading time:** 15-20 minutes
**Prepared for:** Research team meeting, March 6, 2026

---

## Table of Contents

1. [What is Claude Flow?](#1-what-is-claude-flow)
2. [Prerequisites](#2-prerequisites)
3. [Installation](#3-installation)
4. [Your First Session](#4-your-first-session)
5. [Your First Swarm](#5-your-first-swarm)
6. [Memory Basics](#6-memory-basics)
7. [Common First-Day Tasks](#7-common-first-day-tasks)
8. [Key Commands Quick Reference](#8-key-commands-quick-reference)
9. [Where to Go Next](#9-where-to-go-next)
10. [Troubleshooting](#10-troubleshooting)

---

## 1. What is Claude Flow?

**Claude Code** is Anthropic's official command-line interface (CLI) for working with Claude. It gives you a single AI assistant that can read your files, edit code, run commands, and search your codebase -- all from the terminal.

**Claude Flow** is an orchestration platform that runs on top of Claude Code. It extends that single assistant into a coordinated team of specialized AI agents that can work together on complex tasks.

Here is the simplest way to think about it:

- **Claude Code** = one skilled research assistant sitting at your computer.
- **Claude Flow** = a research team with a coordinator, subject-matter experts, reviewers, and shared institutional memory, all working on your project simultaneously.

What claude-flow enables:

- **Multi-agent swarms**: Spin up teams of AI agents with different specializations (researcher, coder, reviewer, tester) that collaborate on a task.
- **Persistent memory**: Store findings, decisions, and context so that your next session picks up where you left off -- even days or weeks later.
- **Intelligent task routing**: Describe what you need done, and claude-flow figures out which agents and approach best fit the work.
- **Collaborative AI workflows**: Break large research tasks (literature reviews, code analysis, manuscript drafting) into parallel subtasks that multiple agents handle concurrently.

You do not need to understand all of these on day one. Start with Claude Code alone, and layer in claude-flow capabilities as your comfort grows.

---

## 2. Prerequisites

Before installing, make sure you have the following on your machine.

### Required

| Tool | Minimum Version | How to Check |
|------|----------------|--------------|
| **Node.js** | v18 or later | `node --version` |
| **npm** | Comes with Node.js | `npm --version` |
| **A terminal** | -- | Windows Terminal, VS Code integrated terminal, or Git Bash |

### Recommended

| Tool | Why |
|------|-----|
| **Git** | Version control for your projects; many claude-flow features integrate with git repositories |
| **VS Code** | Popular editor with an integrated terminal; claude-flow works well alongside it |

---

## 3. Installation

Open your terminal (Windows Terminal or VS Code integrated terminal) and run the following commands one at a time.

### Step 1: Install Claude Code

```bash
npm install -g @anthropic-ai/claude-code
```

This installs Claude Code globally so you can use the `claude` command from any directory.

### Step 2: Launch Claude Code and Authenticate

```bash
claude
```

The first time you run `claude`, it will walk you through an interactive authentication flow. Follow the on-screen prompts to sign in with your Anthropic account. Once authenticated, your credentials are stored locally and you will not need to sign in again.

After authentication completes, type `/exit` to return to your terminal.

**Note:** Claude Code handles authentication automatically -- you do not need to manually set an API key.

### Step 3: Verify Claude Code

```bash
claude --version
```

You should see a version number. If you get "command not found," see the [Troubleshooting](#10-troubleshooting) section.

### Step 4: Install Claude Flow

```bash
npm install -g @claude-flow/cli
```

This installs claude-flow globally. Always use the globally installed `claude-flow` command -- never use `npx @claude-flow/cli@latest`.

### Step 5: Verify Claude Flow

```bash
claude-flow --version
```

You should see `v3.1.0-alpha.3` or later.

### Step 6: Run Diagnostics

```bash
claude-flow doctor
```

This checks that all dependencies are correctly installed and the system is ready. If it reports any issues, follow the on-screen suggestions to fix them.

### Summary of What You Just Installed

| Command | What It Does |
|---------|--------------|
| `claude` | Starts the Claude Code interactive CLI (single AI assistant) |
| `claude-flow` | Orchestrates multi-agent workflows, memory, routing, and swarms |

---

## 4. Your First Session

Now that everything is installed, let us walk through a basic Claude Code session.

### Starting Claude Code

Open a terminal, navigate to a project directory, and type:

```bash
claude
```

This launches the Claude Code interactive CLI. You will see a prompt where you can type natural-language instructions.

### What You Can Do

Claude Code has a set of built-in tools it uses to interact with your project. You do not need to invoke these tools directly -- just describe what you want, and Claude will choose the right tools. Here are the main ones:

| Tool | What It Does | Example Request |
|------|-------------|-----------------|
| **Read** | Opens and displays file contents | "Read the file src/analysis.py" |
| **Write** | Creates new files | "Create a new Python script that loads our CSV data" |
| **Edit** | Modifies existing files | "Change the plot title in figure_3.py to 'Response Time Distribution'" |
| **Bash** | Runs terminal commands | "Run the test suite with pytest" |
| **Grep** | Searches file contents | "Find all files that reference 'learning_rate'" |
| **Glob** | Finds files by name pattern | "Find all Python files in the src directory" |
| **Agent** | Spawns a background sub-agent for parallel work | "Search the codebase for all configuration patterns" |

### A Simple Interaction

Here is an example of what a first session might look like. After starting `claude`, you might type:

```
Show me the structure of this project -- list the top-level directories and
briefly describe what each one contains based on its name and contents.
```

Claude will use its tools (Glob to find directories, Read to examine files) and give you a structured overview. You can then follow up:

```
Read the file src/data_loader.py and explain what it does.
```

### Ending a Session

Type `/exit` or press `Ctrl+C` to leave the Claude Code session.

### Key Concept

Claude Code works *within your project directory*. It can see and interact with files on your local machine. It does not send your files to the cloud -- it reads them locally and sends only the relevant context to the Claude API for processing.

---

## 5. Your First Swarm

A **swarm** is a team of AI agents working together under a coordinator. This is where claude-flow goes beyond basic Claude Code.

### When to Use a Swarm vs. Single-Agent Work

| Situation | Use |
|-----------|-----|
| Quick question, small edit, file lookup | Single Claude Code session (`claude`) |
| Multi-file analysis, parallel tasks, literature review, complex debugging | Swarm (`claude-flow swarm init`) |
| Anything where you would want 2-5 people working simultaneously | Swarm |

### Starting a Swarm

Run this command from your project directory:

```bash
claude-flow swarm init --topology hierarchical --max-agents 5 --strategy specialized
```

Let us break down what each option means:

| Option | Value | Meaning |
|--------|-------|---------|
| `--topology` | `hierarchical` | One coordinator agent delegates work to specialist agents. Best for most research tasks. Other options include `mesh` (everyone talks to everyone) and `star` (hub-and-spoke). |
| `--max-agents` | `5` | Up to 5 agents can be active at once. Start small; you can increase later. Each agent uses API tokens, so more agents = higher cost. |
| `--strategy` | `specialized` | Each agent has a defined role (researcher, coder, reviewer, etc.) rather than all agents being generalists. |

### Checking Swarm Status

After initialization, check that your swarm is running:

```bash
claude-flow swarm status
```

This shows you which agents are active, what they are working on, and the overall health of the swarm.

### What Happens Inside a Swarm

When you give a swarm a complex task, the coordinator agent:

1. Breaks the task into subtasks.
2. Assigns each subtask to the most appropriate specialist agent.
3. Monitors progress and resolves conflicts.
4. Synthesizes the results into a coherent output.

For example, if you ask a swarm to "review the methodology section of our paper and suggest improvements," the coordinator might assign one agent to check the statistical methods, another to verify citations, and a third to assess the logical flow.

### Stopping a Swarm

When you are done:

```bash
claude-flow swarm stop
```

Always stop your swarm at the end of a session to avoid leaving orphaned agents running in the background.

---

## 6. Memory Basics

One of claude-flow's most valuable features for research is **persistent memory**. Without it, every Claude session starts from scratch. With memory, you can store findings, decisions, and context that persist across sessions -- even days or weeks apart.

### Why This Matters for Research

Imagine you spend an afternoon exploring a new dataset and discover several important patterns. Without memory, your next session knows nothing about those discoveries. With memory, you store them once and retrieve them whenever needed.

### Storing a Finding

```bash
claude-flow memory store --key "finding-1" --value "The API uses REST endpoints with OAuth2 authentication" --namespace research
```

| Parameter | Purpose |
|-----------|---------|
| `--key` | A unique name for this piece of information (like a variable name) |
| `--value` | The actual content you want to store |
| `--namespace` | A category that groups related memories together |

### Searching Memory

When you need to find something you stored previously:

```bash
claude-flow memory search --query "API endpoints" --namespace research
```

This performs a semantic search -- it does not just match exact words. Searching for "API endpoints" will find your stored entry about "REST endpoints with OAuth2 authentication" because the meanings are related.

### Listing Everything in a Namespace

To see all stored entries in a namespace:

```bash
claude-flow memory list --namespace research
```

### Retrieving a Specific Entry

If you know the exact key:

```bash
claude-flow memory retrieve --key "finding-1" --namespace research
```

### Organizing with Namespaces

Think of namespaces as folders for your memory. Here are some namespace patterns that work well for research:

| Namespace | What to Store |
|-----------|---------------|
| `research` | Findings, hypotheses, data observations |
| `methods` | Methodology decisions, parameter choices, analysis approaches |
| `literature` | Key papers, citations, author claims |
| `decisions` | Design decisions and their rationale |
| `patterns` | Recurring patterns discovered in code or data |

You can create any namespace you like -- they are created automatically the first time you store something in them.

---

## 7. Common First-Day Tasks

Here are concrete examples of tasks you are likely to perform in your first week.

### Task 1: Explore a New Codebase

You have just cloned a repository and want to understand its structure.

Start a Claude Code session in the project directory:

```bash
claude
```

Then ask:

```
Give me a high-level overview of this project. What language is it written in,
what are the main modules, and where is the entry point?
```

Follow up with targeted questions:

```
Find all files that contain database queries.
```

```
Read src/models/experiment.py and explain the data model.
```

This is faster than manually reading through unfamiliar code and gives you a structured mental model of the project.

### Task 2: Write a Literature Review with a Swarm

For a more complex task like drafting a literature review section, use a swarm:

```bash
claude-flow swarm init --topology hierarchical --max-agents 5 --strategy specialized
```

Then route the task:

```bash
claude-flow hooks route --task "Draft a literature review section covering adversarial robustness in large language models. Use the 15 papers in Papers/adversarial_robustness/ as source material. The review should be 2000-3000 words in IEEE citation style."
```

The swarm will assign researcher agents to analyze the papers and a writer agent to synthesize the findings. The coordinator ensures consistency and completeness.

### Task 3: Debug a Script

When a script is throwing errors:

```bash
claude-flow hooks route --task "fix the parsing error in src/process.py"
```

Claude-flow routes this to agents specialized in debugging. They will read the file, identify the error, propose a fix, and optionally run tests to verify the fix works.

For simpler debugging, you can also just use Claude Code directly:

```bash
claude
```

Then:

```
The script src/process.py crashes with a KeyError on line 47.
Read the file and fix the bug.
```

### Task 4: Store Findings for Your Next Session

At the end of a productive session, store what you learned:

```bash
claude-flow memory store --key "dataset-structure" --value "The sensor data CSV has 47 columns. Columns 1-10 are metadata, 11-40 are sensor readings (mV), 41-47 are derived features. Missing values encoded as -999." --namespace experiment-1

claude-flow memory store --key "outlier-threshold" --value "After EDA, we determined outliers are readings above 3.2 standard deviations from the rolling mean. This excludes approximately 2.1% of observations." --namespace experiment-1
```

Next time you start a session, retrieve this context:

```bash
claude-flow memory search --query "sensor data format" --namespace experiment-1
```

---

## 8. Key Commands Quick Reference

These are the 10 commands you will use most on day one.

| Command | What It Does |
|---------|-------------|
| `claude` | Start an interactive Claude Code session |
| `claude-flow --version` | Check your claude-flow version |
| `claude-flow doctor` | Run diagnostics to verify setup |
| `claude-flow swarm init --topology hierarchical --max-agents 5 --strategy specialized` | Start a 5-agent swarm |
| `claude-flow swarm status` | Check which agents are active and what they are doing |
| `claude-flow swarm stop` | Shut down all swarm agents |
| `claude-flow memory store --key "name" --value "data" --namespace topic` | Save a piece of information |
| `claude-flow memory search --query "search terms" --namespace topic` | Find stored information by meaning |
| `claude-flow memory list --namespace topic` | List all entries in a namespace |
| `claude-flow hooks route --task "description of work"` | Route a task to the best-fit agents |

---

## 9. Where to Go Next

Once you are comfortable with the basics above, here are your next resources.

### Reference Documentation

- **Comprehensive Reference Manual**: `docs/claude-flow-reference.md` in this repository. Contains the full command reference, all 60+ agent types, the hooks system, topology options, and environment variables.
- **Claude Flow GitHub**: [https://github.com/ruvnet/claude-flow](https://github.com/ruvnet/claude-flow) -- source code, issue tracker, and community discussions.

### Concepts Worth Exploring Next

| Concept | Why It Matters | Reference |
|---------|---------------|-----------|
| **Hooks** | Automate recurring workflows (pre-edit checks, post-task learning) | `claude-flow hooks list` |
| **Task routing** | Let claude-flow choose the optimal agent for any task | `claude-flow hooks route --task "..."` |
| **Agent types** | 60+ specialized agents for different work (security audits, API docs, testing) | Reference manual, Agent Routing Table |
| **Topologies** | Different team structures for different problems (hierarchical, mesh, star) | Reference manual, Anti-Drift Config |
| **Sessions** | Save and restore entire working sessions | `claude-flow session --help` |

### Getting Help

From any claude-flow command, add `--help` to see available options:

```bash
claude-flow swarm --help
claude-flow memory --help
claude-flow hooks --help
```

---

## 10. Troubleshooting

### "claude-flow: command not found"

**Cause:** npm's global installation directory is not in your system PATH.

**Fix:**

1. Find where npm installs global packages:
   ```bash
   npm config get prefix
   ```
2. Add that path (appending `/bin` on Unix-like shells) to your PATH environment variable.
3. On Windows, the typical path is `C:\Users\<username>\AppData\Roaming\npm`. Make sure this is in your system PATH via System Environment Variables.
4. Restart your terminal after changing PATH.

### "Authentication required" or sign-in issues

**Cause:** Claude Code's authentication has expired or was not completed.

**Fix:**

```bash
claude
```

Re-run `claude` and follow the interactive sign-in prompts. Once authenticated, your credentials are stored locally and persist across terminal sessions.

### "Permission denied" during installation

**Cause:** npm does not have permission to write to the global packages directory.

**Fix (choose one):**

- Run your terminal as Administrator (right-click, "Run as administrator").
- Fix npm permissions by changing the global directory:
  ```bash
  mkdir ~/.npm-global
  npm config set prefix '~/.npm-global'
  ```
  Then add `~/.npm-global/bin` to your PATH.

### "Memory search returns nothing"

**Cause:** The memory system may need to be initialized for your project.

**Fix:**

```bash
claude-flow memory init
```

This creates the memory storage backend for the current project. After initialization, try your search again.

Also verify you are searching the correct namespace. Use `claude-flow memory list --namespace <name>` to confirm entries exist.

### "claude: command not found"

**Cause:** Claude Code is not installed globally, or PATH does not include npm's global bin directory.

**Fix:**

```bash
npm install -g @anthropic-ai/claude-code
```

Then verify:

```bash
claude --version
```

If this still fails, see the "command not found" fix above for PATH issues.

### Swarm agents seem stuck or unresponsive

**Fix:**

1. Check status: `claude-flow swarm status`
2. If agents are listed but not progressing, stop and restart the swarm:
   ```bash
   claude-flow swarm stop
   claude-flow swarm init --topology hierarchical --max-agents 5 --strategy specialized
   ```
3. Run diagnostics: `claude-flow doctor`

### General Debugging Steps

For any issue not listed above:

1. Run `claude-flow doctor` -- it checks most common problems automatically.
2. Verify your Node.js version: `node --version` (must be v18+).
3. Verify Claude Code authentication: run `claude` and confirm you can start a session.
4. Check the claude-flow GitHub issues page: [https://github.com/ruvnet/claude-flow/issues](https://github.com/ruvnet/claude-flow/issues).

---

## Companion Documents

- **Comprehensive Reference Manual:** `docs/claude-flow-user-manual.md` -- full coverage of swarms, agents, memory, hooks, governance, and research workflows
- **Quick-Start Cheat Sheet:** `docs/claude-flow-cheatsheet.md` -- 2-page command reference card to keep open while working
- **Internal CLI Reference:** `docs/claude-flow-reference.md` -- technical command surface (used by AI agents)

---

*This guide was prepared for the University of Arizona research team. For questions or issues, contact the PostWach research group.*
