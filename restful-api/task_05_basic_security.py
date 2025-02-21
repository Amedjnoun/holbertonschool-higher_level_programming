#!/usr/bin/python3

"""
Simple secure API using Python & Flask
"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
auth = HTTPBasicAuth()

# In-memory user storage
users = {
    "user1": generate_password_hash("password1"),
    "admin": generate_password_hash("adminpass")
}

# In-memory user roles
user_roles = {
    "user1": "user",
    "admin": "admin"
}


app.config['JWT_SECRET_KEY'] = '0123456789'
jwt = JWTManager(app)


@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(
            users.get(username), password):
        return username


@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    return jsonify(message="Basic Auth: Access Granted")


@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if (username not in users or
            not check_password_hash(users.get(username), password)):
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)


@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    return jsonify(message="JWT Auth: Access Granted")


@app.route('/admin-only')
@jwt_required()
def admin_only():
    current_user = get_jwt_identity()
    if user_roles.get(current_user) != 'admin':
        return jsonify({"error": "Admin access required"}), 403
    return jsonify(message="Admin Access: Granted")


if __name__ == '__main__':
    app.run(debug=True)
