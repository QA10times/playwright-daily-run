import re
import time
from playwright.sync_api import Playwright, sync_playwright, expect, TimeoutError

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://gtm.whr.ai/login?utm_source=10times&utm_medium=web&utm_campaign=right_rail&hash=4IQjAPckGZDk9ArLj1D3pDYc8tvqFPX7ZsemflFWON0=&uid=1048476")
    time.sleep(5)
    page.get_by_role("button", name="Skip").click()
    page.get_by_role("combobox", name="Search Events").click()
    page.get_by_role("combobox", name="Search Events").fill("The American Legion National Convention")
    page.locator("#event-option-0").get_by_text("The American Legion National").click()
    time.sleep(5)
    page.get_by_role("tab", name="Map").click()
    time.sleep(3)
    page.get_by_role("region", name="Map").click(position={"x": 334, "y": 294})
    page.get_by_role("region", name="Map").click(position={"x": 2, "y": 291})
    page.get_by_role("button", name="Event List").click()
    page.get_by_text("1").nth(2).click()
    page.get_by_role("tabpanel", name="Map").get_by_role("button").nth(2).click()

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)