# Flask Authentication Project

A simple Flask web application developed as a technical test.

The project implements a user authentication system with login, registration, dashboard access, profile management, logout, and password/username updates.  
It also includes security-focused improvements such as password hashing, session handling, rate limiting, and protected routes.

## Features

- User login
- User registration
- Session-based authentication
- Protected dashboard
- Profile page with:
  - username update
  - password update
- Logout functionality
- Flash messages for user feedback
- Password hashing with Werkzeug
- Rate limiting on sensitive routes
- SQLite database integration
- Modular project structure with separate controllers and models

## Project Structure

```text
project/
├── app.py
├── controllers/
│   ├── auth.py
│   └── main.py
├── models/
│   └── user_model.py
├── database/
│   ├── app.db
│   ├── init_db.py
│   └── schema.sql
├── templates/
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   └── profile.html
├── static/
├── requirements.txt
└── .env
````

## Requirements

* Python 3
* Flask
* SQLite
* Werkzeug
* python-dotenv
* Flask-Limiter

## How to Run the Project

1. Create and activate the virtual environment.

```bash
python -m venv .venv
```

On Windows:

```bash
.venv\Scripts\activate
```

2. Install the dependencies.

```bash
pip install -r requirements.txt
```

3. Initialize the database.

```bash
python database/init_db.py
```

4. Run the application.

```bash
python app.py
```

5. Open the application in your browser.

```text
http://127.0.0.1:5000
```

## Default Credentials

For the initial test user:

* Username: `admin`
* Password: `admin123`

## Implemented Level

This project reaches the **Advanced** level of the test.

It includes all the required base and intermediate features, plus additional improvements such as:

* modular code organization
* route protection with decorators
* secure password hashing
* flash messages
* profile management
* rate limiting
* `.env` configuration support

## Notes

* The application uses SQLite for lightweight local storage.
* Passwords are not stored in plain text.
* The root route redirects to the login page.
* The browser must be opened manually after starting the Flask server.








