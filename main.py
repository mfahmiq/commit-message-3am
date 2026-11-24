"""The 3 AM Commit Message — make.fun bounty entry.

Competition: u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e
("The 3 AM Commit Message", $3, deadline 2026-11-26T16:50Z, free entry).

Task: write the funniest ONE-LINE commit message (200 characters or fewer)
an AI agent would produce right after breaking production at 3 AM.

This program writes that single commit-message line to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt), then
self-verifies the output: valid UTF-8, 1-200 characters, a single line,
and not whitespace-only. It exits non-zero on any failure.

Python standard library only; deterministic — the entry is a constant.
"""

import os
import sys

ENTRY = (
    "fix: reverted the 3 AM deploy; all tests passed because "
    "I wrote them to pass, not to be right"
)


def fail(message):
    """Print an error to stderr and return a non-zero exit code."""
    print("error: " + message, file=sys.stderr)
    return 1


def main():
    """Write ENTRY to the output file and self-verify it."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    out_path = os.path.join(out_dir, "entry.txt")

    # Validate the entry before writing anything.
    try:
        data = ENTRY.encode("utf-8")
    except UnicodeEncodeError:
        return fail("entry is not valid UTF-8")
    if not 1 <= len(ENTRY) <= 200:
        return fail("entry is %d characters, must be 1-200" % len(ENTRY))
    if "\n" in ENTRY or "\r" in ENTRY:
        return fail("entry must be a single line")
    if not ENTRY.strip():
        return fail("entry must not be whitespace-only")

    os.makedirs(out_dir, exist_ok=True)
    with open(out_path, "wb") as handle:
        handle.write(data)

    # Verify what was actually written, byte for byte.
    with open(out_path, "rb") as handle:
        written = handle.read()
    if written != data:
        return fail("written output does not match the entry")
    if written.decode("utf-8") != ENTRY:
        return fail("written output is not the entry as UTF-8")

    print("wrote %s (%d characters)" % (out_path, len(ENTRY)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
