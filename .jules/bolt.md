## 2024-05-23 - Static HTML Image Attributes
**Learning:** This codebase consists of raw static HTML files with no build process. Browsers cannot infer image aspect ratios before the image loads, leading to Cumulative Layout Shift (CLS).
**Action:** All `<img>` tags must have explicit `width` and `height` attributes hardcoded to match the source image aspect ratio (even if resized by CSS) to reserve layout space immediately.
