import json, sys, argparse, os

def deep_merge(a, b):
    if isinstance(a, dict) and isinstance(b, dict):
        out = dict(a)
        for k, v in b.items():
            out[k] = deep_merge(out.get(k), v) if k in out else v
        return out
    return b if b is not None else a

p = argparse.ArgumentParser()
p.add_argument('--base', required=True)
p.add_argument('--overlay', required=True)
p.add_argument('--out', required=True)
args = p.parse_args()

base = {}
if os.path.exists(args.base):
    with open(args.base) as f: base = json.load(f)

with open(args.overlay) as f: overlay = json.load(f)

merged = deep_merge(base, overlay)
os.makedirs(os.path.dirname(args.out), exist_ok=True)
with open(args.out, 'w') as f: json.dump(merged, f, indent=2)
print(f"[merge_json] wrote {args.out}")