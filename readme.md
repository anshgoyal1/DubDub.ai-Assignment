# To-Do List Application

A simple backend application for implementing a to-do list.

## Requirements

Python 3.10.6

### Setup

1. Clone the repository

```
git clone https://github.com/your-username/todo-list-app.git

```

2. Install the dependencies

```
pip install -r requirements.txt
```

3. Run the application

```
python app.py
```

The application will now be running at http://localhost:5000. You can access the endpoints defined in the application to interact with the to-do list.

Endpoints

- GET /todos: Retrieve a list of all to-do items
- GET /todos/<id>: Retrieve a specific to-do item by ID
- POST /todos: Create a new to-do item
- PUT /todos/<id>: Update an existing to-do item
- DELETE /todos/<id>: Delete a to-do item
