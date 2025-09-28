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
    page.get_by_role("link", name="Tracker").click()
    time.sleep(3)
    page.get_by_role("button", name="Create").click()
    page.get_by_role("button", name="Skip").click()
    page.get_by_role("link", name="Product and Topics").click()
    page.get_by_role("button", name="Skip").click()
    page.get_by_role("textbox", name="Search by Collection name").click()
    page.get_by_role("textbox", name="Search by Collection name").fill("health forward")
    time.sleep(3)
    page.get_by_role("link", name="people template").click()
    page.get_by_role("tab", name="Exclude").first.click()
    page.get_by_role("textbox", name="Type Products/Topics to").click()
    page.get_by_role("textbox", name="Type Products/Topics to").fill("medicine")
    page.get_by_role("button", name="+").click()
    page.get_by_role("textbox", name="Enter Tracker Name").click()
    page.get_by_role("textbox", name="Enter Tracker Name").fill("test")
    page.get_by_role("button", name="Save").click()
    time.sleep(5)
    page.get_by_role("button", name="Skip").click()
    page.get_by_role("button", name="Upcoming Events").click()
    page.get_by_text("Table").click()
    time.sleep(3)
    page.get_by_label("Go to next page").click()
    time.sleep(3)

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
