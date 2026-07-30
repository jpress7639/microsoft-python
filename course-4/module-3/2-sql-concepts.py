# SQL Concepts

# Data types: The foundation of data integrity

# Common SQL data types include:
# - INTEGER: Represents whole numbers.
# - FLOAT: Represents decimal numbers.
# - VARCHAR: Represents variable-length character strings.
# - CHAR: Represents fixed-length character strings.
# - DATE: Represents date values.
# - BOOLEAN: Represents true/false values.
# - TIMESTAMP: Represents date and time values.
# - TEXT: Represents large text data.
# - BLOB: Represents binary large objects, such as images or files.

# Filtering data: Selecting what matters

# SQL's WHERE clause acts like a sieve, allowing you to specify conditions for selecting data, such as comparisons and pattern matching.

# Example, to retrieve all orders placed with a total value greater than $100, you would use:
# SELECT customer_id, order_id, order_date, total_amount
# FROM Order
# WHERE total_amount > 100;

# Query conditions can also be connected with AND and OR
# Example, let's find all customers in the state of California (CA) 
# who have placed orders with a total value greater than $100:
# SELECT customer_id, order_id, order_date, total_amount
# FROM Order
# WHERE state = 'CA' AND total_amount > 100;

# LIKE operator: Pattern matching
# The LIKE operator allows you to search for specific patterns in string data.
# The % wildcard represents zero or more characters
# The _ wildcard represents a single character.
# Example, to find all customers whose names start with 'J':
# SELECT customer_id, name FROM Customer WHERE name LIKE 'J%';

# if a product had the word Keyboard somewhere in its name, you could use:
# SELECT product_id, name FROM Product WHERE name LIKE '%Keyboard%';

# Use a wildcard for all cusomters who have the letter 'a' as the second letter in their name:
# SELECT customer_id, name FROM Customer WHERE name LIKE '_a%';

# This query would like to find customers with 'on' in their names:
# SELECT customer_id, name FROM Customer WHERE name LIKE '%on%';

# IN operator: Checking for Multiple Values
# The IN operator provides a concise way to check if a value matches any value in a list
# Example, to find all customers in the states of California, Oregon, or Washington:
# SELECT customer_id, name, state FROM Customer WHERE state IN ('CA', 'OR', 'WA');

# Grouping Data: Aggregating and Summarizing 
# Grouping data allows you to aggregate data based on shared characteristics, enabling you to derive insights and summaries from your datasets.
# The GROUP BY clause is used to group rows that have the same values in specified columns.

# Common aggregate functions include:
# - COUNT(): Returns the number of rows in a group.
# e.g. - to count the number of customers in the Customer table:
# SELECT COUNT(*) FROM Customer;
# e.g. - to get a count of customers in each state:
# SELECT state, COUNT(*) FROM Customer GROUP BY state;

# Other aggregate functions include:
# - SUM(): Returns the total sum of a numeric column.
# - AVG(): Returns the average value of a numeric column.
# - MAX(): Returns the maximum value in a group.
# - MIN(): Returns the minimum value in a group.

# Example, to count the number of customers in each state:
# SELECT state, COUNT(*) FROM Customer GROUP BY state;

# Joining tables: Connecting related data
# SQL provides JOIN operations based on related columns between tables, allowing you to combine data from multiple tables into a single result set.

# Different types of JOINs include:
# - INNER JOIN: Returns only the rows that have matching values in both tables.
# - LEFT JOIN (or LEFT OUTER JOIN): Returns all rows from the left table and
# - RIGHT JOIN (or RIGHT OUTER JOIN): Returns all rows from the right table and the matching rows from the left table.
# - FULL OUTER JOIN: Returns all rows when there is a match in either table.

# Example, consider a database with two tables: Customers and Orders. 
# To retrieve customer names and their corresponding IDs, you can use an  JOIN:
# SELECT Customer.name, Order.order_id
# FROM Customer
# JOIN Order ON Customer.customer_id = Order.customer_id;

# Join two tables to see Book information with each Review - common field is book_id:
# SELECT *
# FROM Book
# JOIN Review ON Book.book_id = Review.book_id;

# ORMs: Simplifying database interactions
# Object-Relational Mapping (ORM) is a programming technique that allows developers 
# to interact with databases using object-oriented programming languages, rather than writing raw SQL queries. 
# ORMs provide a higher-level abstraction for database operations,
# making it easier to work with databases in a more intuitive and Pythonic way.

# Databases and ORMs: A preview
# Imagine you're building a book review application. 
# You have one model: Book.  
# To tell your application how the database is related to the Python program, 
# you need to use db.Column.

# comment = db.Column(db.Text)

import db # type: ignore

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(100), nullable=False)


# here is a comparison of how SQL and ORM would extract all books 
# containing the phrase Python in the title.

# SQL: SELECT * FROM Book WHERE title LIKE '%Python%';
# ORM: Book.query.filter(Book.title.like('%Python%')).all()

