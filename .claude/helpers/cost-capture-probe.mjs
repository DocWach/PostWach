#!/usr/bin/env node
/**
 * Cost-Capture Probe + Prototype (B0/B1 of cost_instrumentation_spec_2026-07-16)
 *
 * Two jobs:
 *   1. B0 PROBE: when invoked as a SessionEnd hook, dump the EXACT stdin payload
 *      the harness passes (+ any token/cost-ish env vars) so we learn empirically
 *      whether SessionEnd exposes usage. Writes .claude-flow/data/sessionend-probe.json.
 *   2. B1 CAPTURE PROTOTYPE: regardless of stdin, derive the session transcript
 *      path (deterministic: ~/.claude/projects/<slug>/<session_id>.jsonl), parse
 *      per-turn usage blocks, and sum tokens. Proves auto-capture is feasible.
 *
 * Modes:
 *   node cost-capture-probe.mjs          # hook mode: read stdin, probe + parse
 *   node cost-capture-probe.mjs <file>   # manual: parse a specific transcript jsonl
 *
 * Never throws; always exits 0 (hooks must not crash Claude Code).
 */

import { existsSync, mkdirSync, readFileSync, writeFileSync, readdirSync, statSync } from 'fs';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';
import { homedir } from 'os';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
const PROJECT_ROOT = join(__dirname, '..', '..');
const DATA_DIR = join(PROJECT_ROOT, '.claude-flow', 'data');
const PROBE_OUT = join(DATA_DIR, 'sessionend-probe.json');

function ensureDir(d) { try { if (!existsSync(d)) mkdirSync(d, { recursive: true }); } catch { /* noop */ } }

// Deterministic transcript dir for THIS project (Claude Code slugifies the abs path:
// drive-letter lowercased path with every non-alnum run -> '-'; a ' - ' becomes '---').
function transcriptDir() {
  return join(homedir(), '.claude', 'projects',
    'C--Users-pfwac-OneDrive---University-of-Arizona-Documents-03-Projects-00-Hive-Empire-01-Hives-01-PostWach');
}

// Sum usage across all assistant turns in a transcript JSONL.
// output_tokens are the dominant, reliable cost driver; input/cache are recorded
// too but per Claude Code issue #28197 the streaming input figure is unreliable.
function parseTranscript(file) {
  const totals = {
    turns: 0, output_tokens: 0, input_tokens: 0,
    cache_creation_input_tokens: 0, cache_read_input_tokens: 0,
    web_search_requests: 0, web_fetch_requests: 0,
  };
  let raw;
  try { raw = readFileSync(file, 'utf-8'); } catch { return { error: 'unreadable', file }; }
  for (const line of raw.split('\n')) {
    if (!line.trim()) continue;
    let obj;
    try { obj = JSON.parse(line); } catch { continue; }
    const u = obj?.message?.usage;
    if (!u) continue;
    totals.turns += 1;
    totals.output_tokens += u.output_tokens || 0;
    totals.input_tokens += u.input_tokens || 0;
    totals.cache_creation_input_tokens += u.cache_creation_input_tokens || 0;
    totals.cache_read_input_tokens += u.cache_read_input_tokens || 0;
    const st = u.server_tool_use || {};
    totals.web_search_requests += st.web_search_requests || 0;
    totals.web_fetch_requests += st.web_fetch_requests || 0;
  }
  return { file, totals };
}

async function readStdin() {
  return await new Promise((resolve) => {
    let data = '';
    if (process.stdin.isTTY) return resolve('');
    process.stdin.setEncoding('utf-8');
    const timer = setTimeout(() => resolve(data), 1500); // never block a hook
    process.stdin.on('data', (c) => { data += c; });
    process.stdin.on('end', () => { clearTimeout(timer); resolve(data); });
    process.stdin.on('error', () => { clearTimeout(timer); resolve(data); });
  });
}

function findLatestTranscript() {
  const dir = transcriptDir();
  if (!existsSync(dir)) return null;
  let best = null, bestM = 0;
  for (const f of readdirSync(dir)) {
    if (!f.endsWith('.jsonl') || f.startsWith('agent-')) continue;
    try {
      const m = statSync(join(dir, f)).mtimeMs;
      if (m > bestM) { bestM = m; best = join(dir, f); }
    } catch { /* skip */ }
  }
  return best;
}

async function main() {
  ensureDir(DATA_DIR);

  // Manual mode: parse a given transcript and print JSON.
  const arg = process.argv[2];
  if (arg && arg !== 'hook') {
    console.log(JSON.stringify(parseTranscript(arg), null, 2));
    return;
  }

  // Hook mode: capture the empirical B0 evidence.
  const stdinRaw = await readStdin();
  let stdinParsed = null;
  try { stdinParsed = JSON.parse(stdinRaw); } catch { /* leave raw */ }

  // Any env var that might smuggle usage/cost figures.
  const envHits = {};
  for (const [k, v] of Object.entries(process.env)) {
    if (/token|cost|usage|price|billing/i.test(k)) envHits[k] = v;
  }

  // Derive transcript: prefer a path in the payload, else session_id, else newest.
  let transcript = stdinParsed?.transcript_path || null;
  if (!transcript && stdinParsed?.session_id) {
    const cand = join(transcriptDir(), `${stdinParsed.session_id}.jsonl`);
    if (existsSync(cand)) transcript = cand;
  }
  if (!transcript) transcript = findLatestTranscript();

  const report = {
    probed_at_iso_note: 'timestamp omitted (hook clock not stamped here); mtime of PROBE_OUT is the record',
    stdin_present: stdinRaw.length > 0,
    stdin_raw: stdinRaw.slice(0, 4000),
    stdin_parsed_keys: stdinParsed ? Object.keys(stdinParsed) : null,
    stdin_has_token_or_cost:
      stdinParsed ? Object.keys(stdinParsed).some(k => /token|cost|usage/i.test(k)) : false,
    env_token_cost_vars: envHits,
    transcript_used: transcript,
    transcript_parse: transcript ? parseTranscript(transcript) : { error: 'no transcript found' },
  };

  try { writeFileSync(PROBE_OUT, JSON.stringify(report, null, 2), 'utf-8'); } catch { /* noop */ }
  // Also echo to the hook transcript so it's visible if watched live.
  try { console.log(`[cost-probe] wrote ${PROBE_OUT} (stdin keys: ${report.stdin_parsed_keys})`); } catch { /* noop */ }
}

main().catch(() => {}).finally(() => process.exit(0));
