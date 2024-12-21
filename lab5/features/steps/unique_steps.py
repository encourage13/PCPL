from behave import *
class Unique(object):
    def __init__(self, items, **kwargs):
        self.items = iter(items)
        self.seen = set()
        self.ignore_case = kwargs.get('ignore_case', False)

    def __next__(self):
        while True:
            item = next(self.items)
            if self.ignore_case and isinstance(item, str):
                item = item.lower()
            if item not in self.seen:
                self.seen.add(item)
                return item

    def __iter__(self):
        return self

@given('a list of items {items}')
def step_impl(context, items):
    items_list = eval(items)
    context.items = items_list

@given('ignore case is {ignore_case}')
def step_impl(context, ignore_case):
    context.ignore_case = ignore_case == "True"

@when('I create a Unique iterator')
def step_impl(context):
    kwargs = {}
    if hasattr(context, 'ignore_case'):
        kwargs['ignore_case'] = context.ignore_case
    context.unique_iter = Unique(context.items, **kwargs)
    context.result = list(context.unique_iter)


@then('the iterator should yield {expected_result}')
def step_impl(context, expected_result):
    expected = eval(expected_result)
    assert context.result == expected