class Order:
    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self._price = self.validate_price(price)
        Order.all.append(self)

    @staticmethod
    def validate_price(price):
        if isinstance(price, float) and 1.0 <= price <= 10.0:
            return price
        else:
            raise Exception("Price must be a float between 1.0 and 10.0.")

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, value):
        from customer import Customer
        if isinstance(value, Customer):
            self._customer = value
        else:
            raise Exception("customer must be a Customer instance.")

    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, value):
        from coffee import Coffee
        if isinstance(value, Coffee):
            self._coffee = value
        else:
            raise Exception("coffee must be a Coffee instance.")

    @property
    def price(self):
        return self._price  # Immutable
