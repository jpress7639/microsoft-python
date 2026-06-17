# DATA MANIPULATION TACTICS

# NOTE: Data cleaning and preprocessing are often the first and most important steps in any data manipulation workflow.

# DataFrames provide a tabular representation of data, similar to spreadsheets or SQL tables
# Series - represent a single column of data, allowing for efficient operations on individual data attributes.

# pandas provides functions like (fillna) to fill missing values with specified values like the mean or median of the column.
# Or you can use (dropna) to remove rows or columns containing missing values.

# Inconsistencies may occur in various forms. 
# These include things like different date formats, varying units of measurement, or inconsistent capitalization in the data.

# pandas allows you to convert data types using astype, making all values in a column the same type.

# Duplicate entries 
# Duplicate entries can skew analysis results and lead to inaccurate conclusions. 
# pandas' drop_duplicates function quickly identifies and removes duplicate rows

# Outliers are extreme values that are different from the rest of the data. 
# pandas provides statistical functions and visualization tools to help you with outlier detection.

# DATA RESHAPING AND TRANSFORMATION 

# Data reshaping and transformation involve rearranging and modifying the structure of your data to conduct analysis or meet specific requirements. 
# pivot_table function in pandas allows you to create pivot tables, summarizing data based on one or more index columns. 

# melt function unpivots a DataFrame, converting columns into rows.
# This can be helpful when you have data in a wide format, where each column represents a different attribute or measurement

# stack and unstack functions are used to convert between wide and long formats
# Stacking converts column labels into row labels
# Unstacking performs the reverse, rows into column labels

# FILERING AND SUBSETTING 

# loc and iloc indexers give you ways to access specific rows and columns by label or position.
# loc is used for label-based indexing, allowing you to select rows and columns 
# iloc is used for position-based indexing - select rows and columns based on their integer positions

# query method - provides a concise way to filter data using SQL-like syntax

# AGGREGATION AND SUMMARIZATION

# involve condensing your data by applying statistical functions to groups of rows or columns 
# groupby function in pandas based on one or more columns, creating a GroupBy object. 
# You can then apply aggregation functions like sum, mean, count, min, max, and others to each group, generating summary statistics or aggregated values.

# pandas allows you to define custom aggregation functions using lambda functions or user-defined functions.

# JOINING AND MERGING 

# merge function in pandas combines DataFrames based on common columns or indices. 
# It supports various types of joins, including inner joins, outer joins, left joins, and right joins, allowing you to control how the data is combined and which rows are included in the resulting DataFrame.

# join function is similar to merge, but it combines DataFrames based on their indices.
# It is particularly useful when you have DataFrames with hierarchical indices or when you want to combine DataFrames based on their row labels.

# ADVANCED TECHNIQUE 

# Time series analysis can be used if you're working with data that has a temporal component like stock prices, sales data, sensor readings.
# pandas provides specialized tools for handling time series data, including date/time indexing, resampling, and rolling window calculations.

# Resampling lets you change the frequency of your time series data, for example, converting daily data to monthly data

# Date/time indexing allows you to efficiently access and manipulate data based on timestamps


# Text processing and natural language processing (NLP) 
# can be used if your data includes textual information like customer reviews, social media posts, or product descriptions. 

# Python libraries like NLTK and spaCy offer tools for tasks like tokenization, or breaking text into words or phrases

# stemming, which is reducing words to their root form.

# lemmatization or reducing words to their base or dictionary form or sentiment analysis which determines the emotional tone of text. 

# topic modeling lets you identify underlying themes in a collection of documents.

# Machine learning integration is used once you've cleaned, transformed, and explored your data. 
# You can use it to train machine learning models for tasks like prediction, classification, and clustering. 

# Scikit-learn provides a large suite of machine learning algorithms and tools that integrate with pandas DataFrames.

# Python libraries like Matplotlib and Apache Superset provide powerful tools for creating a wide variety of visualizations, enabling you to gain deeper insights into your data and communicate your findings effectively.

# NOTE: PRACTICAL SCENARIO: OPTIMIZING USER EXPERIENCE ON AN E-commerce website

# You've implemented various features, but you're noticing some users aren't completing their purchases. 
# This is where data analysis, specifically Exploratory Data Analysis (EDA), comes in handy!

# Why is this example relevant? 
# Understanding how users interact with your site is crucial for improving performance and conversion rates. EDA provides the tools to uncover these insights.

# Problem: users are abandoning their shopping carts 

# Your Detective Work (EDA - Exploratory Data Analysis)
# Using Python and Pandas - you could load this data into a DataFrame

# You'd perform Data Cleaning to handle any missing values 
# You might use Matplotlib to create visualizations 
# You could use Aggregation to summarize data
# If you have data over time, time series analysis could help see if abandonment rates fluctuate during specific periods

# The Insight: Through this EDA, you might discover that the shipping cost calculation is unclear, or the checkout process has too many steps.