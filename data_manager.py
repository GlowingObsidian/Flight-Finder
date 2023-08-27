import requests


class DataManager:
    def __init__(self, endpoint, auth_key):
        self.endpoint = endpoint
        self.header = {
            "Authorization": auth_key
        }

    def read(self):
        response = requests.get(url=self.endpoint, headers=self.header)
        response.raise_for_status()
        return response.json()

    def edit(self,row, row_number):
        json = {
            "price": {
                "iataCode": row['iataCode'],
            }
        }
        response = requests.put(url=f"{self.endpoint}/{row_number}", json=json, headers=self.header)
        response.raise_for_status()
