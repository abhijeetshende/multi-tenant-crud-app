from flask import Blueprint, jsonify, request
from app.database import db
from app.models import Todo


todo_blueprint = Blueprint('todos', __name__)


@todo_blueprint.route('/todos', methods=['POST'])
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