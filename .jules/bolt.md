## 2024-05-23 - Static HTML Image Attributes
**Learning:** This codebase consists of raw static HTML files with no build process. Browsers cannot infer image aspect ratios before the image loads, leading to Cumulative Layout Shift (CLS).
**Action:** All `<img>` tags must have explicit `width` and `height` attributes hardcoded to match the source image aspect ratio (even if resized by CSS) to reserve layout space immediately.

## 2024-05-24 - Manual Asset Optimization
**Learning:** The absence of an image optimization pipeline means raw assets are served directly to the client. We found 250KB+ images being used for 50px icons.
**Action:** Manually resize and compress images (using tools like Pillow) to their maximum display size (e.g., 512px for manifest icons) before committing. Don't rely on CSS to downscale large files.
