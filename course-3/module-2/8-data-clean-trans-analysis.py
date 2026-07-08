# Cleaning and transforming data for analysis

# Data cleaning and transformation is a critical phase in any data analysis project.
# Data cleaning and transformation:
# the process of fixing or enhancing raw data to make it suitable for analysis

# Common data cleaning tasks
# 1) Handling missing values
# Missing data is a common challenge in real-world datasets - due to entry errors, sensor malfunctions, or incomplete surveys 

# If the missing values are few and randomly scattered throughout your dataset, 
# deleting the corresponding rows or columns may be a reasonable solution

# However, if the missing data is more substantial or patterned, you might consider imputation
# This involves replacing missing values with estimated values based on statistical methods like mean, median, or mode 
# imputation, or even more sophisticated techniques like regression imputation or machine learning models


# 2) Removing duplicates
# can distort your analysis and lead to inaccurate conclusions
# Identifying and removing these duplicates is essential for maintaining data integrity

# Code Example: 
import pandas as pd

# Sample data with duplicate rows
data = {'name': ['Alice', 'Bob', 'Charlie', 'Alice', 'David'], 'age': [25, 30, 35, 25, 40]}
df = pd.DataFrame(data)

# Identify duplicate rows
duplicates = df.duplicated()
print("Duplicate rows:\n", duplicates)

# Remove duplicate rows
df_cleaned = df.drop_duplicates()
print("\nCleaned DataFrame:\n", df_cleaned)

# df.duplicated() function allows focused duplicate detection by specifying relevant columns
# df.drop_duplicates() empowers you to control which duplicates are retained or removed, defaulting to keeping the first unique occurrence.

# Fixing inconcistent Data 
# Dates might be represented in various formats ('YYYY-MM-DD' or 'MM/DD/YYYY'), 
# or categorical variables could contain typos or spelling variations

# e.g. 
import pandas as pd
# Sample data with inconsistent date formats
data = {'date': ['2023-12-31', '12/30/2023', '2023-01-01', '01/02/2023'], 'category': ['Electronics', 'electronics', 'ELECTRONICS', 'Electronic']}
df = pd.DataFrame(data)

# Standardize date formats
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d', errors='coerce')
df['date'] = pd.to_datetime(df['date'], format='%m/%d/%Y', errors='coerce')
df['date'] = df['date'].fillna(pd.to_datetime(df['date'], format='%Y-%m-%d'))

# Standardize categorical values
df['category'] = df['category'].str.lower()
print(df)


# Outlier detection and treatment
# extreme values that deviate significantly from the rest of your data, can either represent genuine anomalies or errors

# Techniques like Z-score or interquartile range (IQR) can help you identify potential outliers. 
# Once identified, you have the flexibility to remove them, transform them using techniques like winsorization or capping, or even retain them, depending on the context of your analysis and your specific goals.

# Common data transformation tasks

# Data type conversion 
# Python's pandas library comes to the rescue here, 
# offering functions like astype() and to_numeric() that make data type conversion a breeze.

# Feature engineering 
# involves creatively crafting new features or transforming existing ones to unlock hidden patterns 
# and boost the performance of machine learning models

# One common technique is creating "dummy variables," which convert categorical data 
# (like colors or categories) into numerical representations that machine learning models can understand

# scaling and normalization: 
# ensures that all numerical features are on a level playing field, 
# preventing any single feature from dominating the model's learning process

# Aggregation is also useful, allowing you to combine data at different levels, 
# such as calculating daily or monthly averages from hourly data.

# Data encoding
# is the process of transforming categorical variables into numerical representations 
# that these algorithms can digest

# Python libraries for data cleaning and transformation

# pandas
# A powerful and versatile library for data analysis
# equipped with a multitude of functions for tackling diverse data cleaning challenges
# provides high-performance data structures like DataFrames, 
# which offer a convenient and intuitive way to organize and manipulate tabular data

# NumPy
# cornerstone library for numerical computing in Python
# provides robust support for arrays and matrices, along with a rich collection of mathematical functions 
# optimized for efficient array operations.

# Scikit-learn
# primarily known as a machine learning library
# offers a valuable set of preprocessing modules specifically designed for data cleaning and transformation
# These modules provide a range of functionalities, including scaling, encoding, and imputation, 
# which are essential steps in preparing your data for machine learning models

# CHALLENGE: Filling missing prices

import pandas as pd
import numpy as np

# Create a DataFrame with missing values
data = {'price': [100, 150, np.nan, 200, np.nan, 180, 120]}
df = pd.DataFrame(data)

# Print the DataFrame before filling missing values
print("Before filling missing values:")
print(df)

# Fill missing values with the median
### YOUR CODE HERE ###
median_price = df['price'].median()
df['price'].fillna(median_price, inplace=True)

# Print the DataFrame after filling missing values
print("\nAfter filling missing values:")
print(df)