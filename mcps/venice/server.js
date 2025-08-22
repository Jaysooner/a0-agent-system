#!/usr/bin/env node
import { fetch } from 'undici';

const API = process.env.VENICE_API_BASE || 'https://api.venice.ai';
const KEY = process.env.VENICE_API_KEY || '';

if (!KEY) console.error('[venice-mcp] VENICE_API_KEY is not set (will 401)');

process.stdin.setEncoding('utf8');
process.stdin.on('data', async (chunk) => {
  try {
    const req = JSON.parse(chunk.trim());
    const res = await fetch(`${API}${req.path}`, {
      method: req.method || 'POST',
      headers: {
        'Authorization': `Bearer ${KEY}`,
        'Content-Type': 'application/json'
      },
      body: req.body ? JSON.stringify(req.body) : undefined
    });
    const text = await res.text();
    process.stdout.write(JSON.stringify({ status: res.status, body: text })+'\n');
  } catch (e) {
    process.stdout.write(JSON.stringify({ error: String(e) })+'\n');
  }
});
