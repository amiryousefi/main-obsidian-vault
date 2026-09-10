---
created: 2026-09-10
---
# My Story (English)

Part of [[Sayman E-Commerce Case Study]]. English version of [[SaymanDigital Story (Farsi)]].

> [!info] At a glance
> - **Client:** Sayman Digital — an e-commerce business, launched on WordPress and later rebuilt on Laravel
> - **Engagements:** three separate returns over several years — 2015, 2017, and 2019–2020
> - **Core role (2019–2020):** Development Team Lead, leading a five-person team through a full WordPress → Laravel migration
> - **Scope:** requirements, architecture, platform evaluation, hiring, developer process, and hands-on execution
> - **Scale at handover:** 5,000+ products, 20,000+ daily visitors, ~100 orders a day
> - **A year later:** 274,000 clicks and 7.38M impressions from Google Search in a single month
>
> For the short, site-ready version of the 2019–2020 rebuild, see [[Sayman — Website Case Study]].

---

## 2015 — First engagement: consulting on a stalled build

Sayman Digital brought me in as a consultant in 2015, while their store was still being built on WordPress and had not launched yet. Both the WordPress implementation itself and the way the team was developing it were causing problems.

### The diagnosis

The picture was clear once I got into it. The WordPress developer on the project was slow and was not producing the output the business needed, and the team was not using git or any real development tooling.

My assessment was that Sayman would eventually need a fully custom-built system. My role became laying out that system's initial architecture and a software roadmap toward it — while making sure whatever shipped in the meantime was actually solid.

### The recommendation

A full custom rebuild was not the right call yet. Sayman was an early-stage company, and that kind of build is expensive before the business can support it.

So the recommendation was a phased path: get a proper WordPress implementation shipped first, with the right person executing it, then grow into a custom platform once the business had earned that investment.

### The outcome

We brought in a more specialized WordPress developer to get execution to where it needed to be, and a working version of the store launched within a short time.

From there the team moved into a custom theme and custom plugins built specifically for Sayman Digital — turning a generic WordPress build into a proper specialty e-commerce platform, exactly as the roadmap called for.

---

## 2017 — Second engagement: infrastructure, hiring, and pricing

The second time I joined, development of the WordPress store was moving along on its own track and a strong development and content team had formed. Following the path set a couple of years earlier, the system had shifted from an off-the-shelf theme to a custom theme and plugins built specifically for the business.

This time my involvement went beyond a single product. I helped with recruiting, and I set up core infrastructure the team did not yet have: a self-hosted GitLab instance, the server it ran on, and an internal ERP deployment.

The specific project I led addressed one of the most important operations in any e-commerce business — pricing. We wanted enough flexibility to update prices quickly, and enough visibility into competitors' prices to stay sharp against the rest of the market. I built an initial version of that system.

My working relationship with Sayman wound down that year, and the idea never went past its first version. It came back later, and at much larger scale, in the rebuild.

---

## 2019–2020 — Third engagement: rebuilding the platform

### Where the company stood

By 2019 the WordPress version had matured into a substantial custom build. As a regional store it had around 20,000 active users and a catalogue of over 5,000 products, processing roughly a hundred orders a day.

This was the point where WordPress started showing its limits. The solution that had once been the best available option for this company — the one that had produced its best results — had become the thing holding it back.

Sayman Digital was now an established business with stable revenue. The first time I joined, the concern was getting started and launching quickly. Now the mindset had to change: every operation — supply, warehousing, sales, support — needed to be enabled by new software rather than worked around.

### Auditing a project already in flight

Before I rejoined, the company had started another project on its own: a companion to the store showing competitive prices across the market, with social features so users could discuss products and suppliers.

It was an appealing project and it had progressed some way. But after reviewing the code and the state of the work, my assessment was that a result was still a long way off.

This was probably the first moment management saw the gap between their vision for launching a product and what the team could actually execute against. The root cause was familiar: no real documentation of the project's current state or its roadmap. That had distorted the team's own estimates and left engineering and management without a shared idea of what was being built or what was deliverable.

We set the project aside so the full team's capacity could go to the main rebuild. The decision mattered more for what it established than for the project itself — from that point on, nothing proceeded without documentation and an agreed scope.

### How I ran the requirements phase

This is where most rebuilds quietly fail. The people who know what a system has to do are rarely the people who can describe it in technical language, so requirements end up written by engineers guessing at the business, and the gap only surfaces after the build.

So the requirements document opened by telling the business the opposite of what they expected: **no technical language was needed.** Instead, there were three ways to contribute.

| Contribution type | What it captured | Example |
|---|---|---|
| **Musts** | Non-negotiable qualities of the new version | "Must support 500 concurrent visitors"; "must be fast and flexible when updating prices" |
| **Ideas and wishes** | Deliberately unformed ambitions, understood to need refinement before becoming technical work | Anything that would make the system stronger |
| **New technical capabilities** | Concrete, specific asks with detail attached | Multi-vendor support |

Splitting it three ways gave people permission to contribute at the level they actually had knowledge at — without overreaching into design, and without staying silent because they could not write a spec.

What came back was the real business:

- Hundreds of near-identical customer comments every day, each answered by copying and pasting from a set of stock replies
- Pricing, described by the business itself as one of the company's biggest problems — the time it took, and the errors it produced
- Bundled products, which the existing system could not express
- Phone-system integration, so order follow-up could show why a customer had called and how far their case had progressed
- Identity tracking across a buyer's full journey, from first visit through review
- Measurability demanded not only of sales, discounts, content, supply and packaging — but of the development team too

Every automation we later built traces back to a line in that document. The work was not chosen because it was interesting to build. It was chosen because someone in the business had described the pain it removed.

### Build or buy: evaluating the alternatives

Before committing to a custom build, we ran a real evaluation, in September 2019.

We compared several open-source Laravel storefront platforms — **Bagisto, Aimeos, AvoRed, GetCandy, and Vanilo** — and mined Magento's much larger feature set for ideas about what a mature store needs.

Aimeos went furthest before we ruled it out, and the reasons were concrete rather than instinctive:

- The core features we needed sat behind paid extensions, and those extensions depended on Elasticsearch and Apache Solr — powerful, but a real infrastructure and knowledge cost on top of the licence
- Developer documentation was thin; in practice, understanding the system meant reading its source
- The paid extensions covered one year of updates, then required paying again
- Even after buying in, we would still need custom development to meet the requirements specific to our market — so "buy" did not remove the build, it added a subscription on top of it

### Estimating the work

We broke the system into roughly **25 subsystems** — products, content, users, notifications, comments and ratings, order processing, discounts, marketplace, accounting sync, API, app management, performance monitoring, cart, files, system event logging, and more.

Then every feature inside them was estimated independently by four developers, including me.

The sheet kept two totals: the maximum estimate across the team, and **the maximum excluding mine**. That second column was deliberate. I was the lead and the most experienced person in the room, which meant my numbers carried more weight than they deserved and would anchor everyone else's. Keeping a total that excluded me was a cheap way to check whether the plan still held without my influence. For the record, my estimates were usually the highest in the sheet.

Averaged out, the work came to roughly **1,700 hours per developer**. That exercise, not the platform comparison alone, is what turned "let's build our own" from a preference into a costed decision the business could actually approve.

### Building the team

We started with four people whose skill levels differed meaningfully, so both managing the work and dividing it by ability mattered from day one. We grew to five over the following sprints, across backend and frontend.

We were also deliberate about *when* to add people. Rather than hiring immediately, we waited a few weeks until the existing team had settled into the new development structure — so we were not fighting onboarding and process adoption on two fronts at once.

### What we built

The result was a Laravel and React platform with marketplace capability, migrated off WordPress with near-zero downtime. Products, users and full order history moved without the store going dark.

Beyond the storefront:

- **Operational tooling** — bulk price updates, advanced invoicing, and discount management scoped by user, product, and product variation
- **Omnichannel notifications** across email, SMS, web, and app push
- **Permissions and roles**, plus a documented RESTful API covering users, stores, products, pages, categories and site options
- **Accounting synchronisation** — orders posting automatically into the accounting system, with validation that blocked mismatched serial numbers at entry instead of surfacing them during reconciliation
- **KYC and fraud prevention** — scoring signals like account characteristics, prior order history, and payment-card verification. This module already existed in the old store, so rather than rewriting it we extracted its classes for reuse
- **A price-monitoring service** (Python, Django) that crawled competitor sites and surfaced relevant price changes automatically
- **Back-office automation** (Python, Flask, Selenium) for regulatory registration, external registry lookups, and bank identity verification — processes with no API of their own, automated by driving the web panels directly

That last point is worth pausing on. When the external systems a business depends on offer no integration path, the choice is to leave the work manual forever or to automate the interface that does exist. We scripted the browser.

### Going remote mid-project

We started in person, but COVID and the lockdowns arrived partway through.

Because the team already worked from written process and documentation inside the project-management system, we were ready for remote work when it came. The mechanics survived the transition intact. Communication was the harder part — keeping a team genuinely connected remotely was a cultural shift that touched everyone.

Meanwhile the old platform still had to run. Our team included the developers who had built it, and because we had documented it first, we already knew which parts to maintain and which improvements to let go. COVID drove more online shopping, which meant more load on exactly the system we were replacing. We kept it performing on user experience, speed and SEO, while directing as much capacity as possible toward the new build.

### Measuring delivery

Across four two-week sprints between November 2019 and January 2020, task completion moved **57% → 87% → 84% → 89%**.

The first number is as informative as the last. That sprint was disrupted by an infrastructure failure outside the team's control, and the retrospective named it plainly rather than absorbing it into a vague shortfall. Knowing precisely why a sprint missed is what makes the next one predictable.

By this point the team was also operating under a written scoring rubric covering timesheet discipline, peer sprint scores, task completion rate, and separate scores for the scrum master and for management — meaning that by the end of 2019 this was a team with formal Scrum roles holding itself to measurable standards.

### Closing the loop with the team

In December 2019 I ran a structured retrospective across the team, asking what single thing they would change, what they personally wanted to fix, how team management could improve, and what could be done about our processes.

The useful part was not the questions. It was sorting every answer by **who could actually act on it** — management, the individual, or the team — so nothing landed in the gap where everyone agrees a problem exists and no one owns it.

The team asked for time to mentor juniors, time to study and stay current, private per-sprint feedback, and more attention to testing and CI/CD.

When the development process was formally written up later, those items were its headline goals. The loop closed: they were asked, and what they asked for was built into how the team worked.

### Beyond engineering

By mid-2021 the brief had widened past the development team. I was asked to draft the company's working processes as it grew — salary structure and transparency, a continuous evaluation system, seniority and loyalty factors, defined career progression, quarterly team goals, and proper onboarding packages for new hires.

I will be straight about this one: that document was never finished. Its incentive and penalty sections are still empty headings. But being asked to write it at all says something about how far the role had travelled from "lead the developers."

### Hiring the next developer

After the rebuild shipped, I designed and ran a technical hiring round for a Laravel developer — a test-project brief plus a written assessment I built myself, covering three areas rather than one:

- **Framework depth** — middleware, validation, polymorphic relations, query scopes, queues, resource collections, and testing
- **Version control and collaboration** — commit hygiene, branching, and what to actually look for when reviewing someone else's pull request
- **Process fluency** — breaking a real feature into estimated units of work, and how they would participate in a daily standup

Candidates were assessed on all three. Writing correct PHP was table stakes; the questions were designed to reveal whether someone could work inside a team that had standards.

---

## The culture we built

### Shipping and delivering

As results became tangible, we increased how often we delivered. CI/CD had been in place from the start, but early on the team's output only reached management at the end of each sprint.

That became a clear, measurable weekly report, backed by a usable version of the system permanently available for testing on staging.

Building a large product for an established company means the biggest risk is not technical. Beyond the obvious stakeholders there were regular customers, support staff, warehouse operators and supply staff — and the real danger was everyone holding a different idea of what was being built.

Using agile principles, we worked to keep a shared understanding alive in every design decision, not just every sprint. That never meant accommodating every opinion. It meant being explicit about which decisions we were making, which we were deferring, and which we were sacrificing outright — and then following through on necessary refactors without flinching, provided a usable version always existed.

Delivery meetings grew more frequent, sometimes twice a week, and the audience widened past management to the support and warehouse teams, who by then were testing the system themselves.

That did double duty. It kept everyone aligned, and it built familiarity with the new system well ahead of the migration.

> One of the biggest risks in any migration is how comfortable an organisation's people feel about the change. Everyone always believes the old system was better. Starting familiarity early tells people their input is being weighed — and turns them into partners in the build rather than people the build happens to.

In effect the development team was building the product in front of the whole company. Delivery meetings raised the pressure at first, but the confidence that comes from consistently shipping and presenting meant more deliverables at every step. Features reached test servers fast enough that the feedback loop — bugs, requests, UX changes, notes for later — stayed short.

### Communication

Communication was one of the first things I found broken. The side project that had started without me had very little of it, which is also why its documentation was thin.

The old system's track record had earned real trust between management and the original developers — trust that anyone newly added sits outside of by default. That gap showed up as unclear, inefficient communication between the established developers, the newer ones, and management.

My own emphasis on documentation did not automatically fix it. If anything it sometimes crowded out the value of simply talking to each other. Documentation that nobody reads is not communication.

The fix was mundane and effective: more meetings, reading documents aloud together rather than assuming they had been read, and making sure everyone knew their feedback was heard and acted on.

We put deliberate weight on the phrase **shared understanding** — not unanimous agreement on every approach, but always being able to explain the direction and name the blockers, even when not everything could be solved. Sprint meetings, daily standups, and openly available reports built that over time, both day to day and at the level of the bigger picture.

### Ownership

Getting work from planned to delivered required a real culture of ownership. In a company this size, a planned task usually needs more detail before it is genuinely actionable, and the person doing the work has to chase that detail rather than wait for it.

We wrote this into the developer handbook as one governing line:

> **The owner of a task is the owner of that task's details.**

In practice:

- Every task lived on the board with a clear name, an owner, tags, a description, and any attached files or discussion — moving through **Todo → Doing → Today → Review → Done**
- **Today** held only tasks detailed enough to start immediately and small enough to finish by end of day. The test for whether something was broken down far enough was blunt: *can this be done in a block of one and a half to two hours?*
- Whoever took a task followed it from chasing the missing detail, through the code, to the merge — including talking to anyone the task depended on
- Every task got its own branch, named `[description]-TYPE#TASKID`, where `TYPE` was one of `feature`, `enhance`, `cleanup`, `refactor`, `fix`, or `hotfix`. Branches that ignored the convention did not get merged
- Pull requests stayed small enough to genuinely review, and stated what they did and which task they advanced or closed
- Time was logged against the task as a formal step of the workflow, not an afterthought

Owning a task end to end — from the details needed to start, through the code, through the documentation — creates a far stronger sense of responsibility than a hand-off model does. It also means every dependency gets surfaced by the person doing the work, rather than discovered later by someone else.

---

## Scale, a year after handover

In **June 2021** — roughly a year after the rebuild shipped and after my day-to-day involvement had ended — the platform recorded **274,000 clicks** and **7.38 million impressions** from Google Search in that single month.

I want to be careful about how I claim that number. Search performance belongs substantially to the marketing and content teams, and by then the platform had been running and evolving without me for a year.

That is exactly why I find it the most satisfying figure in this story. It is not evidence of a launch. It is evidence that what we built kept carrying real commercial traffic long after the person who led the build had left.

---

## What I take from it

Three separate returns to the same company, years apart, is its own kind of signal — each time for a different problem: execution and tooling in 2015, a specific operational system in 2017, and a full platform and organisational rebuild in 2019.

What ties them together is that each engagement left something behind that outlived it. A WordPress store that grew into a full specialty platform. Infrastructure a growing team could stand on. And finally a Laravel platform, an integrated ERP, and a development culture that kept running and compounding long after my day-to-day involvement ended.
