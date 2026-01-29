## 2024-05-23 - Static HTML Image Attributes
**Learning:** This codebase consists of raw static HTML files with no build process. Browsers cannot infer image aspect ratios before the image loads, leading to Cumulative Layout Shift (CLS).
**Action:** All `<img>` tags must have explicit `width` and `height` attributes hardcoded to match the source image aspect ratio (even if resized by CSS) to reserve layout space immediately.

## 2024-05-24 - Manual Image Optimization
**Learning:** In a static site without an image optimization pipeline, high-resolution source images (e.g., 900x900px) serve full bytes even when displayed as icons (48x48px).
**Action:** Manually resize and compress images to their largest required display dimension (e.g., 512x512 for manifest icons) to reduce payload size significantly.
