# LISTS
# . Within a single list, you can store an assorted collection of items, 
# whether they are numbers, strings, other lists, or even a mix of different data types.
# when order matters 

# Key characteristics: Order preserved, mutable (you can modify the contents), indexable (each item in a list has a unique position or index)

my_list = [1, 2.1, "hello", [3, 4]]

print(my_list[0])

# Accessing ^
# Extracting subsets with slicing (the end index is not inclusive) [1:3], would only get 1 + 2


# extending your list to add multiple items extend() versus append() - only one

tasks = ["Take a nap"]

new_tasks = ["Go for a walk", "Read a book"]

tasks.extend(new_tasks)

# Adding and removing: Need to add another item to your shopping list? 
# No problem, just use the .append() method to tack it onto the end. 
# Forgot something? .remove() (the first occurence of the item) it or .pop() (removes and returns the last item in the list) it off the list.

# Slicing and replacing: Want just the first three items? 
# Slice the list like this: my_list[:3]. 

# Need to change the middle items? 
# Slice and replace: my_list[2:5] = [new_item1, new_item2].

# Lists have built-in methods to sort themselves (my_list.sort()) 
# and to find the index of a specific item (my_list.index(item)).

# del statement:
# Deletes objects, variables, or specific elements within mutable data structures like lists and dictionaries.



# Flexible data types:
# Lists can hold values of any data type, even lists or dictionaries. 
# This allows for complex and nested data structures.

shopping_list = ["apples", "bananas", "milk"]  # List for items
item_quantities = {"apples": 3, "bananas": 1}  # Dictionary for quantities

# User adds an item
shopping_list.append("eggs")
item_quantities["eggs"] = 12 

# User increases the quantity of bananas
item_quantities["bananas"] += 2

# User removes apples
shopping_list.remove("apples")
del item_quantities["apples"]

# Print updated list and dictionary
print(shopping_list)
print(item_quantities)



# Tuples - lists but they are immutable - you cannot change contents once created 

my_tuple = (10, 20, "python")

# You can still access individual elements with slicing or indexing 
# an example is like geographic coordinates

coordinates = (37.7749, -122.4194)  # Latitude, longitude of San Francisco
birth_date = (1990, 12, 25)       # Year, month, day

# Sets
unique_colors = {"red", "green", "blue"}
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers)    # Removes duplicates

coordinates = (37.7749, -122.4194)  # Latitude and longitude of San Francisco

# Need to remove duplicates from a list? 
# Convert it into a set, and Python will automatically take care of it. 
# Sets are also great for checking membership – asking, "Is this item in my collection?"



# SETS - Collections of unique items
# track things like unique users, unique words in a document

my_set = {1, 2, 3, 3} 

print(my_set)  # Output: {1, 2, 3} - duplicate elements are eliminated 

# you cannot index sets, you can add(), remove(),
#  join elements of two sets union()
# intersection() - elements common to both sets
# difference() - find what's different in the sets

liked_by = {12345, 67890, 98765} # User IDs

# DICTIONARIES - most versatile and widely used in data structures
# labeled storange boxes
# a powerful way to store and organize info by associating each piece of data within a key 

my_dict = {"name": "Alice", "age": 30, "city": "New York"}

# access valyes like this my_dict["age"] - returns 30

# Common Operations 
# get() - safely retrieve a value by its key 
# items() - get all key-value pairs as a list 
# keys() - gets all keys in dictionary 
# values() - get all values in the dictionary 
# update() - merge one dictionary into an existing one

products = {

		"P101": {"name": "Laptop", "price": 999.99},

		"P102": {"name": "Smartphone", "price": 599.99}

		}

print(products["P101"]["price"])


# Challenge 

shopping_cart = []

shopping_cart.append("apple")
shopping_cart.append("banana")
shopping_cart.append("milk")

print("Shopping Cart:")

for item in shopping_cart:
    print(item)


# WHICH IS THE RIGHT ONE? Ask these questions

# UNIQUE VALUES, ORDER
# WILL YOU NEED TO MODIFY?
# HOW CRUCIAL IS SPEED FOR YOUR APPLICATION?

# WHAT KIND OF INFORMATION ARE YOU WORKING WITH? 
# ARE THERE RELATIONSHIPS OR HIERARCHIES?

# OPERATIONS: WHAT ACTIONS WILL YOU BE PERFORMING? 
# PERFORMANCE REQUIREMENTS: HOW LARGE IS YOUR DATASET? WILL YOU NEED TO BE QUICK?
# MEMORY: ARE YOU WORKING IN A LOW MEMORY ENVIRONMENT?
# READABILITY: HOW EASY DO YOU NEED THIS TO BE READABLE FOR YOU OR OTHERS?

# E-COMMERCE

# personalized product recommendations to enhance customer engagement
# They chose dictionaries - tailored shopping experience 
# Contained User ID, email address
# Increased Customer Engagement and Sales 

# SOCIAL MEDIA

# Trending topics in real time, based on hashtags in user posts
# Lists were used to store incoming posts in chronological order
# Sets were then used to filter out duplicate hashtags, counted only once 
# System continuously processed posts, unique hashtags were then counted and ranked to determine the trending topics

# FRAUD DETECTION

# They chose list - maintaining chronological order of transactions 
# Stored historical transaction data 
# Dictionaries were able to look up current transactions against established customer profiles 
# Any significant deviations triggered alerts for potential fraud

# KEY FACTORS IN DATA STRUCTURE SELECTION

# 1) WHAT TYPE OF DATA ARE YOU WORKING WITH?

# ORDERED - Lists and Tuples are good choices 
# UNORDERED - Sets are useful

# MUTABLE - Lists and dictionaries are mutable
# IMMUTABLE - Tuples are immutable

# 2) WHAT OPERATIONS WILL YOU BE PERFORMING MOST FREQUENTLY?

# ADDING/REMOVING - Lists are great for adding/removing at the end, 
# sets and dictionaries provide fast addition/removal for unique items

# SEARCHING - Dictionaries excel for fast lookups by key, sets are efficient for checking membership

# SORTING - Lists for a specific order can support efficient sorting algorithms

# 3) HOW MUCH DATA ARE YOU DEALING WITH?
# SMALL DATASETS - performance differences may not be noticeable
# LARGE DATASETS - performance is crucial, search in a list could be much slower than searching in a dictionary 

# 4) WHAT ARE THE TIME AND SPACE COMPLEXITY REQUIREMENTS?
# Time complexity: How does the time it takes to perform an operation scale with the size of the dataset?
# Searching in a sorted list takes a logarithmic time (O(log n)) while unsorted takes linear (O(n))

# Space Complexity: How much memory does the data structure consume as the dataset grows?


import timeit

# List lookup
list_data = list(range(100000))
lookup_value = 99999
list_time = timeit.timeit(lambda: lookup_value in list_data, number=1000)

# Dictionary lookup
dict_data = {i: i for i in range(100000)}
dict_time = timeit.timeit(lambda: lookup_value in dict_data, number=1000)

print("List lookup time:", list_time)
print("Dictionary lookup time:", dict_time)

# In this example, you'll likely see that dictionary lookup is significantly faster than list lookup, especially for large datasets.)

# ALTERNATIVE STRUCTURES

# 1) DEQUE (DOUBLE-ENDED QUEUE)
# WHEN TO USE - Implementing queues and stacks where you have to add/remove from BOTH ENDS
# Simulating real-world scenarios like lines, decks of cards, or undo/redo functionality

# 2) HEAPQ (PRIORITY QUEUE)
# WHEN TO USE - Task scheduling, prioritizing urgency or importance
# Dijstra's algorithm for finding the shortest path in a graph
# Implementing priority-based systems

# 3) COLLECTIONS.COUNTER
# Takes an iterable (list/string) and counts the occurences of each unique item
# Word frequency in text, occurence of items in a list, finding the most common elements in a dataset

from collections import deque, Counter

# Deque example
queue = deque()
queue.append("task1")
queue.append("task2")
print(queue.popleft())  # Output: task1

# Counter example
text = "This is a sample text with some repeated words words"
word_counts = Counter(text.split())
print(word_counts)  # Output: Counter({'words': 2, 'This': 1, 'is': 1, ...})