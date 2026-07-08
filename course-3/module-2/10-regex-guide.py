# Reference guide to Regex

# Reference guide to Regex: Unlocking the power of pattern matching

# Regular expressions (regex or regexp) are a powerful tool for working with text data
# provide a concise and flexible way to search, match, and manipulate strings based on patterns
# regular expressions - a specialized language for describing patterns within text

# What are regular expressions?
# regular expression - a sequence of characters that defines a search pattern
# can be as simple as a single character or as complex as a combination of characters, quantifiers, and special symbols

# incredibly useful for tasks like:

# Searching for specific information: You can use regex to find email addresses, 
# phone numbers, dates, or any other pattern within a large body of text.

# Data validation: Regex can ensure that user input conforms to a specific format, 
# such as a strong password or a valid zip code.

# Data cleaning and transformation: Regex can be used to remove unwanted characters, 
# standardize formats, and extract relevant information from messy data.

# Text replacement: You can use regex to find and replace specific patterns within a text, 
# making it a valuable tool for editing and formatting.

# The building blocks of regular expressions

# Literal characters: These are the simplest form of patterns. They match themselves exactly. 
# For example, the regex cat would match the string "cat" but not "Cat" or "catalog".

# Metacharacters: These are special characters that have a meaning beyond their literal interpretation.
#  
# Some common metacharacters include:
# . (dot): Matches any single character except a newline.
# * (asterisk): Matches zero or more occurrences of the preceding element.
# + (plus): Matches one or more occurrences of the preceding element.
# ? (question mark): Matches zero or one occurrence of the preceding element.
# [] (character class): Matches any single character within the brackets. For example, [aeiou] matches any vowel.
# ^ (caret): When used inside a character class, it negates the class. For example, [^aeiou] matches any character that is not a vowel.

# Quantifiers: These specify how many times an element should appear. 
# The most common quantifiers are *, +, and ?, as mentioned above.
# You can also use curly braces {} to specify a more precise range. 
# For example, a{2,4} matches "aa", "aaa", or "aaaa".

# Anchors: Anchors match the start (^) or end ($) of a string. 
# When used with the re.MULTILINE flag, they also match the start or end of each line within a multiline string. 

# The most common anchors are:
# ^ (caret): Matches the start of a line.
# $ (dollar sign): Matches the end of a line.

# Groups: These allow you to treat multiple characters as a single unit. 
# You can use parentheses () to create groups. 
# For example, (ab)+ matches one or more repetitions of "ab".


# Using regular expressions in Python

# CODE EXAMPLE

import re

text = "Please contact me at john.doe@example.com or jane.doe@company.org for more information."

email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"

email_matches = re.findall(email_pattern, text) # The `findall()` function returns a list of all the matches.

print(email_matches) 

# This code will output:
# ['john.doe@example.com', 'jane.doe@company.org']

# import re: This line imports the `re` module, which provides functions for working with regular expressions.
# text: This variable contains the text we want to search for email addresses.
# email_pattern: This is the regular expression pattern for matching email addresses.
# re.findall(email_pattern, text): This line uses the `findall()` function from the `re` module to find all occurrences of the `email_pattern` in the `text`. 
# print(email_matches) - This line prints the list of email addresses that were found.

# Extracting other data types

# Phone Numbers: `r"\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b"`
# Dates: `r"\b\d{1,2}[-/]\d{1,2}[-/]\d{2,4}\b"`
# URLs: `r"https?://\S+"`

# Beyond regular expressions: NLP and machine learning
# For more complex data extraction tasks, you might need to explore other techniques, such as:

# (NLP) libraries: NLP libraries like NLTK and spaCy provide tools for analyzing and understanding the structure and meaning of text
# Machine learning models: This approach can be more accurate than regular expressions for tasks that are difficult to define with simple patterns.

# Data cleaning and transformation with Python

# Removing duplicates: This ensures each data point is unique.
# Filling missing values: This can be done using various strategies, such as replacing missing values with the mean or median.
# Standardizing formats: This ensures consistency across your data.

# Automating tasks with Python scripts
# the biggest advantages of using Python for data extraction and processing is the ability to automate tasks
# You can write Python scripts that combine regular expressions, data cleaning techniques, and analysis to create powerful workflows

# RECAP: 
# Regular expressions are a versatile tool for working with text data.
# Python provides a built-in module (`re`) for using regular expressions.
# You can use regular expressions to extract various types of data, such as email addresses, phone numbers, and dates.
# For more complex tasks, consider using NLP libraries or machine learning models.
# Python libraries like pandas make it easy to clean and transform data.
# Python scripts can automate data-driven workflows, saving time and effort.