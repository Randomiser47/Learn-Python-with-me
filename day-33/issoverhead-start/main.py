import requests
from datetime import datetime
import smtplib 
import time

MY_LAT = "ENTER YOUR OWN " # Your latitude
MY_LONG = "ENTER YOUR OWN " # Your longitude
my_email = 'ENTER YOUR OWN EMAIL'
password = 'ENTER YOUR OWN APP PASSWORD '

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
while True:
    time.sleep(60)
    #If the ISS is close to my current position
    if abs(MY_LAT - iss_latitude) <= 5 and abs(MY_LONG - iss_longitude)<=5 and time_now.hour >= sunset or time_now.hour <= sunrise:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email,password=password)
            connection.sendmail(from_addr=my_email,to_addrs=my_email,
                                msg= f"Subject: Tuesday Motivation Email \n\n LOOK UP THE ISS IS ABOVE YOU")
        





# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



