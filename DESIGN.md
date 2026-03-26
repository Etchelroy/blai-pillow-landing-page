# PILLOW E-COMMERCE LANDING PAGE DESIGN

**SUMMARY:** Clean, premium pillow landing page with white-dominant layout, calming blue accents, and trust-focused messaging that guides visitors from product discovery to checkout.

---

## LAYOUT

**STICKY NAVIGATION (top, fixed)**
- Left: Logo/brand name (32px height)
- Center: Nav links (Home, Shop, About, Reviews)
- Right: Cart icon + Search icon
- Height: 64px, white background, subtle shadow below
- Full width, z-index priority

**HERO SECTION (full viewport height)**
- Split layout: 50% left text, 50% right image
- Left side: Headline (48px), subheadline (20px), 2 CTAs (Shop Now + Learn More buttons)
- Right side: Hero pillow product image (full height, cover fill)
- Background: White
- Text aligned left, generous padding (80px top/bottom, 60px left/right)

**PRODUCT GRID SECTION**
- Headline centered (40px) + subtext (18px)
- 4-column responsive grid (3 col tablet, 1 col mobile)
- Card height: 280px
- Each card: image (200px tall), product name (20px bold), short description (14px), price (24px bold blue), "Add to Cart" button
- Spacing: 24px gap between cards, 80px section padding top/bottom

**BENEFITS SECTION (3-column layout)**
- Background: Off-white (#F9FAFB)
- Headline centered (40px)
- 3 benefit cards, each with:
  - Icon area (80x80px, blue background circle)
  - Benefit title (20px bold)
  - Description text (16px)
- Cards: 240px width, 320px height, white background, 8px rounded corners
- Padding: 80px top/bottom, 60px left/right

**TESTIMONIALS SECTION**
- Background: White
- Headline centered (40px)
- 3-column carousel/grid of testimonial cards
- Each card: 280px wide, 240px tall, white background, 2px blue left border
- Content: 16px quote text, 14px reviewer name + role below
- Star rating (5 stars, blue #2563EB) above quote
- Padding: 80px section

**TRUST BADGES ROW**
- Background: Light blue (#EFF6FF)
- Centered horizontal layout: 4-5 badge groups
- Each badge: icon (48x48px) + text (14px) + label (12px gray)
- Examples: "30-Night Trial", "Free Shipping", "100% Natural Materials", "2-Year Warranty"
- Height: 120px, padding 40px top/bottom

**NEWSLETTER SIGNUP**
- Background: White
- Centered text: Headline (32px), description (16px)
- Input field: 100% max-width 400px, 16px font, 48px height, blue border on focus
- Button: "Subscribe" (48px height, blue background, white text)
- Padding: 80px top/bottom, centered

**FOOTER**
- Background: Dark blue (#1E293B) or very dark gray
- 4 columns: Company info, Shop links, Customer Service, Social icons
- Text: 14px, light gray (#D1D5DB)
- Links: white on hover, 2px blue underline
- Bottom bar: copyright (12px gray), centered
- Height: 340px total

---

## COLORS

| Element | Hex | Usage |
|---------|-----|-------|
| **Primary Background** | #FFFFFF | Main page background, cards, hero |
| **Secondary Background** | #F9FAFB | Benefits section, subtle contrast areas |
| **Accent Light Blue** | #EFF6FF | Trust badges row, hover states |
| **Primary Blue** | #2563EB | Buttons, links, accents, icons |
| **Dark Blue (Footer)** | #1E293B | Footer background |
| **Primary Text** | #1F2937 | Headlines, body copy (dark gray) |
| **Secondary Text** | #6B7280 | Descriptions, metadata (medium gray) |
| **Light Text** | #D1D5DB | Footer text, captions |
| **Border/Lines** | #E5E7EB | Card borders, dividers |
| **Success/Hover** | #1D4ED8 | Darker blue on button hover |

---

## COMPONENTS

**BUTTON â "Shop Now" / "Add to Cart" (Primary)**
- Dimensions: 48px height, 160px width (responsive)
- Background: #2563EB
- Text: White, 16px bold, uppercase letter-spacing
- Border radius: 6px
- Hover: Background #1D4ED8, slight lift shadow (0 4px 12px rgba(37, 99, 235, 0.3))
- Focus: 2px white outline, 4px offset
- Cursor: pointer

**BUTTON â "Learn More" (Secondary)**
- Dimensions: 48px height, 160px width
- Background: Transparent
- Text: #2563EB, 16px bold
- Border: 2px solid #2563EB
- Hover: Background #EFF6FF, border stays blue
- Focus: 2px blue outline
- Border radius: 6px

**INPUT FIELD â Newsletter Email**
- Height: 48px
- Width: 100% (max 400px)
- Font: 16px, system font
- Padding: 0 16px
- Border: 2px solid #E5E7EB
- Border radius: 6px
- Focus: Border #2563EB, shadow 0 0 0 3px #EFF6FF
- Placeholder text: #9CA3AF (light gray)

**PRODUCT CARD**
- Width: responsive (25% desktop, 33% tablet, 100% mobile)
- Background: White
- Border: 1px solid #E5E7EB
- Border radius: 8px
- Image area: 200px tall, cover fill, rounded top
- Text area: 80px (product name + description + price)
- Hover: Shadow 0 10px 25px rgba(0, 0, 0, 0.1), slight scale up (1.02)
- Transition: 200ms ease

**TESTIMONIAL CARD**
- Width: 280px
- Background: White
- Border: 2px solid #2563EB (left side only)
- Border radius: 4px
- Padding: 24px
- Star rating: 5 stars, each 18px, #2563EB
- Quote: 16px, #1F2937, italic
- Name: 14px bold, #1F2937
- Role: 12px, #6B7280
- Hover: Shadow 0 8px 20px rgba(37, 99, 235, 0.15)

**NAVIGATION LINK**
- Font: 16px medium
- Color: #1F2937
- Hover: #2563EB, underline 2px
- Focus: Outline 2px #2563EB, 2px offset
- Padding: 8px 12px

**TRUST BADGE**
- Icon: 48x48px, centered, blue (#2563EB)
- Text below: 14px bold, #1F2937
- Label below text: 12px, #6B7280
- Total width: 120px, centered

---

## INTERACTIONS

**HOVER â Product Card**
- Shadow increases: 0 10px 25px rgba(0, 0, 0, 0.1)
- Card scales slightly: 1.02x
- Image brightness: +5% overlay fade
- Duration: 200ms ease-out
- "Add to Cart" button becomes more prominent (darker blue)

**CLICK â "Shop Now" Button**
- Button fills with darker blue (#1D4ED8)
- Micro-press animation: scale down 0.98 for 100ms
- Navigate to /shop (TBD by dev)
- Visual feedback: 300ms transition

**CLICK â "Add to Cart"**
- Button text changes to "Added â" temporarily (2 seconds)
- Cart icon in nav blinks/pulses (blue glow)
- Small toast notification (optional): "Item added to cart" (4px gap from cart, 12px text, white bg, slide in from right)
- Then revert to "Add to Cart"

**FOCUS â Navigation Links**
- 2px solid blue (#2563EB) outline, 2px offset
- Visible to keyboard users (Tab key)
- No outline-color removal

**FOCUS â Input Field (Newsletter)**
- Border color: #2563EB
- Shadow: 0 0 0 3px #EFF6FF
- Placeholder text remains visible until typing

**HOVER â Button (Secondary "Learn More")**
- Background: #EFF6FF
- Border: 2px solid #2563EB (stays)
- Text: #2563EB (stays)
- Slight lift: box-shadow 0 4px 12px rgba(37, 99, 235, 0.2)

**STICKY NAV â Scroll Behavior**
- Appears fixed at top on scroll-down
- Subtle shadow appears at 32px scroll: 0 2px 8px rgba(0, 0, 0, 0.08)
- Nav links remain same color/style
- Logo stays 32px height throughout

**CLICK â Testimonial Card**
- Optional: Card scales to 1.05x, shadow deepens
- If carousel: swipe left/right advances to next testimonial (touch gesture)
- Keyboard: Left/Right arrow keys advance on desktop

---

## IMAGES

**HERO SECTION (Right 50%)**
- URL: `https://images.unsplash.com/photo-1585771724684-38269d6639fd?w=1000&q=80`
- Description: Luxury white pillow on white bedding, serene, premium feel
- Alt text: "Premium white pillow on bed"
- Aspect ratio: full-height cover, no crop distortion

**BENEFITS SECTION â Card 1 Icon (Comfort)**
- URL: `https://images.unsplash.com/photo-1555539594-58d7cb561601?w=200&q=80`
- Description: Person sleeping peacefully on pillow
- Alt text: "Comfortable sleep icon"
- Size: 80x80px in blue circle background

**BENEFITS SECTION â Card 2 Icon (Durability)**
- URL: `https://images.unsplash.com/photo-1600821069394-acb48d80f4d5?w=200&q=80`
- Description: Close-up of high-quality fabric texture
- Alt text: "Durable material texture"
- Size: 80x80px in blue circle background

**BENEFITS SECTION â Card 3 Icon (Eco-Friendly)**
- URL: `https://images.unsplash.com/photo-1441974231531-c6227db76b6e?w=200&q=80`
- Description: Natural green leaves, organic materials
- Alt text: "Eco-friendly natural materials"
- Size: 80x80px in blue circle background

**PRODUCT GRID â Product Card 1 Image**
- URL: `https://images.unsplash.com/photo-1585771724684-38269d6639fd?w=400&q=80`
- Description: White pillow, premium, front view
- Alt text: "Classic White Pillow"

**PRODUCT GRID â Product Card 2 Image**
- URL: `https://images.unsplash.com/photo-1578500494198-246f612d03b3?w=400&q=80`
- Description: Memory foam pillow, contoured shape
- Alt text: "Memory Foam Pillow"

**PRODUCT GRID â Product Card 3 Image**
- URL: `https://images.unsplash.com/photo-1506439773649-6e0eb8cfb237?w=400&q=80`
- Description: Cooling gel pillow, modern design
- Alt text: "Cooling Gel Pillow"

**PRODUCT GRID â Product Card 4 Image**
- URL: `https://images.unsplash.com/photo-1541961017774-22349e4a1262?w=400&q=80`
- Description: Adjustable loft pillow, side view
- Alt text: "Adjustable Loft Pillow"

**TESTIMONIALS SECTION â Background (Optional)**
- URL: `https://images.unsplash.com/photo-1506439773649-6e0eb8cfb237?w=1200&q=80`
- Description: Soft, blurred pillow background
- Alt text: "Testimonials background"
- Applied as very subtle, low-opacity (8-12%) background behind text

**TRUST BADGES â Shipping Icon**
- URL: `https://images.unsplash.com/photo-1586528116039-c48148d8e644?w=200&q=80`
- Description: Package/shipping imagery
- Alt text: "Free Shipping"

**TRUST BADGES â Quality Icon**
- URL: `https://images.unsplash.com/photo-1454496522488-7a8e488e8606?w=200&q=80`
- Description: Checkmark, quality assurance
- Alt text: "100% Quality Guarantee"

---

## STYLE NOTES

**Typography:**
- Font family: System stack (âapple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif)
- Headings: 40â48px (h1), 32px (h2), 20px (h3), font-weight 600â700, line-height 1.2
- Body text: 16px, font-weight 400, line-height 1.6, #1F2937
- Small text/labels: 14px, font-weight 500, #6B7280, line-height 1.4

**Spacing (8px grid):**
- Section padding: 80px vertical (10 Ã 8px), 60px horizontal (7.5 Ã 8px)
- Card gaps: 24px (3 Ã 8px)
- Button padding: 12px horizontal (1.5 Ã 8px), 16px vertical (2 Ã 8px)
- Text padding in cards: 24px (3 Ã 8px)

**Visual Feel:**
- Premium, minimal, calming
- Lots of white space (breathing room)
- Soft shadows (0 2px 8px rgba(0, 0, 0, 0.08) for subtle depth)
- Smooth transitions: 200â300ms ease for interactive elements
- Border radius: 6â8px for modern, rounded look (not sharp corners)
- No heavy borders; use subtle 1px lines (#E5E7EB)

**Responsive Breakpoints:**
- Desktop: 1200px+ (4 cols, full nav)
- Tablet: 768pxâ1199px (2â3 cols, simplified nav)
- Mobile: <768px (1 col, hamburger nav, stacked sections)

**Micro-interactions:**
- Buttons: slight lift on hover, press animation on click
- Links: underline on hover, blue color, outline on focus
- Cards: shadow increase, scale 1.02 on hover
- Scroll triggers: testimonials/benefits fade in on scroll (optional parallax subtle effect)

**Accessibility Compliance (WCAG AA):**
- All text: 4.5:1 contrast minimum (#2563EB on white = 5.3:1 â)
- Buttons: 48px min height/width for touch targets
- Focus states: Visible 2px outline on all interactive elements
- Semantic HTML: `<button>`, `<nav>`, `<main>`, `<section>`, `<h1âh6>` used correctly
- ARIA labels: Form inputs have labels, icons have alt text or aria-label
- Keyboard nav: Tab through all buttons/links, Enter/Space to activate, no keyboard traps

---

**END OF DESIGN SPECIFICATION**

Developer: Use these exact hex colors, image URLs, dimensions, and interaction descriptions. No design decisions remainâimplement as specified.