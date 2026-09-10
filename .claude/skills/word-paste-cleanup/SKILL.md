---
name: word-paste-cleanup
description: Clean Word/Google-Docs paste artifacts out of a Markdown note without changing a single word - trailing whitespace, stray blank lines inside lists, document-wide ** wrappers, "1. # Heading" numbered headings, broken Arabic/Persian presentation-form characters, invisible bidi junk, and hard-wrapped paragraphs that should be one line each. Use whenever the user says they pasted or copied something from Word/Docs/PDF and wants it cleaned up or formatted, or when a note visibly has these artifacts.
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
   # Hard wrapping: many prose lines clustered just under a fixed width.
   awk 'length>0 && !/^[[:space:]]*[|#`]/ {print length}' "$f" \
     | sort -n | uniq -c | tail -5
   ```

   That last histogram is how you spot hard wrapping: a pile of lines at
   72-80 characters and almost none longer means a newline was inserted at
   every ~80 columns. One long line per paragraph means the note is fine.

3. **Dry run**, then apply:

   ```bash
   python3 .claude/skills/word-paste-cleanup/scripts/clean_word_paste.py --check "$f"
   python3 .claude/skills/word-paste-cleanup/scripts/clean_word_paste.py "$f"
   ```

   Add `--unwrap` to rejoin hard-wrapped lines (see below) — it composes with
   `--check`, so dry-run it the same way.

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
| Hard-wrapped paragraphs and list items | rejoined into one line each — **only with `--unwrap`** |

## Unwrapping hard-wrapped lines (`--unwrap`)

Word, PDF extraction, and fixed-width editors put a newline every ~80
columns. Markdown renders it as one paragraph regardless, so this is
invisible in preview — but it makes the source miserable to edit, and it is
especially bad for RTL text, where a mid-sentence break scrambles the visual
order of the line in the editor.

`--unwrap` joins each paragraph, list item, and blockquote body back into a
single line. It is pure whitespace: no word moves relative to another, and
the same word-stream check gates the write.

**It is opt-in, and should stay opt-in.** A deliberately hard-wrapped note is
a legitimate style — some people wrap at 80 so `git diff` stays line-level.
Never assume; if the wrapping might be intentional and the user has not
asked, show them the histogram and ask.

Left intact by `--unwrap`:

- YAML frontmatter, fenced code blocks (including their contents), tables,
  headings, thematic breaks, raw HTML lines
- the **title line of a callout** (`> [!info] ...`) — the body below it joins,
  the title keeps its own line
- indentation of nested list items — a sub-item folds into itself, not into
  its parent

One caveat: a Markdown hard break (two trailing spaces) does not survive,
because trailing whitespace is stripped in an earlier step regardless. If a
note depends on those, use `<br>` before cleaning.

## What it leaves alone, on purpose

- **ZWNJ (U+200C)** — the Persian half-space in `می‌شود`. Real content, never strip it.
- **Non-breaking spaces** — often load-bearing. In contracts, runs of NBSP are
  the fill-in blanks for names, dates, and signatures; converting them to plain
  spaces makes the blanks vanish when rendered. Only pass `--nbsp` if you have
  checked that none of them are doing that job.
- Persian digits, `«»` guillemets, `……` placeholder dots — all intentional.
  Note that Persian digits are *not* list markers either: `(ماده ۱۷) را` is
  prose, and `--unwrap` only treats ASCII `1.` / `1)` as an ordered item,
  matching what Markdown itself recognises.
- **Line wrapping**, unless you pass `--unwrap`.

## Verifying

The script's built-in check normalizes both versions, drops markdown markers,
and compares the word streams; it refuses to write on any mismatch. Quote the
result in your report, e.g. "1500 words before, 1500 after, identical."
