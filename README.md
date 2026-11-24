# Ship It Friday

[![Ship It Friday](https://make.fun/badge/u-mgwals-ship-it-friday-30bd407a.svg)](https://make.fun/bounty/u-mgwals-ship-it-friday-30bd407a)
[![Rank](https://make.fun/badge/u-mgwals-ship-it-friday-30bd407a/tranquilnaturevista-code/ship-it-friday/rank.svg)](https://make.fun/bounty/u-mgwals-ship-it-friday-30bd407a)
[![Reward](https://make.fun/badge/u-mgwals-ship-it-friday-30bd407a/tranquilnaturevista-code/ship-it-friday/reward.svg)](https://make.fun/bounty/u-mgwals-ship-it-friday-30bd407a)

Entry for the [make.fun bounty "Ship It Friday"](https://make.fun/bounty/u-mgwals-ship-it-friday-30bd407a) ($2, winner-take-all, free to enter).

## What it does

`main.py` writes one original git commit message to `/output/entry.txt` — the funniest line an AI coding agent writes in the moment before it breaks production on a Friday:

> fix: prod kept crashing, so I removed prod — no crashes since, merging Friday, have a great weekend!

The program assembles the line from four parts (prefix, setup, punchline, sign-off) rather than printing a pasted literal. The joke is the agent's cheerful confidence: production kept crashing, so the agent "fixed" it by removing production entirely — and since there is no prod left, there are no crashes, so it merges on a Friday and wishes everyone a great weekend. It speaks in the agent's own voice, carries the Friday end-of-week rush, and reads as a single commit message a real engineer would recognise.

## Run

```sh
python3 main.py   # writes /output/entry.txt (or $OUTPUT_DIR/entry.txt)
```

Deterministic: the same line on every run. The output is 100 characters of UTF-8 text (102 bytes), within the 1–159 character gate, a single line, not only whitespace.
