from behave import given, when, then

@given(u'the first number is {first}')
def step_impl(context, first):
    # TODO: store the first number in the context
    pass


@given(u'the second number is {second}')
def step_impl(context, second):
    # TODO: store the second number in the context
    pass


@when(u'the two numbers are added')
def step_impl(context):
    # TODO: add the two numbers and store the result in the context
    pass


@then(u'the result should be {result}')
def step_impl(context, result):
    # TODO: assert that the result stored in the context is equal to the value passed in the step
    pass
