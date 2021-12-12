from flask import Blueprint, jsonify
from database.ticketing import Ticketing

queue_bp = Blueprint('queue', __name__)

def queue_error(msg=None):
    return jsonify(
        {
            "status" : False,
            "result" : msg
        }
    )

@queue_bp.route('/<queue_code>')
def queue_checking(queue_code):
    ticketing = Ticketing()

    if not queue_code:
        return queue_error()
    else:
        return {
            "status" : True,
            "result" : ticketing.queue_data(queue_code)
        }

@queue_bp.route('/updateState/<int:member>')
def queue_update(member):
    ticketing = Ticketing()
    if member > 0 and member <= 10:
        return jsonify(
            {
                "status" : True,
                "result" : ticketing.queue_update(member)
            }
        )
    else:
        queue_error()
