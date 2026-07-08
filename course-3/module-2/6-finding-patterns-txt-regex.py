# Finding patterns in text with Regex

# Think of regex as a highly specialized language designed to describe patterns within text
# These patterns can be as simple as a specific word or phrase or as complex as email addresses, 
# phone numbers, or even specific HTML tags within a webpage

# In the realm of Python programming, the re module serves as your gateway 
# to harnessing the power of regular expressions.

# Understanding regular expressions

# You can pinpoint sequences of characters, combinations of letters and numbers, 
# specific symbols, or even the presence or absence of whitespace.

# NOTE: E.g. consider the seemingly simple regex \d+.
# This unassuming pattern acts as a vigilant numerical detective, 
# meticulously scanning text to identify and capture sequences of one or more digits
# This regex could be your key to effortlessly extracting prices, inventory quantities, 
# or any other numerical data nestled amidst the descriptive text.


# NOTE: E.g. we have the more intricate regex \b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b.
# is expertly designed to ensnare email addresses from the vast ocean of text
# This regex demonstrates the ability to craft precise patterns that target specific types of information, 
# even within complex and unstructured text data

# Extracting information from text

# Web scraping - gathering product prices from an e-commerce site
# Regex - craft patterns that precisely match the HTML tags and attributes where price data resides
# With re module - you can systematically scan the website's HTML code, 
# effortlessly extracting the desired prices, transforming a potentially tedious task into an automated process

# Log files - can be overwhelming 
# Regex acts as a powerful filter - error messages, suspicious user login attempts
# regex empowers you to extract actionable insights, aiding in both troubleshooting and security analysis.

# Data cleaning - text data often riddled with inconsistencies and errors, extra spaces, typos, inconsistent formatting 
# Regex - applying carefully crafted patterns, you can ensure that your data is pristine and ready for further processing, 
# laying a solid foundation for accurate and meaningful results.

# Key Concepts and Techniques 
# Character classes serve as the building blocks of your regex patterns - define sets of characters you aim to match 
# [a-z] acts as a filter, allowing only lowercase letters to pass through
# \d specifically targets any digit

# Quantifiers - dictate how many times a character or a group of characters should appear for a successful match
# + -  signifies that the preceding character or group must occur at least once
# ? - indicates that it's optional - it can appear zero or one time

# Anchors - markers within your text 
# ^ anchor, for instance, insists that a match must begin at the start of a line
# $ mandates that it concludes at the end of a line

# Groups - introduce the concept of capturing specific portions of the matched text
# e.g. (\d{3})-(\d{3})-(\d{4})
# captures a phone number (in North America), neatly organizing it into three distinct groups: area code, prefix, and line number

# Examples of Use
# Pattern: \d+
# This pattern matches one or more digits (0-9).

# Pattern: [A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}
# This pattern matches email addresses, local part (username) containing letters, numbers, and specific symbols, followed by an "@" symbol, a domain name with letters, numbers, hyphens, and dots, and a top-level domain (e.g., .com, .org) of at least two letters

# Pattern: \b\w+\b  
# This pattern matches individual words. \b denotes word boundaries, ensuring that it matches whole words and not parts of words.

# Pattern: \d{3}-\d{3}-\d{4}
# This pattern matches phone numbers in the format "XXX-XXX-XXXX".

# Pattern: https?://[^\s]+
# This pattern matches URLs (web addresses).


# Example: how you might search a string named user_input to see if it contains a valid phone number

# Save the pattern in a variable for comparison
# phone_number_pattern = r"^(\d{3}) \d{3}-\d{4}$"
# # Compare the user_input variable to the regex pattern
# if re.match(phone_number_pattern, user_input): 
#   print(f"{phone_number} is a valid phone number.")
# else:
#   print(f"{phone_number} is not a valid phone number.")



# Challenge: Validate Email Addresses with Regular Expressions

import re

def validate_email(email):
    """
    Validates an email address using a regular expression.

    Args:
        email: The email address to validate.

    Returns:
        True if the email is valid, False otherwise.
    """
    email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
    if re.match(email_pattern, email):
        return True
    else:
        return False


# Test cases
emails = [
    "test@example.com",
    "invalid.email",
    "another_test@domain.co.uk",
    "not_valid@.com",
    "user+123@company.net"
]

# Parsing dates and times

# Regex offers a solution by allowing you to extract these temporal elements 
# from text and convert them into a standardized format

# Sentiment Analysis 

# Regular expressions can assist in this process by identifying keywords or phrases 
# within text data that signal positive or negative sentiment
# By applying regex patterns to social media posts, product reviews, or customer feedback, 
# you can gain a quantitative understanding of public opinion, 
# aiding in marketing strategies, product development, and brand reputation management

# Navigating the challenges of regex
# NOTE: syntax of regex can be cryptic and difficult to grasp, particularly when dealing with intricate patterns
# The combination of special characters, quantifiers, and anchors can create expressions that resemble a secret code, 
# potentially intimidating newcomers

# Another concern raised is the potential computational overhead associated with regex, 
# especially when applied to massive datasets

# With dedicated practice and a willingness to learn, the syntax of regex can become second nature

# PRACTICAL SCENARIO:

# One of your tasks is to ensure that all product prices displayed on the website 
# are correctly formatted and can be easily extracted for analysis or database storage.

# The Challenge: Product prices might appear in various formats across different parts of the website or in data feeds. 
# For example, you might see "$19.99", "£10.50", "25.00 USD", or even "Free". 

# How Regex Helps (Concept: Data Extraction & Pattern Matching)
# Instead of writing complex code with many if statements to check for every possible price format
# You can use a single, powerful Regex pattern
# a Regex pattern like \d+\.\d{2} could be used to find numbers with at least one digit before a decimal point and exactly two digits after it (e.g., "19.99", "10.50").
# You could then combine this with other Regex features to handle currency symbols or extract the number specifically.