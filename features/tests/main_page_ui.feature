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


  Scenario: Verify at least 10 benefit cells are displayed on the Target Circle page
    Given I open the Target Circle page
    When I wait for the benefit cells to load
    Then I should see at least 10 benefit cells on the page