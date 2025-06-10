import re
import time
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://gtm.whr.ai/login?utm_source=10times&utm_medium=web&utm_campaign=right_rail&hash=4IQjAPckGZDk9ArLj1D3pDYc8tvqFPX7ZsemflFWON0=&uid=1048476")
    time.sleep(5)

    # Click Skip if available
    try:
        page.get_by_role("button", name="Skip").click(timeout=3000)
    except:
        print("Skip button not found or already skipped")

    # Navigate to settings page
    page.goto("https://gtm.whr.ai/internal/settings/product")

    # Locate the input field and update value
    input_field = page.locator("div:nth-child(4) > div:nth-child(2) > .p-2").first
    input_field.click()
    input_field.fill("")  # Clear existing text
    input_field.click()
    input_field.fill("test")

    # Click Save
    page.get_by_role("main").get_by_role("button").click()

    # Optional: Wait for toast/success message if known
    # page.wait_for_selector("text=Saved successfully", timeout=5000)

    time.sleep(2)  # Wait for value to persist (if needed)

    # Validate that the value is actually saved
    page.reload()
    input_field_after = page.locator("div:nth-child(4) > div:nth-child(2) > .p-2").first
    actual_value = input_field_after.input_value()

    if actual_value == "test":
        print("✅ Test value saved successfully.")
    else:
        print("❌ Failed to save 'test' value. Found:", actual_value)
        raise Exception("Validation failed: test value not saved.")

    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
