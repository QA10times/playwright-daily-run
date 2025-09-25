import re
import time
from playwright.sync_api import Playwright, sync_playwright, expect, TimeoutError

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://gtm.whr.ai/login?utm_source=10times&utm_medium=web&utm_campaign=right_rail&hash=4IQjAPckGZDk9ArLj1D3pDYc8tvqFPX7ZsemflFWON0=&uid=1048476")
    time.sleep(5)
    page.goto("https://gtm.whr.ai/internal/search/events")
    page.get_by_role("button", name="Skip").click()
    page.get_by_role("button", name="Audience Profile").click()
    page.get_by_role("option", name="Accountants").click()
    page.get_by_role("button", name="Audience Country").click()
    page.get_by_role("searchbox", name="Search").click()
    page.get_by_role("searchbox", name="Search").fill("india")
    page.get_by_label("Audience Country").get_by_text("India", exact=True).click()
    page.get_by_role("button", name="Apply Filters").click()
    page.get_by_role("tab", name="Table").click()
    page.get_by_role("cell", name="Audience Zone").locator("div").click()
    page.get_by_role("cell", name="Audience Country").locator("div").click()


    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)