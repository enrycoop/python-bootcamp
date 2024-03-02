"""
Codici di risposta

1xx: attendi
2xx: Risultato corretto
3xx: richiesta errata
4xx: client error
5xx: server error
"""
import smtplib
import time

import requests
from datetime import datetime

MY_LAT = 41.201260
MY_LONG = 16.598539

my_email = "johnpython1987@gmail.com"
password = "mdwoudhzrgooyygh"


def in_range():
    """Controlla se la tua posizione è tra -5 e +5 gradi rispetto alla posizione della ISS"""
    resp = requests.get(url='http://api.open-notify.org/iss-now.json')
    # consente di non scrivere tutte le possibili combinazioni di eccezioni
    resp.raise_for_status()

    data_response = resp.json()

    longitute = float(data_response['iss_position']['longitude'])
    latitude = float(data_response['iss_position']['latitude'])

    iss_position = (longitute, latitude)
    print(f"iss position: {iss_position}, my coordinates: ({MY_LONG}, {MY_LAT})")
    return MY_LAT - 5 <= latitude <= MY_LAT + 5 and MY_LONG - 5 <= longitute <= MY_LONG + 5


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()

    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    print(sunrise)
    print(sunset)

    time_now = datetime.now().hour
    print(f"time check: {sunrise} < {time_now} < {sunset}")
    return not sunrise < time_now < sunset


while True:

    message = ""
    if in_range():
        message = "La ISS sta passando sopra di te!"

        if not is_night():
            message += " Ti sarà difficile vederla adesso :("

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="enrycoop92@gmail.com",
                msg=f"Subject:Alza la testa!\n\n{message}")
        print("SEND MESSAGE!!!! THE ISS IS PASSING FROM HERE!!!!!")
    time.sleep(60)