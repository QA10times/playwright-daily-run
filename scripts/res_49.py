import time
from playwright.sync_api import Playwright, sync_playwright, TimeoutError

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://geo.whr.ai/login?utm_source=10times&utm_medium=web&utm_campaign=right_rail&hash=4IQjAPckGZDk9ArLj1D3pDYc8tvqFPX7ZsemflFWON0=&uid=1048476")
    time.sleep(5)

    try:
        page.get_by_role("button", name="Skip").click(timeout=5000)
        page.get_by_role("button", name="Location").click()
        page.get_by_role("combobox", name="E.g. Bengaluru, Karnataka").click()
        page.get_by_role("combobox", name="E.g. Bengaluru, Karnataka").fill("india")
        time.sleep(2)
        page.get_by_role("option", name="India Country").locator("div").click()
        page.get_by_role("button", name="Frequency Show Frequency in").click(timeout=5000)
        page.get_by_role("checkbox", name="Weekly").click(timeout=5000)
        page.get_by_role("checkbox", name="Quarterly").click(timeout=5000)
        page.get_by_role("checkbox", name="Bi-Annual").click(timeout=5000)
        page.get_by_role("button", name="Apply Filters").click(timeout=5000)
        page.get_by_role("tab", name="Table").click()
        time.sleep(3)
        page.get_by_role("cell", name="Forecasted").click(timeout=5000)
        page.get_by_role("cell", name="Frequency").click(timeout=5000)

        print("✅ Test Passed: All elements found and actions performed successfully.")

    except TimeoutError as e:
        raise AssertionError(f"❌ Test Failed: Element not found or action failed - {e}")

    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)