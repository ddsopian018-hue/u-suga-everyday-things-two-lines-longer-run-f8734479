"""Everyday Things, Two Lines, Longer Run — make.fun entry.

Writes one two-line explanation of rain to $MAKEFUN_OUTPUT_DIR/entry.txt.
Pure stdlib, deterministic, no network.
"""

import os

LINE_1 = (
    "Rain is the sky wringing out a giant grey sponge it soaked up from the sea, "
    "so the water it borrowed comes back down in drops you can catch on your tongue."
)

LINE_2 = (
    "The sponge fits because clouds really do collect water and let it fall "
    "when the drops get too heavy to float, but it leaves out that no sponge "
    "exists at all, since the vapour cools, gathers into tiny droplets, and "
    "falls on its own."
)


def main() -> None:
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    text = LINE_1 + "\n" + LINE_2 + "\n"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
