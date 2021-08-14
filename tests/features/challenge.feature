Feature: Challenge
    Scenario: Create Account on Page
        Given The automation challenge homepage
        When User creates a user Account
        Then User should see their data on Contact Information section

    Scenario Outline: Search for a product
        Given The automation challenge homepage
        And An existing user
        When The user searches for a desired product <product>
        And Goes into the <product> details page
        Then The user should be in correct detail page

        Example:
        |product|
        |glasses|