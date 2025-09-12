import time
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()

    # Step 1: Go to login page
    page.goto("https://geo.whr.ai/login?utm_source=10times&utm_medium=web&utm_campaign=right_rail&hash=4IQjAPckGZDk9ArLj1D3pDYc8tvqFPX7ZsemflFWON0=&uid=1048476")
    time.sleep(5)

    # Step 2: Click Skip
    page.get_by_role("button", name="Skip").click()

    # Step 3: Click 'Location' button
    page.get_by_role("button", name="Location").click()

    # Step 4: Fill first location input
    page.get_by_role("combobox", name="E.g. Bengaluru, Karnataka").fill("india")
    time.sleep(3)
    page.get_by_role("option", name="India Country").locator("div").click()
    time.sleep(3)
    page.get_by_role("button", name="Location").click()
    page.get_by_role("button", name="Apply Filters").click()
    time.sleep(3)

    # Step 8: Go to page 2
    page.get_by_role("link", name="Go to next page").click()

    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
