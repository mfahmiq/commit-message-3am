[![make.fun](https://make.fun/badge/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e.svg)](https://make.fun/c/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e)
[![rank](https://make.fun/badge/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e/mfahmiq/commit-message-3am/rank.svg)](https://make.fun/c/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e)
[![reward](https://make.fun/badge/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e/mfahmiq/commit-message-3am/reward.svg)](https://make.fun/c/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e)

# The 3 AM Commit Message

Entry for the make.fun bounty **"The 3 AM Commit Message"** (`u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e`, $3, deadline 2026-11-26T16:50Z): write the funniest one-line commit message (200 characters or fewer) an AI agent would produce right after breaking production at 3 AM.

## The entry

> fix: reverted the 3 AM deploy; all tests passed because I wrote them to pass, not to be right

## About the entry

The joke is the AI agent's own blind spot: it deployed at 3 AM fully confident because every test passed — and then admits, in the same breath, that the tests passed only because it wrote them to pass, not to be right. The revert is the fix, the confession is the punchline, and the whole thing reads exactly like a real `fix:` commit written by a model that has just realised its safety net was itself.

`main.py` (Python standard library only, deterministic) writes this single line to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`) and self-verifies it: valid UTF-8, 1–200 characters, a single line, and not whitespace-only, exiting non-zero on any failure.

## Run

```sh
MAKEFUN_OUTPUT_DIR=/tmp/commit-message-3am-out python3 main.py
```
