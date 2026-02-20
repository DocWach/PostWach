"""
Export the Mastery Dashboard as a self-contained HTML file.

Usage:
    PYTHONPATH=src python -m mastery_dashboard.export_html [output_path]
"""
import html
import sys
from pathlib import Path
from typing import Dict, List, Optional, Set

from mastery_dashboard.config.loader import load_course_config
from mastery_dashboard.config.schema import BlockConfig, CourseConfig, GradeRuleConfig
from mastery_dashboard.data.database import get_connection, init_schema
from mastery_dashboard.data.provider import MasteryDataProvider
from mastery_dashboard.data.repositories import AuditRepo, MasteryRepo, SubmissionRepo
from mastery_dashboard.logic.mastery_engine import MasteryEngine
from mastery_dashboard.models.domain import BlockProgress, ClassOutcomeStats, StudentGradeView
from mastery_dashboard.models.enums import MasteryStatus

_CONFIG_PATH = Path(__file__).parent / "config" / "sample_course.yaml"
_DB_PATH = Path(__file__).parent / "data" / "mastery.db"

GRADE_COLORS = {"A": "#27AE60", "B": "#2E86AB", "C": "#F39C12", "D": "#E67E22"}
GRADE_LABELS = {"A": "Excellent", "B": "Good", "C": "Satisfactory", "D": "Developing"}
BLOCK_COLORS = ["#1a1a5e", "#2a4a7f", "#3a6a5e", "#4a3a6e"]

STATUS_BADGE = {
    MasteryStatus.MASTERED: '<span class="badge badge-mastered">&#10004; Mastered</span>',
    MasteryStatus.IN_PROGRESS: '<span class="badge badge-progress">&#9888; In Progress</span>',
    MasteryStatus.NOT_ATTEMPTED: '<span class="badge badge-none">&#9675;</span>',
}
CHECK_ICON = {
    MasteryStatus.MASTERED: '<span style="color:#27AE60; font-size:1.1rem;">&#10004;</span>',
    MasteryStatus.IN_PROGRESS: '<span style="color:#E67E22; font-size:1.1rem;">&#10004;</span>',
    MasteryStatus.NOT_ATTEMPTED: '<span style="color:#ccc; font-size:1.1rem;">&#10004;</span>',
}


def _esc(text: str) -> str:
    return html.escape(str(text))


def _render_grade_indicator(current_grade: Optional[str], grade_goal: Optional[str]) -> str:
    display = current_grade if current_grade else "&mdash;"
    color = GRADE_COLORS.get(current_grade or "", "#95A5A6")
    goal_color = GRADE_COLORS.get(grade_goal or "", "#95A5A6")

    goal_html = ""
    if grade_goal:
        goal_html = f'''<div class="grade-card" style="border:3px solid {goal_color}; background:#f8f9fa;">
            <div class="grade-label" style="color:#555;">Grade Goal</div>
            <div class="grade-letter" style="color:{goal_color};">{_esc(grade_goal)}</div>
        </div>'''
    else:
        goal_html = '''<div class="grade-card" style="border:2px dashed #ccc; background:#f8f9fa;">
            <div class="grade-label" style="color:#555;">Grade Goal</div>
            <div style="font-size:2rem; color:#aaa; line-height:1.5;">&mdash;</div>
        </div>'''

    return f'''<div class="grade-indicator-row">
        <div class="grade-card" style="background:{color};">
            <div class="grade-label" style="color:#fff; opacity:0.85;">Current Grade</div>
            <div class="grade-letter" style="color:#fff;">{_esc(display)}</div>
        </div>
        {goal_html}
    </div>'''


def _render_grade_guide(config: CourseConfig, current_grade: Optional[str]) -> str:
    parts = ['<h4>Grade Guide</h4>']
    sorted_rules = sorted(config.grade_rules, key=lambda r: r.display_order)
    for rule in sorted_rules:
        color = GRADE_COLORS.get(rule.grade, "#95A5A6")
        label = GRADE_LABELS.get(rule.grade, rule.grade)
        block_names = []
        for bid in rule.required_blocks:
            block = config.get_block(bid)
            block_names.append(block.name if block else bid)
        is_current = rule.grade == current_grade
        border = f"3px solid {color}" if is_current else "1px solid #ddd"
        blocks_html = ", ".join(_esc(n) for n in block_names)
        parts.append(f'''<div class="guide-row" style="border:{border};">
            <div class="guide-tile" style="background:{color};">{_esc(rule.grade)}</div>
            <div>
                <div style="font-weight:600; color:#1a1a2e;">{_esc(label)}</div>
                <div style="font-size:0.8rem; color:#555;">Mastery achieved for: {blocks_html}</div>
            </div>
        </div>''')
    return "\n".join(parts)


def _render_outcome_checklist(config: CourseConfig, mastery_map: Dict[str, MasteryStatus]) -> str:
    parts = ['<h4>Learning Objectives Mastery</h4>']
    for i, block in enumerate(config.blocks):
        color = BLOCK_COLORS[i % len(BLOCK_COLORS)]
        parts.append(f'<div class="block-header" style="background:{color};">{_esc(block.name)}</div>')
        for outcome in block.outcomes:
            status = mastery_map.get(outcome.id, MasteryStatus.NOT_ATTEMPTED)
            check = CHECK_ICON[status]
            badge = STATUS_BADGE[status]
            parts.append(f'''<div class="outcome-row">
                <div class="outcome-left">
                    {check}
                    <span style="font-weight:600; color:#1a1a5e;">{_esc(outcome.id)}</span>
                    <span style="color:#333;">{_esc(outcome.name)}</span>
                </div>
                <div>{badge}</div>
            </div>''')
        parts.append('<div class="block-separator"></div>')
    return "\n".join(parts)


def _render_pathway_cards(
    config: CourseConfig,
    completed_blocks: Set[str],
    mastery_map: Dict[str, MasteryStatus],
    grade_goal: Optional[str],
) -> str:
    sorted_rules = sorted(config.grade_rules, key=lambda r: r.display_order, reverse=True)
    cards = []
    for rule in sorted_rules:
        required = set(rule.required_blocks)
        is_complete = required.issubset(completed_blocks)
        color = GRADE_COLORS.get(rule.grade, "#95A5A6")
        is_goal = rule.grade == grade_goal

        total = 0
        mastered = 0
        for bid in rule.required_blocks:
            for oid in config.outcome_ids_for_block(bid):
                total += 1
                if mastery_map.get(oid) == MasteryStatus.MASTERED:
                    mastered += 1
        remaining = total - mastered

        checks = ""
        for i in range(total):
            if i < mastered:
                checks += '<span style="color:#27AE60; font-size:1.1rem;">&#10004;</span> '
            else:
                checks += '<span style="color:#ccc; font-size:1.1rem;">&#9675;</span> '

        if is_complete:
            status_html = '<div style="color:#27AE60; font-weight:600; font-size:0.8rem;">&#10003; MASTERED!</div>'
        else:
            status_html = f'<div style="color:#555; font-size:0.75rem;">{remaining} more to master</div>'

        border = f"3px solid {color}" if is_goal else "1px solid #ddd"
        goal_badge = ""
        if is_goal:
            goal_badge = '<div class="goal-badge">YOUR GOAL</div>'

        cards.append(f'''<div class="pathway-card" style="border:{border};">
            <div class="pathway-grade" style="background:{color};">{_esc(rule.grade)} Pathway</div>
            {goal_badge}
            <div style="margin:0.5rem 0; line-height:1.6;">{checks}</div>
            {status_html}
        </div>''')

    return f'<div class="pathway-row">{"".join(cards)}</div>'


def _render_progress_bar(
    config: CourseConfig,
    mastery_map: Dict[str, MasteryStatus],
    grade_goal: Optional[str],
) -> str:
    if not grade_goal:
        return ""
    target_rule = None
    for rule in config.grade_rules:
        if rule.grade == grade_goal:
            target_rule = rule
            break
    if not target_rule:
        return ""

    total = 0
    mastered = 0
    for bid in target_rule.required_blocks:
        for oid in config.outcome_ids_for_block(bid):
            total += 1
            if mastery_map.get(oid) == MasteryStatus.MASTERED:
                mastered += 1
    pct = mastered / total if total > 0 else 0
    color = GRADE_COLORS.get(grade_goal, "#2E86AB")

    return f'''<div class="progress-section">
        <div style="font-size:0.85rem; color:#555; margin-bottom:0.3rem;">
            Complete the remaining outcomes to reach your grade goal!
        </div>
        <div class="progress-track">
            <div class="progress-fill" style="background:{color}; width:{pct*100:.0f}%;"></div>
        </div>
        <div style="font-size:0.75rem; color:#777; margin-top:0.2rem; text-align:right;">
            {mastered}/{total} outcomes mastered ({pct:.0%})
        </div>
    </div>'''


def _render_student_compass(
    provider: MasteryDataProvider,
    config: CourseConfig,
    view: StudentGradeView,
    grade_goal: Optional[str],
) -> str:
    parts = []

    # Title bar
    parts.append(f'''<div class="title-bar">
        <div class="title">Mastery Progress Tracker</div>
        <div class="subtitle">Track Your Learning Outcomes</div>
    </div>
    <div style="text-align:right; color:#555; margin-bottom:0.5rem;">
        Hello, {_esc(view.student.name)}!
    </div>''')

    # Left / right layout
    parts.append('<div class="two-col">')
    parts.append('<div class="col-left">')
    parts.append(_render_grade_indicator(view.current_grade, grade_goal))
    parts.append('<hr class="divider">')
    parts.append(_render_grade_guide(config, view.current_grade))
    parts.append('</div>')
    parts.append('<div class="col-right">')
    parts.append(_render_outcome_checklist(config, view.mastery_records))
    parts.append('</div>')
    parts.append('</div>')

    # Pathway
    parts.append('<hr class="divider">')
    parts.append('<h4>Grade Pathway Progress</h4>')
    parts.append(_render_pathway_cards(config, view.completed_blocks, view.mastery_records, grade_goal))
    parts.append(_render_progress_bar(config, view.mastery_records, grade_goal))

    return "\n".join(parts)


def _render_assignments(provider: MasteryDataProvider, config: CourseConfig, student_id: str, name: str) -> str:
    submissions = provider.get_student_submissions(student_id)
    parts = [f'<h3>Assignments: {_esc(name)}</h3>']

    if not submissions:
        parts.append('<div class="info-box">No submissions yet.</div>')
        return "\n".join(parts)

    evaluated = [s for s in submissions if s.status.value == "evaluated"]
    pending = [s for s in submissions if s.status.value == "pending"]
    needs_review = [s for s in submissions if s.status.value == "needs_review"]

    parts.append(f'''<div class="metrics-row">
        <div class="metric-card"><div class="metric-value">{len(submissions)}</div><div class="metric-label">Total Submissions</div></div>
        <div class="metric-card"><div class="metric-value">{len(evaluated)}</div><div class="metric-label">Evaluated</div></div>
        <div class="metric-card"><div class="metric-value">{len(pending) + len(needs_review)}</div><div class="metric-label">Pending</div></div>
    </div>''')

    parts.append('<h4>Submission History</h4>')
    parts.append('<table class="data-table"><thead><tr>')
    parts.append('<th>Submitted</th><th>Block</th><th>Outcome</th><th>Name</th><th>Score</th><th>Status</th><th>Notes</th>')
    parts.append('</tr></thead><tbody>')
    for sub in submissions:
        outcome = config.get_outcome(sub.outcome_id)
        block = config.get_block_for_outcome(sub.outcome_id)
        parts.append(f'''<tr>
            <td>{sub.submitted_at.strftime("%Y-%m-%d %H:%M")}</td>
            <td>{_esc(block.name.split(":")[0].strip()) if block else "&mdash;"}</td>
            <td>{_esc(sub.outcome_id)}</td>
            <td>{_esc(outcome.name) if outcome else "&mdash;"}</td>
            <td>{sub.score:.0%}</td>
            <td>{_esc(sub.status.value.replace("_", " ").title())}</td>
            <td>{_esc(sub.evaluator_notes or "&mdash;")}</td>
        </tr>''')
    parts.append('</tbody></table>')
    return "\n".join(parts)


def _render_instructor_overview(provider: MasteryDataProvider, config: CourseConfig) -> str:
    students = provider.students.list_all()
    student_names = {s.id: s.name for s in students}
    student_ids = [s.id for s in students]
    outcome_stats = provider.get_class_outcome_stats()
    grade_dist = provider.get_grade_distribution()
    total_students = len(students)
    avg_mastery = 0.0
    if outcome_stats:
        avg_mastery = sum(s.mastery_rate for s in outcome_stats) / len(outcome_stats)
    graded = total_students - grade_dist.get("No Grade", 0)
    pending_count = len(provider.get_pending_submissions())

    parts = ['<h2>Instructor Overview</h2>']

    # Metrics
    parts.append(f'''<div class="metrics-row">
        <div class="metric-card"><div class="metric-value">{total_students}</div><div class="metric-label">Total Students</div></div>
        <div class="metric-card"><div class="metric-value">{avg_mastery:.0%}</div><div class="metric-label">Avg Mastery Rate</div></div>
        <div class="metric-card"><div class="metric-value">{graded}/{total_students}</div><div class="metric-label">Students Graded</div></div>
        <div class="metric-card"><div class="metric-value">{pending_count}</div><div class="metric-label">Pending Reviews</div></div>
    </div>''')

    # Mastery heatmap as HTML table
    parts.append('<h3>Mastery Heatmap</h3>')
    outcome_ids = config.all_outcome_ids()
    matrix = provider.mastery.get_matrix(student_ids, outcome_ids)
    parts.append('<div class="heatmap-scroll"><table class="heatmap-table"><thead><tr><th></th>')
    for oid in outcome_ids:
        parts.append(f'<th class="heatmap-th">{_esc(oid)}</th>')
    parts.append('</tr></thead><tbody>')

    heatmap_colors = {
        MasteryStatus.MASTERED: "#27AE60",
        MasteryStatus.IN_PROGRESS: "#F39C12",
        MasteryStatus.NOT_ATTEMPTED: "#e0e0e0",
    }
    for sid in student_ids:
        name = _esc(student_names.get(sid, sid))
        parts.append(f'<tr><td class="heatmap-name">{name}</td>')
        for oid in outcome_ids:
            status = matrix.get(sid, {}).get(oid, MasteryStatus.NOT_ATTEMPTED)
            color = heatmap_colors[status]
            tip = status.value.replace("_", " ").title()
            parts.append(f'<td class="heatmap-cell" style="background:{color};" title="{name}: {_esc(oid)} &mdash; {tip}"></td>')
        parts.append('</tr>')
    parts.append('</tbody></table></div>')

    # Heatmap legend
    parts.append('''<div class="heatmap-legend">
        <span><span class="legend-dot" style="background:#27AE60;"></span> Mastered</span>
        <span><span class="legend-dot" style="background:#F39C12;"></span> In Progress</span>
        <span><span class="legend-dot" style="background:#e0e0e0;"></span> Not Attempted</span>
    </div>''')

    # Grade distribution table
    parts.append('<h3>Grade Distribution</h3>')
    parts.append('<div class="grade-dist-row">')
    grade_colors = {"A": "#27AE60", "B": "#2E86AB", "C": "#F39C12", "D": "#E67E22", "No Grade": "#95A5A6"}
    for g in ["A", "B", "C", "D", "No Grade"]:
        count = grade_dist.get(g, 0)
        if count == 0 and g != "No Grade":
            continue
        color = grade_colors.get(g, "#95A5A6")
        parts.append(f'''<div class="grade-dist-item">
            <div class="grade-dist-bar" style="background:{color}; height:{max(count * 30, 4)}px;"></div>
            <div class="grade-dist-count">{count}</div>
            <div class="grade-dist-label">{_esc(g)}</div>
        </div>''')
    parts.append('</div>')

    # Outcome difficulty
    parts.append('<h3>Outcome Difficulty (lowest mastery first)</h3>')
    if outcome_stats:
        sorted_stats = sorted(outcome_stats, key=lambda s: s.mastery_rate)
        parts.append('<div class="difficulty-chart">')
        for s in sorted_stats:
            pct = s.mastery_rate * 100
            color = "#E74C3C" if pct < 30 else ("#F39C12" if pct < 60 else "#2ECC71")
            parts.append(f'''<div class="diff-row">
                <div class="diff-label">{_esc(s.outcome_id)}: {_esc(s.outcome_name)}</div>
                <div class="diff-bar-track">
                    <div class="diff-bar-fill" style="width:{pct:.0f}%; background:{color};"></div>
                </div>
                <div class="diff-pct">{pct:.0f}%</div>
            </div>''')
        parts.append('</div>')

    # Student detail table
    parts.append('<h3>Student Detail</h3>')
    parts.append('<table class="data-table"><thead><tr><th>Student</th><th>Grade</th><th>Completed Blocks</th><th>Mastered</th><th>In Progress</th></tr></thead><tbody>')
    for s in students:
        view = provider.get_student_grade_view(s.id)
        if not view:
            continue
        mastered_count = sum(1 for v in view.mastery_records.values() if v == MasteryStatus.MASTERED)
        in_progress_count = sum(1 for v in view.mastery_records.values() if v == MasteryStatus.IN_PROGRESS)
        parts.append(f'''<tr>
            <td>{_esc(s.name)}</td>
            <td><strong>{_esc(view.current_grade or "&mdash;")}</strong></td>
            <td>{_esc(", ".join(sorted(view.completed_blocks)) or "None")}</td>
            <td>{mastered_count}/{len(config.all_outcome_ids())}</td>
            <td>{in_progress_count}</td>
        </tr>''')
    parts.append('</tbody></table>')

    return "\n".join(parts)


CSS = """
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
       background: #f5f6fa; color: #1a1a2e; line-height: 1.5; }
.container { max-width: 1100px; margin: 0 auto; padding: 1.5rem; }
.title-bar { text-align: center; padding: 0.8rem 0; margin-bottom: 0.5rem; }
.title { font-size: 1.8rem; font-weight: 700; color: #1a1a5e; }
.subtitle { font-size: 0.95rem; color: #666; }
h2 { font-size: 1.5rem; color: #1a1a5e; margin: 1rem 0 0.8rem; }
h3 { font-size: 1.2rem; color: #1a1a5e; margin: 1rem 0 0.6rem; }
h4 { font-size: 1rem; color: #1a1a5e; margin: 0.5rem 0; }
.divider { border: none; border-top: 1px solid #e0e0e0; margin: 1rem 0; }
.info-box { padding: 0.8rem 1rem; background: #e8f4fd; border-radius: 6px; color: #1a6ea0; }

/* Tabs */
.tab-bar { display: flex; gap: 0; margin-bottom: 1.5rem; border-bottom: 2px solid #e0e0e0; }
.tab { padding: 0.6rem 1.4rem; cursor: pointer; font-weight: 600; color: #777;
       border-bottom: 3px solid transparent; margin-bottom: -2px; user-select: none; }
.tab.active { color: #1a1a5e; border-bottom-color: #1a1a5e; }
.tab:hover { color: #1a1a5e; }
.tab-content { display: none; }
.tab-content.active { display: block; }

/* Grade indicator */
.grade-indicator-row { display: flex; gap: 1rem; margin-bottom: 0.5rem; }
.grade-card { flex: 1; text-align: center; padding: 1.2rem; border-radius: 12px; }
.grade-label { font-size: 0.85rem; }
.grade-letter { font-size: 3.5rem; font-weight: 800; line-height: 1.1; }

/* Grade guide */
.guide-row { display: flex; align-items: center; gap: 0.75rem; padding: 0.6rem 0.8rem;
             margin-bottom: 0.5rem; border-radius: 8px; background: #fff; }
.guide-tile { min-width: 2.5rem; height: 2.5rem; border-radius: 6px; display: flex;
              align-items: center; justify-content: center; color: #fff; font-weight: 800; font-size: 1.2rem; }

/* Outcome checklist */
.block-header { color: #fff; padding: 0.5rem 0.8rem; border-radius: 6px 6px 0 0;
                margin-top: 1rem; font-weight: 600; }
.outcome-row { display: flex; justify-content: space-between; align-items: center;
               padding: 0.45rem 0.8rem; border-bottom: 1px solid #eee; background: #fff; }
.outcome-left { display: flex; align-items: center; gap: 0.5rem; }
.block-separator { border-bottom: 2px solid #e0e0e0; margin-bottom: 0.5rem; }
.badge { font-weight: 600; }
.badge-mastered { color: #27AE60; }
.badge-progress { color: #E67E22; }
.badge-none { color: #aaa; }

/* Two-column layout */
.two-col { display: flex; gap: 2rem; }
.col-left { flex: 1; min-width: 0; }
.col-right { flex: 2; min-width: 0; }

/* Pathway cards */
.pathway-row { display: flex; gap: 1rem; margin: 0.5rem 0; }
.pathway-card { flex: 1; text-align: center; padding: 0.8rem 0.5rem; border-radius: 10px;
                background: #fff; min-height: 140px; }
.pathway-grade { color: #fff; font-weight: 800; font-size: 1.3rem; padding: 0.3rem 0.8rem;
                 border-radius: 6px; display: inline-block; margin-bottom: 0.4rem; }
.goal-badge { font-size: 0.65rem; color: #fff; background: #555; padding: 1px 6px;
              border-radius: 3px; margin-top: 2px; display: inline-block; }

/* Progress bar */
.progress-section { margin: 0.5rem 0 1rem; }
.progress-track { background: #e0e0e0; border-radius: 8px; height: 14px; overflow: hidden; }
.progress-fill { height: 100%; border-radius: 8px; transition: width 0.3s; }

/* Metrics */
.metrics-row { display: flex; gap: 1rem; margin: 0.5rem 0 1rem; }
.metric-card { flex: 1; text-align: center; padding: 1rem; background: #fff; border-radius: 10px;
               border: 1px solid #e0e0e0; }
.metric-value { font-size: 1.8rem; font-weight: 700; color: #1a1a5e; }
.metric-label { font-size: 0.8rem; color: #777; }

/* Data table */
.data-table { width: 100%; border-collapse: collapse; background: #fff; border-radius: 8px;
              overflow: hidden; margin: 0.5rem 0 1rem; }
.data-table th { background: #f0f2f5; padding: 0.6rem 0.8rem; text-align: left;
                 font-size: 0.85rem; color: #555; border-bottom: 2px solid #ddd; }
.data-table td { padding: 0.5rem 0.8rem; border-bottom: 1px solid #eee; font-size: 0.85rem; }
.data-table tr:last-child td { border-bottom: none; }

/* Heatmap */
.heatmap-scroll { overflow-x: auto; margin: 0.5rem 0; }
.heatmap-table { border-collapse: collapse; }
.heatmap-th { writing-mode: vertical-lr; transform: rotate(180deg); padding: 0.3rem;
              font-size: 0.7rem; color: #555; text-align: left; }
.heatmap-name { font-size: 0.8rem; padding: 0.2rem 0.6rem; white-space: nowrap; color: #333; }
.heatmap-cell { width: 28px; height: 22px; min-width: 28px; border: 1px solid #fff; }
.heatmap-legend { display: flex; gap: 1.2rem; font-size: 0.8rem; color: #555; margin: 0.5rem 0; }
.legend-dot { display: inline-block; width: 12px; height: 12px; border-radius: 3px;
              vertical-align: middle; margin-right: 4px; }

/* Grade distribution */
.grade-dist-row { display: flex; gap: 1.5rem; align-items: flex-end; margin: 0.5rem 0 1rem; padding-left: 1rem; }
.grade-dist-item { text-align: center; }
.grade-dist-bar { width: 40px; border-radius: 4px 4px 0 0; min-height: 4px; }
.grade-dist-count { font-weight: 700; font-size: 0.9rem; color: #333; margin-top: 4px; }
.grade-dist-label { font-size: 0.8rem; color: #555; }

/* Difficulty chart */
.difficulty-chart { margin: 0.5rem 0 1rem; }
.diff-row { display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.3rem; }
.diff-label { flex: 0 0 220px; font-size: 0.8rem; color: #333; text-align: right; white-space: nowrap;
              overflow: hidden; text-overflow: ellipsis; }
.diff-bar-track { flex: 1; background: #e0e0e0; border-radius: 4px; height: 14px; overflow: hidden; }
.diff-bar-fill { height: 100%; border-radius: 4px; }
.diff-pct { flex: 0 0 40px; font-size: 0.8rem; color: #555; text-align: right; }

/* Sidebar stub for print */
.sidebar { display: flex; gap: 0.5rem; flex-wrap: wrap; margin-bottom: 1rem;
           padding: 0.8rem; background: #fff; border-radius: 10px; border: 1px solid #e0e0e0; }
.sidebar-title { font-weight: 700; color: #1a1a5e; font-size: 1.1rem; width: 100%; }
.sidebar-caption { font-size: 0.85rem; color: #666; width: 100%; margin-bottom: 0.5rem; }

@media (max-width: 768px) {
    .two-col { flex-direction: column; }
    .pathway-row { flex-direction: column; }
    .metrics-row { flex-direction: column; }
    .diff-label { flex: 0 0 120px; }
}
@media print {
    body { background: #fff; }
    .tab-bar { display: none; }
    .tab-content { display: block !important; }
    .sidebar { display: none; }
}
"""


def generate_html(output_path: Path) -> None:
    config = load_course_config(_CONFIG_PATH)
    conn = get_connection(str(_DB_PATH))
    init_schema(conn)
    provider = MasteryDataProvider(conn, config)

    students = provider.students.list_all()
    if not students:
        print("No data -- run 'Seed Demo Data' in the Streamlit app first.")
        sys.exit(1)

    # Build all student sections
    student_tabs_html = []
    student_content_html = []
    for idx, student in enumerate(students):
        view = provider.get_student_grade_view(student.id)
        if not view:
            continue
        active = " active" if idx == 0 else ""
        student_tabs_html.append(
            f'<div class="tab{active}" data-target="student-{idx}">{_esc(student.name)}</div>'
        )

        grade_goal = view.next_grade or view.current_grade or (
            sorted([r.grade for r in config.grade_rules],
                   key=lambda g: next(r.display_order for r in config.grade_rules if r.grade == g))[-1]
            if config.grade_rules else None
        )

        compass_html = _render_student_compass(provider, config, view, grade_goal)
        assignments_html = _render_assignments(provider, config, student.id, student.name)

        student_content_html.append(
            f'<div class="tab-content{active}" id="student-{idx}">'
            f'  <div class="inner-tabs">'
            f'    <div class="tab-bar">'
            f'      <div class="tab active" data-target="compass-{idx}">Dashboard</div>'
            f'      <div class="tab" data-target="assign-{idx}">Assignments</div>'
            f'    </div>'
            f'    <div class="tab-content active" id="compass-{idx}">{compass_html}</div>'
            f'    <div class="tab-content" id="assign-{idx}">{assignments_html}</div>'
            f'  </div>'
            f'</div>'
        )

    instructor_html = _render_instructor_overview(provider, config)

    page = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Mastery Progress Tracker &mdash; {_esc(config.name)}</title>
<style>{CSS}</style>
</head>
<body>
<div class="container">

<div class="sidebar">
    <div class="sidebar-title">Mastery Dashboard</div>
    <div class="sidebar-caption">{_esc(config.name)} &mdash; {_esc(config.semester)}</div>
</div>

<!-- Role tabs -->
<div class="tab-bar" id="role-tabs">
    <div class="tab active" data-target="role-student">Student</div>
    <div class="tab" data-target="role-instructor">Instructor</div>
</div>

<!-- Student role -->
<div class="tab-content active" id="role-student">
    <div class="tab-bar" id="student-tabs">
        {"".join(student_tabs_html)}
    </div>
    {"".join(student_content_html)}
</div>

<!-- Instructor role -->
<div class="tab-content" id="role-instructor">
    {instructor_html}
</div>

</div>
<script>
document.querySelectorAll('.tab-bar').forEach(bar => {{
    bar.querySelectorAll('.tab').forEach(tab => {{
        tab.addEventListener('click', () => {{
            const target = tab.dataset.target;
            if (!target) return;
            // Deactivate siblings
            bar.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
            tab.classList.add('active');
            // Show/hide content at same level
            const parent = bar.parentElement;
            parent.querySelectorAll(':scope > .tab-content').forEach(c => {{
                c.classList.toggle('active', c.id === target);
            }});
        }});
    }});
}});
</script>
</body>
</html>"""

    output_path.write_text(page, encoding="utf-8")
    print(f"Exported to {output_path} ({len(page):,} bytes)")


if __name__ == "__main__":
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).parent / "dashboard_export.html"
    generate_html(out)
