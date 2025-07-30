import re
from playwright.sync_api import Playwright, sync_playwright, expect
import time


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://gtm.whr.ai/signin")
    page.goto("https://gtm.whr.ai/login?utm_source=10times&utm_medium=web&utm_campaign=right_rail&hash=4IQjAPckGZDk9ArLj1D3pDYc8tvqFPX7ZsemflFWON0=&uid=1048476")
    time.sleep(5)
    page.goto("https://gtm.whr.ai/internal/search/events?view=table")
    page.goto("https://gtm.whr.ai/internal/search/events?view=table&status=active%2Ccancelled%2Cpostponed&active_gte=2025-01-01&active_lte=2025-01-31&locationIds=5dc0b154-e2d8-5160-9bd6-dd8175a58c47&ratings=0-1%2C2-3&show=branded%2Cseries%2Cforecasted%2Crating%2CestimatedExhibitors%2CtrustScore%2CaudienceSpread%2CaudienceZone%2CeconomicImpact%2Crankings%2Cscores%2Cmaturity%2Cfrequency%2Calerts")
    page.mouse.move(0, 500)
    page.get_by_role("link", name="Dashboard").click()
    page.mouse.move(500, 0)
    time.sleep(5)
    page.get_by_placeholder("Search Events").click()
    page.get_by_placeholder("Search Events").fill("magic las vegas")
    page.get_by_text("MAGIC LAS VEGAS", exact=True).click()
    page.mouse.move(0, 500)
    page.get_by_role("link", name="Dashboard").click()
    page.mouse.move(500, 0)
    page.wait_for_timeout(5)
    page.get_by_role("combobox").filter(has_text="Event Type").click()
    page.get_by_label("Tradeshows").click()
    page.get_by_role("button", name="Location").click()
    page.get_by_role("combobox", name="E.g. Bengaluru, Karnataka").fill("india")
    page.get_by_role("option", name="India", exact=True).click()
    page.get_by_role("button", name="Dates").click()
    page.get_by_role("button", name="12 months").click()
    page.get_by_role("button", name="Dates 1 Jul, 2025 - 30 Jun,").click()
    page.get_by_role("button", name="Explore Events").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
