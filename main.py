# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import os
from dotenv import load_dotenv
from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from notification_manager import NotificationManager

load_dotenv()

SHEETY_AUTH_KEY = os.getenv("SHEETY_AUTH_KEY")
SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT")
TEQUILA_API_KEY = os.getenv("TEQUILA_API_KEY")
TEQUILA_ENDPOINT = os.getenv("TEQUILA_ENDPOINT")
TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH = os.getenv("TWILIO_AUTH")
SENDER = os.getenv("SENDER")
RECEIVER = os.getenv("RECEIVER")

sheet_data = DataManager(SHEETY_ENDPOINT, SHEETY_AUTH_KEY)
flight_data = FlightSearch(TEQUILA_ENDPOINT, TEQUILA_API_KEY)
notif_manager = NotificationManager(TWILIO_SID, TWILIO_AUTH)

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
    body = f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}"
    notif_manager.sendNotification(body, SENDER, RECEIVER)