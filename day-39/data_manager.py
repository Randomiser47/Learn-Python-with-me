import requests
from pprint import pprint
import os
from dotenv import load_dotenv
load_dotenv()
SHEETY_URL = os.getenv('SHEETY_URL')
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
USER_AUTH =(f'{username}',f'{password}')
class DataManager:
        def __init__(self):
        #This class is responsible for talking to the Google Sheet.
        #Sheety API keys and url

            self.header_json = {
                'Content-Type':'application/json'
            }
            self.data = {

            'price': {
                'city': 'Rawalpind',
                'iataCode': 'LHR',
                'lowestPrice': '22'
            }
            }
            
        def get_destination_data(self):
             response_getprice = requests.get(url=SHEETY_URL,headers=self.header_json,auth=USER_AUTH)
             self.destination_data = response_getprice.json()['prices']
             return self.destination_data
           
        def post(self):
            response_sheety = requests.get(url=SHEETY_URL,headers= self.header_json)
            print(response_sheety.status_code)
            pprint(response_sheety.json())

        def put(self):
            for i in self.destination_data:
                self.putdata = {
                    'price': {
                        'iataCode': i['iataCode']
                    }
                }
                response_put = requests.put(url=f"{SHEETY_URL}/{i['id']}", headers=self.header_json, json=self.putdata, auth=USER_AUTH)
                print(response_put.status_code)
                pprint(response_put.json())
                print(response_put.text)

