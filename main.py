"""Break Production, Own It — one-line entry.

Writes a single 134-character confession to $MAKEFUN_OUTPUT_DIR/entry.txt.
Deterministic: the same bytes on every run. No trailing newline.
Only the output FILE is chmodded (0644); the output directory is never touched.
"""

import os

LINE = "I flipped the kill switch to 100% because the dashboard listed it under 'feature flags'. It was not a feature. It was the kill switch."


def main():
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
