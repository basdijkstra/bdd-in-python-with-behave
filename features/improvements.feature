Feature: Improvements

  Let's see what impact using parameterized step definitions, Scenario Outlines and Backgrounds have on our step definitions

  Background: Starting with an empty bucket
    Given we start with an empty bucket of paint

  Scenario Outline: Mixing two colours yields the right result
	When we add <first> paint
	And we add <second> paint
	Then the result is <result> paint
	Examples:
	| first | second | result |
	|   red | yellow | orange |
	|  blue | yellow |  green |
	|   red |   blue | purple |
