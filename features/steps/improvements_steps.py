from behave import given, when, then, use_step_matcher

use_step_matcher("re")

@given(u'we start with an empty bucket of paint')
def step_impl(context):
    pass


@when(u'we add (?P<color>.*) paint')
def step_impl(context, color):
    pass

@then(u'the result is (?P<result>orange|green|purple) paint')
def step_impl(context, result):
    pass
