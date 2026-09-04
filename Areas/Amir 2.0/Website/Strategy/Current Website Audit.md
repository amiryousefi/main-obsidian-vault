---
created: 2026-05-27
source: amiryousefi.com/info/current-website-audit.md
---

# amiryousefi.com - current website audit (May 27, 2026)

## Scope reviewed
- Homepage: `https://amiryousefi.com`
- Metadata and social tags from `<head>`
- Public route checks (`/about`, `/projects`, `/portfolio`, `/blog`, `/contact`, etc.)
- `robots.txt`

## What exists today

### 1. Site structure
- The site is currently a **single-page personal profile**.
- The homepage is reachable and loads correctly.
- Common subpages return a GitHub Pages 404 (no additional public pages detected in this review).

### 2. Main messaging
- Positioning: full-stack web developer + IT analyst/consultant.
- Hero headline: "Hello I'm Amir Yousefi!"
- About copy explains:
  - full-stack development experience across database, backend, frontend, and UI/UX
  - consulting and analysis background in IT projects
- Primary action: social/profile links ("Let's connect", "Connect with me").

### 3. Outbound links present
- GitHub
- LinkedIn
- Medium
- YouTube
- Twitter/X
- Instagram

### 4. Technical/SEO signals observed
- Has title and meta description.
- Has canonical, Open Graph, and Twitter card tags.
- Uses a profile image and favicon.
- Served via GitHub Pages + Cloudflare.

## Weak points / critique

### High impact
1. **No portfolio proof on the site itself**
   - The homepage claims strong capability, but there are no project cards, case studies, outcomes, or metrics.
   - Visitors must leave the site to judge your work, which adds friction and hurts conversion.

2. **No clear conversion path**
   - There is no direct "Hire me", "Book a call", or contact form CTA.
   - Social links are useful, but they are weak as a primary conversion flow for business inquiries.

3. **Single-page depth is too limited for 2026 expectations**
   - No dedicated pages for projects, services, resume, writing, or contact.
   - This reduces discoverability and makes the brand feel less active/current.

### Medium impact
4. **Copy quality and readability issues**
   - Several grammar/style problems ("on my developer side", "as I was in many I.T projects", inconsistent capitalization/punctuation).
   - Long dense paragraphs reduce scanability and confidence.
   - Value proposition is broad; it does not quickly say who you help and what outcomes you deliver.

5. **Metadata implementation has correctness gaps**
   - Canonical and some OG values are set to protocol-relative placeholders like `//` instead of full absolute URLs.
   - `og:image` is not an absolute URL.
   - `twitter:site` appears to point to a template account (`@tailwindmade`) rather than your own brand handle.

6. **Limited trust and authority signals**
   - No testimonials, client logos, certifications, notable achievements, or quantified impact.
   - No timeline of experience or role history.

### Lower impact (but worthwhile)
7. **Accessibility and semantic opportunities**
   - The page appears visually simple, but semantic landmark structure can be improved (for example explicit `nav/main/footer` landmarks).
   - Image alt text is generic ("author") and can be made more descriptive.

8. **Content freshness risk**
   - The page appears long-lived with minimal visible evolution; this can signal inactivity to recruiters/clients.

## Recommended direction for the next version
- Build a multi-section or multi-page structure:
  - Home (clear value proposition)
  - Projects/Case Studies
  - Services
  - About
  - Contact
- Add strong CTAs: email button, meeting booking link, simple contact form.
- Rewrite copy to be concise, outcome-oriented, and audience-specific.
- Add proof: featured projects, metrics, testimonials, and resume highlights.
- Fix metadata to use absolute canonical/OG URLs and correct social handles.
- Improve semantic structure and accessibility details during redesign.
