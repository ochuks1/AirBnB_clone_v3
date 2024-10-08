from flask import jsonify, request
from models import storage, City, State

@app.route('/api/v1/states/<state_id>/cities', methods=['GET', 'POST'])
def handle_cities(state_id):
    """Retrieve or create City objects for a State."""
    state = storage.get(State, state_id)
    if state is None:
        return jsonify({"error": "Not found"}), 404

    if request.method == 'GET':
        cities = [city.to_dict() for city in state.cities]
        return jsonify(cities)

    if request.method == 'POST':
        if not request.get_json():
            return jsonify({"error": "Not a JSON"}), 400
        if 'name' not in request.get_json():
            return jsonify({"error": "Missing name"}), 400

        city_data = request.get_json()
        new_city = City(state_id=state_id, **city_data)
        new_city.save()
        return jsonify(new_city.to_dict()), 201

@app.route('/api/v1/cities/<city_id>', methods=['GET', 'DELETE', 'PUT'])
def handle_city(city_id):
    """Retrieve, delete, or update a City object."""
    city = storage.get(City, city_id)
    if city is None:
        return jsonify({"error": "Not found"}), 404

    if request.method == 'GET':
        return jsonify(city.to_dict())

    if request.method == 'DELETE':
        city.delete()
        return jsonify({}), 200

    if request.method == 'PUT':
        if not request.get_json():
            return jsonify({"error": "Not a JSON"}), 400

        for key, value in request.get_json().items():
            if key not in ['id', 'state_id', 'created_at', 'updated_at']:
                setattr(city, key, value)
        city.save()
        return jsonify(city.to_dict()), 200
