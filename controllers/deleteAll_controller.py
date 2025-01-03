from flask import jsonify
from store import todos


def deleteAll_route(app):
    @app.route('/delete-todo', methods=['DELETE'])
    def deleteAllTodo():
        # Empty todos check
        if len(todos) == 0:
            return jsonify({'msg':'Todo list is empty.', 'status':400}), 400
        # Delete all todos
        todos.clear()
        return jsonify({'msg':f"Your todos deleted successfully.", 'status':200}), 200
