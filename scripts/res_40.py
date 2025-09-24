import time
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()

    # Step 1: Go to login page
    page.goto("https://gtm.whr.ai/login?utm_source=10times&utm_medium=web&utm_campaign=right_rail&hash=4IQjAPckGZDk9ArLj1D3pDYc8tvqFPX7ZsemflFWON0=&uid=1048476")
    time.sleep(5)

    # Step 2: Click Skip
    page.get_by_role("button", name="Skip").click()

    page.get_by_role("switch", name="Show ratings").click()
    page.get_by_role("button", name="User Rating Show ratings").click()
    page.get_by_role("checkbox", name="-1").click()
    page.get_by_role("checkbox", name="-4").click()
    page.get_by_role("button", name="Apply Filters").click()
    time.sleep(5)
    page.get_by_role("tab", name="Table").click()
    time.sleep(3)
    page.get_by_role("cell", name="Event Rating").locator("div").click()
    time.sleep(3)
    cell = page.locator("td:has(div.grid-cols-3)").first
    value_text = cell.inner_text().strip()

    try:
        value = float(value_text)
        if (0.0 <= value <= 1.0) or (3.0 <= value <= 4.0):
            print(f"✅ Value {value} is within the accepted range.")
        else:
            raise AssertionError(f"❌ Value {value} is outside the allowed range.")
    except ValueError:
        raise AssertionError(f"❌ Could not convert '{value_text}' to float.")
    page.get_by_role("tabpanel", name="Table").get_by_label("Go to next page").click()


with sync_playwright() as playwright:
    run(playwright)
