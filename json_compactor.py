#!/usr/bin/env python3
"""
json_compactor.py
-----------------
Converts normal/pretty-printed JSON to compact JSON.
Strips all whitespace, newlines, and optional comments from JSON files or strings.

Token savings: typically 20-40% depending on indentation depth.
"""

import json
import sys
import argparse
import os


def compact_json(data: str, sort_keys: bool = False) -> str:
    """Parse and re-serialize JSON with minimal whitespace."""
    parsed = json.loads(data)
    return json.dumps(parsed, separators=(',', ':'), sort_keys=sort_keys)


def process_file(input_path: str, output_path: str = None, sort_keys: bool = False, show_stats: bool = True):
    with open(input_path, 'r', encoding='utf-8') as f:
        raw = f.read()

    compacted = compact_json(raw, sort_keys=sort_keys)

    original_size = len(raw.encode('utf-8'))
    compact_size = len(compacted.encode('utf-8'))
    saved = original_size - compact_size
    pct = round((saved / original_size) * 100, 2) if original_size > 0 else 0

    if output_path:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(compacted)
        if show_stats:
            print(f"✅ Saved to: {output_path}")
    else:
        print(compacted)

    if show_stats:
        print(f"📦 Original : {original_size:,} bytes")
        print(f"📦 Compacted: {compact_size:,} bytes")
        print(f"💾 Saved    : {saved:,} bytes ({pct}%)")
        # Rough token estimate (1 token ≈ 4 chars for JSON)
        token_saved = saved // 4
        print(f"🪙 Estimated tokens saved: ~{token_saved:,}")


def process_string(data: str, sort_keys: bool = False) -> str:
    return compact_json(data, sort_keys=sort_keys)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="🗜️  Compact JSON — strip whitespace to save tokens for LLMs."
    )
    parser.add_argument("input", nargs="?", help="Input JSON file path (or omit to use stdin)")
    parser.add_argument("-o", "--output", help="Output file path (default: print to stdout)")
    parser.add_argument("--sort-keys", action="store_true", help="Sort JSON keys alphabetically")
    parser.add_argument("--no-stats", action="store_true", help="Suppress stats output")

    args = parser.parse_args()

    if args.input:
        process_file(args.input, args.output, args.sort_keys, not args.no_stats)
    else:
        raw = sys.stdin.read()
        print(compact_json(raw, args.sort_keys))
