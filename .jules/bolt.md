# Bolt's Performance Journal

## 2024-05-22 - CLS and Image Attributes
**Learning:** In a static HTML project without a build step, browsers cannot infer image dimensions before the image downloads. This causes massive Cumulative Layout Shift (CLS) as the page reflows.
**Action:** Always manually add explicit `width` and `height` attributes to `<img>` tags that match the source image aspect ratio. This reserves the layout space immediately.

## 2024-05-22 - Preconnect Resource Hints
**Learning:** The application heavily relies on third-party CDNs (Cloudflare for icons, Google Fonts) which were blocking rendering.
**Action:** Added `<link rel="preconnect">` and `dns-prefetch` for `fonts.googleapis.com`, `fonts.gstatic.com`, and `cdnjs.cloudflare.com`. This initiates the handshake early, reducing latency for critical assets.
