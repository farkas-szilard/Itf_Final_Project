import time
from telnetlib import EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from base_page import BasePage


class LoginPage(BasePage):
    LOGIN_ICON = (By.PARTIAL_LINK_TEXT, "Sign In")
    EMAIL = (By.ID, "email")
    PASSWORD = (By.ID, "pass")
    LOGIN_BUTTON = (By.XPATH, "/html/body/div[2]/main/div[3]/div/div[2]/div[1]/div[2]/form/fieldset/div[4]/div[1]/button/span")
    DROPDOWN_ARROW = (By.XPATH, "/html/body/div[2]/header/div[1]/div/ul/li[2]/span/button")
    LOGIN_PAGE_URL = f"{BasePage._BASE_URL}//customer/account/login"
    SIGN_IN = (By.XPATH, "/html/body/div[2]/header/div[1]/div/ul/li[2]/a")
    LOG_OUT_BUTTON = (By.XPATH, "/html/body/div[2]/header/div[1]/div/ul/li[2]/div/ul/li[3]/a")
    EMAIL_ERROR = (By.ID, "email-error")
    SIGN_IN_ERROR = (By.XPATH, '//div[@class="message-error error message"]')
    NO_PASSWORD_ERROR = (By.ID, "pass-error")

    LOGIN_BUTTON = (By.XPATH, "/html/body/div[2]/main/div[3]/div/div[2]/div[1]/div[2]/form/fieldset/div[4]/div[1]/button/span")
    SIGN_IN_ERROR = (By.XPATH, '//div[@class="message-error error message"]')
    EMAIL_ERROR = (By.ID, "email-error")
    WELCOME_BAR = (By.XPATH, "//*[@class='logged-in']")
    NO_PASSWORD_ERROR = (By.ID, "pass-error")
    DROPDOWN_ARROW = (By.XPATH, "/html/body/div[2]/header/div[1]/div/ul/li[2]/span/button")
    my_account = (By.XPATH, "/html/body/div[2]/header/div[1]/div/ul/li[2]/div/ul/li[1]/a")
    LOG_OUT_BUTTON = (By.XPATH, "/html/body/div[2]/header/div[1]/div/ul/li[2]/div/ul/li[3]/a")
    SIGN_IN = (By.XPATH, "/html/body/div[2]/header/div[1]/div/ul/li[2]/a")
    login_fail_error = (By.XPATH, '//*[@id="maincontent"]/div[2]/div[2]/div/div/div')

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

    def click_my_account(self):
        try:
            WebDriverWait(self.browser, 2).until(
                EC.visibility_of_element_located(self.DROPDOWN_ARROW)
            )
            # If the element is found within 2 seconds, proceed with the click
            self.click(self.DROPDOWN_ARROW)
            time.sleep(3)
            self.click(self.my_account)
            time.sleep(2)
            # Rest of your code here
        except TimeoutException:
            # If the element is not found within 2 seconds, enter the else block
            raise AssertionError("Login credentials are INVALID")
        # if self.is_displayed(self.DROPDOWN_ARROW):
        #     self.click(self.DROPDOWN_ARROW)
        #     time.sleep(2)
        #     self.click(self.my_account)
        # else:
        #     self.click(self.SIGN_IN)
        #     time.sleep(2)
        #     self.insert(self.EMAIL, text="email")
        #     raise AssertionError("Login credentials are INVALID")

    def check_url(self):
        expected_url = "https://magento.softwaretestingboard.com/customer/account/"
        self.browser.implicitly_wait(10)
        # self.click(self.DROPDOWN_ARROW)
        # # time.sleep(2)
        # self.click(self.my_account)
        if expected_url == self.browser.current_url:
            pass
        else:
            self.click(self.SIGN_IN)
            time.sleep(2)
            self.insert(self.EMAIL, text="email")
            raise AssertionError("Login credentials are INVALID")

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



    # def check_url(self):
    #     expected_url = "https://magento.softwaretestingboard.com/customer/account/"
    #     self.browser.implicitly_wait(10)
    #     if expected_url == self.browser.current_url:
    #         pass
    #     else:
    #         self.click(self.SIGN_IN)
    #         time.sleep(2)
    #         # self.insert(self.EMAIL, text="email")
    #         raise AssertionError("Login credentials are INVALID")
    #
    # def log_out(self):
    #     self.click(self.DROPDOWN_ARROW)
    #     time.sleep(2)
    #     self.click(self.LOG_OUT_BUTTON)
    #     time.sleep(2)
