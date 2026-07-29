# Working with databases review

# Defining key database terms

# relational database: A type of database that organizes data into tables 
# (relations) with rows and columns, allowing for efficient storage, retrieval, 
# and management of structured data.

# SQL - Structured Query Language, a standard programming language used to manage 
# and manipulate relational databases.

# Object-Relational Mappers (ORMs) - Tools that allow developers to interact with 
# a relational database using an object-oriented paradigm, 
# abstracting away the underlying SQL queries.
# Examples of ORM include SQLAlchemy, Django ORM, and Hibernate.

# Mastering CRUD operations
# CRUD operations are the fundamental building blocks of database interactions,
# enabling developers to create, read, update, and delete data within a database.

# Create - The operation of adding new records to the database.
# Read - The operation of retrieving existing records from the database.
# Update - The operation of modifying existing records in the database.
# Delete - The operation of removing records from the database.

# The role of databases in web applications
# data persistence - Databases provide a means to store and retrieve data persistently,
# ensuring that information remains intact even after the application is closed or restarted.

# databases let you perform queries - which are requests to retrieve specific data 
# from the database based on certain criteria.
# Queries allow us to retrieve and display information tailored to user needs
# filtering, sorting, and aggregating data to provide meaningful insights and enhance user experiences.

# By leveraging databases, web applications can deliver personalized experiences, 
# responding to user input and presenting relevant information in real-time. 

# ORMs: Simplifying database interactions
# They act as intermediaries between the object-oriented world of 
# programming languages like Python and the relational world of databases.

# ORMs provide a higher-level abstraction: 
# allowing developers to interact with databases using 
# familiar object-oriented concepts like classes and objects

# Example, a scenario where a User model represents a table in a database.
# With ORM, you can create a new user record by simply creating a User object, setting its attributes, 
# and calling save() method provided by the ORM.

# Setting up databases and connecting to web applications

# There are popular options like SQLite, MySQL, PostgreSQL, and MongoDB, 
# each with its own strengths and use cases.

# SQLite - A lightweight, file-based database that is easy to set up and use.
# ideal for smaller projects and development environments.

# PostgreSQL - A powerful, open-source relational database known for its robustness,
# scalability, and support for advanced features like JSON data types and full-text search.

# Once your database is set up, 
# you can connect it to your Django or Flask application using a database driver or an ORM.

# Defining models and schemas for data representation
# Models - In the context of web applications, 
# models are classes that represent the structure and behavior of data entities in the application.
# They provide a blueprint for how data is stored, retrieved, and manipulated within the application.

# Models also define the relationships between tables, 
# such as one-to-one, one-to-many, or many-to-many relationships. 

# ORMs can also perform CRUD operations.
# They provide a simple and intuitive interface for performing these operations.
# For example: to create a new user record, you can create a User object, set its attributes (such as name, email, and password),
# and then call the save() method provided by the ORM to persist the data to the database.

# To retrieve user records, the ORM's query API filters the User model based on specific conditions,
# such as retrieving all users with a certain email address or users whose names start with a particular letter.

# The ORM would translate these filter conditions into SQL SELECT statements, 
# executing them against the database and returning the matching user records as User objects.

# Updating user information involves retrieving the corresponding User object, 
# modifying its attributes, and then calling the save() method again.

# Deleting a user record is as simple as calling the delete() method on the corresponding User object