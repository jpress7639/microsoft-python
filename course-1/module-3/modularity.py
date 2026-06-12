# Benefits Modularity adds to your code 

# Modular code enhances readability, 
# making it easier for you and others to understand. 
# Instead of navigating complicated instructions, 
# your functions have a descriptive name that clearly defines its purpose.

# Functions can be reused throughout your code. This saves development time and reduces errors.
# Modular code makes it easier to isolate and fix errors. You can focus on the specific function that's causing the problem.

def calculate_area(width=1, height=1): # width and height are set to defaults
    area = width * height
    return area

result = calculate_area() 
print(result)  # Output: 1

result = calculate_area(5, 3)  # versatitlity remains in tact 
print(result)  # Output: 15

# BE CAREFUL when using mutable arguments like dictionaries or lists as defaults 

# Use none as a default value for mutable arguments 

def greet(name, greeting="Hello"):
    print(greeting, name)

greet("Alice")  # Output: Hello Alice

greet("Bob", "Good morning")  # Output: Good morning Bob
greet("Carol", "Howdy")      # Output: Howdy Carol

# Keyword Arguments 
# Variable Number of Arguments (*args and **kwargs) 

# *args - to collect positional arguments into a tuple 
# **kwargs - to collect keyword arguments into a dictionary

def flexible_function(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

flexible_function(1, 2, 3, name="Alice", age=30)

# 1, 2, 3, for positional arguments 
# Alice and age=30 for keyword arguments

def create_user_profile(name, age, occupation="Student", interests=None): # Use None as default
    """
    Creates a user profile with optional interests.

    Args:
        name (str): The user's name (required).
        age (int): The user's age (required).
        occupation (str, optional): The user's occupation (defaults to "Student").
        interests (list, optional): A list of the user's interests (defaults to None).
    """
    if interests is None:  # Initialize if None
        interests = [] 

    profile = {
        "name": name,
        "age": age,
        "occupation": occupation,
        "interests": interests
    }

    return profile

# Usage
user1 = create_user_profile("Alice", 25, "Software Engineer", ["Coding", "Hiking"])
user2 = create_user_profile("Bob", 18)  # Uses default occupation and no interests
user3 = create_user_profile("Carol", 30, interests=["Gardening", "Reading"])

print(user1)
print(user2)
print(user3)


# PRACTICE - MAKE SANDWICH 

def make_sandwich(bread_type, filling, cheese=None, toasted=False):

    if cheese != None and toasted == True:
        sandwich = (f"Making a toasted {bread_type} sandwich with {filling} and {cheese} cheese.")
    elif cheese != None and toasted == False:
        sandwich = (f"Making a {bread_type} sandwich with {filling} and {cheese} cheese.")
    elif cheese == None and toasted == True:
        sandwich = (f"Making a toasted {bread_type} sandwich with {filling}.")
    else:
        sandwich = (f"Making a {bread_type} sandwich with {filling}.")

    return sandwich

make_sandwich("wheat", "turkey", "cheddar", True)
make_sandwich("rye", "ham")