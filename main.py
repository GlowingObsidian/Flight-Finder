# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import os
from dotenv import load_dotenv
from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta

load_dotenv()

SHEETY_AUTH_KEY = os.getenv("SHEETY_AUTH_KEY")
SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT")
TEQUILA_API_KEY = os.getenv("TEQUILA_API_KEY")
TEQUILA_ENDPOINT = os.getenv("TEQUILA_ENDPOINT")

sheet_data = DataManager(SHEETY_ENDPOINT, SHEETY_AUTH_KEY)
# sheet_data = {'prices': [{'city': 'Paris', 'iataCode': '', 'lowestPrice': 54, 'id': 2}, {'city': 'Berlin', 'iataCode': '', 'lowestPrice': 42, 'id': 3}, {'city': 'Tokyo', 'iataCode': '', 'lowestPrice': 485, 'id': 4}, {'city': 'Sydney', 'iataCode': '', 'lowestPrice': 551, 'id': 5}, {'city': 'Istanbul', 'iataCode': '', 'lowestPrice': 95, 'id': 6}, {'city': 'Kuala Lumpur', 'iataCode': '', 'lowestPrice': 414, 'id': 7}, {'city': 'New York', 'iataCode': '', 'lowestPrice': 240, 'id': 8}, {'city': 'San Francisco', 'iataCode': '', 'lowestPrice': 260, 'id': 9}, {'city': 'Cape Town', 'iataCode': '', 'lowestPrice': 378, 'id': 10}]}

flight_data = FlightSearch(TEQUILA_ENDPOINT, TEQUILA_API_KEY)

for city in sheet_data.read()['prices']:
    if city['iataCode'] == '':
        data = {
            "price": {
                "iataCode": flight_data.getIATA(city['city'])
            }
        }
        sheet_data.edit(city['id'], data)
        print("updated IATA", city['city'])

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for city in sheet_data.read()['prices']:
    flight = flight_data.checkFlights(
        "LON",
        city['iataCode'],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
