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
    string = hbnb
    return string


# Route to URL endpoint, with formatted output
@app.route('/c/string:<text>', strict_slashes=False)
def language_c(text):
    """Returns HTML formatted replaced content"""
    string = 'C is'
    return f'{string} {text}'


# Route to URL variable endpoint with a formatted default value,
@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/string:<text>', strict_slashes=False)
def language_c(text):
    """Returns HTML formatted replaced output"""
    string = 'Python is '
    return f'{string} {text.replace('_', ' ')}'



# Route to URL endpoint, with a formatted default value
@app.route('/number/int:<n>', strict_slashes=False)
def num(n):
    """Returns HTML content"""
    if n:
        return f'{n} is a number'


# Route to HTML rendered endpoint
@app.route('/number_template/int:<n>', strict_slashes=False)
def num_template(n):
    """Returns HTML rendered template"""
    if n:
        return render_template('5-number.html', number=n)
