## 2024-05-23 - Image CLS Optimization
**Learning:** Static sites without a build system often miss explicit image dimensions, leading to Cumulative Layout Shift (CLS) as images load.
**Action:** Always add explicit `width` and `height` attributes to `<img>` tags, matching the source image's aspect ratio (and ideally dimensions), to reserve layout space during loading.
