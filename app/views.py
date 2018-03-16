import urllib2
from flask import request, redirect
from app import app

@app.route('/')
@app.route('/index')

def index():
    page =  "hello world"

    return page
