import re
import time

from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://geo.whr.ai/login?utm_source=10times&utm_medium=web&utm_campaign=right_rail&utm_term=whr_ed_default1&uid=71016155&hash=k2Y5Lb468h1wQSrYuImrOlqANi2SozsfBzEG2tuGK4Q=")
    time.sleep(5)
    page.goto("https://geo.whr.ai/internal/search/events")
    page.get_by_role("button", name="Skip").click()
    page.mouse.move(0, 500)
    page.get_by_role("link", name="Tracker").click()
    page.get_by_role("button", name="Skip").click()
    page.get_by_role("link", name="people template Location Tracker Keep a close eye on event activity within a").click()
    page.get_by_role("button", name="Skip").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
