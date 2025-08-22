#!/usr/bin/env bash
set -euo pipefail
A0_HOME="/root/a0"
ln -sf "$A0_HOME/config/mcp.json" "$A0_HOME/mcp.json" || true