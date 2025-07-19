Feature: Main page UI test

  Scenario: Verify header links has at least 1 link
    Given Open target main page
    Then Verify at least 1 link shown

  Scenario: Verify all header links shown
    Given Open target main page
    Then Verify 6 links shown

  Scenario: User can find Explore other areas of Target
      Given Open target main page
      When Click on About Target
      Then Verify Explore other areas of Target
