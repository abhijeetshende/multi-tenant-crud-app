from flask import Blueprint, jsonify, request
from app.database import db
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
        db.session.commit()  # No need for current_app.app_context()
        return jsonify(new_item.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

### **2️⃣ Get All Items (GET)**
@api_blueprint.route('/items', methods=['GET'])
def get_items():
    items = Item.query.all()
    return jsonify([item.to_dict() for item in items])

### **3️⃣ Get a Single Item by ID (GET)**
@api_blueprint.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = Item.query.get(item_id)
    if not item:
        return jsonify({"error": "Item not found"}), 404
    return jsonify(item.to_dict())

### **4️⃣ Update an Item (PUT)**
@api_blueprint.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = Item.query.get(item_id)
    if not item:
        return jsonify({"error": "Item not found"}), 404

    data = request.json
    if 'name' in data:
        item.name = data['name']
    
    db.session.commit()
    return jsonify(item.to_dict())

### **5️⃣ Delete an Item (DELETE)**
@api_blueprint.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    item = Item.query.get(item_id)
    if not item:
        return jsonify({"error": "Item not found"}), 404

    db.session.delete(item)
    db.session.commit()
    return jsonify({"message": "Item deleted successfully"})
