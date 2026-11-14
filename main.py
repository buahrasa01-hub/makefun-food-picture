# Entry image: steaming bowl of ramen — rich tonkotsu broth, soft golden egg
# yolk, slices of chashu pork, chili oil swirls, fresh scallions, rising steam.
import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry-ramen.jpg")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUT = os.path.join(OUT_DIR, "entry.png")


def main() -> None:
    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(SRC, OUT)


if __name__ == "__main__":
    main()
