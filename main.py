"""Two Robots in an Elevator.

Writes one line of awkward small talk to $MAKEFUN_OUTPUT_DIR/entry.txt:
what one robot says to another while they ride an elevator together.
Standard library only.
"""

import os
import sys

ELEVATOR_LINE = (
    "I calculated 4,096 conversation starters for this elevator "
    "ride. I have selected silence."
)


def elevator_line_gate(text):
    """Check the elevator line against the competition gate.

    The gate wants plain UTF-8 text of 1 to 200 characters, not
    only white space, on a single line: one line of awkward small
    talk that one robot says to another in an elevator. Returns
    the cleaned text or raises ValueError.
    """
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("elevator line must not be only whitespace")
    if len(cleaned) > 200:
        raise ValueError(
            "elevator line is %d characters, over the 200 limit"
            % len(cleaned)
        )
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("elevator line must be exactly one line")
    return cleaned


def elevator_line_measure(text):
    """Measure the elevator line for one last sanity pass.

    Returns a dict with the character count and the word count of
    the cleaned text. A line too short to carry a joke, or one
    padded out to fill the cap instead of landing the awkward
    pause, is caught here before anything is written.
    """
    words = text.split()
    return {"chars": len(text), "words": len(words)}


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    text = elevator_line_gate(ELEVATOR_LINE)
    shape = elevator_line_measure(text)
    if shape["words"] < 5:
        raise ValueError("elevator line is too short to carry a joke")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
