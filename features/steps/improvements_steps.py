from behave import given, when, then

@given(u'we start with an empty bucket of paint')
def step_impl(context):
    pass


@when(u'we add red paint')
def step_impl(context):
    pass


@when(u'we add yellow paint')
def step_impl(context):
    pass


@then(u'the result is orange paint')
def step_impl(context):
    pass


@when(u'we add blue paint')
def step_impl(context):
    pass


@then(u'the result is green paint')
def step_impl(context):
    pass


@then(u'the result is purple paint')
def step_impl(context):
    pass
