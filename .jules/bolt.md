## 2024-05-23 - Image Optimization and CLS
**Learning:** Static sites without build steps require manual image optimization and explicit `width`/`height` attributes to prevent CLS.
**Action:** Always resize images to the largest required display size (e.g., manifest icon size) and compress them. Add explicit `width` and `height` attributes to `<img>` tags matching the source aspect ratio.
