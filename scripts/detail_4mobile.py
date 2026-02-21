import sys
import time
import re
from playwright.sync_api import Playwright, sync_playwright, Error


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True, slow_mo=500)
    device = playwright.devices["iPhone 13"]
    context = browser.new_context(**device)
    page = context.new_page()

    # Login page
    page.goto(
        "https://gtm.whr.ai/login?utm_source=10times&utm_medium=web&utm_campaign=right_rail&hash=4IQjAPckGZDk9ArLj1D3pDYc8tvqFPX7ZsemflFWON0=&uid=1048476"
    )
    time.sleep(5)

    # Navigate to event page
    page.goto("https://gtm.whr.ai/internal/event/6047ff7c-8bb5-5754-b59f-28530c617057")

    try:
        with page.expect_popup() as popup_info:
            page.locator("#layout-main").get_by_role("link").filter(
                has_text=re.compile(r"^$")
            ).click()

        popup = popup_info.value
        popup.wait_for_load_state()
        print("✅ TEST PASS: Popup page opened successfully.")

    except Error as e:
        print(f"❌ TEST FAIL: Popup page did not open. Error: {e}")

    finally:
        context.close()
        browser.close()


with sync_playwright() as playwright:
    run(playwright)
