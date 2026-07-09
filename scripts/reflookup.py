#!/usr/bin/env python3
"""R019 /reflookup -- search approved + pending reference stores.

Returns ranked candidate refs matching a topic, author surname, year, or DOI,
across the portfolio approved.bib AND pending/imported_from_endnote.bib.
The drafting agent invokes this BEFORE writing any citation, to prefer reuse
of an existing approved entry over running /refverify on something new.

See: docs/proposed_R019_references_verification_gate.md §6 (Companion commands)
"""

import argparse
import re
import sys
import unicodedata
from pathlib import Path

DEFAULT_APPROVED = r"C:\Users\pfwac\OneDrive - University of Arizona\Documents\04 Resource Library\00 Verified References\approved.bib"
DEFAULT_PENDING = r"C:\Users\pfwac\OneDrive - University of Arizona\Documents\04 Resource Library\00 Verified References\pending\imported_from_endnote.bib"


def normalize_name(s):
    if not s:
        return ''
    s = re.sub(r"\{\\[`'\"\^~=.]([A-Za-z])\}", r'\1', s)
    s = re.sub(r"\\[`'\"\^~=.]([A-Za-z])", r'\1', s)
    s = s.replace('{', '').replace('}', '')
    s = unicodedata.normalize('NFKD', s)
    s = ''.join(c for c in s if not unicodedata.combining(c))
    return s.lower().strip()


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
    if not authors_field:
        return None
    s = authors_field.strip()
    m = re.match(r'^\{(.+)\}$', s)
    if m:
        return m.group(1).strip()
    first = s.split(' and ')[0].strip()
    if first.startswith('{') and first.endswith('}'):
        first = first[1:-1].strip()
    if ',' in first:
        return first.split(',')[0].strip()
    parts = first.split()
    if parts:
        return parts[-1]
    return None


def normalize_doi(s):
    if not s:
        return ''
    s = s.strip().lower()
    s = re.sub(r'^https?://(dx\.)?doi\.org/', '', s)
    s = re.sub(r'^doi:\s*', '', s)
    return s


def one_line_summary(bibkey, entry):
    f = entry['fields']
    surname = first_surname(f.get('author', f.get('editor', ''))) or '?'
    year = f.get('year', '?')
    title = f.get('title', '').replace('\n', ' ').strip()
    if len(title) > 80:
        title = title[:77] + '...'
    venue = (
        f.get('journal')
        or f.get('booktitle')
        or f.get('howpublished')
        or f.get('publisher')
        or ''
    )
    venue = venue.replace('\n', ' ').strip()
    if len(venue) > 40:
        venue = venue[:37] + '...'
    parts = [f'{surname} {year}']
    if title:
        parts.append(f'"{title}"')
    if venue:
        parts.append(f'[{venue}]')
    return ' | '.join(parts)


def score_entry(entry, query, query_terms, want_doi, want_year, want_surname):
    f = entry['fields']
    score = 0
    hit_fields = []

    if want_doi:
        entry_doi = normalize_doi(f.get('doi', ''))
        if entry_doi and entry_doi == want_doi:
            return 10000, ['doi-exact']

    if want_surname and want_year:
        surname = normalize_name(first_surname(f.get('author', f.get('editor', ''))) or '')
        year = f.get('year', '').strip()
        if surname and year == want_year:
            if surname == want_surname or surname.startswith(want_surname):
                score += 500
                hit_fields.append('author+year')

    haystacks = {
        'title': f.get('title', ''),
        'author': f.get('author', '') + ' ' + f.get('editor', ''),
        'journal': f.get('journal', '') + ' ' + f.get('booktitle', '') + ' ' + f.get('publisher', ''),
        'keywords': f.get('keywords', ''),
        'abstract': f.get('abstract', ''),
        'bibkey': '',
    }

    bibkey_text = entry.get('_bibkey', '')

    field_weights = {
        'title': 30,
        'author': 20,
        'journal': 15,
        'keywords': 25,
        'abstract': 5,
    }

    for term in query_terms:
        if not term:
            continue
        nterm = term.lower()
        if nterm in bibkey_text.lower():
            score += 40
            hit_fields.append(f'bibkey~{nterm}')
        for field, text in haystacks.items():
            if not text:
                continue
            if nterm in text.lower():
                score += field_weights.get(field, 5)
                hit_fields.append(f'{field}~{nterm}')

    return score, hit_fields


def main():
    ap = argparse.ArgumentParser(
        description='R019 reference lookup -- search approved + pending stores.'
    )
    ap.add_argument('query', nargs='*', default=[],
                    help='Search terms. Can be free text, author surname, year, or DOI. '
                         'Optional if --doi, --author, --year, or --keyword is provided.')
    ap.add_argument('--approved-store', default=DEFAULT_APPROVED)
    ap.add_argument('--pending-store', default=DEFAULT_PENDING)
    ap.add_argument('--doi', help='Search by exact DOI match (short-circuit).')
    ap.add_argument('--author', help='Author surname (combine with --year for exact author+year match).')
    ap.add_argument('--year', help='Publication year (combine with --author).')
    ap.add_argument('--keyword', help='Exact keyword match against the "keywords" field.')
    ap.add_argument('--max-results', type=int, default=10)
    ap.add_argument('--approved-only', action='store_true',
                    help='Skip pending; search only approved.bib.')
    args = ap.parse_args()

    approved = parse_bib(args.approved_store)
    pending = parse_bib(args.pending_store) if not args.approved_only else {}

    for k, v in approved.items():
        v['_bibkey'] = k
    for k, v in pending.items():
        v['_bibkey'] = k

    pending_only = {k: v for k, v in pending.items() if k not in approved}

    query_str = ' '.join(args.query).strip()
    query_terms = [t for t in re.split(r'\s+', query_str) if t]

    if not query_str and not (args.doi or args.author or args.year or args.keyword):
        ap.error('provide query terms or at least one of --doi/--author/--year/--keyword')

    want_doi = normalize_doi(args.doi) if args.doi else ''
    if not want_doi:
        for t in query_terms:
            if '10.' in t and '/' in t:
                want_doi = normalize_doi(t)
                break

    want_year = args.year
    if not want_year:
        for t in query_terms:
            if re.fullmatch(r'(19|20)\d{2}', t):
                want_year = t
                break

    want_surname = normalize_name(args.author) if args.author else ''
    if args.keyword:
        query_terms.append(args.keyword)

    all_pool = []
    for k, v in approved.items():
        all_pool.append(('APPROVED', k, v))
    for k, v in pending_only.items():
        all_pool.append(('PENDING ', k, v))

    print(f'/reflookup -- query: "{query_str}"')
    if want_doi:
        print(f'  DOI filter:    {want_doi}')
    if want_surname and want_year:
        print(f'  author+year:   {want_surname} {want_year}')
    print(f'  approved pool: {len(approved)} entries')
    if not args.approved_only:
        print(f'  pending pool:  {len(pending_only)} entries')
    print()

    scored = []
    for status, bibkey, entry in all_pool:
        score, hits = score_entry(entry, query_str, query_terms,
                                  want_doi, want_year, want_surname)
        if score > 0:
            scored.append((score, status, bibkey, entry, hits))

    if want_doi:
        scored.sort(key=lambda r: (0 if r[1] == 'APPROVED' else 1, -r[0]))
    else:
        scored.sort(key=lambda r: (0 if r[1] == 'APPROVED' else 1, -r[0]))

    if not scored:
        print('No matches.')
        print()
        print('Next step: this looks like a new ref. Run /refverify to either')
        print('  (a) find a duplicate-of-approved via DOI dedup, or')
        print('  (b) start the single-model triple-check workflow.')
        sys.exit(2)

    n = min(args.max_results, len(scored))
    print(f'Top {n} of {len(scored)} matches:')
    print()
    pending_only_results = True
    for score, status, bibkey, entry, hits in scored[:n]:
        if status == 'APPROVED':
            pending_only_results = False
        summary = one_line_summary(bibkey, entry)
        hits_str = (','.join(hits[:4]) + ('...' if len(hits) > 4 else '')) if hits else '-'
        print(f'  [{status}] @{bibkey}')
        print(f'             {summary}')
        print(f'             score={score} hits={hits_str}')
        print()

    if pending_only_results:
        print('NOTE: all matches are in pending/. To use any of these in a manuscript,')
        print('      run /refverify <bibkey> first to promote it to approved.bib.')
    else:
        print('Prefer reuse of an APPROVED entry. Use the bibkey directly in your draft.')
    sys.exit(0)


if __name__ == '__main__':
    main()
