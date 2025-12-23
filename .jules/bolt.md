## 2024-05-22 - [Optimized Critical Rendering Path]
**Learning:** `welcome.html` was loading the entire Font Awesome library (approx 70KB) but not using any of its icons.
**Action:** Removed the unused `<link>` tag. Always audit external dependencies to ensure they are actually used.
