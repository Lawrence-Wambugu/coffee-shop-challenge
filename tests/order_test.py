import pytest
from order import Order
from customer import Customer
from coffee import Coffee


def test_order_initializes_correctly():
    customer = Customer("Alice")
    coffee = Coffee("Latte")
    order = Order(customer, coffee, 5.5)

    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 5.5

def test_order_rejects_invalid_price_type():
    customer = Customer("Alice")
    coffee = Coffee("Latte")

    with pytest.raises(Exception):
        Order(customer, coffee, "five")

def test_order_rejects_price_out_of_range():
    customer = Customer("Alice")
    coffee = Coffee("Latte")

    with pytest.raises(Exception):
        Order(customer, coffee, 0.5)

    with pytest.raises(Exception):
        Order(customer, coffee, 15.0)

def test_order_rejects_invalid_customer_type():
    coffee = Coffee("Latte")

    with pytest.raises(Exception):
        Order("Alice", coffee, 5.5)

def test_order_rejects_invalid_coffee_type():
    customer = Customer("Alice")

    with pytest.raises(Exception):
        Order(customer, "Latte", 5.5)
