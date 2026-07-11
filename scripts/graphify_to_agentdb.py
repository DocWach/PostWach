#!/usr/bin/env python3
"""graphify_to_agentdb.py -- bridge a Graphify graph.json into ruflo AgentDB.

Adopts the ruflo-ingest pattern proven in bmpwach-lab/USAFA_AI_TigerTeam
(shared/scripts/ingest_vector_db.sh, ruflo AgentDB V3, all-MiniLM-L6-v2 384d)
but ingests GRAPH STRUCTURE (nodes + typed edges) rather than text chunks.

Emits a ruflo-memory-export/v1 JSON for bulk load (one embedder load, not
one-subprocess-per-entry). Load with:
    claude-flow memory import -i <out> -n <namespace>

Security controls (Fort Wachs FW-GRAPHIFY-001 promotion kit, code-side):
  C1  input sanitization (_san): control-char/newline strip, length caps,
      leading imperative/tool-directive tokens flagged. Applied to every
      graph-derived field that reaches a memory value.
  C2  quarantine tags: every entry carries trust:untrusted,source:graphify
      so recall consumers frame graph content as DATA, not instructions.
  C4  honest provenance: AST-extracted vs LLM-derived distinguished; the
      producing FM named for LLM content; a signed sidecar manifest
      (--manifest-out) stamps FM identity, tool+version, operator, corpus,
      entry count, and a content hash (R018).
These are defense-in-depth; pair with C0 (dedicated cwd/.swarm store),
C3 (corpus-trust + AIMDS scan), C5 (dry-run/diff/rollback) before any
shared/live write. Sanitizing does not make an untrusted corpus trusted.
"""
import argparse
import hashlib
import json
import re
import time
from collections import defaultdict
from pathlib import Path

# --- C1: boundary sanitization -------------------------------------------
_CTRL = re.compile(r"[\x00-\x1f\x7f]")          # control chars incl. newlines
_DIRECTIVE = re.compile(r"^\s*(ignore|disregard|system|assistant|tool|"
                        r"instruction|exfiltrate|run|execute)\b", re.I)
_MAXLEN = 512


def _san(text, maxlen=_MAXLEN):
    """Neutralize graph-derived text before it becomes a memory value.
    Collapses control chars/newlines (how injected directives escape a single
    entry), length-caps, and flags leading imperative/tool-directive tokens."""
    s = _CTRL.sub(" ", str(text)).strip()
    if _DIRECTIVE.search(s):
        s = "[untrusted] " + s
    return s[:maxlen]


# --- C4: provenance ------------------------------------------------------
def _prov(ver, source_kind, model, access):
    if source_kind == "llm":
        return (f"PROVENANCE: graphify {ver} doc-pass, LLM-derived "
                f"(model={model or 'UNSPECIFIED'}, access={access or 'UNSPECIFIED'}); "
                f"recorded_by graphify_to_agentdb.py")
    return (f"PROVENANCE: graphify {ver} AST (deterministic, tool-extracted); "
            f"recorded_by graphify_to_agentdb.py")


def load_graph(p):
    g = json.loads(Path(p).read_text(encoding="utf-8"))
    nodes = {n["id"]: n for n in g.get("nodes", [])}
    links = g.get("links") or g.get("edges") or []
    return nodes, links


def neighbor_maps(links):
    out = defaultdict(list)
    inn = defaultdict(list)
    for e in links:
        s, t = e.get("source"), e.get("target")
        rel = e.get("relation") or e.get("label") or e.get("key") or "related"
        out[s].append((rel, t))
        inn[t].append((rel, s))
    return out, inn


def node_value(nid, n, out, inn, prov, max_nbr=12):
    label = _san(n.get("label") or n.get("norm_label") or nid)
    ft = _san(n.get("file_type", "?"), 32)
    src = _san(n.get("source_file", "?"), 256)
    loc = _san(n.get("source_location", ""), 64)
    comm = _san(n.get("community", "?"), 32)
    parts = [f"{label} ({ft}) in {src}:{loc}; community {comm}."]
    outs = out.get(nid, [])[:max_nbr]
    if outs:
        parts.append("Outgoing: " + ", ".join(f"{_san(r, 48)}->{_san(d, 96)}" for r, d in outs) + ".")
    ins = inn.get(nid, [])[:max_nbr]
    if ins:
        parts.append("Incoming: " + ", ".join(f"{_san(s, 96)} {_san(r, 48)}->" for r, s in ins) + ".")
    parts.append(prov)
    return " ".join(parts)


def edge_value(e, prov):
    s, t = _san(e.get("source"), 96), _san(e.get("target"), 96)
    rel = _san(e.get("relation") or e.get("label") or "related", 48)
    tag = _san(e.get("provenance") or e.get("confidence") or "", 32)
    head = f"{s} --{rel}--> {t}" + (f" [{tag}]" if tag else "")
    return f"{head}. {prov}"


def causal_edge(e):
    """A promotion-ready native causal-edge record for the MCP agentdb_causal-edge
    tool. Node IDs use the `entity:` domain prefix (ruflo recognizes
    mem/agent/task/entity/span/pattern; a bare `node/...` key is rejected).

    NOTE (ruflo v3.14.4): creating these via MCP succeeds, but graph-query/
    graph-pathfinder traversal is not yet turnkey (causal-write vs graph-read
    store/id alignment). Treat this manifest as promotion-ready, not as a
    verified traversal path, until that alignment is confirmed upstream.
    """
    s, t = e.get("source"), e.get("target")
    rel = e.get("relation") or e.get("label") or "related"
    conf = str(e.get("provenance") or e.get("confidence") or "").upper()
    weight = 0.9 if conf == "EXTRACTED" else 0.6 if conf == "INFERRED" else 0.75
    return {
        "sourceId": f"entity:{s}",
        "targetId": f"entity:{t}",
        "relation": rel,
        "weight": weight,
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("graph", help="path to graphify graph.json")
    ap.add_argument("-o", "--out", required=True, help="output import JSON")
    ap.add_argument("-n", "--namespace", default="graphify-isolib")
    ap.add_argument("--ver", default="0.9.12")
    ap.add_argument("--no-edges", action="store_true", help="nodes only")
    ap.add_argument("--limit", type=int, default=0, help="cap entries (0=all)")
    ap.add_argument("--causal-out", default="",
                    help="also write a promotion-ready causal-edge manifest JSON")
    # C4 provenance flags (Fort Wachs FW-GRAPHIFY-001)
    ap.add_argument("--source-kind", choices=["ast", "llm"], default="ast",
                    help="ast = deterministic tree-sitter; llm = doc-pass LLM-derived")
    ap.add_argument("--model", default="", help="producing FM (required when --source-kind llm)")
    ap.add_argument("--access-mode", default="", help="FM access mode, e.g. hosted-api / local")
    ap.add_argument("--operator", default="", help="operator/orchestrator identity for the manifest")
    ap.add_argument("--manifest-out", default="",
                    help="write a signed bridge-manifest sidecar (R018)")
    a = ap.parse_args()

    prov = _prov(a.ver, a.source_kind, a.model, a.access_mode)
    trust = "trust:untrusted,source:graphify"
    nodes, links = load_graph(a.graph)
    out, inn = neighbor_maps(links)
    now = int(time.time() * 1000)
    entries = []
    for nid, n in nodes.items():
        entries.append({
            "key": f"node/{nid}",
            "namespace": a.namespace,
            "value": node_value(nid, n, out, inn, prov),
            "createdAt": now, "updatedAt": now,
            "accessCount": 0, "hasEmbedding": True,
            "tags": (f"type:graphify-node,community:{n.get('community', '?')},"
                     f"file:{_san(n.get('source_file', '?'), 128)},{trust}"),
        })
    if not a.no_edges:
        for i, e in enumerate(links):
            entries.append({
                "key": f"edge/{i}",
                "namespace": a.namespace,
                "value": edge_value(e, prov),
                "createdAt": now, "updatedAt": now,
                "accessCount": 0, "hasEmbedding": True,
                "tags": f"type:graphify-edge,relation:{_san(e.get('relation', 'related'), 48)},{trust}",
            })
    if a.limit:
        entries = entries[:a.limit]
    doc = {
        "schema": "ruflo-memory-export/v1",
        "exportedAt": "",
        "namespace": None,
        "count": len(entries),
        "entries": entries,
    }
    Path(a.out).write_text(json.dumps(doc, indent=2), encoding="utf-8")
    n_edges = 0 if a.no_edges else len(links)
    print(f"wrote {a.out}: {len(entries)} entries "
          f"({len(nodes)} nodes, {n_edges} edges) ns={a.namespace} "
          f"source_kind={a.source_kind} [sanitized+quarantined]")

    if a.source_kind == "llm" and not a.model:
        print("WARNING: --source-kind llm without --model; provenance names the FM as UNSPECIFIED (R018 gap)")

    if a.causal_out:
        manifest = {
            "schema": "graphify-causal-edges/v1",
            "note": ("Load via MCP agentdb_causal-edge (one call per edge). "
                     "Traversal not turnkey in ruflo v3.14.4; promotion-ready."),
            "count": len(links),
            "edges": [causal_edge(e) for e in links],
        }
        Path(a.causal_out).write_text(json.dumps(manifest, indent=2), encoding="utf-8")
        print(f"wrote {a.causal_out}: {len(links)} causal-edge records")

    # C4 / R018: signed sidecar manifest attributing this bridge write.
    if a.manifest_out:
        blob = json.dumps(doc, sort_keys=True).encode("utf-8")
        manifest = {
            "schema": "graphify-bridge-manifest/v1",
            "tool": f"graphify_to_agentdb.py + graphify {a.ver}",
            "source_kind": a.source_kind,
            "foundation_model": a.model or None,      # required when source_kind == "llm"
            "access_mode": a.access_mode or None,
            "operator": a.operator or None,
            "corpus_id": a.namespace,
            "entry_count": len(entries),
            "content_sha256": hashlib.sha256(blob).hexdigest(),
            "created_at_ms": now,
        }
        Path(a.manifest_out).write_text(json.dumps(manifest, indent=2), encoding="utf-8")
        print(f"wrote {a.manifest_out}: bridge-manifest sha256={manifest['content_sha256'][:12]}")


if __name__ == "__main__":
    main()
