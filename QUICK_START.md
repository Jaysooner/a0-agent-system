# A0 Enhanced - Quick Start Guide

## Overview
This is an enhanced version of Agent Zero with:
- 🚀 **RunPod-ready deployment**
- 🔑 **Automatic API key loading**
- 📧 **AgentMail SDK pre-installed** 
- 🌐 **Venice.ai integration**
- 🗄️ **PostgreSQL memory system**
- 🛠️ **Claude Code pre-installed**
- 🔧 **25+ specialized MCP agents**

## RunPod Deployment

### 1. Build & Push Image
```bash
# Build the enhanced image
docker build -f docker/run/Dockerfile --build-arg BRANCH=main -t a0-enhanced .

# Tag for your registry
docker tag a0-enhanced your-registry/a0-enhanced:latest

# Push to registry
docker push your-registry/a0-enhanced:latest
```

### 2. Deploy on RunPod
1. **Create new pod** with your image: `your-registry/a0-enhanced:latest`
2. **Set environment variables** for your API keys:
   ```
   ANTHROPIC_API_KEY=your_key_here
   OPENAI_API_KEY=your_key_here
   VENICE_API_KEY=your_key_here
   AGENTMAIL_API_KEY=your_key_here
   ```
3. **Expose port**: `8080`
4. **Start pod**

### 3. Access Your Agent
- Web UI: `https://your-pod-id-8080.proxy.runpod.net`
- API: `https://your-pod-id-8080.proxy.runpod.net/api`

## Local Development

### Quick Start
```bash
git clone https://github.com/Jaysooner/a0-agent-system.git
cd a0-agent-system
docker compose up -d
```

### With Memory System
```bash
cd local-assistant-pack
cp .env.example .env
# Edit .env with your API keys
docker compose up -d
```

## Features

### Available Agents
- **Code Agent** - Software development
- **Research Agent** - Web research & analysis  
- **Email Agent** - Email automation via AgentMail
- **Venice Agent** - AI model interactions
- **Memory Agent** - Long-term memory management
- **And 20+ more specialized agents**

### API Endpoints
- `POST /api/chat` - Chat with agents
- `POST /api/memory/import` - Import memory data
- `GET /api/agents` - List available agents
- `GET /api/health` - Health check

### Environment Variables
See `.env.runpod.example` for complete list of supported variables.

## Troubleshooting

### Common Issues
1. **Missing API keys**: Check environment variables are set
2. **Port conflicts**: Ensure port 8080 is available
3. **Memory issues**: Increase container memory allocation
4. **Build failures**: Ensure Docker has sufficient disk space

### Logs
```bash
# Container logs
docker logs a0-enhanced

# Agent logs
tail -f /exe/logs/agent.log
```

## Next Steps
- Configure additional MCP servers in `/exe/mcps/`
- Customize agents in `/exe/agents/`
- Import your existing memory data
- Set up email automation with AgentMail

For detailed deployment instructions, see `RUNPOD_DEPLOYMENT.md`