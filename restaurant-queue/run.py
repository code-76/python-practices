from flask import Flask, request
from ticketing import Ticketing

app = Flask(__name__)
ticketing = Ticketing()

@app.route("/")
def welcome():
    return "<h1>Welcome Home!</h1>"

@app.route("/getTicketing", methods=['GET', 'POST'])
def get_ticketing():
    total_of_member = request.args.get("total")
    ticketing_number = ticketing.get(int(total_of_member))
    return "Ticketing number : " + str(ticketing_number)

if __name__ == '__main__':
    app.run(port=8080)
