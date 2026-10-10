#!/usr/bin/env bash
# Baixa a geometria de solo (GND_DRAW) dos aeródromos para .dados/<ICAO>/.
# O repositório vatsim-brasil/atcops-desenho-solo é privado: precisa do gh autenticado com acesso a ele.
# Uso: ./baixar.sh [ICAO ...]   (sem argumentos, baixa todos)
set -euo pipefail
cd "$(dirname "$0")"
REPO=vatsim-brasil/atcops-desenho-solo
REF=a8655e9ad556e901e95fff941ffd6b6ce8c74bb8  # versão usada para gerar os SVGs atuais
ICAOS=("$@")
[ ${#ICAOS[@]} -eq 0 ] && ICAOS=(SBGR SBCT SBGL SBRF SBSV SBVT)
for icao in "${ICAOS[@]}"; do
  mkdir -p ".dados/$icao"
  gh api "repos/$REPO/contents/GND_DRAW/$icao?ref=$REF" --jq '.[] | select(.name | endswith(".geojson")) | .path' |
    while read -r path; do
      gh api -H 'Accept: application/vnd.github.raw' "repos/$REPO/contents/$path?ref=$REF" > ".dados/$icao/$(basename "$path")"
    done
  echo "$icao: $(ls ".dados/$icao" | wc -l) arquivos"
done
