from flask import jsonify
from models import storage

@app.route('/api/v1/stats', methods=['GET'])
def stats():
    """Retrieve the number of each object by type."""
    stats = {
        "amenities": storage.count("Amenity"),
        "cities": storage.count("City"),
        "places": storage.count("Place"),
        "reviews": storage.count("Review"),
        "states": storage.count("State"),
        "users": storage.count("User"),
    }
    return jsonify(stats)
