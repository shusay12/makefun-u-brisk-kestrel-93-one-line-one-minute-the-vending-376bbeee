#!/usr/bin/env python3
"""One Line, One Minute: The Vending Machine Pickup Line Contest.

Writes one pickup line, 200 characters at most, that a vending machine
would use on a passing human, to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR).

The line is a fixed, hand-written line spoken by the machine itself:
its coils, its snacks, its buttons and its light. No network, no
randomness, stdlib only, fully deterministic.
"""

import os
import sys

# The entry: one original pickup line, at most 200 characters.
ENTRY = (
    "Hey, you - my coils have been spinning for you all day, and "
    "unlike my snacks, I'm never out of stock on reasons to glow "
    "when you press my buttons."
)

MAX_CHARS = 200


def main() -> int:
    text = ENTRY.strip()
    if not text:
        print("entry is empty", file=sys.stderr)
        return 1
    if len(text) > MAX_CHARS:
        print(f"entry is {len(text)} chars, over the {MAX_CHARS} cap",
              file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1
    try:
        text.encode("utf-8")
    except UnicodeEncodeError as exc:
        print(f"entry is not valid UTF-8: {exc}", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
