## 2025-01-12 - [Image Optimization & CLS Prevention]
**Learning:** Adding explicit `width` and `height` attributes to `<img>` tags is critical for preventing Cumulative Layout Shift (CLS), even if CSS defines the size. The browser reserves the space based on the HTML attributes before CSS is parsed.
**Action:** Always verify `img` tags have `width` and `height` attributes matching their displayed aspect ratio or CSS dimensions.

## 2025-01-12 - [Asset Size Optimization]
**Learning:** The project contained a 256KB logo image (`tsc-logo.jpg`) used at small sizes (80px-100px). Optimizing this to ~36KB (512px width) significantly reduces bandwidth without visible quality loss.
**Action:** Check asset sizes during exploration. Large assets used for small UI elements are prime targets for quick wins.
