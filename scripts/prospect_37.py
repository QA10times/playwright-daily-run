import re
import time
from playwright.sync_api import Playwright, sync_playwright, expect, TimeoutError

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://geo.whr.ai/login?utm_source=10times&utm_medium=web&utm_campaign=right_rail&hash=4IQjAPckGZDk9ArLj1D3pDYc8tvqFPX7ZsemflFWON0=&uid=1048476&platform=geo")
    time.sleep(5)
    page.goto("https://geo.whr.ai/internal/search/events")
    page.get_by_role("button", name="Skip").click()
    page.get_by_role("tab", name="People").click()
    time.sleep(5)
    page.get_by_role("button", name="User Name").click()
    page.get_by_role("textbox", name="Search by Name").click()
    page.get_by_role("textbox", name="Search by Name").fill("abdul")
    page.get_by_role("button", name="Apply Filters").click()
    time.sleep(3)
    page.get_by_role("link", name="Abdul").first.click()
    time.sleep(3)
    page.get_by_role("heading", name="Description").click()

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
