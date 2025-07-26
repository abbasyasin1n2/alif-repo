from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import hashlib
import os
from datetime import datetime
from functools import wraps

# Import our database module
from database import (
    init_database, get_user_by_id, get_user_by_username,
    create_user, log_activity, get_user_stats, test_connection
)

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'your-secret-key-change-this-in-production')

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Please log in to access this page.'

class User(UserMixin):
    def __init__(self, id, username, email, password_hash):
        self.id = id
        self.username = username
        self.email = email
        self.password_hash = password_hash

@login_manager.user_loader
def load_user(user_id):
    user_data = get_user_by_id(user_id)
    if user_data:
        return User(user_data['id'], user_data['username'], user_data['email'], user_data['password_hash'])
    return None

def hash_password(password):
    """Hash password using SHA-256"""
    return hashlib.sha256(password.encode()).hexdigest()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        password_hash = hash_password(password)

        user_data = get_user_by_username(username)

        if user_data and user_data['password_hash'] == password_hash:
            user_obj = User(user_data['id'], user_data['username'], user_data['email'], user_data['password_hash'])
            login_user(user_obj)

            # Log the login activity
            log_activity(user_data['id'], 'login', 'User logged in', request.remote_addr)

            flash('Logged in successfully!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password!', 'error')

    return render_template('auth/login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password != confirm_password:
            flash('Passwords do not match!', 'error')
            return render_template('auth/register.html')

        # Check if user already exists
        if get_user_by_username(username):
            flash('Username already exists!', 'error')
            return render_template('auth/register.html')

        password_hash = hash_password(password)

        # Create the user
        if create_user(username, email, password_hash):
            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('login'))
        else:
            flash('Registration failed. Please try again.', 'error')

    return render_template('auth/register.html')

@app.route('/logout')
@login_required
def logout():
    # Log the logout activity
    log_activity(current_user.id, 'logout', 'User logged out', request.remote_addr)

    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('index'))

@app.route('/dashboard')
@login_required
def dashboard():
    # Get some basic statistics for the dashboard
    stats = get_user_stats()
    return render_template('dashboard.html', stats=stats)

@app.route('/test-db')
def test_db():
    """Test database connection - useful for debugging"""
    if test_connection():
        return "Database connection successful!"
    else:
        return "Database connection failed!"

if __name__ == '__main__':
    # Test database connection first
    if not test_connection():
        print("Warning: Database connection failed!")
        print("Please check your database configuration.")
        print("See DATABASE_SETUP.md for setup instructions.")
    else:
        print("Database connection successful!")

        # Initialize database tables
        if init_database():
            print("Database initialized successfully!")
        else:
            print("Database initialization failed!")

    app.run(debug=True)
