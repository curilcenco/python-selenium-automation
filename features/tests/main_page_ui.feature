Feature: Main page UI test

  Scenario: Verify header links has at least 1 link
    Given Open target main page
    Then Verify at least 1 link shown

  Scenario: Verify all header links shown
    Given Open target main page
    Then Verify 6 links shown


  Scenario:Opens target sign in page verifies Sign in
    Given Open target main
    When Click Account
    And Sign in
    And Enters correct email and click Continue
    And Click Continue
    And Incorrect password
    And Clicks Sign in with password
    Then Verifies that an error message is shown