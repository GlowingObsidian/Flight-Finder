import requests

class FlightSearch:
    def __init__(self,endpoint, auth_key):
        self.endpoint = f"{endpoint}locations/query"
        self.auth_key = auth_key

    def getIATA(self,city):
        headers={"apikey": self.auth_key}
        query = {"term": city, "location_types": "city"}
        response = requests.get(url=self.endpoint, params=query, headers=headers)
        response.raise_for_status()
        return response.json()['locations'][0]['code']