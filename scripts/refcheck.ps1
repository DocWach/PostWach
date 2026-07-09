# R019 references verification gate (PowerShell wrapper).
# See: docs/proposed_R019_references_verification_gate.md
python (Join-Path $PSScriptRoot 'refcheck.py') @args
exit $LASTEXITCODE
