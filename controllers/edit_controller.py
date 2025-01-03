from flask import request, jsonify
from store import todos


def edit_route(app):
    @app.route('/edit-todo/<string:todoId>', methods=['PUT'])
    def editTodo(todoId):
        data = request.json
        # Valid field check
        allowed_fields = ['todo']
        for field in data:
            if field not in allowed_fields:
                return jsonify({'msg':f"Invalid field -> {field}.", 'status':400}), 400
        # Empty todos check
        if len(todos) == 0:
            return jsonify({'msg':'Todo list is empty.', 'status':400}), 400
        # Valid id check
        for i in range(len(todos)):
            if todoId == todos[i]['id']:
                todos[i]['todo'] = data['todo']
                return jsonify({'msg':f'Your todo updated successfully.', 'status':200}), 200
        return jsonify({'msg':f"Invalid Id -> {todoId}.", 'status':400}), 400
