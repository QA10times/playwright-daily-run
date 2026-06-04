import re
import time
from playwright.sync_api import Playwright, sync_playwright, TimeoutError


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(
        headless=True,
        slow_mo=500
    )

    context = browser.new_context()
    page = context.new_page()

    # Login page
    page.goto(
        "https://gtm.whr.ai/login?utm_source=10times&utm_medium=web&utm_campaign=right_rail&hash=4IQjAPckGZDk9ArLj1D3pDYc8tvqFPX7ZsemflFWON0=&uid=1048476&platform=gtm"
    )

    time.sleep(5)

    # Search page
    page.goto("https://gtm.whr.ai/internal/search/events")

    # Skip onboarding popup
    try:
        page.get_by_role("button", name="Skip").click(timeout=5000)
    except:
        pass

    # Companies tab
    page.get_by_role("tab", name="Companies").click()

    # ---------------- FILTERS ---------------- #

    page.get_by_role("button", name="Company Location").click()

    location_box = page.get_by_role(
        "combobox",
        name="E.g. Bengaluru, Karnataka"
    )

    location_box.click()
    location_box.fill("united")

    page.get_by_role(
        "option",
        name="United States Country"
    ).click()

    page.get_by_role(
        "button",
        name="Company Location United States"
    ).click()

    # Participation Role
    page.get_by_role("button", name="Participation Role").click()
    page.get_by_role("checkbox", name="Exhibit").click()
    page.get_by_role("button", name="Participation Role").click()

    # Participation Frequency
    page.get_by_role("button", name="Participation Frequency").click()

    page.get_by_role("checkbox", name="High", exact=True).click()
    page.get_by_role("checkbox", name="Very Low").click()
    page.get_by_role("checkbox", name="Medium").click()

    page.get_by_role("button", name="Participation Frequency").click()

    # Activeness
    page.get_by_role("button", name="Activeness").click()
    page.get_by_role("checkbox", name="Dormant").click()
    page.get_by_role("button", name="Activeness").click()

    # Event Type
    page.get_by_role("button", name="Event Type").click()
    page.get_by_role("checkbox", name="Tradeshows").click()
    page.get_by_role("button", name="Event Type").click()

    # Followers
    page.get_by_role("button", name="Followers", exact=True).click()

    page.get_by_role("checkbox", name="- 500").click()
    page.get_by_role("checkbox", name="1k - 5k").click()
    page.get_by_role("checkbox", name="10k - 25k").click()
    page.get_by_role("checkbox", name="50k - 100k").click()
    page.get_by_role("checkbox", name="200k+").click()

    # Apply filters
    page.get_by_role("button", name="Apply Filters").click()

    # ---------------- OPEN FIRST COMPANY CARD ---------------- #

    page.wait_for_selector(
        "a[href^='/internal/company/']:visible",
        timeout=60000
    )

    first_card = page.locator(
        "a[href^='/internal/company/']:visible"
    ).first

    with page.expect_popup() as popup_info:
        first_card.click()

    company_page = popup_info.value

    company_page.wait_for_load_state("domcontentloaded")

    # ---------------- COMPANY PAGE ACTIONS ---------------- #

    company_page.get_by_role("button", name="medium").click()
    company_page.get_by_role("button", name="dormant").click()

    company_page.get_by_text("USA").first.click()

    # ---------------- EXHIBIT CARD VALIDATION ---------------- #

    exhibit_card = company_page.locator(
        "div[class*='flex-col']"
    ).filter(
        has_text="Exhibit"
    ).first

    exhibit_card.wait_for(state="visible", timeout=30000)

    text = exhibit_card.inner_text()

    print(f"Card Text: {text}")

    match = re.search(r"\b\d+\b", text)

    if not match:
        raise Exception("No numeric count found in Exhibit card")

    count = int(match.group())

    print(f"Exhibit Count: {count}")

    assert count > 0, f"Exhibit count is {count}"

    # Click only if count > 0
    exhibit_card.click()

    print("Exhibit card clicked successfully")

    # ---------------- CLEANUP ---------------- #

    time.sleep(5)

    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)