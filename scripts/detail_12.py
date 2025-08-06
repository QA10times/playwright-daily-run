import sys
from playwright.sync_api import Playwright, sync_playwright, TimeoutError


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()

    print("✅ Opening Login Page")
    page.goto(
        "https://gtm.whr.ai/login?utm_source=10times&utm_medium=web&utm_campaign=right_rail&hash=4IQjAPckGZDk9ArLj1D3pDYc8tvqFPX7ZsemflFWON0=&uid=1048476"
    )
    page.wait_for_timeout(5000)

    print("✅ Navigating to Event Page")
    page.goto("https://gtm.whr.ai/internal/event/a07b2635-2fd1-5038-ab1f-143a3eec4de4")
    page.wait_for_timeout(3000)

    print("✅ Clicking 'Event POC'")
    page.get_by_role("button", name="Event POC").click()

    print("✅ Clicking 'Show details'")
    page.get_by_role("button", name="Show details").first.click()

    print("✅ Clicking Email link")
    page.get_by_text("gsoffice@geochemsoc.org").first.click()

    print("✅ Clicking 'Read More'")
    page.get_by_text("Read More").click()

    print("✅ Clicking 'Show Less'")
    page.get_by_text("Show Less").click()

    # --------✅ Validation step after clicks --------

    # Define expected content you want to confirm is present after clicks
    # Example: text that should appear after Read More expands (replace with your actual expected content)
    EXPECTED_TEXT = "The Goldschmidt Conference is"

    print(f"\n✅ Verifying if expected text '{EXPECTED_TEXT}' is present on page...")
    try:
        page.get_by_text(EXPECTED_TEXT).wait_for(state="visible", timeout=5000)
        print("\n🎉 TEST PASS: Expected data found on page.")
    except TimeoutError:
        print("\n❌ TEST FAIL: Expected data not found after interactions!")
        # Optionally dump page HTML for debugging
        with open("page_dump.html", "w", encoding="utf-8") as f:
            f.write(page.content())
        sys.exit(1)

    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
