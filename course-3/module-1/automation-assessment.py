# AUTOMATION ASSESSMENT 
# Automation delegates those repetitive tasks to computers, freeing us for more strategic and impactful work.

# helps the team focus on personalized support and making creative choices and personal connections 

# Identifying automation opportunities 

# 1) Feasibility - can this task be automatable? Does it have a set pattern?
# 2) Data - does the task rely on data that's accessible?
# 3) Evaluate skills and resources - do you have the Python to build the automation script?

# e.g. social media marketing team - spend hours a week to deliver reports to stakeholders
# developed a Python script that automatically pulled the data for the social media APIs, 
# generated visually appealing reports, and emailed to stakeholders on a routine basis

# e.g. software company's onboarding process 
# it involved a lot of manual steps, sending welcome emails, creating user ​accounts, assigning initial tasks. 
# built a Python script that triggered a series of action when a new user signed up that automated all of that 

# PRIORITIZING AUTOMATION EFFORTS

# Where to start? 
# Focus on tasks with the biggest impact, the most time-consuming, error-prone, or those ​causing bottlenecks.
# automation can improve accuracy and reduce the risks of costly mistakes

# By focusing on high-impact tasks, you'll maximize the benefits of your automation efforts. 
# Prioritization also means balancing the potential benefits of automation against the effort it takes.

# Some tasks are easy to automate versus others that need more complex code

# Priority Checklist 
# 1) Complexity - is the task logic simple and predictable?
# 2) Tools - are there already made Python libraries to help?
# 3) Expertise - does your team have the skills to handle this? 

# Other factors
# 1) Scalability - might be wise to automate early on as business expands
# 2) Employee Morale - freed from the boring repetitive task
# 3) Risk mitigation - some tasks that need high accuracy 


# IDENTIFYING AUTOMATION OPPORTUNITIES 

# when trying to identify tasks that could be done with automation

# Are there any tasks that I find myself doing over and over again, 
# tasks that eat up my time but don't necessarily require my full brainpower?

# automating reporting process example

import pandas as pd
import requests
from bs4 import BeautifulSoup 

# Generate an automation workflow for data collection from csv and website

def extract_from_website(url):
    # Function to extract data from html website
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        # Find a table element
        table = soup.find('table')

        # If a table is found, extract the data
        if table:
            headers = [th.text for th in table.find('tr').find_all('th')]
            data = []
		  # The loop will find all tr tags (table rows)
            for row in table.find_all('tr')[1:]:
			# Within each table row, select all td (table data)
                row_data = [td.text for td in row.find_all('td')]
			# Appends the value from the td to the data array
                data.append(dict(zip(headers, row_data)))

            return pd.DataFrame(data)
        else:
            print("No table found on the page.")
            return None
    except Exception as e:
        print(f"Error fetching URL: {e}")
        return None
    
def gather_data_from_sources():
  data_from_csv = pd.read_csv('sales_data.csv')
  # Example: Fetching data from a website using requests & BeautifulSoup 
  web_data_url = 'https://example.com/marketing_data'
  data_from_website = extract_from_website(web_data_url)   
  return pd.concat([data_from_csv, data_from_website], axis=1) # Combine data

def process_and_format_data(data):
  # ... Process data to create Price Per Unit column.
  formatted_data = data[['Total Order Price', 'Number of Units']] 
  formatted_data['Price Per Unit'] = formatted_data['Total Order Price'] / formatted_data['Number of Units']
  return formatted_data

def generate_report(data):
  # Generate final report (could use pandas' to_excel, or libraries like ReportLab, matplotlib, etc).
  data.to_excel('marketing_report.xlsx')
  print("Report generated successfully!") 
    
# Main Automation Flow
raw_data = gather_data_from_sources()
processed_data = process_and_format_data(raw_data)
generate_report(processed_data)

# gather_data_from_sources() function acts as the data collection hub, 
# equipped to retrieve information from diverse sources such as CSV files, databases, APIs, 
# or even through web scraping techniques using libraries like requests and BeautifulSoup.

# process_and_format_data() function steps in to clean, transform, calculate, and restructure the data, 
# ensuring it aligns perfectly with the report's requirements. 

# generate_report() function takes this refined data and crafts the final report, 
# offering flexibility in output formats, from simple Excel exports to visually rich PDFs 
# or interactive visualizations, depending on the chosen libraries or methods

# CHOOSING THE RIGHT TOOLS 

# For those simpler, more straightforward automations, 
# you might not even need to write a single line of code

# There's a growing landscape of no-code or low-code automation platforms that 
# empower you to create automations through intuitive, visual interfaces

# pandas -> renowned for its data manipulation capabilities
# ReportLab -> could be employed to generate the final polished report.

# Zapier -> acts as a bridge between different applications, 
# allowing to seamlessly connect data sources and automate the data transfer process 

# Illustrative Python code showcasing tool selection for automation
# Scenario 1: Python-Powered Automation 
import pandas as pd 
# ... other potential libraries based on task: os, requests, BeautifulSoup, etc. 
def automate_with_python(task_complexity):
  if task_complexity == "simple":
    # ... Code for simple file operations, basic data handling, etc.
    print("Python automating simple tasks!")
    # return simple_task_function()
  elif task_complexity == "complex":
    # ... Code leveraging pandas for data analysis, web scraping, etc.
    print("Python handling complex automation with its powerful libraries!")
    # return complex_task_function() 

# Scenario 2: No-Code Automation (Conceptual)
def automate_with_no_code(platform):
  if platform == "Zapier":
    # ... Conceptual representation of Zapier automation setup
    print("Zapier automating tasks with its visual interface!")
  # ... other no-code platforms could be added here
# User's Choice & Task Complexity
comfortable_with_coding = True  # Or False
task_complexity = "complex"     # Or "simple"
if comfortable_with_coding:
  automate_with_python(task_complexity)
else:
  automate_with_no_code("Zapier") 
print("Automation in action! Choose the tools that empower you.")

# The power of small steps
# success lies in pacing yourself and building momentum gradually
# NOTE: It's tempting to dive headfirst into automating every single task that crosses your path, but resist the urge

# Overcoming Challenges and Objections

# Others might find the prospect of learning new tools and technologies intimidating
# Some might harbor concerns that automation will render their roles obsolete

# By automating those mundane, repetitive tasks that drain our time and energy, 
# we liberate ourselves to focus on what truly matters - 
# the creative, strategic, and innovative aspects of our work


