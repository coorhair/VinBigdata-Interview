from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow


ma = Marshmallow()


class CallLog(ma.Schema):
    username = fields.String(required=True, validate=validate.Length(max=32, min=1))
    call_duration = fields.Integer(required=True, validate=validate.Range(min=1))


class CallBilling(ma.Schema):
    username = fields.String(required=True, validate=validate.Length(max=32, min=1))


call_log_schema = CallLog()
call_billing_schema = CallBilling()
