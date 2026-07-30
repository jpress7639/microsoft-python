# Building a RESTful API with Flask-Restful

from flask import Flask, jsonify, request
from flask_restful import Api, Resource # type: ignore

app = Flask(__name__)
api = Api(app)

class BookList(Resource):
    def get(self):
        # logic to retrieve all books
        return {'books': ["The Lord of the Rings", "Pride and Prejudice", "To Kill a Mockingbird", "1984", "Harry Potter and the Sorcerer's Stone"]}
        # replace with actual data 

    def post(self):
        # Logic to create a new book
        data = request.get_json()  # Get book data from request body
        new_book = data.get('title')  # Extract the book title from the request data
        return {'message': 'Book created successfully', 'book': new_book}, 201

    class Book(Resource):
        def get(self, book_id):
            # Logic to retrieve a specific book
            return {'book': f"Book with ID {book_id}"}

        def put(self, book_id):
        # Logic to update a specific book
            data = request.get_json()  # Get updated book data from request body
            updated_book = data.get('title')  # Extract the updated book title from the request data
            return {'message': 'Book updated successfully', 'book': updated_book}

        def delete(self, book_id):
            # Logic to delete a specific book
            return {'message': f'Book with ID {book_id} deleted successfully'}

api.add_resource(BookList, '/api/books')
api.add_resource(BookList.Book, '/api/books/<int:book_id>')

if __name__ == '__main__':
    app.run(debug=True)

# Best practices

# Use meaningful resource names: Use plural nouns for resource names 
# (e.g., /api/books) to represent collections of resources.

# Return appropriate HTTP status codes: Use standard HTTP status codes 
# to indicate the outcome of API requests (e.g., 200 OK, 201 Created, 404 Not Found).

# Handle errors gracefully: Provide meaningful error messages and appropriate status 
# codes for error scenarios (e.g., 400 Bad Request, 404 Not Found).

# Consider security and authentication: Implement authentication and authorization 
# mechanisms to protect sensitive resources and ensure that only authorized users can access them.

# Document your API: Provide clear and comprehensive documentation for your API endpoints, 
# including request/response formats, available methods, and any authentication requirements.