
from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Determine the absolute path to welcome.html
        cwd = os.getcwd()
        welcome_path = f"file://{cwd}/welcome.html"

        print(f"Navigating to {welcome_path}")
        page.goto(welcome_path)

        # Wait for the page to load
        page.wait_for_load_state("networkidle")

        # Verify the timer elements are visible (ID tgTimer)
        if page.is_visible("#tgTimer"):
            print("Timer is visible")
        else:
            print("Timer is NOT visible")

        # Take a screenshot
        page.screenshot(path="verification/welcome_page.png")
        print("Screenshot saved to verification/welcome_page.png")

        # Check for console logs (we expect none from our optimized functions)
        # Note: Playwright captures console messages via event listener, but we can just check if page runs without error.

        # Also check tempered-glass.html
        tg_path = f"file://{cwd}/tempered-glass.html"
        print(f"Navigating to {tg_path}")
        page.goto(tg_path)
        page.wait_for_load_state("networkidle")

        page.screenshot(path="verification/tempered_glass_page.png")
        print("Screenshot saved to verification/tempered_glass_page.png")

        browser.close()

if __name__ == "__main__":
    run()
