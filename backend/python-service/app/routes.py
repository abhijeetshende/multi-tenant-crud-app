from flask import Blueprint, jsonify

api_blueprint = Blueprint('api', __name__)

@api_blueprint.route('/test', methods=['GET'])
def test_route():
    return jsonify({"message": "Routes are working!"})
