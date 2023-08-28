import requests
from flight_data import FlightData


class FlightSearch:
    def __init__(self, endpoint, auth_key):
        self.endpoint = endpoint
        self.auth_key = auth_key

    def getIATA(self, city):
        headers = {"apikey": self.auth_key}
        query = {"term": city, "location_types": "city"}
        response = requests.get(url=f"{self.endpoint}locations/query", params=query, headers=headers)
        response.raise_for_status()
        return response.json()['locations'][0]['code']

    def checkFlights(self, origin_city_code, destination_city_code, from_time, to_time):
        headers = {"apikey": self.auth_key}
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }

        response = requests.get(url=f"{self.endpoint}v2/search", params=query, headers=headers)

        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: £{flight_data.price}")
        return flight_data
