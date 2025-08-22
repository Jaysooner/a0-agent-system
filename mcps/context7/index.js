#!/usr/bin/env node
import { spawn } from 'node:child_process';
const child = spawn('npx', ['-y', '@upstash/context7-mcp'], { stdio: 'inherit' });
child.on('exit', (c) => process.exit(c ?? 0));
