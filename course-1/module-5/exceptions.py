# Exceptions are Python's way to pause and giving information about the error
# This includes the type of exception and location 

# Comes in form of an object
# ZeroDivisionError - trying to divide by 0, 
# FoundError - trying to access a file that doesn't exist, 
# TypeError - performing an operation on incompatible types,
# ValueError - trying to pass an inappropriate value to a function
# IndexError - trying to access a list or sequence that is out of bounds
# SyntaxError - if there's an error in syntax
# AttributeError - if an attribute reference or assignment fails

# Traceback - gives a path that led to the error 
# We use try and except blocks that catches this to navigate how to handle the error

# These catches provide a solution instead of having the program crash 
# This improves user experience 

# NameError - doesn't recognize the name, 
# referencing a variable or function, or module that hasn't been properly defined or imported

# e.g.
def myfunction():
    local_var = 10
    print(local_var) # NameError: name 'local_var' is not defined

myfunction()

# TypeError
# combining data in ways Python doesn't allow
# Mismatched operations 
# Incorrect function arguments 
# Class inheritence issues 

# Solutions 
# converting a number using str() or convert a string to an integer using int()

# You can use isinstance() to verify types
def calculate_area(length, width): 
    if not isinstance(length, (int, float)) or not isinstance(width, (int, float)): 
        raise TypeError("Length and width must be numbers.") 
    return length * width

print(calculate_area(5, 'three')) # TypeError: Length and width must be numbers.

# IndexError
# Out of bounds access - when you try to index in a list that doesn't have the correct number 
# Empty Sequences - attempting to access any index in an empty list, tuple, or string

my_list = [1, 2, 3]
for i in range(len(my_list)):
    print(my_list[i])

my_list = []
try:
    print(my_list[0])
except IndexError:
    print("The list is empty.")    


# KeyError 
# occurs when you try to access a value in a dictionary using a key that doesn't exist
# Nonexistent key
# Dynamic key creation - if you're constructing dictionary keys on the fly (based on user input or other calculations)

# before access a dictionary value by its key, use the in operator to check if the key is present
# if key in my_dict: ...

# the get() method allows you to retrieve a value from a dictionary, it returns a default you specify if it doesn't exist

# you can use a try-except block to catch a KeyError to provide alternative behavior

my_dict = {"a": 1, "b": 2}
try:
    print(my_dict["c"])
except KeyError:
    print("Key not found in dictionary.")

# Encountering exceptions is not a sign of failure - it's a natural part of programming

import logging

my_dict = {"a": 1, "b": 2}
try:
    print(my_dict["c"])
except KeyError as e:
    logging.error(f"KeyError encountered: {e}")
    # Handle the error or provide a fallback mechanism


import logging

def get_city_population(populations, city):
    try:
        return populations[city]
    except KeyError:
        raise KeyError(f'City "{city}" not found in population data.')

city_populations = {"New York": 8336817, "Los Angeles": 3979576, "Chicago": 2679044}
city_name = "New York"

print(get_city_population(city_populations, city_name))

# city_name = "Tampa"
# print(get_city_population(city_populations, city_name))


# TRY EXCEPT ELSE FINALLY STRUCTURE 
# allows you to anticipate and catch errors during your programs run time 

# helps with an unexpected error - provides alternative paths or messages 
# except blocks can communicate with the app's users
# structure clearly separates the code with exceptions and error handling 
# good for debugging - traceback info can provide where the problem originated
# robust and reliable - make your code less prone to unexpected failures 


# Attempt risky operations
# Catch and handle exceptions 
# run your code

# TRY - Works for risky operations that you think would cause an error 
# EXCEPT - would be able to catch different errors 
# ELSE - optional, only if no exceptions are raised
# FINALLY - contains code that will always be executed, closing files

# File handling - may encounter situations where it doesn't exist or is corrupted
# Network operations - connections, timeouts, failed requests, can wrap in a try/except
# User import - typos, data that could trigger errors

