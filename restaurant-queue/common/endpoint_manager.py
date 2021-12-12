from flask import Flask
from common.endpoint_action import EndpointAction

class EndpointManager(object):

    def __init__(self, name=__name__) -> None:
        super().__init__()
        self.__app = Flask(name)

    def run(self, host, port, debug=False):
        self.__app.run(host=host, port=port, debug=debug)
    
    def add_endpoint(self, endpoint=None, endpoint_name=None, handler=None, methods=None):
        self.__app.add_url_rule(endpoint, endpoint_name, EndpointAction(handler), methods)