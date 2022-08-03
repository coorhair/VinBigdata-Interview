import math
from ..db import get_db
from ..model import Call
from ..objectid import PydanticObjectId


def save_call_log(**kwargs):
    db = get_db()
    call = Call(**kwargs)
    insert_result = db.mobile_calls.insert_one(call.to_bson())
    call.id = PydanticObjectId(str(insert_result.inserted_id))
    return call.to_json()


def calc_call_billing(username):
    db = get_db()
    total_call = db.mobile_calls.count_documents({'username': username})
    total_block = 0
    if total_call:
        records = db.mobile_calls.aggregate([
            {
                '$match': {"username": username}
            },
            {
                '$project': {"call_duration": 1}
            },
            {
                '$group': {
                    "_id": None,
                    "total": {
                        '$sum': "$call_duration"
                    }
                }
            }
        ])
        records = list(records)
        if records:
            total_ms = records[0]['total']
            if total_ms:
                total_block = math.ceil(total_ms/30000)
    return total_call, total_block
