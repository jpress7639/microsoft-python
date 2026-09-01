from http import client

from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

posts = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/posts', methods=['GET'])
def get_posts():
# You need to implement the /posts endpoint to handle GET requests (requests for retrieving data). This endpoint should return a list of all blog posts in JSON format.  
# The get_posts function in app.py already has a decoration for a GET at the /posts URL. The function should be modified to return the posts, encoded in JSON format.
    return jsonify(posts)


@app.route('/posts', methods=['POST'])
def create_post():

    data = request.get_json()

    if not data or 'title' not in data or 'content' not in data:
        return jsonify({"error": "Invalid data"}), 400
    # TODO: Validate the data to ensure it exists, it has a 'title' and a 'content', if not, 
    # TODO: Return an error response (400 Bad Request) with a meaningful error message
    
    new_post = {
        "id": len(posts) + 1,
        "title": data["title"],
        "content": data["content"]
    }

    posts.append(new_post)

    return jsonify(new_post), 201
    # TODO: Create a new post dictionary with an ID, title, and content from the data variable

    # TODO: Append the new post to the 'posts' list

    # TODO: Return the new post as JSON with a 201 Created status code

if __name__ == '__main__':
    app.run(debug=True)