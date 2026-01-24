from playwright.sync_api import sync_playwright
import os

def take_screenshot():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        filepath = os.path.abspath("index.html")
        page.goto(f"file://{filepath}")
        page.screenshot(path="verification/index_logo.png")
        print("Screenshot saved to verification/index_logo.png")
        browser.close()

if __name__ == "__main__":
    take_screenshot()
