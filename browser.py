from selenium import webdriver


class Browser:
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.implicitly_wait(10)

    def close_window(self):
        self.browser.close()
