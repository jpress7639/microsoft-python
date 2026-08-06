# Metaclasses: The architect of classes in Python

# Metaclasses determine the way classes are created in object-oriented programming. 
# They are a powerful feature of Python that allows developers to customize class creation and behavior.

# Classes define the attributes and methods within the code, 
# while metaclasses controls how those attributes and methods are created and customized.

# There are two types of metaclasses in Python:
# 1) type metaclass: The default metaclass in Python, 
# which is used to create new classes.

# 2) Custom metaclasses: Developers can create their own metaclasses 
# by inheriting from the type metaclass and overriding its methods.

# NOTE: You can create your own custom metaclasses by 
# subclassing the built-in 'type' metaclass and overriding its methods.

# Custom metaclasses can:
# Modify attributes - you can add, remove, or modify attributes 
# of a class during its creation.

# Enforce rules - you can enforce certain rules or constraints on the class, 
# such as requiring certain methods to be implemented.

# Generate code - you can generate code dynamically based on the class definition,
# allowing for more flexible and reusable code.
# Particularly useful in frameworks or domain-specific languages (DSLs) 
# where you want to create classes with specific behaviors or patterns.

# DSLs - Domain-Specific Languages (DSLs) are specialized programming 
# languages designed for a specific domain or problem space.

# For programmers, metaclasses give you control over the class creation process,
# allowing you to tailor classes to meet specific needs to implement design patterns.

# Tips for using metaclasses effectively:
# 1) Use metaclasses sparingly: Metaclasses can add complexity to your code,
# so use them only when necessary. Consider whether a simpler solution,
# such as class decorators or mixins, could achieve the same result.

# 2) Clearly document your metaclasses: Since metaclasses can be complex 
# and may not be familiar to all developers,
# it's important to provide clear documentation and examples of how 
# they work and how to use them.

# 3) Write comprehensive unit tests: Metaclasses can introduce subtle bugs or unexpected behavior,
# so it's important to write comprehensive unit tests to ensure that your metaclasses work as expected.

# Modifying classes on the fly 

# A metaclass may be able to automatically register your view classes, 
# which are responsible for handling requests and returning responses in a web application.

# Metaclasses enable you to modify classes on the fly, 
# allowing you to add or remove attributes and methods dynamically.

# They can also be used to enforce certain rules or constraints on the class,
# such as requiring certain methods to be implemented or ensuring that certain attributes are present.
# This way, metaclasses can help you create more flexible and reusable code,
# allowing you to define classes that can adapt to different situations and requirements.

# Metaclasses can also be used to enforce naming conventions or coding standards,
# ensuring that your code adheres to best practices and is easy to read and maintain.

# Metaclasses can generate code dynamically based on certain conditions or requirements.

# Process on how to use them:
# Step 1: Define a metaclass by subclassing the built-in 'type' 
# metaclass and overriding its methods.

# Example:
class myMetaclass(type):
    def __new__(cls, name, bases, attrs):
        # Modify the class attributes or methods here
        attrs['new_attribute'] = 'This is a new attribute'
        return super().__new__(cls, name, bases, attrs)

# Step 2: Override the __new__ method to customize the class creation process.
# You customize this method to modify the class attributes or methods before the class is created.

# Example:
class myMetaclass(type):
    def __new__(cls, name, bases, attrs):
        # Modify the class attributes or methods here
        attrs['new_attribute'] = 'This is a new attribute'
        return super().__new__(cls, name, bases, attrs)

# def __init__(cls, name, bases, attrs): 
# can also be overridden to customize the class initialization process.

# Step 3: Assign the metaclass to a class by using the 'metaclass' keyword argument in the class definition.
# Example:
class MyClass(metaclass=myMetaclass): # this class will use the myMetaclass metaclass
    # Class attributes and methods go here
    pass
# NOTE: Specific to Python3 - if Python2, you would use __metaclass__ = myMetaclass instead of the metaclass keyword argument.

# Metaprogramming use cases: Beyond the basics 

# In the world of code, you can write programs that can:

# Generate code dynamically based on certain conditions or requirements.
# Adapt to different situations and requirements by modifying classes on the fly.
# Create custom mini-languages or DSLs that are tailored to specific domains or problem spaces.

# Metaprogramming
# Metaprogramming allows you to write code that is more adaptable, reusable, and concise. 
# It can automate repetitive tasks, enforce coding standards, and create more flexible and reusable code.

# Creating DSLs
# A DSL is a specialized programming language designed for a specific domain or problem space.
# Think of SQL for databases, HTML for web pages, or CSS for styling.

# Metaprogramming allows you to create your own DSLs in Python, enabling you to define classes and methods that are tailored to your specific needs.

# Example: 
class Character:
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength

    def reduce_health(self, by):
        self.health -= by
        print(f"{self.name} now has {self.health} health.")

# DSL-like functions for Character creation
def create_character(name, health, strength):
    return Character(name, health, strength)

def create_enemy(name, health, strength):
    return Character(name, health, strength)

# DSL-like function for actions
def when(action_description, action_function):
    print(f"Action: {action_description}")
    action_function()

# Named function for the action
def hero_attack_goblin():
    goblin.reduce_health(by=hero.strength)

# Example usage (DSL-like):
hero = create_character(name="Hero", health=100, strength=50)
goblin = create_enemy(name="Goblin", health=20, strength=10)

when("Hero attacks Goblin", hero_attack_goblin)

# Explanation:
# Character class defines the structure and behavior of characters in the game.

# Creation functions (create_character and create_enemy) 
# provide a DSL-like interface for creating characters and enemies.

# Action function (when) allows you to define actions in a more 
# readable and expressive way, similar to a DSL.

# DSL Example: The code above demonstrates how you can create a 
# DSL-like interface for character creation and actions in a game.

# This code snippet is almost like english, makin it easier for game developers to define game logic.

# Frameworks
# Metaprogramming allows framework developers to create flexible and extensible systems. 

# Introspection
# Automatically connect the dots: A framework like Flask uses introspection 
# to automatically connect routes to view functions based on naming conventions or decorators.

# Provide helpful information: Frameworks can use introspection to provide 
# helpful information to developers, such as listing available routes or generating documentation based on the code structure.

# Dynamic Code
# Frameworks use this to:
# Create things dynamically: An ORM (Object-Relational Mapping) framework can 
# dynamically create database tables based on class definitions, 
# allowing developers to define their data models in code without having to write SQL statements.

# Adapt to different situations: A web framework can dynamically generate HTML 
# templates based on the data being displayed, allowing developers to create dynamic web pages 
# that adapt to different user inputs or data sources.

# Why this matters:
# Flexibility: Metaprogramming allows developers to create more flexible and adaptable code,
# which can be especially useful in frameworks or libraries that need to support a wide range of use cases.

# Extensibility: Metaprogramming allows developers to create more extensible code,
# which can be especially useful in frameworks or libraries that need to support a wide range of use cases.

# Less code, more power: Metaprogramming allows developers to write less code while achieving more functionality,
# which can be especially useful in frameworks or libraries that need to support a wide range of use cases.

# Python offers several features that enable metaprogramming:

# 1) Decorators: Decorators are a way to modify the behavior of functions 
# or classes without changing their source code. 
# They can be used to add functionality, enforce rules, or modify behavior dynamically.

# 2) Metaclasses: Metaclasses allow you to customize class creation and behavior,
# enabling you to modify attributes, enforce rules, or generate code dynamically.

# 3) Monkey patching: Monkey patching is a technique that allows 
# you to modify or extend the behavior of existing classes or modules at runtime.

# Imagine you're writing a program that calculates the area of a rectangle
def calculate_area(length, width): 
    """Calculates the area of a rectangle.""" 
    return length * width

# Now, you want to make sure that the length and width are always positive numbers.
# You can use a decorator to enforce this rule without modifying the original function.
def positive_arguments (func):
    """A decorator that checks if function arguments are positive"""
    def wrapper (*args):
        for arg in args:
            if arg <= 0:
                raise ValueError("Arguments must be positive numbers.") 
        return func(*args)
    return wrapper

@positive_arguments
def calculate_area(length, width):
    """Calculates the area of a rectangle."""
    return length * width

print(calculate_area(5, 3)) # Works fine
print(calculate_area(-2, 4)) # Raises a ValueError

# Another Example: Say you're building a program that needs to create different types of user accounts, 
# each with specific properties

def create_user_class(class_name, attributes):
    """Dynamically creates a user class with given attributes."""
    def __init__(self, **kwargs):
        for attr, value in kwargs.items():
            if attr in attributes:
                setattr(self, attr, value)
            else:
                raise AttributeError(f"Invalid attribute: {attr}")
    class_attrs = {"__init__": __init__}
    for attr in attributes:
        class_attrs[attr] = None
    return type(class_name, (object,), class_attrs) # Using type() to create a new class dynamically

BasicUser = create_user_class("BasicUser", ["username", "email"])
PremiumUser = create_user_class("PremiumUser", ["username", "email", "subscription_level"]) # Corrected line

basic_user = BasicUser(username="Alice", email="alice@example.com")
premium_user = PremiumUser(username="Bob", email="bob@example.com", subscription_level="gold")

print(basic_user.username)  # Output: Alice
print(premium_user.subscription_level)  # Output: gold

# the type() function is used to dynamically create classes 
# based on the provided class name and attributes.