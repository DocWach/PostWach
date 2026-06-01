#!/usr/bin/env python3
"""
AI-Swarm Productivity Scorecard Analyzer
=========================================
Reads YAML scorecards from data/scorecards/, computes derived metrics,
and compares against published baselines.

Usage:
    python analyze_scorecards.py            # Print summary tables
    python analyze_scorecards.py --csv      # Also write CSV output
"""

import argparse
import csv
import io
import os
import sys
from datetime import datetime
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML is required. Install with:")
    print("  pip install pyyaml")
    sys.exit(1)

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

SCRIPT_DIR = Path(__file__).resolve().parent
SCORECARDS_DIR = SCRIPT_DIR / "data" / "scorecards"

BASELINES = {
    "academic_pages_per_hour": 0.75,
    "copilot_speedup_factor": 1.55,
    "metr_experienced_factor": 0.81,
    "senior_copilot_factor": 1.10,
}

DERIVED_FIELDS = [
    "wall_clock_hours",
    "pages_per_hour",
    "lines_per_hour",
    "cost_per_page",
    "cost_per_file",
    "agent_utilization",
    "tokens_per_artifact",
    "rework_ratio",
]

# Non-numeric values found in numeric fields (e.g., "~2400", free-text comments).
# Skipped during arithmetic but reported at end so schema discipline is visible.
DATA_QUALITY_ISSUES = []

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def safe_get(data, *keys, default=None):
    """Drill into nested dicts, returning default if any key is missing or None."""
    current = data
    for key in keys:
        if not isinstance(current, dict):
            return default
        current = current.get(key)
        if current is None:
            return default
    return current


def safe_div(numerator, denominator):
    """Divide, returning None if either operand is None or denominator is zero."""
    if numerator is None or denominator is None:
        return None
    if not isinstance(numerator, (int, float)) or isinstance(numerator, bool):
        return None
    if not isinstance(denominator, (int, float)) or isinstance(denominator, bool):
        return None
    if denominator == 0:
        return None
    return numerator / denominator


def as_num(value, source_file=None, field=None, allow_list=False):
    """Coerce value to a number, or return None if not numeric.

    Logs non-numeric inputs to DATA_QUALITY_ISSUES so the analyzer never silently
    swallows malformed scorecard fields. If allow_list, treats lists as len(list)
    (some scorecards put `rework_files: []` instead of `rework_files: 0`).
    """
    if value is None:
        return None
    if isinstance(value, bool):
        return None
    if isinstance(value, (int, float)):
        return value
    if allow_list and isinstance(value, list):
        return len(value)
    if source_file is not None and field is not None:
        DATA_QUALITY_ISSUES.append({
            "file": source_file,
            "field": field,
            "value": repr(value)[:80],
            "type": type(value).__name__,
        })
    return None


def parse_time(t):
    """Parse a time string (HH:MM) or datetime.time into minutes since midnight."""
    if t is None:
        return None
    if hasattr(t, "hour"):
        return t.hour * 60 + t.minute
    t_str = str(t).strip()
    for fmt in ("%H:%M", "%H:%M:%S"):
        try:
            parsed = datetime.strptime(t_str, fmt)
            return parsed.hour * 60 + parsed.minute
        except ValueError:
            continue
    return None


def compute_wall_clock_hours(start, end):
    """Compute hours between start_time and end_time."""
    start_min = parse_time(start)
    end_min = parse_time(end)
    if start_min is None or end_min is None:
        return None
    diff = end_min - start_min
    if diff <= 0:
        diff += 24 * 60  # crossed midnight
    return diff / 60.0


def fmt(value, decimals=2):
    """Format a numeric value for display, returning '-' for None or non-numeric."""
    if not isinstance(value, (int, float)) or isinstance(value, bool):
        return "-"
    return f"{value:.{decimals}f}"


# ---------------------------------------------------------------------------
# Core: compute derived metrics for one scorecard
# ---------------------------------------------------------------------------


def compute_derived(card):
    """Compute all derived metrics for a single scorecard dict. Returns a dict."""
    src = card.get("_source_file", "<unknown>")

    start = safe_get(card, "session", "start_time")
    end = safe_get(card, "session", "end_time")

    wall_clock = compute_wall_clock_hours(start, end)
    # Allow manual override for retroactive scorecards without start/end times
    if wall_clock is None:
        wall_clock = as_num(
            safe_get(card, "session", "wall_clock_hours_override"),
            src, "session.wall_clock_hours_override",
        )
    pages = as_num(safe_get(card, "output", "pages_produced"), src, "output.pages_produced")
    lines = as_num(safe_get(card, "output", "total_lines_written"), src, "output.total_lines_written")
    cost = as_num(safe_get(card, "ai_efficiency", "total_cost_usd"), src, "ai_efficiency.total_cost_usd")
    files_created = as_num(safe_get(card, "output", "total_files_created", default=0), src, "output.total_files_created") or 0
    files_modified = as_num(safe_get(card, "output", "total_files_modified", default=0), src, "output.total_files_modified") or 0
    total_files = files_created + files_modified
    agents = as_num(safe_get(card, "ai_efficiency", "agents_spawned"), src, "ai_efficiency.agents_spawned")
    failures = as_num(safe_get(card, "process", "agent_failures", default=0), src, "process.agent_failures") or 0
    tokens_in = as_num(safe_get(card, "ai_efficiency", "tokens_input"), src, "ai_efficiency.tokens_input")
    tokens_out = as_num(safe_get(card, "ai_efficiency", "tokens_output"), src, "ai_efficiency.tokens_output")
    rework = as_num(
        safe_get(card, "process", "rework_files", default=0),
        src, "process.rework_files", allow_list=True,
    ) or 0

    artifacts = safe_get(card, "output", "artifacts", default=[])
    artifact_count = len(artifacts) if isinstance(artifacts, list) else 0

    total_tokens = None
    if tokens_in is not None and tokens_out is not None:
        total_tokens = tokens_in + tokens_out

    return {
        "wall_clock_hours": wall_clock,
        "pages_per_hour": safe_div(pages, wall_clock),
        "lines_per_hour": safe_div(lines, wall_clock),
        "cost_per_page": safe_div(cost, pages),
        "cost_per_file": safe_div(cost, total_files) if total_files > 0 else None,
        "agent_utilization": safe_div(agents - failures, agents) if agents else None,
        "tokens_per_artifact": safe_div(total_tokens, artifact_count),
        "rework_ratio": safe_div(rework, total_files) if total_files > 0 else None,
    }


# ---------------------------------------------------------------------------
# Load scorecards
# ---------------------------------------------------------------------------


def load_scorecards():
    """Load all YAML scorecards from data/scorecards/, skipping templates and schemas."""
    if not SCORECARDS_DIR.is_dir():
        print(f"ERROR: Scorecards directory not found: {SCORECARDS_DIR}")
        sys.exit(1)

    cards = []
    skipped = []
    errors = []

    for path in sorted(SCORECARDS_DIR.glob("*.yaml")):
        name_lower = path.name.lower()
        if "template" in name_lower or "schema" in name_lower:
            skipped.append(path.name)
            continue
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = yaml.safe_load(f)
            if data is None:
                errors.append((path.name, "empty file"))
                continue
            data["_source_file"] = path.name
            data["_derived"] = compute_derived(data)
            cards.append(data)
        except Exception as e:
            errors.append((path.name, str(e)))

    # Also check .yml extension
    for path in sorted(SCORECARDS_DIR.glob("*.yml")):
        name_lower = path.name.lower()
        if "template" in name_lower or "schema" in name_lower:
            skipped.append(path.name)
            continue
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = yaml.safe_load(f)
            if data is None:
                errors.append((path.name, "empty file"))
                continue
            data["_source_file"] = path.name
            data["_derived"] = compute_derived(data)
            cards.append(data)
        except Exception as e:
            errors.append((path.name, str(e)))

    return cards, skipped, errors


# ---------------------------------------------------------------------------
# Aggregation
# ---------------------------------------------------------------------------


def aggregate_by_hive(cards):
    """Group cards by hive and compute aggregate stats."""
    hives = {}
    for card in cards:
        hive = safe_get(card, "session", "hive", default="unknown")
        hives.setdefault(hive, []).append(card)

    results = {}
    for hive, hive_cards in sorted(hives.items()):
        n = len(hive_cards)
        derived_lists = {field: [] for field in DERIVED_FIELDS}

        for card in hive_cards:
            for field in DERIVED_FIELDS:
                val = card["_derived"].get(field)
                if val is not None:
                    derived_lists[field].append(val)

        means = {}
        for field in DERIVED_FIELDS:
            vals = derived_lists[field]
            means[field] = sum(vals) / len(vals) if vals else None

        total_pages = sum(
            (as_num(safe_get(c, "output", "pages_produced", default=0)) or 0)
            for c in hive_cards
        )
        total_hours = sum(
            c["_derived"].get("wall_clock_hours", 0) or 0 for c in hive_cards
        )

        results[hive] = {
            "sessions": n,
            "total_pages": total_pages,
            "total_hours": total_hours,
            "means": means,
        }

    return results


# ---------------------------------------------------------------------------
# Display
# ---------------------------------------------------------------------------


def print_header(title):
    width = 78
    print()
    print("=" * width)
    print(f"  {title}")
    print("=" * width)


def print_session_table(cards):
    """Print per-session summary table."""
    print_header("PER-SESSION SUMMARY")

    if not cards:
        print("  (no scorecards found)")
        return

    # Column widths
    col_id = 30
    col_num = 10

    header = (
        f"{'Session ID':<{col_id}} "
        f"{'Hive':<12} "
        f"{'Hours':>{col_num}} "
        f"{'Pages':>{col_num}} "
        f"{'Pg/Hr':>{col_num}} "
        f"{'Ln/Hr':>{col_num}} "
        f"{'$/Pg':>{col_num}} "
        f"{'Util%':>{col_num}} "
        f"{'Rework':>{col_num}}"
    )
    print(header)
    print("-" * len(header))

    for card in cards:
        sid = safe_get(card, "session", "id", default=card["_source_file"])
        hive = safe_get(card, "session", "hive", default="?")
        d = card["_derived"]
        pages = safe_get(card, "output", "pages_produced")

        util_pct = fmt(d["agent_utilization"] * 100, 0) if d["agent_utilization"] is not None else "-"

        print(
            f"{str(sid):<{col_id}} "
            f"{str(hive):<12} "
            f"{fmt(d['wall_clock_hours']):>{col_num}} "
            f"{fmt(pages):>{col_num}} "
            f"{fmt(d['pages_per_hour']):>{col_num}} "
            f"{fmt(d['lines_per_hour'], 0):>{col_num}} "
            f"{fmt(d['cost_per_page']):>{col_num}} "
            f"{util_pct:>{col_num}} "
            f"{fmt(d['rework_ratio']):>{col_num}}"
        )


def print_hive_table(hive_aggs):
    """Print cross-session aggregates by hive."""
    print_header("AGGREGATES BY HIVE")

    if not hive_aggs:
        print("  (no data)")
        return

    col_hive = 14
    col_num = 10

    header = (
        f"{'Hive':<{col_hive}} "
        f"{'Sessions':>{col_num}} "
        f"{'Tot Hours':>{col_num}} "
        f"{'Tot Pages':>{col_num}} "
        f"{'Avg Pg/Hr':>{col_num}} "
        f"{'Avg Ln/Hr':>{col_num}} "
        f"{'Avg $/Pg':>{col_num}} "
        f"{'Avg Util%':>{col_num}}"
    )
    print(header)
    print("-" * len(header))

    for hive, agg in hive_aggs.items():
        m = agg["means"]
        util_pct = fmt(m["agent_utilization"] * 100, 0) if m["agent_utilization"] is not None else "-"

        print(
            f"{hive:<{col_hive}} "
            f"{agg['sessions']:>{col_num}} "
            f"{fmt(agg['total_hours']):>{col_num}} "
            f"{fmt(agg['total_pages']):>{col_num}} "
            f"{fmt(m['pages_per_hour']):>{col_num}} "
            f"{fmt(m['lines_per_hour'], 0):>{col_num}} "
            f"{fmt(m['cost_per_page']):>{col_num}} "
            f"{util_pct:>{col_num}}"
        )


def print_baseline_comparison(cards):
    """Compare observed metrics against published baselines."""
    print_header("BASELINE COMPARISON")

    pph_vals = [c["_derived"]["pages_per_hour"] for c in cards if c["_derived"]["pages_per_hour"] is not None]

    if not pph_vals:
        print("  Insufficient data for baseline comparison (no pages_per_hour values).")
        print("  Fill start_time, end_time, and pages_produced in scorecards.")
        return

    observed_pph = sum(pph_vals) / len(pph_vals)
    baseline_pph = BASELINES["academic_pages_per_hour"]
    speedup = observed_pph / baseline_pph if baseline_pph > 0 else None

    print(f"  Observed avg pages/hour:  {observed_pph:.2f}  (n={len(pph_vals)} sessions)")
    print(f"  Academic baseline:        {baseline_pph:.2f}  (literature: 0.5-1.0 pg/hr)")
    print()

    if speedup is not None:
        print(f"  Your speedup factor:      {speedup:.2f}x  over academic baseline")
        print()
        print("  Reference speedup factors:")
        print(f"    Copilot (Peng 2023):    {BASELINES['copilot_speedup_factor']:.2f}x  (constrained coding tasks)")
        print(f"    METR experienced devs:  {BASELINES['metr_experienced_factor']:.2f}x  (19% SLOWER with AI)")
        print(f"    Senior + Copilot:       {BASELINES['senior_copilot_factor']:.2f}x  (8-13% gain)")
        print()

        print("  Interpretation:")
        if speedup > BASELINES["copilot_speedup_factor"]:
            print(f"    Swarm throughput ({speedup:.2f}x) EXCEEDS the Copilot benchmark ({BASELINES['copilot_speedup_factor']:.2f}x).")
            print("    This suggests multi-agent orchestration yields gains beyond single-agent assist.")
            print("    Caveat: different task types (technical writing vs. coding); direct comparison is illustrative, not causal.")
        elif speedup > BASELINES["senior_copilot_factor"]:
            print(f"    Swarm throughput ({speedup:.2f}x) is above senior+Copilot ({BASELINES['senior_copilot_factor']:.2f}x)")
            print("    but below the Copilot constrained-task benchmark ({:.2f}x).".format(BASELINES['copilot_speedup_factor']))
            print("    Consistent with productivity gains from AI-assisted research workflows.")
        elif speedup > 1.0:
            print(f"    Swarm throughput ({speedup:.2f}x) shows modest gains over unassisted baseline.")
            print("    Consider whether overhead (agent coordination, rework) is limiting net throughput.")
        else:
            print(f"    Swarm throughput ({speedup:.2f}x) is AT or BELOW unassisted baseline.")
            print("    This echoes the METR finding: AI assistance does not always accelerate experienced practitioners.")
            print("    Investigate: high rework_ratio, agent_failures, or blocked_minutes may explain the drag.")

    # Agent utilization note
    util_vals = [c["_derived"]["agent_utilization"] for c in cards if c["_derived"]["agent_utilization"] is not None]
    if util_vals:
        avg_util = sum(util_vals) / len(util_vals)
        print()
        print(f"  Agent utilization:        {avg_util*100:.0f}%  (n={len(util_vals)})")
        if avg_util < 0.80:
            print("    Below 80% — significant agent waste. Review failure causes.")
        elif avg_util < 0.95:
            print("    Acceptable range. Some agent failures are expected in exploratory work.")
        else:
            print("    Excellent utilization. Minimal agent waste.")


def print_data_quality(issues):
    """Report non-numeric values that were skipped during arithmetic."""
    print_header("DATA QUALITY ISSUES")
    if not issues:
        print("  No data quality issues detected.")
        return
    print(f"  {len(issues)} non-numeric value(s) in numeric fields (skipped, not fatal):")
    print()
    by_file = {}
    for issue in issues:
        by_file.setdefault(issue["file"], []).append(issue)
    for fname in sorted(by_file):
        print(f"  {fname}:")
        for issue in by_file[fname]:
            print(f"    {issue['field']:<45} = {issue['value']}  ({issue['type']})")
        print()


# ---------------------------------------------------------------------------
# CSV output
# ---------------------------------------------------------------------------


def write_csv(cards, hive_aggs):
    """Write two CSV files: sessions.csv and hive_aggregates.csv."""
    out_dir = SCRIPT_DIR / "data"

    # Per-session CSV
    session_path = out_dir / "sessions.csv"
    with open(session_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        header = [
            "session_id", "date", "hive", "researcher",
            "pages_produced", "total_lines_written",
            "total_files_created", "total_files_modified",
            "agents_spawned", "agent_failures", "swarm_topology",
            "tokens_input", "tokens_output", "total_cost_usd",
            "rework_files",
        ] + DERIVED_FIELDS
        writer.writerow(header)

        for card in cards:
            d = card["_derived"]
            row = [
                safe_get(card, "session", "id"),
                safe_get(card, "session", "date"),
                safe_get(card, "session", "hive"),
                safe_get(card, "session", "researcher"),
                safe_get(card, "output", "pages_produced"),
                safe_get(card, "output", "total_lines_written"),
                safe_get(card, "output", "total_files_created"),
                safe_get(card, "output", "total_files_modified"),
                safe_get(card, "ai_efficiency", "agents_spawned"),
                safe_get(card, "process", "agent_failures"),
                safe_get(card, "ai_efficiency", "swarm_topology"),
                safe_get(card, "ai_efficiency", "tokens_input"),
                safe_get(card, "ai_efficiency", "tokens_output"),
                safe_get(card, "ai_efficiency", "total_cost_usd"),
                safe_get(card, "process", "rework_files"),
            ] + [d.get(field) for field in DERIVED_FIELDS]
            writer.writerow(["" if v is None else v for v in row])

    print(f"\n  Sessions CSV:     {session_path}")

    # Hive aggregates CSV
    hive_path = out_dir / "hive_aggregates.csv"
    with open(hive_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        header = ["hive", "sessions", "total_hours", "total_pages"] + [
            f"avg_{field}" for field in DERIVED_FIELDS
        ]
        writer.writerow(header)

        for hive, agg in hive_aggs.items():
            m = agg["means"]
            row = [hive, agg["sessions"], agg["total_hours"], agg["total_pages"]] + [
                m.get(field) for field in DERIVED_FIELDS
            ]
            writer.writerow(["" if v is None else v for v in row])

    print(f"  Hive aggregates:  {hive_path}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main():
    parser = argparse.ArgumentParser(
        description="Analyze AI-Swarm productivity scorecards."
    )
    parser.add_argument(
        "--csv", action="store_true",
        help="Write CSV files to data/ for further analysis"
    )
    args = parser.parse_args()

    print(f"Scorecard directory: {SCORECARDS_DIR}")
    cards, skipped, errors = load_scorecards()

    print(f"Loaded: {len(cards)} scorecard(s)")
    if skipped:
        print(f"Skipped: {', '.join(skipped)}")
    if errors:
        print("Errors:")
        for name, err in errors:
            print(f"  {name}: {err}")

    if not cards:
        print("\nNo scorecards to analyze. Add YAML files to data/scorecards/.")
        return

    print_session_table(cards)

    hive_aggs = aggregate_by_hive(cards)
    print_hive_table(hive_aggs)

    print_baseline_comparison(cards)

    print_data_quality(DATA_QUALITY_ISSUES)

    if args.csv:
        write_csv(cards, hive_aggs)

    print()


if __name__ == "__main__":
    main()
