from selenium import webdriver


class Browser:
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.implicitly_wait(5)

    def close_window(self):
        self.browser.close()