---
created: 2026-07-31
source: Amir2.0/next-steps.md
---

# Next steps — from built to live

Status (July 2026): the site is built and pushed. `final/` in the
new-amiryousefi.com repo is the deploy target — tagline "I turn complexity
into direction", 3 pages, priced offers ($950 / from $8,500 / $7,500 mo),
case studies, remote-worldwide positioning. Nothing below is a design task.
The redesign chapter is closed.

## 1. Fill the four launch blockers (~1 hour, only Amir can do these)

- [ ] Create the `hello@amiryousefi.com` mailbox (or replace it in `final/src/data/site.ts`)
- [ ] Create a Cal.com/Calendly "Fit call — 30 min" event; paste URL into `site.ts` → `bookingUrl`
- [ ] Confirm TodaysCrypto, Sayman, OxinGame can be named publicly (else anonymize)
- [ ] Verify the "20k+ daily visitors" and "3 CTO roles" figures — correct or delete

## 2. Deploy (~30 min)

- [ ] Import new-amiryousefi.com repo into Vercel, **Root Directory = `final`**
- [ ] Point amiryousefi.com at Vercel; retire the 2019 GitHub Pages site
- [ ] Add a favicon + OG image and basic analytics (Vercel Analytics is one click)

## 3. Align the profiles (~1 hour)

- [ ] LinkedIn: headline → tagline + advisor positioning; location current;
      link to the new site
- [ ] GitHub profile README + Medium bio: same line, same link

## 4. Start the only motion that makes money (week 1, ongoing)

- [ ] Send 10 warm messages to former colleagues/founders — offer the free
      fit call, not the website
- [ ] KPI #1: **warm conversations per week** (target 4). Follower counts
      are not a KPI.

## 5. First content (week 2)

- [ ] Publish the five field principles as a LinkedIn post + on the site
      (they're already written — `operating-system/src/data/principles.ts`)
- [ ] Monthly public progress note thereafter (per goals-and-kpis.md)

## Rules carried over

- No new themes, no new plans, no new repos until #1–#4 are done.
- A claim ships only if it survives a "prove it on a call" test.
- Revenue comes from conversations, not redesigns (see gulftech/reality-check.md).
