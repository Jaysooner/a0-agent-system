CREATE EXTENSION IF NOT EXISTS vector;

-- memories store (shared with earlier pack)
CREATE TABLE IF NOT EXISTS memories (
  id BIGSERIAL PRIMARY KEY,
  scope TEXT NOT NULL,
  title TEXT NOT NULL,
  content TEXT NOT NULL,
  created_at TIMESTAMPTZ DEFAULT now(),
  updated_at TIMESTAMPTZ DEFAULT now(),
  embedding vector(1536)
);
CREATE INDEX IF NOT EXISTS idx_mem_scope ON memories(scope);
CREATE INDEX IF NOT EXISTS idx_mem_fts ON memories USING GIN (to_tsvector('english', title || ' ' || content));

-- conversations & messages
CREATE TABLE IF NOT EXISTS conversations (
  id BIGSERIAL PRIMARY KEY,
  name TEXT,
  created_at TIMESTAMPTZ DEFAULT now()
);
CREATE TABLE IF NOT EXISTS messages (
  id BIGSERIAL PRIMARY KEY,
  conversation_id BIGINT REFERENCES conversations(id) ON DELETE CASCADE,
  role TEXT NOT NULL, -- system|user|assistant|tool
  content TEXT NOT NULL,
  created_at TIMESTAMPTZ DEFAULT now()
);
