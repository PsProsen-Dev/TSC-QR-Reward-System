from playwright.sync_api import sync_playwright, expect

def verify_timer():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Load the file locally
        page.goto("file:////app/welcome.html")

        # Check if the page loaded
        print("Page loaded:", page.title())

        # Check if timer elements exist and are visible
        expect(page.locator("#tgTimerLabel")).to_be_visible()
        expect(page.locator("#tgDays")).to_be_visible()

        # Wait a bit to ensure timer updates
        page.wait_for_timeout(2000)

        # Get initial value
        days = page.locator("#tgDays").text_content()
        seconds = page.locator("#tgSeconds").text_content()
        print(f"Days: {days}, Seconds: {seconds}")

        # Take a screenshot
        page.screenshot(path="verification/timer_verification.png")
        print("Screenshot saved to verification/timer_verification.png")

        # Check console for errors (we should see our 'Timer initialized' log but no errors)
        page.on("console", lambda msg: print(f"Console log: {msg.text}"))

        browser.close()

if __name__ == "__main__":
    verify_timer()
