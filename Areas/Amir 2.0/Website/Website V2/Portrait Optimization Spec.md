---
created: 2026-05-28
source: amiryousefi.com/info/website-v2/portrait-optimization-spec.md
---

# Portrait optimization spec (website)

Date: May 28, 2026  
Status: source located and optimized assets generated

## Generated outputs

Source:
- `info/Amir Yousefi.jpg`

Generated:
- `code/website-v2/assets/amir-yousefi-hero-1024.webp`
- `code/website-v2/assets/amir-yousefi-hero-800.webp`
- `code/website-v2/assets/amir-yousefi-hero-480.webp`
- `code/website-v2/assets/amir-yousefi-hero-1024.jpg` (JPEG fallback)

## Optimization goals

- Keep visual quality high for premium feel.
- Minimize file size for fast loading.
- Preserve facial detail and natural skin tones.

## Recommended processing

1. Crop for composition (portrait-focused, enough breathing room around face).
2. Mild color and contrast balancing for site palette harmony.
3. Export to WebP quality range ~72-82.
4. Keep hero image payload ideally under ~300KB for primary size if visually acceptable.

## Portrait style target (confirmed)
- **Natural realistic**
- Preserve authentic skin tones and facial texture.
- Avoid dramatic filters and over-stylized grading.

## Integration guidance

- Use responsive `<picture>` setup in hero section.
- Provide descriptive `alt` text.
- Avoid heavy filters that make portrait look artificial.

## Next action required

Next step:
- wire these responsive assets into the Website V2 hero `<picture>` element.
