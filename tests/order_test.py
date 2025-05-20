# tests/test_order.py

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from coffee import Coffee
from customer import Customer
from order import Order

import unittest

class TestOrder(unittest.TestCase):
    def test_valid_order(self):
        c = Customer("Lily")
        coffee = Coffee("Espresso")
        order = Order(c, coffee, 5.5)

        self.assertEqual(order.customer, c)
        self.assertEqual(order.coffee, coffee)
        self.assertEqual(order.price, 5.5)

    def test_invalid_customer_type(self):
        coffee = Coffee("Latte")
        with self.assertRaises(TypeError):
            Order("NotACustomer", coffee, 4.0)

    def test_invalid_coffee_type(self):
        customer = Customer("Milo")
        with self.assertRaises(TypeError):
            Order(customer, "NotACoffee", 3.0)

    def test_invalid_price_type(self):
        c = Customer("Nora")
        coffee = Coffee("Macchiato")
        with self.assertRaises(ValueError):
            Order(c, coffee, "not a float")

    def test_invalid_price_range(self):
        c = Customer("Owen")
        coffee = Coffee("Mocha")
        with self.assertRaises(ValueError):
            Order(c, coffee, 0.5)
        with self.assertRaises(ValueError):
            Order(c, coffee, 12.0)

    def test_price_is_immutable(self):
        c = Customer("Zoe")
        coffee = Coffee("Ristretto")
        order = Order(c, coffee, 5.0)
        with self.assertRaises(AttributeError):
            order.price = 6.0

if __name__ == '__main__':
    unittest.main()
