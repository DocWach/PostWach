#!/usr/bin/env node
/**
 * SessionEnd helper: terminate idle agents to keep AgentDB from accumulating
 * orphaned rows across sessions. Implements the CLAUDE.md rule
 * "Terminate idle agents at session end."
 *
 * Orphaned agent rows are harmless (not live processes, no CPU/RAM), but they
 * inflate `agent_list` output and can confuse diagnostics.
 *
 * Fail-silent: never crashes Claude Code on hook errors.
 */

import { McpClient, parseToolResult } from './mcp-client.mjs';

const DIM = '\x1b[2m';
const GREEN = '\x1b[0;32m';
const RESET = '\x1b[0m';

async function main() {
  const client = new McpClient();
  try {
    await client.start({ timeoutMs: 8000 });
    const list = parseToolResult(await client.call('agent_list', {}, { timeoutMs: 5000 }));
    const agents = (list && list.agents) || [];
    const idle = agents.filter((a) => a.status === 'idle' && (a.taskCount || 0) === 0);

    if (idle.length === 0) {
      console.log(`${DIM}[AgentCleanup] No idle agents to terminate${RESET}`);
      return;
    }

    const results = await Promise.allSettled(
      idle.map((a) =>
        client.call('agent_terminate', { agentId: a.agentId }, { timeoutMs: 3000 }),
      ),
    );
    const terminated = results.filter((r) => r.status === 'fulfilled').length;
    console.log(`${GREEN}[AgentCleanup] ✓ Terminated ${terminated}/${idle.length} idle agents${RESET}`);
  } catch (err) {
    console.log(`${DIM}[AgentCleanup] Skipped (non-critical): ${err.message}${RESET}`);
  } finally {
    await client.close();
  }
}

main();
