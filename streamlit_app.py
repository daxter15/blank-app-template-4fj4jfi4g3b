# Weather API Python

import requests
#import json
from random import choice

import streamlit as st
# pip install streamlit (wrap in try to install ??)


title_str = ("Weather API App :mostly_sunny:")# declared here as variable due to the function use later.
st.title(title_str)
st.header("Current Weather:")


# 50.819965116480034, -1.212066575041191
lat = "50.81"
long = "-1.21"


def conv_kmh_mph(kmh):
    global mph
    mph = round((kmh / 1.609344), 1)
    return str(mph)

# r = requests.get("https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m")

weather_api_pull = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&current=temperature_2m,wind_speed_10m,relative_humidity_2m")
#### Add in humidity again?
### "relative_humidity_2m"

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

    ### Title to change with current weather?...
    ### https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/
    ### 
    ### 371	🌤️	:mostly_sunny:
    ### 372	🌤️	:sun_small_cloud:
    ### 373	🌥️	:barely_sunny:
    ### 374	🌥️	:sun_behind_cloud:
    ### 375	🌦️	:partly_sunny_rain:
    ### 376	🌦️	:sun_behind_rain_cloud:
    ### 377	🌧️	:rain_cloud:
    ### 378	🌨️	:snow_cloud:
    ### 379	🌩️	:lightning:
    ### 380	🌩️	:lightning_cloud:
    ### 1758	☀️	:sunny:
    ### 1759	☁️	:cloud:
    ### 1760	☂️	:umbrella:
    ### 1854	❄️	:snowflake:



## Streamlit metrics
# st.metric(label, value, delta=None, delta_color="normal", help=None, label_visibility="visible")
# st.metric("Temperature", current_temp, delta=yesterday_temp_compare)

# Get yesterdays details temp
previous_day_weather_api_pull = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&past_days=1&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m")
#previous_day = previous_day_weather_api_pull.json()
#print(previous_day_weather_api_pull.json())

# find the current hour
from datetime import datetime
#print(datetime.now())
#print(datetime.now().hour)
yesterday_now_temp = (previous_day_weather_api_pull.json()['hourly']['temperature_2m'][((datetime.now().hour) -1)])
#print(yesterday_now_temp)
yesterday_temp_compare = round((float(current_temp_deg[0]) - yesterday_now_temp), 1)
#print(type(current_temp_deg[0]))
#print(current_temp_deg[0])
#print(yesterday_temp_compare)
yesterday_now_wind = (previous_day_weather_api_pull.json()['hourly']['wind_speed_10m'][((datetime.now().hour) -1)])
# convert to mph
yesterday_now_wind_mph = conv_kmh_mph(yesterday_now_wind)
#print(yesterday_now_wind_mph)
yesterday_wind_compare = round((float(current_wind_mph) - float(yesterday_now_wind_mph)), 1)
#print(yesterday_wind_compare)
#print(yesterday_now_wind_mph)

## Humidity
current_humidity_str = str((weather_api_pull.json()['current']['relative_humidity_2m'])), ((weather_api_pull.json()['current_units']['relative_humidity_2m']))
current_humidity = (weather_api_pull.json()['current']['relative_humidity_2m'])
print(current_humidity)
yesterday_now_humidity = (previous_day_weather_api_pull.json()['hourly']['relative_humidity_2m'][((datetime.now().hour) -1)])
yesterday_humidity_compare =  (int(current_humidity) - int(yesterday_now_humidity))



# Adding columns
col1, col2, col3 = st.columns(2)

col1.metric("Temperature", current_temp_deg_str, yesterday_temp_compare)
### Delta should be the differential between current and previous (otherwise it always flags as a positive change)

col2.metric("Wind Speed", current_wind_mph_str, yesterday_wind_compare)

col3.metric("Humidity", current_humidity_str, yesterday_humidity_compare)

#### ----- ####
# Add A Button to update results (test)
#https://docs.streamlit.io/develop/api-reference/widgets/st.button

title_str_list = [
        ":mostly_sunny:",
        ":sun_small_cloud:",
        ":barely_sunny:",
        ":sun_behind_cloud:",
        ":partly_sunny_rain:",
        ":sun_behind_rain_cloud:",
        ":rain_cloud:",
        ":snow_cloud:",
        ":lightning:",
        ":lightning_cloud:",
        ":sunny:",
        ":cloud:",
        ":umbrella:",
        ":snowflake:"
        ]

def secret_button_title_change():
    
    global title_str
    title_str = ("Weather API App " + (choice(title_str_list))) # Use choice to select a random title emoji from list
    ## Add in check to avoid duplicate meaning no change?


    st.title(title_str) # Does not work...adds a new title..
    

if st.button("'Secret' Button...:grey_question:", "button_1_secret", "Secret button does secret things..."):
    secret_button_title_change() # Does not work... adds a new Title..

x = st.slider('Secrets!!', 1, 13)
st.write(title_str_list[x])




#### ----- ####