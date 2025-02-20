#!/usr/bin/python3
"""
This module contains a simple Flask API with several endpoints to manage user
data.
Endpoints:
- /: Home route, returns a welcome message.
- /data: Returns a list of all usernames.
- /status: Returns a status message.
- /users/<username>: Returns data for a specific user.
- /add_user: Adds a new user to the users dictionary.
"""


from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

users = {}


@app.route('/')
def home():
    return "Welcome to the Flask API!"


@app.route('/status')
def status():
    return "OK"


@app.route('/data')
def get_data():
    if not users:
        return jsonify({"error": "No users found"}), 404
    return jsonify(list(users.keys()))


@app.route('/users/<username>')
def get_user(username):
    if not users:
        return jsonify({"error": "No users found"}), 404
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid JSON data"}), 400
        username = data.get('username')
        if not username:
            return jsonify({"error": "Username is required"}), 400
        if username in users:
            return jsonify({"error": "Username already exists"}), 400
        if 'age' not in data:
            return jsonify({"error": "Age is required"}), 400
        age = data.get('age')
        if age is not None:
            try:
                age = int(age)
            except (ValueError, TypeError):
                return jsonify({"error": "Age must be an integer"}), 400
        if 'name' not in data:
            return jsonify({"error": "Name is required"}), 400
        if 'city' not in data:
            return jsonify({"error": "City is required"}), 400
        users[username] = {
            "username": username,
            "name": data.get('name', ''),
            "age": data.get('age', 0),
            "city": data.get('city', '')
        }

        return jsonify({
            "message": "User added successfully",
            "user": users[username]
        }), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


users = {
    "jane": {
        "username": "jane",
        "name": "Jane",
        "age": 28,
        "city": "Los Angeles"
    },
    "john": {
        "username": "john",
        "name": "John",
        "age": 30,
        "city": "New York"
    }
}


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({"error": "Endpoint not found"}), 404


if __name__ == "__main__":
    app.run()
