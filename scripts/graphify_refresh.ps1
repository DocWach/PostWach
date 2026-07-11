<#
.SYNOPSIS
  L3 lifecycle refresh: build a cleaned mirror of a corpus -> graphify (code-only, no LLM)
  -> graphify_to_agentdb bridge -> ruflo AgentDB import. Keeps a Graphify structural graph
  fresh in AgentDB as code changes.

.DESCRIPTION
  Zero model / zero egress / zero RAM. The source corpus is treated READ-ONLY: it is mirrored
  (logs / .claude-flow / caches stripped) into a work dir OUTSIDE OneDrive, and Graphify runs
  on the mirror so no graphify-out is ever written into OneDrive. Intended to be launched
  (backgrounded) from the PostWach SessionStart hook, or run manually.

  Stable install: C:\Users\pfwac\tools\graphify\venv
  Work dir:       C:\Users\pfwac\tools\graphify\work   (mirror + import file + log; outside OneDrive)

.PARAMETER Corpus   Source folder to graph (read-only). Default: isomorphism-library.
.PARAMETER Namespace  ruflo AgentDB namespace. Default: graphify-postwach.
                      Query: claude-flow memory search -q "<q>" -n graphify-postwach
.PARAMETER Force    Rebuild + re-import even if the graph looks up to date.

.NOTES
  Disable auto-refresh: remove the graphify entry from 01 PostWach/.claude/settings.json
  (SessionStart). MCP-surface memory_search reads a different DB than this CLI import; query
  this namespace with `claude-flow memory search`.
#>
param(
  [string]$Corpus = "C:\Users\pfwac\OneDrive - University of Arizona\Documents\03 Projects\00_Hive_Empire\01 Hives\01 PostWach\Papers\SE_Math_Foundations\isomorphism-library",
  [string]$Namespace = "graphify-postwach",
  [switch]$Force
)
# Native tools (graphify) write warnings to stderr; under "Stop" + *>> PowerShell 5.1 turns
# those into terminating NativeCommandError. Keep native stderr non-fatal; gate on $LASTEXITCODE.
$ErrorActionPreference = "Continue"
$gf     = "C:\Users\pfwac\tools\graphify\venv\Scripts\graphify.exe"
$py     = "C:\Users\pfwac\tools\graphify\venv\Scripts\python.exe"
$bridge = Join-Path $PSScriptRoot "graphify_to_agentdb.py"
$work   = "C:\Users\pfwac\tools\graphify\work"
$mirror = Join-Path $work "corpus-mirror"
New-Item -ItemType Directory -Force -Path $work, $mirror | Out-Null
$log    = Join-Path $work "refresh.log"
$graph  = Join-Path $mirror "graphify-out\graph.json"
$import = Join-Path $work "bridge_import.json"

"[{0}] refresh start corpus={1} ns={2}" -f (Get-Date -Format s), $Corpus, $Namespace | Add-Content $log

# Staleness gate: skip if the mirror graph is newer than the newest source code file.
if (-not $Force -and (Test-Path $graph)) {
  $graphTime = (Get-Item $graph).LastWriteTimeUtc
  $newest = Get-ChildItem $Corpus -Recurse -File -Include *.py, *.md, *.json -ErrorAction SilentlyContinue |
            Where-Object { $_.FullName -notmatch '\\graphify-out\\|\\\.claude-flow\\|\\\.git\\' } |
            Sort-Object LastWriteTimeUtc -Descending | Select-Object -First 1
  if ($newest -and $newest.LastWriteTimeUtc -le $graphTime) {
    "[{0}] up to date; skip" -f (Get-Date -Format s) | Add-Content $log
    return
  }
}

# 1. cleaned mirror OUTSIDE OneDrive (strip noise; keep the mirror's own graphify-out across runs)
robocopy $Corpus $mirror /MIR /XD .claude-flow .git .pytest_cache __pycache__ .ipynb_checkpoints graphify-out /XF *.log *.pyc *.pid /NFL /NDL /NJH /NJS /NC /NS /NP | Out-Null
if ($LASTEXITCODE -le 7) { $global:LASTEXITCODE = 0 }

# 2. graph the mirror (tree-sitter AST, no LLM). extract if first run, else update.
if (Test-Path $graph) { & $gf update $mirror *>> $log } else { & $gf extract $mirror --code-only *>> $log }
# 3. bridge graph.json -> ruflo import file
& $py $bridge $graph -o $import -n $Namespace *>> $log
# 4. import into ruflo AgentDB (namespace-isolated; --merge dedups unchanged entries)
Push-Location $work
try { claude-flow memory import -i $import -n $Namespace *>> $log } finally { Pop-Location }
"[{0}] refresh done" -f (Get-Date -Format s) | Add-Content $log
