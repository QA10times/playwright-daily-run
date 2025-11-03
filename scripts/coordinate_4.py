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
    page.mouse.move(0, 500)
    page.get_by_role("link", name="Coordinate").click()
    time.sleep(3)
    page.get_by_role("button", name="Type").click()
    page.get_by_role("checkbox", name="Cold").click()
    page.get_by_role("button", name="Status").click()
    page.get_by_role("checkbox", name="In Progress").click()
    page.get_by_role("button", name="Dates").click()
    page.get_by_role("button", name="12 months").click()
    page.get_by_role("button", name="Upvote", exact=True).click()
    page.get_by_role("checkbox", name="By me").click()
    page.get_by_role("checkbox", name="By others").click()
    time.sleep(3)
    page.get_by_role("tab", name="All Events").click()
    page.get_by_role("button", name="In Progress").first.click()

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
