
from ast import JoinedStr
import requests
import json
from data.datasources import NumberDataSourcesImpl
from utils.hkjc import HKJCRequest

class RemoteNumberDataSource(NumberDataSourcesImpl):
    def __init__(self):
        NumberDataSourcesImpl.__init__(self)
        self.hk_request = HKJCRequest()

    def load(self, sd="", ed=""):
        self.hk_request.set_params(sd=sd, ed=ed)
        response = self.hk_request.get
        if response.status_code == 200:
            response_json = json.loads(response.text)
            for data in response_json:
                self.add(data["no"].split("+"))