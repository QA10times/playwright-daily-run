import re
import time

from playwright.sync_api import Playwright, sync_playwright, expect, TimeoutError


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://geo.whr.ai/login?utm_source=10times&utm_medium=web&utm_campaign=right_rail&hash=4IQjAPckGZDk9ArLj1D3pDYc8tvqFPX7ZsemflFWON0=&uid=1048476")
    time.sleep(5)
    page.get_by_role("button", name="Skip").click()
    page.get_by_role("button", name="Event Format").click()
    page.get_by_role("checkbox", name="In Person").click()
    page.get_by_role("checkbox", name="Hybrid").click()
    page.get_by_role("button", name="Location").click()
    page.get_by_role("combobox", name="E.g. Bengaluru, Karnataka").click()
    page.get_by_role("combobox", name="E.g. Bengaluru, Karnataka").fill("india")
    time.sleep(2)
    page.get_by_role("option", name="India Country").locator("div").click()
    page.get_by_role("button", name="Dates").click()
    page.get_by_role("button", name="12 months").click()
    page.get_by_role("button", name="Apply Filters").click()
    time.sleep(3)
    page.get_by_role("tab", name="Table").click()
    time.sleep(5)
    page.get_by_role("tabpanel", name="Table").get_by_label("Go to next page").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
