from behave import *
import requests

@given(u'{user} is an active ParaBank user')
def is_an_active_parabank_user(context, user):
    context.user = 12212


@when(u'they apply for a {amount} dollar loan')
def they_apply_for_a_loan(context, amount):

    headers = {'Accept': 'application/json'}
    query_params = {'customerId': context.user, 'amount': amount, 'downPayment': 10, 'fromAccountId': 12345}

    context.response = requests.post(
        f'https://parabank.parasoft.com/parabank/services/bank/requestLoan',
        headers=headers,
        params=query_params
    )


@then(u'the loan application is {result}')
def step_impl(context, result):
    response_json = context.response.json()
    print(response_json)
    assert response_json['approved'] == (result == 'approved')
