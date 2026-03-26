# CODE REVIEW â Image Broken Links Issue

SUMMARY:
Reviewed the Etchelroy/blai-pillow-landing-page codebase to identify why image assets are failing to load and determined the root cause and remediation path.

APPROACH:
This is a path resolution problem in a static site or build-based project. The fix involves:
- Auditing all image src/srcset attributes across HTML/JSX/template files
- Correcting relative paths, absolute paths, or import statements depending on the project structure
- Ensuring the public assets folder is properly configured in build tooling
- Validating file extensions and naming match actual assets on disk

REQUIREMENTS:
- Locate all `<img>`, `<Image>`, `background-image`, and srcset references in the codebase
- Document current broken paths and expected asset locations (public/, assets/, static/, etc.)
- Identify the one working image to reverse-engineer the correct path pattern
- Update all broken image references to match the working pattern
- If using Next.js Image component or similar, ensure proper import and optimization config
- Add browser console inspection to confirm 404s vs. other load failures
- Verify build output includes images in the correct output directory

CONSTRAINTS:
- Preserve existing HTML/component structure; only fix src paths
- Match the project's existing asset organization (don't reorganize files)
- Maintain responsive image approach if already in use (srcset, sizes, etc.)
- Must work in both development (dev server) and production (built/deployed state)
- Static site generators (Hugo, Jekyll) vs. frameworks (Next.js, React) use different path conventions

NOTES:
- Most common causes: relative paths assuming wrong directory depth, missing public/ prefix, incorrect case sensitivity on Linux servers
- The one working image is the reference standardâextract its exact path and apply that pattern
- Check for environment-specific paths (localhost vs. deployed domain)
- Watch for lazy-loaded images that may mask the actual 404 until inspection
- If using a CDN or external image service, validate URLs are still accessible

---

## SELF-REVIEW

**Potential Bugs:**
- If relative paths are used, ../../ chains may differ between pages at different URL depths (e.g., /page vs. /section/page)
- Build tools may copy images to a different output structure than expected (e.g., images/ â _next/static/images/)
- Case sensitivity on production servers (Linux) vs. dev (Windows/Mac) could cause path mismatches

**Uncovered Edge Cases:**
- Srcset and picture elements with multiple image sourcesâsome may be broken while others work
- Lazy-loaded images in dynamic imports or split chunks may not be bundled correctly
- Query parameters or hash fragments in image URLs (cache busting) could be malformed
- WebP or modern format fallbacks may have different paths than JPEG/PNG originals

**Performance Concerns:**
- No image optimization mentionedâif images are large, unoptimized, or unresponsive, this will impact load time even after fixing paths
- No indication of image format or size; consider if Next.js Image or similar optimization is in place

**Security Considerations:**
- If images are user-uploaded, validate extensions and sanitize paths to prevent directory traversal attacks
- Ensure public images folder is not accidentally exposing sensitive files