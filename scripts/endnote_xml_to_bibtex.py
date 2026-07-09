#!/usr/bin/env python3
"""Convert an EndNote XML export to BibTeX, with a companion pending-manifest.

Reads an EndNote v18+ XML export (the XML produced by File -> Export with
'EndNote XML' output style). Emits a BibTeX file and a pending-manifest YAML
that flags every entry as awaiting Byzantine verification per R019.

Usage:
    endnote_xml_to_bibtex.py <input.xml> <output.bib> <manifest.yaml>
"""

import re
import sys
import unicodedata
import xml.etree.ElementTree as ET
from collections import Counter
from pathlib import Path
from datetime import date


REFTYPE_TO_BIBTEX = {
    'Journal Article': 'article',
    'Conference Proceedings': 'inproceedings',
    'Conference Paper': 'inproceedings',
    'Book': 'book',
    'Book Section': 'incollection',
    'Edited Book': 'book',
    'Thesis': 'phdthesis',
    'Report': 'techreport',
    'Government Document': 'techreport',
    'Standard': 'techreport',
    'Web Page': 'misc',
    'Online Database': 'misc',
    'Generic': 'misc',
    'Electronic Article': 'article',
    'Unpublished Work': 'unpublished',
    'Film or Broadcast': 'misc',
    'Computer Program': 'misc',
    'Aggregated Database': 'misc',
    'Manuscript': 'unpublished',
}


def style_text(elem):
    if elem is None:
        return ''
    return ''.join(elem.itertext()).strip()


def get_child_text(parent, *path):
    cur = parent
    for tag in path:
        if cur is None:
            return ''
        cur = cur.find(tag)
    return style_text(cur)


def get_authors(record, kind='authors'):
    contributors = record.find('contributors')
    if contributors is None:
        return []
    group = contributors.find(kind)
    if group is None:
        return []
    return [style_text(a) for a in group.findall('author') if style_text(a)]


def clean_doi(s):
    if not s:
        return ''
    s = s.strip()
    s = re.sub(r'^https?://(?:dx\.)?doi\.org/', '', s)
    s = re.sub(r'^https?://doi-org\.ezproxy\.lib\.vt\.edu/', '', s)
    s = re.sub(r'^https?://doi[-.]org/', '', s)
    s = re.sub(r'^doi:\s*', '', s, flags=re.IGNORECASE)
    return s.strip()


def bib_escape(s):
    if not s:
        return ''
    s = s.replace('\r\n', ' ').replace('\n', ' ').replace('\r', ' ')
    s = re.sub(r'\s+', ' ', s).strip()
    s = s.replace('\\', '\\textbackslash{}')
    s = s.replace('{', '\\{').replace('}', '\\}')
    s = s.replace('&', '\\&').replace('%', '\\%').replace('$', '\\$')
    s = s.replace('#', '\\#').replace('_', '\\_')
    return s


def normalize_slug(s):
    if not s:
        return ''
    s = unicodedata.normalize('NFKD', s)
    s = ''.join(c for c in s if not unicodedata.combining(c))
    s = re.sub(r'[^A-Za-z0-9]+', '', s)
    return s.lower()


STOPWORDS = {
    'the', 'a', 'an', 'on', 'in', 'of', 'for', 'and', 'or', 'to', 'with',
    'using', 'toward', 'towards', 'into', 'from', 'by', 'as', 'at', 'is',
    'are', 'be', 'this', 'that', 'these', 'those', 'new', 'novel',
    'introduction', 'overview', 'study', 'review', 'analysis', 'case',
}


def first_meaningful_word(title):
    if not title:
        return ''
    for w in re.findall(r'[A-Za-z][A-Za-z0-9\-]*', title):
        slug = normalize_slug(w)
        if slug and slug not in STOPWORDS and len(slug) >= 3:
            return slug
    return ''


def first_surname(author_str):
    if not author_str:
        return ''
    if ',' in author_str:
        return author_str.split(',')[0].strip()
    parts = author_str.strip().split()
    return parts[-1] if parts else ''


def make_bibkey(authors, year, title, used):
    if authors:
        surname_slug = normalize_slug(first_surname(authors[0]))
    else:
        surname_slug = 'anon'
    if not surname_slug:
        surname_slug = 'anon'
    year_slug = year if re.match(r'^\d{4}$', year or '') else 'nd'
    word = first_meaningful_word(title) or 'paper'
    base = f'{surname_slug}{year_slug}{word}'[:60]
    bibkey = base
    n = 0
    while bibkey in used:
        n += 1
        bibkey = f'{base}{chr(ord("a") + n - 1)}'
        if n > 25:
            bibkey = f'{base}_{n}'
            if bibkey not in used:
                break
    return bibkey


def convert_record(record, used_keys):
    ref_type_el = record.find('ref-type')
    ref_type_name = ref_type_el.get('name', '') if ref_type_el is not None else ''
    bib_type = REFTYPE_TO_BIBTEX.get(ref_type_name, 'misc')

    title = get_child_text(record, 'titles', 'title')
    secondary = get_child_text(record, 'titles', 'secondary-title')
    journal = get_child_text(record, 'periodical', 'full-title') or secondary
    authors = get_authors(record, 'authors')
    editors = get_authors(record, 'secondary-authors') or get_authors(record, 'tertiary-authors')
    year = get_child_text(record, 'dates', 'year')
    volume = style_text(record.find('volume'))
    number = style_text(record.find('number'))
    pages = style_text(record.find('pages'))
    publisher = style_text(record.find('publisher'))
    address = style_text(record.find('pub-location'))
    edition = style_text(record.find('edition'))
    isbn = style_text(record.find('isbn'))
    doi_raw = style_text(record.find('electronic-resource-num'))
    doi = clean_doi(doi_raw)
    url = ''
    for u in record.findall('.//urls/related-urls/url'):
        cand = style_text(u)
        if cand and not cand.startswith('internal-pdf://'):
            url = cand
            break
    abstract = style_text(record.find('abstract'))
    keywords_list = [style_text(k) for k in record.findall('.//keywords/keyword') if style_text(k)]
    rec_number = style_text(record.find('rec-number'))

    bibkey = make_bibkey(authors or editors, year, title, used_keys)
    used_keys.add(bibkey)

    fields = []
    if authors:
        fields.append(('author', ' and '.join(authors)))
    if editors and bib_type in ('book', 'incollection', 'inproceedings'):
        fields.append(('editor', ' and '.join(editors)))
    if title:
        fields.append(('title', title))
    if bib_type == 'article' and journal:
        fields.append(('journal', journal))
    elif bib_type in ('inproceedings', 'incollection') and (secondary or journal):
        fields.append(('booktitle', secondary or journal))
    if volume:
        fields.append(('volume', volume))
    if number:
        fields.append(('number', number))
    if pages:
        fields.append(('pages', pages))
    if year:
        fields.append(('year', year))
    if publisher:
        fields.append(('publisher', publisher))
    if address:
        fields.append(('address', address))
    if edition:
        fields.append(('edition', edition))
    if isbn:
        fields.append(('isbn', isbn))
    if doi:
        fields.append(('doi', doi))
    if url and not doi:
        fields.append(('url', url))
    if keywords_list:
        fields.append(('keywords', ', '.join(keywords_list)))
    if abstract:
        fields.append(('abstract', abstract))
    fields.append(('endnote_rec_number', rec_number))
    fields.append(('endnote_ref_type', ref_type_name))

    lines = [f'@{bib_type}{{{bibkey},']
    for name, value in fields:
        lines.append(f'  {name:11s} = {{{bib_escape(value)}}},')
    if lines[-1].endswith(','):
        lines[-1] = lines[-1].rstrip(',')
    lines.append('}')
    return bibkey, bib_type, ref_type_name, '\n'.join(lines), authors, year, doi, title


def main():
    if len(sys.argv) != 4:
        print('Usage: endnote_xml_to_bibtex.py <input.xml> <output.bib> <manifest.yaml>')
        sys.exit(2)

    xml_path = Path(sys.argv[1])
    bib_path = Path(sys.argv[2])
    manifest_path = Path(sys.argv[3])

    text = xml_path.read_text(encoding='utf-8')
    root = ET.fromstring(text)
    records = root.findall('.//record')

    print(f'Parsed {len(records)} records from {xml_path.name}')

    used_keys = set()
    entries = []
    counters = {'bib_type': Counter(), 'ref_type': Counter()}
    no_authors = []
    no_year = []
    duplicates_by_doi = {}

    for rec in records:
        bibkey, bib_type, ref_type_name, bib_block, authors, year, doi, title = convert_record(rec, used_keys)
        entries.append({
            'bibkey': bibkey,
            'bib_type': bib_type,
            'ref_type': ref_type_name,
            'bib_block': bib_block,
            'authors': authors,
            'year': year,
            'doi': doi,
            'title': title,
        })
        counters['bib_type'][bib_type] += 1
        counters['ref_type'][ref_type_name] += 1
        if not authors:
            no_authors.append(bibkey)
        if not year:
            no_year.append(bibkey)
        if doi:
            duplicates_by_doi.setdefault(doi, []).append(bibkey)

    with bib_path.open('w', encoding='utf-8') as f:
        f.write('% =====================================================================\n')
        f.write('% EndNote XML Import (pending Byzantine verification)\n')
        f.write('% =====================================================================\n')
        f.write(f'% Source:   {xml_path}\n')
        f.write(f'% Imported: {date.today().isoformat()}\n')
        f.write(f'% Records:  {len(entries)}\n')
        f.write('% Status:   PENDING. None of these entries are approved. They must pass\n')
        f.write('%           the R019 Byzantine-Bayesian verification protocol before\n')
        f.write('%           being moved to ../approved.bib. Bibkeys are auto-generated\n')
        f.write('%           (surname+year+firstword); may collide with approved.bib keys\n')
        f.write('%           and will be renamed at promotion time.\n')
        f.write('% =====================================================================\n\n')
        for e in entries:
            f.write(e['bib_block'])
            f.write('\n\n')

    with manifest_path.open('w', encoding='utf-8') as f:
        f.write('# =====================================================================\n')
        f.write('# Pending References Manifest (from EndNote XML import)\n')
        f.write('# =====================================================================\n')
        f.write('# All entries below are PENDING. They have NOT been verified per the\n')
        f.write('# R019 Byzantine-Bayesian protocol. Conversion preserved EndNote field\n')
        f.write('# content but did not re-verify against authoritative external sources.\n')
        f.write('# =====================================================================\n\n')
        f.write('schema_version: "1.0"\n')
        f.write(f'source_xml: "{xml_path.as_posix()}"\n')
        f.write(f'imported_date: "{date.today().isoformat()}"\n')
        f.write(f'imported_by: claude-opus-4-7\n')
        f.write(f'record_count: {len(entries)}\n')
        f.write(f'status: pending\n\n')
        f.write('defaults:\n')
        f.write('  verified: false\n')
        f.write('  verification_mode: not-yet-verified\n')
        f.write('  pending_byzantine_verification: true\n\n')
        f.write('summary:\n')
        f.write('  bib_type_counts:\n')
        for t, c in counters['bib_type'].most_common():
            f.write(f'    {t}: {c}\n')
        f.write('  ref_type_counts:\n')
        for t, c in counters['ref_type'].most_common():
            qkey = t if re.match(r'^[A-Za-z0-9_]+$', t) else f'"{t}"'
            f.write(f'    {qkey}: {c}\n')
        f.write(f'  entries_without_authors: {len(no_authors)}\n')
        f.write(f'  entries_without_year: {len(no_year)}\n')
        dup_doi_keys = [d for d, ks in duplicates_by_doi.items() if len(ks) > 1]
        f.write(f'  duplicate_dois: {len(dup_doi_keys)}\n')
        if dup_doi_keys:
            f.write('  duplicate_doi_examples:\n')
            for d in dup_doi_keys[:10]:
                f.write(f'    "{d}": {duplicates_by_doi[d]}\n')

    print(f'Wrote BibTeX:    {bib_path} ({bib_path.stat().st_size // 1024} KB)')
    print(f'Wrote manifest:  {manifest_path} ({manifest_path.stat().st_size // 1024} KB)')
    print()
    print('Top BibTeX types:')
    for t, c in counters['bib_type'].most_common(5):
        print(f'  {c:5d}  {t}')
    print()
    print(f'Anomalies: {len(no_authors)} without authors, {len(no_year)} without year, {len(dup_doi_keys)} duplicate DOIs')


if __name__ == '__main__':
    main()
