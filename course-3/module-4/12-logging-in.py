# Logging: Your automation script's diary

# Logging in Python serves as a meticulous record-keeper for your automation scripts
# Diligently captures crucial events, unexpected errors, and valuable data generated during scripts execution

# Why logging matters 
# Without logging, you have no idea what's going wrong or where to start looking for the problem.

# By strategically placing logging statements:
# you create a trail of breadcrumbs 
# that helps you trace the flow of your script and diagnose issues effectively.
# Allows you to track the flow of execution
# Monitor the values of variables 
# Gain sights into the behavior and state of your script during execution

# The basics 

# Python has a built-in logging module - makes it easy to implement logging in your scripts
# First step is to import the logging module
# Once imported, configure the logging system itself by setting the log level, format, and output destination (e.g., console or file)

# Example:
# import logging
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filename='app.log')

# After configuration, you can use different logging levels to record messages:
# logging.debug("This is a debug message")
# logging.info("This is an info message")
# logging.warning("This is a warning message")
# logging.error("This is an error message")
# logging.critical("This is a critical message")

# DEBUG - Detailed information, typically of interest only when diagnosing problems
# INFO - Confirmation that things are working as expected, general information
# WARNING - An indication that something unexpected happened, or indicative of some problem in the near future (e.g., ‘disk space low’). The software is still working as expected.
# ERROR - Due to a more serious problem, the software has not been able to perform some function.
# CRITICAL - A very serious error, indicating that the program itself may be unable to continue running.

# Pros and Cons of Logging 
# Pros:
# - Provides a detailed record of script execution
# - Helps in diagnosing and troubleshooting issues
# - Can be configured to capture different levels of detail

# Cons:
# - Can introduce performance overhead if used excessively
# - Requires proper management of log files to avoid disk space issues
# - May expose sensitive information if not handled carefully

