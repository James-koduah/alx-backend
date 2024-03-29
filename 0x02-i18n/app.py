#!/usr/bin/env python3
"""
basic flask app
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
import pytz
from datetime import datetime


app = Flask(__name__)
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """Config class for our app"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route("/")
def hello():
    """A route that returns a welcome string"""
    return render_template('index.html')


@babel.localeselector
def get_locale():
    """Select language locale"""

    language = request.args.get('locale')
    if language in app.config['LANGUAGES']:
        return language

    if g.user:
        lan = g.user.get('locale')
        if lan is not None and lan in app.config['LANGUAGES']:
            return lan

    lang = request.headers.get('locale')
    if lang in app.config['LANGUAGES']:
        return lang

    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    """Get a user from the mock database"""
    id = request.args.get('login_as')
    if id:
        try:
            user = users.get(int(id))
            return user
        except Exception as e:
            return None
    return None


@babel.timezoneselector
def get_timezone():
    """Get the timezone"""
    zone = request.args.get('timezone')
    if zone in pytz.all_timezones:
        return zone
    else:
        raise pytz.exceptions.UnknownTimeZoneError

    if g.user:
        zone = g.user.get('timezone')
        if zone and zone in pytz.all_timezone:
            return zone
        else:
            raise pytz.exceptions.UnknwnTimeZoneError

    return app.config['BABEL_DEFAULT_TIMEZONE']


@app.before_request
def before():
    """Executed before all other functions"""
    g.user = get_user()
    fmt = "%b %d, %Y %I:%M:%S %p"
    time_now = pytz.utc.localize(datetime.utcnow())
    time = time_now.astimezone(pytz.timezone(get_timezone()))
    g.time = time.strftime(fmt)


if __name__ == '__main__':
    app.run()
