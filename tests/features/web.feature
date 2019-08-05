# Created by Arquillos at 05/08/2019
Feature: DuckDuckGo Web Browsing
  As a web surfer,
  I want to find information online,
  So I can learn new things and get things done.

  Background:
    Given the DuckDuckGo home page is displayed

  Scenario: Basic DuckDuckGo search
    When the user searches for arcade cabinet
    Then results are shown for arcade cabinet

  Scenario: Lenghty DuckDuckGo Search
    When the user searches for the phrase:
      """
      Is it getting better
      Or do you feel the same?
      Will it make it easier on you now?
      You got someone to blame
      """
    Then one of the results contains "One"


