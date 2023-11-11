from behave import  *


@given("I am on the login page")
def step_imp(context):
    context.login_page.navigate_to_login_page()

@when('I insert "{email}" email')
def step_impl(context, email):
    context.login_page.insert_email(email)

@when("I insert a password")
def step_impl(context):
    context.login_page.insert_password()

@when("I click on the sign in button")
def step_impl(context):
    context.login_page.click_sign_in()

@then("Account sign-in incorrect error is displayed")
def step_impl(context):
    context.login_page.check_for_incorrect_sign_in_error()
