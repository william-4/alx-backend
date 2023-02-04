#!/usr/bin/env python3
"""
Module that instantiates Flask, Babel and renders a simple html page
"""

from flask import Flask, render_template, request
from flask_babel import Babel


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

@babel.localeselector
def get_locale():
    """
    Select best language match
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index():
    """
    Route to our index page
    """
    return render_template('3-index.html')


if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0", debug=True)
