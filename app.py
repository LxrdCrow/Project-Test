import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for, session

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')


USERNAME = 'admin'
PASSWORD = 'admin123'

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    pass #da implementare dopo

@app.route('/dashboard')
def dashboard():
    pass #implementare dopo

if __name__ == '__main__':
    app.run(debug=True)
