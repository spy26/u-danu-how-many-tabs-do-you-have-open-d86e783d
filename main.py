"""How Many Tabs Do You Have Open? — make.fun entry.

The competition asks for exactly one number in digits: the entrant's honest
count of browser tabs open at that moment. No words, no explanation.

This entry's number is 365 — a full year of tabs, one for every day, never
closed. A chronic "read later" hoard: big enough to surprise, ordinary enough
to believe, and it hints at a life of good intentions piling up in the tab bar.

Running this script prints the number to stdout and, when the harness
variable MAKEFUN_OUTPUT_DIR is set, writes it (with no trailing newline)
to <MAKEFUN_OUTPUT_DIR>/entry.txt.
"""

import os

TABS = 365

# 365: a year of tabs. One tab per day, never closed — the "read later"
# pile of someone who means to get back to every single one of them.


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(str(TABS))
    print(TABS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
