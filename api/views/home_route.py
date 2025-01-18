"""A python script that starts a Flask Web application"""

# Imported modules
from api.views import app_views
from flask import Flask, render_template, request, session, flash, redirect, url_for
from models import storage
from models.user import User
from werkzeug.security import check_password_hash, generate_password_hash


# Flask instance
app = Flask(__name__)
app.secret_key = 'your_secret_key'


# Route endpoint to Login page
@app_views.route('/login', methods=['GET', 'POST'], strict_slashes=False)
def login_page():
    """Login page"""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Query the database for the user
        # Define get_user_by_username method in storage engines
        user = storage.get_user_by_username(username)

        if user and check_password_hash(user.password, password):
            session['username'] = username # Save the username in session
            flash('Login successful', 'success')
            return redirect(url_for('app_views.home_page'))
        else:
            flash('Incorrect username or password', 'error')

    return render_template('login.html')


# Route endpoint for signup page
@app_views.route('/signup', methods=['GET', 'POST'], strict_slashes=False)
def signup_page():
    """Signup page"""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')

        # Check if user already exists
        if storage.get_user_by_username(username):
            flash('Username already exists', 'error')
        else:
            # Hash the password
            hashed_password = generate_password_hash(password)

            # Create a new user instance
            new_user = User(
                username=username,
                email=email,
                password=hashed_password,
                first_name=request.form.get('first_name', ''),
                last_name=request.form.get('last_name', '')
            )

            # Save created user to the database
            storage.new(new_user)
            storage.save()

            flash('Account created successfully, Please login', 'success')
            # Redirect to login page after successful signup
            return redirect(url_for('login_page'))
        
    return render_template('signup.html')


# route endpoint to logout
@app_views.route('/logout', strict_slashes=False)
def logout():
    """Logout"""
    session.pop('username', None) # Remove the username from the session
    flash('You were logged out', 'info')
    return redirect(url_for('login_page'))


# Route endpoint to homepage
@app_views.route('/', strict_slashes=False)
@app_views.route('/home', strict_slashes=False)
def home_page():
    """Home page"""
    if 'username' not in session:
        flash('Please login to access the home page', 'error')
        return redirect(url_for('app_views.login_page'))

    return render_template('home.html', username=session['username'])
