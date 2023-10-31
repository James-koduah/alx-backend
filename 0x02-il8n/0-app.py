#!/usr/bin/env python3
"""
basic flask app
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """A route that returns a welcome string"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run('0.0.0.0', 5000)
