from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base_page import BasePage


class LoginPage(BasePage):
    LOGIN_PAGE_URL = f"{BasePage._BASE_URL}//customer/account/login"
    LOGIN_ICON = (By.PARTIAL_LINK_TEXT, "Sign In")
    EMAIL = (By.ID, "email")
    PASSWORD = (By.ID, "pass")
    LOGIN_BUTTON = (By.XPATH, '//button[@class="action login primary"]')
    SIGN_IN_ERROR = (By.XPATH, '//div[@class="message-error error message"]')
    EMAIL_ERROR = (By.ID, "email-error")
    WELCOME_BAR = (By.XPATH, "//*[@class='logged-in']")

    def navigate_to_login_page(self):
        self.browser.get(BasePage._BASE_URL)
        self.click(self.LOGIN_ICON)

    def insert_email(self, email):
        # email_element = self.browser.find_element(*self.EMAIL)
        # email_element.send_keys(email)
        self.insert(locator=self.EMAIL, text=email)

    def insert_password(self,password):
        self.insert(self.PASSWORD, password)

    def click_sign_in(self):
        self.click(self.LOGIN_BUTTON)

    def check_for_incorrect_sign_in_error(self):
        assert self.is_displayed(self.SIGN_IN_ERROR)

    def check_for_email_error(self):
        assert self.is_displayed(self.EMAIL_ERROR)

    # def check_email_error_text(self):
    #     expected_error = "This is a required field."
    #     error_element = self.browser.find_element(By.ID, "email-error")
    #     actual_error = error_element.text
    #     assert expected_error == actual_error

    # def check_email_error_text(self):
    #     expected_error = {email_error}
    #     actual_error = self.get_text(self.EMAIL_ERROR)
    #     assert expected_error == actual_error
    def check_email_error_text(self, expected_error):
        actual_error = self.get_text(self.EMAIL_ERROR)
        assert expected_error == actual_error

    # def check_welcome_msg(self):
    #     element = WebDriverWait(driver, 10).until(
    #         EC.text_to_be_present_in_element(your_locator, "Welcome")
    #     )

    # def check_welcome_msg(self):
    #     actual_error = self.get_text(self.WELCOME_BAR)
    #     assert "Welcome" in actual_error

    def check_welcome_msg(self):
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(self.WELCOME_BAR)
        )

        actual_message = self.get_text(self.WELCOME_BAR)
        expected_phrase = "Welcome"
        assert expected_phrase in actual_message

    def check_welcome_msg(self):
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(self.WELCOME_BAR)
        )

        actual_message = self.get_text(self.WELCOME_BAR)
        expected_phrase = "Welcome"

        print(f"Actual message: '{actual_message}'")
        assert expected_phrase in actual_message, f"Expected '{expected_phrase}' in the message, but found: '{actual_message}'"
