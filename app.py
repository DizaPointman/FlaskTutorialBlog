from flask import Flask, render_template

# import the render_template() helper function that lets you render
# HTML template files that exist in the templates folder you’re about to create

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

# index() view function returns the result of calling render_template() with
# index.html as an argument, this tells render_template() to look for a file
# called index.html in the templates folder
