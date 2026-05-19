import sqlite3
import os
from werkzeug.security import generate_password_hash

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, '..', 'database', 'app.db')
SCHEMA_PATH = os.path.join(BASE_DIR, '..', 'database', 'schema.sql')

def init_db():
    connection = sqlite3.connect(DB_PATH)
    
    with open(SCHEMA_PATH, 'r') as file:
        connection.executescript(file.read())
    
    hashed_password = generate_password_hash('admin123')
    
    connection.execute(
        "INSERT OR IGNORE INTO users (username, password) VALUES (?, ?)",
        ('admin', hashed_password)
    )
    
    connection.commit()
    connection.close()
    print("Database initialized successfully.")

if __name__ == '__main__':
    init_db()