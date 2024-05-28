import datetime
import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = "aj8364524@gmail.com"
MY_PASS = "bhux ioiu gpaq xgvl"
RECEIVER_EMAIL = "anishajoshi5210@gmail.com"

MY_LAT = 20.593683
MY_LONG = 78.962883

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]['longitude'])
    iss_position = (iss_latitude, iss_longitude)
    print(iss_position)

    # Check if our position is within +5 or -5 degree of the iss position
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0  # for off (to convert 24hr to 12 hr format)
    }
    response = requests.get("https://api.sunrise-sunset.org/json", parameters)
    response.raise_for_status()
    data = response.json()
    print(data)
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"])
    print(sunrise)
    print(sunset)

    time_now = datetime.now().hour
    print(time_now)

    if time_now <= sunrise or time_now >= sunset:
        return True

# if iss overhead and nighttime send an email:-
while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASS)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=RECEIVER_EMAIL,
            msg="SUBJECT: Look Up\n\n The ISS is above you in sky."
        )
