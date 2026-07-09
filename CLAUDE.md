# PostDoc Project Instructions

## Rules
- [R101] Do what has been asked; nothing more, nothing less. @quality [all] risk:high
- [R102] NEVER create files unless absolutely necessary. Prefer editing existing files. @quality [edit] risk:medium
- [R103] NEVER proactively create documentation files (*.md) unless explicitly requested. @quality [edit] risk:medium
- [R104] NEVER save working files, text/mds, or tests to the root folder. @quality [edit] risk:medium
- [R105] NEVER commit .env, API keys, credentials, or secrets. @security [bash,edit] risk:critical
- [R106] ALWAYS use the globally installed `claude-flow` command in shell usage and MCP registrations (`.mcp.json`). Never use `npx`-based invocations (`npx @claude-flow/cli@latest`, `npx claude-flow@alpha`). Implements global [R017]. @quality [bash,edit] risk:high
- [R108] When PostWach's code compiles and tests pass, create the SEAD handoff within 30 minutes. Do not debug deployment, rendering, or infrastructure issues beyond initial diagnosis. PostWach owns architecture; SEAD owns build engineering. Applies to executable software artifacts (compiled code, deployable services, container images). Document/manuscript typesetting (any source format) stays with the originating researcher. @process [all] risk:medium
- [R109] References in manuscripts MUST exist in the portfolio approved-references store at `04 Resource Library/00 Verified References/`. Implements global [R019]. Pre-render gate: `01 PostWach/scripts/refcheck.py`. @quality @research [edit] risk:critical

## File Organization
- `/src` - Source code
- `/tests` - Test files
- `/docs` - Documentation and session archives
- `/config` - Configuration
- `/scripts` - Utility scripts
- `/Papers` - Research papers and manuscripts (AI4RE_SLR, AI_Investing_Platform, Dissertation_Journal, Agentic_AI_Swarms_SE, Neuro_Symbolic_Wargaming)
- [R107] `/Background docs` - Reference publications (read-only, never modify). @research [edit] risk:high

## Architecture
- Research co-pilot project; no compiled build artifacts.
- Primary outputs are manuscripts, analysis scripts, and literature reviews.
- Claude Flow v3.1.x provides agent orchestration via globally installed CLI.

## Parallel Execution
- Batch all related operations in ONE message (file ops, bash commands, agent spawns).
- For complex multi-file tasks, use Task tool with `run_in_background: true` for concurrent agents.
- After spawning background agents, report what's running and wait for results.

## Agent Governance
- When spawning swarm agents, register memory gate authorities:
  - Main session / coordinator agents: `coordinator` role
  - Search and reviewer agents: `worker` role (limited write, scoped namespaces)
- Terminate idle agents at session end. Do not leave orphaned agents across sessions.

## Build & Test
- No compiled build step; test scripts live in `/tests`.
- Run tests with: `python -m pytest tests/` or project-specific test commands.
- Validate paper formatting with project-specific linting when available.

## Cross-Project Role
- PostWach is the CTO / Chief Scientist for the research portfolio.
- Maintains `docs/project-registry.md` (hive/output classification) and `docs/capability-index.md`.
- Alpha Empress (COO) handles governance compliance; PostWach handles capability quality.

## Claude Flow CLI
For full reference: `docs/claude-flow-reference.md`

```bash
claude-flow swarm init --topology hierarchical --max-agents 8 --strategy specialized
claude-flow memory search --query "search terms"
claude-flow memory store --key "name" --value "data" --namespace patterns
claude-flow hooks route --task "[task description]"
```
