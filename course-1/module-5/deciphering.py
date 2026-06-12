# DECIPHERING ERROR MESSAGES 

# ERROR TYPE - this is the first clue, classifying the error into broad categories 
# Syntax Errors - grammatical mistakes, typo
# Runtime Errors - emerge during program execution, e.g. Zero Division or Index Errors
# Logical Errors - runs without crashing but the output is wrong 

# Error message - this goes deeper - with more specific description 
# Line number - it's telling you the precise line where Python first detected the issue 

# Print Statements - sprinkle print() calls to display values of variables, function outputs, or messages

# Debuggers - like pdb or ipdb - they let you pause your code's execution at specific lines 

# Isolation - comment out sections of code to see if the error still occurs 

# Challenging assumptions - double-check your logic, review library documentation, not overlooking edge cases 

def calculatediscount(price, percentage):
	if percentage < 0 or percentage > 100:
		return "Invalid discount percentage" # Incorrect behavior
	discountamount = price * (percentage / 100)
	return price - discountamount
print(calculatediscount(100, 150)) # Should be an error

# The problem is the function incorrectly returns a string when the discount percentage is invalid.
# It should raise an exception instead to signal an error condition.

# Print Statements: We've already added print(percentage) inside the function.
# Observe Output: The output "150" confirms the invalid input.
# The Fix: Replace the return statement with a ValueError exception.

def calculate_discount(price, percentage):
    if percentage < 0 or percentage > 100:
        raise ValueError("Discount percentage must be between 0 and 100")
    discount_amount = price * (percentage / 100)
    return price - discount_amount
try:
    print(calculate_discount(100, 150))
except ValueError as e:
    print(f"Error: {e}")

# Version Control
# can use systems like Git are a cornerstone 
# they meticulously track every change you make 
# git log - to view the history
# git diff - to compare different versions 
# git checkout - revert to a specific commit where the feature was still functioning 

# TEST-DRIVEN DEVELOPMENT 
# where you write tests before you write the actual code - a safety net

# Example of logging in a web application: In a web application, you might log:

# DEBUG: Detailed information about function inputs and outputs.
# INFO: Key events like user logins or successful form submissions.
# WARNING: Potential issues like a user attempting to access a restricted page.
# ERROR: Exceptions or other critical errors that require immediate attention. These logs can be written to files, databases, or even sent to centralized logging services for analysis.

import logging
logging.basicConfig(filename='myapp.log', level=logging.DEBUG)
def divide(x, y):
    try:
        result = x / y
        logging.info(f"Successfully divided {x} by {y} to get {result}")
        return result
    except ZeroDivisionError:
        logging.error("Division by zero attempted!")
        return None
divide(10, 2)
divide(5, 0)

