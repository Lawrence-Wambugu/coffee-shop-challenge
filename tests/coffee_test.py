import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def test_coffee_name_validation():
    with pytest.raises(Exception):
        Coffee("ab")  # short name




def test_coffee_initializes_correctly():
    coffee = Coffee("Cappuccino")
    assert coffee.name == "Cappuccino"

def test_coffee_name_validation():
    with pytest.raises(Exception):
        Coffee(123)

    with pytest.raises(Exception):
        Coffee("A")  # Too short

def test_coffee_is_immutable():
    coffee = Coffee("Latte")
    with pytest.raises(AttributeError):
        coffee.name = "Espresso"

def test_coffee_orders_and_customers():
    customer1 = Customer("Alice")
    customer2 = Customer("Bob")
    coffee = Coffee("Espresso")

    Order(customer1, coffee, 3.5)
    Order(customer2, coffee, 4.0)

    assert len(coffee.orders()) == 2
    assert set(coffee.customers()) == {customer1, customer2}

def test_coffee_num_orders_and_average_price():
    customer = Customer("Alice")
    coffee = Coffee("Americano")

    customer.create_order(coffee, 3.0)
    customer.create_order(coffee, 5.0)
    customer.create_order(coffee, 4.0)

    assert coffee.num_orders() == 3
    assert coffee.average_price() == 4.0
