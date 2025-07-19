Feature: Cart tests

  Scenario: 'Your cart is empty' message is shown for empty cart
    Given Open target main page
    When Click on Cart icon
    Then Verify 'Your cart is empty' message is shown

     Scenario: 'Your cart is empty' message
      Given target.com
      When Click on Cart ico
      Then Verify message “Your cart is empty”
