import pytest
from pytest_bdd import scenario, given, when, then, parsers

from cucumbers import CucumberBasket


EXTRA_TYPES = {
    'Number': int
}

CONVERTERS = {
    'initial': int,
    'some': int,
    'total': int,
}


@pytest.mark.parametrize(
    ['initial', 'some', 'total'],
    [(1, 2, 3),
     (2, 4, 6),
     (0, 1, 1)]
)
@scenario('../features/cucumbers.feature', 'Add cucumbers to a basket')
def test_add(initial, some, total):
    pass


@given('the basket has <initial> cucumbers')
def basket(initial):
    return CucumberBasket(initial_count=initial)


@when('<some> cucumbers are added to the basket')
def add_cucumbers(basket, some):
    basket.add(some)


@then('the basket contains <total> cucumbers')
def basket_has_total(basket, total):
    assert basket.count == total


@when(parsers.cfparse('"{some:Number}" cucumbers are removed from the basket', EXTRA_TYPES))
def remove_cucumbers(basket, some):
    basket.remove(some)
