from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # This will allow all domains

@app.route('/api/books', methods=['GET']) # takes the data and returns it in JSON format
def get_books():
    books = [
        {"id": 1, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
        {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee"},
        {"id": 3, "title": "1984", "author": "George Orwell"}
    ]
    return jsonify(books) # returns the list of books in JSON format

if __name__ == '__main__':
    app.run(debug=True) # runs the Flask application in debug mode, which provides detailed error messages and automatically reloads the server when code changes are detected.