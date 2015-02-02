import requests

class GenericApiCaller():
    
    @staticmethod
    def getJsonData(url, payload):
        r = requests.get(url, params=payload)
        return r.json();
