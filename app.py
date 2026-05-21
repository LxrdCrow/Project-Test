import os
from dotenv import load_dotenv
from flask import Flask, redirect, url_for
from controllers.auth import auth_bp, limiter
from controllers.main import main_bp

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')
app.config['SESSION_PERMANENT'] = False

limiter.init_app(app)
app.register_blueprint(auth_bp)
app.register_blueprint(main_bp)

@app.route('/')
def index():
    return redirect(url_for('auth.login'))

if __name__ == '__main__':
    app.run(debug=True)