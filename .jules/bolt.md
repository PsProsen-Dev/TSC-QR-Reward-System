## 2025-01-18 - [Logo & LCP Optimization]
**Learning:** Optimizing the main brand asset (logo) and its delivery yielded significant gains.
- **Image Size:** Resizing `tsc-logo.jpg` from 957x778 to 512x512 (matching manifest requirements) and optimizing compression reduced file size by ~80% (256KB -> 49KB).
- **LCP:** Preloading the logo and using `fetchpriority="high"` ensures the LCP element loads as fast as possible.
- **CLS:** Explicit `width` and `height` attributes (even with CSS) help the browser reserve space during the initial paint, reducing layout shifts.
- **PWA:** Linking the existing `manifest.json` enables PWA installation, which was previously dormant.

**Action:** Always check for unlinked `manifest.json` files and oversized LCP images in static sites.
