import re
from playwright.sync_api import Playwright, sync_playwright, expect

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True, slow_mo=200)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://gtm.whr.ai/signin")
    page.get_by_role("link", name="Sign up").click()
    page.get_by_role("tab", name="Location Insights").click()

    # Wait for the navigation to finish
    page.wait_for_load_state("load")

    # Check the final URL
    expected_url = "https://geo.whr.ai/signup"
    assert page.url == expected_url, f"Unexpected URL: {page.url}"

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
