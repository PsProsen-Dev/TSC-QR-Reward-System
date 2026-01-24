from playwright.sync_api import sync_playwright
import sys
import os

def verify_logo_optimization():
    files_to_check = [
        "index.html",
        "welcome.html",
        "tempered-glass.html",
        "reward.html",
        "tasks-new.html"
    ]

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()

        overall_passed = True

        for filename in files_to_check:
            page = context.new_page()
            filepath = os.path.abspath(filename)
            file_passed = True

            if filename == "tempered-glass.html":
                page.add_init_script("localStorage.setItem('tsc_completed_tasks', 'true');")

            print(f"Checking {filename}...")
            try:
                page.goto(f"file://{filepath}")

                # Check for either .logo or .header-logo
                logo = page.locator(".logo, .header-logo").first

                if logo.count() == 0:
                    print(f"Error in {filename}: No logo found via selector '.logo, .header-logo'")
                    file_passed = False
                    overall_passed = False
                    continue

                src = logo.get_attribute("src")
                if not src or "tsc-logo.jpg" not in src:
                    print(f"Error in {filename}: Invalid src {src}")
                    file_passed = False
                else:
                    print(f"Found logo in {filename}: src={src}")

                width = logo.get_attribute("width")
                height = logo.get_attribute("height")
                fetchpriority = logo.get_attribute("fetchpriority")

                if width != "512":
                    print(f"Error in {filename}: Missing or incorrect width attribute (expected '512', got '{width}')")
                    file_passed = False

                if height != "512":
                    print(f"Error in {filename}: Missing or incorrect height attribute (expected '512', got '{height}')")
                    file_passed = False

                if fetchpriority != "high":
                    print(f"Error in {filename}: Missing or incorrect fetchpriority attribute (expected 'high', got '{fetchpriority}')")
                    file_passed = False

                if not file_passed:
                     print(f"Outer HTML: {logo.evaluate('el => el.outerHTML')}")
                     overall_passed = False

            except Exception as e:
                print(f"Exception checking {filename}: {e}")
                overall_passed = False

            page.close()

        browser.close()

        if overall_passed:
            print("\n✅ Verification PASSED: All logo images have correct attributes.")
            sys.exit(0)
        else:
            print("\n❌ Verification FAILED: Some logo images are missing attributes.")
            sys.exit(1)

if __name__ == "__main__":
    verify_logo_optimization()
