# API Authentication & Authorization Notes

## 1. What is an API?
- API = Application Programming Interface.
- Allows different applications to communicate and share data.
- Acts as a contract: send a request, receive a response.

## 2. REST API basics
- REST stands for Representational State Transfer.
- Works over HTTP and uses resources exposed by endpoints.
- Common HTTP methods:
  - `GET` - read data
  - `POST` - create new data
  - `PUT` - update existing data
  - `DELETE` - remove data
- Common status codes:
  - `200 OK` - success
  - `201 Created` - resource created
  - `204 No Content` - successful delete
  - `400 Bad Request` - invalid client request
  - `401 Unauthorized` - missing or invalid credentials
  - `404 Not Found` - resource missing
  - `500 Internal Server Error` - server-side issue

## 3. Request and response formats
- APIs commonly send and receive JSON.
- Example JSON payload:

```json
{
  "name": "John Doe",
  "email": "john.doe@example.com",
  "age": 30
}
```

## 4. Python `requests` library
- `requests` makes HTTP calls easy in Python.
- It handles connection setup, headers, query strings, and response parsing.
- Basic GET request:

```python
import requests

url = "https://api.example.com/data"
response = requests.get(url)
print(response.status_code)
print(response.json())
```

- POST request with JSON body:

```python
import requests

url = "https://api.example.com/users"
payload = {
    "name": "Jane Doe",
    "email": "jane.doe@example.com"
}
response = requests.post(url, json=payload)
print(response.status_code)
print(response.text)
```

- Use timeouts to avoid hanging requests:

```python
response = requests.get("https://api.example.com/data", timeout=10)
```

- Handle common errors:

```python
import requests

try:
    response = requests.get("https://api.example.com/data", timeout=10)
    response.raise_for_status()
    data = response.json()
except requests.Timeout:
    print("Request timed out")
except requests.HTTPError as err:
    print(f"HTTP error: {err}")
except requests.RequestException as err:
    print(f"Request failed: {err}")
```

## 5. Authentication vs Authorization
- Authentication = verify identity.
- Authorization = decide what that identity is allowed to do.

### Authentication methods
- API Keys: simple tokens sent with requests.
- OAuth: third-party authorization without sharing credentials.
- JWT (JSON Web Token): self-contained tokens with signed claims.

### Authorization models
- RBAC (Role-Based Access Control): access based on user role.
- ABAC (Attribute-Based Access Control): access based on attributes of user, resource, and environment.

## 6. JWT overview
- JWTs are compact tokens used for authentication and authorization.
- Structure: header, payload, signature.
- Contains claims like user ID, roles, and permissions.
- Benefits:
  - self-contained token
  - tamper-resistant signature
  - easy to send in headers

### Example: sending a bearer token

```python
import requests

url = "https://api.example.com/user/profile"
headers = {
    "Authorization": "Bearer your_jwt_token_here"
}
response = requests.get(url, headers=headers)
print(response.status_code)
print(response.json())
```

## 7. Why API security matters
- Prevents data breaches and unauthorized access.
- Protects against unauthorized transactions and system abuse.
- Keeps services reliable and user data safe.
- Good security is essential for trust and stability.

## 8. Practical API note-taking tips
- Note the endpoint, method, and required headers.
- Track the expected status codes and response format.
- Keep examples for GET, POST, and auth headers.
- Record whether the API uses API keys, OAuth, or JWT.
