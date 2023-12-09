from browser import Browser
from pages.login_page import LoginPage
from pages.my_account_page import MyAccountPage


def before_all(context):
    context.browser = Browser()
    context.login_page = LoginPage()
    context.my_account_page = MyAccountPage()


def after_all(context):
    context.browser.close_window()
