## 2024-05-22 - [Optimizing JS Animations with WAAPI]
**Learning:** Replacing JavaScript-driven animations (style.transform + setTimeout) with the Web Animations API (element.animate) reduces Main Thread workload and avoids layout thrashing.
**Action:** When finding `setInterval` loops that manually manipulate DOM styles for animation, verify browser support and switch to WAAPI or CSS Keyframes. Ensure keyframe timing exactly matches the original JS timing to prevent visual regressions (e.g., Snap-to vs Transition).
