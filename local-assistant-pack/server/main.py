import os, json, time
from typing import List, Optional, Dict, Any
from fastapi import FastAPI, Body, HTTPException, Query
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv
import requests
from openai import OpenAI

load_dotenv()

PROVIDER = os.getenv("PROVIDER", "openai")

# DB
def db():
    conn = psycopg2.connect(
        host=os.getenv("PG_HOST","pgmemory"),
        port=int(os.getenv("PG_PORT","5432")),
        user=os.getenv("POSTGRES_USER","a0"),
        password=os.getenv("POSTGRES_PASSWORD","a0pass"),
        dbname=os.getenv("POSTGRES_DB","a0memory"),
    )
    return conn

# Simple memory search (FTS)
def search_memories(q: str, limit: int = 8):
    conn = db()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute(
        """
        SELECT id, scope, title, left(content, 800) AS snippet
        FROM memories
        WHERE to_tsvector('english', title || ' ' || content) @@ plainto_tsquery('english', %s)
        ORDER BY updated_at DESC
        LIMIT %s
        """, (q, limit)
    )
    rows = cur.fetchall()
    cur.close(); conn.close()
    return rows

# Chat models
def call_openai(messages):
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    model = os.getenv("OPENAI_MODEL","gpt-5")
    resp = client.chat.completions.create(model=model, messages=messages)
    return resp.choices[0].message.content

def call_openrouter(messages):
    api = "https://openrouter.ai/api/v1/chat/completions"
    key = os.getenv("OPENROUTER_API_KEY")
    model = os.getenv("OPENROUTER_MODEL","meta-llama/llama-3.1-70b-instruct")
    headers = {"Authorization": f"Bearer {key}"}
    payload = {"model": model, "messages": messages}
    r = requests.post(api, json=payload, headers=headers, timeout=180)
    if r.status_code != 200:
        raise HTTPException(status_code=500, detail=r.text)
    return r.json()["choices"][0]["message"]["content"]

def call_local(messages):
    base = os.getenv("LOCAL_API_BASE","http://vllm:8000/v1")
    model = os.getenv("LOCAL_MODEL","local")
    r = requests.post(f"{base}/chat/completions", json={"model": model, "messages": messages}, timeout=180)
    if r.status_code != 200:
        raise HTTPException(status_code=500, detail=r.text)
    return r.json()["choices"][0]["message"]["content"]

def run_model(messages):
    if PROVIDER == "openrouter":
        return call_openrouter(messages)
    if PROVIDER == "local":
        return call_local(messages)
    return call_openai(messages)

# Schemas
class ChatRequest(BaseModel):
    conversation_id: Optional[int] = None
    user: str
    use_memory: bool = True
    memory_query: Optional[str] = None
    system_prompt: Optional[str] = None

app = FastAPI()

@app.post("/chat")
def chat(req: ChatRequest):
    # ensure conversation
    conn = db(); cur = conn.cursor(cursor_factory=RealDictCursor)
    conv_id = req.conversation_id
    if conv_id is None:
        cur.execute("INSERT INTO conversations(name) VALUES(%s) RETURNING id", ("default",))
        conv_id = cur.fetchone()["id"]
    # build messages
    sys_msg = req.system_prompt or "You are a helpful assistant."
    messages = [{"role":"system","content":sys_msg}]
    # pull prior messages
    cur.execute("SELECT role, content FROM messages WHERE conversation_id=%s ORDER BY id ASC", (conv_id,))
    history = cur.fetchall()
    messages.extend([{"role": m["role"], "content": m["content"]} for m in history])
    # memory retrieval
    if req.use_memory:
        q = req.memory_query or req.user[:128]
        hits = search_memories(q, limit=8)
        if hits:
            mem_block = "\n".join([f"- [{h['scope']}] {h['title']}: {h['snippet']}" for h in hits])
            messages.append({"role":"system","content":f"Relevant long-term memory:\n{mem_block}"})
    # append user
    messages.append({"role":"user","content":req.user})
    # store user message
    cur.execute("INSERT INTO messages(conversation_id, role, content) VALUES(%s,%s,%s)", (conv_id,"user",req.user))
    conn.commit()
    # call model
    reply = run_model(messages)
    # store assistant
    cur.execute("INSERT INTO messages(conversation_id, role, content) VALUES(%s,%s,%s)", (conv_id,"assistant",reply))
    conn.commit()
    cur.close(); conn.close()
    return {"conversation_id": conv_id, "reply": reply}

# Import memory.json (same format we exported earlier)
@app.post("/import/memory")
def import_memory(file: Dict[str, Any] = Body(...)):
    data = file
    items = []
    prefs = data.get("preferences",{})
    if prefs.get("style"):
        items.append(("preference","style",prefs["style"]))
    if prefs.get("deliverables"):
        items.append(("preference","deliverables",prefs["deliverables"]))
    for p in data.get("projects",[]):
        title = f"project:{p.get('name')}"
        items.append(("project", title, json.dumps(p, ensure_ascii=False)))
    for m in data.get("long_term_memories",[]):
        items.append(("persona", m["title"], m["summary"]))

    conn = db(); cur = conn.cursor()
    cur.executemany("INSERT INTO memories(scope,title,content) VALUES(%s,%s,%s)", items)
    conn.commit(); cur.close(); conn.close()
    return {"inserted": len(items)}

# Import chat log (simple JSON lines: {"role": "...", "content": "..."})
class ChatLogImport(BaseModel):
    conversation_id: Optional[int] = None
    name: Optional[str] = "imported"
    messages: List[Dict[str,str]]

@app.post("/import/chat")
def import_chat(payload: ChatLogImport):
    conn = db(); cur = conn.cursor()
    conv_id = payload.conversation_id
    if conv_id is None:
        cur.execute("INSERT INTO conversations(name) VALUES(%s) RETURNING id", (payload.name,))
        conv_id = cur.fetchone()[0]
    rows = [(conv_id, m["role"], m["content"]) for m in payload.messages]
    cur.executemany("INSERT INTO messages(conversation_id, role, content) VALUES(%s,%s,%s)", rows)
    conn.commit(); cur.close(); conn.close()
    return {"conversation_id": conv_id, "inserted": len(rows)}

# Search memories endpoint
@app.get("/memories/search")
def memories_search(q: str = Query(...), limit: int = Query(8)):
    return search_memories(q, limit=limit)
