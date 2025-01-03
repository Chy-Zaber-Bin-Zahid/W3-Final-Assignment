from flask import request, jsonify
import uuid
from store import todos


def add_route(app):
    @app.route('/add-todo', methods=['POST'])
    def addTodo():
        data = request.json
        # Valid field check
        allowed_fields = ['todo']
        for field in data:
            if field not in allowed_fields:
                return jsonify({'msg':f"Invalid field -> {field}.", 'status':400}), 400
        # Remove extra white space
        todo = data['todo'].strip().replace(" ","")
        # Empty todo check
        if len(todo) == 0:
            return jsonify({'msg':'Todo can not be empty.', 'status':400}), 400
        todoId = uuid.uuid4().hex
        data['id'] = todoId
        todos.append(data)
        print(todos)
        return jsonify({'msg':f'New todo added successfully -> {todoId}', 'status':200}), 200
            