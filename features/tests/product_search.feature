Feature: Test Scenarios for Search functionality

  Scenario: User can search for a product
    Given Open Google page
    When Input Car into search field
    And Click on search icon
    Then Product results for Car are shown


  Scenario: Verifies that Your cart is empty
    Given Open target.com
    When Click on cart icon
    Then Verify Your cart is empty message is shown


  Scenario: Sign In
    Given Open target.com
    When Click Sign In
    And From right side navigation menu, click Sign In
    Then Verify Sign In form opened
