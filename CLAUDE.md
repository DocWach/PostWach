# Project Instructions

## Rules
- Do what has been asked; nothing more, nothing less.
- NEVER create files unless absolutely necessary. Prefer editing existing files.
- NEVER proactively create documentation files (*.md) unless explicitly requested.
- NEVER save working files, text/mds, or tests to the root folder.

## File Organization
- `/src` - Source code
- `/tests` - Test files
- `/docs` - Documentation
- `/config` - Configuration
- `/scripts` - Utility scripts
- `/Papers` - Research papers and manuscripts

## Parallel Execution
- Batch all related operations in ONE message (file ops, bash commands, agent spawns).
- For complex multi-file tasks, use Task tool with `run_in_background: true` for concurrent agents.
- After spawning background agents, report what's running and wait for results.

## Claude Flow CLI (coordination via Bash)
For full reference: `docs/claude-flow-reference.md`

```bash
# Essential commands
npx @claude-flow/cli@latest swarm init --topology hierarchical --max-agents 8 --strategy specialized
npx @claude-flow/cli@latest memory search --query "search terms"
npx @claude-flow/cli@latest memory store --key "name" --value "data" --namespace patterns
npx @claude-flow/cli@latest hooks route --task "[task description]"
```
