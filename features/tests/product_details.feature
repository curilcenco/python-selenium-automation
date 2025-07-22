Feature: Tests for product page

  Scenario: User can select colors
    Given Open target product A-54551690 page
    Then Verify user can click through colors

#  Scenario: Add a product to cart and verify its presence and details
#    Given Open target main page
#    When Add product to cart from search results
#    And Store product info
#    And Confirm Add to Cart button from side navigation
#    Then Verify that every product has name and image