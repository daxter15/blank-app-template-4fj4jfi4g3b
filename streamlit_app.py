# Weather API Python

import requests

#import json

import streamlit as st
# pip install streamlit (wrap in try to install ??)

# 50.819965116480034, -1.212066575041191
lat = "50.81"
long = "-1.21ccc"

# r = requests.get("https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m")

weather_api_pull = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&current=temperature_2m,wind_speed_10m")

print(weather_api_pull.status_code)

if weather_api_pull.status_code != 200: # If status other than 200, then show error message
    print("Unable to contact Weather API")
    print(weather_api_pull.status_code)
    current_temp_deg_str = "Unable to contact Weather API"
    current_wind_mph_str = "Unable to contact Weather API"
else:
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
    current_temp_deg_str = str(str(current_temp_deg[0]) + current_temp_deg[1]) # Convert to string for use with st.metrics later

    # Wind Speed

    print(((weather_api_pull.json()['current']['wind_speed_10m'])), ((weather_api_pull.json()['current_units']['wind_speed_10m'])))

    current_wind_kmh = str((weather_api_pull.json()['current']['wind_speed_10m'])), ((weather_api_pull.json()['current_units']['wind_speed_10m']))
    current_wind_kmh_str = str(str(current_wind_kmh[0]) + current_wind_kmh[1]) # Convert to string for use with st.metrics later
    # Convert to mph
    current_wind_mph = round((((weather_api_pull.json()['current']['wind_speed_10m'])) / 1.609344), 1) # Current kmh / 1.609344 for mph
    current_wind_mph_str = (str(current_wind_mph) + "mph") # Convert float to str, then concatenate
    #print(current_wind_mph_str)


## Streamlit metrics
# st.metric(label, value, delta=None, delta_color="normal", help=None, label_visibility="visible")
# st.metric("Temperature", current_temp, delta=yesterday_temp_compare)

st.metric("Temperature", current_temp_deg_str)

st.metric("Wind Speed", current_wind_mph_str)
