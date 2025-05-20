# Coffee Shop Challenge

This project is a Python-based simulation of a coffee shop system. It includes classes for managing customers, coffee types, and orders, along with unit tests to ensure the functionality of the system.

## Features

- **Customer Management**: Create and manage customers with unique names.
- **Coffee Management**: Define coffee types with specific attributes.
- **Order Management**: Create orders linking customers and coffee, with price validation.
- **Analytics**: Calculate the number of orders, average price, and identify the most frequent customer for a specific coffee.

## Project Structure

```
.
├── README.md
├── coffee_shop
│   ├── __init__.py
│   ├── coffee.py
│   ├── customer.py
│   └── order.py
├── tests
│   ├── __init__.py
│   ├── test_coffee.py
│   ├── test_customer.py
│   └── test_order.py
└── requirements.txt
```

- `coffee_shop`: Package containing the core functionality of the coffee shop.
  - `coffee.py`: Defines the `Coffee` class with attributes like `name`, `size`, and `price`.
  - `customer.py`: Defines the `Customer` class for managing customer information.
  - `order.py`: Defines the `Order` class for creating and managing orders.
- `tests`: Package containing unit tests for the coffee shop classes.
  - `test_coffee.py`: Tests for the `Coffee` class.
  - `test_customer.py`: Tests for the `Customer` class.
  - `test_order.py`: Tests for the `Order` class.
- `requirements.txt`: Lists the project dependencies.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/coffee-shop-challenge.git
   ```

2. Navigate to the project directory:

   ```bash
   cd coffee-shop-challenge
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

To run the coffee shop simulation, execute the following command:

```bash
python -m coffee_shop
```

## Running Tests

To run the unit tests for the coffee shop classes, use the following command:

```bash
pytest
```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make the changes and commit them.
4. Push the branch to your forked repository.
5. Create a pull request describing your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Inspired by the need to simulate real-world systems using object-oriented programming.
- Thanks to the open-source community for their valuable resources and tools.
