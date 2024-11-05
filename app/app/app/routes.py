from flask import jsonify, request, Blueprint
from . import db
from .models import User, InventoryItem
from .demand_prediction import predict_demand

main = Blueprint('main', __name__)

@main.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user = User(username=data['username'], user_type=data['user_type'], location=data['location'])
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201

@main.route('/inventory', methods=['POST'])
def add_inventory():
    data = request.get_json()
    user_id = data['user_id']
    item = InventoryItem(name=data['name'], quantity=data['quantity'], user_id=user_id)
    db.session.add(item)
    db.session.commit()
    return jsonify({'message': 'Inventory item added successfully'}), 201

@main.route('/predict_demand', methods=['GET'])
def get_demand_prediction():
    # Dummy historical data, would be fetched from database
    history = [100, 120, 130, 115, 140]
    predicted_demand = predict_demand(history)
    return jsonify({'predicted_demand': predicted_demand}), 200
