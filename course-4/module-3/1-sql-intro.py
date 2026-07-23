# SQL

# (Structured Query Language) is a standard language for managing and manipulating relational databases. 
# It allows you to perform various operations such as 
# querying data, inserting new records, updating existing records, and deleting records from a database.

# SQL provides a way to interact with these tables to retrieve and manipulate data.
# It is widely used in various applications, from web development to data analysis, 
# and is supported by many database management systems (DBMS) such as MySQL, PostgreSQL, SQLite, and Microsoft SQL Server.

# Syntax of SQL:
# First you use the SELECT statement to specify the columns you want to retrieve from a table.
# If you use the asterisk (*) symbol, it means you want to retrieve all columns from the table.
# Next, you use the FROM clause to specify the table from which you want to retrieve the data.
# With the WHERE clause, you can filter the data based on specific conditions.
# WHERE searches for rows where that criteria is true. You can use comparison operators such as =, <, >, <=, >=, and <> (not equal) to define the conditions.

# You can use comparison operators to filter data based on specific conditions. 
# For example, you can use the = operator to find rows where a column matches a specific value, 
# or the > operator to find rows where a column is greater than a certain value.
# or you can use the LIKE operator to search for patterns in string data,
# or the IN operator to check if a value exists in a list of values.

# For complex filters, you can use AND and OR operators to combine multiple conditions.
# For example, you can use AND to require that multiple conditions are true,
# or use OR to allow for either condition to be true.

# Python provides libraries such as sqlite3, psycopg2, and SQLAlchemy 
# that allow you to connect to databases and execute SQL queries from your Python code.

# Code Example:
import sqlite3
# Connect to a SQLite database (or create a new one if it doesn't exist)
connection = sqlite3.connect('example.db')
cursor = connection.cursor()

# Create a table
cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')

# Insert data into the table
cursor.execute("INSERT INTO users (name, age) VALUES ('Alice', 30)")
cursor.execute("INSERT INTO users (name, age) VALUES ('Bob', 25)")

# Commit the changes and close the connection
connection.commit()
connection.close()

# Example with PyODBC (for connecting to other databases like MySQL, PostgreSQL, etc.)
import pyodbc # type: ignore
# Connect to a database using ODBC
connection = pyodbc.connect('DRIVER={SQL Server};SERVER=your_server;DATABASE=your_database;UID=your_username;PWD=your_password')
cursor = connection.cursor()
# Execute a query
cursor.execute("SELECT * FROM your_table")
# Fetch and print the results
for row in cursor.fetchall():
    print(row)
connection.close()

