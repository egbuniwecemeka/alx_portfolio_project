"""A python script that starts a Flask Web application"""
from flask import Flask

app = Flask(__name__)


# Route definition
@app.route('/', strict_slashes=False)
def home_page():
    return "<p>Hello World!</p>"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
