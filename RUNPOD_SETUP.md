# Agent Zero RunPod Setup Guide

This guide explains how to deploy Agent Zero on RunPod with all necessary dependencies and API key configuration.

## 🚀 Quick Start

### 1. Build the Docker Image

```bash
# Build the local development image
docker build -f DockerfileLocal -t agent-zero:local .

# Or build the production image
docker build -f docker/run/Dockerfile -t agent-zero:latest .

# Build with Venice API key (optional)
docker build --build-arg VENICE_API_KEY=your_venice_key -f DockerfileLocal -t agent-zero:local .
```

### 2. Deploy on RunPod

When creating a RunPod container, use the following configuration:

#### Environment Variables

Set these environment variables in your RunPod container:

**Required API Keys:**
```bash
# Anthropic API Key (for Claude models)
ANTHROPIC_API_KEY=your_anthropic_api_key_here

# AgentMail Configuration
AGENTMAIL_API_KEY=your_agentmail_api_key_here
AGENTMAIL_DEFAULT_PROVIDER=gmail
AGENTMAIL_SENDER=your_email@example.com
AGENTMAIL_SAFE_MODE=true

# Venice API Key (optional - for Venice AI models)
VENICE_API_KEY=your_venice_api_key_here

# Optional: Other API Keys
OPENAI_API_KEY=your_openai_api_key_here
GOOGLE_API_KEY=your_google_api_key_here
GROQ_API_KEY=your_groq_api_key_here
```

**System Configuration:**
```bash
# Branch to use (default: local)
BRANCH=local

# Web UI Configuration
WEB_UI_HOST=0.0.0.0
WEB_UI_PORT=80

# Authentication (optional)
AUTH_LOGIN=admin
AUTH_PASSWORD=your_password_here
```

#### Port Configuration

Expose these ports in RunPod:
- **Port 80**: Web UI
- **Port 22**: SSH access
- **Port 8000**: FastAPI health checks and Swagger UI
- **Port 8888**: Jupyter Lab
- **Ports 9000-9009**: Additional services

#### Container Settings

- **Container Disk**: 50GB minimum
- **GPU**: Optional (for local models)
- **RAM**: 8GB minimum, 16GB recommended
- **CPU**: 4 cores minimum, 8 cores recommended

## 📦 What's Included

### Python Dependencies
- **anthropic**: Official Anthropic Python SDK
- **claude-code**: Claude Code execution capabilities
- **agentmail**: AgentMail Python SDK for email automation
- **fastapi**: Fast API framework
- **uvicorn**: ASGI server
- **httpx**: HTTP client
- **aiofiles**: Async file operations
- **python-multipart**: File upload support
- **runpod**: RunPod Python SDK
- **jupyterlab**: Jupyter Lab for interactive development

### Node.js MCP Servers
- **@upstash/context7-mcp**: Context management
- **agentmail-mcp**: Email automation MCP server

### RunPod Integration
- **RunPod CLI (runpodctl)**: Command-line interface for RunPod
- **FastAPI Health Checks**: Health monitoring at `/health`
- **Swagger UI**: API documentation at `/docs`
- **Jupyter Lab**: Interactive development environment
- **Venice API Integration**: Support for Venice AI models

### Pre-configured Agents
- **Orchestrator**: Coordinates sub-agents and tools
- **AgentMail Worker**: Executes email-related tasks
- **Prompt Refiner**: Optimizes prompts
- **Software Engineer**: Code generation and review
- **MCP Expert**: Manages MCP server connections

## 🔧 API Key Loading

The Docker image automatically loads API keys from environment variables into the `.env` file on startup. The script looks for:

1. **Any variable ending with `_API_KEY`** (e.g., `ANTHROPIC_API_KEY`, `OPENAI_API_KEY`, `VENICE_API_KEY`)
2. **AgentMail variables** (e.g., `AGENTMAIL_API_KEY`, `AGENTMAIL_DEFAULT_PROVIDER`)
3. **Anthropic variables** (e.g., `ANTHROPIC_API_KEY`)

### Example Environment Variables

```bash
# Core API Keys
ANTHROPIC_API_KEY=sk-ant-api03-...
OPENAI_API_KEY=sk-...
GOOGLE_API_KEY=AIza...
VENICE_API_KEY=your_venice_key_here

# AgentMail Configuration
AGENTMAIL_API_KEY=your_agentmail_key
AGENTMAIL_DEFAULT_PROVIDER=gmail
AGENTMAIL_SENDER=your_email@gmail.com
AGENTMAIL_SAFE_MODE=true

# Optional: Additional providers
GROQ_API_KEY=gsk_...
MISTRAL_API_KEY=your_mistral_key
```

## 🎯 Usage Examples

### 1. Email Automation with AgentMail

```python
# The AgentMail worker can:
# - Login to email providers
# - Search and fetch emails
# - Compose and send emails
# - Handle attachments
# - Monitor mailboxes for new messages
```

### 2. Code Generation with Claude Code

```python
# Claude Code provides:
# - Advanced code generation
# - Code review and analysis
# - Multi-file project support
# - Context-aware coding
```

### 3. RunPod Integration

The image includes RunPod-specific features:
- **Health Checks**: Visit `http://your-pod:8000/health` for status
- **API Documentation**: Visit `http://your-pod:8000/docs` for Swagger UI
- **Venice Integration**: Check Venice API key status at `http://your-pod:8000/venice`
- **Jupyter Lab**: Access at `http://your-pod:8888` for interactive development
- **RunPod CLI**: Use `runpodctl` for RunPod management

### 4. Alternative Startup Modes

You can start the container with different modes:

```bash
# Standard Agent Zero mode (default)
docker run ... agent-zero:latest

# RunPod extras mode (FastAPI + Jupyter)
docker run ... agent-zero:latest /usr/local/bin/start-a0-extras
```

## 🔍 Troubleshooting

### Common Issues

1. **API Keys Not Loading**
   - Check that environment variables are properly set in RunPod
   - Verify the variable names match the expected format
   - Check container logs for API key loading messages

2. **Port Access Issues**
   - Confirm ports are exposed in RunPod configuration
   - Check firewall settings
   - Verify the container is running on the correct ports

3. **RunPod Integration Issues**
   - Ensure RunPod SDK is installed: `pip install runpod`
   - Check RunPod CLI installation: `runpodctl --version`
   - Verify FastAPI health endpoint: `curl http://localhost:8000/health`

### Logs and Debugging

```bash
# Check container logs
docker logs <container_id>

# Access the container shell
docker exec -it <container_id> /bin/bash

# Check API key loading
cat /git/agent-zero/.env

# Test health endpoint
curl http://localhost:8000/health

# Check Venice API key
curl http://localhost:8000/venice

# Access Jupyter Lab
# Open browser to http://your-pod:8888
```

## 🔐 Security Considerations

1. **API Key Security**
   - Never commit API keys to version control
   - Use RunPod's secure environment variable storage
   - Rotate keys regularly
   - Use least-privilege access

2. **Network Security**
   - Use HTTPS for external access
   - Configure proper authentication
   - Limit port exposure to necessary services

3. **Container Security**
   - Keep the base image updated
   - Scan for vulnerabilities
   - Use non-root user when possible

## 📚 Additional Resources

- [Agent Zero Documentation](https://github.com/agent0ai/agent-zero)
- [RunPod Documentation](https://docs.runpod.io/)
- [AgentMail Documentation](https://agentmail.ai/)
- [Anthropic Claude Documentation](https://docs.anthropic.com/)
- [Venice AI Documentation](https://venice.ai/)

## 🤝 Support

For issues with this Docker image:
1. Check the troubleshooting section above
2. Review container logs
3. Verify environment variable configuration
4. Open an issue on the GitHub repository

---

**Note**: This Docker image is optimized for RunPod deployment and includes all necessary dependencies for Agent Zero with AgentMail, Claude Code, and RunPod integration.
