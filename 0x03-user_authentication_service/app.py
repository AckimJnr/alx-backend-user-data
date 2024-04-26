#!/usr/bin/env python3
""" Main application file for the Flask API."""
from flask import Flask, jsonify, request
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'])
def home():
    """Home route."""
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def users():
    """register a new user."""
    email = request.form.get('email')
    password = request.form.get('password')

    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"}), 200
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'])
def login(email: str, password: str) -> str:
    """login user."""
    email = request.form.get('email')
    password = request.form.get('password')
    if AUTH.valid_login(email, password):
        session_id = AUTH.create_session(email)
        return jsonify(
            {"email": email,
             "message": "logged in",
             "session_id": session_id}), 200
    return jsonify({"message": "wrong password"}), 401


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
