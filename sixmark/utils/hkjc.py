import requests
import json

class HKJCRequest:
    def __init__(self):
        self.domain = "https://bet.hkjc.com/marksix/getJSON.aspx"
        self.start_date = ""
        self.end_date = ""

    def set_params(self, **kwargs):
        self.start_date = kwargs.get("sd", "")
        self.end_date = kwargs.get("ed", "")

    @property
    def get(self):
        """
            property getter: ready-only
            params: sd = 20220501, ed = 20220630, sb = 0
        """
        try:
            url = "{}?sd={}&ed={}&sb=0".format(self.domain, self.start_date,  self.end_date)
            response = requests.post(url, headers={'Content-Type': 'application/json'})
            if response.ok:
                return response
        except:
            print("Error: RemoteNumberDataSource.get()")
            return None