from playwright.sync_api import sync_playwright
import time
import re

def get_temp_email_and_otp():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, slow_mo=1000)

        # Correct mobile device setup
        device = p.devices["iPhone 13"]
        context = browser.new_context(**device)

        page = context.new_page()

        # Step 1: Navigate to Temp-Mail
        page.goto("https://tempmailo.com")
        time.sleep(5)

        # Step 2: Get Temporary Email Address
        temp_email = page.locator("input#i-email").input_value()
        print(f"Temporary Email: {temp_email}")

        # Step 3: Use temp_email for signup
        page2 = context.new_page()
        page2.goto("https://gtm.whr.ai/signup")

        page2.fill("input[name='email']", temp_email)
        page2.get_by_role("tab", name="Participants").click()
        page2.click("button[type='submit']")

        page.bring_to_front()
        page.get_by_role("button", name="Back to inbox").click()
        otp = None

        try:
            page.wait_for_selector("text=no-reply@gtm.whr.ai", timeout=30000)
            page.locator("text=no-reply@gtm.whr.ai").click()
            time.sleep(2)

            iframe_locator = page.frame_locator("iframe#fullmessage")
            otp_element = iframe_locator.locator("p").nth(2)
            otp_element.wait_for()

            otp_text = otp_element.inner_text()
            otp_match = re.search(r"\b\d{6}\b", otp_text)

            if otp_match:
                otp = otp_match.group(0)
                print(f"OTP Found: {otp}")
            else:
                browser.close()
                return None

        except Exception as e:
            print("Failed to fetch OTP:", e)
            browser.close()
            return None

        try:
            otp_field_selector = 'input[data-input-otp="true"]'
            page2.wait_for_selector(otp_field_selector, timeout=10000)
            page2.fill(otp_field_selector, otp)
            page2.click("button[type='submit']")
            print("Signup process automated successfully!")

        except Exception as e:
            print("Failed to enter OTP:", e)

        browser.close()

if __name__ == "__main__":
    get_temp_email_and_otp()
