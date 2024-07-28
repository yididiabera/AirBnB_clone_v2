#!/usr/bin/python3
"""A module that starts a flask web app"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Returns the content at the index route"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns the content at the hbnb route"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """Returns the content at the /c/<text> route"""
    return "C " + text.replace("_", " ")


@app.route('/python/', defaults={'text': 'is cool'})
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text):
    """Returns the content at the /python/<text> route"""
    return "Python " + text.replace("_", " ")


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """Returns the content at the /number/<n> route"""
    return "%d is a number" % n


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
