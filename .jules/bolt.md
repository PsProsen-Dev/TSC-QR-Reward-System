## 2024-05-23 - [LCP Optimization via Image Attributes]
**Learning:** Adding explicit `width` and `height` attributes to images is crucial for preventing Cumulative Layout Shift (CLS) before CSS loads. `fetchpriority="high"` helps the browser prioritize the Largest Contentful Paint (LCP) element.
**Action:** Always check for missing image dimensions and priority hints on LCP elements in static sites.
