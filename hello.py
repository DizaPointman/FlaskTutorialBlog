from flask import Flask
# importing Flask from the flask package

app = Flask(__name__)
# creating Flask application instance
# passing the special variable __name__ that holds the name of the current Python module.
# It’s used to tell the instance where it’s located—you need this because Flask sets up some paths behind the scenes


@app.route('/')
def hello():
    return 'Hello World!'

# decorator that turns a regular Python function into a Flask view function
# converts the function’s return value into an HTTP response to be displayed by an HTTP client
# pass the value '/' to @app.route() to signify that this function will respond
# to web requests for the URL /, which is the main URL
