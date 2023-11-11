from browser import Browser
from selenium.webdriver.support.select import Select


class BasePage(Browser):
    _BASE_URL = "https://magento.softwaretestingboard.com/"

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

    def select_dropdown_option_by_text(self, dropdown_locator, text):
        dropdown_element = self.find(dropdown_locator)
        select = Select(dropdown_element)
        select.select_by_visible_text(text)

    def check_checkbox(self, checkbox_locator):
        checkbox_element = self.find(checkbox_locator)

        if not checkbox_element.is_selected():
            self.click(checkbox_locator)

    def uncheck_checkbox(self, checkbox_locator):
        checkbox_element = self.find(checkbox_locator)

        if checkbox_element.is_selected():
            self.click(checkbox_locator)
