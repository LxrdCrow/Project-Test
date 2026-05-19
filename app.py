import os
import sqlite3

from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import check_password_hash, generate_password_hash
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

limiter = Limiter(
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
) # Initialize the limiter for rate limiting

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

DATABASE = 'database/app.db'

def get_db_connection():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection

@app.route('/login', methods=['GET', 'POST'])
@limiter.limit("5 per minute")
def login():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if not username or not password:
            return render_template('login.html', error='Please enter both username and password') # Validate that both fields are filled
        if len(password) < 8:
            return render_template('login.html', error='Password must be at least 8 characters long') # Validate password length

        connection = get_db_connection()
        user = connection.execute(
            'SELECT * FROM users WHERE username = ?',
            (username,) # Use a tuple for the parameter to prevent SQL injection
        ).fetchone()
        connection.close()

        if user and check_password_hash(user['password'], password):
            session['user_id'] = user['id']
            session['username'] = user['username']
            return redirect(url_for('dashboard'))

        return render_template('login.html', error='Invalid credentials')

    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html', username=session['username'])


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
@limiter.limit("10 per hour") # Limit registration attempts to prevent abuse
def register():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Input validation: Ensure username and password are provided and meet basic criteria
        if not username or not password:
            return render_template('register.html', error='Please enter both username and password')
        if len(password) < 8:
            return render_template('register.html', error='Password must be at least 8 characters long')

        hashed_password = generate_password_hash(password)

        connection = get_db_connection()
        try:
            connection.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)",
                (username, hashed_password)
            )
            connection.commit()
        except sqlite3.IntegrityError:
            return render_template('register.html', error='Username already exists')
        finally:
            connection.close()

        return redirect(url_for('login'))

    return render_template('register.html')