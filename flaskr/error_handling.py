from flask import jsonify


def handle_404(e):
    return jsonify(error=str(e)), 404


def handle_duplicate_key(e):
    return jsonify(error=f"Duplicate key error."), 400

