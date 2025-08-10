import re
import time
from playwright.sync_api import Playwright, sync_playwright, expect, TimeoutError

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://gtm.whr.ai/login?utm_source=10times&utm_medium=web&utm_campaign=right_rail&hash=4IQjAPckGZDk9ArLj1D3pDYc8tvqFPX7ZsemflFWON0=&uid=1048476")
    time.sleep(5)
    page.get_by_role("button", name="Skip").click()
    page.get_by_role("button", name="Maturity").click()
    page.get_by_role("radio", name="New").click()
    page.get_by_role("button", name="Apply Filters").click()

    # Locator for the 'Maturity' badge text
    badge_locator = page.locator(
        "[id=\"radix-\\:r29\\:-content-table\"] > div > .flex-1 > .h-\\[calc\\(100vh-210px\\)\\] > .w-full > .\\[\\&_tr\\:last-child\\]\\:border-0 > tr > td:nth-child(9) > .badge_primary"
    ).first

    badge_text = badge_locator.inner_text().strip()

    # Check condition
    if badge_text.lower() == "new":
        print("✅ Test Passed: Badge text is 'New'")
    else:
        raise AssertionError(f"❌ Test Failed: Badge text is '{badge_text}' instead of 'New'")

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
