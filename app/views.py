import urllib2
from flask import request, redirect
from app import app

@app.route('/')
@app.route('/index')

def index():
    #headers = """<link rel= "stylesheet" type= "text/css" href= "{{ url_for('static',filename='styles/mainpage.css') }}">"""
    
    body = """<html>
    <head>
    <link rel= "stylesheet" type= "text/css" href="{{ url_for('static', filename='mainpage.css')}}" }}">
    </head>
    <body>

    <h1>Heading</h1>

    <p>hello world</p>

    </body>
    </html>

    """

    page = body
    return page
