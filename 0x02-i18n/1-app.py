#!/usr/bin/env python3
"""
Module that instantiates Flask, Babel and renders a simple html page
"""

from flask import Flask, render_template
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


@app.route('/', strict_slashes=False)
def index():
    """
    Route to our index page
    """
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0", debug=True)
