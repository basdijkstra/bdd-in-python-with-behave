from behave import *


@given(u'a number {first_number}')
def step_impl(context, first_number):
    pass


@given(u'another number {second_number}')
def step_impl(context, second_number):
    pass


@when(u'I add these numbers')
def step_impl(context):
    pass


@then(u'the result is {result}')
def step_impl(context, result):
    pass
