# A0 Local Assistant Pack — Host chats & memories locally

This gives you a local service that:
- Stores **conversations** and **memories** in Postgres (pgvector-ready).
- Retrieves relevant memories and injects them into prompts.
- Calls **OpenAI**, **OpenRouter**, or **local vLLM** (OpenAI-compatible).
- Imports the **exported memory.json** from our chat.

## Quick start
```bash
unzip a0-local-assistant-pack.zip
cd a0-local-assistant-pack

cp .env.example .env    # set PROVIDER + keys
docker compose up -d    # launches Postgres + API

# talk
python3 cli.py
# or POST to http://localhost:8088/chat with JSON body:
# {"user":"hello world"}
```

## Use your exported context
`POST /import/memory` with the JSON we exported earlier (memory.json):
```bash
curl -X POST http://localhost:8088/import/memory   -H "Content-Type: application/json"   --data-binary @../a0-memory-export/memory.json
```

## Import chat history
`POST /import/chat`
```json
{
  "name": "chatgpt-thread-1",
  "messages": [
    {"role":"user","content":"hi"},
    {"role":"assistant","content":"hello!"}
  ]
}
```

## Switch models
- **OpenAI**: set `PROVIDER=openai`, `OPENAI_API_KEY`, `OPENAI_MODEL` in `.env`
- **OpenRouter**: set `PROVIDER=openrouter`, `OPENROUTER_API_KEY`, `OPENROUTER_MODEL`
- **Local vLLM**: set `PROVIDER=local`, start a vLLM container exposing `/v1/chat/completions`, and set `LOCAL_API_BASE` + `LOCAL_MODEL`

## Does the exported memory work with other models?
**Yes.** The export is plain JSON/Markdown. Any model (OpenAI, OpenRouter, local) can use it via the retrieval layer:
- We search the `memories` table (FTS or vector).
- We prepend top hits as a **system memory block**.
- The downstream model is model-agnostic.

## Tables
- `memories(scope, title, content, embedding?)`
- `conversations(id, name)`
- `messages(conversation_id, role, content)`

## Endpoints
- `POST /chat` — chat with optional memory retrieval
- `POST /import/memory` — import exported memory.json
- `POST /import/chat` — import a thread
- `GET /memories/search?q=...` — search memories

Optionally plug embeddings to fill `embedding` and enable vector search.
