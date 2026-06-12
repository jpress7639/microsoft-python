# Print Debugging 
# checking your code's integrity by strategically inserting 

def calculate_average(numbers):
    print("Input numbers:", numbers)
    total = sum(numbers)
    print("Total:", total)
    count = len(numbers)
    print("Count:", count)
    average = total / count
    print("Average:", average)
    return average

# print parenthesis statements into your code 
# to show you how the different sections of your program are performing.

# track variable values at different stages - to see how they change 
# function entry and function exit 
# loop iteration - shows you the current iteration within a loop
# conditional checks - feedback if an if statement is working 

# Advanced techniques 
# formatting output - more informative and structure output - makes it easier to parse
# conditional printing - if statements as to when specific messages are displayed 
# logging - larger projects or longer running scripts, structured logs about detailed info in execution

import logging

logging.basicConfig(filename='app.log', level=logging.DEBUG)
logging.debug('This is a debug message')
logging.info('This is an informational   message')
logging.warning('This is a warning message')
logging.error('This is an error message')

# Info, Debug, Custom Messages, Error

# 1) Identify Suscipicious Code Sections 
# 2) Insert Print Statements 
# 3) Run Your Code 
# 4) Analyze the Output - check printed values and messages 
# 5) Pinpoint the Error 
# 6) Iterate and Refine - making necessary corrections and rerun code

# you can add Breakpoints in your IDE where code will run and stop where you marked it

# ASSERTIONS 
# they're statements that express conditions you expect to be true at specific points.
# If an assertion fails, meaning the condition is not met, 
# the program raises an exception, immediately alerting you to the problem.

def calculate_area(length, width):
    assert length > 0, "Length must be positive"
    assert width > 0, "Width must be positive"
    return length * width

# DEBUGGERS 
# Debuggers are like time machines for your code. 
# hey allow you to pause execution, inspect the current state of variables, 
# and step through your code line by line, observing how values change. 
# finds an error quickly
# gives you a granular view throughout your code 
# set breakpoints to stop the code in different periods to see how it's working
# it better helps you understand the code's behavior 

# built-in Python debugger (pdb)
# IDE comes in with built-in debuggers 
# Python's logging module allows you to record events 
# Print debugging - strategically involves printing debug statements 

# REPRODUCE THE ERROR 
# print(int("This cannot be turned into an integer"))

# TEST YOUR CODE WITH VARIOUS INPUT OR EDGE CASES 
# Keep a debugging journal to isolate solutions 