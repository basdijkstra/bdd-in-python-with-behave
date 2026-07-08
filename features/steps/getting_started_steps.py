from behave import given, when, then

@given(u'a feature file with steps without step definitions')
def step_impl(context):
    pass


@when(u'I generate step definitions for the steps')
def step_impl(context):
    pass


@then(u'the steps will be implemented by the generated step definitions')
def step_impl(context):
    pass
