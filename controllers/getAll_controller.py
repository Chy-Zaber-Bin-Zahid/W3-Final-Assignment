from flask import jsonify
from store import todos


def getAll_route(app):
    @app.route('/get-todo', methods=['GET'])
    def getAllTodo():
        # Empty todos check
        if len(todos) == 0:
            return jsonify({'msg':'Todo list is empty.', 'status':400}), 400
        return jsonify({'msg':f"Your todos -> {todos}.", 'status':200}), 200
