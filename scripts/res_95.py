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
    page.get_by_role("button", name="Location").click()
    page.get_by_role("combobox", name="E.g. Bengaluru, Karnataka").fill("india")
    time.sleep(3)
    page.get_by_role("option", name="India Country").locator("div").click()
    page.get_by_role("button", name="Apply Filters").click()
    page.get_by_role("button", name="Apply Filters").click()
    time.sleep(5)
    page.get_by_role("tab", name="Map").click()
    time.sleep(3)
    page.get_by_role("button", name="Event List").click()
    page.get_by_label("Go to next page").click()
    time.sleep(3)
    page.get_by_role("button").filter(has_text=re.compile(r"^$")).nth(4).click()

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
