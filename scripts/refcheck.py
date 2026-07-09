#!/usr/bin/env python3
"""R019 reference verification gate.

Checks that every bibliography entry in a manuscript exists in the portfolio
approved-references store (and optional local overlay). Exits non-zero on
miss in --strict mode (default). See:
docs/proposed_R019_references_verification_gate.md
"""

import argparse
import re
import sys
import unicodedata
from pathlib import Path


def normalize_name(s):
    if not s:
        return ''
    s = re.sub(r"\{\\[`'\"\^~=.]([A-Za-z])\}", r'\1', s)
    s = re.sub(r"\\[`'\"\^~=.]([A-Za-z])", r'\1', s)
    s = s.replace('{', '').replace('}', '')
    s = unicodedata.normalize('NFKD', s)
    s = ''.join(c for c in s if not unicodedata.combining(c))
    return s.lower().strip()

DEFAULT_STORE = r"C:\Users\pfwac\OneDrive - University of Arizona\Documents\04 Resource Library\00 Verified References\approved.bib"
DEFAULT_PENDING_STORE = r"C:\Users\pfwac\OneDrive - University of Arizona\Documents\04 Resource Library\00 Verified References\pending\imported_from_endnote.bib"


def parse_bib(path):
    text = Path(path).read_text(encoding='utf-8')
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
        for fm in field_pat.finditer(body):
            fname = fm.group(1).lower()
            fval = fm.group(2)
            if fval.startswith('{') and fval.endswith('}'):
                fval = fval[1:-1]
            elif fval.startswith('"') and fval.endswith('"'):
                fval = fval[1:-1]
            fields[fname] = fval.strip()
        entries[bibkey] = {'type': etype, 'fields': fields}
    return entries


def first_surname(authors_field):
    surnames = all_surnames(authors_field)
    return surnames[0] if surnames else None


def all_surnames(authors_field):
    if not authors_field:
        return []
    s = authors_field.strip()
    m = re.match(r'^\{(.+)\}$', s)
    if m:
        return [m.group(1).strip()]
    out = []
    for chunk in s.split(' and '):
        c = chunk.strip()
        if c.startswith('{') and c.endswith('}'):
            c = c[1:-1].strip()
        if ',' in c:
            out.append(c.split(',')[0].strip())
        else:
            parts = c.split()
            if parts:
                out.append(parts[-1])
    return out


def index_by_author_year(entries):
    idx = {}
    for bibkey, e in entries.items():
        f = e['fields']
        year = f.get('year', '').strip()
        if not year:
            continue
        author_names = all_surnames(f.get('author', ''))
        editor_names = all_surnames(f.get('editor', ''))
        names = author_names + editor_names
        aliases = [a.strip() for a in f.get('aliases', '').split(',') if a.strip()]
        for s in names + aliases:
            normalized = normalize_name(s)
            if not normalized:
                continue
            key = (normalized, year)
            if bibkey not in idx.setdefault(key, []):
                idx[key].append(bibkey)
            first_word = normalized.split()[0]
            if first_word and first_word != normalized:
                fk = (first_word, year)
                if bibkey not in idx.setdefault(fk, []):
                    idx[fk].append(bibkey)
    return idx


def extract_bibkeys_from_md(text):
    return set(re.findall(r'(?<![\w])@([A-Za-z][\w]+)', text))


def extract_bib_section(text):
    m = re.search(
        r'^#{1,3}\s*References\s*$(.+?)(?=^#{1,3}\s|\Z)',
        text,
        re.DOTALL | re.MULTILINE,
    )
    if not m:
        return []
    section = m.group(1)
    out = []
    for line_m in re.finditer(
        r'^\s*(\d+)\.\s+(.+?)(?=^\s*\d+\.\s|\Z)',
        section,
        re.DOTALL | re.MULTILINE,
    ):
        out.append({'num': int(line_m.group(1)), 'text': ' '.join(line_m.group(2).split())})
    return out


_TITLE_TOKEN_RE = re.compile(r'[A-Za-zÀ-ſ]{4,}')
_TITLE_STOPWORDS = {
    'this', 'that', 'with', 'from', 'into', 'using', 'toward', 'towards',
    'their', 'these', 'those', 'where', 'which', 'while', 'between',
    'introduction', 'mathematical', 'theory', 'systems', 'system', 'engineering',
    'proceedings', 'international', 'conference', 'journal', 'edition', 'second',
    'third', 'fourth', 'first', 'volume', 'available', 'online',
}


def _title_tokens(text):
    return {t.lower() for t in _TITLE_TOKEN_RE.findall(text or '')} - _TITLE_STOPWORDS


def pick_best_by_title(candidates, entries_dict, manuscript_bib_text):
    bib_tokens = _title_tokens(manuscript_bib_text)
    best = candidates[0]
    best_score = -1
    for c in candidates:
        c_title = entries_dict.get(c, {}).get('fields', {}).get('title', '')
        c_tokens = _title_tokens(c_title)
        score = len(bib_tokens & c_tokens)
        if score > best_score:
            best_score = score
            best = c
    return best


def extract_first_author_year(bib_text):
    year_m = re.search(r'\b(19|20)\d{2}\b', bib_text)
    year = year_m.group(0) if year_m else None

    first_chunk = bib_text.split(',')[0].strip()
    m = re.match(r"^(?:[A-Z]\.\s*(?:[A-Z]\.\s*)*)?([A-Za-zÀ-ſ][A-Za-zÀ-ſ0-9\-']+)", first_chunk)
    if m:
        return m.group(1), year
    return None, year


def main():
    ap = argparse.ArgumentParser(description='R019 references verification gate.')
    ap.add_argument('manuscript', help='Manuscript markdown file to check')
    ap.add_argument('--portfolio-store', default=DEFAULT_STORE,
                    help='Path to portfolio approved.bib')
    ap.add_argument('--local-store', help='Optional local overlay approved.bib path')
    ap.add_argument('--include-pending', action='store_true',
                    help='Also load pending/imported_from_endnote.bib; pending matches '
                         'report as PENDING (do not cause non-zero exit under --strict)')
    ap.add_argument('--pending-store', default=DEFAULT_PENDING_STORE,
                    help='Path to pending bib (used only when --include-pending is set)')
    mode = ap.add_mutually_exclusive_group()
    mode.add_argument('--strict', action='store_true',
                      help='Exit non-zero on any miss (default)')
    mode.add_argument('--advisory', action='store_true',
                      help='Exit 0 even on misses; print warnings only')
    ap.add_argument('--autoverify', action='store_true',
                    help='[stub] On miss, would auto-launch /refverify')
    ap.add_argument('--bibkey-mode', action='store_true',
                    help='Force pandoc @bibkey extraction mode')
    args = ap.parse_args()

    is_strict = not args.advisory

    portfolio = parse_bib(args.portfolio_store)
    local = parse_bib(args.local_store) if args.local_store else {}
    approved_entries = {**portfolio, **local}
    approved_keys = set(approved_entries.keys())
    ay_idx_approved = index_by_author_year(approved_entries)

    pending_entries = {}
    pending_keys = set()
    ay_idx_pending = {}
    if args.include_pending:
        pending_entries = parse_bib(args.pending_store)
        pending_keys = set(pending_entries.keys()) - approved_keys
        pending_only = {k: v for k, v in pending_entries.items() if k in pending_keys}
        ay_idx_pending = index_by_author_year(pending_only)

    print('refcheck.py — R019 reference verification gate')
    print(f'  manuscript:      {args.manuscript}')
    print(f'  portfolio store: {args.portfolio_store}')
    print(f'                   ({len(portfolio)} approved entries)')
    if args.local_store:
        print(f'  local store:     {args.local_store}')
        print(f'                   ({len(local)} entries)')
    if args.include_pending:
        print(f'  pending store:   {args.pending_store}')
        print(f'                   ({len(pending_entries)} pending entries, {len(pending_keys)} unique vs approved)')
    print(f'  mode:            {"STRICT (exit nonzero on miss)" if is_strict else "ADVISORY (warnings only)"}')
    print()

    ms_text = Path(args.manuscript).read_text(encoding='utf-8')

    bibkeys_in_text = extract_bibkeys_from_md(ms_text)
    bib_entries = extract_bib_section(ms_text)

    use_bibkey_mode = args.bibkey_mode or (bibkeys_in_text and not bib_entries)
    missing = []
    pending_hits = []
    approved_hits = []

    if use_bibkey_mode:
        print(f'Mode: pandoc @bibkey')
        print(f'Found {len(bibkeys_in_text)} cite keys.')
        for k in sorted(bibkeys_in_text):
            if k in approved_keys:
                print(f'  OK (approved) @{k}')
                approved_hits.append(k)
            elif args.include_pending and k in pending_keys:
                print(f'  ?? (pending)  @{k}')
                pending_hits.append(k)
            else:
                print(f'  MISS          @{k}')
                missing.append(k)
        total = len(bibkeys_in_text)
    else:
        print('Mode: IEEE numbered bibliography')
        if not bib_entries:
            print('  No bibliography section found (looked for ^#{1,3} References).')
            print('  If this manuscript splits body from refs, run refcheck on the refs file.')
            sys.exit(0)
        print(f'Found {len(bib_entries)} bibliography entries.')
        for be in bib_entries:
            surname, year = extract_first_author_year(be['text'])
            preview = (be['text'][:75] + '...') if len(be['text']) > 75 else be['text']
            if surname and year:
                norm = normalize_name(surname)
                cands_a = ay_idx_approved.get((norm, year), [])
                cands_p = ay_idx_pending.get((norm, year), []) if args.include_pending else []
                if cands_a:
                    bk = pick_best_by_title(cands_a, approved_entries, be['text']) if len(cands_a) > 1 else cands_a[0]
                    suffix = '' if len(cands_a) == 1 else f' (+{len(cands_a)-1} more candidates; tiebreak by title)'
                    print(f'  OK (approved) #{be["num"]:2d}  -> {bk:32s} ({surname}, {year}){suffix}')
                    approved_hits.append({'num': be['num'], 'bibkey': bk, 'text': be['text']})
                elif cands_p:
                    bk = pick_best_by_title(cands_p, pending_entries, be['text']) if len(cands_p) > 1 else cands_p[0]
                    suffix = '' if len(cands_p) == 1 else f' (+{len(cands_p)-1} more candidates; tiebreak by title)'
                    print(f'  ?? (pending)  #{be["num"]:2d}  -> {bk:32s} ({surname}, {year}){suffix}')
                    pending_hits.append({'num': be['num'], 'bibkey': bk, 'text': be['text']})
                else:
                    print(f'  MISS          #{be["num"]:2d}  ?? {surname} {year} | {preview}')
                    missing.append(be)
            else:
                print(f'  ???           #{be["num"]:2d}  cannot extract surname/year | {preview}')
                missing.append(be)
        total = len(bib_entries)

    print()
    if args.include_pending:
        print(f'Summary: {len(approved_hits)} approved, {len(pending_hits)} pending, '
              f'{len(missing)} missing  (total: {total})')
    else:
        print(f'Summary: {total - len(missing)}/{total} matched, {len(missing)} missing')

    if args.autoverify and missing:
        print()
        print(f'[--autoverify] {len(missing)} missing entries should be routed through /refverify:')
        for m in missing:
            if isinstance(m, dict):
                print(f'  /refverify (manuscript line #{m.get("num", "?")}) -- {m.get("text", "")[:80]}')
            else:
                print(f'  /refverify @{m}')

    sys.exit(1 if (missing and is_strict) else 0)


if __name__ == '__main__':
    main()
