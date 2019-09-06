#!/usr/bin/python3
""" starts a Flask web application"""
from flask import Flask, render_template
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    """display “Hello HBNB!”"""
    return 'Hello HBNB!'

@app.route('/hbnb')
def hbnb():
    """ display “HBNB”"""
    return 'HBNB'

@app.route('/c/<text>')
def c(text):
    '''display “C ” followed by the value of the text'''
    return('C {}'.format(text.replace('_', ' ')))

@app.route('/python/')
def py():
    """ The default value of text is “is cool”"""
    return("Python is cool")

@app.route('/python/<text>')
def pyis(text):
    """display “Python ”, followed by the value of the text variable """
    return("Python {}".format(text.replace("_", " "))

@app.route('/number/<int:n>')
def isnum(n):
''' display only if is a numer '''
    return '{:d} is a number'.format(n)

@app.route('/number_template/<int:n>')
def num_temp(n):
''' display a HTML page only if n is an integer: '''
    return render_template('5-number.html', n=n)

@app.route('/number_odd_or_even/<int:num>')
def is_odd_or_even(num):
""" display a HTML page only if n is an integer"""
    return render_template('6-number_odd_or_even.html', n=n)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
