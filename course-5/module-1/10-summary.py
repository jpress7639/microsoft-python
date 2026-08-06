# Decorators, Generators, and Context Managers Summary

# Decorator basics: a decorator is a function that takes another function as 
# input and returns a new function that adds some functionality to the original function. 
# Decorators are often used for logging, caching, and authorization.

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before")
        result = func(*args, **kwargs)
        print("After")
        return result
    return wrapper

@my_decorator
def greet():
    print("Hi")

# Function vs method decorators: 
# function decorators wrap standalone functions; method decorators wrap methods in classes 
# but must handle self (or cls) as the first argument.

# Common decorator uses: logging to record calls and errors, 
# and caching (memoization) to store expensive results and return them when the same inputs are used again.

# Generator basics: a generator is a function that uses yield to produce a sequence of values one at a time, 
# pausing between values and resuming where it left off.

def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1

for x in count_up_to(3):
    print(x)

# yield vs return: yield produces a value and pauses the function, 
# while return exits the function and provides a value.

# Context manager basics: 
# a context manager manages setup and teardown of resources (files, network connections, locks) 
# and is used with the with statement to guarantee release, even if an exception occurs.

with open("data.txt") as f:
    data = f.read()
# file is automatically closed here 

# Common mistakes to watch out for:
# Forgetting to return the inner wrapper in a decorator: if the outer decorator function doesn't return wrapper, 
# the decorated function will be None or the wrong object.

# Losing function metadata: a plain wrapper hides the original funtion's name, docstring, and other attributes. 
# Use functools.wraps to preserve them.

# Treating generators like normal lists: generators are exhausted after one iteration. 
# To reuse, you must create a new generator.

# Mixing yield and return value incorrectly: a generator can yield multiple values but can only return once, 
# and the return value is not accessible in the same way as yielded values.
# return some_valye inside a generator raises StopIteration with that value, which is not the same as yielding it.

# Manually managing resources instead of with: opening files or network connections without 'with' 
# leads to resource leaks if exceptions occur before cleanup.

# Assuming contect managers prevent exceptions: they don't stop exceptions from happening
# they ensure cleanup happens even when an exception occurs, but the exception still propagates unless handled.

# introspection - is the ability of a program to examine the type or properties of an object at runtime.
# best used for debugging, logging, and dynamic behavior in programs.

# hasattr - is a built-in function that checks if an object has a specific attribute.
# getattr - is a built-in function that retrieves the value of an attribute from an object by name.
# dir - is a built-in function that returns a list of all attributes and methods of an object, including inherited ones.

# metaclasses - are classes of classes that define how classes behave. A class is an instance of a metaclass.
# best used for enforcing coding standards, creating APIs, and implementing design patterns.

# monkey patching - is the practice of modifying or extending code at runtime without altering the original source code.
# best used for testing, adding features to third-party libraries, and fixing bugs in production code

def get_public_attributes(obj):
    """Return a sorted list of non-callable, non-underscore attribute names of obj.

    Use introspection tools like dir and getattr to discover attributes.
    """
    attributes = []
    for attr in dir(obj): # dir returns a list of all attributes and methods of an object, including inherited ones.
        if not attr.startswith('_'):
            value = getattr(obj, attr) # getattr retrieves the value of an attribute or method from an object by name.
            if not callable(value):
                attributes.append(attr)
    return sorted(attributes)



def copy_public_attributes(source, target):
    """Copy public, non-callable attributes from source to target.

    Use get_public_attributes(source) to determine which attributes to copy.
    Overwrite any existing attributes on target with the same names.
    Return target.
    """
    for attr in get_public_attributes(source):
        value = getattr(source, attr)
        setattr(target, attr, value)
    return target

import logging

def logger(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logging.info(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        logging.info(f"{func.__name__} returned: {result}")
        return result
    return wrapper

logging.basicConfig(filename="my_app.log", level=logging.INFO)

@logger
def my_function(a, b):
    return a + b

result = my_function(5, 3)
print(f"Result: {result}")