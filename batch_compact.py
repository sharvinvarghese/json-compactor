#!/usr/bin/env python3
"""
batch_compact.py
----------------
Batch-compact all JSON files in a folder.
Useful for compressing datasets, API response caches, or config bundles.
"""

import os
import json
import argparse
from json_compactor import compact_json


def batch_process(folder: str, output_folder: str = None, sort_keys: bool = False):
    files = [f for f in os.listdir(folder) if f.endswith('.json')]
    if not files:
        print("No JSON files found.")
        return

    total_original = 0
    total_compact = 0

    out_dir = output_folder or os.path.join(folder, "compacted")
    os.makedirs(out_dir, exist_ok=True)

    for fname in files:
        fpath = os.path.join(folder, fname)
        with open(fpath, 'r', encoding='utf-8') as f:
            raw = f.read()
        try:
            compacted = compact_json(raw, sort_keys)
            orig = len(raw.encode('utf-8'))
            comp = len(compacted.encode('utf-8'))
            total_original += orig
            total_compact += comp
            out_path = os.path.join(out_dir, fname)
            with open(out_path, 'w', encoding='utf-8') as f:
                f.write(compacted)
            pct = round((orig - comp) / orig * 100, 1) if orig > 0 else 0
            print(f"  ✅ {fname}: {orig:,} → {comp:,} bytes ({pct}% saved)")
        except json.JSONDecodeError as e:
            print(f"  ❌ {fname}: Invalid JSON — {e}")

    if total_original > 0:
        total_saved = total_original - total_compact
        total_pct = round(total_saved / total_original * 100, 2)
        token_saved = total_saved // 4
        print(f"\n📊 Total: {total_original:,} → {total_compact:,} bytes")
        print(f"💾 Saved : {total_saved:,} bytes ({total_pct}%)")
        print(f"🪙 Estimated tokens saved: ~{token_saved:,}")
        print(f"📁 Output : {out_dir}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Batch compact JSON files in a folder.")
    parser.add_argument("folder", help="Folder containing .json files")
    parser.add_argument("-o", "--output", help="Output folder (default: <folder>/compacted)")
    parser.add_argument("--sort-keys", action="store_true", help="Sort JSON keys")
    args = parser.parse_args()
    batch_process(args.folder, args.output, args.sort_keys)
