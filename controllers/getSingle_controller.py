from flask import jsonify
from store import todos


def getSingle_route(app):
    @app.route('/get-todo/<string:todoId>', methods=['GET'])
    def getSingleTodo(todoId):
        # Empty todos check
        if len(todos) == 0:
            return jsonify({'msg':'Todo list is empty.', 'status':400}), 400
        # Valid id check
        for i in range(len(todos)):
            if todoId == todos[i]['id']:
                return jsonify({'msg':f'Your todo -> {todos[i]['todo']}', 'status':200}), 200
        return jsonify({'msg':f"Invalid Id -> {todoId}.", 'status':400}), 400


        
            