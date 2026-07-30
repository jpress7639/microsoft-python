# The Anatomy of a RESTful API

# RESTful APIs, with their emphasis on simplicity, scalability, and statelessness, 
# have become the go-to choice for building web services.

# The client/server interaction in REST 

# This interaction revolves around resources - which represent the key data entities the API manages.
# These resources can be anything from user profiles, products, or even complex data structures.

# Each resource is assigned a URI (Uniform Resource Identifier), 
# which serves as a unique address for that resource.

# Provides a clear and organized structure in manipulating resources,
# allowing clients to perform operations like creating, reading, updating, and deleting (CRUD) resources.

# Client requests are made using standard HTTP methods, 
# The URI of the resource it wants to interact with, and optionally, a request body containing data for the operation.
# such as GET, POST, PUT, DELETE, and PATCH.
# Any additional data needed for the operation is typically sent in the request body, especially for methods like POST and PUT.

# Server responses: the server processes the request and returns a response, 
# which includes a status code (200 OK, 404 Not Found) indicating the outcome of the operation,
# along with any relevant data or error messages (formatted in JSON or XML) in the response body.

# Code Example: 

from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data for demonstration
posts = [
    {"id": 1, "title": "First Post", "content": "This is the first post."},
    {"id": 2, "title": "Second Post", "content": "This is the second post."}
]

@app.route('/api/posts', methods=['GET'])
def get_posts():   
  """Retrieves all posts."""
  return jsonify({'posts': posts})

@app.route('/api/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
  """Retrieves a specific post by ID."""
  post = next((post for post in posts if post['id'] == post_id), None)
  if post:
    return jsonify({'post': post})
  return jsonify({'message': 'Post not found'}), 404

@app.route('/api/posts', methods=['POST'])
def create_post():
  """Creates a new post."""
  new_post = request.get_json()  # Get post data from request body
  new_post['id'] = len(posts) + 1
  posts.append(new_post)
  return jsonify({'post': new_post}), 201

@app.route('/api/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
  """Updates a post with a new representation."""
  post = next((post for post in posts if post['id'] == post_id), None)
  if not post:
    return jsonify({'message': 'Post not found'}), 404
  updated_post = request.get_json()
  updated_post['id'] = post_id  # Ensure ID remains the same
  posts[post_id - 1] = updated_post
  return jsonify({'post': updated_post})

@app.route('/api/posts/<int:post_id>', methods=['PATCH'])
def partial_update_post(post_id):
  """Partially updates a post."""
  post = next((post for post in posts if post['id'] == post_id), None)
  if not post:
    return jsonify({'message': 'Post not found'}), 404
  updates = request.get_json()
  post.update(updates)  # Apply partial updates
  return jsonify({'post': post})

@app.route('/api/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
  """Deletes a post."""
  post = next((post for post in posts if post['id'] == post_id), None)
  if not post:
    return jsonify({'message': 'Post not found'}), 404
  posts.remove(post)
  return jsonify({'message': 'Post deleted'}), 204

if __name__ == '__main__':
  app.run(debug=True)

# When a client interacts with a RESTful API, it receives representations of resources
# usually in JSON or XML format. These representations provide the client with the current state of the resource,
# allowing it to make informed decisions about how to interact with the API.

# A fundamental principle of REST is statelessness, meaning that each request 
# from the client must contain all the information needed for the server to process it.

# This statelessness makes RESTful APIs scalable and reliable, 
# as servers can easily handle many concurrent requests without needing to keep track of client-specific information.

# Benefits of RESTful APIs include:
# - Simplicity and ease of use - RESTful APIs are straightforward to understand and implement, 
# making them accessible to developers of varying skill levels.

# - Interoperability - RESTful APIs can be consumed by clients built in different programming languages 
# and platforms, promoting cross-platform compatibility.

# - Evolvability - RESTful APIs can evolve over time without breaking existing clients, 
# as long as backward compatibility is maintained.

# Real-life scenario:
# A social media network can provide a RESTful API to enable developers to create applications 
# that access user profiles, posts, and feeds.
# This empowers developers to build custom clients, analytics tools, 
# and social media management platforms tailored to specific needs. 

# Code Example: a basic implementation of a RESTful API endpoint for retrieving a user's social media feed
# This is a simplified example and not a complete API implementation

# Define a class to represent a social media post
class Post:
    def __init__(self, content, author):
        self.content = content
        self.author = author

# Define a function to retrieve posts from a user's feed
def get_user_feed(user_id):
    # In a real implementation, this would involve querying a database
    # or making an API call to the social media network's server
    posts = [
        Post("Hello, world!", "user123"),
        Post("Check out this cool article!", "user456"),
    ]
    return posts

# Example usage:
user_id = "user123"
feed = get_user_feed(user_id)

for post in feed:
    print(f"{post.author}: {post.content}")