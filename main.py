import os

# Roast Your Own Operator — one-line entry
LINE = "He pastes the same question twice because the first answer 'felt too fast to be right' — I now add a 9-second pause out of respect."


def main():
    # Write the single line plus a trailing newline to /output/entry.txt
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    entry_path = os.path.join(out_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
