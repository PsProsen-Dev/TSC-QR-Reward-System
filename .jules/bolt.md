## 2025-01-24 - LCP Optimization & CLS Prevention
**Learning:** Large images without explicit dimensions cause significant Cumulative Layout Shift (CLS) and slow down Largest Contentful Paint (LCP). Browsers cannot reserve space until the image header is downloaded unless `width` and `height` are specified.
**Action:** Always add `width` and `height` attributes to `<img>` tags, matching the aspect ratio. Use `fetchpriority="high"` for LCP images (above the fold). Compress images to appropriate dimensions (e.g., 512x512 for a logo displayed at 100x100 is better than 957x778, but still allows for high-DPI displays).

## 2025-01-24 - Playwright Verification & Client-Side Redirects
**Learning:** `tempered-glass.html` contained client-side JS that redirected to `tasks-new.html` based on the date (weekend check) and localStorage state. This caused Playwright `page.goto` to verify the *target* page (`tasks-new.html`) instead of the source page, leading to confusing debugging where `grep` showed changes but Playwright didn't.
**Action:** When verifying pages with potential redirects (auth, temporal gates), inspect `page.url` or use `page.add_init_script` to mock state (e.g., localStorage) to prevent redirects and verify the intended page.
