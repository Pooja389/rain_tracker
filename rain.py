from twilio.rest import Client
auth_token = "your_token"
acc_sid = "your_sid"


import requests
my_loc_lat = "your_latitude"
my_loc_lon = "your_longitude"
api_key = "your_api_key"
url_ = f"https://api.openweathermap.org/data/2.5/forecast?lat={my_loc_lat}&lon={my_loc_lon}&appid={api_key}"

response = requests.get(url=url_)
response.raise_for_status()
data = response.json()

will_rain = False
for i in range(3):
    day_weather = data["list"][i]["weather"][0]["main"]
    if day_weather == "Rain":
        will_rain = True
        break

if will_rain:
    client = Client(acc_sid,auth_token)
    message = client.messages.create(body = "Rain Rain\nIt will be raining today take umbrella",
                                 from_ = "whatsapp:+14155238886",to="whatsapp:+your_verified_number")    



 


