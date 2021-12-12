from flask import Blueprint, jsonify
from database.ticketing import Ticketing
from common.db import Database

ticketing_bp = Blueprint('ticketing', __name__)

def ticketing_error(msg=None):
    return jsonify(
        {
            "status" : False,
            "result" : msg
        }
    )

@ticketing_bp.route('/member/<int:member>')
def acquire_ticketing(member):
    ticketing = Ticketing()
    if member > 0 and member <= 10:
        return jsonify(
            {
                "status" : True,
                "result" : ticketing.acquire_ticketing(member)
            }
        ) 
    else: 
        return ticketing_error()