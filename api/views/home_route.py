"""A python script that starts a Flask Web application"""

# Imported modules
from api.views import app_views
from flask import (
    render_template, request, session, flash, redirect, url_for,jsonify
)
from models import storage
from models.user import User
from werkzeug.security import check_password_hash, generate_password_hash


# Route endpoint to Login page
@app_views.route('/login', methods=['GET', 'POST'], strict_slashes=False)
def login_page():
    """Login page and API endpoint for authentication"""
    if request.method == 'POST':
        # handle API requests of content type JSON
        if request.content_type == 'application/json':
            data = request.json
            username = data.get('username')
            password = data.get('password')

            if not username or not password:
                return jsonify({'error': 'Missing username or password'}), 400
            
            # Query the database for the user
            # Define get_user_by_username method in storage engines
            user = storage.get_user_by_username(username)

            if user and check_password_hash(user.password, password):
                 # Save the username and user_id in session
                session['username'] = username
                session['user_id'] = user.id
                return jsonify({'message': 'Login successful', 'user_id': user.id}), 200
                # return redirect(url_for('app_views.home_page'))
            else:
                return jsonify({'error': 'Incorrect username or password'})
            
        # Handle form submission    
        else:
            username = request.form.get('username')
            password = request.form.get('password')

            # Query the database for the user
            user = storage.get_user_by_username(username)

            if user and check_password_hash(user.password, password):
                # Save user in the sesion
                session['username'] = username
                session['user_id'] = user.id
                flash('Login successful', 'success')
                return  redirect(url_for('app_views.home_page'))
            else:
                flash('Incorrect username or password', 'error')
                return redirect(url_for('app_views.login_page'))

    # Otherwise, render login page for GET request
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
