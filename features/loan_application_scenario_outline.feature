Feature: Loan application
  As a loan application evaluator
  I want to only approve loan requests that meet our agreed upon loan amount rules
  So the risk associated with supplying loans remains within regulatory boundaries

  Scenario Outline: loan applications under $1000 are always approved
    Given John is an active ParaBank user
    When they apply for a <amount> dollar loan
    Then the loan application is approved
    Examples:
      | amount |
      | 999    |
      | 1      |