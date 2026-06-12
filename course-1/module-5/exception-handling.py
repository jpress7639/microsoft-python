# TRY-EXCEPT BLOCK

try: 
    result = 10 * 0
except ZeroDivisionError:
    print("Don't divide by zero!")

# MULTI_LAYERED ERROR 

# TRY EXCEPT-ELSE

try:
    number = int(input("Enter a number:"))
    result = 10 / number
    print("The Result is", result)
except ValueError:
    print("invalid input! Please enter a valid number")

except ZeroDivisionError:
    print("Error! Division by zero is not allowed")

finally: 
    print("This will always execute, even if there's an exception.")


# Raise Exceptions

def calculate_age(birth_year):
    current_year = 2026
    if birth_year > current_year:
        raise ValueError("Birth year cannot be in the future")
    return current_year - birth_year

try:
    age = calculate_age(2025)
except ValueError as e:
    print(e)


# WHY EXCEPTION HANDLING IS CRUCIAL IN MODERN SOFTWARE DEVELOPMENT 

# Preventing abrupt crashes
# can also lead to data loss, particularly when the program is in the midst of critical operations

# Graceful recovery and user experience
# Instead of crashing, it can provide informative messages to users, 
# suggest alternative actions, or attempt to resolve the issue internally.

# Streamlined debugging
# When an exception occurs, it provides a detailed traceback, indicating the exact line of code 
# where the error happened and the sequence of events leading up to it. 

# Professionalism and reliability
# demonstrates a commitment to quality and professionalism
# you've taken the time to consider potential problems and have put measures in place to mitigate them

# TRY-EXCEPT-FINALLY TRIO
# TRY: This is where you put the code that might cause an error. 
# For example, if you're trying to open and read a file, you put that code inside a try block. 
# You're basically saying, 'Try to do this, but be prepared for something to go wrong.'

# EXCEPT: The except block is your contingency plan. 
# You specify the type of exception you expect to catch and define the actions 
# your code should take if that specific exception occurs. 
# For instance, if you're expecting a FileNotFoundError, 
# you can write an except FileNotFoundError block that prints an error message and perhaps prompts the user for a different file path.

# FINALLY: This block is your code's optional cleanup, 
# ensuring critical actions are performed regardless of whether exceptions occur. 
# Code within the finally block is guaranteed to execute, making it essential for releasing resources acquired in the try block. 

file_name = "sample.txt"
try:
    with open(file_name, 'r') as file:
        contents = file.read()
        print(contents)
except FileNotFoundError:
    print("Error: File not found -", file_name)

# ZeroDivisionError: This exception is raised when you attempt to divide a number by zero.
# TypeError: If you try to perform an operation on incompatible data types (e.g., adding a string and an integer), you'll encounter a TypeError.
# FileNotFoundError: Trying to access a file that doesn't exist triggers this exception (as shown in the above example).
# IndexError: This exception arises when you try to access an element in a sequence (such as a list or a string) using an invalid index. For example, trying to access the 10th element in a list that only has 5 elements would raise an IndexError.
# KeyError: If you attempt to access a key that doesn't exist in a dictionary, you'll get a KeyError.#

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero")
except TypeError:
    print("Error: Invalid data types")

# LOGGING is the practice of recording details about exceptions and other events in your code.

# import logging

# try:
#     # Your potentially error-prone code here
# except Exception as e:
#     logging.error(f"An error occurred: {e}")  # Logs the exception with details

# CUSTOM EXCEPTIONS

# class InvalidCredentialsError(Exception):
#     pass

# # ... later in your code ...
# if not valid_credentials(username, password):
#     raise InvalidCredentialsError("Incorrect username or password")

# AVOID OVERLY BROAD EXCEPT CLAUSES
# It is generally discouraged to throw a bare except clause 
# You might not even realize there's a problem until the app starts behaving strangely

# DUCK TYPING 
# focuses on how an object behaves rather than its strict type. 
# it allows for dynamic and adaptable code, but can also lead to unexpected runtime errors when objects don't behave as expected

# ERROR HANDLING PHILOSOPHIES
# LBYL (Look Before You Leap)
# Explicitly checking for potential errors before executing code

# EAFP (Easier to Ask Forgiveness than Permission)
# Advocates for trying the operation first and then catching any exceptions that might occur 
# More Pythonic due to emphasis on readability and conciseness

# CODE CHALLENGE

#Task:
# Write a Python function named read_file_contents that takes file_path as an argument.

# Inside the function, use a try-except block to attempt to open the file, read its contents, and print them to the console.

# Handle the FileNotFoundError specifically by printing an appropriate error message if the file doesn't exist.

# Tips:
# Name your file variable file.

# Use the  with open() statement, which ensures that the file is closed automatically, so calling file.close() in the finally block won’t be necessary.

def read_file_contents(file_path):
    try:
        with open(file_path, "r") as file:
            contents = file.read()
            print(contents)
    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
         
