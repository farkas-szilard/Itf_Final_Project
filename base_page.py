from browser import Browser


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
