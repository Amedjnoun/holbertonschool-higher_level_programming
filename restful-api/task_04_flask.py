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
    return "OK", 200


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
        users[username] = data
        return jsonify({"message": "User added", "user": data}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run()
