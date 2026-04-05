from flask import Blueprint, request, jsonify

tasks_bp = Blueprint('tasks', __name__)

tasks = [
    {"id": 1, "task": "Learn AWS"},
    {"id": 2, "task": "Build Cloud Project"}
]

@tasks_bp.route("/", methods=["GET"])
def get_tasks():
    return jsonify(tasks)

@tasks_bp.route("/", methods=["POST"])
def add_task():
    data = request.get_json()
    new_task = {
        "id": len(tasks) + 1,
        "task": data.get("task")
    }
    tasks.append(new_task)
    return jsonify(new_task), 201
