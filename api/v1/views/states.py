from flask import Flask, jsonify, request
from models import storage, State

@app.route('/api/v1/states', methods=['GET', 'POST'])
def handle_states():
    """Retrieve or create State objects."""
    if request.method == 'GET':
        states = [state.to_dict() for state in storage.all(State).values()]
        return jsonify(states)

    if request.method == 'POST':
        if not request.get_json():
            return jsonify({"error": "Not a JSON"}), 400
        if 'name' not in request.get_json():
            return jsonify({"error": "Missing name"}), 400
        
        state_data = request.get_json()
        new_state = State(**state_data)
        new_state.save()
        return jsonify(new_state.to_dict()), 201

@app.route('/api/v1/states/<state_id>', methods=['GET', 'DELETE', 'PUT'])
def handle_state(state_id):
    """Retrieve, delete, or update a State object."""
    state = storage.get(State, state_id)
    if state is None:
        return jsonify({"error": "Not found"}), 404

    if request.method == 'GET':
        return jsonify(state.to_dict())

    if request.method == 'DELETE':
        state.delete()
        return jsonify({}), 200

    if request.method == 'PUT':
        if not request.get_json():
            return jsonify({"error": "Not a JSON"}), 400
        
        for key, value in request.get_json().items():
            if key not in ['id', 'created_at', 'updated_at']:
                setattr(state, key, value)
        state.save()
        return jsonify(state.to_dict()), 200
