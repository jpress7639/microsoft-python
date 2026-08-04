# Creating cleaner, more readable, and more efficient code

# Decorators: Enhancing functionality with a touch of magic
# Decorators - are functions that take another function as input 
# and return a new function that adds some functionality to the original function. 
# They are often used for 
# logging - can be used to log function calls and their arguments
# access control - can be used to restrict access to certain functions based on user roles or permissions
# caching - can be used to cache the results of expensive function calls to improve performance
# input validation - can be used to validate the inputs to a function before executing it
# memoization - can be used to store the results of expensive function calls to avoid redundant computations, and more.

# How they work:
# Defining a decorator function that takes a function as input 
# Wrapping the original function with additional functionality
# Returning the enhanced function
# Applying the decorator to a function using the @ syntax

# Code Example:
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before the function call")
        result = func(*args, **kwargs)
        print("After the function call")
        return result
    return wrapper

# Function decorators - are a convenient way to apply decorators to functions using the @ syntax
# Example: 
@my_decorator
def say_hello(name):
    print(f"Hello, {name}!")


# Class decorators - are a way to apply decorators to classes, 
# allowing you to modify or enhance the behavior of a class
# Example:
def my_class_decorator(cls): # taking a class as input
    class WrappedClass: # defining a new class that wraps the original class
        def __init__(self, *args, **kwargs): 
            # using args and kwargs to allow for any number of arguments 
            # to be passed to the class constructor
            self.wrapped_instance = cls(*args, **kwargs)

        def __getattr__(self, name): 
        # overriding the __getattr__ method to delegate attribute access to the wrapped instance
            return getattr(self.wrapped_instance, name)

    return WrappedClass

# Method decorators - are a way to apply decorators to methods within a class, 
# allowing you to modify or enhance the behavior of a method
# Example:
def my_method_decorator(method):
    def wrapper(self, *args, **kwargs): # using args and kwargs to allow for any number of arguments to be passed to the method
        print("Before the method call")
        result = method(self, *args, **kwargs) 
        # calling the original method with self, args, 
        # and kwargs to ensure it behaves as expected
        print("After the method call")
        return result
    return wrapper

# Benefits:
# Code reusability - can be applied to multiple functions without modifying their code
# Separation of concerns - can separate the core logic of a function from its additional functionality
# Readability - can make code more readable by clearly indicating the additional functionality being applied to a function

# Potential Complexities:
# Debugging - can make debugging more challenging, as the original function is wrapped in another function

# Nested decorators - can make code harder to read and understand, 
# especially when multiple decorators are applied to a single function

# Generators: Generating values on the fly
# Generators - are a special type of iterator that allows you to generate values on the fly
# They are useful for handling large datasets or streams of data without loading everything into memory at once

# Benefits:
# Memory efficiency - can generate values on the fly without loading everything into memory at once
# Lazy evaluation - can generate values only when they are needed, which can improve performance
# Simplified iteration - can simplify iteration over large datasets or streams of data
# Infinite sequences - can generate infinite sequences of values without running out of memory
# Pipelines and data processing - can be used to create pipelines for processing data in a memory-efficient manner

# yield statement - is used to produce a value from a generator function 
# and pause its execution, allowing it to be resumed later

# Code Example:
def my_generator():
    for i in range(5):
        yield i

# Fibonacci Sequence Generator - is a generator function that produces the Fibonacci sequence on the fly
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Can be called upon like this: 
# for num in fibonacci_generator():

# This example demonstrates a generator function that yields values from 0 to 4.

# Context Managers: Managing resources with elegance
# Context managers - are a way to manage resources, such as files or network connections,
# ensuring that they are properly acquired and released, even in the presence of errors or exceptions

# The power of the with statement
# The with statement is used to create a context in which a resource is acquired and released automatically.

# Encapsulation for clarity and robustness:
# Context managers encapsulate the setup and teardown logic for a resource,
# making code more readable and less error-prone.

# Benefits:
# Improved readability - can make code more readable by clearly indicating the resource being managed and its scope
# Exception handling - can ensure that resources are properly released even in the presence of errors or exceptions
# Reduced code duplication - can reduce code duplication by encapsulating the setup and teardown logic for a resource in a single place
# Customizable behavior - can customize the behavior of a context manager by defining the __enter__ and __exit__ methods

# Code Example:
class MyContextManager:
    def __enter__(self):
        print("Acquiring resource")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Releasing resource")

# This example demonstrates a custom context manager that acquires and releases a resource.
# Can be called @contextlib.contextmanager to create a context manager from a generator function.