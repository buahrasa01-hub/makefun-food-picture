# food-picture-01 entry: a steaming bowl of ramen with tonkotsu broth, a soft
# egg, chashu pork, and chili oil swirls. The program copies entry-ramen.jpg
# to <MAKEFUN_OUTPUT_DIR>/entry.png byte for byte (JPEG bytes, .png name),
# because appetite first: the judge sees the food, not the code.
"""make.fun entry for competition food-picture-01 (standard library only)."""

import os

SOURCE = "entry-ramen.jpg"
OUTPUT_NAME = "entry.png"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)), SOURCE)
    with open(src, "rb") as f:
        data = f.read()
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, OUTPUT_NAME), "wb") as f:
        f.write(data)
    print("wrote", os.path.join(out_dir, OUTPUT_NAME), len(data), "bytes")


if __name__ == "__main__":
    main()
