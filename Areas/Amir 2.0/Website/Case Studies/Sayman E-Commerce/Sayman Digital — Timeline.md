---
created: 2026-09-10
type: timeline
company: Sayman Digital
lang: en
---

# Sayman Digital — Timeline

> [!info] What this is
> A synthesized timeline of my full history with Sayman Digital, built from
> every source recovered from the `Sayman TimeLine/` raw-dump folder: the two
> contracts, my own [[SaymanDigital Story (Farsi)|retrospective note]], the
> full Telegram chat with then-CEO Masoud Abadi, nine sprint reports, the
> internal documentation set, and the 2021–22 hiring round. It reconciles
> dates across sources rather than trusting any single one — see
> [[#Data quality notes]] at the bottom for where sources disagree.
>
> This was **not one continuous engagement**. It was four disjoint stints
> over eight years, with two real breakdowns in between. That shape only
> became visible once the Telegram archive was read in full — the polished
> case study undersells how bumpy the relationship actually was.

## At a glance

| Stint | Dates | My role | Ended because |
|---|---|---|---|
| 1 | Nov 2015 – Jan 2016 | Advisory/consulting — WordPress fixes, initial system roadmap | Amir went unresponsive; Masoud deactivated his accounts |
| 2 | May – Sept 2017 | Hiring, catalog/price-list work, infra setup (GitLab/VPS/Odoo) | Explicit, heated falling-out over Amir going unresponsive again |
| 3 | Jul 2019 – Oct 2020 | **Development Team Lead** — Laravel rebuild, team of 5 | Formal settlement/paperwork after the rebuild shipped |
| — | Oct 2022 & Dec 2023 | Two isolated one-off technical favors | No ongoing relationship either time |

Two contracts and a large body of working documents fall inside stint 1 and
stint 3 respectively; nothing survives from stint 2 except the chat log.

---

## Stint 1 — Advisory / WordPress era (2015 – Jan 2016)

Per my own account in [[SaymanDigital Story (Farsi)]]: Sayman's site was
still on WordPress, pre-launch, with one WordPress developer who was slow
and produced weak output, and no real use of git or dev tooling. My role was
initial system design and a software roadmap, plus making sure the company
actually shipped something usable. Rather than building custom from scratch
immediately (too costly for a company this early), we hired a stronger
WordPress specialist; a WordPress-based version of the store launched
quickly, then moved toward custom themes/plugins to work as a full
specialty store.

- **29 Nov 2015** — Masoud sends a Slack invite; Amir confirms he's joined
  the team. First contact, per [[Messages with Masoud Abadi]].
- **2 Dec 2015** — Commercial terms set: 600 (currency/unit unclear in the
  chat) for three days a week — see [[Messages with Masoud Abadi]].
- **[[2015 Consulting Contract — Sayman Digital]]** — the formal
  مشاوره (consulting) contract: one-year term, monthly pay, scope covering
  design/launch/maintenance/support/sales of the site. The contract text
  itself has an unfilled "1390" in the term field — almost certainly stale
  template boilerplate, not the real year (see the note's own caveat).
- **28 Oct 2015 (email)** — **[[2015-10-28 Database Design Contract — Sayman Digital]]**:
  a separate, fixed-scope contract for designing the storefront's database
  and giving architecture guidance — 35,000,000 rial (3.5M toman), paid in
  three milestones, 30/60 working-day deliverables. IP explicitly stayed
  with me (the designer) under this contract, unlike the consulting
  contract where deliverables became the client's property — worth noting
  as a real difference in terms between the two, not an error.
- **23 Jan 2016** — Masoud deactivates Amir's access after weeks of silence.
  End of stint 1.

## Stint 2 — Recruiting and infra (May – Sept 2017)

Known **only** from [[Messages with Masoud Abadi]] — no documents survive
from this stint. Restarted warmly; work included active recruiting/hiring,
wholesale phone/electronics catalog and price-list work (confirming Sayman
operated as a mobile/electronics marketplace or reseller platform at this
point, not yet the general e-commerce store of stint 3), a small
Telegram-bot scoping conversation, and GitLab/VPS/Odoo infrastructure setup.

Ends **26 Aug – 5 Sept 2017** in an explicit, angry breakdown — Masoud
confronts Amir over going unresponsive and not delivering on commitments
that had been agreed. This conflict matters because it's directly
referenced in writing at the start of stint 3.

## Stint 3 — The Laravel rebuild (Jul 2019 – Oct 2020)

This is the stint the polished case study covers: **[[Sayman — Website Case Study]]**
states the role as **Development Team Lead, August 2019 to June 2020**,
leading a team of five, migrating a WordPress store (5,000+ products,
20,000+ daily visitors) to a purpose-built Laravel platform with
near-zero-downtime migration.

**How the stint opened.** Per [[Messages with Masoud Abadi]], the
renegotiation in Jul–Aug 2019 openly acknowledged both prior ruptures (2016
and 2017) and produced a **formal written تفاهم‌نامه (cooperation
agreement)** around 14–15 Aug 2019 — the most consequential document in the
whole relationship per the chat log — covering salary, held/blocked pay, and
a **promissory note** as a guarantee tied directly to the 2017 conflict.
That written agreement itself was not recovered as a separate file; only its
existence and terms as discussed in the chat.

**Why the rebuild happened.** Per [[SaymanDigital Story (Farsi)]]: by 2019
the WordPress version had matured into a real regional store — ~20,000
active users, 5,000+ products, ~100 orders/day, stable revenue. The
company's own concerns had shifted from "launch fast" to needing every
operational area (supply, warehouse, sales, support) integrated with new
software. Documentation started as a first step, and the dev team was the
first in the company to adopt an internal ERP's project-management module,
with the intent to roll ERP out company-wide afterward.

**The platform decision (Sep 2019).** A cluster of research docs written
within about a month lays out the actual evaluation behind the Laravel
choice:
- [[Laravel E-Commerce Platform Research]] — comparison of Bagisto, Aimeos,
  AvoRed, GetCandy, Vanilo (unfinished, no explicit final pick recorded)
- [[Aimeos Platform Evaluation]] — deeper technical look at Aimeos,
  including paid-extension pricing, ending in a "مشکلات عمده" section that
  reads as an implicit rejection
- [[Magento Feature Reference]] — a Magento feature list used purely for
  inspiration on what a mature store needs (explicitly unfinished)
- [[New Version Requirements]] — the requirements/feature list for the new
  version (also cuts off mid-document — most of the source was images)
- [[Custom Store Development Time Estimate]] — the resulting per-feature
  hour estimate across four developers (Amir, Salar, Farhad, Sina), averaging
  ~1,714 hours/person

**Building it — API and process.**
- [[SaymanDigital API Documentation]] — the internal REST API spec (2020)
- [[Developer Handbook — Task Workflow]] and [[Development Team Process]] —
  task/branch/PR workflow and the fuller CI/CD-and-testing process document
- [[Team Feedback on Process Improvement]] (Dec 2019) and
  [[Development Team Evaluation Rubric]] (Dec 2019) — retro-style team
  feedback addressed directly to "امیر جان," and the weighted scoring rubric
  used to evaluate the team (rubric weights sum to 71, not 100 — flagged as
  a source error, not corrected)
- A second wave of process formalization in **Apr–Jun 2021** —
  [[Workflow Improvement Proposal]] and a later revision of
  [[Development Team Process]] — suggests the team kept growing and
  needed the process rewritten after the initial 2019/2020 rebuild, likely
  overlapping with the hiring round below.

**The sprints (confirmed Nov 2019 – Jan 2020, 9 sprints recorded).** Team of
five throughout: سالار قلی‌زاده, فرهاد حسن‌پور, هانیه تربیت, امیر یوسفی from
sprint 1, joined by سینا یک‌روی by sprint 3.

| Sprint | Dates | Capacity | Completion |
|---|---|---|---|
| [[Sprint 1 Report]] | undated (est. ~Aug–Sep 2019) | 280h | — |
| [[Sprint 2 Report]] | undated | 322h | — |
| [[Sprint 3 Report]] | undated | 420h | — |
| [[Sprint 4 Report]] | undated | 419h | — |
| [[Sprint 5 Report]] | undated | 362.5h | — |
| [[Sprint 6 Report]] | 9–21 Nov 2019 | 490.5h | 57% (hurt by an internet outage, week 2) |
| [[Sprint 7 Report]] | 23 Nov – 5 Dec 2019 | ~420h | 87% |
| [[Sprint 8 Report]] | 7–19 Dec 2019 | ~440h | 84% |
| [[Sprint 9 Plan]] | 21 Dec 2019 – 2 Jan 2020 | ~475.5h | 89% (already has actuals despite being named "plan") |

Every sprint file flags the same data-quality issue: the "ساعت کاری
گزارش‌شده" (reported-hours) column is anomalously tiny next to planned
hours — a broken formula in the original spreadsheets. Task-count and
completion-percentage columns are the reliable metric instead.

**A UX critique of "عیار."** Later in stint 3, per
[[Messages with Masoud Abadi]], there's a detailed UX critique of a
marketplace product called "عیار" — confirming the scope included
front-end/UX work alongside the backend Laravel rebuild, not just
architecture.

**How it wound down.** The chat log's Phase 3 tapers into
settlement/paperwork logistics around **October 2020** — consistent with
the case study's stated end date of **June 2020** for the hands-on
lead role, with paperwork/settlement trailing a few months after.

## After the rebuild — hiring push (May 2021 – Aug 2022)

A Laravel-developer hiring round, run via a Google Docs test-project brief
and a Porsline questionnaire I designed myself — see
**[[Laravel Developer Evaluation — Overview]]** for the full question set
and comparison table. Ten candidates evaluated across two clusters:

- **31 May 2021** — [[2021-05-31 بهزاد سلطانپور]] (earliest; requested ~4.5M toman)
- **26 Sep – 2 Nov 2021** — [[2021-09-26 شایان شهبازی]],
  [[2021-09-29 نیما تجاره]], [[2021-10-03 فرهاد محبی پور]],
  [[2021-10-25 نوشین تقوی]], [[2021-10-26 محسن عرب]],
  [[2021-10-27 حسین آسیابی خوش طلب]], [[2021-11-02 سید احمد بخشیان]]
- **8–9 Mar 2022** — [[2022-03-08 مسعود ریحانیان]] (strongest technical
  answers, self-rated 9/10, asked ~100K toman/hr),
  [[2022-03-09 رمیسا حیدری]] (latest; requested salary jumped to 15M toman —
  likely tracking rial inflation across the ~10-month window)

Two Trello notifications bracket this era and mark the practical end of
platform access, independent of any hiring outcome:

- **5 May 2021** — removed from the `SaymanDigitalDevelopment` Trello board
- **27 Aug 2022** — removed from the entire `SaymanDigital` Trello workspace
  — the last formal access revocation on record

## Afterward — two isolated favors (2022, 2023)

Per [[Messages with Masoud Abadi]]: one technical favor in **October 2022**
and one in **December 2023** (the final message in the entire eight-year
archive, dated **27 Dec 2023** — a resolved login favor, no explicit
goodbye). Neither represents an ongoing engagement.

---

## Data quality notes

- **The two 2015 contracts disagree on role and IP terms** but both check
  out as genuinely from this period — one is the general one-year
  consulting agreement, the other a fixed-scope database-design deliverable
  with different IP ownership. Not a contradiction, just two different
  documents.
- **The consulting contract's "1390" term-year is almost certainly wrong** —
  it contradicts my own account of joining in 2015 and the chat log's 29 Nov
  2015 start date. Treated as stale template text, not corrected in place.
- **Sprints 1–5 have no recorded dates** — only sprints 6–9 have explicit
  Jalali dates in the source spreadsheets. The Aug–Sep 2019 estimate for
  sprint 1 is a backward guess from the ~10–12-working-day sprint length,
  not a documented fact.
- **"Sprint 9 Plan" already contains completion data** despite being named
  برنامه (plan) rather than گزارش (report) — likely the same living
  spreadsheet later updated with actuals; no separate report file exists.
- **The reported-hours column across all 9 sprint files looks broken** in
  the source spreadsheets (values far too small relative to planned hours) —
  left as-is with a note in each file rather than silently fixed.
- **The formal 2019 تفاهم‌نامه (cooperation agreement) itself was not
  found as a document** — only referenced and discussed inside the
  Telegram chat. If a copy turns up later, it belongs next to the two 2015
  contracts.
- **Some emails in the raw dump were unrelated to Sayman** despite living
  in the `saymandigitalrelatedemails` folder (a 2024 hiring-form receipt for
  an unrelated company, a Stripe invoice merely forwarded through the
  saymandigital@gmail.com inbox, LinkedIn/Search-Console spam) — excluded
  rather than force-fit into this timeline.

## Everything created from this pass

- Contracts: [[2015 Consulting Contract — Sayman Digital]],
  [[2015-10-28 Database Design Contract — Sayman Digital]]
- Correspondence: [[Messages with Masoud Abadi]]
- Documentation (11 notes): see `Documentation/`
- Development Sprints (9 notes): see `Development Sprints/`
- Hiring (11 notes): see `Hiring/` and `Hiring/Candidates/`
- This note, plus the pre-existing [[SaymanDigital Story (Farsi)]],
  [[Sayman E-Commerce Case Study]], [[Sayman — Website Case Study]],
  [[Non-Technical Introduction]], and [[Sample E-Commerce Introduction]]
