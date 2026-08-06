# Building a timer decorator: Track your function's speed

# Decorators
# A function that takes another function as input and returns a new function 
# that adds some functionality to the original function.

# This promotes code reusability and separation of concerns, 
# allowing you to add functionality to existing functions without modifying their code.

# Building a timer decorator: 
import time
def timer(func):
# We define a decorator function timer that takes a function func as input. 
# This func represents the function we want to decorate.
	"""A decorator that measures the execution time of a function."""
	def wrapper(*args, **kwargs): 
	# Inside timer, we define another function wrapper that accepts any arguments (*args and **kwargs) 
		"""Inner function that wraps the decorated function."""
		start_time = time.time() # wrapper records the start time using time.time()
		result = func(*args, **kwargs) # Execute the original function with provided arguments and store the result
		end_time = time.time() # Record the end time
		execution_time = end_time - start_time # calculates the execution time
		print (f"Function {func.__name__} took {execution_time: .4f} seconds.") # prints it using an f-string
		return result
	return wrapper


@timer # We use the @timer syntax above my_function to apply the decorator.
# This means that when my_function is called, it will be wrapped by the timer decorator,
# which will measure and print the execution time of my_function.
def my_function(a, b):
	"""A simple function that adds two numbers."""
	time.sleep(1) # Simulate some work
	return a + b


result = my_function(5, 3)
print (f" Result: {result}")

# Think of them as reusable building blocks that can be attached to your functions to 
# enhance their capabilities without altering their core code.

# They can be used for:
# Authorization - checking if a user has permission to access a specific function
# Caching - Storing a function's result to avoid redundant computations
# Input validation - ensuring the arguments passed to a function meet certain criteria
# Logging - recording function calls and their arguments for debugging or monitoring purposes
# Keep your code clean - instead of repeating the same lines of code in multiple functions
# Promote reusability - by creating a decorator once and applying it to multiple functions
# Improve organization - by separating the core logic of a function from its additional functionality

# Instead of adding timing code to each function individually, you can create a timer decorator. 

# Generators
# Generators are special functions in Python that produce a sequence of values on demand, 
# instead of computing and storing all the values in memory at once.

def log_file_reader (filename): # generator function that takes a filename as input
	"""A generator that reads a log file line by line."""
	with open(filename, 'r') as f: # with open to ensure proper file handling, automatically closing the file after reading
		for line in f:
			yield line.strip() # yield is the heart of a generator function, allowing it to produce a value and pause its execution,
            # returning the line without leading/trailing whitespace, and resuming from where it left off when the next value is requested.

for line in log_file_reader ('my_log.txt'):
	# Process each line here
	print(line)
# when you iterate over the generator, it reads the log file line by line, yielding one line at a time.

# Context Managers
# Context managers are a way to manage resources in Python, ensuring that they are properly acquired and released.
# They are particularly useful in situations where you need to perform actions before and after a specific operation,
# such as:

# Acquiring and releasing locks: Preventing race conditions in multithreaded applications.

# Connecting to and disconnecting from a database: Ensuring proper database connection management.

# Changing the current working directory: 
# Reverting to the original directory after performing operations in a different location.

# By using context managers, you can encapsulate these setup and teardown actions, 
# making your code cleaner and more robust.

# The with statement is used to create a context in which a resource is acquired and released automatically.

# Code Example:
import sys
import io
from contextlib import contextmanager

@contextmanager 
# The @contextmanager decorator is used to define a context manager function, 
# which allows you to create a context in which resources are managed automatically.
def suppress_stdout():
    """Temporarily suppresses stdout."""
    original_stdout = sys.stdout # Save the original stdout so we can restore it later
    sys.stdout = io.StringIO() # Redirects stdout to a StringIO object, effectively suppressing any output that would normally be printed to the console.
    try:
        yield
    finally:
        sys.stdout = original_stdout # Restore the original stdout, ensuring that any output printed after the context manager is restored to normal behavior.

# Example usage:
with suppress_stdout(): 
	# with suppress_stdout() creates a context in which stdout is suppressed, 
    # meaning that any print statements within this block will not produce output to the console.
    print("This won't be displayed.")

print("This will be displayed.")

# Decorators, generators, and context managers are indispensable tools in the Python developer's arsenal. 
# They enhance code functionality, efficiency, and readability, promoting modularity, reusability, and maintainability.

# Consider these benefits and applications:
# Enhanced expressiveness - Decorators, generators, and context managers allow you to express 
# complex behaviors in a concise and readable manner.

# Improved code organization - By separating concerns and encapsulating functionality, 
# these constructs help keep your codebase organized and maintainable.

# Increased productivity - Leveraging these tools can lead to faster development and easier debugging,
# as they provide built-in mechanisms for common programming tasks.

# Advanced applications - Decorators can be used for metaprogramming, generators for asynchronous programming,
# and context managers for resource management in complex systems.