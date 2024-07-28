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

@app.route('/c/<text>')
def c_with_params(text):
    """
    Displaying 'C' followed by the value in <text>
    """
    text_no_undersore = text.replace('_', ' ')
    return "C {}".format(text_no_undersore)

@app.route('/python', defaults={'text': 'is_cool'})
@app.route('/python/<text>')
def python_with_text_params(text):
    """
    displaying python is magic
    """
    text_no_underscore = text.replace('_', ' ')
    return "python{}".format(text_no_underscore)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)