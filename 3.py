from flask import Flask, request, redirect

app = Flask(__name__)

# Intentionally using a simple list to store tasks
tasks = []

@app.route('/')
def index():
    # Directly return HTML
    html = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>To-Do List</title>
    </head>
    <body>
        <h1>To-Do List</h1>
        <form action="/add" method="POST">
            <input type="text" name="task" placeholder="Add a task">
            <button type="submit">Add</button>
        </form>
        
        <ul>
            {% for task in tasks %}
                <li>{ task }
                    <form action="/delete/{{ loop.index0 }}" method="POST" style="display:inline;">
                        <button type="submit">Delete</button>
                    </form>
                </li>
            {% else %}
                <li>No tasks yet!</li>
            {% endfor %}
        </ul>
    </body>
    </html>
    '''

    # Render the HTML with the tasks
    return html.replace('{{ tasks }}', str(tasks))

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form['task']
    # Check if the task is empty before adding
    if task.strip():  # Ensure that the task is not just spaces
        tasks.append(task)
    return redirect('/')

@app.route('/delete/<int:task_index>', methods=['POST'])
def delete_task(task_index):
    try:
        # Safely remove task by index
        tasks.pop(task_index)
    except IndexError:
        print("Task not found")
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=False)
