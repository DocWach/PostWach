#!/usr/bin/env node
/**
 * Cost Capture (B1) — SessionEnd auto-capture of token usage into the research ledger.
 *
 * B0 CONFIRMED (2026-07-16): the SessionEnd hook stdin carries `transcript_path` directly
 * (docs were wrong; it's not Stop-only). We parse that transcript, sum the FOUR token
 * components the API meters separately (input / cache-write / cache-read / output), scan for
 * subagent `<usage>` annotations, compute a notional cost, and APPEND a per-session snapshot
 * row to research_token_ledger.md. Prints a visible one-line confirmation (was invisible as a
 * probe — the principal ran it and "saw nothing pop up"; this fixes that).
 *
 * Idempotent: a session already in the ledger is not appended twice.
 * Never throws; always exits 0 (a hook must not crash Claude Code).
 *
 * Modes:
 *   node cost-capture.mjs           # hook mode: read stdin, capture, append, print
 *   node cost-capture.mjs <file>    # manual: parse a transcript, print JSON (no append)
 */
import { existsSync, mkdirSync, readFileSync, writeFileSync, appendFileSync, readdirSync, statSync } from 'fs';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';
import { homedir } from 'os';

const __dirname = dirname(fileURLToPath(import.meta.url));
const PROJECT_ROOT = join(__dirname, '..', '..');
const DATA_DIR = join(PROJECT_ROOT, '.claude-flow', 'data');
const PROBE_OUT = join(DATA_DIR, 'sessionend-probe.json');
const LEDGER = join(PROJECT_ROOT, 'Papers', 'AI_Swarm_Productivity', 'data', 'research_token_ledger.md');
const MARKER = '<!-- AUTOCAPTURE:B1 -->';

// Notional blended $/1M (see research_token_ledger + cost_dashboard.py). Output dominates;
// blended 40/40/20 Opus/Sonnet/Fable. Input blend ~ $5.2/M; cache-write 1.25x, cache-read 0.1x.
const USD = { inPerM: 5.2, outPerM: 26.0 };
const cost = (t) =>
  (t.input * USD.inPerM
    + t.cache_write * USD.inPerM * 1.25
    + t.cache_read * USD.inPerM * 0.1
    + (t.output + t.subagent_output) * USD.outPerM) / 1_000_000;

function transcriptDir() {
  return join(homedir(), '.claude', 'projects',
    'C--Users-pfwac-OneDrive---University-of-Arizona-Documents-03-Projects-00-Hive-Empire-01-Hives-01-PostWach');
}

function parseTranscript(file) {
  const t = { turns: 0, input: 0, cache_write: 0, cache_read: 0, output: 0, subagent_output: 0 };
  let raw;
  try { raw = readFileSync(file, 'utf-8'); } catch { return { error: 'unreadable', file, totals: t }; }
  // Subagent usage is scraped from harness task-notifications / Agent tool-results, which repeat
  // the same figure many times (every Bash `cat` of a result re-injects it). DEDUPE by the unique
  // event id: workflow notifications carry <task-id>, Agent results carry agentId. Skip assistant
  // lines (our authored code/prose). Without this the parser over-counts ~10x (12.7M vs true 1.16M).
  const wf = /<task-id>([a-z0-9]+)<\/task-id>[\s\S]*?<subagent_tokens>\s*(\d+)\s*<\/subagent_tokens>/g;
  const ag = /agentId["\s:]+([a-z0-9]+)[\s\S]{0,4000}?<usage>\s*subagent_tokens:\s*(\d+)/g;
  const wfMap = {}, agMap = {};
  for (const line of raw.split('\n')) {
    if (!line.trim()) continue;
    let o; try { o = JSON.parse(line); } catch { continue; }
    const role = o?.message?.role || o?.type;
    const u = o?.message?.usage;
    if (u) {
      t.turns++;
      t.input += u.input_tokens || 0;
      t.cache_write += u.cache_creation_input_tokens || 0;
      t.cache_read += u.cache_read_input_tokens || 0;
      t.output += u.output_tokens || 0;
    }
    if (role === 'assistant') continue;
    let m;
    wf.lastIndex = 0; while ((m = wf.exec(line)) !== null) wfMap[m[1]] = parseInt(m[2], 10);
    ag.lastIndex = 0; while ((m = ag.exec(line)) !== null) agMap[m[1]] = parseInt(m[2], 10);
  }
  for (const v of Object.values(wfMap)) t.subagent_output += v;
  for (const v of Object.values(agMap)) t.subagent_output += v;
  return { file, totals: t };
}

async function readStdin() {
  return await new Promise((resolve) => {
    if (process.stdin.isTTY) return resolve('');
    let d = ''; process.stdin.setEncoding('utf-8');
    const timer = setTimeout(() => resolve(d), 1500);
    process.stdin.on('data', (c) => (d += c));
    process.stdin.on('end', () => { clearTimeout(timer); resolve(d); });
    process.stdin.on('error', () => { clearTimeout(timer); resolve(d); });
  });
}

function newestTranscript() {
  const dir = transcriptDir(); if (!existsSync(dir)) return null;
  let best = null, bestM = 0;
  for (const f of readdirSync(dir)) {
    if (!f.endsWith('.jsonl') || f.startsWith('agent-')) continue;
    try { const m = statSync(join(dir, f)).mtimeMs; if (m > bestM) { bestM = m; best = join(dir, f); } } catch {}
  }
  return best;
}

const M = (n) => (n / 1_000_000).toFixed(2) + 'M';

async function main() {
  try { if (!existsSync(DATA_DIR)) mkdirSync(DATA_DIR, { recursive: true }); } catch {}

  const arg = process.argv[2];
  if (arg && arg !== 'hook') { console.log(JSON.stringify(parseTranscript(arg), null, 2)); return; }

  const stdinRaw = await readStdin();
  let sp = null; try { sp = JSON.parse(stdinRaw); } catch {}
  const sid = sp?.session_id || 'unknown';
  let transcript = sp?.transcript_path || (sp?.session_id && join(transcriptDir(), `${sp.session_id}.jsonl`));
  if (!transcript || !existsSync(transcript)) transcript = newestTranscript();

  // Keep the B0 probe record too (still useful diagnostics).
  try {
    writeFileSync(PROBE_OUT, JSON.stringify({
      stdin_parsed_keys: sp ? Object.keys(sp) : null,
      stdin_has_token_or_cost: sp ? Object.keys(sp).some(k => /token|cost|usage/i.test(k)) : false,
      transcript_used: transcript,
    }, null, 2), 'utf-8');
  } catch {}

  const parsed = transcript ? parseTranscript(transcript) : { totals: null };
  const t = parsed.totals;
  if (!t) { console.log('[cost-capture] no transcript found; nothing appended'); return; }
  t.subagent_output = t.subagent_output || 0;
  const usd = cost(t);

  // Idempotency: skip if this session already has a row.
  let ledger = '';
  try { ledger = existsSync(LEDGER) ? readFileSync(LEDGER, 'utf-8') : ''; } catch {}
  const shortSid = sid.slice(0, 8);
  if (ledger.includes(`| ${shortSid} `)) {
    console.log(`[cost-capture] session ${shortSid} already in ledger; skipped`);
    return;
  }

  const dateStr = (transcript.match(/(\d{4}-\d{2}-\d{2})/) || [])[1] || ''; // best-effort; usually empty
  const row = `| ${shortSid} | ${dateStr || 'session-end'} | ${t.input} | ${t.cache_write} | `
    + `${t.cache_read} | ${t.output} | ${t.subagent_output} | $${usd.toFixed(2)} |`;

  try {
    if (!ledger.includes(MARKER)) {
      const header = `\n\n## Auto-captured sessions (B1, going-forward) ${MARKER}\n`
        + `All four API-metered token components + subagent output, per session, parsed from the\n`
        + `session transcript at SessionEnd. \`$\` is NOTIONAL (blended rates; actual marginal ~0 on\n`
        + `subscription). input=fresh uncached, cache_write=1.25x in, cache_read=0.1x in, output=full out.\n\n`
        + `| session | date | input | cache_write | cache_read | output | subagent_out | notional $ |\n`
        + `|---|---|---|---|---|---|---|---|\n`;
      appendFileSync(LEDGER, header + row + '\n', 'utf-8');
    } else {
      appendFileSync(LEDGER, row + '\n', 'utf-8');
    }
  } catch (e) {
    console.log(`[cost-capture] append failed (non-critical): ${e.message}`);
    return;
  }

  console.log(`[cost-capture] session ${shortSid}: out ${M(t.output)} + subagent ${M(t.subagent_output)}, `
    + `cache_read ${M(t.cache_read)}, ~$${usd.toFixed(2)} notional -> appended to research_token_ledger.md`);
}

main().catch(() => {}).finally(() => process.exit(0));
