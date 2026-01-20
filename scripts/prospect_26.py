import re
import time
from playwright.sync_api import Playwright, sync_playwright, expect, TimeoutError

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://gtm.whr.ai/login?utm_source=10times&utm_medium=web&utm_campaign=right_rail&hash=4IQjAPckGZDk9ArLj1D3pDYc8tvqFPX7ZsemflFWON0=&uid=1048476&platform=gtm")
    time.sleep(5)
    page.goto("https://gtm.whr.ai/internal/search/events")
    page.get_by_role("button", name="Skip").click()
    page.get_by_role("tab", name="Companies").click()
    time.sleep(5)
    page.get_by_role("combobox", name="Search Events").click()
    page.get_by_role("combobox", name="Search Events").fill("magic")
    page.get_by_text("MAGIC LAS VEGAS").click()
    time.sleep(3)
    card = page.locator("a.block[href^='/internal/company/']").first
    card.wait_for(state="attached", timeout=60000)

    with page.expect_navigation(url=re.compile(r"/internal/company/")):
        card.evaluate("el => el.click()")
    time.sleep(3)
    with page.expect_popup() as page1_info:
        page.get_by_role("link", name="MAGIC LAS VEGAS").click()
    page1 = page1_info.value
    page1.goto("https://gtm.whr.ai/internal/event/4b00a3c7-26a1-5350-bc21-9abe9c97ee7a")
    page1.get_by_text("MAGIC LAS VEGAS", exact=True).first.click()

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
