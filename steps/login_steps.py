from behave import *


@given("I am on the login page")
def step_imp(context):
    context.login_page.navigate_to_login_page()


@when('I insert "{email}" email')
def step_impl(context, email):
    context.login_page.insert_email(email)


@when('I insert "{password}" password')
def step_impl(context, password):
    context.login_page.insert_password(password)


@when("I click on the sign in button")
def step_impl(context):
    context.login_page.click_sign_in()


@when('I click the My Account dropdown menu for username "{username}"')
def step_impl(context, username):
    context.login_page.click_my_account(username)


@when('I click on the forgot your password button')
def step_impl(context):
    context.login_page.click_forgot_password()


@when('I click on the create account button')
def step_impl(context):
    context.login_page.click_create_account()


@then('I can login into the application and see user "{username}" Account page')
def step_impl(context, username):
    context.login_page.check_url(username)


@then("I log out")
def step_impl(context):
    context.login_page.log_out()


@then("Email error is displayed")
def step_impl(context):
    context.login_page.check_for_email_error()


@then('Email error message contains "{email_error}"')
def step_imp(context, email_error):
    context.login_page.check_email_error_text(email_error)


@then("Incorrect sign in error is displayed")
def step_impl(context):
    context.login_page.check_for_incorrect_sign_in_error()


@then("Password error is displayed")
def step_imp(context):
    context.login_page.check_for_no_password_error()


@then('Password error message contains "{password_error}"')
def step_imp(context, password_error):
    context.login_page.check_password_error_text(password_error)


@then('Password reset page loads')
def step_impl(context):
    context.login_page.check_reset_password_url()


@then('Create account page loads')
def step_impl(context):
    context.login_page.check_create_account_url()
