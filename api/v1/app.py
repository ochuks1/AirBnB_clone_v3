#!/usr/bin/python3
@app.errorhandler(404)
def not_found(e):
    """Return a JSON formatted 404 error response."""
    return jsonify({"error": "Not found"}), 404
