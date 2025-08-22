#!/usr/bin/env bash
set -euo pipefail
if ! command -v runpodctl >/dev/null 2>&1; then
  echo "runpodctl not found" >&2
  exit 1
fi
case "${1:-}" in
  list) runpodctl get pods ;;
  gpus) runpodctl get gpus ;;
  *) echo "usage: server.sh [list|gpus]" && exit 2 ;;
esac
