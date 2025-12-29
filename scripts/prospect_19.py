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
    page.get_by_role("button", name="Company Location").click()
    page.get_by_role("combobox", name="E.g. Bengaluru, Karnataka").click()
    page.get_by_role("combobox", name="E.g. Bengaluru, Karnataka").fill("united")
    page.get_by_role("option", name="United States Country").click()
    page.get_by_role("button", name="Company Location United States").click()
    page.get_by_role("button", name="Participation Role").click()
    page.get_by_role("checkbox", name="Exhibitor").click()
    page.get_by_role("button", name="Participation Role").click()
    page.get_by_role("button", name="Participation Frequency").click()
    page.get_by_role("checkbox", name="High", exact=True).click()
    page.get_by_role("checkbox", name="Very Low").click()
    page.get_by_role("checkbox", name="Medium").click()
    page.get_by_role("button", name="Participation Frequency").click()
    page.get_by_role("button", name="Activeness").click()
    page.get_by_role("checkbox", name="Dormant").click()
    page.get_by_role("button", name="Activeness").click()
    page.get_by_role("button", name="Event Type").click()
    page.get_by_role("checkbox", name="Tradeshows").click()
    page.get_by_role("button", name="Event Type").click()
    page.get_by_role("button", name="Followers", exact=True).click()
    page.get_by_role("checkbox", name="- 500").click()
    page.get_by_role("checkbox", name="1k - 5k").click()
    page.get_by_role("checkbox", name="10k - 25k").click()
    page.get_by_role("checkbox", name="50k - 100k").click()
    page.get_by_role("checkbox", name="200k+").click()
    page.get_by_role("button", name="Apply Filters").click()
    time.sleep(3)

    card = page.locator("a.block[href^='/internal/company/']").first
    card.wait_for(state="attached", timeout=60000)

    with page.expect_navigation(url=re.compile(r"/internal/company/")):
        card.evaluate("el => el.click()")
    time.sleep(3)
    page.get_by_role("button", name="medium").click()
    page.get_by_role("button", name="dormant").click()
    page.get_by_text("USA").click()
    label = page.get_by_text("Exhibited", exact=True).first
    card = label.locator("xpath=ancestor::div[contains(@class,'flex')]").first

    count = int(re.search(r"\d+", card.inner_text()).group())
    assert count > 0
    label.click()

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
