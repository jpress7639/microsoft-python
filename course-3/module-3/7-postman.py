# Postman: Examining API responses

# APIs or application programming interfaces are essentially sets of rules that allow different applications to communicate with each other.

# Postman is a free tool that lets you send API requests and review responses. You can think of it as a testing ground for your API calls.
# It lets you craft requests, send them off, and then analyze what comes back. 

# API rate limiting and error handling

# Rate limits - restrict the number of requests you can make in a specific timeframe
# This is due to preventing server overload, fair usage, controlling costs
# Going over rate limits can result in a user being temporarily block or permanently removed from accessing the APIs

# Tips for handling rate limits
# Respect API Limits
# Add Delays 
# Cache Often
# Upgrade as Needed 

# Errors can still occur for a multitude of reasons 
# Incorrect parameters, missing data, unsupported format
# Server-side errors where the API may be unavailable 

# Error handling is essential for your application 

# Graceful Error Handling 
# Use try-except blocks - place API calls in them without crashing the program
# Informative Error Messages - explain to the user that's concise and helpful
# Incorporate retry logic - that trys again after a little time
# Use logging - record logs with Python's tools to track 