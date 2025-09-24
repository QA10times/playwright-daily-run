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
    page.mouse.move(0, 500)
    page.get_by_role("link", name="Tracker").click()
    time.sleep(3)
    page.get_by_role("button", name="Create").click()
    page.get_by_role("button", name="Skip").click()
    page.get_by_role("button", name="Create Custom").click()
    page.get_by_role("button", name="Location").click()
    page.get_by_role("combobox", name="E.g. Bengaluru, Karnataka").fill("india")
    page.get_by_role("option", name="India Country").locator("div").click()
    page.get_by_role("button", name="Location India").click()
    page.get_by_role("button", name="Dates").click()
    page.get_by_role("button", name="12 months").click()
    page.get_by_role("button", name="Dates").click()
    page.get_by_role("textbox", name="Enter Tracker Name").click()
    page.get_by_role("textbox", name="Enter Tracker Name").fill("test")
    page.get_by_role("button", name="Save").click()
    page.get_by_role("button", name="Skip").click()
    time.sleep(10)
    page.get_by_text("Table").click()
    page.locator("td button:has(svg.lucide-bookmark)").nth(3).click()
    page.get_by_role("radio", name="Bookmark").click()
    page.get_by_role("button", name="Submit").click()
    time.sleep(3)
    page.get_by_role("button", name="Bookmarked Events").click()
    page.get_by_role("cell").filter(has_text=re.compile(r"^$")).get_by_role("button").click()
    page.get_by_role("radio", name="Un-Bookmark").click()
    page.get_by_role("button", name="Submit").click()

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)