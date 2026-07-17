#!/usr/bin/env python3
"""
Cost dashboard + backfill-estimator for the AI_Swarm_Productivity scorecard corpus.

Part B2 (dashboard) + Part A (backfill calibration) of cost_instrumentation_spec_2026-07-16.

Stdlib only (no PyYAML): scorecards span three schema versions with inline `#` comments,
so fields are pulled by targeted regex rather than a YAML parse. That is deliberately
tolerant -- a missing field degrades to a fallback, never a crash.

Primary unit = subagent OUTPUT tokens (the ledger's unit, the dominant cost driver).
Model: est_subagent_tokens = agents_spawned * PER_AGENT_MEDIAN, calibrated on the
known-token scorecards. Sessions with 0 agents contribute ~0 SUBAGENT tokens (their
main-loop tokens are real but are NOT in this unit and are not recoverable from the
scorecards -- stated honestly, not hidden).

Usage:
    python cost_dashboard.py calibrate   # print calibration table + aggregate estimate
    python cost_dashboard.py dashboard   # write cost_dashboard_<latest-date>.md
    python cost_dashboard.py             # both
"""
import os
import re
import sys
import glob
import json
import datetime
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
SCORECARD_DIR = os.path.join(HERE, "data", "scorecards")
LEDGER = os.path.join(HERE, "data", "research_token_ledger.md")

# --- Notional dollar model (for projection only; actual marginal $ ~= 0 on sub/toll-free) ---
# Authoritative Claude output rates per 1M tokens: Opus 4.x $25, Sonnet 4.6 $15, Fable 5 $50.
# Blended ~40/40/20 Opus/Sonnet/Fable OUTPUT. (Corrected 2026-07-16: prior model used $13/M,
# which understated Opus output at $15 instead of $25.)
NOTIONAL_USD_PER_MTOK_OUT = 0.40 * 25 + 0.40 * 15 + 0.20 * 50  # = 26.0 $/M output tokens
NOTIONAL_USD_PER_MTOK_IN = 0.40 * 5 + 0.40 * 3 + 0.20 * 10      # = 5.2 $/M input tokens (blended)
# Cache multipliers on the input rate: write (5-min) 1.25x, read 0.1x.
USD_CW = NOTIONAL_USD_PER_MTOK_IN * 1.25   # cache-write $/M
USD_CR = NOTIONAL_USD_PER_MTOK_IN * 0.10   # cache-read  $/M

# Fable-derivation share of tokens (only these become a pay-per-use toll after the Jul-19 cliff).
FABLE_TOLL_SHARE = 0.175  # midpoint of the spec's 15-20%

# --- Transcript recovery (real four-component API usage; machine-local, ~Jun22-Jul16 only) ---
import glob as _glob
from os.path import expanduser as _exp
TRANSCRIPT_DIR = os.path.join(
    _exp("~"), ".claude", "projects",
    "C--Users-pfwac-OneDrive---University-of-Arizona-Documents-03-Projects-00-Hive-Empire-01-Hives-01-PostWach")
_TS_RE = re.compile(r'"timestamp"\s*:\s*"(\d{4}-\d{2}-\d{2})')


def _iso_week_of(datestr):
    return iso_week(datestr)


def parse_transcript_usage(path):
    """Sum the four API-metered components from a transcript JSONL; date = first line timestamp."""
    tot = {"input": 0, "cache_write": 0, "cache_read": 0, "output": 0, "turns": 0, "date": None}
    try:
        raw = open(path, encoding="utf-8", errors="replace").read()
    except OSError:
        return None
    m = _TS_RE.search(raw)
    tot["date"] = m.group(1) if m else None
    for line in raw.split("\n"):
        if '"usage"' not in line:
            continue
        try:
            o = json.loads(line)
        except ValueError:
            continue
        u = (o.get("message") or {}).get("usage")
        if not u:
            continue
        tot["turns"] += 1
        tot["input"] += u.get("input_tokens", 0)
        tot["cache_write"] += u.get("cache_creation_input_tokens", 0)
        tot["cache_read"] += u.get("cache_read_input_tokens", 0)
        tot["output"] += u.get("output_tokens", 0)
    return tot


def recover_components():
    """Parse surviving main + subagent transcripts into per-week four-component totals."""
    if not os.path.isdir(TRANSCRIPT_DIR):
        return None
    main_files = [f for f in _glob.glob(os.path.join(TRANSCRIPT_DIR, "*.jsonl"))
                  if not os.path.basename(f).startswith("agent-")]
    sub_files = _glob.glob(os.path.join(TRANSCRIPT_DIR, "**", "agent-*.jsonl"), recursive=True)
    out = {"main": {}, "subagent": {}}
    for label, files in (("main", main_files), ("subagent", sub_files)):
        weeks = defaultdict(lambda: {"input": 0, "cache_write": 0, "cache_read": 0,
                                     "output": 0, "files": 0, "turns": 0})
        tot = {"input": 0, "cache_write": 0, "cache_read": 0, "output": 0, "files": 0, "turns": 0}
        for f in files:
            u = parse_transcript_usage(f)
            if not u:
                continue
            wk = _iso_week_of(u["date"])
            for k in ("input", "cache_write", "cache_read", "output", "turns"):
                weeks[wk][k] += u[k]; tot[k] += u[k]
            weeks[wk]["files"] += 1; tot["files"] += 1
        out[label] = {"weeks": dict(weeks), "total": tot}
    return out


def component_cost(t):
    return (t["input"] * NOTIONAL_USD_PER_MTOK_IN
            + t["cache_write"] * USD_CW
            + t["cache_read"] * USD_CR
            + t["output"] * NOTIONAL_USD_PER_MTOK_OUT) / 1_000_000

FIELD_RE = {
    "id":     re.compile(r"^\s*id:\s*([0-9A-Za-z_.-]+)", re.M),
    "date":   re.compile(r"^\s*date:\s*([0-9]{4}-[0-9]{2}-[0-9]{2})", re.M),
    "hive":   re.compile(r"^\s*hive:\s*([A-Za-z0-9_-]+)", re.M),
    "schema": re.compile(r'schema_version:\s*"?([0-9.]+)"?', re.M),
    "agents": re.compile(r"^\s*agents_spawned:\s*([0-9]+)", re.M),
    "tokens": re.compile(r"^\s*tokens_output:\s*([0-9]+)", re.M),
    "lines":  re.compile(r"^\s*total_lines_written:\s*([0-9]+)", re.M),
    "pages":  re.compile(r"^\s*pages_produced:\s*([0-9]+)", re.M),
}
SUMMARY_RE = re.compile(r"task_summary:\s*>?\s*\n?((?:.|\n)*?)(?=\n\s*#|\n\s*\n|\noutput:)", re.M)

FNAME_RE = re.compile(r"(?P<date>\d{4}-\d{2}-\d{2})-(?P<hive>[A-Za-z-]+?)-(?P<seq>\d+)\.yaml$")

TYPE_KEYWORDS = [
    ("derivation/Fable", ("fable", "derivation", "derive", "witness", "morphism", "rbw", "candidate")),
    ("review/refverify", ("refverify", "reference", "citation", "review", "audit", "red/blue", "adjudicat")),
    ("governance",       ("governance", "registr", "rule", "policy", "r020", "r019", "scorecard", "compliance")),
    ("paper/manuscript", ("paper", "manuscript", "section", "draft", "figure", "slr", "abstract", "typeset")),
    ("ops/tooling",      ("hook", "tooling", "script", "config", "repo", "ledger", "dashboard", "skill", "cleanup", "instrument")),
]


def infer_type(summary, fname):
    text = ((summary or "") + " " + fname).lower()
    for label, kws in TYPE_KEYWORDS:
        if any(k in text for k in kws):
            return label
    return "ops/tooling"


def first(regex, text, default=None, cast=str):
    m = regex.search(text)
    if not m:
        return default
    try:
        return cast(m.group(1))
    except (ValueError, IndexError):
        return default


def load_classifications():
    """Optional: agent-derived per-file type labels from the Part-A classifier sweep.
    Prefer these over the heuristic when present. Returns {file: {type, size_proxy, confidence}}."""
    import json
    path = os.path.join(HERE, "data", "scorecard_classifications_2026-07-16.json")
    if not os.path.exists(path):
        return {}
    try:
        with open(path, encoding="utf-8") as fh:
            data = json.load(fh)
    except (ValueError, OSError):
        return {}
    rows = data.get("classifications", data) if isinstance(data, dict) else data
    return {r["file"]: r for r in rows if isinstance(r, dict) and "file" in r}


def load_cards():
    classified = load_classifications()
    cards = []
    for path in sorted(glob.glob(os.path.join(SCORECARD_DIR, "*.yaml"))):
        fname = os.path.basename(path)
        with open(path, encoding="utf-8", errors="replace") as fh:
            text = fh.read()
        fm = FNAME_RE.search(fname)
        date = first(FIELD_RE["date"], text) or (fm.group("date") if fm else None)
        hive = first(FIELD_RE["hive"], text) or (fm.group("hive") if fm else "unknown")
        agents = first(FIELD_RE["agents"], text, 0, int)
        tokens = first(FIELD_RE["tokens"], text, None, int)
        summary = first(SUMMARY_RE, text, "")
        cards.append({
            "file": fname,
            "id": first(FIELD_RE["id"], text) or fname.replace(".yaml", ""),
            "date": date,
            "hive": (hive or "unknown").lower().replace("gi-joe", "gijoe"),
            "schema": first(FIELD_RE["schema"], text, "1.0"),
            "agents": agents,
            "tokens_measured": tokens,          # None if not recorded
            "lines": first(FIELD_RE["lines"], text, None, int),
            "pages": first(FIELD_RE["pages"], text, None, int),
            "type": (classified.get(fname, {}).get("type") or infer_type(summary, fname)),
            "type_source": ("agent-classifier" if fname in classified else "heuristic"),
        })
    return cards


def calibrate(cards):
    """Per-agent output-token multiplier from clean multi-agent measured points."""
    pts = []
    for c in cards:
        if c["tokens_measured"] and c["agents"] and c["agents"] >= 2:
            pts.append((c["agents"], c["tokens_measured"], c["tokens_measured"] / c["agents"]))
    per_agent = sorted(p[2] for p in pts)
    n = len(per_agent)
    median = per_agent[n // 2] if n % 2 else (per_agent[n // 2 - 1] + per_agent[n // 2]) / 2
    q1 = per_agent[max(0, int(n * 0.25))]
    q3 = per_agent[min(n - 1, int(n * 0.75))]
    return {"points": pts, "n": n, "median": median, "q1": q1, "q3": q3, "raw": per_agent}


def estimate(cards, cal):
    med, q1, q3 = cal["median"], cal["q1"], cal["q3"]
    for c in cards:
        if c["tokens_measured"] is not None:
            c["est_tokens"] = c["tokens_measured"]
            c["lo"] = c["hi"] = c["tokens_measured"]
            c["basis"] = "measured"
        elif c["agents"] and c["agents"] > 0:
            c["est_tokens"] = round(c["agents"] * med)
            c["lo"] = round(c["agents"] * q1)
            c["hi"] = round(c["agents"] * q3)
            c["basis"] = "estimated:agents"
        else:
            # 0 agents => ~0 SUBAGENT tokens (main-loop tokens are real but out-of-unit).
            c["est_tokens"] = 0
            c["lo"] = c["hi"] = 0
            c["basis"] = "estimated:zero-agent(main-loop only, out-of-unit)"
    return cards


def iso_week(date):
    if not date:
        return "unknown"
    try:
        y, m, d = (int(x) for x in date.split("-"))
        iso = datetime.date(y, m, d).isocalendar()
        return f"{iso[0]}-W{iso[1]:02d}"
    except ValueError:
        return "unknown"


def aggregate(cards):
    # per key: [tokens, cards, agents, lo, hi, n_measured]
    agg = {"hive": defaultdict(lambda: [0, 0, 0, 0, 0, 0]),
           "week": defaultdict(lambda: [0, 0, 0, 0, 0, 0]),
           "type": defaultdict(lambda: [0, 0, 0, 0, 0, 0])}
    tot_tok = tot_lo = tot_hi = tot_meas = tot_agents = 0
    n_meas = 0
    for c in cards:
        tot_tok += c["est_tokens"]; tot_lo += c["lo"]; tot_hi += c["hi"]; tot_agents += c["agents"]
        is_meas = 1 if c["basis"] == "measured" else 0
        if is_meas:
            tot_meas += c["tokens_measured"]; n_meas += 1
        for k, key in (("hive", c["hive"]), ("week", iso_week(c["date"])), ("type", c["type"])):
            row = agg[k][key]
            row[0] += c["est_tokens"]; row[1] += 1; row[2] += c["agents"]
            row[3] += c["lo"]; row[4] += c["hi"]; row[5] += is_meas
    return agg, dict(tot_tok=tot_tok, tot_lo=tot_lo, tot_hi=tot_hi, tot_meas=tot_meas,
                     n_meas=n_meas, tot_agents=tot_agents, n=len(cards))


def row_flag(n_meas, n_cards):
    """measured / estimated / mixed label for a rollup row."""
    if n_meas == 0:
        return "estimated"
    if n_meas == n_cards:
        return "measured"
    return f"mixed ({n_meas}m/{n_cards - n_meas}e)"


def usd(tokens):
    return tokens / 1_000_000 * NOTIONAL_USD_PER_MTOK_OUT


def fmt_m(t):
    return f"{t/1_000_000:.2f}M"


def render_dashboard(cards, cal, agg, tot):
    latest = max((c["date"] for c in cards if c["date"]), default="unknown")
    lines = []
    P = lines.append
    P(f"# Cost Dashboard — AI_Swarm_Productivity ({tot['n']} scorecards, as of {latest})")
    P("")
    P("**Unit:** `subagent_tokens` — the harness-reported per-agent figure the scorecards recorded. NOTE")
    P("(2026-07-16): this is NOT verified to equal API output tokens. In the one case checkable against a")
    P("surviving subagent transcript, the annotation (52,241) was ~16x the transcript output (3,269); the")
    P("ratio is not constant (search-heavy agents inflate it). Treat as a harness cost-proxy, not output.")
    P("Dollars are a NOTIONAL projection")
    P(f"at ~${NOTIONAL_USD_PER_MTOK_OUT:.1f}/M output tokens (blended 40/40/20 Opus/Sonnet/Fable); actual")
    P("marginal $ ~= 0 on subscription + toll-free-Fable + external Codex. **R016: (a) MODELED ESTIMATE.**")
    P("")
    P(f"Auto-generated by `cost_dashboard.py`. Calibration: {cal['n']} clean multi-agent measured points, "
      f"median **{cal['median']/1000:.0f}k** output tokens/agent (IQR {cal['q1']/1000:.0f}k-{cal['q3']/1000:.0f}k).")
    P("")
    P("## Cumulative")
    P(f"- **subagent_output_tokens (est):** {fmt_m(tot['tot_tok'])}  (band {fmt_m(tot['tot_lo'])}–{fmt_m(tot['tot_hi'])})")
    P(f"- of which **measured** (14 cards): {fmt_m(tot['tot_meas'])}; **modeled** (rest): {fmt_m(tot['tot_tok']-tot['tot_meas'])}")
    P(f"- **total agents spawned (corpus):** {tot['tot_agents']}")
    P(f"- **notional $ (if API-billed):** ${usd(tot['tot_tok']):,.0f}  (band ${usd(tot['tot_lo']):,.0f}–${usd(tot['tot_hi']):,.0f})")
    P(f"- **actual marginal $:** ~0  (subscription + toll-free-Fable pre-Jul-19 + Codex external)")
    P(f"- **post-Jul-19 Fable toll exposure:** ~{fmt_m(tot['tot_tok']*FABLE_TOLL_SHARE)} tokens "
      f"(~{FABLE_TOLL_SHARE*100:.0f}% Fable-derivation share) => ~${usd(tot['tot_tok']*FABLE_TOLL_SHARE):,.0f} notional")
    P("")
    P("*All per-row token figures are MODELED ESTIMATES with a ±band (from the per-agent IQR),")
    P("except rows flagged `measured`. `mixed` = some cards measured, some estimated.*")
    P("")
    for dim, title in (("hive", "Per hive"), ("type", "Per session type"), ("week", "Per week")):
        P(f"## {title}")
        P("| " + dim + " | est tokens | band | flag | cards | agents |")
        P("|---|---|---|---|---|---|")
        rows = sorted(agg[dim].items(), key=lambda kv: kv[1][0], reverse=True)
        for k, (tok, n, ag, lo, hi, nm) in rows:
            band = "—" if lo == hi else f"{fmt_m(lo)}–{fmt_m(hi)}"
            P(f"| {k} | {fmt_m(tok)} | {band} | {row_flag(nm, n)} | {n} | {ag} |")
        P("")
    P("## Fidelity / caveats (R016 (a))")
    P("- All 14 calibration points are RECENT heavy sessions (Jun 23–Jul 16). Early/lighter sessions are")
    P("  extrapolated by agent-count; expect the aggregate accurate to **±30–50%**, worse for Feb–May rows.")
    P("- 0-agent sessions (main-loop-only) contribute ~0 in THIS unit; their real main-loop tokens are not")
    P("  in the scorecards and are not recovered here. The cumulative is a SUBAGENT-token floor for those.")
    P("- Ephemeral raw usage is gone for ~240 of 257; this is an ESTIMATE, not recovery.")
    return "\n".join(lines) + "\n", latest


def render_backfill_report(cards, cal, agg, tot):
    latest = max((c["date"] for c in cards if c["date"]), default="unknown")
    n_agent = sum(1 for c in cards if c.get("type_source") == "agent-classifier")
    L = []
    P = L.append
    P(f"# Cost Backfill Report — AI_Swarm_Productivity ({tot['n']} scorecards)")
    P(f"*Generated {latest} by `cost_dashboard.py report`. Companion to `fable_cost_ledger.md`.*")
    P("")
    P("**R016: (a) MODELED ESTIMATE — not recovery.** Raw per-session usage (task-notification")
    P("`usage` blocks, `/cost`) is ephemeral and gone for ~240 of 258 sessions. This report models")
    P("subagent output tokens from the fields the scorecards DO carry, calibrated on the 14 that")
    P("recorded tokens. Treat the aggregate as an order-of-magnitude (±30–50%), not accounting-grade.")
    P("")
    P("## Method")
    P("1. **Unit:** `subagent_tokens` — the harness figure the scorecards recorded. NOT verified = API")
    P("   output tokens (one checkable case: annotation 52,241 vs transcript output 3,269, ~16x; ratio")
    P("   varies by agent type). A harness cost-proxy. The `$` applies an output rate to it as an estimate.")
    P("2. **Calibrate:** on scorecards recording both `tokens_output` and `agents_spawned>=2`,")
    P(f"   compute output-tokens-per-agent. n={cal['n']} clean points; per-agent (k tokens): "
      f"{[round(x/1000) for x in cal['raw']]}.")
    P(f"   → median **{cal['median']/1000:.0f}k**/agent, IQR [{cal['q1']/1000:.0f}k, {cal['q3']/1000:.0f}k].")
    P("3. **Classify:** all 258 sessions typed by a 10-agent classifier sweep reading each scorecard +")
    P(f"   matching archive ({n_agent}/{tot['n']} agent-labeled). Types: derivation/Fable, paper/manuscript,")
    P("   governance, ops/tooling, review/refverify.")
    P("4. **Apply:** measured where recorded; else `agents × median` with band `agents × [Q1,Q3]`;")
    P("   0-agent sessions → ~0 subagent tokens (main-loop-only; out of this unit).")
    P("")
    P("## Aggregate")
    P(f"- **cumulative subagent-output tokens (est):** {fmt_m(tot['tot_tok'])}  "
      f"(band {fmt_m(tot['tot_lo'])}–{fmt_m(tot['tot_hi'])})")
    P(f"- measured (14 cards): {fmt_m(tot['tot_meas'])}; modeled ({tot['n']-tot['n_meas']} cards): "
      f"{fmt_m(tot['tot_tok']-tot['tot_meas'])}")
    P(f"- total agents spawned: {tot['tot_agents']}")
    P(f"- **notional $ (API-rate, ${NOTIONAL_USD_PER_MTOK_OUT:.0f}/M out):** ${usd(tot['tot_tok']):,.0f} "
      f"(band ${usd(tot['tot_lo']):,.0f}–${usd(tot['tot_hi']):,.0f}); **actual marginal $ ≈ 0**.")
    P("")
    P("*Every token figure below is a MODELED ESTIMATE carrying a ±band (per-agent IQR), except rows")
    P("flagged `measured`; `mixed (Nm/Ne)` = N measured / N estimated cards in that row.*")
    P("")
    for dim, title in (("hive", "By hive"), ("type", "By session type"), ("week", "By week")):
        P(f"### {title}")
        P("| " + dim + " | est tokens | band | flag | cards | agents |")
        P("|---|---|---|---|---|---|")
        for k, (t, n, a, lo, hi, nm) in sorted(agg[dim].items(), key=lambda kv: kv[1][0], reverse=True):
            band = "—" if lo == hi else f"{fmt_m(lo)}–{fmt_m(hi)}"
            P(f"| {k} | {fmt_m(t)} | {band} | {row_flag(nm, n)} | {n} | {a} |")
        P("")
    P("## Fidelity / honest caveats")
    P("- All 14 calibration points are RECENT heavy sessions (Jun 23–Jul 16); early/lighter sessions")
    P("  (Feb–May) are extrapolated by agent-count and are the weakest rows. Aggregate ±30–50%.")
    P("- The per-agent median (80k) hides real variance (26k–131k). Small-N sessions dominated by one")
    P("  large agent, or many light agents, are individually unreliable; the AGGREGATE is the deliverable.")
    P("- 0-agent (main-loop-only) sessions contribute ~0 here. Their real main-loop tokens exist but are")
    P("  not in the scorecards; the cumulative is a SUBAGENT-token FLOOR for those sessions.")
    P("- Dollars are notional (subscription + toll-free-Fable + external Codex ⇒ ~0 actual marginal).")
    P("")
    P("## Per-session appendix")
    P("| id | date | hive | type | agents | basis | est tokens | band |")
    P("|---|---|---|---|---|---|---|---|")
    for c in sorted(cards, key=lambda c: (c["date"] or "", c["id"])):
        basis = {"measured": "M", "estimated:agents": "E",
                 "estimated:zero-agent(main-loop only, out-of-unit)": "0"}.get(c["basis"], "E")
        band = "—" if c["lo"] == c["hi"] else f"{fmt_m(c['lo'])}–{fmt_m(c['hi'])}"
        P(f"| {c['id']} | {c['date']} | {c['hive']} | {c['type']} | {c['agents']} | {basis} | "
          f"{fmt_m(c['est_tokens'])} | {band} |")
    P("")
    P("*basis: M=measured, E=estimated (agents×median), 0=zero-agent (main-loop only).*")
    return "\n".join(L) + "\n", latest


def render_recovery(rec, latest):
    L = []
    P = L.append
    P(f"# Cost Recovery — real four-component API usage (transcripts), as of {latest}")
    P("")
    P("**R016: (b) RECOVERED / MEASURED**, not modeled — parsed directly from the surviving session and")
    P("subagent transcript JSONL (`~/.claude/projects/<slug>/`), which carry the four components the API")
    P("meters: `input` (fresh), `cache_write` (1.25× in), `cache_read` (0.1× in), `output` (full out).")
    P("This is the ACCURATE cost basis — distinct from the legacy `subagent_tokens` proxy backfill, which")
    P("is a harness figure ~16× transcript output in the one checkable case (see the backfill report).")
    P("")
    P("**Coverage caveat.** Transcripts survive only for **~2026-06-22 → 07-16** (main back to ~06-19).")
    P("Feb–mid-June has NO transcripts — not recoverable. Not every subagent transcript persists")
    P("(background / worktree-cleaned agents leave none), so subagent totals are a FLOOR. Dates are the")
    P("first in-transcript timestamp; dollars are NOTIONAL (blended rates; actual marginal ~0 on subscription).")
    P("")
    grand = {"input": 0, "cache_write": 0, "cache_read": 0, "output": 0}
    for label in ("main", "subagent"):
        t = rec[label]["total"]
        for k in grand:
            grand[k] += t[k]
    P("## Totals (real API tokens)")
    P("| stream | files | input | cache_write | cache_read | output | notional $ |")
    P("|---|---|---|---|---|---|---|")
    for label in ("main", "subagent"):
        t = rec[label]["total"]
        P(f"| {label} | {t['files']} | {fmt_m(t['input'])} | {fmt_m(t['cache_write'])} | "
          f"{fmt_m(t['cache_read'])} | {fmt_m(t['output'])} | ${component_cost(t):,.0f} |")
    gc = component_cost(grand)
    P(f"| **combined** | — | {fmt_m(grand['input'])} | {fmt_m(grand['cache_write'])} | "
      f"{fmt_m(grand['cache_read'])} | {fmt_m(grand['output'])} | **${gc:,.0f}** |")
    P("")
    P("## Cost by component (combined) — where the dollars actually are")
    P("| component | tokens | rate $/M | notional $ | % of $ |")
    P("|---|---|---|---|---|")
    comps = [("input", grand["input"], NOTIONAL_USD_PER_MTOK_IN),
             ("cache_write", grand["cache_write"], USD_CW),
             ("cache_read", grand["cache_read"], USD_CR),
             ("output", grand["output"], NOTIONAL_USD_PER_MTOK_OUT)]
    for name, tok, rate in comps:
        c = tok / 1_000_000 * rate
        P(f"| {name} | {fmt_m(tok)} | ${rate:.2f} | ${c:,.0f} | {(c/gc*100 if gc else 0):.0f}% |")
    P("")
    P("*Note the split: `cache_read` is the volume giant but cheap; `output` is small volume but the")
    P("cost driver. The output-only proxy saw neither the true volume nor the cache cost.*")
    P("")
    for label in ("main", "subagent"):
        P(f"## Per week — {label}")
        P("| week | files | input | cache_write | cache_read | output | notional $ |")
        P("|---|---|---|---|---|---|---|")
        wk = rec[label]["weeks"]
        for k in sorted(wk, key=lambda w: wk[w]["output"], reverse=True):
            t = wk[k]
            P(f"| {k} | {t['files']} | {fmt_m(t['input'])} | {fmt_m(t['cache_write'])} | "
              f"{fmt_m(t['cache_read'])} | {fmt_m(t['output'])} | ${component_cost(t):,.0f} |")
        P("")
    return "\n".join(L) + "\n"


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "both"

    if mode == "recovery":
        rec = recover_components()
        if not rec:
            print("No transcript dir found — recovery unavailable on this machine.")
            return
        latest = "2026-07-16"
        md = render_recovery(rec, latest)
        out = os.path.join(HERE, "data", f"cost_recovery_report_{latest}.md")
        with open(out, "w", encoding="utf-8") as fh:
            fh.write(md)
        g = {k: rec["main"]["total"][k] + rec["subagent"]["total"][k]
             for k in ("input", "cache_write", "cache_read", "output")}
        print(f"Recovered (real API tokens): output {fmt_m(g['output'])}, cache_read {fmt_m(g['cache_read'])}, "
              f"notional ${component_cost(g):,.0f}")
        print(f"Wrote {out}")
        return

    cards = load_cards()
    cal = calibrate(cards)
    cards = estimate(cards, cal)
    agg, tot = aggregate(cards)

    if mode in ("calibrate", "both"):
        print(f"Calibration: {cal['n']} clean multi-agent measured points")
        print(f"  per-agent output tokens: median {cal['median']/1000:.1f}k  "
              f"IQR [{cal['q1']/1000:.1f}k, {cal['q3']/1000:.1f}k]")
        print(f"  raw per-agent (k): {[round(x/1000) for x in cal['raw']]}")
        print(f"Corpus: {tot['n']} cards, {tot['tot_agents']} agents total, {tot['n_meas']} measured")
        print(f"Cumulative subagent-output tokens (est): {fmt_m(tot['tot_tok'])} "
              f"[{fmt_m(tot['tot_lo'])}, {fmt_m(tot['tot_hi'])}]")
        print(f"  measured portion: {fmt_m(tot['tot_meas'])}; modeled: {fmt_m(tot['tot_tok']-tot['tot_meas'])}")
        print(f"Notional $ (API-rate): ${usd(tot['tot_tok']):,.0f} "
              f"[{usd(tot['tot_lo']):,.0f}, {usd(tot['tot_hi']):,.0f}]")

    if mode in ("dashboard", "both"):
        md, latest = render_dashboard(cards, cal, agg, tot)
        out = os.path.join(HERE, "data", f"cost_dashboard_{latest}.md")
        with open(out, "w", encoding="utf-8") as fh:
            fh.write(md)
        print(f"\nWrote {out}")

    if mode in ("report", "both"):
        md, latest = render_backfill_report(cards, cal, agg, tot)
        out = os.path.join(HERE, "data", f"cost_backfill_report_{latest}.md")
        with open(out, "w", encoding="utf-8") as fh:
            fh.write(md)
        print(f"Wrote {out}")

    return cards, cal, agg, tot


if __name__ == "__main__":
    main()
