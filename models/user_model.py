import os
import sqlite3

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.join(BASE_DIR, '..', 'database', 'app.db')

def get_db_connection():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection

def get_user_by_username(username):
    connection = get_db_connection()
    user = connection.execute(
        'SELECT * FROM users WHERE username = ?',
        (username,)
    ).fetchone()
    connection.close()
    return user

def get_user_by_id(user_id):
    connection = get_db_connection()
    user = connection.execute(
        'SELECT * FROM users WHERE id = ?',
        (user_id,)
    ).fetchone()
    connection.close()
    return user

def create_user(username, hashed_password):
    connection = get_db_connection()
    try:
        connection.execute(
            'INSERT INTO users (username, password) VALUES (?, ?)',
            (username, hashed_password)
        )
        connection.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        connection.close()

def update_username(user_id, new_username):
    connection = get_db_connection()
    try:
        connection.execute(
            'UPDATE users SET username = ? WHERE id = ?',
            (new_username, user_id)
        )
        connection.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        connection.close()

def update_password(user_id, hashed_password):
    connection = get_db_connection()
    connection.execute(
        'UPDATE users SET password = ? WHERE id = ?',
        (hashed_password, user_id)
    )
    connection.commit()
    connection.close()