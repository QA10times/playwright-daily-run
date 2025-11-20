import sys
import time

from playwright.sync_api import Playwright, sync_playwright, TimeoutError


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()

    print("✅ Navigating to login page")
    page.goto("https://gtm.whr.ai/login?utm_source=10times&utm_medium=web&utm_campaign=right_rail&hash=4IQjAPckGZDk9ArLj1D3pDYc8tvqFPX7ZsemflFWON0=&uid=1048476&platform=gtm")
    time.sleep(5)

    print("✅ Navigating to event page")
    page.goto("https://gtm.whr.ai/internal/event/4b00a3c7-26a1-5350-bc21-9abe9c97ee7a")
    time.sleep(5)

    print("✅ Waiting for 'Search Events' button to appear")
    search_button = page.get_by_role("button", name="Search Events")
    search_button.wait_for(state="visible", timeout=10000)

    print("✅ Clicking 'Search Events' and waiting for navigation")
    try:
        with page.expect_navigation(timeout=10000):
            search_button.click()
        print("\n🎉 TEST PASS: Navigation detected after clicking 'Search Events'.")
    except TimeoutError:
        print("\n❌ TEST FAIL: No navigation happened after clicking 'Search Events'.")
        # Optionally dump page for debugging
        with open("no_navigation_dump.html", "w", encoding="utf-8") as f:
            f.write(page.content())
        sys.exit(1)

    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
