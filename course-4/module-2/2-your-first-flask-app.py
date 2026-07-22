# Your first Flask App

# Step one: Set up a virtual environment

# Create a project folder
# mkdir first-flask-project
# cd first-flask-project

# Create a Virtual Environment

# Use the venv module to create a virtual environment. This will create a new directory called venv that contains a copy of the Python interpreter and a local version of the pip package manager.
# python3 -m venv venv

# Activate the virtual environment
# On macOS and Linux:
# source venv/bin/activate

# On Windows:
# venv\Scripts\activate

## Step two: Install Flask

# Use pip to install Flask in the virtual environment. This will download and install Flask and its dependencies.
# pip install Flask

# Step three: Create the app.py file
# Create a new file called app.py in the project folder. This file will contain the code for your Flask application.

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Flask!'

if __name__ == '__main__':
    app.run(debug=True)

# Step four: Run the application
# Run the application by executing the following command in the terminal:
# python -m flask run
# This will start the Flask development server, and you should see output indicating that the server is running. 
# You can access the application by opening a web browser and navigating to http://127.0.0.1:5000/

# The name variable is a special Python variable that is set to the name of the module in which it is used. 
# When you run a Python script, __name__ is set to '__main__', 
# so this line tells Flask to use the current module as the application.

# Debug mode is a very important mode
# When debug mode is enabled, the server will automatically reload for code changes and show an interactive debugger in the browser if an error occurs.

# Databases enable you to persist data. 
# By doing this, it allows your application to store and retrieve data as needed.

# Flask's routing magic 

# Flask routes are the pathways within your web application that map specific URLs to ​corresponding Python functions.

# Decorators are a powerful feature in Python that allow you to modify the behavior of functions or classes. In Flask, decorators are used to define routes and specify the URL patterns that should trigger specific functions.

# the most common decorator is the @app.route() decorator, which is used to define a route for a specific URL.
# when a user visits a homepage, the @app.route('/') decorator tells Flask to call the hello() function and return the string 'Hello, Flask!' as the response.

# Flasks allows you to specify HTTP methods a route should handle.
# Example:

from flask import request # we need request to handle the form submission

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        return 'Form submitted!' # handle the form submission here
    else:
        # render the form for GET requests
        return 'Submit form here.' # render the form for GET requests

# render_template() is a function provided by Flask that allows you to render HTML templates and return them as responses to client requests.

# Example:

from flask import render_template

@app.route('/greet/<name>') # This is a route that takes a dynamic parameter <name> from the URL. When a user visits /greet/some_name, the greet() function will be called with some_name as the argument for the name parameter.
def greet(name): # The name parameter is captured from the URL and passed to the function.
    return render_template('greet.html', name=name)

# Flask routing and templating

# Routing in Flask acts as the traffic director and defines the mapping 
# between URLs and corresponding Python functions responsible for handling requests. 

# Meanwhile, templating allows for the easy generation of HTML content, 
# providing a clean separation between application logic and presentation.

# Routing patterns in Flask: The URL-to-function mapping

# Flask's routing system uses decorators, which are special functions that modify the behavior 
# of other functions, to establish clear associations between URL patterns 
# and the Python functions responsible for handling them

# The `@app.route()` decorator acts as the support in this process. 

# By accepting a URL pattern as its argument, it forges a direct link between that 
# pattern and the decorated function.

# It embraces dynamic URL components enclosed within angle brackets, like `<variable_name>`.

# If there was a route defined as `@app.route('/user/<username>')`. 
# Here, `<username>` acts as a dynamic placeholder.
# When a user visits a URL like `/user/johndoe`, 
# Flask captures the value `johndoe` and passes it as an argument to the associated function, 
# allowing for personalized responses based on the URL input.

# It further enhances flexibility by offering URL pattern matching through the use of converters.
# Consider the route `@app.route('/post/<int:post_id>')`. 
# In this case, the `<int:post_id>` converter ensures that only integer values are accepted for the `post_id` parameter.

# Template syntax in Flask: Dynamic HTML generation
# Flask employs the Jinja2 templating engine to dynamically generate HTML content.

# This allows for: 
# 1) Variable substitution to seamlessly integrate dynamic data into HTML templates.
# 2) Control structures like loops and conditionals to manage the flow of content dynamically.
# 3) Template inheritance to promote code reusability and maintain a consistent layout across multiple pages.

# Variable substitution is at the heart of Jinja2's dynamic capabilities.
# E.g. <h1>Welcome, {{ username }}!</h1> 
# Here, the `{{ username }}` placeholder is replaced with the actual value of the `username` variable when the template is rendered.

# Control structures in Jinja2, such as loops and conditionals, empower developers to manage the flow of content dynamically.
# The {% if condition %} and {% endif %} tags enable conditional rendering of HTML content based on the evaluation of a Python expression
# {% for item in items %} and tags facilitate iteration over collections, allowing you to generate lists or tables.

# Template inheritance is a cornerstone of Jinja2 and a best practice for maintaining clean and reusable code.
# Base templates define the common layout elements of your web pages, such as headers, footers, and navigation menus. 

# Best practices for organizing Flask Projects:
# Structure your projects with a clear separation of concerns, 
# grouping related files and modules together.
# Use blueprints to modularize your application, making it easier to manage and scale.

# Another practice is to employ a consistent naming convention 
# for files, directories, and functions, enhancing code readability and maintainability.
# Descriptive names that accurately reflect their purpose contribute to a self-documenting codebase.

# Flask extensions are excellent resources full of pre-built tools that can significantly 
# enhance your application's functionality without requiring you to reinvent the wheel.

# Real-life scenarios where Flask is used include:

# Think of a blog application built with Flask:
# Routing plays a crucial role, mapping URLs like `/blog/<post_id>` to functions that retrieve and display specific blog posts.

# An e-commerce platform can leverage Flask's routing to handle 
# product pages, shopping carts, and checkout processes.
# from product listings (/products) and individual product pages (/products/<product_id>) to the cart and checkout process (/cart).

# Social networking sites
# Heavy reliance on routing to manage user profiles (/user/<username>), news feed (/feed), and messaging (/messages).

# Some developers might argue that these mechanisms introduce a level of complexity compared to simpler frameworks.