"""Loading Screen Gold — entry for make.fun.

Writes one line to /output/entry.txt.
The line is a loading-screen tip of at most 200 characters for stressed developers and AI coding agents.
"""
import os

LINE = "Tip: if your code compiles on the first try, check that you actually changed anything."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
