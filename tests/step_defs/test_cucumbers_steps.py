from pytest_bdd import scenario, given, when, then

from cucumbers import CucumberBasket


@scenario('../features/cucumbers.feature', 'Add cucumbers to a basket')
def test_add():
    pass


@scenario('../features/cucumbers.feature', 'Remove cucumbers from a basket')
def test_remove():
    pass


@given("the basket has 2 cucumbers")
def basket():
    return CucumberBasket(initial_count=2)


@when("4 cucumbers are added to the basket")
def add_cucumbers(basket):
    basket.add(4)


@then("the basket contains 6 cucumbers")
def basket_has_total(basket):
    assert basket.count == 6


@given("the basket has 4 cucumbers")
def basket_remove():
    return CucumberBasket(initial_count=4)


@when("3 cucumbers are removed from the basket")
def remove_cucumbers(basket_remove):
    basket_remove.remove(3)


@then("the basket contains 1 cucumber")
def basket_removed(basket_remove):
    assert basket_remove.count == 1
