# Use the pre-built base image for A0
# FROM agent-zero-base:local
FROM agent0ai/agent-zero-base:latest

# Check if the argument is provided, else throw an error
ARG BRANCH
RUN if [ -z "$BRANCH" ]; then echo "ERROR: BRANCH is not set!" >&2; exit 1; fi
ENV BRANCH=$BRANCH

# Copy filesystem files to root
COPY ./fs/ /

# pre installation steps
RUN bash /ins/pre_install.sh $BRANCH

# install A0
RUN bash /ins/install_A0.sh $BRANCH

# install additional software
RUN bash /ins/install_additional.sh $BRANCH

# Install additional Python packages and dependencies
RUN pip install --no-cache-dir \
    anthropic \
    claude-code \
    agentmail \
    fastapi \
    uvicorn \
    httpx \
    aiofiles \
    python-multipart \
    psycopg2-binary \
    pgvector \
    typer \
    rich \
    click \
    imapclient \
    mailparser \
    && pip cache purge

# Install Node.js tools for MCP servers and dependencies
RUN npm install -g \
    @upstash/context7-mcp \
    agentmail-mcp \
    playwright-mcp \
    web-search-mcp \
    http-checker-mcp \
    report-gen-mcp \
    intel-feeds-mcp \
    undici

# Create tools directory and copy MCP server files
RUN mkdir -p /git/agent-zero/tools && \
    mkdir -p /git/agent-zero/tools/agentmail-mcp && \
    mkdir -p /git/agent-zero/tools/web-search-mcp && \
    mkdir -p /git/agent-zero/tools/playwright-mcp && \
    mkdir -p /git/agent-zero/tools/http-checker-mcp && \
    mkdir -p /git/agent-zero/tools/report-gen-mcp && \
    mkdir -p /git/agent-zero/tools/intel-feeds-mcp

# Create basic MCP server files
RUN echo 'console.log("AgentMail MCP Server starting...");' > /git/agent-zero/tools/agentmail-mcp/server.js && \
    echo 'console.log("Web Search MCP Server starting...");' > /git/agent-zero/tools/web-search-mcp/server.js && \
    echo 'console.log("Playwright MCP Server starting...");' > /git/agent-zero/tools/playwright-mcp/server.js && \
    echo 'console.log("HTTP Checker MCP Server starting...");' > /git/agent-zero/tools/http-checker-mcp/server.js && \
    echo 'console.log("Report Gen MCP Server starting...");' > /git/agent-zero/tools/report-gen-mcp/server.js && \
    echo 'console.log("Intel Feeds MCP Server starting...");' > /git/agent-zero/tools/intel-feeds-mcp/server.js

# Set up API key loading script
RUN echo '#!/bin/bash' > /exe/load_api_keys.sh && \
    echo 'echo "Loading API keys from environment variables..."' >> /exe/load_api_keys.sh && \
    echo 'if [ ! -f /git/agent-zero/.env ]; then' >> /exe/load_api_keys.sh && \
    echo '    touch /git/agent-zero/.env' >> /exe/load_api_keys.sh && \
    echo 'fi' >> /exe/load_api_keys.sh && \
    echo 'for var in $(env | grep -E "^[A-Z_]+_API_KEY="); do' >> /exe/load_api_keys.sh && \
    echo '    key=$(echo "$var" | cut -d= -f1)' >> /exe/load_api_keys.sh && \
    echo '    value=$(echo "$var" | cut -d= -f2-)' >> /exe/load_api_keys.sh && \
    echo '    echo "$key=$value" >> /git/agent-zero/.env' >> /exe/load_api_keys.sh && \
    echo 'done' >> /exe/load_api_keys.sh && \
    echo 'for var in $(env | grep -E "^AGENTMAIL_"); do' >> /exe/load_api_keys.sh && \
    echo '    key=$(echo "$var" | cut -d= -f1)' >> /exe/load_api_keys.sh && \
    echo '    value=$(echo "$var" | cut -d= -f2-)' >> /exe/load_api_keys.sh && \
    echo '    echo "$key=$value" >> /git/agent-zero/.env' >> /exe/load_api_keys.sh && \
    echo 'done' >> /exe/load_api_keys.sh && \
    echo 'for var in $(env | grep -E "^ANTHROPIC_"); do' >> /exe/load_api_keys.sh && \
    echo '    key=$(echo "$var" | cut -d= -f1)' >> /exe/load_api_keys.sh && \
    echo '    value=$(echo "$var" | cut -d= -f2-)' >> /exe/load_api_keys.sh && \
    echo '    echo "$key=$value" >> /git/agent-zero/.env' >> /exe/load_api_keys.sh && \
    echo 'done' >> /exe/load_api_keys.sh && \
    echo 'for var in $(env | grep -E "^VENICE_"); do' >> /exe/load_api_keys.sh && \
    echo '    key=$(echo "$var" | cut -d= -f1)' >> /exe/load_api_keys.sh && \
    echo '    value=$(echo "$var" | cut -d= -f2-)' >> /exe/load_api_keys.sh && \
    echo '    echo "$key=$value" >> /git/agent-zero/.env' >> /exe/load_api_keys.sh && \
    echo 'done' >> /exe/load_api_keys.sh && \
    echo 'for var in $(env | grep -E "^POSTGRES_"); do' >> /exe/load_api_keys.sh && \
    echo '    key=$(echo "$var" | cut -d= -f1)' >> /exe/load_api_keys.sh && \
    echo '    value=$(echo "$var" | cut -d= -f2-)' >> /exe/load_api_keys.sh && \
    echo '    echo "$key=$value" >> /git/agent-zero/.env' >> /exe/load_api_keys.sh && \
    echo 'done' >> /exe/load_api_keys.sh && \
    echo 'echo "API keys loaded successfully"' >> /exe/load_api_keys.sh && \
    chmod +x /exe/load_api_keys.sh

# Install a0-bundle components
RUN echo '#!/bin/bash' > /exe/install_bundle.sh && \
    echo 'cd /git/agent-zero' >> /exe/install_bundle.sh && \
    echo 'if [ -f "./scripts/install_a0_bundle.sh" ]; then' >> /exe/install_bundle.sh && \
    echo '    bash ./scripts/install_a0_bundle.sh' >> /exe/install_bundle.sh && \
    echo 'fi' >> /exe/install_bundle.sh && \
    chmod +x /exe/install_bundle.sh

# cleanup repo and install A0 without caching, this speeds up builds
ARG CACHE_DATE=none
RUN echo "cache buster $CACHE_DATE" && bash /ins/install_A02.sh $BRANCH

# post installation steps
RUN bash /ins/post_install.sh $BRANCH

# Expose ports
EXPOSE 22 80 9000-9009

RUN chmod +x /exe/initialize.sh /exe/run_A0.sh /exe/run_searxng.sh /exe/run_tunnel_api.sh

# Load API keys, install bundle, and initialize runtime
CMD ["/bin/bash", "-c", "/exe/load_api_keys.sh && /exe/install_bundle.sh && /exe/initialize.sh $BRANCH"]
