import os, typer
from fastapi import FastAPI
import uvicorn

app = FastAPI(title="AgentMail MCP")

@app.get("/health")
def health():
    ok = all(os.getenv(k) for k in ["AGENTMAIL_IMAP_HOST","AGENTMAIL_IMAP_USER","AGENTMAIL_IMAP_PASS"])
    return {"ok": ok}

def main():
    uvicorn.run(app, host="127.0.0.1", port=0)

if __name__ == "__main__":
    typer.run(main)
