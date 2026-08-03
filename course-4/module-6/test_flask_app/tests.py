from flask import Flask, jsonify, request 
from flask_testing import TestCase 

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({'message': 'Hello, World!'})

# Create a test scenario:
class MyTestCase(TestCase): # this class inherits from TestCase
    def create_app(self): # this method is required to create the app instance for testing
        app.config['TESTING'] = True # Set the testing configuration to True
        return app

def test_index(self): # this method tests the index route
    response = self.client.get('/') # Make a GET request to the index route
    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.json, {'message': 'Hello, World!'})