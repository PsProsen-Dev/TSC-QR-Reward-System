## 2024-05-23 - Static HTML Image Attributes
**Learning:** This codebase consists of raw static HTML files with no build process. Browsers cannot infer image aspect ratios before the image loads, leading to Cumulative Layout Shift (CLS).
**Action:** All `<img>` tags must have explicit `width` and `height` attributes hardcoded to match the source image aspect ratio (even if resized by CSS) to reserve layout space immediately.

## 2024-05-24 - Static Asset Optimization
**Learning:** Static sites without a build pipeline often accumulate unoptimized assets (e.g., raw camera uploads, mismatched formats). `mobile-stand.png` was actually a WebP file, and `tsc-logo.jpg` was 256KB for a 80px display.
**Action:** Manually resize and optimize images to their largest display dimension (e.g., 512px for manifest icons, 128px for thumbnails) using Python/Pillow scripts. Check file signatures, not just extensions.
