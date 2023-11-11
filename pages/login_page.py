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

    def navigate_to_login_page(self):
        self.browser.get(BasePage._BASE_URL)
        self.click(self.LOGIN_ICON)

    def insert_email(self, email):
        # email_element = self.browser.find_element(*self.EMAIL)
        # email_element.send_keys(email)
        self.insert(locator=self.EMAIL, text=email)

    def insert_password(self):
        self.insert(self.PASSWORD, "abcd1234")

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

