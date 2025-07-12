from playwright.sync_api import sync_playwright
import time
import re

def get_temp_email_and_otp():
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=True, slow_mo=1000)  # Use headless=True for headless mode
        context = browser.new_context()
        page = context.new_page()

        # Step 1: Navigate to Temp-Mail
        page.goto("https://tempmailo.com")
        time.sleep(5)  # Wait for the email to load

        # Step 2: Get Temporary Email Address
        temp_email = page.locator("input#i-email").input_value()
        print(f"Temporary Email: {temp_email}")

        # Step 3: Use temp_email for signup on the target site
        # Navigate to the target site (example.com)
        page2 = context.new_page()
        page2.goto("https://gtm.whr.ai/signup")  # Replace with your signup page URL

        # Fill the signup form
        page2.fill("input[name='email']", temp_email)
        page2.get_by_role("listitem").filter(has_text="Research and M&A").click()
        page2.click("button[type='submit']")  # Submit the form

        # Wait for OTP email to arrive in Temp-Mail inbox
        page.bring_to_front()  # Switch back to the Temp-Mail page
        otp = None

        try:
            # Wait for the email to appear in the inbox (timeout after 30 seconds)
            page.wait_for_selector("text=no-reply@gtm.whr.ai", timeout=30000)
            # Open the first email in the inbox
            page.locator("text=no-reply@gtm.whr.ai").click()
            time.sleep(2)  # Wait for the email to load

            # Switching to iframe to fetch the OTP
            iframe_locator = page.frame_locator("iframe#fullmessage")

            # Locate the OTP element inside the iframe
            otp_element = iframe_locator.locator("p").nth(2)  # Target the second <p> tag inside the iframe
            otp_element.wait_for()

            # Extract the OTP
            otp_text = otp_element.inner_text()
            otp_match = re.search(r"\b\d{6}\b", otp_text)  # Match the 4-digit OTP
            if otp_match:
                otp = otp_match.group(0)
                print(f"OTP Found: {otp}")
            else:
                print("OTP not found in the email.")
                browser.close()
                return None

        except Exception as e:
            print("Failed to fetch OTP. No OTP email found within the timeout period.")
            print(f"Error: {e}")
            browser.close()
            return None

        try:
            # Use a flexible selector for the OTP input field
            otp_field_selector = 'input[data-input-otp="true"]'

            # Wait for the OTP input field to be visible and enabled
            page2.wait_for_selector(otp_field_selector, timeout=10000)

            # Fill the OTP into the input field
            page2.fill(otp_field_selector, otp)

            # Submit the OTP form
            page2.click("button[type='submit']")  # Adjust this selector if needed
            print("Signup process automated successfully!")

        except Exception as e:
            print("Failed to enter OTP.")
            print(f"Error: {e}")

        browser.close()

if __name__ == "__main__":
    get_temp_email_and_otp()