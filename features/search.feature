Feature: Search

  Scenario: Login facebook
    Given I navigate to the facebook Home page
    When I enter username password and click login button
    Then I see my facebook home page