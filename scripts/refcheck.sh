#!/usr/bin/env bash
# R019 references verification gate (bash wrapper).
# See: docs/proposed_R019_references_verification_gate.md
exec python "$(dirname "$0")/refcheck.py" "$@"
