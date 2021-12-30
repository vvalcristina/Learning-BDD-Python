from behave import *

@given('que eu instalei o behave')
def step_impl01(context):
    print('test')

@when('eu implementar um teste')
def step_impl02(context):
    assert True is not False

@then('o behave vai montar um cenario')
def step_impl03(context):
    assert context.failed is False