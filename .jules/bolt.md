## 2024-05-22 - [LCP & CLS Optimization in Static Sites]
**Learning:** In static HTML sites without a build system, explicit `width` and `height` attributes on `<img>` tags are critical for preventing Cumulative Layout Shift (CLS), even if CSS overrides the dimensions. The browser needs the aspect ratio early. Also, `fetchpriority="high"` on LCP images (like logos above the fold) significantly improves LCP metric.
**Action:** Always verify `width`, `height`, and `fetchpriority` on critical above-the-fold images in static HTML files.
