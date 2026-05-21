from functools import wraps

from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from werkzeug.security import check_password_hash, generate_password_hash
from models.user_model import get_user_by_username, create_user

limiter = Limiter(
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)

auth_bp = Blueprint('auth', __name__)

# Protects routes that require authenticated session
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please log in first')
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated_function


# Rate limiting applied to prevent brute-force login attempts
@auth_bp.route('/login', methods=['GET', 'POST'])
@limiter.limit("10 per minute")
def login():
    if 'user_id' in session:
        return redirect(url_for('main.dashboard'))

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if not username or not password:
            flash('Please enter username and password')
            return redirect(url_for('auth.login'))

        user = get_user_by_username(username)

        if not user or not check_password_hash(user['password'], password):
            flash('Invalid credentials')
            return redirect(url_for('auth.login'))

        session['user_id'] = user['id']
        session['username'] = user['username']

        flash('Login successful')
        return redirect(url_for('main.dashboard'))

    return render_template('login.html')


@auth_bp.route('/register', methods=['GET', 'POST'])
@limiter.limit("10 per hour")
def register():
    if 'user_id' in session:
        return redirect(url_for('main.dashboard'))

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if not username or not password:
            flash('Please fill all fields')
            return redirect(url_for('auth.register'))

        if len(password) < 8:
            flash('Password must be at least 8 characters long')
            return redirect(url_for('auth.register'))

        hashed_password = generate_password_hash(password)
        success = create_user(username, hashed_password)

        if not success:
            flash('Username already exists')
            return redirect(url_for('auth.register'))

        flash('Registration successful')
        return redirect(url_for('auth.login'))

    return render_template('register.html')


@auth_bp.route('/logout')
@login_required
def logout():
    session.clear()
    flash('You have been logged out')
    return redirect(url_for('auth.login'))