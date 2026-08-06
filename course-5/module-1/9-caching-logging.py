# Real-world decorators: Caching, logging, and beyond

# Decorators can let you sprinkle extra functionality into your code without cluttering the core logic.
# They can be used for caching, logging, authentication, and more.

# Your code stays clean - decorators allow you to separate concerns, keeping your core logic focused and uncluttered.
# You can reuse your "add-ons" - decorators can be applied to multiple functions or methods, allowing you to reuse the same functionality across different parts of your codebase.
# Code becomes more organized - decorators can help you organize your code by separating concerns and encapsulating functionality in a clear and structured way.

# Caching with Decorators:
# Caching is like having a cheat sheet for your function. It stores the results of previous calculations, 
# and if the function is called again with the same inputs, 
# it simply retrieves the answer from the cache instead of recalculating it.

# It's a clever technique where your function keeps a record of its previous calculations.
# Now, when your function is called again with the same inputs, it doesn't have to do all the heavy lifting.

# This is incredibly useful for functions that perform time-consuming operations, like:

# Fetching data from a website or API - instead of downloading the same data multiple times, 
# you can cache the results and retrieve them quickly.

# Performing complex calculations - if your function does some heavy math, 
# caching can save you from repeating the same calculations over and over again.

# Processing large datasets - if your function processes a large dataset, 
# caching can help you avoid reprocessing the same data multiple times.

# Example of caching with a decorator:
from functools import lru_cache # built-in decorator that caches the results of a function based on its inputs.


@lru_cache(maxsize=None) # the @lru_cache decorator tells Python to cache the results of the fibonacci function.
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))  # Output: 55

# Logging with Decorators:
# Logging is like having a diary for your code. 
# It keeps track of what your code is doing, when it's doing it, and what inputs and outputs it's working with.

# It allows you to record important events, errors, and other information 
# that can help you understand how your code is behaving and troubleshoot issues.

# This log becomes an invaluable tool for understanding your code's behavior, especially when things go wrong.

# Funtion calls: 'Suspect function 'calculate_total' was called at 10:30AM with the following arguments..."
# Important events: "User 'john_doe' logged in at 2:15PM."
# Errors and exceptions: "An error occurred in 'process_data' at 3:45PM: IndexError: list index out of range."

# You can:
# Track down bugs - by logging function calls, inputs, and outputs, 
# you can trace the flow of your code and identify where things might be going wrong.

# Monitor performance - by logging the time taken for function calls or other operations, 
# you can identify bottlenecks and optimize your code.

# Understand user behavior - by logging user interactions, 
# you can gain insights into how users are using your application and identify areas for improvement.

# Audit security - by logging security-related events, 
# you can monitor for suspicious activity and ensure that your application is secure.

# Instead of manually adding print statements or logging calls throughout your code,
# you can use decorators to automatically log function calls, inputs, and outputs.

# Code Example:
import logging # built-in module that provides a flexible framework for emitting log messages from Python programs.

def logger(func): 
    def wrapper(*args, **kwargs): 
        logging.info(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}") 
        result = func(*args, **kwargs) 
        logging.info(f"{func.__name__} returned: {result}") 
        return result 
    return wrapper

"""A decorator that logs function calls."""
logging.basicConfig(filename="my_app.log",level=logging.INFO) 

@logger # the @logger decorator wraps the my_function with the logger function,
def my_function(a, b): 
    """A simple function that adds two numbers.""" 
    return a + b

result = my_function(5, 3) 
print(f"Result: {result}")

# Exploring beyond - Decorators are incredibly versatile and can be used for a wide range of purposes beyond caching and logging.

# Authorization - decorators can be used to enforce access control, 
# ensuring that only authorized users can access certain functions or resources.

# Input validation - decorators can be used to validate inputs to functions,
# ensuring that they meet certain criteria before the function is executed.

# Retrying - decorators can be used to automatically retry a function if it fails,
# which can be useful for handling transient errors in network requests or other operations.

# Timing - decorators can be used to measure the time taken for a function to execute,
# which can be useful for performance monitoring and optimization.

# Debugging - decorators can be used to add debugging information to functions,
# such as printing the function's name, arguments, and return value, which can help with

# Code Profiling - decorators can be used to profile the performance of functions,
# measuring metrics such as execution time, memory usage, and call counts, which can help identify
# performance bottlenecks and optimize code.

# With decorators, you can:
# Give your functions abilities - decorators can add new capabilities to your functions, 
# such as caching, logging, or authorization, without modifying the core logic of the function.

# Create reusable components - decorators can be applied to multiple functions or methods, 
# allowing you to create reusable components that can be easily shared across your codebase.

# Organize your code - decorators can help you organize your code by separating concerns 
# and encapsulating functionality in a clear and structured way.