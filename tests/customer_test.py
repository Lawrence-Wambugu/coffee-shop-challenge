import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def test_coffee_name_validation():
    with pytest.raises(Exception):
        Coffee("ab")  # name too short




def test_customer_initializes_correctly():
    customer = Customer("Alice")
    assert customer.name == "Alice"

def test_customer_name_validation():
    with pytest.raises(Exception):
        Customer(123)

    with pytest.raises(Exception):
        Customer("")

    with pytest.raises(Exception):
        Customer("A" * 20)  

def test_customer_can_create_order():
    customer = Customer("Alice")
    coffee = Coffee("Latte")
    order = customer.create_order(coffee, 4.5)

    assert isinstance(order, Order)
    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 4.5

def test_customer_orders_and_coffees():
    customer = Customer("Bob")
    coffee1 = Coffee("Espresso")
    coffee2 = Coffee("Latte")
    customer.create_order(coffee1, 3.0)
    customer.create_order(coffee2, 4.0)
    customer.create_order(coffee1, 3.5)

    assert len(customer.orders()) == 3
    assert set(customer.coffees()) == {coffee1, coffee2}

def test_customer_most_aficionado():
    customer1 = Customer("Alice")
    customer2 = Customer("Bob")
    coffee = Coffee("Mocha")

    customer1.create_order(coffee, 5.0)
    customer1.create_order(coffee, 4.0)
    customer2.create_order(coffee, 7.0)

    assert Customer.most_aficionado(coffee) == customer1
