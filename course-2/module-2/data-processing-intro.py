# Pandas is designed to be user-friendly 
# Specifically for data processing and manipulation

# DataFrame -  It's a two-dimensional table-like structure where data is organized into rows and columns.
# It's a two-dimensional table-like structure where data is organized into rows and columns.

# Three Key Components 

# Data - actual information stored in the DataFrame
# Index - separate structure that identifies each row 
# Column - different variables or features in your dataset 

# Three Common Operations 

# indexing - access specific elements in DataFrame, by row labels, function.lock accessor, integer position function.ilock
# helpful for tasks like retrieving a particular value 

# slicing - allows you to select a range of rows or columns at once
# incredibly useful when you want to extract a subset of your data for further analysis or visualization

# filtering - allows you to select rows based on specific conditions or criteria 
# particularly valuable for data cleaning for outliers or irrelevant data 
# a particular columns value is greater than a certain threshold

# THE IMPORTANCE OF INDEXING IN DATA ANALYSIS 

# Pandas indexing is the cataloging system for DataFrames, 
# allowing you to quickly and accurately pinpoint the data you need.

# By providing direct access to specific subsets of data, indexing empowers you to slice, dice, 
# and reshape your DataFrames to extract meaningful insights and use informed decision-making.

# Two of the most fundamental indexing methods in pandas are .loc and .iloc

# .loc method - this is label-based, uses row and column tlabels to access data 
# e.g. .loc['customer_123', 'purchase_amount'] 
# would retrieve the purchase amount for the customer with the ID 'customer_123'.
# can handle both single labels and slices of labels

# .iloc - it is position based 
# .iloc[5, 2] would access the value in the third column of the sixth row.
# it also supports slicing 

# Boolean indexing - mask-based indexing 
# You create a boolean mask, which is essentially an array of True and False values that 
# indicate which rows or columns meet specific criteria.
# you use this mask to select only the data that corresponds to the True values.


# df[(df['membership_level'] == 'Platinum') & (df['number_of_purchases'] > 10)]

# Boolean indexing is incredibly powerful because it allows you to combine multiple conditions 
# using logical operators like & (and), | (or), and ~ (not). 

# Other indexing methods

# .at or .iat - express lane for individual values
# They are optimized for speed and can be faster than .loc and .iloc when you only need to retrieve or modify a single value.

# Setting and modifying values - lets you modify existing values or assign new values to specific locations within a DataFrame
# df.loc['customer_123', 'membership_level'] = 'Gold' would upgrade customer_123 to a 'Gold' member.
# This capability enables you to perform in-place data changes and updates

# Multi-level indexing - can be used when your data has a natural hierarchy.
# Multi-level indexing in pandas lets you create DataFrames with multiple levels of row or column labels.
# This makes it easier to organize, access, and analyze data with complex structures. 
# It allows you to perform operations like grouping, aggregating, and pivoting data across multiple levels, providing an insightful view of your data.

# query() method - offers a SQL-like syntax for querying DataFrames
# can be an alternative for boolean indexing, especially for complex queries 
# bridges gap between pandas and SQL

# USE CASE: ANALYZING SALES DATA
# You want to calculate the total sales for a specific product, say 'Product A', in the 'North' region. 
# Using .loc, you can achieve this with a single line of code:

# NOTE: total_sales = df.loc[(df['Product'] == 'Product A') & (df['Region'] == 'North')]['Sales'].sum()

# This code snippet combines boolean indexing with .loc to filter the DataFrame based on the product and region, then selects the 'Sales' column and calculates the sum, giving you the total sales for 'Product A' in the 'North' region

# USE CASE: EXTRACTIG CUSTOMER INFORMATION

# You're a customer service representative and need to quickly retrieve the contact details of a customer named 'John Doe'. .loc is your go-to tool here:

# NOTE: customer_info = df.loc[df['Name'] == 'John Doe', ['Email', 'Phone']]

# This simple yet powerful line of code uses .loc to find the row where the 'Name' is 'John Doe' 
# and then selects only the 'Email' and 'Phone' columns, 
# providing you with the necessary customer information in a neatly organized DataFrame. 

# BEST PRACTICES FOR INDEXING:

# Choose the right method:
# if you know the labels, use .loc
# for position-based access, go with .iloc

# when filtering data based on conditions - boolean indexing 
# lightning-fast access to single values - consider .at or .iat

# Chaining for efficiency
# pandas lets you chain multiple indexing operations together, making your code more concise and efficient.

# Clarity over cleverness 
# While pandas offers advanced indexing capabilities, always prioritize code readability. 

# Handle missing data
# issing values (NaN) can create problems in your indexing operations. 
# Use methods like .fillna() or .dropna() to handle them appropriately, ensuring the accuracy and reliability of your analysis. 
# Proper handling of missing data is crucial to avoid unexpected errors and ensure the validity of your results.

# Leverage multi-level indexing - If there's a hierarchal structure 
# It will make your code more organized and easier to interpret, reflecting the natural relationships within your data.

# PRACTICAL SCENARIO

# The Scenario: Your company wants to identify customers who have made more than 5 purchases 
# and live in a specific region, say "California," to offer them an exclusive loyalty discount.

# CONNECTING TO THE CONCEPTS

# DataFrame: Your entire customer order history would be stored in a pandas DataFrame. 
# This DataFrame would have columns like 
# 'CustomerID', 'Region', 'NumberOfPurchases', 'OrderDate', 'Product', etc. 
# It's a perfect way to organize this structured data.

# Filtering: To find customers with more than 5 purchases, you would use filtering. 
# You'd apply a condition to the 'NumberOfPurchases' column (e.g., df[df['NumberOfPurchases'] > 5]). 
# This creates a new DataFrame containing only the rows that meet your criteria.

# .loc for Specific Selection: Once you have those customers, you might want to further narrow down your list to only those in "California." 
# You could use the .loc method to select rows where the 'Region' column equals 'California' 
# (e.g., df.loc[df['Region'] == 'California']). 
# This allows you to precisely select data based on its label (the region name).

# Boolean Indexing: The conditions you use for filtering 
# (like df['NumberOfPurchases'] > 5 or df['Region'] == 'California') 
# are essentially creating a "boolean mask" – a series of True or False values. 
# Pandas uses this mask to select the rows where the condition is True. 
# This is a core part of how filtering works!

# This example shows how you can combine different indexing and filtering techniques to answer specific business questions from a large dataset.



