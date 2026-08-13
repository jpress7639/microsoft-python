# Deploying Python Apps to Cloud Summary

# Deployment is packaging your Python code, dependencies, and configuration, 
# then making it available as an application (via VMs, containers, serverless, or PaaS like Azure App Service).

# Virtual Machines (VMs) emulate full computers: you manage OS, runtime, and app; 
# good when you need full control or specific system dependencies.

# Containers package your app and dependencies in a lightweight, portable unit;
# they run consistently across environments and are great for microservices.

# Serverless functions run code in response to events without managing servers;
# they scale automatically and are cost-effective for event-driven workloads.

# Flask application basics: a typical entry point exposes an app object:
from flask import Flask, app
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, world!"

# Azure App Service is a PaaS that hosts web apps, APIs, and mobile backends;
# it abstracts infrastructure management, allowing you to focus on code.

# Azure Functions is a serverless compute service that runs code in response to events;
# it automatically scales and is ideal for event-driven workloads.

# Kubernetes is an open-source container orchestration platform that automates deployment, scaling, and management of containerized applications;
# it provides features like automated rollouts, service discovery, load balancing, and self-healing.

# Common mistakes to watch out for:
# 1. Not specifying dependencies in requirements.txt or Pipfile.
# 2. Not configuring the app for production (e.g., using debug mode in Flask).
# 3. Not setting environment variables for sensitive information.
# 4. Confusing pods and services in Kubernetes; pods are the smallest deployable units,
# while services provide stable endpoints for accessing pods.

# 5. Treating Kubernetes containers as the smallest unit: in Kubernetes, 
# the smallest deployable unit is a pod, which can contain one or more tightly coupled containers