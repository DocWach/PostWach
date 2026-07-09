#!/usr/bin/env python3
"""R019 /refverify -- single-model triple-check workflow + DOI dedup.

MVP scope (Phase 5a):
  - Step 0: DOI dedup pre-check against approved.bib and pending/*.bib.
  - Step 0a: Dedup-of-same-DOI inside pending (survivor selection).
  - Step 1-3: Field comparison between agent-fetched canonical values
    and the candidate's claimed values. The script does NOT fetch from
    the web; the calling agent does (WebSearch + WebFetch in-session)
    and passes results in via the --evidence JSON file or --field flags.
  - Step 4: Promote a verified candidate from pending/ -> approved.bib
    + manifest.yaml entry (verification_mode: single-model-triple-check).
  - Step 5 (human-attested): The --attest path, locked behind a real
    human identifier in --attested-by. The agent cannot self-attest.

OUT OF SCOPE for the MVP (deferred to Phase 5b):
  - The full Byzantine N=3 protocol with Codex + Gemini + Bayesian
    aggregation across independent models. That requires the tri-model
    review pipeline orchestration which is not wired into this script.

See: docs/proposed_R019_references_verification_gate.md §5, §5.1, §6
"""

import argparse
import json
import re
import sys
import unicodedata
from datetime import date
from pathlib import Path

DEFAULT_STORE_DIR = r"C:\Users\pfwac\OneDrive - University of Arizona\Documents\04 Resource Library\00 Verified References"
DEFAULT_APPROVED = DEFAULT_STORE_DIR + r"\approved.bib"
DEFAULT_PENDING = DEFAULT_STORE_DIR + r"\pending\imported_from_endnote.bib"
DEFAULT_MANIFEST = DEFAULT_STORE_DIR + r"\manifest.yaml"
DEFAULT_QUARANTINE = DEFAULT_STORE_DIR + r"\quarantine"

LOAD_BEARING_FIELDS = ['author', 'title', 'year', 'journal', 'booktitle',
                       'volume', 'number', 'pages', 'doi', 'url']

# Ref types that legitimately may lack an external authoritative source.
# Used to recommend the human-attested path when --attest is plausible.
NO_EXTERNAL_SOURCE_TYPES = {
    'misc', 'unpublished', 'video', 'lecture', 'personal-communication',
    'sponsor-restricted',
}


def normalize_doi(s):
    if not s:
        return ''
    s = s.strip().lower()
    s = re.sub(r'^https?://(dx\.)?doi\.org/', '', s)
    s = re.sub(r'^doi:\s*', '', s)
    return s


def parse_bib(path):
    p = Path(path)
    if not p.exists():
        return {}
    text = p.read_text(encoding='utf-8')
    entries = {}
    entry_pat = re.compile(
        r'@(\w+)\s*\{\s*([^,\s]+)\s*,\s*((?:[^{}]|\{(?:[^{}]|\{[^{}]*\})*\})*)\s*\}',
        re.DOTALL,
    )
    field_pat = re.compile(
        r'(\w+)\s*=\s*(\{(?:[^{}]|\{[^{}]*\})*\}|"[^"]*"|\w+)',
    )
    for m in entry_pat.finditer(text):
        etype = m.group(1).lower()
        bibkey = m.group(2)
        body = m.group(3)
        fields = {}
        raw_fields = {}
        for fm in field_pat.finditer(body):
            fname = fm.group(1).lower()
            fval = fm.group(2)
            raw_fields[fname] = fval
            if fval.startswith('{') and fval.endswith('}'):
                fval = fval[1:-1]
            elif fval.startswith('"') and fval.endswith('"'):
                fval = fval[1:-1]
            fields[fname] = fval.strip()
        entries[bibkey] = {
            'type': etype,
            'fields': fields,
            'raw_fields': raw_fields,
            'raw_entry': m.group(0),
        }
    return entries


def normalize_compare(s):
    if s is None:
        return ''
    s = str(s)
    s = re.sub(r"\{\\[`'\"\^~=.]([A-Za-z])\}", r'\1', s)
    s = re.sub(r"\\[`'\"\^~=.]([A-Za-z])", r'\1', s)
    s = s.replace('{', '').replace('}', '')
    s = unicodedata.normalize('NFKD', s)
    s = ''.join(c for c in s if not unicodedata.combining(c))
    s = re.sub(r'[‐‑‒–—−]', '-', s)
    s = re.sub(r'[‘’‚‛]', "'", s)
    s = re.sub(r'[“”„‟]', '"', s)
    s = re.sub(r'\s+', ' ', s).strip().lower()
    return s


def field_match(claimed, canonical):
    a = normalize_compare(claimed)
    b = normalize_compare(canonical)
    if not a and not b:
        return True
    if not a or not b:
        return False
    if a == b:
        return True
    if a in b or b in a:
        return True
    return False


def step0_doi_dedup(candidate_doi, approved, pending):
    canon = normalize_doi(candidate_doi)
    if not canon:
        return {'status': 'NO-DOI'}
    approved_hits = []
    for bk, e in approved.items():
        if normalize_doi(e['fields'].get('doi', '')) == canon:
            approved_hits.append(bk)
    pending_hits = []
    for bk, e in pending.items():
        if bk in approved:
            continue
        if normalize_doi(e['fields'].get('doi', '')) == canon:
            pending_hits.append(bk)
    if approved_hits:
        return {'status': 'DUPLICATE-OF-APPROVED', 'bibkeys': approved_hits,
                'doi': canon}
    if len(pending_hits) >= 2:
        return {'status': 'DEDUP-NEEDED-IN-PENDING', 'bibkeys': pending_hits,
                'doi': canon}
    if len(pending_hits) == 1:
        return {'status': 'PENDING-CANDIDATE', 'bibkeys': pending_hits,
                'doi': canon}
    return {'status': 'NOT-IN-STORE', 'doi': canon}


def load_evidence(args):
    canonical = {}
    if args.evidence_json:
        data = json.loads(Path(args.evidence_json).read_text(encoding='utf-8'))
        if 'fields' in data:
            canonical = dict(data['fields'])
        else:
            canonical = dict(data)
    for f in (args.field or []):
        if '=' not in f:
            raise SystemExit(f'--field expects key=value, got: {f}')
        k, v = f.split('=', 1)
        canonical[k.strip().lower()] = v.strip()
    evidence_urls = []
    if args.evidence_url:
        evidence_urls.extend(args.evidence_url)
    if args.evidence_json:
        data = json.loads(Path(args.evidence_json).read_text(encoding='utf-8'))
        if isinstance(data, dict) and 'evidence_urls' in data:
            evidence_urls.extend(data['evidence_urls'])
    return canonical, evidence_urls


def compare_fields(candidate_entry, canonical):
    claimed = candidate_entry.get('fields', {}) if candidate_entry else {}
    results = {}
    for f in LOAD_BEARING_FIELDS:
        c = canonical.get(f)
        if c is None:
            continue
        claimed_val = claimed.get(f, '')
        if field_match(claimed_val, c):
            status = 'OK'
        elif not normalize_compare(claimed_val):
            status = 'ENRICH'
        else:
            status = 'DIFF'
        results[f] = {
            'claimed': claimed_val,
            'canonical': c,
            'match': status == 'OK',
            'status': status,
        }
    return results


def render_comparison_table(results):
    if not results:
        return '  (no fields supplied by agent for comparison)'
    out = []
    out.append(f'  {"field":<10} {"status":<6}  claimed vs canonical')
    for fname, r in results.items():
        flag = r.get('status', 'OK' if r['match'] else 'DIFF')
        claimed = (r['claimed'] or '(empty)')[:50]
        canon = (r['canonical'] or '(empty)')[:50]
        out.append(f'  {fname:<10} {flag:<6}  "{claimed}"')
        out.append(f'  {"":10} {"":6}    -> "{canon}"')
    return '\n'.join(out)


def serialize_bib_entry(bibkey, entry):
    if 'raw_entry' in entry and entry['raw_entry']:
        return entry['raw_entry']
    fields = entry.get('fields', {})
    lines = [f'@{entry.get("type", "misc")}{{{bibkey},']
    for k, v in fields.items():
        lines.append(f'  {k} = {{{v}}},')
    lines.append('}')
    return '\n'.join(lines)


def append_to_approved(approved_path, bib_text):
    p = Path(approved_path)
    existing = p.read_text(encoding='utf-8') if p.exists() else ''
    if not existing.endswith('\n'):
        existing += '\n'
    new = existing + '\n' + bib_text.rstrip() + '\n'
    p.write_text(new, encoding='utf-8')


def append_manifest_entry(manifest_path, entry_yaml):
    p = Path(manifest_path)
    existing = p.read_text(encoding='utf-8') if p.exists() else ''
    if not existing.endswith('\n'):
        existing += '\n'
    new = existing + '\n' + entry_yaml.rstrip() + '\n'
    p.write_text(new, encoding='utf-8')


def update_manifest_entry_inplace(manifest_path, bibkey, field_updates):
    p = Path(manifest_path)
    text = p.read_text(encoding='utf-8')
    block_re = re.compile(
        r'(^\s*- bibkey:\s*' + re.escape(bibkey) + r'\s*$)(.*?)(?=^\s*- bibkey:|\Z)',
        re.DOTALL | re.MULTILINE,
    )
    m = block_re.search(text)
    if not m:
        return False
    header = m.group(1)
    body = m.group(2)
    updated_body = body
    for field, new_value in field_updates.items():
        field_re = re.compile(
            r'(^\s*' + re.escape(field) + r':\s*)("[^"]*"|\S+)(\s*(?:#[^\n]*)?$)',
            re.MULTILINE,
        )
        if field_re.search(updated_body):
            updated_body = field_re.sub(
                lambda mm: f'{mm.group(1)}"{new_value}"{mm.group(3)}',
                updated_body, count=1,
            )
        else:
            indent_m = re.search(r'^(\s+)\S', body, re.MULTILINE)
            indent = indent_m.group(1) if indent_m else '    '
            insertion = f'{indent}{field}: "{new_value}"\n'
            updated_body = updated_body.rstrip('\n') + '\n' + insertion
    new_text = text[:m.start()] + header + updated_body + text[m.end():]
    p.write_text(new_text, encoding='utf-8')
    return True


def build_manifest_yaml_block(bibkey, mode, verified_by, evidence_urls,
                              confidence, primary_source, notes,
                              attested_by=None, attestation_rationale=None,
                              evidence_local=None):
    today = date.today().isoformat()
    lines = [
        f'  - bibkey: {bibkey}',
        f'    verified: true',
        f'    verification_mode: {mode}',
        f'    verified_date: "{today}"',
    ]
    if mode == 'human-attested':
        lines.append(f'    attested_by: {attested_by}')
        lines.append(f'    attested_date: "{today}"')
        rationale = (attestation_rationale or '').replace('\n', '\n      ')
        lines.append(f'    attestation_rationale: |')
        lines.append(f'      {rationale}')
        if evidence_local:
            lines.append(f'    evidence_local: "{evidence_local}"')
        lines.append(f'    pending_byzantine_verification: false')
    else:
        lines.append(f'    verified_by:')
        for vb in (verified_by or ['claude-opus-4-7']):
            lines.append(f'      - {vb}')
        if primary_source:
            lines.append(f'    primary_source: "{primary_source}"')
        lines.append(f'    evidence_urls:')
        for u in (evidence_urls or []):
            lines.append(f'      - "{u}"')
        if not evidence_urls:
            lines.append(f'      []')
        lines.append(f'    consensus: "1/1"')
        lines.append(f'    confidence: {confidence}')
        lines.append(f'    pending_byzantine_verification: true')
    if notes:
        notes_clean = notes.replace('\n', ' ').strip()
        lines.append(f'    notes: "{notes_clean}"')
    lines.append(f'    revalidate_after: null')
    return '\n'.join(lines)


def quarantine_dup(quarantine_dir, survivor_bibkey, dup_bibkey, dup_entry, doi, transcript):
    qdir = Path(quarantine_dir)
    qdir.mkdir(parents=True, exist_ok=True)
    fname = f'duplicate-of-{survivor_bibkey}--{dup_bibkey}.md'
    today = date.today().isoformat()
    md = (
        f'# Quarantined duplicate: @{dup_bibkey}\n\n'
        f'**Survivor:** @{survivor_bibkey}\n'
        f'**DOI:** {doi}\n'
        f'**Quarantined:** {today}\n'
        f'**Reason:** duplicate-of-pending-DOI -> deduplication via Step 0a\n\n'
        f'## Original pending bib entry\n\n'
        f'```bibtex\n{serialize_bib_entry(dup_bibkey, dup_entry)}\n```\n\n'
        f'## Verification transcript\n\n'
        f'{transcript or "(no transcript supplied)"}\n'
    )
    (qdir / fname).write_text(md, encoding='utf-8')
    return qdir / fname


def scan_and_print_stale(manifest_path):
    p = Path(manifest_path)
    if not p.exists():
        print(f'manifest not found: {manifest_path}', file=sys.stderr)
        return
    text = p.read_text(encoding='utf-8')
    today = date.today().isoformat()
    pattern = re.compile(
        r'- bibkey:\s*(\S+)(.*?)(?=^\s*- bibkey:|\Z)',
        re.DOTALL | re.MULTILINE,
    )
    print(f'refverify.py --list-stale  (today: {today})')
    print(f'  manifest: {manifest_path}')
    print()
    stale = []
    for m in pattern.finditer(text):
        bibkey = m.group(1).strip()
        body = m.group(2)
        rev_m = re.search(r'revalidate_after:\s*["\']?([^"\'\s#]+)["\']?', body)
        if not rev_m:
            continue
        rev = rev_m.group(1).strip()
        if rev in ('null', '~', ''):
            continue
        if rev <= today:
            mode_m = re.search(r'verification_mode:\s*(\S+)', body)
            ver_m = re.search(r'version_used:\s*["\']?([^"\']+)["\']?', body)
            stale.append({
                'bibkey': bibkey,
                'revalidate_after': rev,
                'verification_mode': mode_m.group(1) if mode_m else '?',
                'version_used': ver_m.group(1) if ver_m else None,
            })
    if not stale:
        print('No stale entries. Manifest is fresh.')
        return
    print(f'Found {len(stale)} stale entries (revalidate_after <= today):')
    for s in stale:
        soft = f'  software v{s["version_used"]}' if s['version_used'] else ''
        print(f'  @{s["bibkey"]:32s}  revalidate_after={s["revalidate_after"]}  '
              f'mode={s["verification_mode"]}{soft}')
    print()
    print('Refresh workflow (software cites):')
    print('  1. Agent: WebSearch upstream release page for current canonical version.')
    print('  2. refverify.py --candidate-bibkey <key> \\')
    print('       --field current_version=<new> --field version_checked_date=' + today + ' \\')
    print('       --evidence-url <upstream-release-url> --promote')
    print('  3. Confirm manifest updated; new revalidate_after auto-set by promote.')


def main():
    ap = argparse.ArgumentParser(
        description='R019 /refverify -- single-model triple-check + DOI dedup (MVP).'
    )
    ap.add_argument('--candidate-bibkey',
                    help='Bibkey of a candidate already in pending/ to verify.')
    ap.add_argument('--candidate-doi',
                    help='DOI of the candidate ref (used for Step 0 dedup).')
    ap.add_argument('--candidate-bib',
                    help='Path to a small .bib file containing the candidate entry '
                         '(use when the candidate is not yet in the pending store).')
    ap.add_argument('--field', action='append',
                    help='Canonical field key=value, repeatable. The agent fills these '
                         'from authoritative external sources (WebSearch/WebFetch).')
    ap.add_argument('--evidence-json',
                    help='Path to a JSON file with {"fields": {...}, "evidence_urls": [...]}.')
    ap.add_argument('--evidence-url', action='append',
                    help='Authoritative source URL, repeatable. R019 allowlist applies.')
    ap.add_argument('--verified-by', default='claude-opus-4-7',
                    help='Model identifier of the verifying agent (default: claude-opus-4-7).')
    ap.add_argument('--confidence', default='high', choices=['high', 'medium', 'low'])
    ap.add_argument('--primary-source', help='Primary source identifier (DOI, ISBN, URL).')
    ap.add_argument('--notes', default='', help='Free-form notes to include in manifest.')
    ap.add_argument('--promote', action='store_true',
                    help='On MATCH, promote the candidate to approved.bib + manifest.yaml.')
    ap.add_argument('--attest', action='store_true',
                    help='Human-attested verification path (R019 §5.1). '
                         'Requires --attested-by and --attestation-rationale.')
    ap.add_argument('--attested-by',
                    help='Human identifier (e.g., paulwach@arizona.edu). '
                         'Required when --attest is set. Agents cannot self-attest.')
    ap.add_argument('--attestation-rationale',
                    help='Specific reason external verification is not possible. '
                         'Required when --attest is set.')
    ap.add_argument('--attestation-evidence-local',
                    help='Optional path to a local copy of the source.')
    ap.add_argument('--no-external-source', action='store_true',
                    help='Mark the candidate as having no authoritative external source. '
                         'Triggers a NO-EXTERNAL-SOURCE recommendation to use --attest.')
    ap.add_argument('--approved-store', default=DEFAULT_APPROVED)
    ap.add_argument('--pending-store', default=DEFAULT_PENDING)
    ap.add_argument('--manifest', default=DEFAULT_MANIFEST)
    ap.add_argument('--quarantine-dir', default=DEFAULT_QUARANTINE)
    ap.add_argument('--list-stale', action='store_true',
                    help='Scan manifest.yaml for entries past their revalidate_after date '
                         'and print them. Use this to find software cites and in-press refs '
                         'that need a current_version refresh or full re-verification.')
    ap.add_argument('--refresh', action='store_true',
                    help='Update an EXISTING manifest entry in-place with --field values. '
                         'Use for software-version refresh (current_version, '
                         'version_checked_date) or any other field touch-up. Does NOT touch '
                         'approved.bib. Requires --candidate-bibkey and one or more --field.')
    args = ap.parse_args()

    if args.list_stale:
        scan_and_print_stale(args.manifest)
        sys.exit(0)

    if args.refresh:
        if not args.candidate_bibkey or not args.field:
            print('ERROR: --refresh requires --candidate-bibkey AND one or more --field key=value.',
                  file=sys.stderr)
            sys.exit(4)
        updates = {}
        for f in args.field:
            if '=' not in f:
                print(f'ERROR: --field "{f}" missing "=" separator.', file=sys.stderr)
                sys.exit(4)
            k, v = f.split('=', 1)
            updates[k.strip()] = v.strip()
        updates.setdefault('version_checked_date', date.today().isoformat())
        ok = update_manifest_entry_inplace(args.manifest, args.candidate_bibkey, updates)
        if not ok:
            print(f'ERROR: bibkey @{args.candidate_bibkey} not found in manifest.', file=sys.stderr)
            sys.exit(5)
        print(f'[REFRESH-OK] @{args.candidate_bibkey} manifest updated in-place:')
        for k, v in updates.items():
            print(f'  {k}: "{v}"')
        sys.exit(0)

    approved = parse_bib(args.approved_store)
    pending = parse_bib(args.pending_store)
    candidate_bib_extra = parse_bib(args.candidate_bib) if args.candidate_bib else {}

    candidate_bibkey = args.candidate_bibkey
    candidate_entry = None
    if candidate_bibkey:
        candidate_entry = (
            approved.get(candidate_bibkey)
            or pending.get(candidate_bibkey)
            or candidate_bib_extra.get(candidate_bibkey)
        )
        if not candidate_entry:
            print(f'ERROR: candidate bibkey @{candidate_bibkey} not found in '
                  f'approved.bib, pending/, or --candidate-bib.', file=sys.stderr)
            sys.exit(3)

    candidate_doi = args.candidate_doi
    if not candidate_doi and candidate_entry:
        candidate_doi = candidate_entry['fields'].get('doi', '')

    print('refverify.py -- R019 single-model triple-check (MVP)')
    print(f'  candidate bibkey: @{candidate_bibkey or "(unset)"}')
    print(f'  candidate doi:    {candidate_doi or "(unset)"}')
    print(f'  approved store:   {args.approved_store}  ({len(approved)} entries)')
    print(f'  pending store:    {args.pending_store}  ({len(pending)} entries)')
    print()

    # --- Attestation path short-circuits the dedup/comparison flow. ---
    if args.attest:
        if not args.attested_by or not args.attestation_rationale:
            print('ERROR: --attest requires --attested-by AND --attestation-rationale.',
                  file=sys.stderr)
            sys.exit(4)
        # Reject obviously agent-shaped attesters. Real humans only.
        bad = ('claude', 'gpt', 'gemini', 'codex', 'agent', 'bot', 'sonnet', 'opus')
        ab_lower = args.attested_by.lower()
        if any(b in ab_lower for b in bad):
            print(f'ERROR: --attested-by="{args.attested_by}" looks like an agent identifier. '
                  f'Human-attested verification requires a real human (R019 §5.1).',
                  file=sys.stderr)
            sys.exit(4)
        if not candidate_bibkey:
            print('ERROR: --attest requires --candidate-bibkey.', file=sys.stderr)
            sys.exit(4)
        print(f'[ATTEST] {candidate_bibkey} attested by {args.attested_by}')
        if not args.promote:
            print('Dry-run (no --promote). Manifest entry that WOULD be written:')
            print(build_manifest_yaml_block(
                candidate_bibkey, 'human-attested',
                None, None, args.confidence, None, args.notes,
                args.attested_by, args.attestation_rationale,
                args.attestation_evidence_local))
            sys.exit(0)
        # Promote: add to approved.bib (if not already there) + manifest.
        if candidate_bibkey not in approved:
            entry = candidate_entry
            append_to_approved(args.approved_store,
                               serialize_bib_entry(candidate_bibkey, entry))
        append_manifest_entry(args.manifest, build_manifest_yaml_block(
            candidate_bibkey, 'human-attested',
            None, None, args.confidence, None, args.notes,
            args.attested_by, args.attestation_rationale,
            args.attestation_evidence_local))
        print(f'[ATTEST-OK] @{candidate_bibkey} promoted via human-attested.')
        sys.exit(0)

    # --- Step 0 / 0a: DOI dedup pre-check. ---
    dedup = step0_doi_dedup(candidate_doi, approved, pending) if candidate_doi else \
            {'status': 'NO-DOI'}
    print(f'[Step 0] DOI dedup pre-check: {dedup["status"]}')
    if dedup['status'] == 'DUPLICATE-OF-APPROVED':
        print(f'  DOI {dedup["doi"]} already approved as: ' +
              ', '.join('@' + b for b in dedup['bibkeys']))
        print('  Reuse the existing approved bibkey. No verification needed.')
        sys.exit(0)
    if dedup['status'] == 'DEDUP-NEEDED-IN-PENDING':
        print(f'  DOI {dedup["doi"]} appears in MULTIPLE pending entries: ' +
              ', '.join('@' + b for b in dedup['bibkeys']))
        print('  Step 0a: verify canonical metadata once, then designate a survivor.')
        if not candidate_bibkey:
            print('  ERROR: must specify --candidate-bibkey (the prospective survivor) '
                  'to run dedup.', file=sys.stderr)
            sys.exit(5)
        if candidate_bibkey not in dedup['bibkeys']:
            print(f'  ERROR: --candidate-bibkey @{candidate_bibkey} is not among the '
                  f'same-DOI pending set.', file=sys.stderr)
            sys.exit(5)
    elif dedup['status'] == 'PENDING-CANDIDATE':
        print(f'  DOI {dedup["doi"]} matches one pending entry: @{dedup["bibkeys"][0]}')
        if not candidate_bibkey:
            candidate_bibkey = dedup['bibkeys'][0]
            candidate_entry = pending[candidate_bibkey]
            print(f'  Adopting @{candidate_bibkey} as the candidate.')
    print()

    # --- NO-EXTERNAL-SOURCE branch routes to attestation. ---
    if args.no_external_source:
        print('[NO-EXTERNAL-SOURCE] Candidate ref-type plausibly lacks an authoritative '
              'external source.')
        print('  Cannot run the single-model triple-check workflow.')
        print('  Route via the human-attested path (R019 §5.1):')
        print('    refverify.py --candidate-bibkey <bk> --attest \\')
        print('      --attested-by <human-id> \\')
        print("      --attestation-rationale '<specific reason external verification is impossible>'")
        print('  The agent CANNOT self-attest.')
        sys.exit(6)

    # --- Steps 1-3: field comparison. ---
    canonical, evidence_urls = load_evidence(args)
    if not canonical:
        print('[Step 1-3] No canonical fields supplied. The agent must run')
        print('  WebSearch + WebFetch against the R019 allowlist, then pass results in')
        print('  via --field key=value (repeatable) or --evidence-json <path>.')
        print('  Required load-bearing fields:', ', '.join(LOAD_BEARING_FIELDS))
        sys.exit(7)

    print(f'[Step 1-3] Field comparison against agent-fetched canonical:')
    results = compare_fields(candidate_entry or {}, canonical)
    print(render_comparison_table(results))
    print()

    if not results:
        print('[Verdict] INDETERMINATE: no overlapping fields between candidate and canonical.')
        sys.exit(8)

    diffs = [f for f, r in results.items() if r.get('status') == 'DIFF']
    enrichments = [f for f, r in results.items() if r.get('status') == 'ENRICH']
    if diffs:
        print(f'[Verdict] MISMATCH: {len(diffs)} field(s) differ: {", ".join(diffs)}')
        print('  Promote BLOCKED. Either fix the candidate fields against the canonical')
        print('  source, or quarantine if the canonical source contradicts the candidate.')
        sys.exit(9)
    if enrichments:
        print(f'[Verdict] MATCH-WITH-ENRICHMENT: {len(enrichments)} field(s) added from canonical: {", ".join(enrichments)}')
        print('  Promotion proceeds; missing fields are filled from canonical, not contradicted.')

    print(f'[Verdict] MATCH: all {len(results)} compared load-bearing fields agree.')
    if not args.promote:
        print()
        print('Dry-run (no --promote). To promote, re-run with --promote.')
        if candidate_bibkey:
            print('Manifest entry that WOULD be written:')
            print(build_manifest_yaml_block(
                candidate_bibkey, 'single-model-triple-check',
                [args.verified_by], evidence_urls, args.confidence,
                args.primary_source, args.notes))
        sys.exit(0)

    # --- Step 4: promote candidate. ---
    if not candidate_bibkey:
        print('ERROR: --promote requires --candidate-bibkey.', file=sys.stderr)
        sys.exit(10)

    # Dedup case: quarantine the losers.
    if dedup['status'] == 'DEDUP-NEEDED-IN-PENDING':
        losers = [b for b in dedup['bibkeys'] if b != candidate_bibkey]
        for loser in losers:
            qp = quarantine_dup(args.quarantine_dir, candidate_bibkey,
                                loser, pending.get(loser, {}),
                                dedup['doi'],
                                f'Verified canonical metadata via single-model triple-check '
                                f'on {date.today().isoformat()}.')
            print(f'  Quarantined @{loser} -> {qp}')

    if candidate_bibkey not in approved:
        append_to_approved(args.approved_store,
                           serialize_bib_entry(candidate_bibkey, candidate_entry))
        print(f'  Appended @{candidate_bibkey} to {args.approved_store}')
    append_manifest_entry(args.manifest, build_manifest_yaml_block(
        candidate_bibkey, 'single-model-triple-check',
        [args.verified_by], evidence_urls, args.confidence,
        args.primary_source, args.notes))
    print(f'  Appended manifest entry to {args.manifest}')
    print(f'[PROMOTED] @{candidate_bibkey}')
    sys.exit(0)


if __name__ == '__main__':
    main()
