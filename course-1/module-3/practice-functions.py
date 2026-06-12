# The starting code has a call to a function, happy_birthday, that you will be writing.

def happy_birthday(age, name):
    print(f"Happy Birthday  {name} and congratulations on turning {age} years old!")


# Begin by writing the function definition for a get_lucky_number function. Remember, this function should not require any input parameters (one line of code). Avoid type hints for the return value.

import random

# Insert code here
def get_lucky_number():
  lucky_num = random.randint(1,100)
  # Insert code here
  return lucky_num

# Get a lucky number between 1 and 100
lucky_number = get_lucky_number()

print("Your lucky number is:", lucky_number)

# In this example, you will write a function to calculate the discounted total based on whether a user is a member of the discount club or not.

# Insert code here
def calc_sale_price(amount, member):
	if member:
		# Members receive a 15% discount (0.15)
		amount = amount - (amount * 0.15)
	else:
		# Non-members get a 5% discount (0.05)
		amount = amount - (amount * 0.05)

	# Round amount to two decimal places
	# Save back in the amount variable
	# Insert code here
	amount = round(amount, 2)
	# Return amount to the main program
	# Insert code here
	return amount
# Example price (already provided)
full_price = 150.50

# Call function for members
member_price = calc_sale_price(full_price, True)
print("Member price:",member_price)

# Call function for non-members
non_member_price = calc_sale_price(full_price, False)
print("Non-member price:",non_member_price)

# SCOPE

def display_color_works():
  shirt_color = "Pink"
  print("First shirt color is:", shirt_color)
  
def display_color_failure():
  # Try to access 'color' directly (this will cause an error)
    try:
        print("Your shirt color is:", shirt_color)
    except NameError:
        print("Variable is not found!")

# The shirt_color variable is in scope in this function
display_color_works()

# The shirt_color variable is not in scope in this function
# display_color_failure()

# Using functions from another module

