# PANDAS CHEAT SHEET

# Dictionaries 
# are ideal for structured data, where keys represent column names and values correspond to column data, 
# streamlining DataFrame creation from pre-organized data. 

import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 28]}

df = pd.DataFrame(data)

# Lists of Lists 
# are convenient for tabular data. 
# Each inner list represents a row, and an optional columns argument specifies column names, 
# ensuring clarity and interpretability. 
# This method is handy when you have data organized in a list-of-lists format, 
# perhaps after reading data from a text file or scraping a website.

data = [['Alice', 25], ['Bob', 30], ['Charlie', 28]]

df = pd.DataFrame(data, columns=['Name', 'Age'])

# CSV files 
# give pandas the ability to seamlessly load data from them into DataFrames using the read_csv function. 
# This function handles parsing and structuring. 

df = pd.read_csv('data.csv')

# pandas also provides similar functions like read_excel, read_json, and read_sql 
# for importing data from other popular formats, making it adaptable to your specific data sources.

# Inspecting a DataFrame 

# df.head() - displays the first few rows (default 5)
# df.tail() - displays the last few rows (default 5)
# df.shape() - returns a tuple representing the dimensions of the DataFrame 
# df.info() - creates a concise summary of the DataFrame, encompassing column names, data types

# df.describe() - computes descriptive statistics for numeral columns, 
# offering insights into data distribution and central tendencies 
# includes metrics like count, mean, standard deviation, minimum, maximum, and quartiles, 
# which help you understand the characteristics of your numerical data.

# Selecting and Filtering Data 

# Single column selection - retrieves a single column by its name 

df['Age']

# Multiple column selection - extracts multiple columns by passing a list of column names within double square brackets

df[['Name', 'Age']]

# df.loc[] employs label-based indexing, allowing you to select rows based on their index labels, which can be strings, integers, or even dates. 

df.loc[0]       # Select the row with index label 0

# df.iloc[] leverages integer-based indexing, 
# enabling row selection based on their integer positions (starting from 0). 

df.iloc[0]      # Select the first row (position 0)
df.iloc[:3]    # extract the first three rows

# Filtering Data 
# is done with Boolean indexing and serves as a powerful tool for filtering rows based on specific conditions.
# It involves creating a boolean mask (a Series of True/False values) by applying comparison operators or logical conditions to one or more columns

df[df['Age'] > 25]  # Filter rows where 'Age' is greater than 25

# Querying data - complexing filtering scenarios involving multiple conditions or intricate logic

df.query('Age > 25 and Name == "Bob"') # Filter rows based on multiple conditions

# Handling Missing Data - missing values, denoted as NaN, are common to find

# df.isnull() - generates a boolean DataFrame mirroring the original, where True indicates a missing value and False represents a non-missing value.
# provides a comprehensive overview, quickly asses the extent of what is misisng 

# df['Age'].isnull() - applies the same logic to a specific column, highlighting missing values in that column 

# df.dropna() - removes rows containing any missing values 
# when missing values are relatively sparse 
# and their removal doesn't significantly impact the representativeness of the data

# df.fillna() - replaces missing values with a specified value (e.g., 0), a simple imputation technique suitable for certain cases.
# it may introduce bias 

# df['Age'].fillna(df['Age'].mean(), inplace=True)
# more sophisticated approach, imputing missing values in a column with its mean
#  The inplace=True argument modifies the DataFrame directly, conserving memory
# often preferred when missing values are assumed to be randomly distributed 
# and you want to maintain the overall statistical properties of the data



