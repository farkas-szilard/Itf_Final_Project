from selenium.webdriver.common.by import By

from base_page import BasePage
from pages.login_page import LoginPage


class MyAccountPage(LoginPage):
    # EDIT_CONTACT_INFO = (By.XPATH, '//*[@id="maincontent"]/div[2]/div[1]/div[3]/div[2]/div/div[2]/a[1]')
    EDIT_CONTACT_INFO = (By.LINK_TEXT, "Edit")
    EDIT_PWD = (By.XPATH, '//a[@class="action change-password"]')

    def navigate_to_my_account_page(self):
        self.browser.get(BasePage._BASE_URL)
        self.click((By.PARTIAL_LINK_TEXT, "Sign In"))
        self.log_in()
        self.click(self.DROPDOWN_ARROW)
        self.click(self.MY_ACCOUNT)

    def click_edit_contact_info(self):
        self.click(self.EDIT_CONTACT_INFO)

    def check_edit_contact_info_url(self):
        expected_url = "https://magento.softwaretestingboard.com/customer/account/edit/"
        assert expected_url == self.browser.current_url

    def click_change_pwd(self):
        self.click(self.EDIT_PWD)

    def check_change_pwd_url(self):
        expected_url = "https://magento.softwaretestingboard.com/customer/account/edit/changepass/1/"
        assert expected_url == self.browser.current_url
