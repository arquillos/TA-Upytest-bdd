Feature: Cucumber Basket
    As a gardener,
    I want to carry cucumbers in a basket,
    So that I don't drop them all.

    Scenario Outline: Add cucumbers to a basket
        Given the basket has "<initial>" cucumbers
        When "<some>" cucumbers are added to the basket
        Then the basket contains "<total>" cucumbers

        Examples: Amounts
            | initial   | some  | total |
            | 1         | 2     | 3     |
            | 2         | 3     | 5     |
            | 0         | 1     | 1     |
            | 0         | 0     | 0     |

    Scenario: Remove cucumbers from a basket
        Given the basket has "5" cucumbers
        When "3" cucumbers are removed from the basket
        Then the basket contains "2" cucumbers