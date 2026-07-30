# A practical example of consuming an external API

import requests

api_key: str = "YOUR_API_KEY"  # Replace with your actual API key
city: str = "New York"  # Replace with the desired city name

url: str = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
# the URL is including the API key and the city name as query parameters 
# to fetch the weather data for that specific city.

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    weather_description = data['weather'][0]['description']
    temperature = data['main']['temp']
    print(f"Weather in {city}: {weather_description}, Temperature: {temperature}K")
else:
    print(f"Failed to retrieve weather data. Status code: {response.status_code}")

# Keeping your data secure with API authentication and authorization

# Authentication vs. authorization
# Authentication is the process of verifying the identity of a user or application 
# attempting to access an API.

# Authorization is the process of determining whether the authenticated user or application
# has the necessary permissions to access specific resources or perform certain actions.

# Once the individual or application’s identity has been verified through the authentication 
# is when the authorization steps in to determine what actions 
# the authenticated user or application is permitted to perform within the API's ecosystem.

# Authorization confirms that even authenticated users can only perform actions they are explicitly allowed to do. 

# Authentication methods
# API Key: A unique identifier provided to developers to access an API.
# NOTE: it's crucial to handle API keys with care, as their exposure can lead to unauthorized access

# OAuth: A token-based authentication protocol that allows users to grant 
# third-party applications access to their resources without sharing their credentials.
# OAuth achieves this by providing a secure and user-friendly way to authorize access, 
# enhancing both security and user experience

# JWT (JSON Web Token): A compact, URL-safe token format that is used for 
# securely transmitting information between parties as a JSON object.
# JWTs are particularly well-suited for stateless API communication, 
# where maintaining session information on the server can be challenging.

# Best practices for securing API access

# NOTE: APIs are susceptible to abuse and denial-of-service attacks, 
# where malicious actors flood the API with excessive requests, 
# potentially overwhelming the system and disrupting service for legitimate users.
# NOTE: Rate limiting acts as a traffic controller, 
# restricting the number of requests an API can handle within a given timeframe. 
# You can prevent abuse, ensure fair access to all users, 
# and maintain the stability and performance of your API by implementing rate limiting.

# Input validation: Validate incoming data to prevent injection attacks 
# and ensure that only valid and expected data is processed by the API.

# It is important to use encryption for data protection, both in transit and at rest.
# Encryption at rest: Encrypt sensitive data stored on the server to protect it from unauthorized access.
# Encryption in transit: Use secure communication protocols (e.g., HTTPS) 
# to encrypt data transmitted between clients and the API server, preventing eavesdropping and tampering.
# HTTPS: Use HTTPS to encrypt data in transit, 
# ensuring that sensitive information such as API keys and user data is transmitted securely.

# By maintaining comprehensive logs of API activity, you provide valuable insights into usage patterns and potential security incidents. 