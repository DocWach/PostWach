"""Extract reviewer comments from a .docx file into structured JSON.

Usage:
    python extract_docx_comments.py <path-to-docx> [--out comments.json]

Outputs a JSON file with:
  - comments: list of {id, parent_id, author, initials, date, text, anchored_quote, paragraph_context}
  - reviewers: list of {id, name, comment_count}
  - extraction_metadata: {source, extracted_at, total_comments}
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import zipfile
from datetime import datetime, timezone
from pathlib import Path
from xml.etree import ElementTree as ET

W_NS = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
W15_NS = "{http://schemas.microsoft.com/office/word/2012/wordml}"


def _text_of_paragraph(p_elem) -> str:
    parts = []
    for t in p_elem.iter(f"{W_NS}t"):
        if t.text:
            parts.append(t.text)
    return "".join(parts)


def _text_of_comment(c_elem) -> str:
    paragraphs = []
    for p in c_elem.findall(f"{W_NS}p"):
        ptext = _text_of_paragraph(p)
        if ptext:
            paragraphs.append(ptext)
    return "\n\n".join(paragraphs).strip()


def parse_comments(comments_xml: bytes) -> dict[str, dict]:
    root = ET.fromstring(comments_xml)
    out = {}
    for c in root.findall(f"{W_NS}comment"):
        cid = c.attrib.get(f"{W_NS}id")
        out[cid] = {
            "id": cid,
            "author": c.attrib.get(f"{W_NS}author", ""),
            "initials": c.attrib.get(f"{W_NS}initials", ""),
            "date": c.attrib.get(f"{W_NS}date", ""),
            "text": _text_of_comment(c),
        }
    return out


def parse_extended(extended_xml: bytes) -> dict[str, str | None]:
    """Return {paraId: parentParaId or None} mapping for threading."""
    root = ET.fromstring(extended_xml)
    out = {}
    for ce in root.findall(f"{W15_NS}commentEx"):
        para_id = ce.attrib.get(f"{W15_NS}paraId")
        parent_id = ce.attrib.get(f"{W15_NS}paraIdParent")
        if para_id:
            out[para_id] = parent_id
    return out


def parse_ids(ids_xml: bytes | None) -> dict[str, str]:
    """Map comment.id -> paraId via commentsIds.xml if present."""
    if not ids_xml:
        return {}
    root = ET.fromstring(ids_xml)
    out = {}
    for c in root.findall(f"{W15_NS}commentId"):
        cid = c.attrib.get(f"{W15_NS}paraId")
        durable = c.attrib.get(f"{W15_NS}durableId")
        if cid and durable:
            out[durable] = cid
    return out


def extract_anchors(document_xml: bytes, comment_ids: list[str]) -> dict[str, dict]:
    """Walk document.xml in order and capture text between commentRangeStart/End for each id.

    Returns {id: {anchored_quote, paragraph_context}}.
    """
    root = ET.fromstring(document_xml)

    open_ranges: dict[str, list[str]] = {}
    results: dict[str, dict] = {cid: {"anchored_quote": "", "paragraph_context": ""} for cid in comment_ids}

    para_text_buffer: list[tuple[ET.Element, str]] = []
    current_para_text: list[str] = []

    for elem in root.iter():
        tag = elem.tag
        if tag == f"{W_NS}commentRangeStart":
            cid = elem.attrib.get(f"{W_NS}id")
            if cid in results:
                open_ranges[cid] = []
        elif tag == f"{W_NS}commentRangeEnd":
            cid = elem.attrib.get(f"{W_NS}id")
            if cid in open_ranges:
                results[cid]["anchored_quote"] = "".join(open_ranges[cid]).strip()
                del open_ranges[cid]
        elif tag == f"{W_NS}t":
            if elem.text:
                for buf in open_ranges.values():
                    buf.append(elem.text)

    return results


def extract_paragraph_context(document_xml: bytes, comment_ids: list[str]) -> dict[str, str]:
    """For each comment id, find the paragraph(s) that contain its anchor and return paragraph text."""
    root = ET.fromstring(document_xml)
    contexts = {cid: "" for cid in comment_ids}

    for p in root.iter(f"{W_NS}p"):
        starts_in_p: list[str] = []
        for ref in p.iter(f"{W_NS}commentRangeStart"):
            cid = ref.attrib.get(f"{W_NS}id")
            if cid in contexts:
                starts_in_p.append(cid)
        if starts_in_p:
            ptext = _text_of_paragraph(p)
            for cid in starts_in_p:
                if not contexts[cid]:
                    contexts[cid] = ptext
    return contexts


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("docx", help="Path to .docx with reviewer comments")
    ap.add_argument("--out", default=None, help="Output JSON path (default: alongside docx)")
    args = ap.parse_args()

    docx_path = Path(args.docx)
    if not docx_path.exists():
        print(f"ERROR: {docx_path} not found", file=sys.stderr)
        sys.exit(1)

    out_path = Path(args.out) if args.out else docx_path.with_suffix(".comments.json")

    with zipfile.ZipFile(docx_path) as z:
        names = z.namelist()
        comments_xml = z.read("word/comments.xml") if "word/comments.xml" in names else b""
        extended_xml = z.read("word/commentsExtended.xml") if "word/commentsExtended.xml" in names else b""
        ids_xml = z.read("word/commentsIds.xml") if "word/commentsIds.xml" in names else None
        document_xml = z.read("word/document.xml")

    if not comments_xml:
        print("No comments found in docx.", file=sys.stderr)
        sys.exit(0)

    comments = parse_comments(comments_xml)
    anchors = extract_anchors(document_xml, list(comments.keys()))
    contexts = extract_paragraph_context(document_xml, list(comments.keys()))

    enriched = []
    for cid, c in sorted(comments.items(), key=lambda x: int(x[0]) if x[0].isdigit() else 0):
        enriched.append({
            "id": cid,
            "author": c["author"],
            "initials": c["initials"],
            "date": c["date"],
            "text": c["text"],
            "anchored_quote": anchors.get(cid, {}).get("anchored_quote", ""),
            "paragraph_context": contexts.get(cid, ""),
        })

    reviewer_counts: dict[str, int] = {}
    for c in enriched:
        reviewer_counts[c["author"]] = reviewer_counts.get(c["author"], 0) + 1

    payload = {
        "extraction_metadata": {
            "source": str(docx_path.name),
            "extracted_at": datetime.now(timezone.utc).isoformat(),
            "total_comments": len(enriched),
            "extractor": "extract_docx_comments.py",
        },
        "reviewers": [
            {"name": name, "comment_count": count}
            for name, count in sorted(reviewer_counts.items(), key=lambda x: -x[1])
        ],
        "comments": enriched,
    }

    out_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Wrote {out_path} ({len(enriched)} comments, {len(reviewer_counts)} reviewers)")


if __name__ == "__main__":
    main()
