from flask import Flask, request, jsonify
import csv
import uuid

app = Flask(__name__)

csv_file = 'todos.csv'

todos = []
def write_to_csv(todo):
    with open(csv_file, 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['id', 'title', 'is_completed'])
        writer.writerow(todo)

def add_todo(TODO):
    title = TODO['title']
    id = str(uuid.uuid4())
    todo = {
        'id': id,
        'title': title,
        'is_completed': False
    }
    # print(todo['id'])
    write_to_csv(todo)
    print(f"Added to-do item: {todo}")


def read_from_csv():
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        todos = [{header[i]: row[i] for i in range(len(header))} for row in reader]
    return todos

@app.route('/todos', methods=['GET', 'POST'])
def todo_list():
    if request.method == 'GET':
        todos = read_from_csv()
        return jsonify(todos)
    if request.method == 'POST':
        todo = request.get_json()
        add_todo(todo)
        return jsonify(todo), 201

@app.route('/todos/<string:id>', methods=['GET', 'PUT', 'DELETE'])

def todo_detail(id):
    todos = read_from_csv()
    todo = next((t for t in todos if t['id'] == str(id)), None)
    if todo is None:
        return jsonify({'error': 'Not found'}), 404
    if request.method == 'GET':
        return jsonify(todo)
    if request.method == 'PUT':
        data = request.get_json()
        todo.update(data)
        with open(csv_file, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'title', 'is_completed'])
            writer.writeheader()
            writer.writerows(todos)
        return jsonify(todo)
    if request.method == 'DELETE':
        todos.remove(todo)
        with open(csv_file, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'title', 'is_completed'])
            writer.writeheader()
            writer.writerows(todos)
        return '', 204



if __name__ == '__main__':
    app.run()