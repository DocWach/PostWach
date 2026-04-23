/**
 * Minimal MCP stdio JSON-RPC client for claude-flow.
 *
 * Spawns `claude-flow mcp start`, performs the initialize handshake, and
 * exposes `call(toolName, args)` for one-shot tool invocations from hooks.
 *
 * Used by SessionStart/SessionEnd helpers to reach the MCP surface without
 * requiring the `@claude-flow/memory` package (which is not shipped in
 * claude-flow v3.5.80). This isolates hooks from upstream package churn.
 */

import { spawn } from 'child_process';

export class McpClient {
  constructor(options = {}) {
    this.cmd = options.cmd || 'claude-flow';
    this.args = options.args || ['mcp', 'start'];
    this.nextId = 1;
    this.pending = new Map();
    this.buffer = '';
    this.proc = null;
    this.initialized = false;
  }

  async start({ timeoutMs = 10000 } = {}) {
    return new Promise((resolve, reject) => {
      const timer = setTimeout(
        () => reject(new Error(`MCP init timeout after ${timeoutMs}ms`)),
        timeoutMs,
      );
      try {
        // Windows: claude-flow is a .cmd shim; invoke via cmd.exe /c to avoid
        // Node's DEP0190 warning about shell:true with argv arrays.
        const isWin = process.platform === 'win32';
        const spawnCmd = isWin ? 'cmd.exe' : this.cmd;
        const spawnArgs = isWin ? ['/c', this.cmd, ...this.args] : this.args;
        this.proc = spawn(spawnCmd, spawnArgs, { stdio: ['pipe', 'pipe', 'pipe'] });
      } catch (e) {
        clearTimeout(timer);
        return reject(e);
      }

      this.proc.on('error', (err) => {
        clearTimeout(timer);
        reject(err);
      });
      this.proc.stdout.on('data', (chunk) => this._onData(chunk));
      this.proc.stderr.on('data', () => { /* silence server banners */ });

      const initId = this.nextId++;
      this.pending.set(initId, {
        resolve: (res) => {
          clearTimeout(timer);
          this._send({ jsonrpc: '2.0', method: 'notifications/initialized' });
          this.initialized = true;
          resolve(res);
        },
        reject: (err) => { clearTimeout(timer); reject(err); },
      });
      this._send({
        jsonrpc: '2.0',
        id: initId,
        method: 'initialize',
        params: {
          protocolVersion: '2024-11-05',
          capabilities: {},
          clientInfo: { name: 'cf-session-hook', version: '1.0' },
        },
      });
    });
  }

  _send(obj) {
    if (!this.proc || !this.proc.stdin.writable) return;
    this.proc.stdin.write(JSON.stringify(obj) + '\n');
  }

  _onData(chunk) {
    this.buffer += chunk.toString('utf-8');
    let idx;
    while ((idx = this.buffer.indexOf('\n')) >= 0) {
      const line = this.buffer.slice(0, idx).trim();
      this.buffer = this.buffer.slice(idx + 1);
      if (!line || line[0] !== '{') continue;
      let msg;
      try { msg = JSON.parse(line); } catch { continue; }
      if (msg.id != null && this.pending.has(msg.id)) {
        const p = this.pending.get(msg.id);
        this.pending.delete(msg.id);
        if (msg.error) p.reject(new Error(msg.error.message || `MCP error code ${msg.error.code}`));
        else p.resolve(msg.result);
      }
    }
  }

  async call(name, args = {}, { timeoutMs = 20000 } = {}) {
    if (!this.initialized) throw new Error('MCP client not initialized');
    return new Promise((resolve, reject) => {
      const id = this.nextId++;
      const timer = setTimeout(() => {
        this.pending.delete(id);
        reject(new Error(`MCP call timeout: ${name} after ${timeoutMs}ms`));
      }, timeoutMs);
      this.pending.set(id, {
        resolve: (res) => { clearTimeout(timer); resolve(res); },
        reject: (err) => { clearTimeout(timer); reject(err); },
      });
      this._send({
        jsonrpc: '2.0',
        id,
        method: 'tools/call',
        params: { name, arguments: args },
      });
    });
  }

  async close() {
    try {
      if (this.proc && !this.proc.killed) this.proc.kill();
    } catch { /* ignore */ }
  }
}

// Claude Flow tool results wrap payload JSON inside result.content[0].text.
// Return the parsed payload, or the raw text if it isn't JSON, or null.
export function parseToolResult(result) {
  if (!result || !Array.isArray(result.content)) return null;
  const item = result.content.find((c) => c.type === 'text');
  if (!item) return null;
  try { return JSON.parse(item.text); }
  catch { return item.text; }
}
