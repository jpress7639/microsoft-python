# Scheduling tasks with Cron Jobs (Linux/macOS)

# cron - a time-based job scheduler that functions as your very own automated task manager
# cron empowers you to schedule the execution of tasks at specific times or intervals

# cron – a silent workhorse that empowers you to automate your workflow, optimize your productivity, 
# and ensure that your system operates seamlessly, even when you're not around.

# Understanding the syntax and structure
# crontab', which adheres to a specific syntax:
# minute hour day-of-month month day-of-week command-to-be-executed

# 0 0 * * * /path/to/backup.sh

# cron job tells your system to execute the script 'backup.sh' every day at midnight
# The zeros in the first two fields signify midnight (0 minutes, 0 hours)
# asterisks indicate that this should happen every day of the month, every month, regardless of the day of the week

# Breaking down the fields
# Each field in the crontab syntax corresponds to a specific time unit, allowing for granular control over your task scheduling
# Minute - 0 to 59
# Hour - 0 to 23 
# Day - can do 1-31 or specific dates
# Month - can input 1-12 or Jan-Dec
# Day of Week - from 0 (Sunday) to 6 (Saturday) or Sun-Sat

# E.g. For instance, to run a script at 10:30 AM every day, you would set the minute field to 30 and the hour field to 10:
# 30 10 * * * /path/to/script.sh

# To illustrate, if you want to run a backup script at 2 AM every day, you'd set the hour field to 2:
# 0 2 * * * /path/to/backup.sh

# For example, to execute a task on the 15th of every month, you would set the day-of-month field to 15:
# 0 0 15 * * /path/to/task.sh

# To run a script every January at midnight you could use either:
# 0 0 1 1 * /path/to/script.sh or 0 0 1 Jan * /path/to/script.sh

# To schedule a task to run every Friday at noon, you would set the day-of-week field to 5 (or Fri) and the hour field to 12:
# 0 12 * * 5 /path/to/task.sh

# Special Characters 

# The flexibility of cron is highlighted through its use of special characters, enabling you to craft intricate scheduling patterns. 
# Asterisk (*) - acts as a wildcard - all possible values in a field 
# Commas - separators for listing multiple specific values
# Hyphens - defining ranges, task to run on weekdays (1-5)
# Slash (/) - allows you to specify increments in a range
# '/2' in the hour field means "every 2 hours". 

# Example Cron Jobs
# # Run a system check every 5 minutes
"""*/5 * * * * /usr/local/bin/system_check.sh"""
# Generate a sales report at 8 AM on the 1st and 15th of every month
"""0 8 1,15 * * /usr/local/bin/generate_sales_report.py"""
# Restart a service every weekday (Monday to Friday) at midnight
"""0 0 * * 1-5 /usr/local/bin/restart_service.sh"""
# Perform database maintenance every 4 hours 
"""0 */4 * * * /usr/local/bin/database_maintenance.sql"""

# Coding challenge: Automated system maintenance
cron_job_input = "30 23 * * * /usr/bin/backup_database.sh"
print(cron_job_input)

# Best Practices 

# Incorporate Error Handling - graceful catch information about the error
# Always use the full path - avoid ambiguity 
# Prioritize the security of your crontab file and script 

# Potential Concerns 
# While it's true that many alternatives exist, cron remains a steadfast and dependable option, 
# especially for tasks that don't require complex orchestration.

# Its straightforward syntax, reminiscent of plain English instructions, makes it remarkably easy to learn and use.
# its deep-rooted integration within Unix-like systems ensures widespread compatibility and support
# making it a familiar and accessible tool for sysadmins across the globe

# PRACTICAL SCENARIO 
# Automating Daily Data Backups for a Web Application
# directly connects to your role as a web developer, where data integrity and application reliability are paramount
# ties into the core concept of Time-based Automation and Scheduled Tasks

# Breaking it down:
# write a Python script that connects to your database, exports the data, and then stores it in a secure location
# Instead of running this script yourself every night, you can use a Scheduled Task (if you're on Windows) or a Cron Job (if you're on Linux/macOS)
# This setup ensures that your data is consistently backed up without any manual intervention, reducing the risk of data loss and giving you peace of mind.

