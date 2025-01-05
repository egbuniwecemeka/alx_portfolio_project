"""A python script that starts a Flask Web application"""
from flask import Flask, render_template

# Flask instance
app = Flask(__name__)


# Route definition to URL triggering function
@app.route('/home', strict_slashes=False)
def home_page():
    return render_template('home.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
