# Guide to 'Automation and scripting with Python'

# Step 1: Version control
# Why do teams use Git?

# Developers frequently modify and improve their code. 
# Version control systems, like Git, help developers manage these changes effectively.

# Benefits:
# 1) Maintain a history: Git keeps a complete record of all modifications to your code.
# 2) Restore previous versions: If a mistake occurs, Git allows you to easily revert to an earlier version of your code.
# 3) Work with others: Git helps developers collaborate effectively on the same codebase.
# 4) Experiment safely: With Git, you can try new approaches without worrying about losing your progress.


# Why GitHub for aspiring developers?
# Showcase your work: Employers want to see what you can do. 
# Use GitHub to display your projects and demonstrate your coding style and abilities.

# Track your progress: Regular activity on GitHub shows your commitment to learning and improving. 
# Employers can see how your skills have developed over time.

# Gain visibility: A strong GitHub profile helps you stand out. 
# Contributing to projects, especially open-source ones, shows initiative and passion.

# Learn collaboration: Working on GitHub projects gives you practical experience with teamwork and collaborative coding practices.

# Step 2: Data handling and preprocessing
# Preparing the data
# Before diving into analysis, it's crucial to prepare your data. 
# This involves loading the dataset (sports_data_missing.csv) into a pandas DataFrame.

# Step 3. Visualization Building and Evaluation
# Visualizing baseball statistics
# First, you'll define a function called create_scatter_plot that creates scatter plots. 
#  In baseball, we often compare offensive statistics like walks (BB) to strikeouts (SO) or home runs (HR) to at bats (AB). 

# Step 4. API Integration with SendGrid
# SendGrid Signup 
# To use Twilio's SendGrid tool, you'll first need to create an account and obtain an API key. 
# When first signing up, you will be provided a recovery code that should be stored securely, in case your account is compromised.

# Before you use the API, you need to define a Sender.
# A Sender is an email account with a company name, address, city, state, and ZIP.
# Once you have completed setting up, visit the Email API menu to access your key. 

# SendGrid API integration
# you will create a function utilizing the SendGrid API to send emails.
# this function takes the email subject, content, and recipient's email address as input. 
# Within the function, you'll construct an email message and use the Sendgrid send() method to send a message, such as a notification that the data analysis is complete or visualizations are ready for review.

# Steps 5 & 6: Automation, Error Handling and Logging
# Automating error handling and logging
# The schedule library in Python provides a straightforward way to schedule tasks like updating data, generating visualizations, and sending alerts at specific intervals.

# In this project, you'll use the schedule library to automate the sending of an email alert every day at 9:00 AM, giving you a taste of how to schedule any task within your analysis workflow.
# A file might be missing, the network connection could drop, or your code might encounter an unforeseen error. 