import time
from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(
        headless=True,
        slow_mo=500
    )

    context = browser.new_context()
    page = context.new_page()

    page.goto(
        "https://gtm.whr.ai/login?utm_source=10times&utm_medium=web&utm_campaign=right_rail&hash=4IQjAPckGZDk9ArLj1D3pDYc8tvqFPX7ZsemflFWON0=&uid=1048476&platform=gtm"
    )

    time.sleep(5)

    page.goto("https://gtm.whr.ai/internal/search/events")

    page.get_by_role("button", name="Skip").click()

    page.get_by_role("tab", name="People").click()

    time.sleep(5)

    page.get_by_role("button", name="User Name").click()

    page.get_by_role("textbox", name="Search by Name").fill("abdul")

    page.get_by_role("button", name="Apply Filters").click()

    time.sleep(3)

    # Handle new tab properly
    # Profile page now opens in the SAME tab
    page.get_by_role("link", name="Abdul").first.click()
    page.wait_for_url("**/internal/user/**", timeout=60000)
    page1 = page

    page1.wait_for_load_state("domcontentloaded")

    page1.get_by_role("heading", name="Description").click()

    time.sleep(5)

    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)