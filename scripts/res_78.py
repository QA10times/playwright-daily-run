import re
import time
from playwright.sync_api import Playwright, sync_playwright, expect, TimeoutError

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://geo.whr.ai/login?utm_source=10times&utm_medium=web&utm_campaign=right_rail&hash=4IQjAPckGZDk9ArLj1D3pDYc8tvqFPX7ZsemflFWON0=&uid=1048476")
    time.sleep(5)
    page.goto("https://geo.whr.ai/internal/search/events")
    page.get_by_role("button", name="Skip").click()
    page.get_by_role("combobox").filter(has_text="Category").click()
    page.get_by_role("option", name="Select All").get_by_role("checkbox").click()
    page.get_by_role("button", name="Save").click()
    page.get_by_role("region", name="Notifications (F8)").get_by_role("button").click()


    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
