## 2024-05-23 - [LCP and CLS Optimization for Static Assets]
**Learning:** For static sites without a build system, manually adding `width` and `height` attributes to images is critical for preventing Cumulative Layout Shift (CLS). Additionally, preloading the Largest Contentful Paint (LCP) image using `<link rel="preload">` and `fetchpriority="high"` significantly improves perceived load performance.
**Action:** Always check `<img>` tags for missing dimension attributes and LCP candidates for preload opportunities in static HTML files.
