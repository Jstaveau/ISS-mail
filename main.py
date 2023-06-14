"""import requests
import datetime as dt
MY_LAT = 51.507351
MY_LONG = -0.127758

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (longitude, latitude)
print(iss_position)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

sunrise_time = sunrise.split("T")[1].split(':')[0]
time_now = dt.datetime.now()

print(sunrise_time)

"""
import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude


#Your position is within +5 or -5 degrees of the ISS position.

time_now = datetime.now()
current_hour = time_now.hour

#If the ISS is close to my current position


def iss_is_close():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if iss_latitude - 5 <= MY_LAT <= iss_latitude + 5 and iss_longitude - 5 <= MY_LONG <= iss_longitude + 5:
        return True
# and it is currently dark


def is_dark():
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
    if current_hour >= sunset or current_hour <= sunrise:
        return True
# Then send me an email to tell me to look up.


def send_mail():
    if iss_is_close() and is_dark():
        with smtplib.SMTP("smtp-mail.outlook.com", port=587) as connection:
            connection.starttls()
            connection.login(user="jonathan.staveau@outlook.com", password="Dicapepasmechant7!")
            connection.sendmail(from_addr="jonathan.staveau@outlook.com",
                                to_addrs="jonathan.staveau@outlook.com",
                                msg="Subject:ISS is in the sky\n\nLook up!")
    print("ok")

# BONUS: run the code every 60 seconds.
while True:
    send_mail()
    time.sleep(60)


