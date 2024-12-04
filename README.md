# rain_tracker
A code that will give message on your phone if it today will be rain with a msg to take an umbrella
# Rain Alert System Using Twilio and OpenWeatherMap

This script sends a WhatsApp message alert if rain is forecasted in your location. It uses the OpenWeatherMap API to fetch weather data and Twilio to send the alert via WhatsApp.

## Features

- Checks weather forecasts for the next 9 hours using the OpenWeatherMap API.
- Detects if rain is expected during this time.
- Sends an alert via WhatsApp using Twilio if rain is detected.

## Prerequisites

- Python 3.8 or later.
- Twilio account with a verified phone number for WhatsApp messaging.
- OpenWeatherMap API key.

## Setup and Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Pooja389/rain_tracker.git
   cd rain_tracker
   ```

2. **install required package**
   pip install requests twilio


3. **Configure the Script:** Replace the placeholder values in the script with your credentials and information:

  auth_token: Your Twilio Auth Token.
  acc_sid: Your Twilio Account SID.
  my_loc_lat: Your latitude.
  my_loc_lon: Your longitude.
  api_key: Your OpenWeatherMap API key.
  +your_verified_number: Your verified WhatsApp number.  
  
## Run the script using python 
  ```bash
  python rain.py 

   
