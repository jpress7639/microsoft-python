# three core conditional statements: if, elif, else
# conditional statements are also the center of game logic

# if statements can detect a file that doesn't exist in a program 

# Pricing Rules at Movie Theater 

children = 8
adults = 12
seniors = 10


age = int(input("What is your age:"))

if age < 12:
    print("The price is $",children)
elif age >= 65:
    print("The price is $",seniors)
else:
    print("You're a loser. The price is $",adults)

# Two of the most fundamental tools in the control flow toolbox are conditional statements and loops.
# without control flow, Python programs wouldn't be able to do much more
# In Python, the cornerstone of conditional statements is the if statement.

temperature = 22  # Example temperature

if temperature < 20:
    print("It might be cold! You might need a jacket.")
else:
    print("It's warm! Enjoy the sunshine.")


temperature = 15  # Let's assume the temperature is 15 degrees Celsius

if temperature < 10:
    print("Wear a jacket! It's cold out there.")
elif 10 <= temperature < 20:
    print("A light sweater should be fine. It's a bit chilly.")
elif 20 <= temperature < 30:
    print("Enjoy the pleasant weather! No need for extra layers.")
else:
    print("It's hot! Stay hydrated and wear sunscreen.")

#for loops are perfect when you know the desired repetition count in advance.

# Example: Print numbers from 1 to 5
for i in range(1, 6):
    print(i)

# while loops, on the other hand, continue as long as a condition holds true.

# Example: Keep asking for input until the user enters "quit"
user_input = ""
while user_input != "quit":
    user_input = input("Enter something (or 'quit' to exit): ")
    print("You entered:", user_input)

# CODING CHALLENGE

numbers = [3, 9, 1, 10, 5, 2, 8]

for number in numbers:
    if number % 2 == 0:
        print(number, " is even")
    else:
        print(number, " is odd")