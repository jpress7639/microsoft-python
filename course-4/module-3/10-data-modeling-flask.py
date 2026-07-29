# Data modeling with Flask-SQLAlchemy

# In Flask SQL Alchemy, models are Python classes that mirror 
# the structure of your database tables.

# Think of each class as a blueprint for a table, 
# with its attributes representing the columns in that table.

# This approach streamlines your development process by letting you work 
# with familiar Python objects instead of raw SQL queries.

# Attributes - characteristics or properties of the model, 
# which correspond to the columns in the database table.
# You can specify the data type of each attribute, such as Integer, String, DateTime, etc.

# Code Example:
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() # Initialize the SQLAlchemy object

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Primary key column
    username = db.Column(db.String(80), unique=True, nullable=False)  # Unique username column
    email = db.Column(db.String(120), unique=True, nullable=False)  # Unique email column

    def __repr__(self): # String representation of the User object - useful for debugging and logging purposes.
        return f'<User {self.username}>'

# This example defines a User model with three attributes: id, username, and email.

# Flask SQL Alchemy establishes a direct mapping between these two worlds.
# Each instance of your Python class represents a row in the corresponding database 
# table, and each attribute of the class maps to a column in that table.

# Once you've defined your models, you need to create the corresponding tables in your database.
# Flask SQL Alchemy provides a convenient way to do this using the db.create_all() method.

# Data Modeling Best Practices:

# 1) Normalization 

# Normalization is the process of organizing this chaos, 
# breaking down large tables into smaller, interconnected ones. 

# By normalizing a database, you create separate tables for "Customers" and "Orders", 
# linked by a foreign key.

# E.g. if a customer changes their address, 
# we only need to update it once in the "Customers" table, 
# and all related orders will automatically reflect the change.

# Code Example: 
class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    orders = db.relationship('Order', backref='customer', lazy=True)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_date = db.Column(db.DateTime, nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)

# 2) Indexing
# Let's say you frequently search for customers by their last name on your e-commerce platform.
# Creating an index on the "last_name" column in the "Customers" table is like 
# having a librarian who instantly points you to the right shelf.

# an index is a data structure that stores a sorted copy of the indexed column 
# along with pointers to the corresponding rows in the actual table.

# When you execute a query that involves the indexed column, 
# the database can quickly locate the relevant data by traversing the index, 
# rather than scanning the entire table. 

# Choosing appropriate data types: The art of optimization
# It's a balancing act between storage efficiency, query performance, and data integrity.

# Storage efficiency:
# Choosing the right data type can significantly reduce the amount 
# of storage space required for your data.

# Query performance:
# Different data types have different performance characteristics.
# For example, integer comparisons are generally faster than string comparisons,
# so if you have a column that will only store numeric values,
# using an integer data type can lead to faster query execution times.

# Data integrity:
# Choosing the right data type can help enforce data integrity by preventing invalid data from being stored in the database. 
# For example, using a date data type for a column that 
# stores dates ensures that only valid date values can be inserted into that column.

# Considering future growth: The architect of scalability

# When designing your data model, it's important to consider how your application might grow in the future.
# For example, if you anticipate that a particular table will eventually need to store millions of rows
# or that a certain column will need to accommodate larger values,
# you should choose data types and structures that can handle that growth without requiring a major redesign of your database schema.

# Examples of planning for future growth
# Choose a NoSQL database If you anticipate storing large volumes of unstructured or semi-structured data.
# NoSQL databases are designed for horizontal scalability, making them well-suited for handling big data applications.

# Implemental partitioning - dividing a large table into smaller, more manageable pieces, called partitions.
# Each partition can be stored and accessed separately, improving query performance and maintenance.

# Sharding involves distributing data across multiple servers based on a sharding key. 
# This approach can help improve performance and scalability by allowing queries to be executed in parallel across multiple servers.

# Caching frequently accessed data involves storing frequently accessed data in memory, 
# reducing the need for disk access.