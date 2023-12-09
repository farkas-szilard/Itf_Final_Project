import time
from telnetlib import EC
from selenium.webdriver.support import expected_conditions as EC

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from base_page import BasePage


class LoginPage(BasePage):
    # LOGIN_ICON = (By.PARTIAL_LINK_TEXT, "Sign In")
    EMAIL = (By.ID, "email")
    PASSWORD = (By.ID, "pass")
    SIGN_IN_BUTTON = (By.ID, "send2")
    DROPDOWN_ARROW = (By.CSS_SELECTOR, 'button[data-action="customer-menu-toggle"]')
    # LOGIN_PAGE_URL = f"{BasePage._BASE_URL}//customer/account/login"
    LOG_OUT_BUTTON = (By.PARTIAL_LINK_TEXT, "Sign Out")
    EMAIL_ERROR = (By.ID, "email-error")
    SIGN_IN_ERROR = (By.XPATH, '//div[@class="message-error error message"]')
    NO_PASSWORD_ERROR = (By.ID, "pass-error")
    MY_ACCOUNT = (By.PARTIAL_LINK_TEXT, "My Account")
    FORGOT_PASSWORD = (By.CSS_SELECTOR, 'a[class="action remind"]')
    CREATE_ACCOUNT = (By.CSS_SELECTOR, 'a[class="action create primary"]')

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
        self.click(self.SIGN_IN_BUTTON)

    def click_my_account(self, username):
        try:
            WebDriverWait(self.browser, 5).until(
                EC.visibility_of_element_located(self.DROPDOWN_ARROW)
            )
            self.click(self.DROPDOWN_ARROW)
            time.sleep(1)
            self.click(self.MY_ACCOUNT)
            time.sleep(1)
        except TimeoutException:
            raise AssertionError(f"Login credentials for {username} are INVALID !!! ")

    def check_url(self, username):
        expected_url = "https://magento.softwaretestingboard.com/customer/account/"
        self.browser.implicitly_wait(10)
        if expected_url == self.browser.current_url:
            pass
        else:
            self.click(self.LOGIN_ICON)
            time.sleep(2)
            self.insert(self.EMAIL, text="email")
            raise AssertionError(f"Login credentials for {username} are INVALID !!!")

    def log_out(self):
        self.click(self.DROPDOWN_ARROW)
        time.sleep(2)
        self.click(self.LOG_OUT_BUTTON)
        time.sleep(2)

    def check_for_email_error(self):
        assert self.is_displayed(self.EMAIL_ERROR)

    def check_email_error_text(self, expected_error):
        actual_error = self.get_text(self.EMAIL_ERROR)
        assert expected_error == actual_error

    def check_for_incorrect_sign_in_error(self):
        assert self.is_displayed(self.SIGN_IN_ERROR)

    def check_for_no_password_error(self):
        assert self.is_displayed(self.NO_PASSWORD_ERROR)

    def check_password_error_text(self, expected_error):
        actual_error = self.get_text(self.NO_PASSWORD_ERROR)
        assert expected_error == actual_error

    def click_forgot_password(self):
        self.click(self.FORGOT_PASSWORD)

    def check_reset_password_url(self):
        expected_reset_password_url = "https://magento.softwaretestingboard.com/customer/account/forgotpassword/"
        # self.browser.implicitly_wait(10)
        assert expected_reset_password_url == self.browser.current_url

    def click_create_account(self):
        self.click(self.CREATE_ACCOUNT)

    def check_create_account_url(self):
        expected_create_account_url = "https://magento.softwaretestingboard.com/customer/account/create/"
        # self.browser.implicitly_wait(10)
        assert expected_create_account_url == self.browser.current_url
