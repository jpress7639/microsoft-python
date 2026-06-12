# Classes are the cornerstone in OOP

# Objects
# They represent real-world entities or abstract concepts within your code. Each object is like a self-contained unit with its own data and the ability to perform actions.

# Classes
# They serve as blueprints or templates for creating objects. Classes define the common characteristics (attributes) and behaviors (methods) that all objects of that class share. 

class BankAccount:
    def __init__(self, balance):
        self._balance = balance  # Private attribute

    def deposit(self, amount):
        self._balance += amount

    def get_balance(self):
        return self._balance


from abc import ABC, abstractmethod

class Animal(ABC):  # Abstract base class
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):  # Concrete subclass
    def make_sound(self):
        return "Bark!"
    
# Car 

class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.fuel_level = 100  # Initial fuel level

# Methods (behaviors)
# Methods are functions defined within the class that operate on the object's data. They represent the actions an object can take. For a Car, methods might include start_engine(), accelerate(), brake(), and refuel()       

class Car:
    # ... (attributes)

    def start_engine(self):
        print(f"The {self.year} {self.make} {self.model}'s engine roars to life!")

    def accelerate(self):
        print(f"The {self.color} {self.make} {self.model} picks up speed!")

    def brake(self):
        print(f"The {self.make} {self.model} comes to a smooth stop.")

# The __init__ method: A special constructor

# The __init__ method, often called the constructor, 
# is a special method that Python automatically calls when you create a new object of your class. 
# Its primary role is to initialize the object's attributes with appropriate values. 
# This ensures that every new object starts with a valid state.

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"Woof! My name is {self.name} and I'm a {self.breed}")

my_milo = Dog("Milo", "Shi-Poo")

    







