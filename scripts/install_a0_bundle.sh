#!/usr/bin/env bash
set -euo pipefail

A0_HOME="/root/a0"
BUNDLE="/root/a0-bundle"

echo "[a0-bundle] Installing into $A0_HOME"

mkdir -p "$A0_HOME/agents" "$A0_HOME/mcps" "$A0_HOME/config" "$A0_HOME/docs"

# Copy agents and MCPs
cp -r "$BUNDLE/agents/"* "$A0_HOME/agents/" 2>/dev/null || true
cp -r "$BUNDLE/mcps/"* "$A0_HOME/mcps/" 2>/dev/null || true

# Copy docs
cp -r "$BUNDLE/docs/"* "$A0_HOME/docs/" 2>/dev/null || true

# Merge config overrides if agent-zero.json exists
if [ -f "$A0_HOME/config/agent-zero.json" ]; then
  python3 "$BUNDLE/scripts/merge_json.py" \
    --base "$A0_HOME/config/agent-zero.json" \
    --overlay "$BUNDLE/config/agent_zero.overrides.json" \
    --out "$A0_HOME/config/agent-zero.json" || true
else
  cp "$BUNDLE/config/agent_zero.overrides.json" "$A0_HOME/config/agent-zero.json"
fi

# Also drop mcp.json for any client that loads it directly
cp "$BUNDLE/config/mcp.json" "$A0_HOME/config/mcp.json"

# Make runpodctl bridge executable
chmod +x "$A0_HOME/mcps/runpodctl/server.sh" 2>/dev/null || true

echo "[a0-bundle] Done."