import re
import time
from playwright.sync_api import Playwright, sync_playwright, expect, TimeoutError


def check_element(page, param):
    pass


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://gtm.whr.ai/login?utm_source=10times&utm_medium=web&utm_campaign=right_rail&hash=4IQjAPckGZDk9ArLj1D3pDYc8tvqFPX7ZsemflFWON0=&uid=1048476&platform=gtm")
    time.sleep(5)
    page.goto("https://gtm.whr.ai/internal/search/events")
    page.get_by_role("button", name="Skip").click()
    page.mouse.move(0, 500)
    page.get_by_role("link", name="Tracker", exact=True).click()
    time.sleep(3)
    page.get_by_role("button", name="Create").click()
    page.get_by_role("button", name="Skip").click()
    time.sleep(3)
    page.locator("#purposeTracker").get_by_role("link", name="New tracker").nth(1).click()
    page.get_by_role("button", name="Skip").click()
    page.get_by_role("textbox", name="Search By Event Name").click()
    page.get_by_role("textbox", name="Search By Event Name").fill("magic las vegas")
    page.get_by_text("MAGIC LAS VEGAS").first.click()
    page.get_by_role("switch", name="Show ratings").click()
    page.get_by_role("textbox", name="Enter Tracker Name").click()
    page.get_by_role("textbox", name="Enter Tracker Name").fill("test")
    page.get_by_role("button", name="Save").click()
    page.get_by_role("button", name="Skip").click()
    page.get_by_role("button", name="Upcoming Events").click()
    page.get_by_text("Table").click()
    time.sleep(5)
    check_element(page, "Rank")
    check_element(page, "Event Rating")
    check_element(page, "Trust")
    check_element(page, "Frequency")
    check_element(page, "Forecasted")
    check_element(page, "Audience Zone")
    page.get_by_role("link", name="Edit").click()
    time.sleep(3)
    page.get_by_role("button", name="Event Type").click()
    page.get_by_role("checkbox", name="Tradeshows").click()
    page.get_by_role("button", name="Save").click()
    page.get_by_role("button", name="Upcoming Events").click()
    time.sleep(3)
    page.get_by_text("Table").click()
    # Wait for the event table to fully load
    page.wait_for_selector("table tbody tr")

    # Scope to the first row only, then get the event name link
    # (excluding the "Tradeshow" type badge link that sits alongside it)
    first_row = page.locator("table tbody tr").first
    event_link = first_row.get_by_role("link").filter(has_not_text="Tradeshow").first

    name = event_link.inner_text()
    print("First event name:", name)

    with context.expect_page() as new_page_info:
        event_link.click()

    new_page = new_page_info.value
    new_page.wait_for_load_state()

    new_page.get_by_text("Overview").click()

    new_page.get_by_text("Tradeshows").first.click()

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)