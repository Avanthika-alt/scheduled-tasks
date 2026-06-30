import requests
import os
from twilio.rest import Client

weather_link = "https://api.openweathermap.org/data/2.5/forecast"
api_key = OWM_API_KEY
LAT = 22.207001
LNG = 84.850998

account_sid = ACCOUNT_SID
auth_token = AUTH_TOKEN
weather_params = {
    "lat": LAT,
    "lon": LNG,
    "appid": api_key,
    "cnt":4

}

response = requests.get(weather_link,params =weather_params )
response.raise_for_status()

weather_data = response.json()


will_rain = False
for n in weather_data["list"]:
    condition_code = n["weather"][0]["id"]
    if int(condition_code) <700:
        will_rain = True
if will_rain:

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="It's going to rain! Bring an Umbrella☔",
        from_="+19133640125",
        to="+919633167444",
    )

print(message.status)


