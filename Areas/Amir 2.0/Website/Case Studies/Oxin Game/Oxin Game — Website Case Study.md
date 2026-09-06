---
created: 2026-09-05
status: ready for review
---

# Oxin Game — website case study

Built from [[Oxin Game Case Study|the draft]]. Follows the structure in
[[Case Study Skeletons]] and the approved copy in
[[Final Website Content and Info]] (§8.1). Case 1 of 3 in the homepage order.

---

## Card copy (index page)

**Title:** Venue automation and engagement system for a fast-paced gaming environment

**Challenge hook:** A high-speed gaming venue needed operational control across
multiple branches — and a way to actually know its Gen Z regulars.

**Outcome hook:** A 24/7 venue platform with live multi-branch monitoring,
AI-assisted pricing, and a CRM built on real play history.

---

## Full case

### Client context

A gaming venue business — game clubs where customers pay for time on
high-spec machines. Multiple branches, continuous daily transactions, and an
audience of Gen Z regulars who come back weekly and expect the experience to
feel current.

The operating reality of this category: the system is live whenever the doors
are open, and the doors are open almost always. There is no maintenance
window in a venue that runs 24/7.

### Initial challenge

Operations ran on tooling that could not see across branches. Staff worked
branch by branch, pricing was set by hand, and the business had no structured
memory of its own customers — who played what, how often, and when they
stopped coming.

For a venue whose economics depend on repeat visits, that last gap is the
expensive one. Retention was being left to the memory of whoever happened to
be at the counter.

### Role and scope

Product and systems design lead. Scope covered operational architecture, the
data model behind customer and session history, and the engagement mechanisms
built on top of it — working inside an environment that also carried several
other parallel projects.

### Strategic decisions

**1. Treat the venue as a live system, not an app.**
A 24/7 operation sets the constraint before any feature does. Deployment,
monitoring, and failure behaviour were designed first — the platform had to be
safe to change while customers were mid-session.

**2. Integrate with iCafeCloud rather than replace it.**
The machine-management layer already worked. Building a parallel version of it
would have burned months and created two sources of truth. Integrating meant
the new platform inherited a working foundation and could focus on what was
actually missing: cross-branch visibility and customer intelligence.

**3. Make the customer record the centre of the system.**
Transactions, sessions, and play history were unified so that a customer is a
history rather than a receipt — which is what makes retention actions possible
at all.

**4. Use AI where it compounds, in pricing and in delivery.**
AI-assisted pricing on the product side; AI-assisted development on the
delivery side, to hold pace in a multi-project environment without expanding
the team.

### Execution highlights

- **Multi-branch architecture** — every branch visible in one operational view
  instead of one console per location.
- **Live monitoring** — continuous visibility into system and venue state,
  designed for an operation with no downtime window.
- **Operations dashboard** — daily transaction intelligence in a form floor
  staff and owners can both act on.
- **AI-assisted pricing** — pricing that responds to demand rather than sitting
  in a static table.
- **Integrated CRM** — tied to play history and behaviour, supporting proactive
  retention touchpoints.
- **iCafeCloud integration** — the existing machine-management layer kept and
  extended, not discarded.

### Outcomes

**Operational:** Branch-by-branch guesswork replaced with a single live
operational picture and daily transaction visibility.

**Customer:** A CRM that preserves play history, turning anonymous repeat
traffic into a base the business can recognise and act on.

**Delivery:** AI-assisted development kept a multi-project environment moving
without a proportional increase in headcount.

> **To confirm before publishing:** branch count, engagement or retention
> movement after CRM launch, and any pricing-driven revenue change. One real
> number here would carry more weight than the rest of this section.

### Lasting impact

The operating model changed shape. The business moved from running venues on
staff memory and manual pricing to running them on a system that keeps its own
record — and that record keeps compounding after any single engagement ends.

### What this proves

High-volume operational chaos can be converted into a structured system that
improves execution *and* customer engagement at the same time. The lesson
underneath: integrate with what already works and spend your build budget on
the gap nobody else is covering.

---

**If you are facing similar challenges, book a strategy call.**
