#!/usr/bin/python3
"""Staring a web app aplication"""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/')
def home():
    """
    function to display Hello HBNB
    """
    return 'Hello HBNB!'

@app.route('/hbnb')
def hbnb():
    """
    printing HBNB to the browser
    """
    return "HBNB"
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)