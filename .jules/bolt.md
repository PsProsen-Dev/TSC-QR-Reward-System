## 2024-01-23 - Static Asset Optimization
**Learning:** In static HTML projects without a build system, raw assets like images can be significantly unoptimized (e.g., 957x778px image used for 80x80px display).
**Action:** Always verify asset dimensions and file size. Use Python scripts with Pillow to resize and optimize images to match usage requirements (e.g., 512x512 for manifest) and reduce LCP.
