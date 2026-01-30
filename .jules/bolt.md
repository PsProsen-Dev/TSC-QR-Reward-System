## 2024-05-23 - Static HTML Image Attributes
**Learning:** This codebase consists of raw static HTML files with no build process. Browsers cannot infer image aspect ratios before the image loads, leading to Cumulative Layout Shift (CLS).
**Action:** All `<img>` tags must have explicit `width` and `height` attributes hardcoded to match the source image aspect ratio (even if resized by CSS) to reserve layout space immediately.

## 2024-05-30 - Manual Image Optimization
**Learning:** Without an image build pipeline, high-resolution source images (e.g., 900x900px PNGs) were being served directly to mobile devices where they were displayed much smaller (e.g., 48x48px). This caused significant unnecessary payload overhead.
**Action:** Manually resize and compress images to their largest required display dimension (e.g., 512x512 for manifest icons) to minimize payload size while maintaining quality.
