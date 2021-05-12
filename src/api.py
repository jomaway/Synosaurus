import json
import requests




class API:


    def __init__(self):
        self.base_url = "https://www.openthesaurus.de/synonyme/​search"
        self.query_string = "test"
        self.options = {
            "similar": False,
            "substring": False,
            "startswith":True,
            "supersynsets":False,
            "supersynsets":False,
            "baseform":False
        }

    def build_url(self):
        url = f"{self.base_url}?q={self.query_string}"
        for key, value in options:
            if value:
                url += f"&{key}=true"
        return url

    def query(self, string):
        self.query_string = string
        response = requests.get(self.build_url())
        if response.status_code != 200:
            return "Error"
        else:
            return response.json()

    def set_option(key, value):
        if self.options[key] and type(value) == bool:
            self.options[key] = value
