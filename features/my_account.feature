Feature: Test the functionality of the My Account page
  #Testing the functionality of the My Account page

  Background:
    Given I am logged in and on the my_account page

  @s11
  Scenario: Check that when I click the edit account information button the correct page loads
    When I click on the edit contact information button
    Then Edit contact information page loads

  @s12
  Scenario: Check that when I click the edit password button the correct page loads
    When I click on the edit password button
    Then Edit password page loads
