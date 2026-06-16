# DATA CLEANING 

# also referred to as data wrangling or data munging 
# is the critical process of transforming this raw data into a clean, structured, and usable format
# nvolves ensuring that the dataset has clear, consistent, 
# and informative headers for each column, making it easy to understand the meaning of the data

# The Importance of Data Cleaning
# The model would learn from these flaws, leading to inaccurate predictions 
# and potentially disastrous consequences in real-world applications.

# acts as a safeguard against such pitfalls, ensuring that your data is trustworthy 
# and your insights are actionable.

# Clean data also facilitates collaboration and knowledge sharing, 
# as it enables others to easily understand and work with your data.

# MISSING VALUES 
# they create gaps that hinder the complete picture. 

# They can originate from various sources, including data entry errors, 
# equipment malfunctions, or the inherent unavailability of certain information.

# OUTLIERS
# Outliers are data points that significantly deviate from the rest of the dataset.
# While outliers can sometimes represent genuine anomalies or interesting phenomena, 
# they can also distort your statistical measures and lead to misleading results.

# INCONSISTENCIES 
# Inconsistencies can stem from various sources, such as data entry errors, 
# changes in data collection methods, or merging data from different sources.

# Inconsistent headers are one common type of inconsistency. 
#For instance, different datasets might use slightly different names for the same column 
# (e.g., "Customer ID" vs. "Cust_ID"), or have variations in capitalization or spacing.

# STRATEGIES FOR ADDRESSING DATA QUALITY PROBLEMS 

# Removing missing data 
# removing data can introduce bias into the analysis, 
# as the remaining data may no longer be representative of the original dataset

# Imputing missing values: not a typo
# specifically means to assign or substitute values for missing data points
# to strategically fill in these gaps and create a more complete dataset for analysis

# NOTE: This approach is simple but may not be suitable for all situations, especially if the missing values are not missing at random.
# More advanced techniques like regression imputation or multiple imputation can also be used

# Dealing with Outliers 

# It's crucial to carefully evaluate outliers before deciding on a course of action, 
# as they may represent genuine anomalies or valuable insights

# It may be fine to remove them if they're due to errors or extreme/irrelevant cases 
# But they may indicate valuable insights or indicate underlying patterns in the data

# Resolving inconsistencies
# requires a careful examination of your data and identifying the root causes
# Data validation rules and checks can be implemented to prevent inconsistencies 
# from creeping into your data in the first place

# When dealing with inconsistencies in Python, you can leverage powerful tools like pandas.
# The replace() function allows you to systematically replace specific values or patterns in your data, ensuring uniformity

# or more complex transformations, the apply() function provides flexibility to apply custom functions to your data,
# enabling you to tailor your cleaning process to specific needs

# Addressing opposing viewpoints 
# data cleaning is widely acknowledged as a critical step in data analysis, 
# some argue that it can introduce bias or distort the original data

# It's important to recognize these concerns and emphasize that data cleaning should be done judiciously and transparently. 
# The goal is to enhance the quality and usability of the data, not to manipulate it to fit preconceived notions.

