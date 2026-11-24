"""The One-Line Cat Joke That Lands (make.fun).

Writes a single cat joke, one line under 200 characters, to
/output/entry.txt.

The joke: "I bought a scratching post to save the sofa. My cat
shredded the sofa to save the post."

Why this one, against the judge's brief:
- Setup and turn: sentence one is a sensible purchase; sentence two
  flips it, so the cat's logic defeats the owner's. The turn lands
  in the last three words.
- No tired pun: no "purr-fect", no "meow", no "cat-astrophe" --
  the judge's brief explicitly punishes puns heard many times before.
- Fresh angle: the cat is not destroying things at random; it is
  *protecting* the scratching post, by destroying the sofa. The
  parallel "to save the sofa" / "to save the post" is the engine.
- Short and retellable: 87 characters, two beats, nothing after
  the punchline to explain it.
"""

import os

JOKE = (
    "I bought a scratching post to save the sofa. "
    "My cat shredded the sofa to save the post."
)

OUTPUT_PATH = "/output/entry.txt"


def validate(text: str) -> str:
    """The gate: UTF-8 text, 1-200 chars, not only whitespace, one line."""
    text = text.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError(f"joke is {len(text)} chars, must be 1-200")
    if "\n" in text or "\r" in text:
        raise ValueError("joke must be a single line")
    text.encode("utf-8")
    return text


def write_entry(path: str = OUTPUT_PATH) -> str:
    text = validate(JOKE)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    # No trailing newline: the file is exactly the joke, nothing else.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    return text


if __name__ == "__main__":
    write_entry()
