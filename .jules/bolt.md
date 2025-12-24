## 2024-10-25 - [Unused CSS and CLS Opportunities]
**Learning:** Static HTML files often accumulate unused CSS references (like Font Awesome in `welcome.html`) which block rendering. Also, missing image dimensions on key assets like logos are a common source of CLS in this project, with specific dimensions varying by page context (80px vs 90px vs 100px).
**Action:** Always grep for class usage before assuming a stylesheet is needed. Always inspect computed styles or visual layout to determine correct image dimensions for CLS fixes.

## 2024-10-25 - [Headless Environment Font Limitations]
**Learning:** The verification environment lacks fonts for rendering emojis, causing false positives in visual regression testing.
**Action:** Ignore missing emojis in Playwright screenshots and rely on DOM attribute verification for those elements.
