#!/usr/bin/env python3
"""
Module that instantiates Flask, Babel and renders a simple html page
"""

from flask import Flask, g, render_template, request
from flask_babel import Babel, _


class Config(object):
    """
    Class to hold the languages of our app
    """
    LANGUAGES = ["en", "fr"]


def get_locale():
    # if a user is logged in, use the locale from the user settings
    user = getattr(g, 'user', None)
    if user is not None:
        return user.locale
    # otherwise try to guess the language from the user accept
    # header the browser transmits.  We support de/fr/en in this
    # example.  The best match wins.
    return request.accept_languages.best_match(Config.LANGUAGES)

def get_timezone():
    """
    Set Babel's default timezone
    """
    user = getattr(g, 'user', None)
    if user is not None:
        return user.timezone


app = Flask(__name__)
babel = Babel(app, locale_selector=get_locale, timezone_selector=get_timezone)


@app.route('/')
def index():
    """
    Route to our index page
    """
    return render_template('3-index.html')
