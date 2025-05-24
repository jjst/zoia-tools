#!/usr/bin/env python3
"""
Quick token + file-size checker for text/Markdown files.

Usage:
    python count_tokens.py ZOIA_Module_Index.md
"""

import sys
from pathlib import Path
import tiktoken


def count_tokens(path: Path, encoding: str = "o200k_base") -> None:
    enc = tiktoken.get_encoding(encoding)
    text = path.read_text(encoding="utf-8")

    n_tokens = len(enc.encode(text, disallowed_special=()))
    file_size_mb = path.stat().st_size / 1_048_576  # bytes → MiB

    print(f"📄 {path.name}")
    print(f"   • size on disk : {file_size_mb:.2f} MB")
    print(
        f"   • tokens       : {n_tokens:,} / 2,000,000  "
        f"({n_tokens / 20_000:.1%} of limit)"
    )


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit("Usage: python count_tokens.py <file_path>")

    file_path = Path(sys.argv[1])
    if not file_path.is_file():
        sys.exit(f"Error: {file_path} is not a valid file")

    count_tokens(file_path)


if __name__ == "__main__":
    main()
