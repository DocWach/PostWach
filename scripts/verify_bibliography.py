"""Verify bibliography for an article markdown file.

- Extracts all in-text author-date citations from the body (sections 1-9 area).
- Extracts all entries from the References section.
- Cross-checks: missing citations (in body, not in references) and orphans (in references, not cited).

Usage: python verify_bibliography.py <path-to-md>
"""
from __future__ import annotations

import re
import sys
from pathlib import Path
from collections import defaultdict


def split_body_and_refs(text: str) -> tuple[str, str]:
    """Return (body_text, references_text)."""
    m = re.search(r"^## References\s*$", text, re.MULTILINE)
    if not m:
        return text, ""
    body = text[: m.start()]
    rest = text[m.end():]
    # references end at the next H2 (e.g., ## Author Biographies)
    end = re.search(r"^## ", rest, re.MULTILINE)
    refs = rest[: end.start()] if end else rest
    return body, refs


def extract_citations(body: str) -> set[str]:
    """Extract author-year keys from body. Returns set like {'Wach 2025', 'INCOSE 2022', ...}.

    Handles formats like:
      (Author 2024)
      (Author1 and Author2 2024)
      (Author1, Author2, and Author3 2024)
      (Author et al. 2024)
      (Author 2024a)
      (Author 2024; OtherAuthor 2025)
      Author (2024)
      Author and Author (2024)
      Author et al. (2024)
    """
    cites = set()

    # Pattern for parenthetical citation chains: (Author 2024; OtherAuthor 2025)
    paren_pattern = re.compile(r"\(([^)]*\d{4}[a-z]?[^)]*)\)")
    for m in paren_pattern.finditer(body):
        block = m.group(1)
        # split on semicolons for multiple cites in one parens
        for chunk in block.split(";"):
            chunk = chunk.strip()
            # find author-year
            yr = re.search(r"\b(\d{4}[a-z]?)\b", chunk)
            if yr:
                year = yr.group(1)
                # author part is everything before the year
                author_part = chunk[: yr.start()].strip().rstrip(",").strip()
                # Skip noise: empty, pure-numeric, has "PLACEHOLDER", obvious URLs
                if not author_part or "PLACEHOLDER" in author_part or "http" in author_part:
                    continue
                # Skip page numbers, DOI, etc.
                if re.match(r"^p\.?\s*\d", author_part) or re.match(r"^pp\.?\s*\d", author_part):
                    continue
                cites.add(_normalize_author_year(author_part, year))

    # Pattern for narrative cites: Author (2024) / Author and Author (2024) / Author et al. (2024)
    narrative_pattern = re.compile(
        r"\b([A-Z][A-Za-zÀ-ſ'\-]+(?:,?\s+(?:and\s+)?[A-Z][A-Za-zÀ-ſ'\-]+|\s+et\s+al\.|(?:,\s+[A-Z][A-Za-zÀ-ſ'\-]+)*(?:,\s+and\s+[A-Z][A-Za-zÀ-ſ'\-]+)?)?)\s+\((\d{4}[a-z]?)\)"
    )
    for m in narrative_pattern.finditer(body):
        author_part = m.group(1).strip()
        year = m.group(2)
        if not author_part:
            continue
        cites.add(_normalize_author_year(author_part, year))

    return cites


def _normalize_author_year(author_part: str, year: str) -> str:
    """Reduce to a canonical 'last_name year' key."""
    # Take first author surname only for matching to references entry
    # Strip common noise
    author_part = re.sub(r"\s+et\s+al\.?$", "", author_part, flags=re.IGNORECASE)
    # Take just the first word (typically a surname or initial-stripped surname)
    parts = re.split(r",|\s+and\s+|\s+", author_part)
    parts = [p for p in parts if p]
    first = parts[0] if parts else ""
    # Strip trailing punctuation
    first = first.rstrip(".,").strip()
    return f"{first} {year}"


def extract_references(refs: str) -> dict[str, str]:
    """Return {key: full_entry} where key is 'first_author_surname year'."""
    entries = {}
    # Reference entries typically start at column 0; split on blank lines
    paragraphs = [p.strip() for p in re.split(r"\n\s*\n", refs) if p.strip()]
    for entry in paragraphs:
        # Extract first surname + year
        # Look for "Surname, Initial." or "Surname, F." or just "Surname"
        # then year
        m = re.match(
            r"\s*([A-Z][A-Za-zÀ-ſ'\-]+)(?:,\s+[A-Z]\.[^.]*?)?(?:[^\d]*?)(\d{4}[a-z]?)",
            entry,
        )
        if m:
            surname = m.group(1)
            year = m.group(2)
            key = f"{surname} {year}"
            entries[key] = entry.replace("\n", " ").strip()
    return entries


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: verify_bibliography.py <path-to-md>", file=sys.stderr)
        sys.exit(1)
    path = Path(sys.argv[1])
    text = path.read_text(encoding="utf-8")
    body, refs = split_body_and_refs(text)

    if not refs:
        print("ERROR: No '## References' section found.", file=sys.stderr)
        sys.exit(1)

    cites = extract_citations(body)
    ref_entries = extract_references(refs)

    print(f"=== Bibliography verification for {path.name} ===\n")
    print(f"Body citations found: {len(cites)}")
    print(f"References list entries: {len(ref_entries)}\n")

    # Citations missing from references
    cite_keys = set(cites)
    ref_keys = set(ref_entries.keys())

    # Try fuzzy matching: if a body cite has 'Wach 2025a' and refs has 'Wach 2025a' great;
    # if body has 'Wach 2025' but refs has 'Wach 2025a' and 'Wach 2025b', that's ambiguous.

    missing = []
    fuzzy_match_only = []
    for c in sorted(cite_keys):
        if c in ref_keys:
            continue
        # try base year (strip trailing letter)
        base_year = re.sub(r"([a-z])$", "", c)
        if base_year in ref_keys:
            continue
        # try matching with trailing letter variants
        matches = [r for r in ref_keys if r.startswith(re.sub(r"([a-z])$", "", c) + "a") or
                   r.startswith(re.sub(r"([a-z])$", "", c) + "b") or
                   r.startswith(re.sub(r"([a-z])$", "", c) + "c") or
                   r.startswith(re.sub(r"([a-z])$", "", c))]
        if matches:
            fuzzy_match_only.append((c, matches))
        else:
            missing.append(c)

    print("--- MISSING CITATIONS (in body, not in references) ---")
    if not missing:
        print("(none)")
    for m in missing:
        print(f"  {m}")
    print()

    print("--- AMBIGUOUS / FUZZY MATCHES (cite needs disambiguation letter or vice versa) ---")
    if not fuzzy_match_only:
        print("(none)")
    for c, ms in fuzzy_match_only:
        print(f"  body cite '{c}' could match: {ms}")
    print()

    # Orphaned references (in references list but not cited)
    orphans = []
    for r in sorted(ref_keys):
        if r in cite_keys:
            continue
        # check if any cite is fuzzy-matched to this ref
        base_r = re.sub(r"([a-z])$", "", r)
        if any(c.startswith(base_r) for c in cite_keys):
            continue
        orphans.append(r)

    print("--- ORPHANED REFERENCES (in references list, not cited in body) ---")
    if not orphans:
        print("(none)")
    for o in orphans:
        snippet = ref_entries[o][:120]
        print(f"  {o}: {snippet}...")


if __name__ == "__main__":
    main()
