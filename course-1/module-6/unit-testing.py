
# UNIT TESTING 
# a piece of code that tests a specific unit or function - tests that it matches the expected result 
# dissecting code into granular testing components 
# craft to examine whether code acts as intended

# Catches errors early - before they cascade into bigger problems 
# Encourage you to write modular - functions and modules that are more focused and independent
# Makes changes less risky - refactor competently 

# Use in complex projects, collaborative environments
# Promotes long-term maintenance and understanding of the system 

# UNIT TESTING PROCESS:
# Identify the unit - the piece/function 
# Define the test case 
# Write the test code
# Execute the tests - a clean run or a failed test is an immediate alert 
# Debug and iterate - solidify your confidence 


# Assertions - statements that verify whether your code is behaving as expected 
def add_numbers(a, b):
    return a + b

add_numbers(2, 3)

# Test cases - a set of these assertions that, together, put a single unit of code through a comprehensive workout
# Test suite - a collection of multiple test cases 
# Test runner - this tool takes your carefully designed suite and executes all test cases 

# This promotes error detection, code confidence, design improvement, living documentation

import pytest 

def calculate_discount(price, percentage):
  return price - (price * percentage / 100)
 
class TestDiscountCalculation:
  def test_ten_percent_discount(self):
    result = calculate_discount(100, 10)
    assert result == 90  # Assertion
 
  def test_invalid_input(self):
    with pytest.raises(TypeError):
      calculate_discount("100", 10)   # Test for incorrect input type
