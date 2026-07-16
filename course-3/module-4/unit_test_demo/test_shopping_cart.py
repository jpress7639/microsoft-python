import unittest
from shopping_cart import calculate_discount

class TestShoppingCart(unittest.TestCase):

    def test_discount_calculation(self):
        original_price = 100
        discount_percentage = 20
        expected_discount_price = 80

        discounted_price = calculate_discount(original_price, discount_percentage)
        self.assertEqual(discounted_price, expected_discount_price)

if __name__ == '__main__':
    unittest.main()

# Additional assertion methods:
# assertNotEqual(a, b) - Check that a and b are not equal
# assertTrue(x) - Check that x is True
# assertFalse(x) - Check that x is False
# assertIs(a, b) - Check that a is b
# assertIn(a, b) - Check that a is in b
# assertNotIn(a, b) - Check that a is not in b
# assertIsInstance(a, b) - Check that a is an instance of b
# assertRaises(exception, callable, *args, **kwargs) - Check that calling callable with the given arguments raises the specified exception

# Best practices
# Test often and early
# Keep tests small and focused
# Use descriptive test names
# Isolate dependencies
# Automate your tests - incorporate them in a continuous integration

