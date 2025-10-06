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
    time.sleep(3)
    page.get_by_role("link", name="Event Participation").click()
    page.get_by_role("button", name="Skip").click()
    page.get_by_role("textbox", name="Search By Event Name").click()
    page.get_by_role("textbox", name="Search By Event Name").fill("magic")
    page.get_by_text("MAGIC LAS VEGAS").click()
    page.get_by_role("switch", name="Show ratings").click()
    page.get_by_role("switch", name="Enable/Disable all advanced").click()
    page.get_by_role("textbox", name="Enter Tracker Name").click()
    page.get_by_role("textbox", name="Enter Tracker Name").fill("test")
    page.get_by_role("button", name="Save").click()
    page.get_by_role("button", name="Skip").click()
    page.get_by_role("button", name="Upcoming Events").click()
    page.get_by_text("Table").click()
    time.sleep(5)
    page.get_by_text("Rank").click()
    page.get_by_text("Event Rating").click()
    page.get_by_text("Trust").click()
    page.get_by_text("Frequency").click()
    page.get_by_text("Forecasted").click()
    page.get_by_text("Audience Zone").click()
    page.get_by_role("link", name="Configurations").click()
    time.sleep(3)
    page.get_by_role("button", name="Event Type").click()
    page.get_by_role("checkbox", name="Tradeshows").click()
    page.get_by_role("button", name="Save").click()
    page.get_by_role("button", name="Upcoming Events").click()
    time.sleep(3)
    page.get_by_text("Table").click()
    # Wait for the event table to fully load
    page.wait_for_selector(".truncate.font-medium a")

    # Get the first event link directly
    event_link = page.locator(".truncate.font-medium a").first

    name = event_link.inner_text()
    print("First event name:", name)

    event_link.click()
    time.sleep(5)

    page.get_by_text("Tradeshows").click()

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)