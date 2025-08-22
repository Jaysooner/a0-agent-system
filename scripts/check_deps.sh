#!/usr/bin/env bash
set -euo pipefail
need() { command -v "$1" >/dev/null 2>&1 || { echo "Missing $1"; exit 1; }; }
need node
need npm
need jq
need python3
need pip3
echo "Deps OK"