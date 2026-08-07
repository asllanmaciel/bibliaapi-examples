#!/usr/bin/env bash
set -euo pipefail

: "${BIBLIA_API_TOKEN:?Defina BIBLIA_API_TOKEN antes de executar}"

curl --fail-with-body --silent --show-error \
  --header "Authorization: Bearer ${BIBLIA_API_TOKEN}" \
  --header "Accept: application/json" \
  "https://bibliaapi.com.br/api/v2/versions/acf/books/jo/chapters/3/verses/16"

printf '\n'
