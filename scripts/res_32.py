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

    page.get_by_role("button", name="Event Entry").click()
    page.get_by_role("checkbox", name="Free").click()
    page.get_by_role("checkbox", name="Paid").click()
    page.get_by_role("button", name="Apply Filters").click()
    time.sleep(5)
    page.get_by_role("link", name="Go to next page").click()


with sync_playwright() as playwright:
    run(playwright)
