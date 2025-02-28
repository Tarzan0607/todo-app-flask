import os
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Persistent storage file
DATA_DIR = "data"  # Change from /data to a local folder
DATA_FILE = os.path.join(DATA_DIR, "todos.json")

# Ensure the directory exists
os.makedirs(DATA_DIR, exist_ok=True)

# Ensure the file exists
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump([], f)


# Load todos
def load_todos():
    with open(DATA_FILE, "r") as f:
        return json.load(f)


# Save todos
def save_todos(todos):
    with open(DATA_FILE, "w") as f:
        json.dump(todos, f)


@app.route("/todos", methods=["GET"])
def get_todos():
    return jsonify(load_todos())


@app.route("/todos", methods=["POST"])
def add_todo():
    todos = load_todos()
    data = request.json
    todos.append(data)
    save_todos(todos)
    return jsonify({"message": "Todo added!"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
