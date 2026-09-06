---
created: 2026-09-05
status: draft
type: blog post — case study deep dive
pillar: 1 — Strategic Architecture & Product Leadership
target: Medium / personal blog
---

# From WordPress to Laravel — what a live migration actually costs

Blog draft built from [[Sayman — Website Case Study]]. Pillar 1 per
[[Content Strategy]]. ~1,660 words.

---

## Headline options

1. **From WordPress to Laravel: What a Live Migration Actually Costs**
   *(recommended — "live" is the differentiator, and cost framing speaks to founders)*
2. **We Rebuilt an E-Commerce Platform Serving 20,000 Visitors a Day. The Code Was the Easy Part.**
3. **Your Legacy System Is Not the Code. It's Everything Nobody Wrote Down.**

---

## Post

Every founder running on a legacy platform eventually gets the same advice:
rebuild it properly. It is good advice. It is also incomplete, because it
describes the work as an engineering project when the expensive part is not
engineering at all.

In 2019 I led a team of five through a migration of an e-commerce business off
WordPress and onto a purpose-built Laravel platform. Five thousand products.
Twenty thousand visitors a day. Real orders, real customers, real history.

The technical rebuild went roughly as planned. Almost everything that made the
project hard sat somewhere else.

### The constraint that changes every decision

A store that is trading cannot go dark.

That sounds obvious written down, and it is routinely ignored in practice. It
is the constraint that separates a migration from a rewrite, and it invalidates
the most natural plan — build the new thing, test it, switch over one weekend.
That plan is fine when you can afford to be wrong for a few hours. When
customers are checking out during the switch, "we'll fix it Monday" is not an
available option.

So the first real decision was not about frameworks. It was accepting that the
migration had to be sequenced as a business event, with the store trading
throughout. We moved products, users, and full order history with almost no
downtime. Every architectural choice that followed was downstream of that one
requirement.

If you are evaluating a rebuild proposal and it does not open with how the
business keeps operating during the transition, you are reading a rewrite plan
wearing a migration costume.

### First, check whether you actually need this

Not every struggling platform needs replacing, and a migration is one of the
most expensive ways to find out you were wrong.

The honest test is whether the constraint is structural or cosmetic. Slow pages,
an ugly admin, a checkout you dislike — these are usually fixable in place, and
a rebuild is a very costly way to buy a redesign. The signals that genuinely
justify a migration look different: every new operational requirement means
another plugin or another workaround; nobody on the team can predict what a
change will break; the data model actively fights the way the business now
works; and the cost of each new feature is rising while its size stays the same.

That last one is the clearest tell. When identical-sized changes take
progressively longer, you are paying interest on a structural problem, and no
amount of tuning changes the trajectory.

In the case I am describing, the business had passed that line. WordPress plus
a layer of custom plugins had carried it a long way — and I want to be precise
here, because the "legacy" label is often used to mean "chosen by someone
else." That stack was the right decision when it was made. It got the company
to five thousand products and twenty thousand daily visitors. It had simply run
out of room, and every further step was being taken by adding another plugin to
a system that already had too many.

Knowing the difference between a platform that is unfashionable and one that is
structurally finished is most of the judgement in this decision.

### Read the old system before you replace any of it

The instinct on inheriting a legacy platform is to look at what it does badly
and start there. That instinct is the single most common cause of failed
migrations.

Before writing meaningful code, we documented the existing system in four
directions. The **custom plugins** — years of accumulated WordPress extensions,
each encoding some decision nobody could still explain. The **data structures**,
including the ones that had drifted from what the schema claimed. The
**operational procedures** — how customer service actually handled a return, how
inventory actually moved, how content actually got published. And the **workflow
seams**, where one team's output silently became another's input.

That last category is where migrations die. A legacy system that has been in
production for years is not a codebase. It is an accumulated record of every
operational decision the business has ever made, most of them undocumented,
many of them load-bearing.

You find these the same way every time. Someone in customer service says "oh,
we always adjust that field before it ships, otherwise the warehouse rejects
it." That sentence is a business rule. It is not in any specification. It is not
in the ticket backlog. It exists in one person's habit, and if you rebuild
without capturing it, you will ship a technically superior platform that breaks
the warehouse on day one.

The rebuild is a solvable engineering problem. The archaeology is the
consulting work, and it is what actually determines whether the new system
survives contact with the business.

### Break the monolith so five people can move at once

An e-commerce platform looks like one thing from outside and is not one thing
inside. We split it into separable sub-systems: catalogue, orders, invoicing,
discounts, notifications, permissions, and the public API.

The reason was organisational before it was architectural. Five engineers
working inside one undifferentiated codebase spend a meaningful fraction of
their week colliding with each other — merge conflicts, blocked branches,
coordination overhead that grows faster than the team does. Clear seams meant
parallel work.

This is the part founders consistently underestimate when they hire. Team
velocity is not the sum of individual velocity. It is that sum minus the cost
of coordination, and architecture is the main lever on that cost. A structure
that lets five people work without waiting on each other is worth more than any
individual engineer's speed.

### The software has more users than you think

We built for three groups who never appear in a typical requirements document:
customer service, shipping and packaging, and supply.

Each had procedures encoded in the old system. Each would have to live inside
the new one every working day. None of them were in the room when the project
was scoped — which is normal, and which is why so many internal tools are
quietly hated by the people required to use them.

Treating them as first-class users changed the requirements. Not
cosmetically — structurally. The bulk price updating tool, the invoicing
design, the discount rules scoped by user, product, and product variation, the
notification system spanning email, SMS, web, and app push: all of that came
from watching how the business actually ran, not from a feature list.

There is a hard commercial argument here, not just an empathetic one. When
internal software fits the operation, staff stop maintaining private
workarounds — the spreadsheet on the side, the shared inbox, the WhatsApp
group where the real coordination happens. Those workarounds are pure
operational cost, and they are invisible on every dashboard you own.

### Automate the processes that have no API

Two of the most valuable pieces we built were not part of the platform at all.

The business needed to register imported goods in government panels for tax
and customs, and to cross-check customer identities with banks to avoid
payment fraud. Both were manual, repetitive, and error-prone. Neither system
offered an API.

So we automated the interface instead of the integration — Python with
Selenium driving the panels the way an operator would, a Flask service exposing
the results, and an admin view so staff could see job status without asking an
engineer. We used the same approach for competitive pricing: a Django service
crawling competitor sites and surfacing every relevant price change, rather
than a person checking manually and missing most of them.

This is unglamorous work and it is often the highest-return work available. The
question is never "does this system expose an API." It is "how much operational
time is this consuming, and what would it take to get most of it back."

### Write the practices down, or rebuild again in three years

We introduced a developer handbook, coding standards, and documentation
*during* the project, not after it.

Doing this mid-delivery feels like a tax. It is the opposite. A team absorbing
new members mid-project either has written standards or has an onboarding
process that consists of interrupting whoever is least busy. The handbook was
what let the team grow without losing pace.

It is also the answer to the question any serious buyer of technical leadership
should ask: what happens after you leave?

Here is the outcome I care most about from that engagement. **The team and the
software kept performing for years after I left.** No emergency rewrite, no
rescue project, no gradual decay into the same state as the platform we
replaced.

That is the real test. Delivery capability that collapses when one person walks
out was never capability — it was dependency. And dependency is easy to
mistake for competence right up until the moment it fails.

### What I would tell a founder facing this

Three things.

**Budget for the archaeology.** The rebuild estimate you have been given is
probably reasonable for the code and probably ignores the discovery work. That
discovery is not overhead; it is the part that determines whether the new
system fits the business.

**Interview the operators.** Customer service, warehouse, and supply know
business rules that exist nowhere else. An afternoon each is cheap. Finding out
after launch is not.

**Judge the plan by what survives your departure.** Written standards, real
documentation, and a team that can absorb new people — these are what
distinguish a platform you own from a platform you rent from whoever built it.

The migration is the easy half. The hard half is capturing what the old system
knew and nobody wrote down.

---

*I work with founders and leadership teams on exactly these decisions —
architecture, migration risk, and building engineering teams that outlast the
project. If you are facing a legacy platform that is holding the business back,
[book a strategy call](#).*

---

## Draft notes

### Voice applied

"Battle-tested builder, professional-humanized" per [[Strategy Q&A Log]] —
operator-led, first-person, no corporate brochure voice. Every claim traces to
[[Sayman — Website Case Study]] and the CV; no invented metrics. Follows the
"prove it on a call" rule from [[Next Steps]].

### SEO

- **Primary keyword:** *WordPress to Laravel migration* — in headline, first
  section, and one subheading.
- **Secondary:** legacy system migration, e-commerce replatforming, zero
  downtime migration, technical debt.
- **Meta description (152 chars):** "A team of five migrated a 20,000-visitor
  e-commerce store off WordPress with almost no downtime. The code was the easy
  part. Here's what actually cost."
- **Internal links:** the Sayman case study page; the services page at the CTA.
- **External links:** Laravel docs for credibility; one reputable
  replatforming-cost source in the archaeology section.
- **Image alt text:** an architecture before/after diagram would earn its place
  — alt "WordPress monolith versus Laravel sub-system architecture for an
  e-commerce platform."

### Next steps

- Replace the `#` in the CTA with the real booking URL — still a launch blocker
  in [[Next Steps]].
- Confirm SaymanDigital can be named publicly, or anonymise to "a digital-goods
  retailer" throughout.
- Repurpose: the archaeology section and the "software has more users than you
  think" section are each a standalone LinkedIn post, per the 2–3 posts/week
  cadence.
