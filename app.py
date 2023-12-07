from flask import Flask, render_template, request, jsonify, redirect, url_for

app = Flask(__name__)

tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    task_content = request.form.get('task_content')
    task_deadline = request.form.get('task_deadline')
    task_priority = request.form.get('task_priority')
    tasks.append({'content': task_content, 'deadline': task_deadline, 'priority': task_priority})
    return redirect(url_for('index'))  # Use url_for to generate the URL for the 'index' route

@app.route('/delete_task/<int:task_index>')
def delete_task(task_index):
    if 0 <= task_index < len(tasks):
        del tasks[task_index]
        return jsonify({'status': 'success'})
    return jsonify({'status': 'error'})

if __name__ == '__main__':
    app.run(debug=True)
