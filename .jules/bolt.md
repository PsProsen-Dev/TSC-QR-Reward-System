## 2024-05-23 - Static HTML Image Attributes
**Learning:** This codebase consists of raw static HTML files with no build process. Browsers cannot infer image aspect ratios before the image loads, leading to Cumulative Layout Shift (CLS).
**Action:** All `<img>` tags must have explicit `width` and `height` attributes hardcoded to match the source image aspect ratio (even if resized by CSS) to reserve layout space immediately.

## 2024-05-23 - Image Optimization for Static Sites
**Learning:** `tsc-logo.jpg` was 256KB and 957x778, but displayed as 512x512 (or smaller) and cropped by CSS. This wasted bandwidth and caused aspect ratio mismatch warnings.
**Action:** Resized image to 512x512 (square) and compressed it to ~50KB using Pillow. This matches `manifest.json` requirements and HTML attributes exactly, saving ~200KB per load.
