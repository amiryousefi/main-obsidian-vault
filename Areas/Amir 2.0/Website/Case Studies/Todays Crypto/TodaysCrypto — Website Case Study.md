---
created: 2026-09-05
status: ready for review
---

# TodaysCrypto — website case study

Built from [[Todays Crypto Case Study|the draft]] and
[[Platform Feature Report]]. Follows [[Case Study Skeletons]] and the approved
copy in [[Final Website Content and Info]] (§8.2). Case 2 of 3.

---

## Card copy (index page)

**Title:** Video platform direction for a crypto-niche audience and regulated publishers

**Challenge hook:** Build a YouTube-class media platform for a volatile
crypto audience — from a standing start, in a chaotic early-stage company.

**Outcome hook:** A three-surface platform with Web3-native identity,
publisher governance, and token and membership economics, delivered by a team
of four.

---

## Full case

### Client context

A Swedish company building a video-sharing platform for the cryptocurrency and
blockchain community — the product category of YouTube, the audience and
compliance profile of crypto. Early-stage, remote, and moving fast.

I have led this as **Chief Technology Officer since December 2020**.

### Initial challenge

Two problems arrived at once, and neither could wait for the other.

The **product** problem: a general-purpose video platform is already hard —
upload, transcode, watch, subscribe, recommend, monetise. This one also needed
wallet-based identity, a platform token, NFT-gated membership, KYC, and market
data, because that is what the audience expects as table stakes.

The **organisational** problem: an early-stage environment with shifting
priorities, direct stakeholder pressure, and no established delivery process.
The risk was not that the platform could not be built. It was that a small
team would be pulled apart by changing direction before it shipped anything
durable.

### Role and scope

CTO. Ownership of architecture, technology decisions, and the development
process itself — plus building and leading the team, and representing
engineering in stakeholder discussions where scope and direction were set.

Team of four.

### Strategic decisions

**1. Split the platform into three surfaces with one contract between them.**
A Next.js web app for viewers, a React panel serving both publishers and
admins, and a Laravel API behind both. One backend contract, three independent
release paths — so creator-facing work never blocked viewer-facing work.

**2. Buy SSR for the viewer app, deliberately.**
A media platform that search engines cannot read has no discovery. Next.js
with server-side rendering was chosen for SEO reach, not developer fashion —
the one place where the architecture had to serve growth directly.

**3. Split the datastore by access pattern.**
Relational data in MySQL; watch times, token points, and channel statistics in
MongoDB. Write-heavy, high-volume behavioural data does not belong in the same
store as business records, and separating them early avoided a painful
migration later.

**4. Treat publisher governance as architecture.**
Regulated publishing, KYC identity verification, and role-separated
admin/publisher tooling were designed into the platform rather than bolted on
under pressure.

**5. Install a delivery process before scaling the team.**
In a chaotic environment, process is not bureaucracy — it is the thing that
keeps four people pointed the same way. Development flow came first, then
hiring.

### Execution highlights

- **Viewer web app** — Next.js with SSR, responsive with distinct mobile and
  desktop component trees, custom video player, personalised feeds, playlists,
  podcasts, and live market pages.
- **Publisher and admin panel** — a single React application serving creator
  workflows and back-office administration, with video studio, bulk editing,
  tagging, and full user management.
- **Laravel API** — OAuth 2.0 via Passport, Redis caching and queues, real-time
  through Laravel WebSockets and Pusher, video stored on S3 and Cloudflare R2.
- **Web3-native identity** — wallet authentication alongside email and magic
  links, so crypto users onboard the way they expect to.
- **Platform economics** — the TCG token, NFT-based Hero memberships, and a
  referral programme, with payments through both Stripe and Coinbase Commerce.
- **Compliance layer** — Idenfy KYC verification and Google 2FA.

### Outcomes

**Platform:** A crypto-focused video platform in production, covering the full
creator-to-viewer loop and supporting regulated publishers.

**Team:** A team built and led through an early-stage environment, with a
delivery process that survived shifting priorities.

**Continuity:** Sustained CTO ownership since 2020 — the architecture set at
the start has carried years of feature growth without a rewrite.

> **To confirm before publishing:** audience scale. The old CV claims ~10M
> users per month; the homepage claims 20k+ daily visitors, which actually
> belongs to Sayman. Pick the number you can defend on a call, or publish this
> case with no traffic claim at all — it is strong without one.

### Lasting impact

The three-surface architecture is still the shape of the product. Decisions
made in the first months — the API contract, the datastore split, SSR for
discovery — are the ones that let a four-person team keep shipping into a
category that changes monthly.

### What this proves

Platform-level direction holds up where content, compliance, and growth
pressures collide at once. The lesson underneath: in a volatile market, the
architecture's job is to make the *next* pivot cheap.

---

**If you are facing similar challenges, book a strategy call.**
