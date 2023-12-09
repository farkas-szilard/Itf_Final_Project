from behave import *


@given("I am loged in and on the my_account page")
def step_imp(context):
    context.my_account_page.navigate_to_my_account_page()

@when("I click on the edit contact information button")
def step_imp(context):
    context.my_account_page.click_edit_contact_info()

@Then("Create edit contact information page loads")
def step_imp(context):
    context.my_account_page.check_edit_contact_info_url()
