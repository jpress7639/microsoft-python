# DICTIONARIES 

# a collection of data items
# each item consists of two parts – a key and a value.

# Key characteristics are: 
# Ordered (the insertion order is preserved)
# Mutable (you can easily add new key-value pairs, modify values of existing keys, remove pairs altogether)
# Key-value access - efficient lookup capabilities

# Create a dictionary to store contact information
contacts = {"Alice": "555-1234", "Bob": "555-5678", "Carol": "555-9012"}

# Look up Bob's phone number
bobs_phone = contacts["Bob"]
print(bobs_phone)
# Output: 555-5678

# Add a new contact
contacts["David"] = "555-4321"

# Update Carol's phone number
contacts["Carol"] = "555-2468"

# Remove Alice's contact information
del contacts["Alice"]

# Print updated contacts
print(contacts)

# They are useful for tasks like:

# Storing and retrieving data
# Organizing information 
# Building complex data structures

# Real World Scenarios include:
# Student Gradebook
# Social Media Profiles
# Product Catalog
# Language Translation
# Configuration Files
# Counting Word Frequency

# TASK

product_catalog = {
    "SKU123": {"name": "Widget A", "price": 19.99, "quantity": 50},
    "SKU456": {"name": "Gadget B", "price": 34.95, "quantity": 25},
    "SKU789": {"name": "Gizmo C", "price": 9.99, "quantity": 100}
}

sku_to_find = "SKU123"

print(f"The price of {product_catalog[sku_to_find]['name']} is ${product_catalog[sku_to_find]['price']}")

# ADVANCED DICTIONARY TECHNIQUES

# Nested Dictionary - similar that they store hierarchal data in a single place 
# representing a project with keys like name, due date, but also track tasks like assignee and due date

# product's name is a key, and the product's sales figures for different regions are stored as values with nested dictionaries

# Dictionary Comprehension - creates dictionaries based on ones that already exist
# applies transformation and filters elements quickly for you to use 

# GET Method - allows you to retrieve a value based on their key


# SETS

# SETS - Collections of unique items
# Key characteristics:
# Unordered, the order is not preserved - as long as you can quickly determine if a specific stamp is a part of it
# Mutable - they are dynamic, you can add new items to a set or remove existing ones 
# Unique - defining feature of sets, each item can only appear once

my_set = {1, 2, 3, 3} 

print(my_set)  # Output: {1, 2, 3} - duplicate elements are eliminated 

# you cannot index sets, you can add(), remove(),
#  join elements of two sets union()
# intersection() - elements common to both sets
# difference() - find what's different in the sets

liked_by = {12345, 67890, 98765} # User IDs

# Create a set of favorite programming languages
languages = {"Python", "JavaScript", "Java"}
# Add "C++" to the set
languages.add("C++")
# Try to add "Python" again (it won't be added because it's a duplicate)
languages.add("Python")
print(languages)  # Output: {'Python', 'C++', 'JavaScript', 'Java'} (order may vary)
# Remove "Java"
languages.remove("Java")
# Create another set of languages
web_languages = {"JavaScript", "HTML", "CSS"}
# Find common languages between the two sets
common_languages = languages.intersection(web_languages)
print(common_languages)  # Output: {'JavaScript'}

# CHALLENGE: MAKING A LIST

# Values provided (do not change)
array = [1, 2, 2, 3, 1, 4, 5, 3]

# The following line will need to change to only store unique values
unique_set = set(array) # makes array into a set to define only unique items

# List conversion and print provided (do not change)
unique_array = list(unique_set)
print(unique_array)