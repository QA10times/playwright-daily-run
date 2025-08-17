import sys
import time
from playwright.sync_api import Playwright, sync_playwright, Error


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()

    # Login page
    page.goto(
        "https://geo.whr.ai/login?utm_source=10times&utm_medium=web&utm_campaign=right_rail&hash=4IQjAPckGZDk9ArLj1D3pDYc8tvqFPX7ZsemflFWON0=&uid=1048476"
    )
    time.sleep(5)

    # Navigate to event page
    page.goto("https://geo.whr.ai/internal/event/a07b2635-2fd1-5038-ab1f-143a3eec4de4")

    try:
        with page.expect_popup() as popup_info:
            page.get_by_role("complementary").filter(has_text="BackConferencesGoldschmidt").get_by_role("link").click()
        popup = popup_info.value

        # Wait until popup is fully loaded
        popup.wait_for_load_state()

        print("✅ TEST PASS: Popup page opened successfully.")
    except Error as e:
        print(f"❌ TEST FAIL: Popup page did not open. Error: {e}")
        sys.exit(1)

    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)