Feature: Tests for product page
#
#  Scenario: User can select colors
#    Given Open target product A-54551690 page
#    Then Verify user can click through colors


  Scenario: User can select colors
    Given Open target product page
    Then Verify user can click through c

  Scenario: Add a product to the cart and verify it is there
    Given I open the Target homepage
    When I search for a product "toothbrush"
    And Click search
    And I add the first product to the cart
    And Click Side Menu add
    And Added to the cart
    And Click Side Menu Btt
    Then Added in cart