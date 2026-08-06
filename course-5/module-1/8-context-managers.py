# Demo: Cleaning up with context managers: Safe resource handling

# Functions of Context Managers:
# Manages resources, ensuring they are properly acquired and released.
# Acts like a "checkout" system for resources, where you "check out" a resource and "return" it when done.
# Automatic cleanup of resources, even in the presence of errors or exceptions.
# Prevents resource leaks, such as open files or database connections, by ensuring they are closed or released properly.
# Ensures smooth operations, even in the presence of errors or exceptions, by providing a structured way to manage resources.

# Why use Context Managers:
# They prevent resource leaks - by ensuring that resources are properly released, even in the presence of errors or exceptions.
# They make your code cleaner - and more readable by encapsulating resource management logic in a single place.
# They handle exceptions gracefully - by providing a structured way to manage resources, even in the presence of errors or exceptions.

# Code Example:

# import contextlib 
# The contextlib module provides utilities for working with context managers and the with statement.
# it is needed to use the @contextmanager decorator, which allows you to define a context manager using a generator function.

with open('my_file.txt', 'w') as f:
    f.write('Hello, World!') # The file is automatically closed when the block is exited, even if an error occurs.

# r for reading
with open('my_file.txt', 'r') as f:
    content = f.read()
    print(content) # Output: Hello, World!

# 'a' for appending
with open('my_file.txt', 'a') as f:
    f.write('\nAppended text.') # The file is automatically closed when the block is exited, even if an error occurs.

# Exception Handling with Context Managers:
try:
    with open('my_file.txt', 'r') as f:
        content = f.read()
        print(content)
except FileNotFoundError: 
    print("File not found. Please check the file path and try again.")
# context managers can be used in conjunction with exception handling to 
# gracefully handle errors that may occur during resource management.

# Real-world Applications of Context Managers:
# Data processing - Context managers can be used to manage resources such as file handles, 
# database connections, or network sockets in data processing pipelines. 
# They ensure that resources are properly acquired and released, even in the presence of errors or exceptions.

# Web development - Context managers can be used to manage resources such as database connections,
# HTTP sessions, or file uploads in web development frameworks.
# They ensure that resources are properly acquired and released, even in the presence of errors or exceptions

# Machine learning - Context managers can be used to manage resources such as GPU memory,
# model checkpoints, or data loaders in machine learning workflows.
# They ensure that resources are properly acquired and released, even in the presence of errors or exceptions
