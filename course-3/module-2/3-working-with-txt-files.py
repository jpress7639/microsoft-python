# WORKING WITH TEXT FILES 

# Text files - are digital repositories where you can store information in a simple, human-readable format

# Opening and reading text files 
# open() function that helps you start working with the information stored in a file

# you need to tell it two things: the name of the file you want to open and how you want to use it.
# This second part is called the 'mode'. 

# The most common modes are 
# 'r' - the default mode and it's for reading only, can't change anything 
# 'w' - for writing, if the file doesn't exist, Python will create it for you
# NOTE: if the file already exists, this mode will erase everything inside it before you start writing
# 'a' - appending - adding new information at the end of the file 
# NOTE: if the file doesn't exist - Python will create it

# e.g.
# In [1]:
# Opening and reading a file
file = open('example.txt', 'r')
content = file.read()
print(content)
file.close()


# Out[1]:
# Hello, this is a text file.

# a more efficient and safer way to handle files using the with statement - 
# automatically close the file once the block is exited

# In [2]:
# Using with statement to open and read a file
# with open('example.txt', 'r') as file:
#     content = file.read()
#     print(content)


# Out[2]:
# Hello, this is a text file.

# once the file is open - you have a variety of methods at your disposal to access its contents 

# most straightforward approach is to read the entire file into your program's memory in one go
# NOTE: This method works well for smaller files where memory usage isn't a concern
# when dealing with larger files, this approach can become problematic as it can consume a significant amount of memory

# Python offers the flexibility to read the file line by line:
# more memory efficient as it only loads one line of the fiule into memory at a time 
# Python provides intuitive tools and techniques to facilitate both of these reading approaches
# NOTE: And don't forget to close the file when you're finished

# 'Write' mode is like starting a new notebook. 

# 'Append' mode, on the other hand, is like adding to an existing notebook
# It lets you add your new information to the end of the file without erasing anything that was already there

# Use the write() method to add your text when the file is open
# NOTE: use special characters like \n to tell the computer to start a new line

# Appending to text files
# This mode ensures that your new content is seamlessly added to the end of the file, 
# preserving all the existing information

# e.g. 
# In [3]:

# Appending to a text file
# with open('newfile.txt', 'a') as file:
#     file.write('Adding a new line to the existing file.\n')


# Reading the updated file
# with open('newfile.txt', 'r') as file:
#     print(file.read())


# Out[3]:

# This is a new file.
# Here we add more text.
# Adding a new line to the existing file.

# Working with CSV files
# CSV files (Comma Separated Values) - a popular and widely used format for storing data in a table-like structure

# working with a csv file in 'csv' module 
# In [4]:
import csv
"""Reading a CSV file"""
# with open('example.csv', mode='r') as file:
#     csv_reader = csv.reader(file)
#     for row in csv_reader:
#         print(row)


output = {
    ['Name', 'Age', 'City'],
    ['Alice', '24', 'New York'],
    ['Bob', '27', 'Los Angeles']
    }

# Reading CSV with Python - You can access each piece of information individually, 
# making it easy to process and analyze the data

# Python also provides a clever way to ensure that your CSV files are handled properly, 
# even if something unexpected happens during your program

# with statement - acts as a safety net, 
# automatically closing the file when you're done with with it or if an error occurs

# CHALLENGES
# File encoding - language your computer uses to understand the characters in a text file
# if you encounter files created with a different encoding - 
# you might need to explicitly specify it when opening the file to ensure accurate interpretation of the content.

# Error handling - the file may not exist, or you may not have the right permissions 
# if you encounter files created with a different encoding,
# you might need to explicitly specify it when opening the file to ensure accurate interpretation of the content.
# it's a good practice to incorporate error handling mechanisms using try-except blocks

# Reading the entire content into memory at once - can be inefficient and lead to performance issues
# it's advisable to adopt strategies like reading the file in smaller chunks 
# or utilizing techniques like generators