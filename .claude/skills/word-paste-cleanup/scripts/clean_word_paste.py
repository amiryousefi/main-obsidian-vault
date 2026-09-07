#!/usr/bin/env python3
"""Clean Word/Google-Docs paste artifacts out of Markdown notes.

Formatting only: never adds, removes, or reorders words.
Run --check first to see what would change; run without it to apply.

Usage:
    clean_word_paste.py --check  FILE [FILE ...]
    clean_word_paste.py          FILE [FILE ...]
    clean_word_paste.py --nbsp   FILE          # also convert NBSP -> space
"""

import argparse
import difflib
import io
import os
import re
import sys
import unicodedata

NBSP = " "
ZWNJ = "‌"
# Invisible junk that carries no meaning in a Markdown note.
JUNK = ["﻿", "​", "‎", "‏", "‪", "‫", "‬",
        "‭", "‮", "⁦", "⁧", "⁨", "⁩"]


def defold_presentation_forms(text):
    """Arabic presentation forms (U+FB50-FDFF, U+FE70-FEFF) -> real letters.

    Word often pastes Persian/Arabic as isolated display glyphs. They look
    almost right but break search, copy and spellcheck. NFKC on just those
    ranges restores the standard letters without touching anything else.
    """
    out = []
    for ch in text:
        cp = ord(ch)
        if 0xFB50 <= cp <= 0xFDFF or 0xFE70 <= cp <= 0xFEFF:
            d = unicodedata.normalize("NFKC", ch)
            out.append(d if d.strip() else ch)
        else:
            out.append(ch)
    return "".join(out)


def clean(text, convert_nbsp=False):
    notes = []

    def note(n, msg):
        if n:
            notes.append(f"{msg}: {n}")

    # 1. Arabic presentation forms -> standard letters.
    n = sum(1 for c in text
            if 0xFB50 <= ord(c) <= 0xFDFF or 0xFE70 <= ord(c) <= 0xFEFF)
    text = defold_presentation_forms(text)
    note(n, "Arabic presentation forms normalized")

    # 2. Line endings and invisible junk (ZWNJ is preserved - it is a real
    #    Persian half-space).
    n = text.count("\r")
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    note(n, "CR line endings removed")
    n = sum(text.count(j) for j in JUNK)
    for j in JUNK:
        text = text.replace(j, "")
    note(n, "invisible/bidi control chars removed")

    # 3. NBSP: off by default. Runs of NBSP are usually load-bearing in
    #    contracts (fill-in blanks for names, dates, signatures).
    if convert_nbsp:
        n = text.count(NBSP)
        text = text.replace(NBSP, " ")
        note(n, "NBSP converted to space")

    lines = [l.rstrip(" \t") for l in text.split("\n")]
    n = sum(1 for a, b in zip(text.split("\n"), lines) if a != b)
    note(n, "trailing whitespace stripped")

    # 4. A stray ** wrapping the whole document (Word bolds the entire body).
    first = next((i for i, l in enumerate(lines) if l.strip()), None)
    last = next((i for i in range(len(lines) - 1, -1, -1) if lines[i].strip()), None)
    if first is not None and last is not None and first != last:
        head, tail = lines[first].lstrip(), lines[last].rstrip()
        if head.startswith("**") and not head.endswith("**") and tail.endswith("**"):
            lines[first] = head[2:].strip()
            lines[last] = tail[:-2].rstrip()
            notes.append("document-wide ** wrapper removed")
            # That bolded first line was the document title. If nothing else
            # in the file is an H1, promote it to one.
            t = lines[first]
            if (t and not t.startswith("#") and len(t) < 80
                    and not t.endswith(".")
                    and not any(l.startswith("# ") for l in lines)):
                lines[first] = "# " + t
                notes.append("title promoted to H1")

    # 5. Word numbered headings: "1. # Title" -> "## 1. Title".
    n = sum(1 for l in lines if re.match(r"^\s*\d+\.\s*#+\s*\S", l))
    lines = [re.sub(r"^\s*(\d+)\.\s*#{1,6}\s*(.+)$", r"## \1. \2", l) for l in lines]
    note(n, "Word numbered headings converted")

    # 6. Blank-line structure: drop blanks between list items, collapse runs,
    #    trim the top and bottom of the file.
    out, dropped = [], 0
    for i, l in enumerate(lines):
        if not l.strip():
            prev = next((x for x in reversed(out) if x.strip()), "")
            nxt = next((x for x in lines[i + 1:] if x.strip()), "")
            is_item = lambda s: bool(re.match(r"^\s*([-*+]|\d+\.)\s", s))
            if is_item(prev) and is_item(nxt):
                dropped += 1
                continue
            if not out or out[-1] == "":
                dropped += 1
                continue
            out.append("")
            continue
        out.append(l)
    while out and not out[-1].strip():
        out.pop()
    note(dropped, "stray blank lines removed")

    return "\n".join(out) + "\n", notes


def words(text):
    """Word stream used to prove the cleanup changed no wording."""
    t = unicodedata.normalize("NFKC", text)
    t = t.replace("**", "").replace(NBSP, " ")
    t = re.sub(r"^\s*(\d+)\.\s*#+\s*", r"\1. ", t, flags=re.M)
    t = re.sub(r"^\s*#+\s*", "", t, flags=re.M)
    return [w for w in t.split() if w]


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("files", nargs="+")
    ap.add_argument("--check", action="store_true",
                    help="report and diff without writing")
    ap.add_argument("--nbsp", action="store_true",
                    help="also convert non-breaking spaces to normal spaces")
    ap.add_argument("--backup", action="store_true",
                    help="write a .bak copy next to the file before editing "
                         "(off by default; the vault is in git)")
    args = ap.parse_args()

    failed = False
    for path in args.files:
        if not os.path.isfile(path):
            print(f"!! not a file: {path}", file=sys.stderr)
            failed = True
            continue

        src = io.open(path, encoding="utf-8").read()
        dst, notes = clean(src, convert_nbsp=args.nbsp)
        name = os.path.basename(path)

        if src == dst:
            print(f"== {name}: already clean")
            continue

        before, after = words(src), words(dst)
        if before != after:
            diff = next((p for p in zip(before, after) if p[0] != p[1]), None)
            print(f"!! {name}: ABORTED - wording would change "
                  f"({len(before)} -> {len(after)} words, first diff: {diff})",
                  file=sys.stderr)
            failed = True
            continue

        print(f"{'--' if args.check else '**'} {name}"
              f" ({len(src.splitlines())} -> {len(dst.splitlines())} lines,"
              f" {len(after)} words unchanged)")
        for n in notes:
            print(f"     - {n}")

        if args.check:
            d = list(difflib.unified_diff(src.splitlines(), dst.splitlines(),
                                          "before", "after", lineterm="", n=1))
            for line in d[:60]:
                print("     " + line)
            if len(d) > 60:
                print(f"     ... {len(d) - 60} more diff lines")
        else:
            if args.backup:
                io.open(path + ".bak", "w", encoding="utf-8").write(src)
            io.open(path, "w", encoding="utf-8").write(dst)

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
