#!/usr/bin/env python3
"""
Module that instantiates Flask and renders a simple html page
"""

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    """
    route to our index page
    """
    return render_template('0-index.html')
