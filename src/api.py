import json
import requests




class OpenthesaurusAPI:


    def __init__(self):
        self.base_url = "https://www.openthesaurus.de/synonyme/search"
        self.format = "application/json"
        self.query_string = "test"
        self.last_result = None
        self.options = {
            "similar": False,
            "substring": False,
            "startswith":False,
            "supersynsets":False,
            "subsynsets":False,
            "baseform":False
        }

    def build_url(self):
        url = f"{self.base_url}?q={self.query_string}&format={self.format}"
        for key, value in self.options.items():
            if value:
                url += f"&{key}=true"
        return url

    def query(self, string):
        self.query_string = string
        print(f"URL: {self.build_url()}")
        response = requests.get(self.build_url())
        if response.status_code != 200:
            return "Error"
        else:
            self.last_response = response
            return response.json()

    def set_option(key, value):
        if self.options[key] and type(value) == bool:
            self.options[key] = value

    
