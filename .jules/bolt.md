## 2025-12-18 - DOM Query Caching in Loops
**Learning:** Repeatedly querying the DOM with document.getElementById inside high-frequency loops (like setInterval) is a common performance anti-pattern in vanilla JS apps.
**Action:** Cache DOM elements outside the loop or lazily initialize them once to reduce layout thrashing and script execution time. Also, avoid console.log in production loops.
