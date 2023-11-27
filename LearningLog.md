# Startup and Commands

1. To run your web application, you’ll first tell Flask where to find the application (the hello.py file in your case) 
with the FLASK_APP environment variable:


'''
export FLASK_APP=hello
'''

2. Then run it in development mode with the FLASK_ENV environment variable:

'''
export FLASK_ENV=development
'''

3. To enable debug mode you can export the FLASK_DEBUG environment variable before running the server

'''
export FLASK_DEBUG=1
'''

4. Run Flask

'''
flask run
'''

Change Port from 5000

'''
flask run -p 5001
'''

# Useful Information

Shutdown Flask
https://mikerayco.com/posts/python/terminate-flask.html
