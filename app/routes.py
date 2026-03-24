from flask import render_template
from flask import Blueprint, request, jsonify

task_routes = Blueprint(
    'task_routes',
    __name__,
    template_folder='templates'
)

tasks = []
task_id_counter = 1

@task_routes.route('/tasks', methods=['POST'])
def create_task():
    global task_id_counter
    data = request.json

    task = {
        "id": task_id_counter,
        "title": data.get("title"),
        "status": "To Do"
    }

    tasks.append(task)
    task_id_counter += 1

    return jsonify(task), 201


@task_routes.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks), 200


@task_routes.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.json

    for task in tasks:
        if task["id"] == task_id:
            task["status"] = data.get("status", task["status"])
            return jsonify(task), 200

    return jsonify({"error": "Task not found"}), 404


@task_routes.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]

    return jsonify({"message": "Task deleted"}), 200

@task_routes.route('/')
def home():
    return render_template('index.html')