# Declaring Lists

new_list = []

primes = [2, 3, 4, 7, 11, 13]

vowels = ["a", "e", "i", "o", "u"]

coin_flips = [True, False, True, True, False]

# Mixed values

student_record = ["Aashvi", 24, "Computer Science", 3.8, True]

# Getting Started with Lists

grocery_list = ["milk", "hummus", "bread", "cheese", "apples"]
print(grocery_list)

# Indexing - starts with 0 when pointing lists out individually 

# Calculate Length of List by 
print(len(grocery_list))

# A safer way to print our the list is to reference the element at length - 1
print(grocery_list[len(grocery_list) - 1])

# More readable fashion

last_index = len(grocery_list) - 1
print(grocery_list[last_index])

# Slicing - extract a portion of your list

print(grocery_list[0:2])

# List comprehension - concise and powerful way in Python to create new lists on existing iterables (like lists, tuples, strings, ranges, etc.)
# [expression for item in iterable]

# [ ... ]: The square brackets signify that the result will be a new list.
# for item in iterable: This part specifies the iterable you are working with and assigns each element in the iterable to the variable item during each iteration. It's similar to the beginning of a for loop.  

exam_scores = [55, 70, 78, 52, 68]
curve_amount = 10
# Use a list comprehension to create a new list of curved grades
curved_grades = [score + curve_amount for score in exam_scores]
print("Original scores:", exam_scores)
print("Curved scores:", curved_grades)

#Common Errors include IndexError - when you try to access an index that doesn't exist
# ValueError - when you ty to use a list method with a value that doesn't make sense. 
# Example: remove() an item that's not on the list

#TWO DIMENSIONAL LISTS

grid = [

	  [1, 2, 3],

	  [4, 5, 6],

	  [7, 8, 9]

	]

# To access an individual number in the grid, you would use two indices. For example, to print the number 6 (second row, third column) you could use the following code:


print(grid[1][2])

