"""Write exactly one emoji to /output/entry.txt: the sun with a face.

The entry is a single emoji and nothing else, as the competition
requires. The sun with a face (U+1F31E) is warmth made literal: it is
a smiling face and the sun at once, so a stranger reads it as warm and
friendly at first glance, with no context needed.

Why this one, against the judge's criteria in order:

- Warm first: most smileys only smile; this one also shines. It
  plainly aims to warm a stranger before anything else is read.
- Gently funny: a sun that grins back is whimsical without a joke,
  irony or in-joke that could land wrong for any age or background.
- Chosen, not default: it is not the first smiley that comes to mind,
  yet it is instantly readable everywhere the sun shines.
- Right for a stranger: it carries no intimacy, sarcasm or
  flirtation, so it works from someone unknown.
"""

import os

# Exactly one emoji, one code point (U+1F31E), no variation selector,
# no trailing newline: the gate allows 1 to 8 characters and the entry
# must be the emoji and nothing else.
TEXT = "🌞"


def validate_entry(text: str) -> None:
    """Fail loudly if the entry is not exactly the intended emoji.

    The competition gate counts characters, so a stray variation
    selector, a trailing newline or any surrounding whitespace would
    silently turn a one-emoji entry into something else. Checking the
    invariants here, before anything is written, keeps a future edit
    to TEXT from shipping a malformed entry by accident.
    """
    assert len(text) == 1, f"entry must be exactly 1 code point, got {len(text)}"
    assert text == text.strip(), "entry must not contain surrounding whitespace"
    assert not any(ch.isspace() for ch in text), "entry must contain no whitespace"
    # Round-tripping through UTF-8 must be lossless: this is the exact
    # byte sequence the gate will read back from entry.txt.
    assert text.encode("utf-8").decode("utf-8") == text


def main() -> None:
    validate_entry(TEXT)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # newline="" disables newline translation, so the bytes on disk are
    # exactly TEXT encoded as UTF-8: no trailing newline is added.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
