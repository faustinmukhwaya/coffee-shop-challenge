# order.py

class Order:
    all_orders = []

    def __init__(self, customer, coffee, price):
        from customer import Customer  # Local import to avoid circular dependency
        from coffee import Coffee  # Local import to avoid circular dependency

        if not isinstance(customer, Customer):
            raise TypeError("customer must be an instance of Customer")
        if not isinstance(coffee, Coffee):
            raise TypeError("coffee must be an instance of Coffee")
        if not isinstance(price, (int, float)) or not (1 <= price <= 10):
            raise ValueError("price must be a float between 1.0 and 10.0")
        
        self._customer = customer
        self._coffee = coffee
        self._price = price
        self.__class__.all_orders.append(self)

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee

    @property
    def price(self):
        return self._price
