from flask import Blueprint, jsonify, request
from app.database import db
from app.models import Todo
from flasgger import swag_from


todo_blueprint = Blueprint('todos', __name__)


@todo_blueprint.route('/todos', methods=['POST'])
@swag_from({
    "tags": ["Todos"],
    "parameters": [
        {
            "name": "body2",
            "in": "body",
            "schema": {
                "type": "object",
                "properties": {
                    "title": {"type": "string"},
                    "description": {"type": "string"},
                    "is_completed": {"type": "boolean"}
                },
                "required": ["title"]
            }
        }
    ],
    "responses": {
        201: {"description": "Todo created successfully"},
        400: {"description": "Invalid input"}
    }
})
def create_todo():
    data = request.json
    if 'title' not in data:
        return jsonify({"error": "Title is required"}), 400

    new_todo = Todo(
        title=data['title'],
        description=data.get('description'),
        is_completed=data.get('is_completed', False),
    )
    db.session.add(new_todo)

    try:
        db.session.commit()
        return jsonify(new_todo.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    
@todo_blueprint.route('/todos', methods=['GET'])
def get_todos():
    todos = Todo.query.all()
    return jsonify([todo.to_dict() for todo in todos])