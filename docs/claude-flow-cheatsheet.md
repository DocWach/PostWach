# Claude Flow v3.1.0 Quick-Start Cheat Sheet

## Setup (one-time)

```bash
npm install -g @anthropic-ai/claude-code
claude                                    # first launch → sign in
npm install -g @claude-flow/cli
claude-flow doctor --fix
```

## Start a Session

```bash
claude                                    # open Claude Code
claude-flow --version                     # verify v3.1.x
claude-flow hooks session-start           # restore prior state
```

## Swarms

```bash
claude-flow swarm init --topology hierarchical --max-agents 8 --strategy specialized
claude-flow swarm status                  # monitor
claude-flow swarm stop                    # tear down
```

| Topology | Best For |
|----------|----------|
| hierarchical | Structured tasks, report writing |
| mesh | Brainstorming, peer review |
| star | Parallel independent tasks |
| ring | Sequential pipeline |

## Agents

```bash
claude-flow agent spawn -t coder         # spawn by type
claude-flow agent list                    # active agents
claude-flow agent status <id>            # inspect one
claude-flow agent stop <id>              # terminate one
claude-flow agent metrics <id>           # performance data
claude-flow agent logs <id>              # view logs
```

Common types: `coder` `reviewer` `tester` `planner` `researcher` `architect` `security-architect`

## Task Routing

```bash
claude-flow hooks route --task "fix the bug in parser.py"
claude-flow hooks explain --topic "why coder agent?"
```

| Code | Task Type | Agents Spawned |
|------|-----------|----------------|
| 1 | Bug fix | coordinator, researcher, coder, tester |
| 3 | Feature | coordinator, architect, coder, tester, reviewer |
| 5 | Refactor | coordinator, architect, coder, reviewer |
| 9 | Security | coordinator, security-architect, auditor |
| 11 | Docs | researcher, api-docs |

## Memory (AgentDB)

```bash
claude-flow memory store --key "name" --value "data" --namespace research
claude-flow memory retrieve --key "name" --namespace research
claude-flow memory search --query "search terms" --namespace research
claude-flow memory list --namespace research
claude-flow memory stats
claude-flow memory init --force           # reset if empty
```

## Session End

```bash
claude-flow hooks session-end --generate-summary --export-metrics
```

## Environment Variables

```bash
CLAUDE_FLOW_LOG_LEVEL=info                # debug | info | warn | error
CLAUDE_FLOW_MEMORY_BACKEND=hybrid         # hybrid | vector | key-value
CLAUDE_FLOW_MEMORY_PATH=./data/memory     # memory storage location
CLAUDE_FLOW_MCP_PORT=3000                 # MCP server port
```

Note: Claude Code handles authentication interactively on first launch -- no API key export needed.

## Troubleshooting

| Problem | Fix |
|---------|-----|
| `command not found` | Verify PATH includes npm global bin (`npm bin -g`) |
| Auth errors | Re-run `claude` and follow sign-in prompts |
| Memory empty | `claude-flow memory init --force` |
| Swarm won't start | `claude-flow doctor --fix` |
| Stale agents | `claude-flow agent list` then `agent stop <id>` |
| Session lost | `claude-flow hooks session-restore --latest` |

## Key Rules

- Always use `claude-flow` (globally installed). Never use `npx @claude-flow/cli@latest`.
- Terminate idle agents at session end. Do not leave orphans across sessions.
- Memory namespaces: `patterns`, `research`, `coordination` (pick one per use case).

## References

- Getting Started Guide: `docs/claude-flow-getting-started.md`
- Full User Manual: `docs/claude-flow-user-manual.md`
- Internal CLI Reference: `docs/claude-flow-reference.md`
- Project repo: https://github.com/ruvnet/claude-flow
