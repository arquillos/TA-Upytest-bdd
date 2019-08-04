from pytest_bdd import scenarios, given, when, then, parsers

from cucumbers import CucumberBasket


EXTRA_TYPES = {
    'Number': int
}

CONVERTERS = {
    'initial': int,
    'some': int,
    'total': int
}

scenarios('../features/cucumbers.feature', example_converters=CONVERTERS)


@given(parsers.cfparse('the basket has "{initial:Number}" cucumbers', EXTRA_TYPES))
@given('the basket has "<initial>" cucumbers')
def basket(initial):
    return CucumberBasket(initial_count=initial)


@when(parsers.cfparse('"{some:Number}" cucumbers are added to the basket', EXTRA_TYPES))
@when('"<some>" cucumbers are added to the basket')
def add_cucumbers(basket, some):
    basket.add(some)


@then(parsers.cfparse('the basket contains "{total:Number}" cucumbers', EXTRA_TYPES))
@then('the basket contains "<total>" cucumbers')
def basket_has_total(basket, total):
    assert basket.count == total


@when(parsers.cfparse('"{some:Number}" cucumbers are removed from the basket', EXTRA_TYPES))
def remove_cucumbers(basket, some):
    basket.remove(some)
