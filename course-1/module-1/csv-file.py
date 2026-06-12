import csv

# Read a CSV file
with open('data.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)


# Iterate: Systematically loop through all the data files, ensuring that every data point is included in the analysis. Loops, such as for loops, allow you to repeat a block of code for each item in a collection, such as a list of files. This eliminates the need for manual repetition and ensures consistency in your analysis.

# Extract: Intelligently read the relevant data from each file, filtering out noise and irrelevant information. Python provides libraries like pandas, which simplifies the process of reading data from various file formats (for example, CSV or Excel) and manipulating it in a structured manner. You can easily select specific columns, filter rows based on conditions, and extract the data you need for your analysis.

