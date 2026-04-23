#!/usr/bin/env node
/**
 * Auto Memory Bridge Hook (MCP-based, Option A-trim)
 *
 * Wires Claude Code session lifecycle to the claude-flow MCP bridge.
 * Replaces the earlier in-process @claude-flow/memory dependency (not shipped
 * in claude-flow v3.5.80) with MCP calls, so this hook survives upstream
 * package churn.
 *
 * Commands:
 *   node auto-memory-hook.mjs import   # SessionStart: MEMORY.md -> AgentDB
 *   node auto-memory-hook.mjs sync     # SessionEnd: no-op (see note below)
 *   node auto-memory-hook.mjs status   # Show bridge state
 *
 * Note on sync: the prior implementation synced AgentDB insights back into
 * MEMORY.md (PageRank-ordered index curation). The MCP surface does not
 * expose that direction, so `sync` is now a logged no-op. MEMORY.md remains
 * hand-curated; the `import` direction runs every SessionStart.
 */

import { existsSync, mkdirSync, readFileSync } from 'fs';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';
import { McpClient, parseToolResult } from './mcp-client.mjs';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
const PROJECT_ROOT = join(__dirname, '../..');
const DATA_DIR = join(PROJECT_ROOT, '.claude-flow', 'data');

const GREEN = '\x1b[0;32m';
const CYAN = '\x1b[0;36m';
const DIM = '\x1b[2m';
const RESET = '\x1b[0m';

const log = (msg) => console.log(`${CYAN}[AutoMemory] ${msg}${RESET}`);
const success = (msg) => console.log(`${GREEN}[AutoMemory] ✓ ${msg}${RESET}`);
const dim = (msg) => console.log(`  ${DIM}${msg}${RESET}`);

if (!existsSync(DATA_DIR)) mkdirSync(DATA_DIR, { recursive: true });

function readConfig() {
  const configPath = join(PROJECT_ROOT, '.claude-flow', 'config.yaml');
  const defaults = {
    learningBridge: { enabled: true },
    memoryGraph: { enabled: true },
    agentScopes: { enabled: true },
  };
  if (!existsSync(configPath)) return defaults;
  try {
    const yaml = readFileSync(configPath, 'utf-8');
    const getBool = (section) => {
      const m = yaml.match(new RegExp(`${section}[\\s\\S]*?enabled:\\s*(true|false)`, 'i'));
      return m ? m[1] === 'true' : undefined;
    };
    const lb = getBool('learningBridge');
    if (lb !== undefined) defaults.learningBridge.enabled = lb;
    const mg = getBool('memoryGraph');
    if (mg !== undefined) defaults.memoryGraph.enabled = mg;
    const as = getBool('agentScopes');
    if (as !== undefined) defaults.agentScopes.enabled = as;
  } catch { /* defaults */ }
  return defaults;
}

async function withMcp(fn, { timeoutMs = 15000 } = {}) {
  const client = new McpClient();
  try {
    await client.start({ timeoutMs });
    return await fn(client);
  } finally {
    await client.close();
  }
}

async function doImport() {
  log('Importing Claude Code auto-memory files into AgentDB via MCP...');
  try {
    const result = await withMcp(async (client) => {
      return parseToolResult(
        await client.call(
          'memory_import_claude',
          { allProjects: true },
          { timeoutMs: 30000 },
        ),
      );
    });
    if (!result) {
      dim('Import returned no data (non-critical)');
      return;
    }
    const imported = result.imported ?? result.count ?? 0;
    const skipped = result.skipped ?? 0;
    const namespace = result.namespace || 'claude-memories';
    success(`Imported ${imported} entries (${skipped} skipped) into ${namespace}`);
    if (result.projects) dim(`├─ Projects scanned: ${result.projects}`);
    if (result.files) dim(`├─ Memory files read: ${result.files}`);
    dim(`└─ Backend: AgentDB (sql.js + ONNX)`);
  } catch (err) {
    dim(`Import skipped (non-critical): ${err.message}`);
  }
}

async function doSync() {
  dim('Sync is a no-op in MCP-only mode (MEMORY.md is hand-curated).');
  dim('Import direction runs at SessionStart; no reverse sync is exposed by MCP.');
}

async function doStatus() {
  const config = readConfig();
  console.log('\n=== Auto Memory Bridge Status ===\n');
  console.log(`  Mode:           MCP-only (Option A-trim)`);
  console.log(`  LearningBridge: ${config.learningBridge.enabled ? '✅ Enabled' : '⏸ Disabled'}`);
  console.log(`  MemoryGraph:    ${config.memoryGraph.enabled ? '✅ Enabled' : '⏸ Disabled'}`);
  console.log(`  AgentScopes:    ${config.agentScopes.enabled ? '✅ Enabled' : '⏸ Disabled'}`);

  try {
    const bridge = await withMcp(async (client) => {
      return parseToolResult(
        await client.call('memory_bridge_status', {}, { timeoutMs: 8000 }),
      );
    }, { timeoutMs: 8000 });

    if (bridge) {
      const cc = bridge.claudeCode || {};
      const db = bridge.agentdb || {};
      const br = bridge.bridge || {};
      console.log(`  MEMORY.md files: ${cc.memoryFiles ?? '?'} across ${cc.projects ?? '?'} projects`);
      console.log(`  AgentDB entries: ${db.totalEntries ?? '?'} (${db.claudeMemoryEntries ?? 0} from Claude memories)`);
      console.log(`  Bridge status:   ${br.status || 'unknown'}`);
    } else {
      console.log(`  Bridge status:   unavailable`);
    }
  } catch (err) {
    console.log(`  Bridge status:   error (${err.message})`);
  }
  console.log('');
}

// Accept the command from any argv position. When launched via
// `node -e "..." import`, argv is [node, "import"]; when launched as
// `node auto-memory-hook.mjs import`, argv is [node, script, "import"].
const VALID = new Set(['import', 'sync', 'status']);
const command = process.argv.slice(1).find((a) => VALID.has(a)) || 'status';

try {
  switch (command) {
    case 'import': await doImport(); break;
    case 'sync': await doSync(); break;
    case 'status': await doStatus(); break;
    default:
      console.log('Usage: auto-memory-hook.mjs <import|sync|status>');
      process.exit(1);
  }
} catch (err) {
  dim(`Error (non-critical): ${err.message}`);
}
