from functools import wraps

from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    session,
    flash,
    make_response
)

from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from werkzeug.security import (
    check_password_hash,
    generate_password_hash
)

from models.user_model import (
    get_user_by_username,
    get_user_by_id,
    create_user,
    update_password
)

limiter = Limiter(
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)

auth_bp = Blueprint('auth', __name__)


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):

        if 'user_id' not in session:
            flash('Please log in first')
            return redirect(url_for('auth.login'))

        return f(*args, **kwargs)

    return decorated_function


@auth_bp.route('/login', methods=['GET', 'POST'])
@limiter.limit("10 per minute")
def login():

    if 'user_id' in session:
        return redirect(url_for('auth.dashboard'))

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        if not username or not password:
            flash('Please enter username and password')
            return redirect(url_for('auth.login'))

        user = get_user_by_username(username)

        if not user:
            flash('Invalid credentials')
            return redirect(url_for('auth.login'))

        if not check_password_hash(user['password'], password):
            flash('Invalid credentials')
            return redirect(url_for('auth.login'))

        session['user_id'] = user['id']
        session['username'] = user['username']

        flash('Login successful')

        return redirect(url_for('auth.dashboard'))

    return render_template('login.html')


@auth_bp.route('/dashboard')
@login_required
def dashboard():

    response = make_response(render_template(
        'dashboard.html',
        username=session['username']
    ))

    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'

    return response

@auth_bp.route('/logout')
@login_required
def logout():

    session.clear()

    flash('You have been logged out')

    return redirect(url_for('auth.login'))


@auth_bp.route('/register', methods=['GET', 'POST'])
@limiter.limit("10 per hour")
def register():

    if 'user_id' in session:
        return redirect(url_for('auth.dashboard'))

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        if not username or not password:
            flash('Please fill all fields')
            return redirect(url_for('auth.register'))

        if len(password) < 12:
            flash('Password must be at least 12 characters long')
            return redirect(url_for('auth.register'))

        hashed_password = generate_password_hash(password)

        success = create_user(username, hashed_password)

        if not success:
            flash('Username already exists')
            return redirect(url_for('auth.register'))

        flash('Registration successful')

        return redirect(url_for('auth.login'))

    return render_template('register.html')


@auth_bp.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():

    user = get_user_by_id(session['user_id'])

    if request.method == 'POST':

        current_password = request.form['current_password']
        new_password = request.form['new_password']
        confirm_password = request.form['confirm_password']

        if not check_password_hash(user['password'], current_password):
            flash('Current password is incorrect')
            return redirect(url_for('auth.profile'))

        if len(new_password) < 12:
            flash('Password must be at least 12 characters long')
            return redirect(url_for('auth.profile'))

        if new_password != confirm_password:
            flash('Passwords do not match')
            return redirect(url_for('auth.profile'))

        hashed_password = generate_password_hash(new_password)

        update_password(session['user_id'], hashed_password)

        flash('Password updated successfully')

        return redirect(url_for('auth.profile'))

    return render_template('profile.html', user=user)