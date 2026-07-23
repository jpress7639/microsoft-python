# Database essentials for web developers

# Types of Database Relationships:
# - One-to-One (1:1): Each record in one table is associated with one record in another table. 
# For example, a user profile and its corresponding user account.

# - One-to-Many (1:N): A single record in one table can be associated
# with multiple records in another table. For example, a single customer can have multiple orders.

# - Many-to-Many (M:N): Multiple records in one table can be associated with multiple records in another table.
# For example, students and courses, where a student can enroll in multiple courses, 
# and a course can have multiple students.

# You can use SQL Queries to:
# - Retrieve specific data from one or more tables.
# - Insert new records into a table.
# - Update existing records in a table.
# - Delete records from a table.

# Web applications act as a bridge between users and databases, 
# allowing users to interact with data through a user-friendly interface.

# Inserting Data into a Database:
# To insert data into a database, you can use the INSERT INTO statement.
# Example, to insert a new book to books table with the title "Pride and Prejustice" and author "Jane Austen", genre "Romance" and set availability to true, you can use the following SQL query:
# INSERT INTO Book (title, author, genre, availability) VALUES ('Pride and Prejudice', 'Jane Austen', 'Romance', true);

# Update the availability of the book to false, you can use the following SQL query:
# UPDATE Book SET availability = false WHERE title = 'Pride and Prejudice';

# Remove the book from the database, you can use the following SQL query:
# DELETE FROM Book WHERE title = 'Pride and Prejudice';
