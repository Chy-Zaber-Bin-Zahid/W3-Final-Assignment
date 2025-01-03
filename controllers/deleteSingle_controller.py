from flask import jsonify
from store import todos


def deleteSingle_route(app):
    @app.route('/delete-todo/<string:todoId>', methods=['DELETE'])
    def deleteSingleTodo(todoId):
        # Empty todos check
        if len(todos) == 0:
            return jsonify({'msg':'Todo list is empty.', 'status':400}), 400
        # Valid id check
        for i in range(len(todos)):
            if todoId == todos[i]['id']:
                deletedTodo = todos.pop(i)
                return jsonify({'msg':f'Your todo deleted successfully -> {deletedTodo}', 'status':200}), 200
        return jsonify({'msg':f"Invalid Id -> {todoId}.", 'status':400}), 400
