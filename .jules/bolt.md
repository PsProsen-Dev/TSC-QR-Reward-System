## 2025-01-14 - Large LCP Image Asset
**Learning:** The primary logo `tsc-logo.jpg` was ~261KB (957x778) but displayed at max 100x100. This disproportionate size significantly impacted LCP.
**Action:** Always check asset dimensions against display dimensions. Resized to 512x416 (retaining PWA icon compatibility) to reduce size by 85%.
