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
    page.get_by_role("combobox", name="Search Events").fill("magic")
    page.locator("#event-option-0").get_by_text("MAGIC LAS VEGAS").click()
    page.get_by_role("link", name="MAGIC LAS VEGAS").click()
    time.sleep(8)

    # Wait for the target section and validate
    try:
        magic_text = page.locator("#layout-main").get_by_role("complementary").get_by_text("MAGIC LAS VEGAS")
        magic_text.wait_for(timeout=5000)  # waits up to 5 seconds
        print("✅ MAGIC LAS VEGAS text found, proceeding with click")
        magic_text.click()
    except TimeoutError:
        print("❌ MAGIC LAS VEGAS text not found, skipping click and exiting early")
        context.close()
        browser.close()
        return  # exit early if not found

    page.get_by_role("button", name="Back").click()

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
