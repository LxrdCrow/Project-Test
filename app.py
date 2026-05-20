import os
from dotenv import load_dotenv
from flask import Flask, redirect, url_for
from controllers.user_controller import auth_bp, limiter

load_dotenv()

app = Flask(__name__)
app.config['SESSION_PERMANENT'] = False
app.secret_key = os.getenv('SECRET_KEY')


limiter.init_app(app)
app.register_blueprint(auth_bp)


@app.route('/')
def index():
    return redirect(url_for('auth.login'))


if __name__ == '__main__':
    app.run(debug=True)