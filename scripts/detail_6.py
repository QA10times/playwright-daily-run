import re
import time

from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://gtm.whr.ai/login?utm_source=10times&utm_medium=web&utm_campaign=right_rail&hash=4IQjAPckGZDk9ArLj1D3pDYc8tvqFPX7ZsemflFWON0=&uid=1048476")
    time.sleep(5)
    page.goto("https://gtm.whr.ai/internal/event/a07b2635-2fd1-5038-ab1f-143a3eec4de4")
    page.get_by_role("button", name="Bookmark Event").click()
    page.get_by_role("radio", name="Bookmark").click()
    page.get_by_role("button", name="Submit").click()
    time.sleep(10)
    page.goto("https://gtm.whr.ai/internal/event/a07b2635-2fd1-5038-ab1f-143a3eec4de4")
    page.get_by_role("button", name="Bookmark Event").click()
    page.get_by_role("radio", name="Un-Bookmark").click()
    page.get_by_role("button", name="Submit").click()
    time.sleep(3)
    page.goto("https://gtm.whr.ai/internal/event/a07b2635-2fd1-5038-ab1f-143a3eec4de4")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
