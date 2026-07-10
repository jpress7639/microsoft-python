# Understanding REST APIs: The basics

# REST APIs, or  Representational State Transfer Application Programming Interfaces, have emerged as a cornerstone of modern web development.

# What is a REST API?
# REST APIs operate on a similar principle, facilitating communication between clients (users or other applications) and servers.

# They adhere to a set of architectural constraints that promote simplicity, scalability, and maintainability.
# At its core, a REST API exposes a collection of resources, which can be any piece of data or functionality that the server manages.

# Endpoints: The gateways to resources
# Endpoints - are the entry points for interacting with specific resources within a REST API
# Each endpoint is associated with a specific URL and represents a distinct resource or action.

# Example: in a social media API, an endpoint like /users might retrieve a list of all users, 
# while /users/12345 might fetch information about a specific user with ID 12345.

# HTTP Methods - often referred as verbs, are action words in REST APIs
# They dictate the operations that clients can execute on the resources exposed by the API

# Common HTTP Methods:

# GET - for retrieving information - asking a question to the API and receiving an answer in return 
# POST - used to create new resources - e.g. if you want to add a new user to the system
# PUT - all about updating existing information - e.g. you need to modify the details of a specific user
# DELETE - is used to remove resources - e.g. removing a user from the system

# Status codes 
# Status codes are three-digit numerical codes that indicate the outcome of an API request.
# They provide valuable feedback to clients about the success or failure of their requests, along with additional information about the nature of the response.

# 200 - A successful GET request would return 200 OK, if it doesn't exist, you'll get a 404 Not Found
# 201 - A successful POST request, if there's a problem with the data - you'll get a 400 Bad Request 
# 200 - A successful PUT request returns, you could get a 400 Bad Request 
# 204 No Content - if there's a successful DELETE request, a server-side error could occur for a 500 Internal Server Error 

# Other Status codes 
# 504 Gateway Timeout if the server is waiting on another server
# 202 Accepted if the server has accepted your request but hasn't processed it yet.

# Request/response formats
# REST APIs exchange data between clients and servers using standardized formats like JSON (JavaScript Object Notation) or XML (Extensible Markup Language)

# Nonfunctional JSON Code Example
{
    "name": "John Doe",
    "email": "john.doe@example.com",
    "age": 30
}

# Nonfunctional XML Code Example
""" <user>
    <name>John Doe</name>
    <email>john.doe@example.com</email>
    <age>30</age>
</user> """

# The role of REST APIs in modern software development

# REST APIs have revolutionized the way software applications interact and exchange data, 
# fostering a landscape of interconnected services and enabling the creation of powerful and flexible web applications.

# As a Python developer, mastering the concepts of REST APIs empowers you to leverage the vast ecosystem of web services, 
# build robust and scalable applications, and contribute to the ever-evolving world of software development.
