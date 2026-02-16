import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True, slow_mo=500)
    device = playwright.devices["iPhone 13"]
    context = browser.new_context(**device)
    page = context.new_page()
    page.goto("https://geo.whr.ai/signin")
    page.get_by_placeholder("Email").click()
    page.get_by_placeholder("Email").fill("")
    page.get_by_role("button", name="Sign In").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)