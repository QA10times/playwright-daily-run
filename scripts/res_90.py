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
    page.get_by_role("combobox", name="Search Events").click()
    page.get_by_role("combobox", name="Search Events").fill("The American Legion National Convention")
    page.locator("#event-option-0").get_by_text("The American Legion National").click()
    time.sleep(5)
    page.get_by_role("tab", name="Map").click()
    time.sleep(3)
    page.locator(".hidden > .flex-1 > .md\\:px-6").click()
    page.get_by_role("region", name="Map").click(position={"x":1,"y":289})
    page.get_by_role("button", name="Event List").click()

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
