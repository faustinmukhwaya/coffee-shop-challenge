import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from coffee import Coffee  # Importing Coffee class
from customer import Customer  # Importing Customer class
from order import Order  # Importing Order class

class TestCoffee(unittest.TestCase):
    def test_average_price_zero(self):
        coffee = Coffee("Espresso")
        self.assertEqual(coffee.name, "Espresso")

    def test_invalid_name_type(self):
        with self.assertRaises(ValueError):
            Coffee(123)

    def test_invalid_name_length(self):
        with self.assertRaises(ValueError):
            Coffee("a")

    def test_name_is_immutable(self):
        coffee = Coffee("Latte")
        with self.assertRaises(AttributeError):
            coffee.name = "Mocha"

    def test_orders_and_customers(self):
        coffee = Coffee("Cappuccino")
        c1 = Customer("Anna")
        c2 = Customer("Ben")

        c1.create_order(coffee, 3.5)
        c2.create_order(coffee, 4.5)

        self.assertEqual(len(coffee.orders), 2)
        self.assertEqual(len(coffee.customers), 2)

    def test_num_orders_and_average_price(self):
        coffee = Coffee("Flat White")
        c1 = Customer("A")
        c2 = Customer("B")
        c1.create_order(coffee, 4.0)
        c2.create_order(coffee, 6.0)

        self.assertEqual(coffee.num_orders(), 2)
        self.assertAlmostEqual(coffee.average_price(), 5.0)

    def test_average_price_zero(self):
        coffee = Coffee("Americano")
        self.assertEqual(coffee.average_price(), 0)

if __name__ == '__main__':
    unittest.main()
