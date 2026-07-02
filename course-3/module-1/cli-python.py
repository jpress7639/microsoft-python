# CLI in Python 

# explore the art of crafting robust and user-friendly CLIs in Python, 
# focusing on two indispensable libraries:  argparse and sys.

# The power of argparse

# argparse library is the go-to solution for handling command-line arguments in Python
# a meticulous organizer that brings order and clarity to the potentially chaotic world of user input

# you gain the power to explicitly define the types of arguments, specify their expected formats, 
# and craft messages that guides uses if they stumble upon errors or uncertainties 

# A simple example

# # we start by importing the argparse library
import argparse

# we create an ArgumentParser object, 
# which acts as the central hub for managing all the arguments our script will accept
parser = argparse.ArgumentParser(description='A friendly greeting script.')
# use parser.add_argument to introduce a specific argument called 'name'
parser.add_argument('name', help='The name of the person to greet.')
# we call parser.parse_args() to process the actual command-line input provided by the user
args = parser.parse_args()
# retrieve the value of the 'name' argument using args.name and seamlessly 
# incorporate it into our personalized greeting message
print(f"Hello, {args.name}!")

# Input is typing in the command line: python greet.py Alice

# Output is the statement printed: “Hello Alice!”

# argparse elevates your script's user-friendliness
# NOTE: If a user gets stuck or unsure, they can simply type python greet.py -h or python greet.py --help

# NOTE: If someone forgets to provide a name, argparse steps in with a helpful error message 
# and a reminder of the correct usage

# Advanced features: 
# allows you to define optional arguments, indicated by the -- prefix, 
# giving users the freedom to provide additional information if they choose

# can also create arguments with predefined choices, ensuring that only valid values are accepted
# argparse enables you to specify the expected data types for arguments, preventing mismatches and potential errors.

# The role of sys

# sys - module acts as a bridge between your Python script and the underlying operating system, 
# offering insights into system-specific details and functionalities

# the sys.argv list stands out as a crucial element for interacting with command-line arguments
# a neatly organized container that captures all the words and phrases typed after
# your script's name when you execute it from the command line

# like a transcript of the conversation between you and your script -> preserving the exact sequence of arguments provided 

# use sys.argv directly to access command line arguments 
# This script checks if any arguments were provided (i.e., if sys.argv has more than one element)
import sys
if len(sys.argv) > 1:
# If so, it assumes the first argument is the name and uses it in the greeting.
    name = sys.argv[1]
    print(f"Hello, {name}!")
else:
# Otherwise, it provides a generic greeting.
    print("Hello, there!")

# Conparison with argparse 
# sys.argv gives you direct access to the raw command-line arguments,
# argparse acts as a sophisticated interpreter

# Imagine sys.argv as a box of puzzle pieces, argparse as the master puzzle solver.
# argparse not only deciphers the individual pieces (arguments) but also validates their correctness, arranges them into a meaningful structure, and even provides helpful hints (help messages)

# Addressing concerns
# Efficiency - often facilitate faster and more precise actions, especially for experienced users who have mastered the command-line environment
# Automation - CLIs seamlessly integrate into scripts and workflows, making them the ideal companions for automation
# Accessibility - hey can be accessed from a wide range of platforms, including those with minimal resources or specialized environments where graphical interfaces might be impractical or unavailable

# Practical Scenario - 

# Automation of Repetitive Tasks (Concept: Command Line Interfaces, argparse)
# A CLI allows you to automate these tasks with simple commands. For instance, you could create a Python script that, when run with specific arguments, automatically deploys your latest code to a staging server.

# Data Processing Script (Concept: Command Line Interfaces, argparse):
# You could write a Python script that takes the filename as a command-line argument.
# Using argparse: Your script would use argparse to define an argument like --file <filename>
# then run it from your terminal like this: python process_users.py --file user_data.csv.

# Configuration Management (Concept: Command Line Interfaces, argparse): 
# Overriding Defaults: You can design your Python scripts to accept command-line options that override default settings. 
# You could run python deploy.py --environment production to deploy to your production server, 
# or python deploy.py --environment development for your development environment.
# This makes your scripts adaptable to various needs without needing to change the code every time.

# PYTHON SCRIPTS AND SHELL COMMANDS 

# Your objective is to process each file individually, extract specific data points or patterns, 
# and then compile these findings into a comprehensive report.

# Python, with its powerful data processing capabilities and ability to interact with files, 
# can seamlessly handle the extraction and manipulation of information from each individual file

# shell commands can be employed to efficiently navigate your file system, automate repetitive tasks, 
# and even perform preliminary data filtering before passing it on to Python for further refinement.

# Data Piping 

# subprocess - module in Python acts as a bridge between your Python code 
# and the vast world of shell commands on the op system

# one of the most powerful features enabled by the subprocess module 
# is the ability to pipe data between commands

# like a virtual pipeline where the output of one command flows directly into the input of another

# e.g. you have a massive log file filled with various entries, 
# and you only want to extract lines containing the word "error."


# grep - designed to search through text input for lines that match a specified pattern.
# you can employ the grep command to filter out the relevant lines and then feed 
# those directly into a Python script for further analysis

#Python error_finder.py
import subprocess

# Use grep to find lines containing "error" in a log file
grep_process = subprocess.Popen(['grep', 'error', 'logfile.txt'], stdout=subprocess.PIPE)

# Pass the output of grep to a Python script for further analysis
python_process = subprocess.Popen(['python', 'analyze_errors.py'], stdin=grep_process.stdout)

# Wait for the Python script to finish
python_process.wait()

# Python analyze_errors.py
import sys

# Read lines containing "error" from standard input (provided by subprocess)
for line in sys.stdin:
  # Process each error line
  print(f"Found: {line.strip()}")

print("Finished analyzing errors.")

# Batch processing 

# When you're faced with a mountain of files or a series of repetitive tasks that seem to stretch on endlessly,
# batch processing emerges as your trusty companion in the realm of automation.

# w/ Python's ability to interact with your file system and execute shell commands, 
# you can craft scripts that effortlessly iterate through directories, 
# apply specific actions to each file, 
# and even gracefully handle any unexpected errors that might arise along the way.

# Python's error handling mechanisms allow you to anticipate 
# and gracefully manage any unexpected issues that might occur during batch processing

import os
import subprocess
for filename in os.listdir('data_directory'):
    if filename.endswith('.csv'):
        # Convert CSV files to Excel using a shell command
        subprocess.call(['libreoffice', '--convert-to', 'xls', filename])

# Error handling and robustness 

# things can go wrong - A file might be missing, a command might fail, or unexpected data might cause issues. 
# You can use try-except blocks to catch potential errors and implement graceful recovery mechanisms. 

try:
    subprocess.run(['rm', 'important_file.txt'], check=True)  # Delete a file, raise an error if it fails
except subprocess.CalledProcessError as e:
    print(f"Error deleting file: {e}")


# Real-world applications
# Data Science and Machine Learning - 
# Python scripts frequently leverage shell commands like sed and awk, or even domain-specific tools, 
# to preprocess raw data before it's fed into machine learning models

# DevOps and System Administration sphere -
# automating tasks like server deployments, log analysis, 
# and system maintenance heavily relies on the synergy between Python's scripting capabilities 
# and the direct system access offered by shell commands

# Web Development - routine tasks such as minifying JavaScript files, compiling CSS, 
# or executing build scripts are often automated using a combination of Python and shell commands, 
# streamlining the development workflow.

# Addressing Concerns 

# NOTE: shell commands and their syntax can vary between Windows, macOS, and Linux. 
# relying heavily on shell commands within your Python scripts might 
# introduce some challenges when it comes to portability across different operating systems

# 1) you can identify cross-platform alternatives to specific shell commands, 
# ensuring that your code functions consistently regardless of the underlying operating system.

# 2) there are libraries like plumbum that provide a powerful abstraction layer over shell commands

