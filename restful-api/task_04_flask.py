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


@app.route('/')
def home():
    return "Welcome to the Flask API!"


@app.route('/data')
def get_data():
    return jsonify(list(users.keys()))


@app.route('/status')
def status():
    return "OK"


@app.route('/users/<username>')
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 400


@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    username = data.get('username')
    if not username:
        return jsonify({"error": "Username is required"}), 400
    users[username] = data
    return jsonify({"message": "User added", "user": data}), 201


users = {
    "jane": {
        "username": "jane",
        "name": "Jane",
        "age": 28,
        "city": "Los Angeles"
    },
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}


if __name__ == "__main__":
    app.run()
