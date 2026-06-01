#!/usr/bin/env bash
# Inventory of ruvnet / claude-flow markings across all git repos in the research tree.

ROOT="/c/Users/pfwac/OneDrive - University of Arizona/Documents/03 Projects/00 My Research"

printf "%-65s | %-40s | %6s | %6s | %6s | %-15s\n" "REPO" "REMOTE" "TOTAL" "RUVTRL" "RUVAUTH" "BRANDING"
printf "%-65s | %-40s | %6s | %6s | %6s | %-15s\n" "----" "------" "-----" "------" "-------" "--------"

find "$ROOT" -maxdepth 4 -type d -name ".git" 2>/dev/null | sed 's|/.git$||' | while read -r repo; do
    cd "$repo" || continue
    short="${repo#$ROOT/}"
    remote=$(git remote get-url origin 2>/dev/null | sed 's|https://github.com/||; s|\.git$||' | head -c 40)
    total=$(git rev-list --count HEAD 2>/dev/null || echo "?")
    ruv_trailer=$(git log --all --pretty=format:"%(trailers:key=Co-Authored-By)" 2>/dev/null | grep -c "ruv@ruv.net" || true)
    ruv_author=$(git log --all --pretty=format:"%ae" 2>/dev/null | grep -c "ruv@ruv.net\|ruvnet" || true)
    branding=""
    [ -d ".claude-flow" ] && branding="${branding}cf-dir "
    [ -f "CLAUDE-FLOW.md" ] && branding="${branding}cf-md "
    grep -l -i "ruvnet\|claude-flow" README.md 2>/dev/null >/dev/null && branding="${branding}README "
    [ -z "$branding" ] && branding="-"
    printf "%-65s | %-40s | %6s | %6s | %6s | %-15s\n" "${short:0:65}" "${remote:-none}" "$total" "$ruv_trailer" "$ruv_author" "$branding"
done
