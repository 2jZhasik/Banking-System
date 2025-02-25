import sqlite3
from flask import Flask, request, jsonify
from database import init_db, register_client, get_balance, deposit_money, withdraw_money

app = Flask(__name__)
init_db()

@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    name = data.get("name")
    message = register_client(name)
    return jsonify({"message": message})

@app.route("/balance", methods=["GET"])
def balance():
    client_id = request.args.get("client_id")
    balance = get_balance(client_id)
    if balance is not None:
        return jsonify({"balance": balance})
    return jsonify({"message": "Client not found"})

@app.route("/deposit", methods=["POST"])
def deposit():
    data = request.get_json()
    client_id = data.get("client_id")
    amount = data.get("amount")
    message = deposit_money(client_id, amount)
    return jsonify({"message": message})

@app.route("/withdraw", methods=["POST"])
def withdraw():
    data = request.get_json()
    client_id = data.get("client_id")
    amount = data.get("amount")
    message = withdraw_money(client_id, amount)
    return jsonify({"message": message})

if __name__ == "__main__":
    app.run(debug=True)
