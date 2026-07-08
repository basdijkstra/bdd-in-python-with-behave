Feature: Calculator

  Simple calculator for adding two numbers

  Scenario Outline: Add two numbers
	Given the first number is <first>
	And the second number is <second>
	When the two numbers are added
	Then the result should be <result>
	Examples:
	| first | second | result |
	|     5 |      5 |     10 |
	|     1 |      1 |      2 |
	|   987 |     13 |   1000 |