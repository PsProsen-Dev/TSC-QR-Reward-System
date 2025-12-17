## 2024-05-23 - [Unoptimized Assets and CSS]
**Learning:** I found that `tsc-logo.jpg` is 256KB but displayed at only ~80px width. This is a massive waste of bandwidth. Also, the site uses massive inline CSS blocks in every HTML file, leading to redundant downloads.
**Action:** In future sessions (or if tools allowed), I should resize/compress images and extract common CSS to a shared file. For now, I used `preload` to at least prioritize the download.
