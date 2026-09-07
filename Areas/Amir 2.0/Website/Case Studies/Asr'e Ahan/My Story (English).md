---
created: 2026-09-02
---
# My Story (English)

Part of [[Asr'e Ahan]].

![[Attachments/AsreAhan/Logo/asreahan-logo.png|420]]

> [!info] At a glance
> - **Role:** IT consultant / advisor — not a full-time hire, not the implementation team
> - **Started:** 8 July 2020, in the middle of the COVID pandemic
> - **Commitment:** 20 hours per month on retainer, with a written report at the end of every month
> - **From first meeting to a developer under contract:** about nine weeks
> - **Result:** a hired team, a documented development process, a shipped version one — still running, and still being updated, more than five years later

---

## Who the client was

Asr'e Ahan is a steel and iron trading business with roughly thirty years behind it. The company started trading iron and steel in 1989, built its position the way that industry is traditionally built — on relationships, phone calls, and physical markets — and by 2019 had decided it needed to be online. It added an e-commerce arm and launched a marketplace for steel sections, connecting producers, distributors, and buyers directly: live pricing across the different steel products, market news, shipping, warehousing, credit sales, and pre-orders.

That combination is the whole reason this engagement is interesting. Here was a company that was genuinely strong and experienced in its own field, entering a field where none of that experience transferred. They knew steel. They did not know how software gets built, how developers are evaluated, or what a healthy development process looks like — and, crucially, they had no internal reference point for telling good technical advice from bad.

## The call before the call

My friend Mohammad called me: a startup he knew was looking to hire a developer. He asked my opinion about the candidate they wanted to bring on, and I ended up putting together their contract for them — both the technical points they needed to account for and the clauses that belong in a software agreement.

That day I told them something they did not act on. They would be better off having an IT consultant alongside them to guide them through this path. A development team on its own can lose its way, or lack a long-term view on the deeper things — like maintainability and the system's capacity to grow.

## The second call

A few months later I got another call from the Asr'e Ahan team.

They had gone ahead without a consultant alongside them, exactly the way I had warned against. Months had passed. Money and time had been spent. There was no real output, the stakeholders were frustrated, and — the part that mattered most — nobody could say clearly what had been built, what worked, or what was left to build.

That is the point where I came in.

## What I was actually hired to do

We signed a consulting agreement with a deliberately broad scope:

- Reviewing and proposing IT solutions that actually moved the company's goals forward
- Establishing and improving the software development process
- Building and maintaining the development roadmap **together with the stakeholders**
- Evaluating and reporting on how the work was being executed
- Recruiting and hiring the technical team

It was a retainer, not a full-time role: **20 hours a month**, with a written report to the client at the end of every month. Everything described below was built inside that budget.

> That constraint is the point, not a footnote. A company at this stage does not need a full-time executive it cannot yet justify. It needs the right decisions made in the right order, and someone accountable for them.

## Working through a pandemic

One more thing shaped all of it: this was the middle of COVID.

We wrote it directly into the contract — the work would be carried out through online meetings and remote collaboration, and if conditions worsened we would renegotiate *how* to continue, not *whether* to. The developer employment contract we later signed said the same thing: remote by default, no fixed place of work, occasional office visits by arrangement.

At the time, that was not the default way of working it later became. Most teams here were treating remote as a temporary emergency and waiting to go back to the office. We decided to treat it as the permanent shape of the team, and to design everything else around that assumption.

## Point A: knowing what already existed

The first thing we did was document the existing system. We mapped the development work that had already been done and the current state of the system, and treated that as point A.

That included getting my own hands on it. I went through their self-hosted GitLab, installed the previous team's source code, and ran and tested it myself. You cannot assess a codebase from a meeting. Four hours of actually standing the thing up told us more about what could be salvaged than any amount of discussion would have.

This is also the moment that answers the question the company could not answer: **what do we already own, and what is it worth?**

## Ending with the old team without losing the work

The previous developer, after frequent conflicts with the stakeholders, was no longer really collaborating — and was blocking the changes the development process needed. We decided to part ways.

But it mattered to us that the earlier effort would not go to waste, and that we would not restart from zero. So instead of simply terminating, I wrote a short handover protocol. It took 45 minutes and it committed both sides:

- The departing developer hands over the **latest** version of all code, the database, all design and engineering documentation, and every other artifact produced for the project
- He **explains how to use them** — source code, database, documentation — rather than just dropping a repository and leaving
- He cooperates with and advises the incoming developer or team
- The company pays everything owed through the final day
- The company **also pays for the hours spent on the handover itself**
- A portion of the payment is held back as a good-performance guarantee, released once those obligations are met

That last pair of clauses is the whole design. A clean handover was made the rational, paid choice for the person leaving, rather than something we had to hope for out of goodwill. Most companies in this position lose everything they paid for in the previous chapter. Asr'e Ahan did not.

## Hiring: process first, then people

The order here surprises people, so it is worth being precise about it. Before we wrote the job ad, and before we ended things with the old team, we wrote down how development would work.

| When | What |
|---|---|
| 8 July 2020 | First meeting — initial discussion and planning |
| 10 July 2020 | **Drafting the development process documentation** (the longest single item that month) |
| 11 July 2020 | Setting up GitLab; meeting with management |
| 22 July 2020 | Writing the developer job ad |
| 24 July 2020 | Writing the old-team handover protocol |
| 4 August 2020 | Reviewing GitLab, installing and testing the existing source code |
| 5–8 August 2020 | Screening resumes, coordination |
| 13 September 2020 | New developer signed |

We wrote a clear job description and listed what was genuinely required to carry the work forward and finish it. We wanted a team that would build both frontend and backend on JS, so we looked mainly for **full-stack developers**. That came from the flexibility we needed:

- It was not yet clear how much of the existing system we could reuse
- It was not yet clear which parts of the road ahead should be built first
- We wanted to be able to move people between areas as those answers emerged
- And full-stack people would read the existing code more easily and understand its different facets

### Hiring under COVID

The pandemic made this considerably harder.

The candidate pool itself had changed. People were reassessing their jobs, some were leaving the market, and others were suddenly open to working for companies in other cities because everything was remote anyway. Meanwhile we had to judge people we would never meet in a room — no shared whiteboard, no walking them past the team, none of the informal signals you normally lean on.

And we were hiring for a company whose stakeholders had just been burned by a developer who stopped collaborating. So communication and collaboration under remote conditions were not soft criteria for us. They were the thing we were most afraid of getting wrong.

We built a system for evaluating candidates, filtered the resumes down to a shortlist, and ran the entire process online.

## The developer handbook

In parallel with hiring, we wrote the document that turned out to matter more than anything else I produced there.

To make sure the new development team — and everyone hired afterwards — shared the same understanding of our standards and process, we created a **developer handbook**. It described how work actually moves, end to end:

- Every piece of work starts as a task on a single GitLab board
- Each task carries everything needed to do it: a clear name, an owner, an estimate, labels, a description, and any attached files or discussion
- Work moves through defined columns — **Open** (the backlog), **Doing**, **Today**, **Review**, **Closed**
- **Today** holds only tasks small enough to be finished by the end of the working day, and specified in enough detail to start immediately
- Every task gets its own branch, following one naming convention, tagged by type: feature, enhance, cleanup, refactor, fix, hotfix
- Every branch ends in a pull request, small enough that another human can genuinely review it, linked back to the task that motivated it
- Estimated time and actual time are both recorded against the task

We did not invent anything new. The company's git was already self-hosted on GitLab, so we ran project management on that same GitLab instance rather than introducing another tool.

### Why we kept it small

We deliberately kept the handbook short and simple. We did not want it to become a burden, and we did not want it to become the kind of document nobody reads. The test was that someone joining the team should be ready to work after a short read.

That constraint did more work than it appears to. A long process document is a process that will be ignored the first time there is deadline pressure — and once it is ignored once, it is dead. A short one survives, because following it is cheaper than working around it.

### Designed for a team that was never in the same room

Both the handbook and the development flow had to work for a team that was fully remote, and that assumption changed the design.

Nothing could depend on someone turning around and asking the person next to them, because there was no person next to them. Decisions had to leave a written trace. The state of any piece of work had to be readable from the board rather than reconstructed from a conversation. A new hire had to be able to onboard themselves.

Today that sounds obvious. In 2020 it was not.

### We made it binding, and we made it part of hiring

Two decisions gave the handbook real weight.

First, we wired it into the employment contract. The new developer was contractually obliged to work according to the company's documented internal standards, which had to be provided to him in written form, with changes effective from the moment they were communicated. The handbook was not onboarding decoration; it was part of the agreement.

Second, we used it in interviews. Every candidate who moved past the first stage read the handbook, and in the next stage we asked them either to explain it back to us or to tell us how they would improve it. That did three things at once: it tested how they think about process, it told us whether they could absorb written material without hand-holding — the core remote skill — and it meant nobody ever joined surprised by how we worked.

### Why this one document outlived me

Of everything I built there, the handbook is the piece that kept working after I left, and I think the reason is worth spelling out, because it generalizes.

**It made the process self-describing.** The board was not a reporting layer on top of the real work — it *was* the work. Any question about what was happening, what it cost, or who was waiting on whom could be answered by looking, not by asking. When the person who designed a process has to be present for the process to run, that is not a process; it is a dependency. The handbook removed me as a dependency on purpose.

**Its simplicity is what made it survivable.** Because it was small, it could be read in one sitting, argued with, and changed. Teams inherit documents they are afraid to touch, and those documents rot quietly while everyone works around them. This one was short enough that improving it was a normal, low-stakes act — we had literally invited candidates to critique it before they were even hired. So it evolved instead of ossifying. The version running there now is not the version I wrote, and that is exactly the intended outcome.

**Its transparency made the process outcome-based rather than activity-based.** Every task had an owner, an estimate, a real time spent against that estimate, a reviewer, and a definition of done that ended in merged code. That combination makes it structurally hard to be busy without producing anything — which, remember, is precisely the failure the company had just lived through. Nobody has to trust a status update when the status is visible.

**It gave the rest of the company a door in.** Other teams and stakeholders — marketing, SEO, the production units — filed their own requirements onto that same board, in the same format. That single decision did more for the relationship between the business and the development team than any meeting could have. The technical people stopped being a black box, and the business people stopped having to ask a favor to get something looked at. They could see their request, see its priority, and see it move.

That is why the handbook mattered more than the code we shipped. Code gets replaced. A clean, simple, transparent way of deciding what to build next does not — it compounds.

## Shipping version one

With the process in place and the team hired, we made the foundational decisions together: the tech stack, which of the existing code should stay and which should go, and what needed to be built new.

Because so much time had already been lost with no clear output, everything pointed at one goal — **publish version one**. We made every decision in service of that, including consciously accepting places where we knew a change would eventually be needed but it was not the right moment to refactor.

In a short time, we shipped the first version of the Asr'e Ahan platform.

Right after that we built a roadmap from the ideal big picture, worked out what maintaining and updating the system would require with very short release cycles, and — using my engineering background to see where the real structural weaknesses were — scheduled the refactors we had deliberately deferred.

## Working with stakeholders over video

Everything required to increase the team's velocity — documenting requirements, and the non-software processes needed to discover new parts of the system and how they should behave — came out of weekly interaction with the development team, the management team, marketing and SEO, the production units, other iron production factories (to understand the industry properly), and the rest of the stakeholders.

Nearly all of it happened online, and this was the part that took the most patience.

Running a remote development team is one thing. Running weekly requirements sessions over video with people who had spent thirty years doing this business face to face, on the phone, and in the market is another. Some of them had never worked that way in their lives. So part of the job was simply making the format work:

- Keep sessions short and specific rather than long and general
- Write down what was agreed and send it back, so nothing depended on memory
- Go to people individually when a group call was not producing the detail we needed

The documentation habit that later spread through the company started here, out of necessity. When you cannot walk down the hall to check something, writing it down stops being bureaucracy and becomes the only way the work moves.

## Roadmap and reporting

The roadmap was never something I handed over finished. It was built and updated together with the stakeholders, which is the only way it stays honest: they own the priorities, I own translating those priorities into something a development team can actually build against.

Alongside it, at the end of every month the client received a written report — what had been done, what was blocked, what was coming next. After a period where months had passed with no visible output, that cadence mattered nearly as much as the work itself. Nobody had to wonder where things stood.

## The results

- The development team had a clear roadmap and simple, unambiguous guidelines to build against
- Management and the main stakeholders had someone who could translate their needs into the development team's language — and could be confident the output would still be usable years later
- Documenting the current state, the target state, and the requirements to get between them was a simple move that spread to other teams
- Those teams not only documented their own processes better, they knew their technical needs would be answered through a defined process rather than through personal relationships

## Five years later

![[Attachments/AsreAhan/Logo/social-logo.jpeg|120]]

Asr'e Ahan has continued for **more than five years** with the development team I hired and helped start — and still does. The system we built is still running and still being updated.

It is also genuinely in use. The platform now handles around **60,000 visits a month** and carries **63 supplier partners** trading on it. I want to be careful about how I claim that: those are the numbers the business runs today, years after my involvement ended, and they belong to the team that kept building. That is exactly why I find them the most satisfying figure in this story. They are not evidence of a launch — they are evidence that what we set up kept compounding without me.

That is the actual goal, and it is a higher bar than shipping: a good software product built alongside a good software development process, both of which outlast the consultant.

## What I take from it

Asr'e Ahan is a good example of a company that can benefit from the skills and knowledge of a consultant who spent many years as a practitioner and is not afraid of execution.

It is also the example I reach for whenever I need to explain the difference between walking this path with a good consultant and walking it without one — because this company did both, in that order, and the contrast is unusually clean.

That difference matters most when you are established and strong in your own industry but only now entering the business of building software. Your existing expertise can fool you about your competence in this one. A good consultant prepares you for the risks and the opportunities ahead, builds better communication between the different partners in the software production chain, and makes sure the path you have laid out is actually being followed.
