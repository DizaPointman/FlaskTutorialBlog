import sqlite3
from flask import Flask, render_template

# import the render_template() helper function that lets you render
# HTML template files that exist in the templates folder you’re about to create

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


app = Flask(__name__)


@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)

# index() view function returns the result of calling render_template() with
# index.html as an argument, this tells render_template() to look for a file
# called index.html in the templates folder
