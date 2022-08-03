from flask import Blueprint, jsonify, request
from .mobile_service import save_call_log, calc_call_billing
from ..validation import call_log_schema, call_billing_schema


mobile_api_v1 = Blueprint('mobile', __name__, url_prefix='/api/v1/mobile')


@mobile_api_v1.route('/<username>/call', methods=['PUT'])
def call_log(username):
    rparams = request.get_json()
    payload = dict(**rparams, username=username.strip() if username else username)
    validation_errors = call_log_schema.validate(payload)
    if validation_errors:
        return jsonify(validation_errors), 400
    try:
        record = save_call_log(**payload)
        return jsonify(record), 200
    except Exception as e:
        return jsonify({
            'error': str(e),
        }), 500


@mobile_api_v1.route('/<username>/billing', methods=['GET'])
def call_billing(username):
    validation_errors = call_billing_schema.validate({"username": username.strip() if username else username})
    if validation_errors:
        return jsonify(validation_errors), 400
    try:
        total_calls, total_blocks = calc_call_billing(username)
        return jsonify({'call_count': total_calls, 'block_count': total_blocks}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
