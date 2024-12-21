Feature: Unique iterator

  Scenario: Iterate over unique items
    Given a list of items [1, 2, 2, 3, 4, 4, 5]
    When I create a Unique iterator
    Then the iterator should yield [1, 2, 3, 4, 5]

  Scenario: Iterate over unique items ignoring case
    Given a list of items ["a", "A", "b", "B", "a"]
    And ignore case is True
    When I create a Unique iterator
    Then the iterator should yield ["a", "b"]

  Scenario: Iterate over mixed-case items without case-insensitivity
    Given a list of items ["a", "A", "b", "B", "a"]
    When I create a Unique iterator
    Then the iterator should yield ["a", "A", "b", "B"]
