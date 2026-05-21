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

from werkzeug.security import (
    check_password_hash,
    generate_password_hash
)

from models.user_model import (
    get_user_by_username,
    get_user_by_id,
    update_password,
    update_username
)

from controllers.auth import login_required

main_bp = Blueprint('main', __name__)


@main_bp.route('/dashboard')
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


@main_bp.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():

    user = get_user_by_id(session['user_id'])

    if request.method == 'POST':

        action = request.form.get('action')

        # CHANGE USERNAME
        if action == 'change_username':

            new_username = request.form['new_username'].strip()

            if not new_username:
                flash('Username cannot be empty')
                return redirect(url_for('main.profile'))

            if new_username == session['username']:
                flash('New username must be different from current one')
                return redirect(url_for('main.profile'))

            # FIX: check BEFORE updating DB
            existing_user = get_user_by_username(new_username)

            if existing_user and existing_user['id'] != session['user_id']:
                flash('Username already taken')
                return redirect(url_for('main.profile'))

            update_username(session['user_id'], new_username)
            session['username'] = new_username

            flash('Username updated successfully')
            return redirect(url_for('main.profile'))

        # CHANGE PASSWORD
        if action == 'change_password':

            current_password = request.form['current_password']
            new_password = request.form['new_password']
            confirm_password = request.form['confirm_password']

            full_user = get_user_by_username(session['username'])

            if not check_password_hash(
                full_user['password'],
                current_password
            ):
                flash('Current password is incorrect')
                return redirect(url_for('main.profile'))

            if current_password == new_password:
                flash('New password must be different from current password')
                return redirect(url_for('main.profile'))

            if len(new_password) < 8:
                flash('Password must be at least 8 characters long')
                return redirect(url_for('main.profile'))

            if new_password != confirm_password:
                flash('Passwords do not match')
                return redirect(url_for('main.profile'))

            hashed_password = generate_password_hash(new_password)

            update_password(
                session['user_id'],
                hashed_password
            )

            flash('Password updated successfully')

            return redirect(url_for('main.profile'))

    return render_template(
        'profile.html',
        user=user
    )