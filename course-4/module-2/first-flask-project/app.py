#!/usr/bin/env python3
# --*- coding: utf-8 -*-

from flask import Flask # reminder the Flask must be captialized because it is a class. The Flask class is the main entry point for creating a Flask web application.

app=Flask(__name__) # this creates a new Flask web application instance. The __name__ variable is a special Python variable that is set to the name of the module in which it is used. When you run a Python script, __name__ is set to '__main__', so this line tells Flask to use the current module as the application.

@app.route('/') # This is a decorator that tells Flask what URL should trigger the function that follows. In this case, it means that when the root URL ("/") of the web application is accessed, the hello() function will be called.

def hello():
    return 'Hello, Flask!'

if __name__ == '__main__':
    app.run(debug=True) # debug=True means that the server will automatically reload for code changes and show an interactive debugger in the browser if an error occurs.