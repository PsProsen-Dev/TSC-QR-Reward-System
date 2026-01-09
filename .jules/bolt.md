## 2025-01-09 - Image Optimization & CLS Prevention
**Learning:** Optimizing the main logo image (`tsc-logo.jpg`) yielded significant performance gains.
- **Original:** 261KB (957x778px)
- **Optimized:** ~36KB (512x512px) - ~86% reduction.
- **Why 512px?** `manifest.json` requires a 512x512 icon. Resizing smaller would blur the PWA icon.
- **CLS Prevention:** Adding explicit `width` and `height` attributes to `<img>` tags prevents layout shifts, even if CSS also sets dimensions.
- **LCP Boost:** Using `<link rel="preload">` and `fetchpriority="high"` for the logo (which is often the LCP element on mobile) significantly improves perceived load time.
**Action:** Always check `manifest.json` before aggressively resizing images used as icons. Use `fetchpriority="high"` for above-the-fold hero images.
