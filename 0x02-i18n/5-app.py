#!/usr/bin/env python3
"""
Module that instantiates Flask, Babel and renders a simple html page
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """
    Class to hold the languages of our app
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


def get_user():
    """
    Returns a user dictionary or None if Id cannot be found
    or if login_as was not passed
    """
    id = request.args.get('login_as', None)
    if id is not None and int(id) in users.keys():
        return (users.get(int(id)))
    return (None)


@app.before_request
def before_request():
    """
    Add user to flask.g object if user is found
    """
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale():
    """
    Select best language match:
    1 - locale from URL parameters
    2 - locale from user settings
    3 - locale from request header
    4 - default locale
    """
    loc = request.args.get('locale')
    if loc in app.config['LANGUAGES']:
        return loc
    if g.user:
        loc = g.user.get('locale')
        if loc and loc in app.config['LANGUAGES']:
            return loc
    loc = request.headers.get('locale', None)
    if loc in app.config['LANGUAGES']:
        return loc
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index():
    """
    Route to our index page
    """
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0", debug=True)
