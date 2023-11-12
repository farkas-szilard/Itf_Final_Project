from behave import  *


@given("I am on the login page")
def step_imp(context):
    context.login_page.navigate_to_login_page()

@when('I insert "{email}" email')
def step_impl(context, email):
    context.login_page.insert_email(email)

@when('I insert "{password}" password')
def step_impl(context,password):
    context.login_page.insert_password(password)

@when("I click on the sign in button")
def step_impl(context):
    context.login_page.click_sign_in()

@then("Incorrect sign in error is displayed")
def step_impl(context):
    context.login_page.check_for_incorrect_sign_in_error()

@then("Email error is displayed")
def step_impl(context):
    context.login_page.check_for_email_error()

@then('Email error message contains "{email_error}"')
def step_imp(context, email_error):
    context.login_page.check_email_error_text(email_error)

@then("I can login into the application and see the sign in bar displaying the welcome message")
def step_imp(context):
    context.login_page.check_welcome_msg()

@then("Password error is displayed")
def step_imp(context):
    context.login_page.check_for_no_password_error()

@then('Password error message contains "{password_error}"')
def step_imp(context, password_error):
    context.login_page.check_password_error_text(password_error)