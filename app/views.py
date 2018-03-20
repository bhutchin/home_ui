import urllib2
from flask import request, redirect
from app import app

@app.route('/')
@app.route('/index')

def index():
    
    headers = """<link rel="stylesheet" type="text/css" href="static/mainpage.css">"""
    body = """<html>
    <head>
    </head>
    <body>

    <h1>Home Control System</h1>
    <input type="button" class="button" value="Music">
    <input type="button" class="button" value="System">
    <input type="button" class="button" value="Help">
    <input type="button" class="button_lower" value="Music">
    <input type="button" class="button_lower" value="System">
    <input type="button" class="button_lower" value="Help">
    </body>
    </html>

    """

    page = body + headers
    return page
