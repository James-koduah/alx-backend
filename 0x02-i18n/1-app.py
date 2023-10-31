#!/usr/bin/env python3
"""
basic flask app
"""
from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """Config class for our app"""
    LANGUAGES = ['en', 'es']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route("/", strict_slashes=False)
def hello():
    """A route that returns a welcome string"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run('0.0.0.0', 5000)
