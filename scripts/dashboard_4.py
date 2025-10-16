import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://whr.ai/demo")
    page.locator("input[name=\"firstName\"]").fill("test")
    page.locator("input[name=\"lastName\"]").fill("test")
    page.locator("input[name=\"busEmail\"]").fill("test@test4.com")
    page.locator("input[name=\"companyName\"]").fill("10times")
    page.locator("input[name=\"jobTitle\"]").fill("qa")
    phone_input = page.locator("input[name='phoneNumber']")
    phone_input.click()
    phone_input.type("8702522256")

    # Dismiss any popup/dialog
    page.once("dialog", lambda dialog: dialog.dismiss())

    # ---- ✅ Wait for API after clicking Submit ----
    with page.expect_response("https://whr.ai/demo") as resp_info:
        page.get_by_role("button", name="Submit").click()

    response = resp_info.value
    status_code = response.status

    if status_code == 200:
        print("✅ API returned 200 - Test Passed")
    else:
        raise AssertionError(f"❌ API returned {status_code}, expected 200")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
