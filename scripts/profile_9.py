import time
from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()

    # Go to login page
    page.goto("https://gtm.whr.ai/login?utm_source=10times&utm_medium=web&utm_campaign=right_rail&hash=4IQjAPckGZDk9ArLj1D3pDYc8tvqFPX7ZsemflFWON0=&uid=1048476&platform=gtm")
    time.sleep(5)

    # Go to profile page
    page.goto("https://gtm.whr.ai/internal/settings/profile")

    # Locate the email textbox
    email_input = page.get_by_role("textbox", name="Email")
    email_input.click()

    # Attempt to fill the email field
    test_email = "dfdf@hdhf.com"
    email_input.fill(test_email)

    # Get the value after attempting to fill
    actual_value = email_input.input_value()

    # Compare the value to determine if it was filled
    if actual_value == test_email:
        raise Exception("❌ Email field is editable. Test failed.")
    else:
        print("✅ Email field is locked (value did not change). Test passed.")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
