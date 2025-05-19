# order.py

class Order:
    def __init__(self, customer, coffee, price):
        if not isinstance(customer, object) or not hasattr(customer, 'name'):
            raise TypeError("Invalid Customer")
        if not isinstance(coffee, object) or not hasattr(coffee, 'name'):
            raise TypeError("Invalid Coffee")
        if not (isinstance(price, float) or isinstance(price, int)) or not (1.0 <= price <= 10.0):
            raise ValueError("Price must be a float between 1.0 and 10.0")

        self._customer = customer
        self._coffee = coffee
        self._price = float(price)

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee

    @property
    def price(self):
        return self._price
