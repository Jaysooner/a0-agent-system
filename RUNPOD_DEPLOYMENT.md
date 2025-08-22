# A0 Agent System - RunPod Deployment Guide

## Overview

This enhanced A0 Agent System includes:
- **Venice.ai API Integration** - Advanced AI model access
- **AgentMail SDK** - Email automation capabilities  
- **Local Assistant Pack** - PostgreSQL memory with pgvector
- **Bug Bounty Research Agent** - Security research capabilities
- **MCP Expert** - Model Context Protocol specialist
- **Enhanced MCP Servers** - Context7, web search, automation tools

## Quick Deployment

### 1. Environment Variables Setup

Set these environment variables in your RunPod pod:

```bash
# Core AI APIs
ANTHROPIC_API_KEY=your_anthropic_key
OPENAI_API_KEY=your_openai_key  
VENICE_API_KEY=your_venice_key

# AgentMail
AGENTMAIL_API_KEY=your_agentmail_key

# Database (optional - for local memory)
POSTGRES_USER=a0
POSTGRES_PASSWORD=a0pass
POSTGRES_DB=a0memory

# Search APIs (optional)
SERPER_API_KEY=your_serper_key
BRAVE_API_KEY=your_brave_key
```

### 2. Build and Deploy

```bash
# Clone your repository
git clone https://github.com/Jaysooner/a0-agent-system.git
cd a0-agent-system

# Build the Docker image
docker build -f docker/run/Dockerfile --build-arg BRANCH=main -t a0-enhanced .

# Run the container
docker run -d \
  --name a0-system \
  -p 22:22 \
  -p 80:80 \
  -p 9000-9009:9000-9009 \
  --env-file .env \
  a0-enhanced
```

## What Gets Installed Automatically

### 1. API Key Loading
- Automatically loads all `*_API_KEY` environment variables
- Supports ANTHROPIC_, AGENTMAIL_, VENICE_, POSTGRES_ prefixes
- Creates `.env` file in container for A0 to use

### 2. Enhanced MCP Servers
- **Venice.ai MCP** - Direct API integration
- **AgentMail MCP** - Email automation  
- **Context7 MCP** - Advanced context management
- **Web Search MCP** - Enhanced search capabilities
- **Playwright MCP** - Browser automation
- **RunPodCTL** - RunPod management bridge

### 3. Specialized Agents
- **Bug Bounty Research Agent** - Security research and analysis
- **MCP Expert** - Model Context Protocol specialist
- **Orchestrator** - Multi-agent coordination
- **Prompt Refiner** - Prompt optimization
- **Software Engineer** - Code generation and review

### 4. Local Assistant Pack (Optional)
- PostgreSQL with pgvector for embeddings
- Local memory persistence
- CLI tools for data management
- API server for external access

## Advanced Configuration

### Venice.ai Integration
The Venice.ai MCP server provides direct API access:
```json
{
  "mcps": {
    "venice": {
      "command": "node",
      "args": ["/git/agent-zero/mcps/venice/server.js"],
      "env": {
        "VENICE_API_KEY": "${VENICE_API_KEY}",
        "VENICE_API_BASE": "https://api.venice.ai"
      }
    }
  }
}
```

### AgentMail Setup
Configure email automation:
```bash
# Set in RunPod environment
AGENTMAIL_API_KEY=your_key
AGENTMAIL_SMTP_HOST=smtp.gmail.com
AGENTMAIL_SMTP_PORT=587
AGENTMAIL_EMAIL=your_email@domain.com
AGENTMAIL_PASSWORD=your_app_password
```

### Local Memory Database
The PostgreSQL instance provides:
- Vector embeddings with pgvector
- Persistent conversation memory
- Cross-session knowledge retention
- API access on port 8088

## Networking

### Exposed Ports
- **22** - SSH access
- **80** - Web UI
- **9000-9009** - Various services
- **8088** - Local assistant API (if enabled)
- **5432** - PostgreSQL (if using local DB)

### Access URLs
- Main UI: `http://your-runpod-ip`
- SSH: `ssh root@your-runpod-ip`
- API: `http://your-runpod-ip:8088` (if local assistant enabled)

## Troubleshooting

### Check Logs
```bash
# Container logs
docker logs a0-system

# A0 specific logs
docker exec a0-system tail -f /git/agent-zero/logs/latest.log

# MCP server logs
docker exec a0-system journalctl -u mcp-servers
```

### Environment Variables
```bash
# Verify API keys loaded
docker exec a0-system cat /git/agent-zero/.env

# Check installed components
docker exec a0-system ls -la /git/agent-zero/mcps/
docker exec a0-system ls -la /git/agent-zero/agents/
```

### Common Issues

1. **API Keys Not Loading**
   - Ensure environment variables are set in RunPod
   - Check `/git/agent-zero/.env` in container
   - Verify naming convention: `*_API_KEY`

2. **MCP Servers Not Starting**
   - Check Node.js dependencies: `npm list -g`
   - Verify server files: `ls /git/agent-zero/mcps/*/`
   - Check individual server logs

3. **Memory Issues**
   - Increase RunPod instance memory
   - Check PostgreSQL logs if using local DB
   - Monitor system resources: `htop`

## Security Notes

- All API keys are loaded securely via environment variables
- SSH access requires proper key setup
- Web UI accessible without authentication by default
- Consider VPN or firewall rules for production use

## Performance Optimization

- **GPU Usage**: Venice.ai models can utilize GPU acceleration
- **Memory**: Recommended 16GB+ RAM for full functionality  
- **Storage**: 50GB+ for models and persistent data
- **Network**: High-speed connection recommended for model API calls

## Support

- GitHub Issues: https://github.com/Jaysooner/a0-agent-system/issues
- Agent Zero Documentation: /git/agent-zero/docs/
- Venice.ai API Docs: /git/agent-zero/docs/Venice.ai-API-Postman-Documentation.htm