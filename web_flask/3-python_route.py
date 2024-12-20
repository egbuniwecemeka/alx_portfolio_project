from markupsafe import escape
from flask import Flask, render_template

app = Flask(__name__)


# Route to root URL endpoint
@app.route('/', strict_slashes=False)
def home_page():
    """Returns the home page"""
    string = 'Hello HBNB!'
    return string


# Route to URL endpoint
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns HTML content"""
    string = 'HBNB!'
    return string


# Route to URL endpoint, with formatted output
@app.route('/c/<string:text>', strict_slashes=False)
def language_c(text):
    """Returns HTML formatted replaced content"""
    string = 'C is '
    return f'{string} {text.replace("_", " ")}'


# Route to URL variable endpoint with a formatted default value,
@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<string:text>', strict_slashes=False)
def language_python(text):
    """Returns HTML formatted replaced output"""
    string = 'Python is '
    return f'{string} {text.replace("_", " ")}'



# Route to URL endpoint, with a formatted default value
@app.route('/number/<int:n>', strict_slashes=False)
def num(n):
    """Returns HTML content"""
    if n:
        return f'{n} is a number'


# Route to HTML rendered endpoint
@app.route('/number_template/<int:n>', strict_slashes=False)
def num_temp(n):
    """Returns HTML rendered template"""
    if n:
        return render_template('5-number.html', n=n)


# Route to HTML rendered endpoint
@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def num_temp_even_odd(n):
    """Returns HTML rendered template"""
    if n % 2 == 0:
        value = 'even'
    else:
        value = 'odd'

    return render_template('6-number_odd_or_even.html', n=n, value=value)
