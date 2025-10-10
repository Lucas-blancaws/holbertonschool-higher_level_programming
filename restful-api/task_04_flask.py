#!/usr/bin/python3

"""Flask application"""

from flask import Flask
from flask import jsonify
from flask import request


app = Flask(__name__)


@app.route("/")
def home():
    """Affiche un message"""
    return ("Welcome to the Flask API!")


users = {}


@app.route("/data")
def get_data():
    """Return une liste de tout les noms d'user"""
    return jsonify(users)


@app.route("/status")
def get_status():
    """Vérifie que l'API fonctionne"""
    return ("OK")


@app.route("/users/<username>")
def new_user(username):
    """Return les données de l'user demandé si présent,
        sinon return une erreur """
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """Reçoit des données JSON, ajoute un nouvel utilisateur
    dans un dico"""
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
    app.run
