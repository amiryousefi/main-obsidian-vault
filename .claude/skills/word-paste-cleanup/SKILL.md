---
name: word-paste-cleanup
description: Clean Word/Google-Docs paste artifacts out of a Markdown note without changing a single word - trailing whitespace, stray blank lines inside lists, document-wide ** wrappers, "1. # Heading" numbered headings, broken Arabic/Persian presentation-form characters, invisible bidi junk. Use whenever the user says they pasted or copied something from Word/Docs/PDF and wants it cleaned up or formatted, or when a note visibly has these artifacts.
---

# Word paste cleanup

Formatting-only cleanup of notes pasted from Word, Google Docs, or a PDF.

**The hard rule: never change a word.** No rewording, no translating, no
reordering, no "while I'm here" edits. Whitespace, markers, and character
encoding only. If something reads wrong, report it — do not fix it.

## Steps

1. **Find the file.** If the user says "this file" and it is not obvious,
   check for recently modified notes:
   `find . -name "*.md" -mmin -120 -not -path "./.obsidian/*" -exec ls -la {} \;`
   A fresh paste is usually the newest file. If two candidates are equally
   plausible, ask rather than guess.

2. **Look before you clean.** Confirm the artifacts are really there:

   ```bash
   f="path/to/note.md"
   for c in 00A0 200B 200C 200E 200F FEFF 0009 000D; do
     n=$(grep -oP "\x{$c}" "$f" | wc -l); [ "$n" -gt 0 ] && echo "U+$c: $n"
   done
   echo "presentation forms: $(grep -oP '[\x{FB50}-\x{FDFF}\x{FE70}-\x{FEFF}]' "$f" | wc -l)"
   echo "trailing-ws lines:  $(grep -cP ' +$' "$f")"
   ```

3. **Dry run**, then apply:

   ```bash
   python3 .claude/skills/word-paste-cleanup/scripts/clean_word_paste.py --check "$f"
   python3 .claude/skills/word-paste-cleanup/scripts/clean_word_paste.py "$f"
   ```

   The script edits in place and leaves **no `.bak` files** — the vault is a
   git repo, so `git diff` is the undo. Pass `--backup` only if you are working
   on a file outside version control. The script **aborts on its own** if the
   word stream would change. It is idempotent —
   re-running prints "already clean".

4. **Judgment pass.** The script deliberately does not touch heading *levels*,
   because that is a per-document call. Read the result and consider by hand:
   - a `# Title` followed by `### Section` with no `##` → promote the sections
     to `##` so the hierarchy is contiguous
   - tables Word flattened into lines, or footnote markers left inline
   Do these with an explicit `Edit`, not a broad regex.

5. **Report** what changed, what you deliberately left, and the word-count
   verification. Do not leave stray `.bak` files behind in the vault; if you
   used `--backup`, delete the copy once the result is verified.

## What the script does

| Artifact | Action |
|---|---|
| Arabic/Persian presentation forms (`ﻣﺘﻌﻬﺪ`) | NFKC on those ranges only → real letters |
| CR / BOM / zero-width / bidi controls | removed |
| Trailing spaces on a line | stripped (Word's accidental hard line breaks) |
| Blank line between every list item | removed → tight list |
| Runs of blank lines, leading/trailing blanks | collapsed |
| `**` wrapping the whole document | removed; bolded title promoted to `# ` |
| `1. # Heading` (Word numbered heading) | → `## 1. Heading` |

## What it leaves alone, on purpose

- **ZWNJ (U+200C)** — the Persian half-space in `می‌شود`. Real content, never strip it.
- **Non-breaking spaces** — often load-bearing. In contracts, runs of NBSP are
  the fill-in blanks for names, dates, and signatures; converting them to plain
  spaces makes the blanks vanish when rendered. Only pass `--nbsp` if you have
  checked that none of them are doing that job.
- Persian digits, `«»` guillemets, `……` placeholder dots — all intentional.

## Verifying

The script's built-in check normalizes both versions, drops markdown markers,
and compares the word streams; it refuses to write on any mismatch. Quote the
result in your report, e.g. "1500 words before, 1500 after, identical."
