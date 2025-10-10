#!/usr/bin/python3

"""Flask application"""

from flask import Flask
from flask import jsonify
from flask import request


app = Flask(__name__)


@app.route("/")
def home():
    return ("Welcome to the Flask API!")


users = {"jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}}


@app.route("/data")
def get_data():
    return jsonify(users)


@app.route("/status")
def get_status():
    return ("OK")


@app.route("/users/<username>")
def get_user(username):
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def get_adduser():
    data = request.get_json()
    if not data or "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data["username"]
    if username in users:
        return jsonify({"message": "User added", "user": data}), 201

    users[username] = data
    return jsonify({"message": "User added", "user": data}), 201


if __name__ == "__main__":
    app.run(debug=True, port=5000)
