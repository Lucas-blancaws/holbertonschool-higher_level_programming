#!/usr/bin/python3

"""Flask application"""

from flask import Flask
from flask import jsonify
from flask import request


app = Flask(__name__)


@app.route("/")
def home():
    return ("Welcome to the Flask API!")

users = {}

@app.route("/data")
def get_data():
    username = list(users.keys())
    return jsonify(users)


@app.route("/status")
def get_status():
    return ("OK")


@app.route("/users/<username>")
def new_user(username):
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json()
    if "username" not in data:
        return jsonify({"error": "Username is required"}), 400
    
    username = data["username"]
    users[username] = {
        "username": username,
        "name": data["name"],
        "age": data["age"],
        "city": data["city"]
    }
    return jsonify({"message": "User added", "user": users[username]}), 201


if __name__ == "__main__":
    app.run(debug=True, port=5000)
