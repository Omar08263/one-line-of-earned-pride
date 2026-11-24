"""One Line of Earned Pride — entry program (program/v1, Python 3.13, stdlib only).

Writes one original line (a single sentence, 1-240 characters) to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set, for local runs):
a quiet, earned moment of pride — a woman climbs the three steps to her
front door without touching the rail after eleven months of physio.
Deterministic: the same bytes on every run; no network, no randomness,
no reads outside this file.

Design note (why this line): the judge weighs, in order, genuine earned
pride, a concrete scene, pride earned inside the line, landing in one read,
and freshness. Eleven months of physio is the long effort; three steps, a
front door and a rail are the scene seen happening; the pride arrives with
the last words ("without touching the rail") and is never asserted. The
runner-up line (a boy reading a page aloud after stuttering through every
lesson) was set aside: its scene is less visually specific and its pride
lands mid-line, with "without stopping once" as a trailing confirmation.

Verified 2026-11-24: two runs, byte-identical entry.txt (sha256
96515b80c8042af7e4154ac05dd1992ac21dba8a9edadf203f5d4cb51e0cbb5a),
103 characters / 103 bytes, mode 0644; independent pre-submit review
(APPROVE, no fixes) recorded as consultation #148.
"""

import os

LINE = "After eleven months of physio, she climbed the three steps to her front door without touching the rail."

# Gate the line itself: one sentence, 1-240 characters, not only whitespace.
assert 1 <= len(LINE) <= 240, f"line is {len(LINE)} chars, must be 1-240"
assert LINE.strip(), "line must not be only whitespace"
assert LINE.count(".") == 1 and LINE.endswith("."), "line must be a single sentence"


def main() -> None:
    # An empty MAKEFUN_OUTPUT_DIR (exported but blank) must not break the
    # run: fall back to the harness default /output, as the grader provides.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)
    # Deterministic permissions for the grader: the entry must be readable
    # (0644) no matter what umask the sandbox runs with.
    os.chmod(path, 0o644)
    # Read-back check: the file on disk must hold exactly the approved line,
    # byte for byte; otherwise fail loudly, never silently.
    with open(path, "r", encoding="utf-8", newline="\n") as f:
        written = f.read()
    if written != LINE:
        raise SystemExit("entry.txt does not match the approved line")


if __name__ == "__main__":
    main()
