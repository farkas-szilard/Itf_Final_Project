Feature: Test the functionality of the My Account page
  @s11
  Scenario: Check that when I click the edit account information the correct page loads
    Given I am loged in and on the my_account page
    When I click on the edit contact information button
    Then Create edit contact information page loads
