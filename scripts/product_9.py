import re
import time

from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()

    # Navigate and login
    page.goto("https://geo.whr.ai/login?utm_source=10times&utm_medium=web&utm_campaign=right_rail&hash=4IQjAPckGZDk9ArLj1D3pDYc8tvqFPX7ZsemflFWON0=&uid=1048476")
    time.sleep(5)
    page.goto("https://geo.whr.ai/internal/search/events")
    page.get_by_role("button", name="Skip").click()

    # Navigate to settings
    page.goto("https://geo.whr.ai/internal/settings/product")

    # Fill the input with spaces
    input_field = page.locator("input").first
    input_field.click()
    input_field.fill("                     ")  # spaces

    # Click save
    page.get_by_role("main").get_by_role("button").click()

    # Refresh the page to simulate reload and verify saved value
    page.reload()

    # Get the input again after refresh
    input_after = page.locator("input").first
    saved_value = input_after.input_value().strip()

    if saved_value:
        print("✅ Input is not empty after refresh:", repr(saved_value))
    else:
        print("❌ Input is empty or just spaces after refresh.")
        raise Exception("Validation failed: input field is blank after refresh.")

    # Clean up
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
