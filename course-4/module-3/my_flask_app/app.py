import email

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy  
from flask_migrate import Migrate 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_flask_app.db' # Database configuration
db = SQLAlchemy(app) # Initialize the database
migrate = Migrate(app, db) # Initialize Flask-Migrate

class User(db.Model): # Define a User model for the database
    id = db.Column(db.Integer, primary_key=True) # Unique identifier for the user
    username = db.Column(db.String(80), unique=True, nullable=False) # Username of the user
    email = db.Column(db.String(120), unique=True, nullable=False) # Email of the user

    def __repr__(self):
        return '<User %r>' % self.username # String representation of the User model

# CRUD Operations with SQLAlchemy
# Create
with app.app_context(): # Create the database tables if they don't exist
    db.create_all() # Create all tables defined by the models
    new_user = User(username='johndoe', email='johndoe@example.com')
    db.session.add(new_user) # Add the new user to the session
    db.session.commit() # Commit the session to save the new user to the database

# Read
with app.app_context(): # Read users from the database
    users = User.query.all() # Query all users from the User model
    for user in users: # Iterate through the list of users
        print(user) # Print each user

# Update
with app.app_context(): # Update a user's email in the database
    user = User.query.filter_by(username='johndoe').first() # Query the user with username 'johndoe'
    if user: # Check if the user exists
        user.email = 'john.doe@example.com' # Update the user's email
        db.session.commit() # Commit the session to save the changes to the database

# Delete
user = User.query.filter_by(username='johndoe').first() # Query the user with username 'johndoe'
if user: # Check if the user exists
    db.session.delete(user) # Delete the user from the session
    db.session.commit() # Commit the session to remove the user from the database

# Filtering 
users_with_gmail = User.query.filter(User.email.like('%@gmail.com')).all() # Query users with Gmail addresses

# Ordering
users_ordered_by_username = User.query.order_by(User.username).all() # Query users ordered

# Limiting
limited_users = User.query.limit(5).all() # Query a limited number of users (5 in this case)

# Counting
user_count = User.query.count() # Count the total number of users in the database

# Error handling
try:
    new_user = User(username='janedoe')
    db.session.add(new_user) # Attempt to add a new user without an email
    db.session.commit() # Commit the session to save the new user to the database
except Exception as e: # Catch any exceptions that occur during the database operation
    db.session.rollback() # Rollback the session to undo any changes made during the transaction
    print(f"An error occurred: {e}") # Print the error message      


@app.route("/") # Define the home route
def home(): # Define the home function that will be called when the home route is accessed
    return "Hello, World!"

if __name__ == "__main__": # Check if the script is run directly (not imported as a module)
    app.run(debug=True)