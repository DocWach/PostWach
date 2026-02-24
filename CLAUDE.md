# PostDoc Project Instructions

## Rules
- [R101] Do what has been asked; nothing more, nothing less. @quality [all] risk:high
- [R102] NEVER create files unless absolutely necessary. Prefer editing existing files. @quality [edit] risk:medium
- [R103] NEVER proactively create documentation files (*.md) unless explicitly requested. @quality [edit] risk:medium
- [R104] NEVER save working files, text/mds, or tests to the root folder. @quality [edit] risk:medium
- [R105] NEVER commit .env, API keys, credentials, or secrets. @security [bash,edit] risk:critical
- [R106] ALWAYS use the globally installed `claude-flow` command, never `npx @claude-flow/cli@latest`. @quality [bash] risk:medium

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
