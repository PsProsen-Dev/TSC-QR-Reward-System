## 2024-05-23 - Static HTML Image Attributes
**Learning:** This codebase consists of raw static HTML files with no build process. Browsers cannot infer image aspect ratios before the image loads, leading to Cumulative Layout Shift (CLS).
**Action:** All `<img>` tags must have explicit `width` and `height` attributes hardcoded to match the source image aspect ratio (even if resized by CSS) to reserve layout space immediately.

## 2024-05-23 - Manual Asset Optimization
**Learning:** Without a build pipeline, assets like `tsc-logo.jpg` can be significantly oversized (e.g., 261KB for a logo displayed at 90px). Python/Pillow scripts are effective for one-off optimizations in this environment.
**Action:** Audit and optimize static assets manually or via script, ensuring they meet `manifest.json` requirements (e.g., 512x512) while minimizing file size.
