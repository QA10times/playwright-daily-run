import re
import time

from playwright.sync_api import Playwright, sync_playwright, expect, TimeoutError


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://gtm.whr.ai/login?utm_source=10times&utm_medium=web&utm_campaign=right_rail&hash=4IQjAPckGZDk9ArLj1D3pDYc8tvqFPX7ZsemflFWON0=&uid=1048476&platform=gtm")
    time.sleep(5)
    page.goto("https://gtm.whr.ai/internal/search/events")
    page.get_by_role("button", name="Skip").click()
    page.get_by_role("combobox", name="Search Events").click()
    page.get_by_role("combobox", name="Search Events").fill("      ")
    time.sleep(3)

    try:
        locator = page.get_by_text("No events found.")
        locator.click()
        print("PASS: 'No events found.' message displayed and clicked.")
    except TimeoutError:
        print("FAIL: 'No events found.' message not displayed.")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
