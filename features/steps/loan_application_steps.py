from behave import *

@given(u'{user} is an active ParaBank user')
def is_an_active_parabank_user(context, user):
    pass


@when(u'they apply for a {amount} dollar loan')
def they_apply_for_a_loan(context, amount):
    pass


@then(u'the loan application is {result}')
def step_impl(context, result):
    pass
