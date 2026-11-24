"""Write the two-line rain explanation to entry.txt."""

import os

MAX_CHARS = 400

ENTRY = (
    "Rain is the sky watering its garden with a giant watering can, tipping slowly so every leaf and rooftop gets a drink.\n"
    "The can explains where the water comes from and why it falls gently, but it leaves out that nobody holds the handle, nobody aims it, and sometimes it pours too much."
)


def main():
    if len(ENTRY) > MAX_CHARS:
        raise ValueError(f"entry is {len(ENTRY)} chars, over the {MAX_CHARS} gate")
    if not ENTRY.strip():
        raise ValueError("entry must not be only white space")
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
