# ORM: How Python talks to databases

# The Object-Relational Mapper (ORM) plays a large role in modern application development, 
# simplifying the interaction between Python applications and relational databases. 

# At its core, an ORM is a powerful tool that allows developers to interact with databases 
# using object-oriented paradigms, abstracting away the complexities of SQL.

# This abstraction layer allows developers to focus on the application logic, 
# leaving the complexities of database interactions to the ORM.

# The translation process
# ORMs translate Python code into SQL queries.
# For example, if you have a Python class representing a "Customer" with attributes like name, email, and address.

# When you create an instance of this class and save it using an ORM, 
# it generates the necessary SQL INSERT statement to store the customer data in the database.

# When you create a Customer object in Python and call the ORM's save() method on it, 
# the ORM inspects the Customer class and its attributes. 
# It then constructs an SQL INSERT statement based on this information, 
# mapping the object's attributes to the corresponding columns in the Customer table and inserting the data into the database.

# Code Example: 
import sqlalchemy  # type: ignore

class Customer:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address
    def save(self):
        # This is a placeholder for the ORM's save method
        # In a real ORM, this would generate an SQL INSERT statement
        # and execute it to store the customer data in the database
        pass

# Usage Example:
customer = Customer("John Doe", "john.doe@example.com", "123 Main St")
customer.save()  # This would trigger the ORM to generate and execute an SQL INSERT statement

# Similarly, when you retrieve customer data using the ORM, 
# it constructs the appropriate SELECT query to fetch the information from the database and populate Python objects.

# For example, if you want to find all customers whose name is "John," 
# you'd use the ORM's query language to express this condition.
# The ORM would then translate this into an SQL SELECT statement 
# with a WHERE clause that filters the results based on the name.

# Code Example:

# Assuming the ORM provides a query method on the Customer class
customers_named_john = Customer.query.filter_by(name="John").all()
for customer in customers_named_john:
    print(customer.name, customer.email, customer.address)
    # This would print the details of all customers named "John" retrieved from the database
    # In a real ORM, this would involve executing an SQL SELECT statement
    # with a WHERE clause filtering by the name "John" and then mapping the results
    # to Customer objects.

# ORMs can handle complex queries involving joins, filters, and aggregations. 
# They provide a rich set of APIs and query languages that allow developers 
# to express database interactions in a Pythonic way. 

# For example, if you want to find all books borrowed by a particular customer, 
# you'd use the ORM to express a join between the Book and Borrower tables, 
# filtered by the customer's ID.
# The ORM would then generate the necessary SQL JOIN and WHERE clauses to execute this query.

# Code Example:
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def save(self):
        # This is a placeholder for the ORM's save method
        # In a real ORM, this would generate an SQL INSERT statement
        # and execute it to store the book data in the database
        pass

class Borrower:
    def __init__(self, customer_id, book_id):
        self.customer_id = customer_id
        self.book_id = book_id
    def save(self):
        # This is a placeholder for the ORM's save method
        # In a real ORM, this would generate an SQL INSERT statement
        # and execute it to store the borrower data in the database
        pass
# Assuming the ORM provides a query method on the Book class
books_borrowed_by_customer = Book.query.join(Borrower).filter(Borrower.customer_id == 1).all()
for book in books_borrowed_by_customer:
    print(book.title, book.author)
    # This would print the details of all books borrowed by the customer with ID 1 retrieved from the database
    # In a real ORM, this would involve executing an SQL SELECT statement
    # with JOIN and WHERE clauses and then mapping the results to Book objects.

# Benefits of ORMs
# By abstracting away the complexities of SQL, 
# ORMs allow developers to write database interactions using familiar Python syntax.
# This leads to increased productivity, reduced likelihood of SQL syntax errors, 
# and a more seamless integration between the application code and the database layer.

# ORMs provide helpful features like automatic schema generation and migration. 
# This means that when you change your Python classes (e.g. add a new attribute),
# the ORM can automatically update the database schema to reflect these changes.

# ORMs promote maintainability by centralizing database interactions within the application code. 
# This makes it easier to manage and update database-related logic, 
# as changes can be made in one place rather than scattered throughout the codebase, reducing the risk of inconsistencies and errors.

# ORMs provide a layer of abstraction between the application and the underlying database.
# This abstraction allows developers to switch between different database systems with minimal code changes.
# For instance, you can seamlessly migrate your application from MySQL to PostgreSQL 
# by simply changing the database configuration in your ORM settings.

# Code Example: 
import sqlalchemy  # type: ignore
from sqlalchemy import create_engine, MetaData # type: ignore
engine = create_engine('sqlite:///:memory:')  # In-memory SQLite database
metadata = MetaData()
metadata.bind = engine
# This sets up an in-memory SQLite database and binds the metadata to the engine,
# allowing SQLAlchemy to manage the database schema and execute SQL statements against this database.

# ORMs help mitigate common security vulnerabilities like SQL injection attacks by automatically parameterizing queries.
# This means that user input is safely handled and incorporated into SQL statements without directly concatenating strings, 
# reducing the risk of malicious input compromising the database.

# ORMs protect against this by automatically escaping user input and using parameterized queries, 
# which make it much harder for attackers to inject harmful SQL code.

# Code Example: 
import sqlalchemy  # type: ignore
from sqlalchemy import Table, Column, Integer, String, MetaData # type: ignore
metadata = MetaData() # Creates a MetaData object to hold information about the database schema, including tables and their columns
customer_table = Table(
    'customer',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(100)),
    Column('email', String(100)),
    Column('address', String(200))
)   

# This defines the structure of the customer table in the database using 
# SQLAlchemy's Table and Column constructs.

# SQL injection is a serious security threat where attackers 
# exploit vulnerabilities in your application's SQL queries to gain unauthorized access 
# to your database or execute malicious commands. 

# Real-life examples:
# a social networking application leverages an ORM to handle user profiles, posts, comments, and friend connections. 
# The ORM streamlines the creation of new user accounts, retrieval of friend lists, and display of personalized news feeds. 

# An e-commerce platform uses an ORM to manage its vast product catalog, customer information, and order history. 
# The ORM simplifies the process of adding new products, updating inventory levels, and processing customer orders.

# A content management system employs an ORM to store and manage articles, blog posts, images, and other media assets.
# The ORM facilitates the creation, editing, and publishing of content, as well as the retrieval of content based on various criteria.

# Opposing Viewpoints
# Some argue that ORMs can introduce a slight performance overhead compared to writing raw SQL queries. 
# However, this overhead is often negligible in most real-world applications, 
# and the benefits of productivity and maintainability far outweigh any minor performance impact.

# ORMs have their own set of APIs and query languages that developers need to learn. 
# However, this learning curve is relatively small compared to mastering SQL, 
# and the long-term benefits of using ORMs justify the initial investment in learning.