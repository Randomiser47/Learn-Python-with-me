import requests
import os
from dotenv import load_dotenv
load_dotenv()

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    #AMADEUS KEYS
    def __init__(self):
        
        self._api_key = os.getenv("API_AMADEUS_KEY")
        self._api_secret = os.getenv("API_AMADEUS_SECRET")
        self.url_amadeus = os.getenv("AMADEUS_URL_TOKEN")

    def _get_new_token(self):
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = {
            "grant_type": "client_credentials",
            "client_id": self._api_key,
            "client_secret": self._api_secret, }
        response = requests.post(self.url_amadeus, headers=headers, data=data)
        self.token = response.json()['access_token']
        return self.token

    def get_destination_code(self):
        url = os.getenv("AMADEUS_URL_GET")
        token = self._get_new_token()
        print(f"Token: {token}")
        
        headers = {
            "Authorization": f"Bearer {token}"
        }
        parameters = {
    "keyword": "PARIS",
    "include": "AIRPORTS",
    "max": "2"
}


        response = requests.get(url=url, headers=headers, params=parameters)
        print(response.status_code)
        print(response.json())

flight_search = FlightSearch()
flight_search.get_destination_code()