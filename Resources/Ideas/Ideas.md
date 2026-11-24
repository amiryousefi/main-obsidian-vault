---
created: 2026-11-24
---

# Ideas

This folder holds one note per idea, each created from [[Idea]].

When an idea becomes real work, create a note in Projects/ from the [[Project]] template, set `status: promoted` and `project: [[...]]` on the idea, and add `From idea: [[...]]` on the project.

## Ideas

- 2026-11-24 · [[School Food Gut Check]]

```dataview
TABLE date AS Date, status AS Status, area AS Area, project AS Project
FROM "Resources/Ideas"
WHERE type = "idea"
SORT status ASC, date DESC
```
