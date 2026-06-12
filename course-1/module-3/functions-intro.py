# Code organization, reusability, abstraction, and collaboration

# Built-in Functions print, lend, input
# User defined functions
# Lambda Functions - anonymous one-line functions that serve as simple operations or arguments to other functions

# basic Syntax

# def function_name(parameters): Step 1
    # Comment as placeholder - Step 2 (Docstring)
    # Write the code - Step 3
    # return result # return statement - Step 4
# Save your function - Step 5

def calculate_area(width, height):
    area = width * height
    return area

width = 5
height = 9
the_area = calculate_area(width, height)
print(f"The area is: {the_area}")

# Classes - blueprints for creating objects, digital entities that sum up a set of attributes, or data, and methods and functions.
# Encapsulation - code organization, Inheritance - hierarchal relationship, and Polymorphism - allows different classes to respond to the same function - 3 important abilities 

# Constructor is automatically called when you create a new object of the class

# The DRY principle: A blueprint for code efficiency
# DON'T REPEAT YOURSELF - advocates for eliminating redundant code, encouraging you to consolidate repetitive instructions 

# It's about reducing surface area for errors

# DRY encourages you to create a centralized function for each task needed to be done 

# Code reusability - it encourages:
# Scalability - breaking down large problems into smaller, more manageable chunks
# Maintanability - You can isolate changes to specific components, minimizing the risk of unintended side effects
# Teamwork - each team member can focus on developing and testing specific fucntions, promoting parallel development
# Readability - functions enhance readability by providing a clear structure
# Debugging - Functions aid in debugging by isolating potential issues 

# Refactoring - is the process of restructuring code, changes the factoring without changing external behavior 

# Functions in the modern Python Ecosystem 
# Decorators - modify behavior of other functions without changing their core logic, @cache
# Generators - produce a sequence of values on demand, improving memory efficiency, enabling elegant solutions 
# F Strings - formatted string provide a concise and readable way to embed expressions directly in a string
# Type Hints - annotations specify the expected data types for function arguments and return values 

# Arguments - are the values you pass into a function, provide necessary data 

# Calling the function triggers its execution, showcases reusability, enhances modularity, easier to break down, debug, and modify

# Variable Scope 
# A scope determines where a variable is accessible 
# All about organization and preventing chaos
# Be cautious when using global variables - one change somewhere can alter throughout
# Global Variables are visible throughout your entire code while Local Variables are available to specific functions or code blocks

def calculate_average(numbers):
    total = 0  # Local variable
    count = len(numbers)  # Local variable
    for num in numbers:
        total += num
    average = total / count
    return average

print(calculate_average([2, 5, 4, 1]))

# This compartmentalization serves several important purposes:
# encapsulation - neatly contained within their designed workspace
# avoiding name collisions - you can reuse the same names in different functions without conflict
# memory management - local variables are created when a function starts and destroyed when it ends

# Global variable
COMPANY_NAME = "Global Tech Solutions"

def print_welcome_message():
    print("Welcome to", COMPANY_NAME.upper())

def print_contact_info():
    print("Contact", COMPANY_NAME, "at info@globaltechsolutions.com") 

# Output: Welcome to GLOBAL TECH SOLUTIONS
print_welcome_message()

# Output: Contact Global Tech Solutions at info@globaltechsolutions.com
print_contact_info()

# excessive use of global variables can make your code harder to follow 
# modifying a global variable can have unintended consequences in other parts 
# Best use of global variables are for storing constants, values that are not intended to be changed during the programs execution
# when you need to share data across multiple functions within a module
# if a module is too large, consider splitting it up into smaller, more focused modules

# LEGB Rule - Local, Enclosing, Global, Built-in

# Nested scopes and the enclosing scope 

def outer_function():
    outer_var = "Hello from the outer function!"
    def inner_function():
        print(outer_var)  # Accessible from the enclosing scope
    inner_function()
outer_function()
# Two nested functions, the outer one labeled outer_function and the inner one inner_function

# Naming conventions - snake case is the best option with underscores
# start with a verb 
# avoid generic names 

# For functions that return a boolean value (True/False), 
# strongly consider using prefixes like is_, has_, or can_ to instantly signal their nature. 

# Anatomy of an Exemplary Docstring

# Purpose - a description of what the function does
# Arguments - a detailed list of all input parameters, clear names, expected data types, brief explanations of each argument, indication if argument is mandatory or optional

# Return value - a clear description of the data type, (None) - if it doesn't return anything

# The balance lies in functions that fit on a single screen without scrolling, typically around 10-20 lines of code. 

# Be vary of side effects
global_sum = 0  # Global variable

def calculate_mean_with_side_effect(numbers):
    global global_sum  # Modifying a global variable
    global_sum = sum(numbers)
    return global_sum / len(numbers)

calculate_mean_with_side_effect([5, 3, 4, 1, 1])


# This is a cleaner version
def calculate_mean(numbers):
    """Calculates the mean of a list of numbers."""
    return sum(numbers) / len(numbers)

calculate_mean([5, 3, 4, 1, 1])

# Write a Python function using a precise descriptive name like calculate_diameter_circle while also incorporating snake case.

def calculate_diameter_circle(radius: float) -> float: # this function is for calculating diameter, passing through the radius as an argument
    diameter = radius * 2 
    """To catch any numbers below 0"""
    if radius < 0:
        return -1
    else:
        return float(diameter)

result = calculate_diameter_circle(7)
print(result)