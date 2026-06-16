# DATA UNIVERSE 

# Population - the entire group you're interested in 
# encompasses every individual, object, 
# or entity that shares the characteristics you aim to study

# Sample - carefully selected subset of the population 
# that acts as its representative
# They enable us to conduct research within feasible constraints
# we can gain valuable insights into the population's characteristics

# Variables - distinct attributes 
# capture the variability within our data, 
# providing the raw material for our investigations

# An example of a bookstore - variables could be:
# Customer demographics: Age, gender, location, income level.

# Purchase history: Number of books purchased, genres preferred, average spending.

# Browsing behavior: Time spent on site, pages visited, click-through rates.

# Customer feedback: Ratings, reviews, survey responses.

# TWO MAIN TYPES OF VARIABLES:
# Numerical (Quantitative): represent quantities that can be measured or counted
# Discrete: values that are distinct and separate, can only be whole number values
# Continuous: can take on any value in a range

# Categorical (Qualitative): represent categories or labels that classify data into distinct groups
# Nominal: categories without any inherent order
# Ordinal: Categories with a meaningful order or ranking 
 
# Bring Python into the picture 
# you'll often use powerful libraries like pandas, 
# which provides a highly efficient data structure called a DataFrame.

# Numerical variables - like int or float (for floating-point numbers)
# Categorical variables - like strings or using the category data type in Pandas
# They optimize memory usage, especially when dealing with large datasets with many repeated categories.

import pandas as pd

# Sample data
data = {'age': [25, 30, 35, 40], 
        'gender': ['male', 'female', 'male', 'female'], 
        'income': [50000, 60000, 75000, 55000]}

# Create a DataFrame
df = pd.DataFrame(data)

# Convert 'gender' to a categorical variable
df['gender'] = df['gender'].astype('category')

# Calculate average income
average_income = df['income'].mean()

# Count the number of males and females
gender_counts = df['gender'].value_counts()

print(average_income)
print(gender_counts)

# we create a DataFrame with age (numerical), gender (categorical), 
# and income (numerical) variables. 
# We convert gender to a categorical type, 
# then calculate the average income and count the occurrences of each gender.

# DATA TYPES

# Integers (int): Whole numbers (e.g., -5, 0, 100).
# Floating-Point Numbers (float): Numbers with decimal points (e.g., 3.14, -2.5).
# Strings (str): Sequences of characters (e.g., "Hello, world!", "Python is awesome").
# Booleans (bool): Represent logical values of True or False.
# Lists (list): Ordered collections of items, potentially of different types (e.g., [1, "apple", 3.14]).
# Dictionaries (dict): Collections of key-value pairs, where keys are unique (e.g., {"name": "Alice", "age": 30}).

# DATA GOVERNANCE 
# You are responsible for implementing security measures to protect data from unauthorized access
# You also need to ensure accuracy, completeness, and consistency of data
# You must abide by individual's privacy rights 
