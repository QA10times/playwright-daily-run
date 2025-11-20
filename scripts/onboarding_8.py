import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://gtm.whr.ai/signin")
    page.goto("https://gtm.whr.ai/login?utm_source=10times&utm_medium=web&utm_campaign=right_rail&hash=c+coFkahU0RlPoDkvRvieFxlDK5Oki9tmdNZlTXmM+w=&uid=69574238&platform=gtm")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)