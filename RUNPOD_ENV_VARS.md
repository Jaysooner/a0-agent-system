# SUPER_AGENT_0 - Environment Variables for RunPod

## 🔑 Required API Keys

Copy and paste these into your RunPod environment variables:

```bash
ANTHROPIC_API_KEY=sk-ant-your-anthropic-key-here
OPENAI_API_KEY=sk-your-openai-key-here
VENICE_API_KEY=your-venice-api-key-here
AGENTMAIL_API_KEY=your-agentmail-api-key-here
```

## 🔧 Optional Configuration

```bash
# Database Configuration
POSTGRES_USER=a0
POSTGRES_PASSWORD=a0pass
POSTGRES_DB=a0memory
PG_HOST=localhost
PG_PORT=5432

# Embedding Models
EMBED_MODEL=text-embedding-3-large
EMBED_DIM=3072

# Venice.ai Configuration
VENICE_API_BASE=https://api.venice.ai

# AgentMail Configuration
AGENTMAIL_SMTP_HOST=smtp.gmail.com
AGENTMAIL_SMTP_PORT=587
AGENTMAIL_EMAIL=your-email@gmail.com
AGENTMAIL_APP_PASSWORD=your-app-password

# OpenRouter (Alternative to OpenAI)
OPENROUTER_API_KEY=sk-or-your-openrouter-key
OPENROUTER_MODEL=meta-llama/llama-3.1-70b-instruct

# Local Model Configuration
LOCAL_API_BASE=http://localhost:8000/v1
LOCAL_MODEL=local

# Provider Selection
PROVIDER=openai
```

## 📋 RunPod Template Variables

When creating your RunPod template, add these environment variables:

| Variable Name | Description | Required |
|---------------|-------------|----------|
| `ANTHROPIC_API_KEY` | Your Claude API key from Anthropic | ✅ |
| `OPENAI_API_KEY` | Your OpenAI API key | ✅ |
| `VENICE_API_KEY` | Your Venice.ai API key | ✅ |
| `AGENTMAIL_API_KEY` | Your AgentMail API key for email automation | ✅ |
| `POSTGRES_PASSWORD` | Custom database password (optional) | ❌ |
| `EMBED_MODEL` | Embedding model for vector search | ❌ |
| `PROVIDER` | AI provider selection (openai/anthropic/venice) | ❌ |

## 🚀 Quick Setup for RunPod

1. **Go to RunPod** → Create Pod → Use Template
2. **Search for:** `SUPER_AGENT_0`
3. **Add Environment Variables** (copy from Required section above)
4. **Set Port:** `8080`
5. **Deploy**

## 🔐 Where to Get API Keys

### Anthropic (Claude)
- Go to: https://console.anthropic.com/
- Create account → API Keys → Create Key
- Format: `sk-ant-...`

### OpenAI
- Go to: https://platform.openai.com/api-keys
- Create account → API Keys → Create new secret key
- Format: `sk-...`

### Venice.ai
- Go to: https://venice.ai/
- Sign up → Dashboard → API Keys
- Format: Custom format

### AgentMail
- Go to: https://agentmail.ai/
- Create account → API Keys → Generate key
- Format: `am_...`

## ⚠️ Security Notes

- **Never share** your API keys publicly
- **Use environment variables** only - don't hardcode in files
- **Rotate keys** regularly for security
- **Monitor usage** to prevent unexpected charges

## 🧪 Test Your Setup

After deployment, verify your environment variables:

```bash
curl https://your-pod-8080.proxy.runpod.net/health
```

Should return:
```json
{
  "status": "healthy",
  "anthropic": "configured",
  "openai": "configured",
  "venice": "configured",
  "agentmail": "configured"
}
```