# Implementing Database Relationships

# One-to-one relationships: The art of augmentation
# In a one-to-one relationship, each record in one table is associated with exactly one record in another table.
# For example, a user profile and its corresponding user account. 
# Each user has only one profile, and each profile belongs to only one user.

# E.g. Consider a User table and a UserProfile table.
# Each user might have an associated profile containing details like their biography, profile picture, or social media links.
# This ensures each user has a single, dedicated profile, preventing data duplication or ambiguity.

# Implementing one-to-one relationships in Flask (SQLAlchemy)
# Flask, with help from SQLAlchemy, an Object Relational Mapper (ORM), 
# provides an elegant way to define and manage database relationships

# SQLAlchemy translates Python objects into database rows, 
# simplifying database interactions and abstracting away the complexities of SQL.

from flask_sqlalchemy import SQLAlchemy # type: ignore

db = SQLAlchemy() # Initialize the SQLAlchemy object to manage database connections and models

class User(db.Model): # Represents the User table in the database
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(120))
    profile = db.relationship('UserProfile', backref='user', uselist=False)

class UserProfile(db.Model): # Represents the UserProfile table in the database
    id = db.Column(db.Integer, primary_key=True)
    bio = db.Column(db.Text)
    profile_picture = db.Column(db.String(200))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

# In this example, the User table has a one-to-one relationship with the UserProfile table.
# The relationship is established using the `db.relationship` 
# in the User model and the `db.ForeignKey` in the UserProfile model.

# This ensures that each user has a single, dedicated profile, and each profile 
# is linked to only one user.

# consider a scenario where you want to display a user's profile information on their account page
# Using the backref, you can easily access the user's profile details through the user object without needing to perform a separate database query.

# One-to-many relationships: The power of hierarchy

# They represent a hierarchical structure where a single record in one table can be linked to multiple records in another table. 
# For example, a single customer can have multiple orders, with each order linked to that customer.

# A classic example in web development is a Blog table and a Post table.
# Each blog can have multiple posts, but each post is linked to a single blog.
# This structure efficiently organizes and manages blog content, 
# ensuring each post is correctly attributed to its source.

# Implementing one-to-many relationships in Flask (SQLAlchemy)

from flask_sqlalchemy import SQLAlchemy # type: ignore

db = SQLAlchemy() # Initialize the SQLAlchemy object to manage database connections and models

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    posts = db.relationship('Post', backref='blog') # Establishes the one-to-many relationship, 
    # allowing access to all posts associated with a specific blog through the `posts` attribute

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    content = db.Column(db.Text)
    blog_id = db.Column(db.Integer, db.ForeignKey('blog.id')) # Establishes the foreign key relationship linking the post to a specific blog

# In this example, the Blog table has a one-to-many relationship with the Post table.
# The relationship is established using the `db.relationship` 
# in the Blog model and the `db.ForeignKey` in the Post model.

# This ensures that each blog can have multiple posts, and each post 
# is linked to only one blog.

# The backref='blog' creates a virtual column in the Post model, providing easy access to the associated blog. 
# This bi-directional relationship is a powerful feature of SQLAlchemy, 
# allowing you to traverse the relationship from either side with ease

# It simplifies querying and data manipulation, making your code more efficient and readable. 
# For instance, you can use the blog.posts attribute to access all the posts associated with a specific blog, 
# or you can use the post.blog attribute to access the blog to which a particular post belongs.

# Many-to-many relationships: The web of interconnections
# In a many-to-many relationship, multiple records in one table can be associated 
# with multiple records in another table.

# Implementing many-to-many relationships in Flask (SQLAlchemy)
from flask_sqlalchemy import SQLAlchemy # type: ignore

db = SQLAlchemy()

# Association table to establish the many-to-many relationship between students and courses
# The enrollments table acts as a bridge between the Student and Course tables, storing the relationships between them. 
enrollments = db.Table('enrollments', 
    db.Column('student_id', db.Integer, db.ForeignKey('student.id'), primary_key=True), 
    db.Column('course_id', db.Integer, db.ForeignKey('course.id'), primary_key=True) 
)
# Establishes the foreign key relationship linking the enrollment to a specific student
# Establishes the foreign key relationship linking the enrollment to a specific course

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    courses = db.relationship('Course', secondary=enrollments, backref=db.backref('students', lazy='dynamic'))

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    students = db.relationship('Student', secondary=enrollments, backref=db.backref('courses', lazy='dynamic'))

    # Establishes the many-to-many relationship with the Student model,
    # allowing access to all students enrolled in a specific course through the `students` attribute

    # The backref='students' in the Student model creates a virtual column in the Course model,
    # providing easy access to all students enrolled in a specific course.
    # This bi-directional relationship allows you to traverse the relationship from either side with ease,
    # making it simple to query and manipulate data related to students and courses efficiently.

# Flask: A flexible and powerful framework
# Its extensibility through a rich ecosystem of extensions allows you to add functionalities 
# like authentication, database migrations, and API development with ease. 

# Choosing the right framework
# Consider factors like project size, team size, and the level of control and customization you desire.
# Flask's minimalist approach also makes it a good choice for microservices and APIs, where a lightweight and focused framework is preferred.

# ORM: Making Databases Talk with Python

# Object-Relational Mapping (ORM) allows developers to interact with databases 
# using Python objects instead of writing raw SQL queries.

# ORM provides a high-level abstraction over the database, 
# allowing developers to work with Python objects and classes instead of writing complex SQL queries.

# How do they do this?
# They map Python classes to database tables and Python objects to rows in those tables.
# This mapping allows developers to perform CRUD (Create, Read, Update, Delete) operations 
# on the database using Python code, without needing to write raw SQL queries.