from flask import Flask, config
import config
from api.ticketing import ticketing_bp
from api.queue import queue_bp
from common.db import Database

app = Flask(__name__)
app.register_blueprint(ticketing_bp, url_prefix='/ticketing')
app.register_blueprint(queue_bp, url_prefix='/queue')

@app.route("/")
def welcome():
    return "<b>Hello Welcome!</n>"

@app.route("/ticketing")
def ticketing():
    return "<b>Welcome to Ticketing System.</b>"

@app.route("/ordering")
def ordering():
    return "<b>Welcome to Ordering System.</b>"

@app.route('/setup')
def setup():
    database = Database()
    database.init()
    return "Connection established!"

if __name__ == '__main__':
    app.run(host=config.HOST, port=config.PORT, debug=config.DEBUG)
