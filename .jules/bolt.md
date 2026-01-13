## 2025-01-13 - [Image Optimization & LCP]
**Learning:** Resizing the main logo image (`tsc-logo.jpg`) from ~256KB to ~38KB was a significant win, but care was needed to ensure the new resolution (512x416) was still sufficient for the PWA icons defined in `manifest.json` (which requested 512x512).
**Action:** Always check `manifest.json` or other consumers of an image before destructively resizing it. Preserving aspect ratio is key, even if it doesn't match the exact square dimensions requested by the manifest.
