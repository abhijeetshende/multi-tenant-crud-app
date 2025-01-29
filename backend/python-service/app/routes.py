from flask import Blueprint, jsonify, request
from app.database import db  # ✅ Use the correct db instance
from app.models import Item

api_blueprint = Blueprint('api', __name__)

### **1️⃣ Create a New Item (POST)**
@api_blueprint.route('/items', methods=['POST'])
def create_item():
    data = request.json
    if 'name' not in data:
        return jsonify({"error": "Name is required"}), 400

    new_item = Item(name=data['name'])
    db.session.add(new_item)
    
    try:
        db.session.commit()  # ✅ Make sure db is initialized before calling commit
        return jsonify(new_item.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
