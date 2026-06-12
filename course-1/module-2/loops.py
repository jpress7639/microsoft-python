for i in range(1, 11):
# this stops before 11
# don't need to define i in this case :)
    print(i)

# A for loop iterates over a sequence, such as a list, tuple, or string, executing a code block for each item in the sequence. 

valid_input = False
while not valid_input:
  user_input = int(input("Please enter a number greater than 0: "))
  if user_input > 0:
    valid_input = True
  else:
    print("Invalid input. Please try again.")

# A while loop, conversely, executes a code block as long as a specified condition remains true. 

# the most common conditional is the if/else statement 

player_score = 80

if player_score > 100:
  print("Congratulations! You scored over 100 points.")
else:
  print("Keep trying to beat your high score!")

# real world applications involve data analysis, web development, game development, and machine learning

# keep loops concise (avoided nesting loops too deeply, break it into more manageable chunks), use meaningful conditions, consider alternative constructs, avoid infinite loops

import random
# this is a standard library import from Python 
secret_number = 5

guess = 0

while guess != secret_number:
  guess = random.randint(1, 10)
  print("Guessing:",guess)

print("I guessed the right number! It was", secret_number)

# range(stop) begins at 0 and stops before the stop value
# range (start, stop) begins at start number and ends before stop
# range(start, stop, step) step is the increment it increases

number = 1
while number <= 10:
    print(number) 
    number = number + 1

option = 0
while option != 4:
    print("1. Perform action 1")
    print("2. Perform action 2")
    print("3. Perform action 3")
    print("4. Quit")

# While loops: Execute as long as a specified condition remains true. These are often used to run until a condition is met.  
# Also notice the variable option was assigned a value of 0. As long as it is not 4 initially, the loop will run at least once.  

# list is a data structure that stores a collection of items

fruits = ["apple", "banana", "cherry"]
# how to take first input in list
first_fruit = fruits[0]
fruits.append("date")
# how to compute the amount of elements
fruit_length = len(fruits)
print(first_fruit)
print(fruit_length)

students = ["Alice", "Bob", "Charlie"]
for student in students:
    print("Hello,", student)

# you can use an i loop - but it's more complicated

students = ["Alice", "Bob", "Charlie"]
for i in range(0,len(students)):
    print("Hello,", students[i])

# harness loops for iteration

import random
roll = 0
while roll != 6:
    roll = random.randint(1, 6) 
    print("You rolled a", roll)

# range() function generates a sequence of numbers
# the for loop iterates over the sequence, accumulating the sum in a total variable

total = 0
for number in range(1, 101): 
    total += number
    print("The sum is:", total)

# while loops can handle more complex tasks like filtering numbers from a list

numbers = [1, 2, 3, 4, 5]
index = 0

while index < len(numbers):
    if numbers[index] % 2 == 0:
        print(numbers[index])
    index += 1

# NESTED LOOPS: AMPLIFYING ITERATION

for i in range(1, 11):
    for j in range(1, 11):
        print(i, "*", j, "=", i * j, end="\t") # Print the equation
    print() # Move to the next line after each row

# The outer loop iterates over the rows, 
# while the inner loop, nested within, handles the columns.    