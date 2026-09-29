#!/usr/bin/env python3
"""Check the copy-ready style paragraph's format and report its length."""
from __future__ import annotations

import argparse
import json
import sys
import unicodedata
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="UTF-8 file path, or - to read standard input")
    args = parser.parse_args()
    text = (sys.stdin.buffer.read().decode("utf-8-sig") if args.file == "-" else Path(args.file).read_text(encoding="utf-8-sig")).strip()
    han_count = sum(unicodedata.name(char, "").startswith(("CJK UNIFIED IDEOGRAPH", "CJK COMPATIBILITY IDEOGRAPH")) for char in text)
    character_count = sum(not char.isspace() for char in text)
    problems = []
    if "\n" in text or "\r" in text:
        problems.append("not_one_paragraph")
    if text.startswith(("#", "- ", "* ", "```", "正向提示词", "一键复制")):
        problems.append("has_wrapper")
    print(json.dumps({"hanzi_reference_count": han_count, "non_whitespace_characters": character_count, "ok": not problems, "problems": problems}, ensure_ascii=False))
    return 0 if not problems else 1


if __name__ == "__main__":
    sys.exit(main())
