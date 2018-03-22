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
    <div class="hcs">
        <h1>Home Control System</h1>
    </div>
    <body>
    <div class="grid-container">
        <div class="grid-item">
            <input type="button" class="button" value="Music">
            <input type="button" class="button" value="System">
            <input type="button" class="button" value="Help">
        </div>
        <div class="grid-item">
            <input type="button" class="button_lower" value="Music">
            <input type="button" class="button_lower" value="System">
            <input type="button" class="button_lower" value="Help">
        </div>
    </div>
    </body>
    </html>

    """

    page = body + headers
    return page

def contact():
    if "help" in requests.form:
        print "blah"

