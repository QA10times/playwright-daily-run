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
    page.mouse.move(0, 500)
    page.get_by_role("link", name="Coordinate").click()
    time.sleep(3)
    page.mouse.move(500, 0)
    page.get_by_role("button", name="Add", exact=True).click()
    page.get_by_role("button", name="Add Manually").click()
    page.get_by_text("Conference", exact=True).click()
    page.get_by_text("Warm").nth(1).click()
    page.get_by_role("textbox", name="Event Name").click()
    page.get_by_role("textbox", name="Event Name").fill("test")
    page.get_by_text("Add Event Location").click()
    page.get_by_role("combobox").click()
    page.get_by_placeholder("E.g. Bengaluru, Karnataka").fill("noi")
    time.sleep(3)
    page.get_by_text("Noir", exact=True).click()
    page.get_by_role("button", name="Save Event").click()
    time.sleep(5)
    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)