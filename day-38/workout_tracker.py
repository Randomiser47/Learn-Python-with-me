import requests
import os 
from datetime import datetime

x_app_id = os.environ.get("x_app_id")
x_app_key = os.environ.get("x_app_key")
nuti_url = os.environ.get("nuti_url")
header = {
'x-app-id':x_app_id,
'x-app-key':x_app_key,
}
query = {
    'gender':'male',
    'weight_kg': 85,
    'height_cm':180.33,
    'age':25,
    'query':input("How much exercise did you do today?")
}
response = requests.post(url=nuti_url, json=query, headers=header,)
nutri_data = response.json()
print(nutri_data)

Sheety_url = os.environ.get("Sheety_url")
response_sheety = requests.get(url=Sheety_url)


today = datetime.now()
date = today.strftime("%Y/%m/%d")
time = today.strftime("%H:%M:%S")
for exercise in nutri_data['exercises']:
    data = {
        "sheet1": {
            "date": date,
            "time": time,
            "exercise":  exercise['name'],
            "duration":  exercise['duration_min'],
            "calories":  exercise['nf_calories'],
        }
    }
    header_json = {
        'Content-Type': 'application/json'
    }

    response_sheety = requests.post(url=Sheety_url, headers=header_json, json=data, auth=('iron_man','ironman422'))
    print(response_sheety.status_code)
    print(response_sheety.text)
