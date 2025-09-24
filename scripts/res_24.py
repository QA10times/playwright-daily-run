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

    page.get_by_role("button", name="Dates").click()
    page.get_by_role("button", name="12 months").click()
    page.get_by_role("button", name="Dates").click()
    page.get_by_role("button", name="Apply Filters").click()
    time.sleep(5)
    page.get_by_role("button", name="Dates").click()
    page.get_by_role("gridcell", name="1", exact=True).first.click()
    page.get_by_role("gridcell", name="30").click()
    page.get_by_role("button", name="Dates").click()
    page.get_by_role("button", name="Apply Filters").click()
    time.sleep(5)
    page.get_by_role("tab", name="Table").click()
    time.sleep(5)
    page.get_by_role("tabpanel", name="Table").get_by_label("Go to next page").click()


with sync_playwright() as playwright:
    run(playwright)
