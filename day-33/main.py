import requests
import datetime as dt

MY_LAT = 33.565109
MY_LONG = 73.016914
LOCAL_UTC_OFFSET = 5

# request = requests.get(url='http://api.open-notify.org/iss-now.json')

# longitude = request.json()['iss_position']['longitude']
# latitude = request.json()['iss_position']['latitude']

# iss_position = f"{latitude},{longitude}"

# print(iss_position)


# with open('iss_position.txt',mode='w') as file:
#     file.write(iss_position)


# UTC PROBLEM
def utc_to_local(utc_hour):
    utc_hour += LOCAL_UTC_OFFSET
    if LOCAL_UTC_OFFSET > 0:
        if utc_hour > 23:
            utc_hour -= 24
    elif LOCAL_UTC_OFFSET < 0:
        if utc_hour < 0:
            utc_hour += 24
    return utc_hour

parameters = {
    "lat":MY_LAT,
    "lng":MY_LONG,

    "formatted":0

}





response = requests.get(url='https://api.sunrise-sunset.org/json',params=parameters, )
response.raise_for_status()
data  = response.json()
sunrise = int(data['results']['sunrise'].split("T")[1].split(":")[0])
sunset = int(data['results']['sunset'].split("T")[1].split(":")[0])

local_sunrise = utc_to_local(sunrise)
local_sunset = utc_to_local(sunset)

print(local_sunrise,local_sunset)

time_now = dt.datetime.now()

print(time_now.hour)