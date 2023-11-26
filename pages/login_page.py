import time

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
    NO_PASSWORD_ERROR = (By.ID, "pass-error")
    dropdown_locator = (By.XPATH, "/html/body/div[2]/header/div[1]/div/ul/li[2]/span/button")
    my_account = (By.XPATH, "/html/body/div[2]/header/div[1]/div/ul/li[2]/div/ul/li[1]/a")
    log_out_button = (By.XPATH, "/html/body/div[2]/header/div[1]/div/ul/li[2]/div/ul/li[3]/a")
    def navigate_to_login_page(self):
        self.browser.get(BasePage._BASE_URL)
        self.click(self.LOGIN_ICON)

    def insert_email(self, email):
        # email_element = self.browser.find_element(*self.EMAIL)
        # email_element.send_keys(email)
        self.insert(locator=self.EMAIL, text=email)

    def insert_password(self, password):
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
    #     WebDriverWait(self.browser, 10).until(
    #         EC.visibility_of_element_located(self.WELCOME_BAR)
    #     )
    #
    #     actual_message = self.get_text(self.WELCOME_BAR)
    #     expected_phrase = "Welcome"
    #
    #     # print(f"Actual message: '{actual_message}'")
    #     assert expected_phrase in actual_message

    def check_for_no_password_error(self):
        assert self.is_displayed(self.NO_PASSWORD_ERROR)

    def check_password_error_text(self, expected_error):
        actual_error = self.get_text(self.NO_PASSWORD_ERROR)
        assert expected_error == actual_error

    def click_my_account(self):
        self.click(self.dropdown_locator)
        # time.sleep(2)
        self.click(self.my_account)
        # time.sleep(2)

    def check_url(self):
        self.is_url_correct(f"{BasePage._BASE_URL}/customer/account/")

    def log_out(self):
        self.click(self.dropdown_locator)
        time.sleep(2)
        self.click(self.log_out_button)
        time.sleep(2)