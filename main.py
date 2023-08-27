# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import os
from dotenv import load_dotenv
from data_manager import DataManager
from flight_search import FlightSearch

load_dotenv()

SHEETY_AUTH_KEY = os.getenv("SHEETY_AUTH_KEY")
SHEETY_ENDPOINT = os.getenv("SHEETY_END_POINT")

sheet_data = DataManager(SHEETY_ENDPOINT, SHEETY_AUTH_KEY)
# sheet_data = {'prices': [{'city': 'Paris', 'iataCode': '', 'lowestPrice': 54, 'id': 2}, {'city': 'Berlin', 'iataCode': '', 'lowestPrice': 42, 'id': 3}, {'city': 'Tokyo', 'iataCode': '', 'lowestPrice': 485, 'id': 4}, {'city': 'Sydney', 'iataCode': '', 'lowestPrice': 551, 'id': 5}, {'city': 'Istanbul', 'iataCode': '', 'lowestPrice': 95, 'id': 6}, {'city': 'Kuala Lumpur', 'iataCode': '', 'lowestPrice': 414, 'id': 7}, {'city': 'New York', 'iataCode': '', 'lowestPrice': 240, 'id': 8}, {'city': 'San Francisco', 'iataCode': '', 'lowestPrice': 260, 'id': 9}, {'city': 'Cape Town', 'iataCode': '', 'lowestPrice': 378, 'id': 10}]}

for city in sheet_data.read()['prices']:
    if city['iataCode'] == '':
        city = FlightSearch(city).getIATA()
        sheet_data.edit(city, city['id'])
        print("updated IATA", city['city'])
