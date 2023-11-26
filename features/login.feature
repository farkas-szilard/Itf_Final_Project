Feature: Test the functionality of the login page
  # Scenariu 1: email inregistrat + parola corecta
  # Scenariu 2: email none + parola incorecta
  # Scenariu 3: email none + parola corecta
  # Scenariu 4: email none + parola none
  # Scenariu 5: email cu format invalid + parola none
  # Scenariu 6: Scenario Outline 1: email neinregistrat + o parola incorecta
  #                     email neinregistrat + parola corecta
  #                     email inregistrat + parola incorecta
  # Scenariu 7: Scenario Outline 2: email cu format invalid + o parola incorecta
  #                     email cu format invalid + o parola corecta
  # Scenariu 8: Scenario Outline 3: email cu format invalid + parola none
  #                     email inregistrat + parola none

  Background:
    Given I am on the login page
  @s1
#  email inregistrat + parola corecta
  Scenario: Check that when valid email and password are provided access is granted to the account page
    When I insert "farkasszilard13+softwaretestingboard@gmail.com" email
    And I insert "Password123" password
    And I click on the sign in button
    And I click the My Account dropdown menu
    Then I can login into the application and see the My Account page
    And I log out


@s2
#  email none + parola incorecta
  Scenario: Check that when user tries to login without providing an email address and incorrect password "This is a required field." error message is displayed
    When I insert " " email
    And I insert "abcd1234" password
    And I click on the sign in button
    Then Email error is displayed
    And Email error message contains "This is a required field."

@s3
#  email none + parola corecta
  Scenario: Check that when user tries to login without providing an email address and correct password "This is a required field." error message is displayed
    When I insert " " email
    And I insert "Password123" password
    And I click on the sign in button
    Then Email error is displayed
    And Email error message contains "This is a required field."

@s4
#  email none + parola none
  Scenario: Check that when user tries to login without providing an email address or a password "This is a required field." error message is displayed
    When I insert " " email
    And I click on the sign in button
    Then Email error is displayed
    And Email error message contains "This is a required field."


@s5
#  email cu format invalid + o parola none
  Scenario: Check that when user tries to login with invalid email format and no password "Please enter a valid email address (Ex: johndoe@domain.com)." error message is displayed
    When I insert "abcd1234" email
    And I click on the sign in button
    Then Email error is displayed
    And Email error message contains "Please enter a valid email address (Ex: johndoe@domain.com)."

@s6
  Scenario Outline: Check that we can't log in with invalid credentials
    When I insert "<email>" email
    And I insert "<password>" password
    And I click on the sign in button
    Then Incorrect sign in error is displayed
    Examples:
      |email|password|
      |unregistered@gmail.com|abcd1234|
      |unregistered@gmail.com|Password123|
      |farkasszilard13+softwaretestingboard@gmail.com|abcd1234|
@s7
  Scenario Outline: Check that we can't log in with invalid credentials and receive email error message
    When I insert "<email>" email
    And I insert "<password>" password
    And I click on the sign in button
    Then Email error is displayed
    And Email error message contains "<error_msg>"
    Examples:
      |email|password|error_msg|
      |abcd1234|abcd1234|Please enter a valid email address (Ex: johndoe@domain.com).|
      |abcd1234|Password123|Please enter a valid email address (Ex: johndoe@domain.com).|
@s8
  Scenario Outline: Check that we can't log in with invalid credentials and receive password error message
    When I insert "<email>unregistered@gmail.com" email
    And I click on the sign in button
    Then Password error is displayed
    And Password error message contains "<psw_error>"
    Examples:
      |email|psw_error|
      |unregistered@gmail.com|This is a required field.|
      |farkasszilard13+softwaretestingboard@gmail.com|This is a required field.|
