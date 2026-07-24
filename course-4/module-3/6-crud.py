# CRUD operations using ORMs

# Object-Relational Mapping (ORM)
# ORM is a technique that allows developers to interact with a database 
# using object-oriented programming languages like Python.

# It maps database tables to Python classes and rows to instances of those classes, 
# enabling developers to perform CRUD (Create, Read, Update, Delete) operations using 
# Python objects instead of writing raw SQL queries.

# This abstraction not only streamlines your code by making it more readable, concise, and expressive,
# It also enhances its maintainability and portability across different database systems.

# How ORMs streamline design
# ORMs achieve this streamlining of design in several key ways, 
# notability abstraction, consistency, portability, and productivity. 

# Abstraction: ORMs provide a layer of abstraction over the database, 
# allowing developers to interact with the database using Python objects and methods 
# rather than writing raw SQL queries. This simplifies database interactions and 
# reduces the complexity of the code, making it easier to understand and maintain.

# Consistency: ORMs enforce a consistent way of interacting with the database, 
# reducing the likelihood of errors and inconsistencies in the code. 
# By using Python objects and methods to perform database operations, 
# developers follow a standardized approach, which enhances code reliability and maintainability.

# For instance, if you add a new attribute to a Python class representing a database table, 
# the ORM can generate the SQL ALTER TABLE statement to add the corresponding column to the table.

# Portability: ORMs enhance the portability of the code across different database systems. 
# Since ORMs provide a consistent interface for interacting with the database, 
# the underlying database can be changed with minimal modifications to the code. 
# This allows developers to switch between different database systems without having to rewrite the database interaction logic, 
# making the application more flexible and adaptable to different environments.

# Productivity: ORMs improve developer productivity by automating repetitive tasks 
# and providing a high-level interface for database interactions. 

# Developers can focus on writing business logic rather than dealing with 
# the intricacies of SQL queries and database management. 

# This leads to faster development cycles and allows developers to build 
# and maintain applications more efficiently.

# ORMs automate many repetitive tasks associated with database interaction.
# For example, instead of manually writing SQL INSERT statements to create new records, 
# you can create Python objects and let the ORM handle the database insertion.

# Creating data: Breathing life into your application
# The 'C' in CRUD means creating your data in the database. 
# With the aid of an ORM, you can create new records by instantiating Python objects that mirror your data models and adding them to a session.
# The ORM's session acts as a staging area where you can collect changes to your data 
# before committing them to the database in a single transaction.
# This approach ensures that all changes are applied atomically, maintaining data integrity and consistency within the database.

# Reading data: Retrieving the information you need
# The 'R' in CRUD means reading or retrieving data from the database.
# With the aid of an ORM, you can read data by querying the Python objects that represent your data models.
# You can pinpoint specific data with primary keys, filter data using various criteria, 
# and even perform complex queries involving relationships between different data models, 
# all through the ORM's query interface without writing raw SQL queries.

# The ORM takes care of the SQL translation, optimizing the query for performance, 
# and presenting you with the results as convenient Python objects ready for your perusal.

# Updating data: Keeping your information current
# The 'U' in CRUD means updating existing data in the database.
# With the aid of an ORM, you can update data by modifying the attributes of the Python objects that represent your data models.
# Once the changes are made, you can commit the session, and the ORM will generate the appropriate SQL UPDATE statements to apply the changes to the database.
# This approach ensures that updates are applied consistently and efficiently, maintaining data integrity and reflecting the latest information in the database.

# In our social media scenario, if a user decides to refresh their profile picture, 
# you'd retrieve their User object, update the profile_picture attribute with the new image, 
# and then commit the changes, allowing the ORM to handle the database interaction.
# The ORM will identify the modified attributes and generate an optimized UPDATE statement 
# that targets only the necessary columns, making database updates more efficient and minimizing the impact on the database.

# Deleting data: Removing what's no longer needed
# The 'D' in CRUD means deleting data from the database.
# The ORM generates the corresponding SQL DELETE statement to expunge the record from the database.

# if a user decides to bid farewell to their account, you'd retrieve their User object 
# and then delete it from the session, entrusting the ORM to handle the database cleanup
# The ORM will not only delete the user record but also 
# any associated posts, comments, or other related data, 
# maintaining the consistency and integrity of your database.

