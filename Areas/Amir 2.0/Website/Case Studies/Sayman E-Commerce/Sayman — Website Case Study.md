---
created: 2026-09-05
status: ready for review
---

# Sayman — website case study

Built from [[Sayman E-Commerce Case Study|the draft]]. Follows
[[Case Study Skeletons]] and the approved copy in
[[Final Website Content and Info]] (§8.3). Case 3 of 3.

---

## Card copy (index page)

**Title:** Legacy e-commerce modernisation, from WordPress to Laravel

**Challenge hook:** A WordPress store carrying 20,000 daily visitors had
outgrown its foundation — and could not afford to go dark during the fix.

**Outcome hook:** A purpose-built Laravel platform with marketplace
capability, migrated with near-zero downtime, still running years after
handover.

---

## Full case

### Client context

SaymanDigital — an e-commerce business selling digital goods, running on
WordPress. **5,000+ products, 20,000+ visitors a day.** Real revenue, real
customers, real order history.

I led the engineering team here as **Development Team Lead, August 2019 to
June 2020**, with a team of five across backend and frontend.

### Initial challenge

The platform had outgrown its foundation. WordPress with a layer of custom
plugins had carried the business to this point and could not carry it further
— every new operational requirement meant another plugin, and every plugin
made the system harder to reason about.

The constraint that shaped everything: this store was trading. A migration
that took the site down, lost order history, or broke the workflows that
customer service and warehouse staff depended on would cost more than the old
platform ever did.

### Role and scope

Team lead with ownership across strategy, architecture, delivery process, and
implementation. Also responsible for recruiting into the team and for the
working practices it adopted.

The scope reached past engineering: customer service, shipping and packaging,
and supply all had procedures encoded in the old system, and all of them had a
stake in the new one.

### Strategic decisions

**1. Study the legacy system before replacing any of it.**
Custom plugins, data structures, customer service methods, inventory
procedures, content creation flow — all documented first. Most failed
migrations fail here: the team rebuilds the visible product and discovers too
late that the business ran on undocumented behaviour buried in the old system.

**2. Break one big e-commerce platform into sub-systems.**
Catalogue, orders, invoicing, discounts, notifications, permissions, and the
public API as separable pieces rather than one monolith. This is what let five
people work in parallel without constant collisions.

**3. Treat the migration as a business event, not a deploy.**
Data and platform moved from WordPress to Laravel with **almost zero
downtime** — sequenced so the store kept trading throughout.

**4. Interview the other teams as users.**
Customer service, shipping and packaging, and supply were treated as
first-class users with their own workflows, not as people who would adapt to
whatever engineering shipped.

**5. Write the practices down.**
A developer handbook, coding standards, and documentation — introduced during
the project, not after it, so the team could absorb new members without losing
pace.

### Execution highlights

- **Laravel platform built from scratch** with marketplace capability, on
  Laravel and React.
- **Near-zero-downtime migration** of products, users, and full order history
  off WordPress.
- **Operational tooling** — bulk price updating, advanced invoicing, and
  discount management scoped by user, product, and product variation.
- **Notification system** across email, SMS, web, and app push.
- **Permissions and roles** management, plus a RESTful API.
- **ERP implementation** alongside the platform work.
- **Price monitoring** (Python, Django) crawling competitor sites and
  surfacing every relevant price change.
- **Sales and support automation** (Python, Flask, Selenium) for government tax
  and customs registration and bank identity cross-checks — processes with no
  API, automated by driving the panels directly.

### Outcomes

**Platform:** A modern e-commerce system serving 5,000+ products to 20,000+
daily visitors, with the operational tooling the business actually ran on.

**Migration:** Products, users, and order history moved with almost no
downtime and no loss of commercial continuity.

**Operations:** Manual pricing, invoicing, tax registration, and fraud checking
replaced with automated flows.

**Team:** Five engineers working to written standards, with a handbook that
outlived the project.

### Lasting impact

This is the case I would point a sceptical buyer at. **The team and the
software kept performing for years after I left.** Delivery capability that
degrades the moment the lead walks out was never capability — it was
dependency.

### What this proves

Legacy systems can be modernised without losing business-critical history or
operational value. The lesson underneath: the migration is the easy half. The
hard half is capturing the undocumented business logic living in the old
system and in the heads of the people using it.

---

**If you are facing similar challenges, book a strategy call.**
