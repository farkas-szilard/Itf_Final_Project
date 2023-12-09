import time

from selenium.webdriver.common.by import By

from browser import Browser


class BasePage(Browser):
    _BASE_URL = "https://magento.softwaretestingboard.com/"
    LOGIN_ICON = (By.PARTIAL_LINK_TEXT, "Sign In")

    def find(self, locator):
        return self.browser.find_element(*locator)

    def click(self, locator):
        self.find(locator).click()

    def insert(self, locator, text):
        self.find(locator).send_keys(text)

    def is_displayed(self, locator):
        return self.find(locator).is_displayed()

    def get_text(self, locator):
        return self.find(locator).text

    def is_url_correct(self, expected_url):
        return expected_url == self.browser.current_url

    def log_in(self):
        self.insert(locator=(By.ID, "email"), text="farkasszilard13+softwaretestingboard@gmail.com")
        self.insert(locator=(By.ID, "pass"), text="Password123")
        self.click((By.ID, "send2"))
