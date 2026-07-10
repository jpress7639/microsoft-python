# API authentication and authorization: Keeping your data secure

# API Keys - Each key is unique, ensuring that only authorized users or applications can access the resources they're intended for.
# When you want to interact with an API, you present your key, placing it within the header or as a parameter in your request 

# API's server checks if the key matches, and if it does, you're granted entry to the requested data or functionality

# Example of an API request 

import requests

api_key = 'YOUR_API_KEY'  # Replace with your actual API key
url = 'https://api.weatherapi.com/v1/current.json' 
params = {'key': api_key, 'q': 'London'}  # 'q' specifies the location

response = requests.get(url, params=params)
data = response.json()  # Convert the response to JSON format

print(data)

# This illustrative example provides a glimpse into the practical implementation of API keys in Python

# NOTE: However, it's crucial to recognize their limitations. While convenient, API keys provide only basic security. 
# To maintain the security of your API keys, it's crucial to avoid storing them directly in code repositories (such as GitHub).

# If an API key is compromised, it can result in misuse of the associated service, data breaches, and financial losses. 

# Regular rotation: Regularly rotating your API keys is a fundamental security practice. It limits the window of opportunity for an attacker to exploit a compromised key.

# Key vaults: Key vaults provide a centralized and secure location to store your API keys. 
# They offer robust encryption and access controls, ensuring that only authorized individuals or services can retrieve the keys

# Benefits of Key Vaults:

# Enhanced security: Key vaults employ strong encryption algorithms to protect your keys at rest.
# Access control: You can define granular access policies to control who can access, manage, and use your keys.
# Audit trails: Key vaults maintain detailed logs of all key access and use, providing valuable insights for security monitoring and compliance.
# Integration: Key vaults often integrate with other security tools and services, enabling a comprehensive security strategy.

# OAuth - Open Authorization 
# It's a protocol that allows users to grant third-party applications limited access to their data on another service, 
# all without having to reveal their precious passwords

# Implementing OAuth in Python typically involves using libraries like requests_oauthlib or provider-specific SDKs (Software Development Kits)

# OAuth stands out for its enhanced security. 
# By keeping passwords out of the equation, it significantly reduces the risk of unauthorized access.

# NOTE: Compared to the simplicity of API keys, implementing OAuth can be more complex.
# It involves understanding different OAuth flows, handling redirects, and managing tokens.

# JWT (JSON Web Tokens)
# serve as a sort of digital passport in the world of secure data transmission

# Each JWT has three distinct sections: 

# the header - provides metadata about the token itself, such as the algorithm used for signing
# payload - where the real information resides, containing claims or statements about the user (like their ID or role) and any other relevant data
# signature - acts as a digital seal, ensuring the token's authenticity and that it hasn't been tampered with during transit.

# You want to ensure that only authenticated users can access certain protected resources within your API.
# Upon successful login, you can issue a JWT to the user

# An example of how to create a JWT in Python using the PyJWT library.
import jwt # type: ignore

secret_key = 'YOUR_SECRET_KEY'  # Keep this secret and secure!
payload = {'user_id': 123, 'exp': 1633543343}  # 'exp' is the expiration timestamp

token = jwt.encode(payload, secret_key, algorithm='HS256')

print(token)

# NOTE: always remember the critical importance of safeguarding your secret key.
# Its compromise could jeopardize the security of your entire JWT system, potentially leading to unauthorized access and data breaches.

# The cost of cutting corners

# Implementing robust authentication and authorization mechanisms, can indeed add a layer of complexity to the development process.
# It requires careful planning, integration of libraries or SDKs, and meticulous handling of sensitive keys and tokens.

# However, it's crucial to weigh this initial effort against the potential consequences of inadequate security. 

# NOTE: A data breach, where sensitive user information is exposed, can be devastating for both your users and your reputation.