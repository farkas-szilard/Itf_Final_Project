Feature: Test the functionality of the login page
  # Scenariu 1: email neinregistrat + o parola oarecare
  # Scenariu 2: username none + parola incorecta
  # Scenariu 3: email cu format invalid + o parola oarecare

  Scenario: Check that "The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later." error message is displayed when user tries to login with unregistered email"
    Given I am on the login page
    When I insert "unregistered@gmail.com" email
    And I insert a password
    And I click on the sign in button
    Then Account sign-in incorrect error is displayed

#  Scenario: Check that "This is a required field." error message is displayed when user tries to login without providing an email address
#    Given I am on the login page
#    When I insert " " email
#    And I insert a password
#    And I click on the sign in button
#    Then Email error is displayed
#    And Email error message contains "This is a required field."
#
#  Scenario: Check that "Please enter a valid email address (Ex: johndoe@domain.com)." error message is displayed when user tries to login with invalid email format
#    Given I am on the login page
#    When I insert "abcd1234" email
#    And I insert a password
#    And I click on the sign in button
#    Then Email error is displayed
#    And Email error message contains "Please enter a valid email address (Ex: johndoe@domain.com)."
