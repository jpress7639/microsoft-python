# PYTEST TIPS AND TRICKS

# Pytest - a powerful yet remarkably user-friendly testing framework 
# that gives you the ability to craft and run tests for your Python projects
# simplicity and flexibility

# Features 
# Streamline test setup and teardown
# Test multiple scenarios efficiently
# Organize your test suite

# Advanced features
# Fixtures 

# Parameterization enhances your testing 
# Parameterization allows you to run the same test function 
# with different input values, efficiently testing various scenarios and 
# edge cases without writing separate test functions.

# Built-in markers 
# External plugins 
# Have descriptive test names
# Have functions be independent to run from each other 

# TEST FUNCTIONS 
# These are plain and simple Python functions that you designate as tests 
# by starting their names with the prefix "test_"

# Within these test functions, you craft assertions - 
# statements that express your expectations about how your code should behave under specific conditions.
# pytest executes these assertions, and if any of them fail, 
# it signals a potential issue in your code that needs your attention.

# FIXTURES 
# hey handle the setup and teardown of resources that your tests depend on, 
# ensuring each test runs in a pristine and isolated environment.

# Simulate an external API without fitting it
# Temporary Database connection 

# PARAMETERIZATION
# With this feature, you can run the same test function multiple times, 
# each time with a different set of input values.

# MARKERS 
# act as labels or tags for your tests 

# PLUGINS
# pytest's true power lies in its extensibility through plugins. 
# The pytest community has developed a vast array of plugins that cater to virtually every testing need imaginable.

# Scenario 1: Web application testing - Ensuring a seamless user experience

# import pytest
# from your_flask_app import app  # Import your Flask app

# @pytest.fixture
# def client():
#     """Create a test client for interacting with the Flask app."""
#     app.config['TESTING'] = True  # Enable testing mode
#     with app.test_client() as client:
#         yield client

# def test_user_registration(client):
#     """Simulate a user registration and check the response."""
#     data = {'username': 'testuser', 'email': 'testuser@example.com', 'password': 'testpassword'}
#     response = client.post('/register', data=data)

#     assert response.status_code == 302  # Expect a redirect after successful registration
#     # Further checks on database or session data can be added here

# def test_login(client):
#     """Simulate a user login and verify the response."""
#     data = {'username': 'existinguser', 'password': 'correctpassword'}
#     response = client.post('/login', data=data)

#     assert response.status_code == 200  # Expect a successful login
#     assert b'Welcome, existinguser' in response.data  # Check if welcome message is present

# More tests for other routes, form submissions, database interactions, etc. can be added here

# Scenario 2: Data science project - Building trust in your models

# import pytest
# import pandas as pd
# from your_data_science_project import clean_data, train_model, predict

# # Sample test data
# @pytest.fixture
# def test_data():
#     data = {'feature1': [1, 2, 3, None], 'feature2': ['A', 'B', 'C', 'D']}
#     return pd.DataFrame(data)

# def test_data_cleaning(test_data):
#     """Verify if data cleaning handles missing values correctly."""
#     cleaned_data = clean_data(test_data)
#     assert cleaned_data['feature1'].isnull().sum() == 0  # Check if missing values are filled

# def test_model_predictions():
#     """Check if model predictions match expected outcomes."""
#     X_test = ...  # Load your test data
#     y_test = ...  # Load corresponding ground truth labels
#     model = train_model(...) 
#     predictions = predict(model, X_test)
#     accuracy = (predictions == y_test).mean()
#     assert accuracy > 0.8  # Set your desired accuracy threshold

# def test_model_performance():
#     """Evaluate model performance using relevant metrics."""
#     # ... Load your evaluation data and calculate metrics (e.g., precision, recall, F1-score)
#     # Assert that the metrics meet your expectations

# CODE CHALLENGE

import pytest 
from length_list import contains_five


def test_contains_five():
    """ Tests the 'contains_five' function"""
    my_list = [1, 3, 5, 7, 9]
    assert contains_five(my_list) == True

# TEST ORGANIZATION AND STRUCTURE - KEEP TESTS TIDY

# KEY PRINCIPLES IN TEST ORGANIZATION

# MODULARITY
# This is a simple calculator class that demonstrates 
# how to write modular tests for its functions.

# Notice  the Calculator method  is preceded by @pytest.fixture. 

# This modular approach enables precise identification of issues, as each test focuses on a single operation. Modifying a function, like add, 
# only necessitates adjustments to its corresponding test, test_add. 

# Moreover, troubleshooting becomes targeted; 
# a failing test_divide_by_zero pinpoints the problem area.

import pytest

class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            raise ValueError("Division by zero!")
        return x / y

class CalculatorTest:
    @pytest.fixture
    def calculator(self):
        from calculator import Calculator
        return Calculator()

    def test_add(self, calculator):
        result = calculator.add(2, 3)
        assert result == 5

    def test_subtract(self, calculator):
        result = calculator.subtract(5, 2)
        assert result == 3

    def test_multiply(self, calculator):
        result = calculator.multiply(4, 3)
        assert result == 12

    def test_divide(self, calculator):
        result = self.calculator.divide(10, 2)
        assert result == 5

    def test_divide_by_zero(self, calculator):
        with pytest.raises(ValueError):
            calculator.divide(5, 0)


# Naming conventions
# Descriptive names for your test functions and files are essential for efficient test organization.

# Fixtures
# They enable you to define setup and teardown code that can be shared across multiple tests, 
# ensuring consistency and reducing redundancy. 

# Markers
# serve as a powerful organizational tool, allowing you to categorize 
# and filter your tests based on their characteristics. 

# Built-in markers like @pytest.mark.slow help identify slow or network-dependent tests

# Parametrization
# allows you to test your code by running the same test function multiple times with different input values, 
# ensuring it functions correctly under different conditions. 

# This Python code implements basic e-commerce 
# functionalities like adding products to a cart, calculating totals with taxes and discounts, 
# and simulating a checkout process, along with unit tests to ensure their correctness:



import pytest

class Product:
    def __init__(self, name, price, quantity=1):
        self.name = name
        self.price = price
        self.quantity = quantity

class Cart:
    def __init__(self):
        self.items = []

    def add_to_cart(self, product):
        self.items.append(product)

    def calculate_total_price(self, tax_rate=0.0, shipping_fee=0.0):
        subtotal = sum(item.price * item.quantity for item in self.items)
        tax = subtotal * tax_rate
        total = subtotal + tax + shipping_fee
        return total

    def apply_discount(self, discount_percentage):
        for item in self.items:
            item.price *= (1 - discount_percentage / 100)

    def checkout(self, payment_gateway):
        total_price = self.calculate_total_price()
        # In a real application, you'd interact with the payment_gateway here
        if payment_gateway.process_payment(total_price):
            # Place the order (logic not shown here)
            return True
        else:
            return False

class TestProductFunctions:
    def test_add_to_cart_successful(self):
        cart = Cart()
        product = Product("Widget", 10.0)
        cart.add_to_cart(product)
        assert len(cart.items) == 1
        assert cart.items[0] == product

    def test_calculate_total_price_accuracy(self):
        cart = Cart()
        cart.add_to_cart(Product("Widget A", 15.0))
        cart.add_to_cart(Product("Widget B", 20.0, 2))  # 2 of these
        total = cart.calculate_total_price(tax_rate=0.07, shipping_fee=5.0)
        expected_total = (15.0 + 20.0 * 2) * 1.07 + 5.0
        assert total == expected_total

    def test_apply_discount_correctly(self):
        cart = Cart()
        cart.add_to_cart(Product("Discounted Item", 50.0))
        cart.apply_discount(20)  # 20% discount
        assert cart.items[0].price == 40

    def test_checkout_successful_payment(self, mocker):
        # Mocking a payment gateway (would be a real integration in a production app)
        mock_payment_gateway = mocker.Mock()
        mock_payment_gateway.proces_payment.return_value = True

        cart = Cart()
        cart.add_to_cart(Product("Something", 100.0))
        result = cart.checkout(mock_payment_gateway)
        assert result is True # Checkout should be successful