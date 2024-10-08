#!/usr/bin/python3
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/v1/status', methods=['GET'])
def status():
    """Returns the status of the API."""
    return jsonify(status='OK')

@app.route('/api/v1/notexist', methods=['GET'])
def not_exist():
    """Handles requests to a non-existent endpoint."""
    return jsonify(error='Not found'), 404

@app.errorhandler(404)
def not_found(error):
    """Handles 404 errors."""
    return jsonify(error='Not found'), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
