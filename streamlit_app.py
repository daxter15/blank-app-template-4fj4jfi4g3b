import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
    # Weather API Python

import requests

import json

import streamlit as st
# pip install streamlit (wrap in try to install ??)

# 50.819965116480034, -1.212066575041191
lat = "50.81"
long = "-1.21"

# r = requests.get("https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m")

weather_api_pull = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&current=temperature_2m,wind_speed_10m")

if weather_api_pull.status_code == 404:
    print("Unable to contact Weather API")
    print(weather_api_pull.status_code)
    exit()

print(type(weather_api_pull.json()))
print(weather_api_pull.json())
print(((weather_api_pull.json().keys())))
# get the current temp
print(((weather_api_pull.json()['current']['temperature_2m'])))
# get the current temp units
print(((weather_api_pull.json()['current_units']['temperature_2m'])))
# get the current wind_speed
print(((weather_api_pull.json()['current']['wind_speed_10m'])))
# get the current wind speed units
print(((weather_api_pull.json()['current_units']['wind_speed_10m'])))
# Put em together and whaddya get...
# Temp
print(((weather_api_pull.json()['current']['temperature_2m'])), ((weather_api_pull.json()['current_units']['temperature_2m'])))
current_temp_deg = str((weather_api_pull.json()['current']['temperature_2m'])), ((weather_api_pull.json()['current_units']['temperature_2m']))

# Wind Speed

print(((weather_api_pull.json()['current']['wind_speed_10m'])), ((weather_api_pull.json()['current_units']['wind_speed_10m'])))
### Convert to mph?
current_wind_kmh = str((weather_api_pull.json()['current']['wind_speed_10m'])), ((weather_api_pull.json()['current_units']['wind_speed_10m']))




#$ curl "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"

# {
#   "current": {
#     "time": "2022-01-01T15:00"
#     "temperature_2m": 2.4,
#     "wind_speed_10m": 11.9,
#   },
#   "hourly": {
#     "time": ["2022-07-01T00:00","2022-07-01T01:00", ...]
#     "wind_speed_10m": [3.16,3.02,3.3,3.14,3.2,2.95, ...],
#     "temperature_2m": [13.7,13.3,12.8,12.3,11.8, ...],
#     "relative_humidity_2m": [82,83,86,85,88,88,84,76, ...],
#   }
# }


## Streamlit metrics
# st.metric(label, value, delta=None, delta_color="normal", help=None, label_visibility="visible")
# st.metric("Temperature", current_temp, delta=yesterday_temp_compare)

st.metric("Temperature", current_temp_deg[0], current_temp_deg[1])

st.metric("Wind Speed", current_wind_kmh[0], current_wind_kmh[1])

