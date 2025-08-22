import os, sys, requests, json

API = os.getenv("A0_LOCAL_API","http://localhost:8088")

def chat(text, conv=None):
    payload = {"user": text, "conversation_id": conv, "use_memory": True}
    r = requests.post(f"{API}/chat", json=payload, timeout=120)
    r.raise_for_status()
    data = r.json()
    print(f"[assistant] {data['reply']}")
    return data["conversation_id"]

if __name__ == "__main__":
    conv = None
    print("Type to chat. Ctrl+C to exit.")
    try:
        while True:
            msg = input("> ").strip()
            if not msg: continue
            conv = chat(msg, conv)
    except KeyboardInterrupt:
        print("\nbye")
