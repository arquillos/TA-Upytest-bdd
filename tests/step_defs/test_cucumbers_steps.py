from pytest_bdd import scenarios, given, when, then, parsers

from cucumbers import CucumberBasket


scenarios('../features/cucumbers.feature')
# @scenario('../features/cucumbers.feature', 'Add cucumbers to a basket')
# def test_add():
#     pass
#
#
# @scenario('../features/cucumbers.feature', 'Remove cucumbers from a basket')
# def test_remove():
#     pass


EXTRA_TYPES = {
    'Number': int
}


@given(parsers.cfparse('the basket has "{initial:Number}" cucumbers', EXTRA_TYPES))
def basket(initial):
    return CucumberBasket(initial_count=initial)


@when(parsers.cfparse('"{some:Number}" cucumbers are added to the basket', EXTRA_TYPES))
def add_cucumbers(basket, some):
    basket.add(some)


@then(parsers.cfparse('the basket contains "{total:Number}" cucumbers', EXTRA_TYPES))
def basket_has_total(basket, total):
    assert basket.count == total


@when(parsers.cfparse('"{some:Number}" cucumbers are removed from the basket', EXTRA_TYPES))
def remove_cucumbers(basket, some):
    basket.remove(some)
