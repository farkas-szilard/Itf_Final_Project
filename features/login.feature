Feature: Test the functionality of the login page
  # Scenariu 1: email neinregistrat + o parola oarecare
  # Scenariu 2: username none + parola incorecta
  # Scenariu 3: email cu format invalid + o parola oarecare

  # Scenariu 4: email inregistrat + parola corecta
  # Scenariu 5: email inregistrat + parola incorecta
  # Scenariu 6: email neinregistrat + parola corecta


  # Scenariu 1: username incorect + parola corecta
  # Scenariu d: username corect + parola none
  # Scenariu e: username none + parola corecta
  # Scenariu f: username none + parola none
  # Scenariu g: username incorect + parola none
  # Scenariu h: username none + parola incorecta
  # Scenariu i: username incorect + parola incorecta
  # Scenariu j: username blocat + parola corecta

#@s1
#  Scenario: Check that "The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later." error message is displayed when user tries to login with unregistered email"
#    Given I am on the login page
#    When I insert "unregistered@gmail.com" email
#    And I insert "abcd1234" password
#    And I click on the sign in button
#    Then Incorrect sign in error is displayed
#
#@s2
#  Scenario: Check that "This is a required field." error message is displayed when user tries to login without providing an email address
#    Given I am on the login page
#    When I insert " " email
#    And I insert "abcd1234" password
#    And I click on the sign in button
#    Then Email error is displayed
#    And Email error message contains "This is a required field."
#
#@s3
#  Scenario: Check that "Please enter a valid email address (Ex: johndoe@domain.com)." error message is displayed when user tries to login with invalid email format
#    Given I am on the login page
#    When I insert "abcd1234" email
#    And I insert "abcd1234" password
#    And I click on the sign in button
#    Then Email error is displayed
#    And Email error message contains "Please enter a valid email address (Ex: johndoe@domain.com)."
#
#@s4
#  Scenario: Check that when valid email and password are provided access is granted to the account page
#  Given I am on the login page
#    When I insert "farkasszilard13+softwaretestingboard@gmail.com" email
#    And I insert "Password123" password
#    And I click on the sign in button
#    Then I can login into the application and see the sign in bar displaying the welcome message
#@s5
#  Scenario:  Check that "The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later." error message is displayed when user tries to login with valid email, but invalid password"
#  Given I am on the login page
#    When I insert "farkasszilard13+softwaretestingboard@gmail.com" email
#    And I insert "abcd1234" password
#    And I click on the sign in button
#    Then Incorrect sign in error is displayed

@s6
  Scenario: Check that "The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later." error message is displayed when user tries to login with unregistered email"
    Given I am on the login page
    When I insert "unregistered@gmail.com" email
    And I insert "abcd1234" password
    And I click on the sign in button
    Then Incorrect sign in error is displayed
