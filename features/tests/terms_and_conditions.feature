# Created by user at 7/22/2025
Feature: # Enter feature name here
  # Enter feature description here

Scenario: User can open and close Terms and Conditions from sign in page
 Given Open sign in page
 When Store original window
 And Click on Terms and Conditions link
 And Switch to the newly opened window
 Then Verify Terms and Conditions page is opened
 And  Close new window and switch
 And Verify original