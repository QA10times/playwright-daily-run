import re
from playwright.sync_api import Playwright, sync_playwright, expect
import time


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True, slow_mo=1000)
    device = playwright.devices["iPhone 13"]
    context = browser.new_context(**device)
    page = context.new_page()
    page.goto("https://gtm.whr.ai/signin")
    time.sleep(5)
    page.goto("https://gtm.whr.ai/login?utm_source=10times&utm_medium=web&utm_campaign=right_rail&hash=4IQjAPckGZDk9ArLj1D3pDYc8tvqFPX7ZsemflFWON0=&uid=1048476&platform=gtm")
    time.sleep(5)
    page.goto("https://gtm.whr.ai/internal/search/events?view=table")
    page.goto("https://gtm.whr.ai/internal/search/events?view=table&status=active%2Ccancelled%2Cpostponed&active_gte=2025-01-01&active_lte=2025-01-31&ratings=0-1%2C2-3&show=branded%2Cseries%2Cforecasted%2Crating%2CestimatedExhibitors%2CtrustScore%2CaudienceSpread%2CaudienceZone%2CeconomicImpact%2Crankings%2Cscores%2Cmaturity%2Cfrequency%2Calerts")
    page.goto("https://gtm.whr.ai/internal")
    page.goto("https://gtm.whr.ai/internal/search/events?status=active%2Ccancelled%2Cpostponed&active_gte=2025-01-01&active_lte=2025-01-31&locationIds=5dc0b154-e2d8-5160-9bd6-dd8175a58c47&ratings=0-1%2C2-3&show=branded%2Cseries%2Cforecasted%2Crating%2CestimatedExhibitors%2CtrustScore%2CaudienceSpread%2CaudienceZone%2CeconomicImpact%2Crankings%2Cscores%2Cmaturity%2Cfrequency%2Calerts&view=table")
    page.goto("https://gtm.whr.ai/internal")
    page.goto("https://gtm.whr.ai/internal/trends")
    page.goto("https://gtm.whr.ai/internal/trends?active_gte=2025-05-01&active_lte=2025-05-31&locationIds=e3ef02ad-2f97-5fa6-9033-9addfad3f0ef&columns=eventCount&eventTypes=tradeshows%2Cconferences%2Cworkshops&categories=technology%2Cmedical-pharma")
    page.goto("https://gtm.whr.ai/internal")
    page.goto("https://gtm.whr.ai/internal/coordinate")
    page.goto("https://gtm.whr.ai/internal")
    page.goto("https://gtm.whr.ai/internal/trackers")
    page.goto("https://gtm.whr.ai/internal/trackers?id=95ad15d5-e8e8-4253-bf1b-2618a93b5795")
    page.goto("https://gtm.whr.ai/internal")
    page.goto("https://gtm.whr.ai/internal/outreach")
    page.goto("https://gtm.whr.ai/internal")
    page.goto("https://gtm.whr.ai/internal/search/companies")
    page.goto("https://gtm.whr.ai/internal")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)