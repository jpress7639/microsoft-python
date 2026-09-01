import unittest
from unittest.mock import patch, Mock
from math_ops import add, subtract, multiply, divide

class TestMathOps(unittest.TestCase):
    @patch('math_ops.add', return_value=5)
    def test_add(self, mock_add):
        self.assertEqual(add(2, 3), 5)

    @patch('math_ops.subtract', return_value=2)
    def test_subtract(self, mock_subtract):
        self.assertEqual(subtract(5, 3), 2)

    @patch('math_ops.multiply', return_value=6)
    def test_multiply(self, mock_multiply):
        self.assertEqual(multiply(2, 3), 6)

    @patch('math_ops.divide', return_value=2)
    def test_divide(self, mock_divide):
        self.assertEqual(divide(6, 3), 2)

    @patch('math_ops.divide', return_value=2)
    def test_divide_without_mock(self, mock_divide):
        self.assertEqual(divide(6, 3), 2)

    @patch('math_ops.divide', side_effect=ValueError("Cannot divide by zero"))
    def test_divide_by_zero(self, mock_divide):
        with self.assertRaises(ValueError):
            divide(6, 0)

if __name__ == "__main__":
    unittest.main()