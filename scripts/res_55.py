import re
import time
from playwright.sync_api import Playwright, sync_playwright, expect, TimeoutError

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://geo.whr.ai/login?utm_source=10times&utm_medium=web&utm_campaign=right_rail&hash=4IQjAPckGZDk9ArLj1D3pDYc8tvqFPX7ZsemflFWON0=&uid=1048476")
    time.sleep(5)
    page.get_by_role("button", name="Skip").click()
    page.get_by_role("button", name="Dates").click()
    page.get_by_role("button", name="12 months").click()
    page.get_by_role("button", name="Dates").click()
    page.get_by_role("button", name="Location").click()
    page.get_by_role("combobox", name="E.g. Bengaluru, Karnataka").click()
    page.get_by_role("combobox", name="E.g. Bengaluru, Karnataka").fill("india")
    time.sleep(2)
    page.get_by_role("option", name="India Country").locator("div").click()
    page.get_by_role("button", name="Products/Topics").click()
    page.get_by_role("textbox", name="Type Products/Topics to").click()
    page.get_by_role("textbox", name="Type Products/Topics to").fill("ai")
    page.get_by_role("button", name="+", exact=True).click()
    page.get_by_role("textbox", name="Type Products/Topics to").click()
    page.get_by_role("textbox", name="Type Products/Topics to").fill("machine")
    page.get_by_role("button", name="+", exact=True).click()
    page.get_by_role("tab", name="Exclude").click()
    page.get_by_role("textbox", name="Type Products/Topics to").click()
    page.get_by_role("textbox", name="Type Products/Topics to").fill("car")
    page.get_by_role("button", name="+", exact=True).click()
    page.get_by_role("textbox", name="Type Products/Topics to").click()
    page.get_by_role("textbox", name="Type Products/Topics to").fill("tank")
    page.get_by_role("button", name="+", exact=True).click()
    page.get_by_role("button", name="Estimated Visitors").click()
    page.get_by_role("checkbox", name="Nano").click()
    page.get_by_role("checkbox", name="Small").click()
    page.get_by_role("checkbox", name="Large").click()
    page.get_by_role("checkbox", name="Ultra").click()
    page.get_by_role("button", name="Apply Filters").click()
    page.get_by_role("tab", name="Table").click()
    page.get_by_role("tabpanel", name="Table").get_by_label("Go to next page").click()

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)