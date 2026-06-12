# 1 - Indentation Errors

x = 0

if x > 5:
    print("x is greater than 5")
else: # corrected indentation
    print("x is less than or equal to 5")

# Solution: Always pay meticulous attention to your indentation. Ensure that statements within loops, conditionals, functions, and classes are properly indented. Most code editors provide visual cues to help you maintain consistent indentation.

# 2 - Variable scope

x = 10

flag = True
if flag is True:
    print(x) # No problem here

# 3 - Immutable Values

value = "Hello"
new_value = "h" + value[1:]
print(new_value)  # Output: hello

# Solution:  When you think you're changing a string, you're actually creating a new one. For example, if you wanted to create a new string with the first letter lowercase, you could do this:  

# 4 - Variable Reassignment

x = 5
if True:
   x = 10  # You've used 'x' again here!
   print(x)  # Output: 10

print(x)  # Output: 10

# Solution: Choose distinct names for your variables to avoid this issue. Some other programming languages have stricter rules and might not allow this, so this happens more commonly in Python than other languages.

# 5 - Overlooking Exceptions

x = 10
y = 0

try:
    result = x / y  # ZeroDivisionError
except ZeroDivisionError:
    print("error: division by Zero") # this catches that zero division error and doesn't break the code

# Imports

# In Python, 'import' is like getting help from another subject. You 'import' code from another file to use in your own program. This can save you time and make your code easier to understand.

# Memory Management

# my_string = ""
# lots_of_as = "a" * 1000000000
# while True:
#   my_string = my_string + lots_of_as  

# Add 1 billion "a" characters - this will never stop and jam up your program

# Memory management is an important part of programming. Even a simple program can cause problems if it doesn't handle memory efficiently.  


