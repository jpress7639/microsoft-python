from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Azure!"

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8000)

# On Azure, click on Create Web App, then select the resource group and app name.
# Name your web app something unique, like "flask-to-azure-demo-<yourname>".
# For the runtime stack, select Python 3.11.
# Choose Linux as the operating system and select a region close to you.
# Pick an app service plan, or create a new one. 
# Click Review + Create, then click Create to deploy your web app.