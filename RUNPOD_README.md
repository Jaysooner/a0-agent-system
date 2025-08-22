# SUPER_AGENT_0 - RunPod Deployment

**Template Name:** `SUPER_AGENT_0`  
**Enhanced Agent Zero with 25+ specialized agents for production deployment**

## 🚀 One-Click Deploy

### RunPod Setup
1. **Template:** Search `SUPER_AGENT_0` 
2. **Image:** `ghcr.io/jaysooner/a0-agent-system:latest`
3. **Port:** `8080`
4. **Disk:** 20GB minimum

### Required Environment Variables
```bash
ANTHROPIC_API_KEY=sk-ant-your-key-here
OPENAI_API_KEY=sk-your-openai-key  
VENICE_API_KEY=your-venice-key
AGENTMAIL_API_KEY=your-agentmail-key
```

### Access Your Deployment
- **Web UI:** `https://your-pod-id-8080.proxy.runpod.net`
- **API:** `https://your-pod-id-8080.proxy.runpod.net/api`

## 🤖 Enhanced Features

### Pre-installed Agents
- **Code Agent** - Development & debugging
- **Research Agent** - Web research & analysis  
- **Email Agent** - Automated email via AgentMail
- **Venice Agent** - Multi-model AI access
- **Memory Agent** - Persistent storage
- **Security Agent** - Code analysis
- **Data Agent** - Database operations
- **+ 18 more specialized agents**

### Production Tools
- ✅ **Claude Code** - AI coding assistant
- ✅ **AgentMail SDK** - Email automation  
- ✅ **Venice.ai** - Multi-model access
- ✅ **PostgreSQL** - Vector memory
- ✅ **25+ MCP Servers** - Extended capabilities

## ⚡ Quick Commands

### Health Check
```bash
curl https://your-pod-8080.proxy.runpod.net/health
```

### Chat API
```bash
curl -X POST https://your-pod-8080.proxy.runpod.net/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Help me code a Python function"}'
```

### Memory Import
```bash
curl -X POST https://your-pod-8080.proxy.runpod.net/api/memory/import \
  -H "Content-Type: application/json" \
  --data-binary @memory.json
```

## 🔧 Configuration

### Container Requirements
- **Memory:** 8GB recommended
- **Storage:** 20GB container disk
- **Network:** Port 8080 exposed
- **GPU:** Optional (CPU supported)

### Optional Environment Variables
```bash
# Database
POSTGRES_PASSWORD=custom_password

# Models  
EMBED_MODEL=text-embedding-3-large
EMBED_DIM=3072

# Venice.ai
VENICE_API_BASE=https://api.venice.ai
```

## 🛠 Troubleshooting

### Common Issues
| Issue | Solution |
|-------|----------|
| 503 Error | Wait 2-3 minutes for startup |
| API Key Error | Check environment variables |
| Memory Error | Increase container RAM |
| Port Error | Ensure 8080 is exposed |

### Startup Time
- **First boot:** 3-5 minutes
- **Subsequent boots:** 1-2 minutes
- **API available:** Check `/health` endpoint

### Logs Access
```bash
# View logs in RunPod console
# Or via API:
curl https://your-pod-8080.proxy.runpod.net/api/logs
```

## 📋 Auto-Updates

**GitHub Container Registry** builds automatically:
- **Repository:** `https://github.com/Jaysooner/a0-agent-system`
- **Registry:** `ghcr.io/jaysooner/a0-agent-system:latest`
- **Updates:** On every push to main branch

### Version Tags
- `latest` - Most recent build
- `sha-abc123` - Specific commit builds

## 🔄 Usage Examples

### Development Task
```json
{
  "message": "Create a FastAPI server with user authentication",
  "agent": "code"
}
```

### Research Task  
```json
{
  "message": "Research the latest trends in AI agent frameworks",
  "agent": "research"
}
```

### Email Automation
```json
{
  "message": "Send a follow-up email to client about project status", 
  "agent": "email"
}
```

---

**Template:** `SUPER_AGENT_0`  
**Repository:** `github.com/Jaysooner/a0-agent-system`  
**Image:** `ghcr.io/jaysooner/a0-agent-system:latest`