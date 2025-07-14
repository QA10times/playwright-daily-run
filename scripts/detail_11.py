import re
import time

from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://geo.whr.ai/login?utm_source=10times&utm_medium=web&utm_campaign=right_rail&hash=4IQjAPckGZDk9ArLj1D3pDYc8tvqFPX7ZsemflFWON0=&uid=1048476")
    time.sleep(5)

    page.goto("https://geo.whr.ai/internal/event/4b00a3c7-26a1-5350-bc21-9abe9c97ee7a")
    time.sleep(5)

    # Click all "Show <number> more" links
    links = page.get_by_role("link", name=re.compile(r"Show \d+ more"))
    count = links.count()
    print(f"Found {count} matching links")

    for i in range(count):
        links.nth(i).click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
