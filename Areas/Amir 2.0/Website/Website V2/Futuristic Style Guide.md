---
created: 2026-05-27
source: amiryousefi.com/info/website-v2/futuristic-style-guide.md
---

> [!note] Overlaps with [[Style Guide]] — both are V2 style guides written the same week (May 27, 2026). Worth merging.

# Website V2 style guide (futuristic premium)

Date: May 27, 2026  
Brand mode: premium futurism  
Design goal: "strategic intelligence, not startup noise"

---

## 1) Design intent

The visual system should feel:
- advanced but trustworthy
- modern but not flashy
- premium but not sterile

This is not a "developer portfolio" aesthetic.  
It is an advisor-grade interface: elegant, intentional, and high-signal.

---

## 2) Core design principles

1. **Depth over decoration**  
   Use layered backgrounds and subtle light effects, not clutter.

2. **Signal hierarchy**  
   Headlines and structure should communicate strategy, not just style.

3. **Restraint wins premium trust**  
   Keep color accents controlled; avoid visual shouting.

4. **Readable intelligence**  
   Every section should be scannable in under 10 seconds.

5. **Motion with purpose**  
   Use animation to guide focus, never as visual noise.

---

## 3) Color system

### Base
- `#060b16` - deep space background
- `#0f1a33` - surface
- `#152345` - elevated surface
- `#eaf1ff` - primary text
- `#9eb0d9` - secondary text

### Accent (primary)
- `#6ea8ff` - brand electric blue
- `#8f7dff` - violet signal
- `#49d6ff` - cyan highlight

### Accent usage rule
- 80% neutral / 20% accent
- CTAs use blue-violet gradient
- keep no more than 2 bright accents visible in one viewport

---

## 4) Typography

## Headings
- Font: `Space Grotesk`, fallback `Inter`, sans-serif
- Character: geometric, modern, confident
- Use:
  - H1: 52-68 px desktop, 36-44 px mobile
  - H2: 30-40 px desktop, 24-30 px mobile

## Body
- Font: `Inter`, fallback system sans
- Size: 18 px desktop / 16-17 px mobile
- Line-height: 1.6 to 1.75 for premium readability

## Tone rule
Headlines are strategic and atmospheric.
Body copy is practical and precise.

---

## 5) Layout system

- Container max width: 1180 px
- Inner content width for text-heavy blocks: 760-820 px
- Section spacing: 96-132 px vertical on desktop
- Card radius: 16-22 px
- Surface blur/overlay allowed for depth panels

Grid patterns:
- Hero: 2-column (story + visual object)
- Core sections: 3-column cards or 2-column split
- CTA zone: centered single-column with generous breathing room

---

## 6) Graphics direction

## Graphic language
- orbital lines
- grid horizons
- glow nodes
- gradient halos
- wireframe-like flow paths

## Do
- use vector/SVG graphics
- keep graphics abstract and conceptual
- use "systems intelligence" visual metaphors

## Avoid
- stock-photo startup clichés
- cartoon illustrations
- noisy 3D gimmicks

---

## 7) Motion and interaction

Recommended interactions:
- soft parallax background drift (very subtle)
- hover-lift on cards (2-4 px)
- glow-intensify on CTA hover
- section fade/slide-in on scroll

Motion timings:
- 180-260ms for UI transitions
- 500-900ms for ambient decorative motion loops

Accessibility:
- respect `prefers-reduced-motion`
- motion must never block readability

---

## 8) UI components

## Buttons
- Primary: gradient fill (`#6ea8ff -> #8f7dff`)
- Secondary: outlined glass panel
- Radius: 12 px
- Shadow: subtle glow only

## Cards
- Dark translucent backgrounds
- 1 px cool-toned border
- Soft inner highlight
- Optional top-edge gradient line for premium feel

## Badges / pills
- low-contrast panels with uppercase micro labels
- use for categories like: Strategy, Architecture, AI, Advisory

---

## 9) Imagery and portrait direction

When portrait is added:
- dark editorial look
- controlled highlights
- confident but calm posture
- avoid overprocessed lifestyle imagery

If no portrait:
- rely on abstract signature graphics + typography system

---

## 10) Page-level style intent

### Home
Cinematic strategic entry with narrative pacing.

### Services
Structured, decision-grade clarity.

### Case studies
Outcome-focused, low-noise proof layout.

### About
Authority + worldview + operating method.

### Book a call
High-trust conversion surface with qualification-first structure.

---

## 11) Content + design pairing rules

- Every major visual section must answer one strategic question.
- Never place dense copy on complex graphics without contrast panels.
- Keep one emotional line + one practical line per section intro.
- Use whitespace to imply confidence and authority.

---

## 12) Implementation notes (V2 prototype)

- Build as a static first-pass with reusable CSS tokens.
- Use SVG assets for hero and ambient backgrounds.
- Keep all key decisions mapped to this guide before framework migration.

---

## 13) Personalization update (May 28, 2026)

To avoid a "too corporate" feel while staying premium:

### Voice-to-visual alignment
- Visual tone should support a **battle-tested builder** identity, not a pure consulting brand facade.
- Keep polish high, but add warmth through narrative spacing and personal section framing.

### Personal imagery rule
- Introduce a personal portrait/graphic element in hero or early proof section.
- Portrait treatment should remain editorial and restrained (dark, confident, minimal retouching).
- Personal imagery should work with, not replace, abstract system graphics.

### Exclusivity cues
- Use subtle high-trust exclusivity language (for example limited advisory capacity).
- Avoid hard scarcity or aggressive conversion gimmicks.

### Narrative priority
- "Who I am" and "why trust me" must visually precede offer packaging.
- Service cards should feel secondary to personal credibility and proof.

---

## 14) Late personalization refinement (May 28, 2026)

### Visual character
- Prefer a **hybrid minimal** visual system:
  - minimal layouts and clean rhythm
  - graphics only where they add meaning
  - avoid decoration without narrative purpose.

### "Soul" requirement
- Introduce warmth through:
  - personal visual cues
  - thoughtful narrative spacing
  - language that signals care and intent.
- Keep execution professional and restrained.

### Premium exclusivity style
- Recommended phrase: **"Selective advisory engagements each quarter."**
- Placement guideline:
  - use as a subtle trust/fit signal
  - avoid repeated scarcity patterns.

### Proof ordering guidance
For strongest first impression in premium flow:
1. Oxin
2. TodaysCrypto
3. Sayman

### Content-rich guidance
- Homepage should include both:
  - **How I Think** (top-level thinking layer)
  - **Field Principles** (practical insight layer)
- Promotional content should exist in two distinct modules:
  - Services
  - Products
