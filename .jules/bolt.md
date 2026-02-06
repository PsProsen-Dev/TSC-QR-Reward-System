## 2024-05-23 - Static HTML Image Attributes
**Learning:** This codebase consists of raw static HTML files with no build process. Browsers cannot infer image aspect ratios before the image loads, leading to Cumulative Layout Shift (CLS).
**Action:** All `<img>` tags must have explicit `width` and `height` attributes hardcoded to match the source image aspect ratio (even if resized by CSS) to reserve layout space immediately.

## 2024-05-23 - Manual Image Optimization in Static Sites
**Learning:** In a static site without a build process, large images (like `tsc-logo.jpg` at 261KB) can be manually optimized. However, careful attention must be paid to aspect ratio (padding vs cropping) and file formats (fixing spoofed extensions like WebP in .png files).
**Action:** Use Python scripts with Pillow to resize, pad (if needed for aspect ratio), and compress images. Always verify visual results to ensure no destructive cropping occurred.
