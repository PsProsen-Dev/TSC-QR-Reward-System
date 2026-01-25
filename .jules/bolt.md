## 2025-01-25 - Image Optimization and CLS Prevention
**Learning:** The main logo `tsc-logo.jpg` was significantly larger (957x778, ~260KB) than needed for its display size (80x80) and did not match the square aspect ratio expected by `manifest.json`. It also lacked explicit dimensions in HTML, contributing to CLS risk.
**Action:** Resized and center-cropped the image to 512x512 (~50KB) to match `manifest.json` requirements and significantly reduce file size. Added `width="512"`, `height="512"`, and `fetchpriority="high"` to `img` tags in critical files to prevent CLS and improve LCP.
