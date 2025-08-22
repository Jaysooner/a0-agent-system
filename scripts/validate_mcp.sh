#!/usr/bin/env bash
set -euo pipefail
if command -v jq >/dev/null 2>&1; then
  echo "[validate] context7 package.json:"
  jq '.name,.scripts' /root/a0/mcps/context7/package.json 2>/dev/null || true
  echo "[validate] venice package.json:"
  jq '.name,.scripts' /root/a0/mcps/venice/package.json 2>/dev/null || true
fi
echo "[validate] agentmail server exists?"
test -f /root/a0/mcps/agentmail/agentmail_mcp/server.py && echo "OK" || echo "MISSING"
echo "[validate] runpodctl bridge:"
test -f /root/a0/mcps/runpodctl/server.sh && echo "OK" || echo "MISSING"