# Python's schedule module: Simplified task scheduling
# the schedule module stands out for its simplicity and ease of use in scheduling tasks

# Understanding the Schedule Module
# the schedule module functions like a well-organized calendar for your Python tasks.

# you tell it what you want to do and when, and it takes care of executing your tasks at the specified times.

# module keeps these instructions diligently and executes them at the right times.
# designed to be lightweight and easy to integrate into your Python projects.

# Code Example illustrating core functionality of schedule module

import schedule # type: ignore
import time

def say_hello():
    print("Hello, it's time for your scheduled task!")

def fetch_news_headlines():
    print("Fetching the latest news headlines...")
    # Add your actual news fetching logic here

def backup_data():
    print("Backing up your important data...")
    # Add your data backup logic here

# Schedule tasks
# schedule.every().day.at("08:00").do(say_hello)  # Daily reminder at 8 AM
# schedule.every(1).hour.do(fetch_news_headlines)  # Fetch news every hour
# schedule.every().day.at("00:00").do(backup_data)  # Data backup at midnight

# Ease of Use and Flexibility

# You'll find yourself using functions like every(), at(), and run_pending() to create and manage your schedules.

# This demonstrates how you can schedule tasks at very short intervals, such as every 2 seconds, using the schedule module.

# schedule module is that it lets you express your scheduling needs in plain Python code, making it intuitive and easy to read.
# You simply write your tasks as Python functions and then tell the schedule module when to run them using its intuitive commands. 

# The beauty of the schedule module is that it's easy to pick up and start using, even if you're new to Python.

# Advanced Scheduling Techniques

# You can schedule jobs to run at specific time intervals using the `every(interval)` method combined with time units like `minutes`, `hours`, `days`, `weeks`, and even `seconds`.

# Let's say you need to run a method named check_logs every 5 minutes. You can use this syntax:

def check_logs():
    print("Checking logs for any issues...")
    # Add your log checking logic here

schedule.every(5).minutes.do(check_logs)

# # Keep the script running to execute scheduled tasks
# while True:
#     schedule.run_pending()
#     time.sleep(1)

# The parameter to every (5) indicates the amount of time, and will be followed by the time unit. To run the same job every 30 seconds, the code would be similar:

schedule.every(30).seconds.do(check_logs)

# Scheduling Jobs on Specific Days
# The `every()` method can also be chained with specific days of the week (e.g., `monday`, `tuesday`, etc.) to schedule tasks on those particular days.

# Let's say you have a payroll function that should run every Saturday:

def payroll():
    print("Running payroll for the week...")

schedule.every().saturday.do(payroll)

# This demonstrates how you can schedule tasks on specific days of the week using the schedule module.

# Scheduling Jobs at Specific Times
# Scheduling a job on a specific day is extremely helpful, but you can further refine it using the `at(time_string)` method to the `every()` method. The `time_string` should be in the 24-hour format (e.g., "09:30", "17:00").

schedule.every().saturday.at("23:30").do(payroll)

# Tagging Jobs
# The `tag(tag_name, ...)` method allows you to assign tags to scheduled jobs, making it easier to manage and identify them later
# Let's say you have two computer maintenance tasks and you want them both to have this tag for easy searching later. You can set them up with the same tag:	

# schedule.every().day.at("00:00").do(backup_1).tag('maintenance')

# schedule.every().sunday.do(defragment_disk).tag('maintenance')

# Finding scheduled jobs
# If your program has many tasks, you can use the `get_jobs()` method:

print(schedule.get_jobs())

# This will print a list of all scheduled jobs, making it easier to keep track of what tasks are scheduled and when they are set to run.

print(schedule.get_jobs(tag='maintenance'))

# This will print a list of all scheduled jobs that have the 'maintenance' tag, making it easier to manage and identify specific tasks.

# Going Further

# If you need even more advanced options, the schedule module may not be for you
# Other libraries like 'AP Scheduler' or 'Celery' provide more advanced scheduling capabilities for complex scenarios.

# Practical Applications

# a busy marketing team that needs to deliver weekly performance reports to your stakeholders.
# You can schedule a job to automatically generate and send these reports every Friday at 17:00:

def send_weekly_report():
    print("Sending weekly performance report...")
    # Add your report generation and sending logic here

schedule.every().friday.at("17:00").do(send_weekly_report)  

# Scenario: The automated reminder system

def send_daily_reminder():
    print("Don't forget to update the project status in the tracking tool!")

def send_weekly_reminder():
    print("Reminder: Weekly team meeting today at 9:00 AM!")

def calculate_volunteer_hours():
    print("Calculating volunteer hours. Results will be emailed!")

# Schedule the daily reminder for every day at 10 AM
schedule.every().day.at("10:00").do(send_daily_reminder).tag('reminders')

# Schedule the weekly reminder for every Monday at 9 AM
schedule.every().monday.at("09:00").do(send_weekly_reminder).tag('reminders')

# Schedule the volunteer hour calculations to be done at 11:59 PM Tuesday and Friday (2 lines of code)
schedule.every().tuesday.at("23:59").do(calculate_volunteer_hours) # no tag
schedule.every().friday.at("23:59").do(calculate_volunteer_hours) # no tag

print("Starting the reminder system...")
print("Currently scheduled tasks:")

# Print out current list of scheduled jobs
print(schedule.get_jobs())

# Instructions to start the scheduler
# You can start the scheduler by running a loop that continuously checks for pending jobs:

while True:
    schedule.run_pending()
    time.sleep(1)

