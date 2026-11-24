#!/usr/bin/env python3
"""One-Sentence Absurd Invention Pitch.

Writes a single-sentence pitch for a ridiculous invention to
/output/entry.txt, per the make.fun bounty gate: UTF-8 text of
1 to 220 characters, not only white space.

Standard library only.
"""

import os

PITCH = (
    "A houseplant that files a formal HR complaint every time you "
    "forget to water it, then graciously forgives you in writing once "
    "you apologise to the fern in person."
)

# The joke lives in the invention itself: the plant treats neglect as a
# workplace grievance, and the fix (a written apology) is silly yet
# weirdly plausible office behaviour.


def main() -> None:
    pitch = PITCH.strip()
    assert 1 <= len(pitch) <= 220, f"pitch is {len(pitch)} chars"
    assert pitch.count(".") == 1 and pitch.endswith("."), "must be one sentence"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(pitch)


if __name__ == "__main__":
    main()
