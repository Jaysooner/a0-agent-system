# Build Instructions for A0 Enhanced

## Docker Build Process

### Local Build
```bash
# From the a0 directory
docker build -f docker/run/Dockerfile --build-arg BRANCH=main -t a0-enhanced .
```

### For Registry Push
```bash
# Build with registry tag
docker build -f docker/run/Dockerfile --build-arg BRANCH=main -t your-registry/a0-enhanced:latest .

# Push to registry
docker push your-registry/a0-enhanced:latest
```

## Build Features

### Automatic Installation
The Dockerfile automatically installs:
- ✅ **AgentMail Python SDK**
- ✅ **Claude Code CLI**
- ✅ **Venice.ai MCP server**
- ✅ **PostgreSQL client libraries**
- ✅ **Node.js dependencies for MCP servers**
- ✅ **A0 Bundle (agents & MCP servers)**
- ✅ **API key loading system**

### Build Arguments
- `BRANCH` - Git branch to clone (default: main)

### Environment Detection
The build process detects and loads:
- API keys matching pattern `*_API_KEY`
- Database credentials
- Service endpoints
- Model configurations

## Build Time Expectations

### Typical Build Times
- **First build**: 15-20 minutes (downloads base image)
- **Subsequent builds**: 5-10 minutes (uses cache)
- **With registry push**: +2-5 minutes

### Build Requirements
- **Disk space**: ~8GB free
- **Memory**: 4GB+ recommended
- **Network**: Stable connection for downloads

## Troubleshooting Build Issues

### Common Problems

#### 1. Network Timeouts
```bash
# Increase timeout
export DOCKER_CLIENT_TIMEOUT=300
export COMPOSE_HTTP_TIMEOUT=300
```

#### 2. Disk Space Issues
```bash
# Clean up Docker
docker system prune -a
```

#### 3. Memory Issues
```bash
# Increase Docker memory in Docker Desktop
# Or add swap space on Linux
sudo fallocate -l 4G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
```

#### 4. Base Image Issues
```bash
# Pull base image manually
docker pull agent0ai/agent-zero-base:latest
```

### Build Logs
To monitor build progress:
```bash
docker build -f docker/run/Dockerfile --build-arg BRANCH=main -t a0-enhanced . --progress=plain
```

## Post-Build Verification

### Test the Image
```bash
# Run container
docker run -d --name a0-test -p 8080:8080 a0-enhanced

# Check logs
docker logs a0-test

# Test health endpoint
curl http://localhost:8080/health

# Cleanup
docker stop a0-test && docker rm a0-test
```

### Verify Components
```bash
# Check installed packages
docker run --rm a0-enhanced pip list | grep agentmail
docker run --rm a0-enhanced which claude
docker run --rm a0-enhanced ls /exe/mcps/
```

## Registry Deployment

### Docker Hub
```bash
docker tag a0-enhanced jaysooner/a0-enhanced:latest
docker push jaysooner/a0-enhanced:latest
```

### AWS ECR
```bash
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 123456789012.dkr.ecr.us-east-1.amazonaws.com
docker tag a0-enhanced 123456789012.dkr.ecr.us-east-1.amazonaws.com/a0-enhanced:latest
docker push 123456789012.dkr.ecr.us-east-1.amazonaws.com/a0-enhanced:latest
```

### Google Container Registry
```bash
docker tag a0-enhanced gcr.io/your-project/a0-enhanced:latest
docker push gcr.io/your-project/a0-enhanced:latest
```

## CI/CD Integration

### GitHub Actions Example
```yaml
name: Build and Push A0 Enhanced
on:
  push:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - name: Build Docker image
      run: docker build -f docker/run/Dockerfile --build-arg BRANCH=main -t a0-enhanced .
    - name: Push to registry
      run: |
        echo ${{ secrets.DOCKER_PASSWORD }} | docker login -u ${{ secrets.DOCKER_USERNAME }} --password-stdin
        docker tag a0-enhanced ${{ secrets.DOCKER_USERNAME }}/a0-enhanced:latest
        docker push ${{ secrets.DOCKER_USERNAME }}/a0-enhanced:latest
```

## Next Steps
After successful build:
1. Test locally with `docker run`
2. Push to your preferred registry
3. Deploy on RunPod or your cloud platform
4. Configure environment variables
5. Access via web UI at port 8080