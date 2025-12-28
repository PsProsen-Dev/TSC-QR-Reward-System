# Bolt's Journal
This journal tracks critical performance learnings for the project.

## 2023-10-26 - [DOM Access Optimization]
**Learning:** Frequent DOM querying in `setInterval` loops (every 1 second) causes unnecessary overhead.
**Action:** Cache DOM elements in variables outside the loop to improve performance and reduce layout thrashing risks.
