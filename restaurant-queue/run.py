import sys
from flask import Flask, request, json
from ticketing import Ticketing
from sqlite3 import Error

app = Flask(__name__)
ticketing = Ticketing()

def get_response(data):
    response = {}
    if not data:
        response['status'] = False
        response['result'] = None
    else:
        response['status'] = True
        response['result'] = data

    return response


@app.route("/")
def welcome():
    return "<h1>Welcome Home!</h1>"

@app.route("/addTicketing", methods=['GET', 'POST'])
def add_ticketing():
    total_of_member = request.args.get("member")
    data = {}
    data['id'] = ticketing.add_ticketing(int(total_of_member))
    return get_response(data)

@app.route("/getAllTicketing")
def get_all_ticketing():
    page = request.args.get("page", default=1)
    order_by = request.args.get("order_by", default="ASC")
    data = ticketing.get_all_ticketing(int(page), order_by)
    return get_response(data)

@app.route("/getTicketingByMember")
def get_ticketing_by_member():
    member = request.args.get("member", default=1)
    ready = request.args.get("ready", default=0)
    data = ticketing.get_ticketing_by_member(int(member), int(ready))
    return get_response(data)

@app.route("/updateState")
def update_state():
    member = request.args.get("member")
    ticketing.update_state(member)
    return "Update Success"

@app.route("/queue")
def queue():
    member = request.args.get("member", default=1)
    ready = request.args.get("ready", default=1)
    data = ticketing.get_ticketing_by_state(member, ready)
    if len(data) > 0:
        return get_response(data[0])
    else: 
        return get_response(None)

if __name__ == '__main__':
    app.run(port=sys.argv[1])
