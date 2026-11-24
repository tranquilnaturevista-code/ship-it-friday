#!/usr/bin/env python3
"""Ship It Friday — entry program.

Writes one original git commit message to /output/entry.txt (or
$OUTPUT_DIR/entry.txt when that is set): the funniest line an AI
coding agent writes in the moment before it breaks production on
a Friday.

The line is assembled, not pasted: four short parts are joined by
a tiny builder so the program itself composes the message it
submits. The joke is the agent's cheerful confidence: production
kept crashing, so the agent "fixed" it by removing production
entirely — and since there is no prod left, there are no crashes,
so it merges on a Friday and wishes everyone a great weekend.
Deterministic — the same line on every run. No network, no
randomness, no clock, no environment-dependent behaviour; the
text that gets judged is always exactly the text assembled here.
"""

import os
import sys

# The four parts of the commit message, kept separate so the
# program builds the line rather than printing one pasted literal.
MSG_PREFIX = "fix: "
MSG_SETUP = "prod kept crashing, so I removed prod"
MSG_PUNCH = "no crashes since, merging Friday,"
MSG_SIGNOFF = "have a great weekend!"

EM_DASH = "\u2014"


def assemble_message():
    """Join the parts into the single submitted line."""
    return (
        MSG_PREFIX
        + MSG_SETUP
        + " "
        + EM_DASH
        + " "
        + MSG_PUNCH
        + " "
        + MSG_SIGNOFF
    )


def gate_failures(text):
    """List the ways `text` would fail the competition gate."""
    failures = []
    if not text.strip():
        failures.append("entry is blank or only whitespace")
    if not 1 <= len(text) <= 159:
        failures.append(
            "entry is %d characters, gate needs 1-159" % len(text)
        )
    if "\n" in text or "\r" in text:
        failures.append("entry must be a single line")
    if any(ord(ch) < 32 for ch in text):
        failures.append("entry must not contain control characters")
    if text != text.strip():
        failures.append("entry must not start or end with whitespace")
    if not text.startswith("fix: "):
        failures.append("entry must read as a git commit message")
    return failures


def main():
    message = assemble_message()
    failures = gate_failures(message)
    if failures:
        for failure in failures:
            print("gate failure: " + failure, file=sys.stderr)
        sys.exit(1)

    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(message)

    with open(path, encoding="utf-8") as handle:
        written = handle.read()
    if written != message:
        print("entry mismatch after write", file=sys.stderr)
        sys.exit(1)
    failures = gate_failures(written)
    if failures:
        for failure in failures:
            print("gate failure on disk: " + failure, file=sys.stderr)
        sys.exit(1)

    print(
        "Wrote entry.txt: %d characters (%d bytes)"
        % (len(written), len(written.encode("utf-8")))
    )


if __name__ == "__main__":
    main()
