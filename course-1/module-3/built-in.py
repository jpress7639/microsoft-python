# Built in Function like len(), str(), sorted()
# makes it more self documenting with readily recognizable calls

# import is what you use to bring in the module
# you also can define the things you need instead of importing everything 
# EXAMPLE

from math import sqrt

root = sqrt(25)


# Creates reliability - tested for accuracy and availability

# print() - communicates with the outside world
# len() - returns the number of items in a sequence
# input() - prompts the user to enter data
# type() - determines the data type of variable or value

# int() - converts data into an integer
# float() - converts data into a floating point number, decimal
# str() - coverts data into a text string

def calculator(number_one, number_two, calculation):
    if calculation == "1":
        total = number_one + number_two
        print(f"The total is {total}!")
    elif calculation == "2":
        total = number_one - number_two
        print(f"The total is {total}!")
    elif calculation == "3":
        total = number_one * number_two
        print(f"The total is {total}!")
    else:
        try:
            division = number_one / number_two
        except ZeroDivisionError:
            print("Sorry, you can't divide by zero")
        else:
            print(f"The total is {division}")

print("Do you wanna use the calculator?")
if input().strip().lower() == "yes":
    print("Please choose your first number:")
    number_one = float(input())
    print(f"You have chosen {number_one}")
    print("Please choose your second number:")
    number_two = float(input())
    print(f"You have chosen {number_two}, what would you like to do")
    print("Choose 1 for addition, 2 for subtraction, 3 for multiplication, or 4 for division")
    calculation = input()
    calculator(number_one, number_two, calculation)
else:
    print("Goodbye")

# Further Built-in Modules 

# ADVANTAGES

# Readability
# Efficiency and productivity
# Reliability - 
# Community Development - bug fixes, optimizations by Python developers

# Math, random, and date-time are the most common



