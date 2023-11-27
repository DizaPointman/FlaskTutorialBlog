# Startup and Commands

1. To run your web application, you’ll first tell Flask where to find the application 
(the hello.py file in your case) with the FLASK_APP environment variable:
~~~
export FLASK_APP=hello
export FLASK_APP=app
~~~

2. Then run it in development mode with the FLASK_ENV environment variable:
~~~
export FLASK_ENV=development
~~~

3. To enable debug mode you can export the FLASK_DEBUG environment variable before running the server
~~~
export FLASK_DEBUG=1
~~~

4. Run Flask
~~~
flask run
~~~

5. Shutdown Flask
~~~
CTRL + C
~~~

Change Port from 5000
~~~
flask run -p 5001
~~~

# Flask Structure

## Rootfolder

app.py

templates/index.html

static/css/style.css

## Stylesheet link
~~~
<link rel="stylesheet" href="{{ url_for('static', filename= 'css/style.css') }}">
~~~

# Useful Information

Shutdown Flask
https://mikerayco.com/posts/python/terminate-flask.html

Bootstrap
https://getbootstrap.com/

Template Inheritance
https://jinja.palletsprojects.com/en/2.10.x/templates/#template-inheritance
