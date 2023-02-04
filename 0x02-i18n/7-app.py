#!/usr/bin/env python3
""" Starts a Flask Web Application """

from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Dict, Union
from datetime import timezone as tmzn
from pytz import timezone
import pytz.exceptions


app = Flask(__name__)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """ Config for a Flask app. """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


def get_user():
    """
    Returns a user dictionary or None if ID value can't be found
    or if 'login_as' URL parameter was not found
    """
    id = request.args.get('login_as', None)
    if id is not None and int(id) in users.keys():
        return users.get(int(id))
    return None


@app.before_request
def before_request():
    """
    Add user to flask.g if user is found
    """
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale():
    """
    Select and return best language match based on supported languages
    """
    local = request.args.get('locale')
    if local in app.config['LANGUAGES']:
        return local
    if g.user:
        local = g.user.get('locale')
        if local and local in app.config['LANGUAGES']:
            return local
    local = request.headers.get('locale', None)
    if local in app.config['LANGUAGES']:
        return local
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """
    Select and return appropriate timezone
    """
    tzone = request.args.get('timezone', None)
    if tzone:
        try:
            return timezone(tzone).zone
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    if g.user:
        try:
            tzone = g.user.get('timezone')
            return timezone(tzone).zone
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    dflt = app.config['BABEL_DEFAULT_TIMEZONE']
    return dflt


@app.route('/', strict_slashes=False)
def hello_world():
    """/ route handler. """
    return render_template('7-index.html')


if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0", debug=True)
