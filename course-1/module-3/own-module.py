# Importance of modules 

# Organization 
# - modules offer a systematic way to compartmentalize code into logical units

# Reusability 
# sets of functions, classes, or variables can be readily imported and utilized

# Namespace management 
# when you define a function, class, or variable in a module, it's confined to that module's namespace
# if you have to functions of the same name in different modules, Python will treat then as separate entities

# Maintainability 
# easier to maintain and update

# ANATOMY OF A PYTHON MODULE
# Functions, Classes, and Variables 

# File: geometry_calculations.py

# import math

# def calculate_area_circle(radius):
#     """Calculates the area of a circle given its radius."""
#     return math.pi * radius**2

# def calculate_circumference_circle(radius):
#     """Calculates the circumference of a circle given its radius."""
#     return 2 * math.pi * radius

# class Rectangle:
#     """Represents a rectangle with width and height."""

#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def calculate_area(self):
#         """Calculates the area of the rectangle."""
#         return self.width * self.height

#     def calculate_perimeter(self):
#         """Calculates the perimeter of the rectangle."""
#         return 2 * (self.width + self.height)
    
# File: main.py

# import geometry_calculations

# radius = 5
# area = geometry_calculations.calculate_area_circle(radius)
# circumference = geometry_calculations.calculate_circumference_circle(radius)

# print(f"Area of circle: {area}")
# print(f"Circumference of circle: {circumference}")

# rect = geometry_calculations.Rectangle(4, 6)
# rect_area = rect.calculate_area()
# rect_perimeter = rect.calculate_perimeter()

# print(f"Area of rectangle: {rect_area}")
# print(f"Perimeter of rectangle: {rect_perimeter}")

# math_utils.py
