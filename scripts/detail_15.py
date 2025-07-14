import sys
import time

from playwright.sync_api import Playwright, sync_playwright, TimeoutError


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()

    print("✅ Navigating to event page")
    page.goto("https://geo.whr.ai/login?utm_source=10times&utm_medium=web&utm_campaign=right_rail&hash=4IQjAPckGZDk9ArLj1D3pDYc8tvqFPX7ZsemflFWON0=&uid=1048476")
    time.sleep(5)
    page.goto("https://geo.whr.ai/internal/event/4b00a3c7-26a1-5350-bc21-9abe9c97ee7a")
    page.wait_for_timeout(5000)  # Wait for full load

    try:
        print("✅ Waiting for Category header")
        category_header = page.locator("h1", has_text="Category")
        category_header.wait_for(state="visible", timeout=10000)
    except TimeoutError:
        print("❌ FAIL: Category header not found.")
        sys.exit(1)

    print("✅ Finding category list under header")
    category_ul = category_header.locator("xpath=following-sibling::ul[1]")

    category_items = category_ul.locator("li")
    count = category_items.count()
    print(f"✅ Found {count} <li> tags under category")

    if count == 2:
        print("\n🎉 TEST PASS: Exactly 2 category values found.")
    else:
        print(f"\n❌ TEST FAIL: Expected 2 categories but found {count}.")
        with open("category_fail_dump.html", "w", encoding="utf-8") as f:
            f.write(page.content())
        sys.exit(1)

    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
