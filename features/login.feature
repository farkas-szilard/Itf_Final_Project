Feature: Test the functionality of the login page
  # Scenariu 1: email inregistrat + parola corecta
  # Scenariu 2: email neinregistrat + o parola incorecta
  # Scenariu 3: email neinregistrat + parola corecta
  # Scenariu 4: email neinregistrat + parola none
  # Scenariu 5: email none + parola incorecta
  # Scenariu 6: email none + parola corecta
  # Scenariu 7: email none + parola none
  # Scenariu 8: email cu format invalid + o parola incorecta
  # Scenariu 9: email cu format invalid + o parola corecta
  # Scenariu 10: email cu format invalid + parola none
  # Scenariu 11: email inregistrat + parola incorecta
  # Scenariu 12: email inregistrat + parola none

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
    Then I log out

#  @s2
##  username neinregistrat + parola incorecta
#  Scenario: Check that when user tries to login with unregistered email and incorrect password "The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later." error message is displayed
#    When I insert "unregistered@gmail.com" email
#    And I insert "abcd1234" password
#    And I click on the sign in button
#    Then Incorrect sign in error is displayed

#  @s3
##  username neinregistrat + parola corecta
#
#  Scenario: Check that when user tries to login with unregistered email and correct password "The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later." error message is displayed
#    When I insert "unregistered@gmail.com" email
#    And I insert "Password123" password
#    And I click on the sign in button
#    Then Incorrect sign in error is displayed

@s4
#  email neinregistrat + parola none
  Scenario: Check that when user tries to login with unregistered email and no password "The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later." error message is displayed
    When I insert "unregistered@gmail.com" email
    And I click on the sign in button
    Then Password error is displayed
    And Password error message contains "This is a required field."

@s5
#  email none + parola incorecta
  Scenario: Check that when user tries to login without providing an email address and incorrect password "This is a required field." error message is displayed
    When I insert " " email
    And I insert "abcd1234" password
    And I click on the sign in button
    Then Email error is displayed
    And Email error message contains "This is a required field."

@s6
#  email none + parola corecta
  Scenario: Check that when user tries to login without providing an email address and correct password "This is a required field." error message is displayed
    When I insert " " email
    And I insert "Password123" password
    And I click on the sign in button
    Then Email error is displayed
    And Email error message contains "This is a required field."

@s7
#  email none + parola none
  Scenario: Check that when user tries to login without providing an email address or a password "This is a required field." error message is displayed
    When I insert " " email
    And I click on the sign in button
    Then Email error is displayed
    And Email error message contains "This is a required field."

@s8
#  email cu format invalid + o parola incorrecta
  Scenario: Check that when user tries to login with invalid email format and correct password "Please enter a valid email address (Ex: johndoe@domain.com)." error message is displayed
    When I insert "abcd1234" email
    And I insert "abcd1234" password
    And I click on the sign in button
    Then Email error is displayed
    And Email error message contains "Please enter a valid email address (Ex: johndoe@domain.com)."

@s9
#  email cu format invalid + o parola correcta
  Scenario: Check that when user tries to login with invalid email format and correct password "Please enter a valid email address (Ex: johndoe@domain.com)." error message is displayed
    When I insert "abcd1234" email
    And I insert "Password123" password
    And I click on the sign in button
    Then Email error is displayed
    And Email error message contains "Please enter a valid email address (Ex: johndoe@domain.com)."

@s10
#  email cu format invalid + o parola none
  Scenario: Check that when user tries to login with invalid email format and no password "Please enter a valid email address (Ex: johndoe@domain.com)." error message is displayed
    When I insert "abcd1234" email
    And I click on the sign in button
    Then Email error is displayed
    And Email error message contains "Please enter a valid email address (Ex: johndoe@domain.com)."

#@s11
##  email inregistrat + parola incorecta
#  Scenario:  Check that when user tries to login with valid email, but invalid password "The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later." error message is displayed
#    When I insert "farkasszilard13+softwaretestingboard@gmail.com" email
#    And I insert "abcd1234" password
#    And I click on the sign in button
#    Then Incorrect sign in error is displayed

@s12
 # email inregistrat + parola none
  Scenario: Check that when user tries to login without providing valid email but no password "This is a required field." error message is displayed under password field
    When I insert "farkasszilard13+softwaretestingboard@gmail.com" email
    And I click on the sign in button
    Then Password error is displayed
    And Password error message contains "This is a required field."

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