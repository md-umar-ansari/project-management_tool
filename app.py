from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
projects = []
tasks = []

@app.route('/projects', methods=['GET', 'POST'])
def manage_projects():
    if request.method == 'POST':
        project = request.json
        projects.append(project)
        return jsonify(project), 201
    return jsonify(projects)

@app.route('/tasks', methods=['GET', 'POST'])
def manage_tasks():
    if request.method == 'POST':
        task = request.json
        tasks.append(task)
        return jsonify(task), 201
    return jsonify(tasks)

if __name__ == '__main__':
    app.run(debug=True)