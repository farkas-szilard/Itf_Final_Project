from behave import *


@given("I am logged in and on the my_account page")
def step_imp(context):
    context.my_account_page.navigate_to_my_account_page()


@when("I click on the edit contact information button")
def step_imp(context):
    context.my_account_page.click_edit_contact_info()


@Then("Edit contact information page loads")
def step_imp(context):
    context.my_account_page.check_edit_contact_info_url()


@when("I click on the edit password button")
def step_imp(context):
    context.my_account_page.click_change_pwd()


@then("Edit password page loads")
def step_imp(context):
    context.my_account_page.check_change_pwd_url()
