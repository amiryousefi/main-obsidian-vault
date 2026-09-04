---
created: 2026-07-31
source: Amir2.0/strategy/website-strategy.md
---

# Website Strategy: `amiryousefi.com`

## The Current Failure
The current live website is a digital artifact from 2019. It positions Amir as a junior "full-stack web developer" looking for freelance work. It actively damages his credibility as a CTO, a gaming company executive, and the future CEO of GULFTECH. 

The Next.js scaffold in the `new-amiryousefi.com` repository is technically impressive but entirely empty. It is a beautiful house with no furniture. The strategy is not to build a better house; the strategy is to move in.

## The Core Objective
The new `amiryousefi.com` must serve as the premium, public-facing headquarters for Amir 2.0. It must accomplish three things immediately:
1. Establish his authority as a Builder-CEO and Creative Technologist.
2. Sell high-ticket advisory services to founders and established businesses.
3. Act as the primary lead generation engine for GULFTECH.

## Information Architecture & Content Strategy

### 1. Homepage (The Authority Anchor)
**Goal:** Immediately communicate premium positioning and direct visitors to the right pathway.
- **Hero Section:** Remove generic developer greetings. 
  - *Suggested Headline:* "Transforming complex technology into business outcomes."
  - *Suggested Subheadline:* "I help founders and leadership teams architect resilient digital systems, integrate practical AI, and build premium products. 15+ years of engineering and product leadership."
- **Social Proof:** Highlight CTO roles (TodaysCrypto, Apprang), OxinGame leadership, and 15 years of experience.
- **Pathways:** Clear entry points for "Advisory Services," "Digital Products," and "GULFTECH Studio."

### 2. Services (The Advisory Engine)
**Goal:** Sell Amir's brain, not his hands.
- **AI-Era Product Strategy:** High-ticket consulting sessions for founders needing roadmap clarity and technical validation.
- **Architecture & Delivery Advisory:** Fractional technical leadership for growing teams hitting scaling bottlenecks.
- **Digital Transformation:** Executive advisory for organizations modernizing their technology stack.
- *Crucial Distinction:* Explicitly state that implementation is handled via GULFTECH, separating Amir's advisory time from execution hours.

### 3. Products (The Scalable Knowledge)
**Goal:** Monetize expertise asynchronously and build a qualified email list.
- **Cloud Readiness Assessment Kit:** A framework for evaluating cloud maturity.
- **Reference Architecture Library:** Production-tested blueprints for common patterns.
- **DevOps Transformation Playbook:** Guides for building platform teams.
- *Action Item:* These products are currently placeholders in the `products.ts` file. Amir must actually write the content for at least *one* of these to launch the site.

### 4. Projects / Case Studies (The Proof)
**Goal:** Demonstrate capability through outcomes, not just code.
- **TodaysCrypto:** Highlight the Next.js/Laravel architecture and leading a remote team.
- **Sayman e-commerce:** Focus on the migration from WordPress to a scalable Laravel platform handling 20k daily visitors.
- **OxinGame:** Frame this as product and systems advisory that modernized operational workflows.
- *Rule:* Do not list side projects or GitHub tutorials here. Only feature projects that drove business outcomes.

### 5. Publications / Thinking (The Intellectual Capital)
**Goal:** House long-form essays and thought leadership.
- Integrate the Medium articles, but *only* if they are updated or relevant. The 2019 technical tutorials should be archived or moved to a separate "Developer Notes" section.
- This section must feature new, strategic writing on AI, MENA tech, and product leadership.

## The GULFTECH Connection
`amiryousefi.com` and GULFTECH are distinct but symbiotic. 
- Amir's site sells *strategy and advisory*.
- GULFTECH sells *execution and delivery*.
- The website must feature a prominent section or banner: "Need a full team to execute? I build premium products through my studio, GULFTECH." This funnels high-intent, well-funded leads directly to the agency.

## Implementation Plan (The Next 14 Days)
Amir 1.0 will want to tweak the Three.js particle animations. Amir 2.0 will ship the content.

1. **Days 1-3:** Open `src/data/site.ts`, `services.ts`, and `projects.ts`. Replace every single placeholder string with the actual copy outlined above.
2. **Days 4-7:** Write the copy for the Homepage and About sections. Ensure the tone is executive, precise, and premium (referencing the GULFTECH style guide).
3. **Days 8-10:** Finalize one digital product (even if it's a simple, high-value PDF checklist) to ensure the Products page functions.
4. **Days 11-14:** Deploy the Next.js site to Vercel. Point the domain. Kill the 2019 site forever.
