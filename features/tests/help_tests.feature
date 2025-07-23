Feature: Tests for Help pages

#  Scenario: User can select Help topic Promotions & Coupons
#    Given Open Help page for Returns
#    Then Verify help Returns page opened
#    When Select Help topic Promotions & Coupons
#    Then Verify help Current promotions page opened
#
#  Scenario: User can select Help topic Target Circle
#    Given Open Help page Returns
#    Then Verify help Returns page opened
#    When Select Help topic Target Circle™
#    Then Verify help About Target Circle page opened

  Scenario: Verify that selecting a help topic opens the correct page
    Given User is on the Target Help page
    When Verify input field
    When User inputs "order" in search input field
    Then Verify dropdown help appear
#   And The "Track my order" help page should open
    And Dropdown selection click
    And Opens the correct url