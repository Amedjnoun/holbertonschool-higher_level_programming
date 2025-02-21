from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager, create_access_token, get_jwt_identity, jwt_required
)
import datetime
"""
basic security
"""
app = Flask(__name__)

# Setup JWT
app.config['JWT_SECRET_KEY'] = '1234567890'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(hours=1)
jwt = JWTManager(app)
auth = HTTPBasicAuth()

# In-memory user store
users = {
    "user1": {
        "password": generate_password_hash("password1"),
        "role": "user"
    },
    "admin": {
        "password": generate_password_hash("adminpass"),
        "role": "admin"
    }
}


@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(
            users[username]["password"], password):
        return username
    return None


# Basic Auth protected route
@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    return jsonify({"message": "Basic Auth: Access Granted"})


# Login route for JWT
@app.route('/login', methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({"error": "Missing JSON"}), 400

    username = request.json.get('username', None)
    password = request.json.get('password', None)

    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 400

    if (username not in users or
            not check_password_hash(users[username]["password"], password)):
        return jsonify({"error": "Invalid credentials"}), 401

    # Create token with role information
    access_token = create_access_token(
        identity=username,
        additional_claims={"role": users[username]["role"]}
    )
    return jsonify({"token": access_token})


# JWT protected route
@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    return jsonify({"message": "JWT Auth: Access Granted"})

# Admin only route


@app.route('/admin-only')
@jwt_required()
def admin_only():
    current_user = get_jwt_identity()
    if users[current_user]["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return jsonify({"message": "Admin Access: Granted"})


# Error handlers
@jwt.unauthorized_loader
def unauthorized_response(callback):
    return jsonify({"error": "Missing Authorization Header"}), 401


@jwt.invalid_token_loader
def invalid_token_callback(error):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    return jsonify({"error": "Token has expired"}), 401


if __name__ == '__main__':
    app.run(debug=True)
