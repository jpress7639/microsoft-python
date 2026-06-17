# Missing data can cause all sorts of trouble in your Python programs, 
# unexpected errors ​in your code, for instance, or incorrect calculations of averages and sums.

# Carefully examine your data and its documentation 

# Best approach depends on:

# How much data is missing - is it at random? is it a slew of questions not answered?
# The type of data that is missing 
# The purpose of your analysis 

# APPROACHES
# Deletion - the most common (dropna in Pandas) - when the amount of data is small

# Imputation - filling in the data with estimated or calculated value
# Can be the mean, median, or mode to replace - each with strengths and weaknesses 

# You can create a separate a category for missing values - when they represent a missing category 

# Machine-learning algorithms - can handle missing data directory without the need for explicit imputation 

# HANDLING DUPLICATE VALUES 

# Entering the same customer twice creates duplicate entries 

# A duplicate value is simply a data ​point that is identical to another data point in your data set.
# this can be an entire row in your spreadsheet or a duplicate values in a single column 

# Can be from simple human error - they input the values twice 
# Sometimes arise from combining data from different sources 
# Occasionally, bugs are occur, creating duplicate entries 

# HOW TO HANDLE 

# Pandas - one common way to drop duplicates

import pandas as pd # importing Pandas
data = pd.read_csv('your_data.csv') # loading data into the program 

duplicates = data.duplicated() # uses the duplicated function to find any duplicate rows 
print(duplicates)

duplicate_rows = data[data.duplicated()] # we want to see the actual rows and print them 
print(duplicate_rows)

data = data.drop_duplicate() # removes the duplicate rows from the DataFrame, keeping the unique ones

# You can customize the drop duplicate function

# Keep the last occurence of each duplicate 
data = data.drop_duplicates(keep='last')

# Keep the first occurrence of each duplicate (this is the default)
data = data.drop_duplicates(keep='first')

# Remove all duplicate rows 
data = data.drop_duplicates(keep=False)

# COMMON CAUSES OF MISSING DATA 

# Human error is an unavoidable aspect of any data collection process, often resulting in missing data. 

# To mitigate such errors, implementing data validation techniques during the data collection 
# and entry process is crucial.

# This could involve setting restrictions on the type of data allowed in certain fields, 
# providing clear instructions to those collecting the data, 
# and using double-entry methods where two individuals independently enter the same data to cross-check for accuracy.

# In scenarios where data is collected through automated systems, 
# such as sensors or monitoring devices, technical issues can lead to periods of missing data. 

# Regular maintenance and calibration of equipment are paramount to minimizing the risk of malfunctions. 
# incorporating redundancy into your data collection system by using multiple sensors 
# to monitor the same parameters can provide backup data in case of individual sensor failures

# Surveys and questionnaires, while valuable tools for gathering data, often face the challenge of non-response. 
# Participants may choose not to answer certain questions, especially those that are sensitive or personal, 
# or they may drop out of the survey altogether.

# This can introduce bias into your dataset as those who respond may not be representative of the entire population, 
# potentially leading to misleading conclusions.

# Careful survey design is key to maximizing participation and minimizing non-response. 
# Clear and concise questions, user-friendly interfaces, and assurances of confidentiality can encourage respondents to complete the survey. 

# offering incentives or sending reminders can further boost participation rates.

# DATA INTEGRATION AND MERGING ISSUES 

# Combining data from different systems can be a complex process. 
# Incompatibilities in data formats, identifiers, or definitions can result in missing values during the integration process. 

# Plan thoroughly and profile your data before integrating data from different sources.
# Understanding the structure, quality, and potential inconsistencies in each dataset enables you to develop effective data cleaning and transformation strategies.

# regulations like GDPR, organizations may opt to delete or anonymize personally identifiable information 
# or sensitive data to protect individuals' rights

# NOTE: Techniques like data masking can help protect sensitive information while 
# preserving the overall structure and patterns within data. 

# exploring synthetic data generation or differential privacy methods can 
# provide alternatives for analysis while safeguarding individual privacy.

# ADDRESSING MISSING DATA WITH PANDAS

# initial step in managing missing data is to pinpoint its location within your dataset.

# pandas provides convenient functions like isnull() and notnull() that create boolean masks,
# highlighting the presence or absence of missing values in your DataFrame. 

# particularly when the amount of missing data is small and the missing items appear random
# pandas' dropna() function offers flexibility in removing rows or columns based on various criteria, 
# such as the number or proportion of missing values they contain.

# Outliers - pandas functions like describe() and quantile(), along with visualization tools like box plots, 
# enable you to identify outliers effectively

# Data often arrives in different formats
# ensuring consistency in data types is crucial for smooth analysis.

# Data type conversions are simplified in pandas with functions like astype(), to_numeric(), and to_datetime().
# These functions allow you to convert columns to the appropriate data types, handling potential errors or inconsistencies in the process.

# Exploratory data analysis (EDA) is a vital phase in any data analysis project, 
# and pandas provides an array of tools to facilitate this process.

# Descriptive statistics, aggregations, and visualizations help you gain a deeper understanding of your data

import pandas as pd
import numpy as np

# Sample DataFrame with missing values
data = {'Name': ['Alice', 'Bob', np.nan, 'David'], 
        'Age': [25, 30, np.nan, 35], 
        'City': ['New York', np.nan, 'London', 'Paris']}
df = pd.DataFrame(data)

# 1. Identifying missing values
print("Missing value counts per column:\n", df.isnull().sum())

# 2. Removing missing values (dropna)
df_dropped = df.dropna()
print("\nDataFrame after dropping rows with any missing value:\n", df_dropped)

# 3. Imputing with mean (for numerical columns)
df_filled_mean = df.fillna(df.mean(numeric_only=True))
print("\nDataFrame after filling missing 'Age' with mean:\n", df_filled_mean)

# 3. Imputing with median (for numerical columns)
df_filled_median = df.fillna(df.median(numeric_only=True))
print("\nDataFrame after filling missing 'Age' with median:\n", df_filled_median)

# 4. Handling outliers (demonstration with 'Age')
# Assuming we identify 40 as an outlier based on domain knowledge or visualization
df['Age_capped'] = df['Age'].clip(upper=40)  # Cap values at 40
print("\nDataFrame with 'Age' capped at 40:\n", df)

# 5. Data type conversion
df['Age'] = pd.to_numeric(df['Age'], errors='coerce')  # Convert to numeric, handling errors
print("\nData types after conversion:\n", df.dtypes)

# 6. Exploratory Data Analysis
print("\nDescriptive statistics:\n", df.describe())

# Group by and aggregate
grouped_data = df.groupby('City')['Age'].mean()
print("\nAverage Age by City:\n", grouped_data)

# used np.nan, a NumPy value representing "not a number", to simulate those missing values. 

# proceed to identify those missing values using isnull().sum() 
# and demonstrate how to remove rows with missing data using dropna()

# two common imputation techniques: 
# filling missing numerical values with the mean and the median using fillna() and mean()/median().

# simulate handling an outlier in the 'Age' column by capping values at 40 using clip() 
# and convert the 'Age' column to a numeric type, handling potential errors using to_numeric()

# we perform some basic EDA by calculating descriptive statistics with describe() 
# and grouping the data by 'City' to compute the average 'Age' using groupby()and mean().

