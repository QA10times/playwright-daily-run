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
    page.get_by_role("tab", name="Companies").click()
    time.sleep(5)
    page.get_by_role("combobox", name="Search Events").click()
    page.get_by_role("combobox", name="Search Events").fill("magic las vegas")
    page.get_by_text("MAGIC LAS VEGAS").first.click()
    time.sleep(3)
    page.wait_for_selector(
        "a[href^='/internal/company/']:visible",
        timeout=60000
    )

    first_card = page.locator(
        "a[href^='/internal/company/']:visible"
    ).first

    with page.expect_popup() as popup_info:
        first_card.click()

    company_page = popup_info.value
    company_page.wait_for_load_state("domcontentloaded")
    time.sleep(3)
    company_page.get_by_role("tab", name="Upcoming").click()
    company_page.get_by_role("textbox", name="Search by Event name").click()
    company_page.get_by_role("textbox", name="Search by Event name").fill("magic las vegas")
    with company_page.expect_popup() as page1_info:
        company_page.get_by_role("link", name="MAGIC LAS VEGAS").click()
    page1 = page1_info.value
    page1.get_by_role("button", name="Contacts").click()

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)