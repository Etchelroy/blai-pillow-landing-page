# PILLOW COMPANY LANDING PAGE â RESEARCH BRIEF

**SUMMARY:**
Landing page for a pillow company using a white primary / blue secondary color scheme, designed to convert visitors into customers through clear value messaging, product showcase, and trust-building elements.

---

**APPROACH:**

**Tech Stack:**
- **Framework:** Next.js 14+ (SSG/SSR for SEO, built-in Image optimization)
- **Styling:** Tailwind CSS with custom white (#FFFFFF) and blue (#2563EB or #1D4ED8) tokens
- **Hosting:** Vercel (Next.js native, built-in CDN, analytics)
- **CMS:** Optional headless CMS (Contentful or Sanity) for product/testimonial management, or hardcoded JSON for MVP
- **Analytics:** Vercel Analytics + Google Tag Manager for conversion tracking
- **Email:** Mailchimp or ConvertKit for newsletter signup

**Why this stack:**
- Next.js handles server-side rendering for SEO (critical for e-commerce)
- Tailwind enforces consistent 8px grid spacing and WCAG color compliance out of box
- Vercel's Image component auto-optimizes for web performance
- Minimal dependencies = faster load times = higher conversion

---

**REQUIREMENTS:**

**Hero Section**
- Full-viewport header with hero image (pillow lifestyle shot or product hero) as background with 40% white overlay
- Centered headline (H1, max 60 chars): value proposition ("Better Sleep. Better You.") in dark gray/charcoal
- Subheadline (max 100 chars) in medium gray
- Two CTAs: Primary blue button ("Shop Now") + secondary white-outline button ("Learn More")
- Mobile: Stack vertically, reduce image size, touch-friendly 48px+ button targets

**Product Showcase Section**
- 3-4 product cards in grid (responsive: 1 col mobile, 2 col tablet, 3 col desktop)
- Each card: product image (aspect ratio 1:1), product name, 1-line description, price, "Add to Cart" CTA
- Hover state: 4px shadow lift, 200ms transition, image slight zoom
- Alt text on all images for accessibility

**Features/Benefits Section**
- 4 benefit blocks in 2x2 grid (mobile: single column)
- Icon + headline + 2-3 line description
- Icons: simple, 48x48px, blue fill on white background
- Examples: "Ergonomic Support," "Temperature Control," "Hypoallergenic," "Lifetime Comfort Guarantee"
- Contrast ratio â¥ 4.5:1 (WCAG AA)

**Testimonials/Social Proof Section**
- 3 testimonial cards with star rating (5 stars), quote, customer name + title
- Cards: white background with 1px light gray border, 8px border-radius
- Mobile carousel (swipe-enabled), desktop grid (3 columns)
- Star icons: yellow/gold (#FBBF24) for visual pop

**Trust Badges Section**
- Horizontal row: free shipping icon, 30-day returns, money-back guarantee, warranty badge
- Each 60x60px, centered text underneath
- Mobile: 2x2 grid, desktop: 4 across

**Newsletter Signup**
- Centered CTA with headline ("Join 50K+ Sleepers")
- Email input field + blue submit button (inline on desktop, stacked on mobile)
- Client-side validation: email format check before submission
- Success state: confirmation message ("Check your inbox!")

**Footer**
- 4 columns (desktop) / 1 column (mobile): Product Links, Customer Service, Company, Legal
- White text on navy/dark blue background (#1F2937 or #111827)
- Copyright, social icons (LinkedIn, Instagram, Facebook), newsletter signup repeat

**Navigation**
- Sticky header: white background, blue logo/text, 56px height (mobile), 64px (desktop)
- Links: Shop, About, FAQ, Contact
- Mobile: hamburger menu icon, slide-out drawer (full viewport width)
- Active link: blue underline (2px) or blue text

---

**CONSTRAINTS:**

**Performance:**
- Core Web Vitals: LCP <2.5s, FID <100ms, CLS <0.1 (Vercel Analytics must track)
- Image optimization: WebP format, lazy loading below fold, next/image component mandatory
- Bundle size: <100KB gzip (critical path JS)
- Mobile-first responsive: test on iPhone 12, iPad, desktop 1440px

**Accessibility (WCAG AA minimum):**
- Color contrast â¥ 4.5:1 for text (white on blue, dark gray on white passes)
- All images have descriptive alt text
- Form inputs have visible labels + error messages
- Keyboard navigation: Tab order logical, focus ring visible (2px blue)
- Screen reader tested: semantic HTML, ARIA labels where needed

**Browser Support:**
- Chrome/Edge 90+, Firefox 88+, Safari 14+, mobile browsers current -1 version
- Graceful degradation for older browsers (no animations, fallback colors)

**Dependencies:**
- Keep external libraries minimal: React, Tailwind, next/image only
- No jQuery, no heavy animation libraries (use CSS animations for micro-interactions)

---

**NOTES:**

**Best Practices:**
- Use semantic HTML: `<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`
- Color palette: White #FFFFFF, Primary Blue #2563EB, Dark Gray #374151, Light Gray #E5E7EB
- Typography: System fonts (Inter, Poppins) for fast load, max 2 font weights (400, 600)
- Spacing: Strict 8px grid (8px, 16px, 24px, 32px, 48px, 64px gaps only)
- Button sizes: 40px min height, 48px target on mobile (touch-friendly)

**Edge Cases:**
- Long product names: truncate to 2 lines with ellipsis, full name on hover (tooltip)
- Mobile hero image: use 16:9 aspect ratio (not full viewport heightâavoid scroll jank)
- Newsletter submission: disable button during submission, show loading spinner
- Form validation: real-time email check (regex or service), prevent duplicate submissions
- No products in cart: empty state message ("Start shopping") instead of empty grid

**SEO/Conversion:**
- Meta tags: dynamic title/description per page section
- Schema markup: Product, LocalBusiness, Review (JSON-LD)
- Open Graph tags for social sharing (image, title, description)
- UTM parameter tracking for ad campaigns
- Heatmap (Hotjar or similar) to monitor scroll depth, CTA clicks

**Design Tokens to Define:**
- Radius: 0px (sharp), 4px (inputs), 8px (cards), 12px (large blocks)
- Shadows: subtle (0 1px 2px rgba), medium (0 4px 6px rgba), lifted (0 10px 15px rgba)
- Animations: 200ms (micro), 300ms (transitions), ease-in-out (smoothness)