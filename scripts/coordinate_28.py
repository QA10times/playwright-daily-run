import re
import time
from playwright.sync_api import Playwright, sync_playwright, expect, TimeoutError

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://gtm.whr.ai/login?utm_source=10times&utm_medium=web&utm_campaign=right_rail&hash=4IQjAPckGZDk9ArLj1D3pDYc8tvqFPX7ZsemflFWON0=&uid=1048476&platform=gtm")
    time.sleep(5)
    page.goto("https://gtm.whr.ai/internal/search/events")
    page.get_by_role("button", name="Skip").click()
    page.mouse.move(0, 500)
    page.get_by_role("link", name="Coordinate").click()
    time.sleep(3)
    page.get_by_role("textbox", name="Search Events").click()
<<<<<<< HEAD
    page.get_by_label(", exact=True).fill("indian han")
=======
    page.get_by_label("", exact=True).fill("indian han")
>>>>>>> 2b388f830d6de749f4bc183a576a27ba734f9e39
    time.sleep(3)
    page.get_by_text("Indian Handicrafts & Gifts").click()
    time.sleep(3)
    page.get_by_role("heading", name="Indian Handicrafts & Gifts").click()
    page.get_by_role("textbox", name="Take a note").click()
    page.get_by_role("textbox", name="Take a note").fill("test")
    page.get_by_role("button", name="Send send").click()
    page.locator("#layout-main header").get_by_role("button").filter(has_text=re.compile(r"^$")).first.click()
    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
