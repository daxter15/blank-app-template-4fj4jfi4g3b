import streamlit as st
import time
import numpy as np
import requests

st.set_page_config(page_title="Temperature 10 day plot", page_icon="📈")

st.markdown("# Temperature 10 day plot")
st.sidebar.header("Temperature 10 day plot")
st.write(
    """This shows a plot of the temperature for the last 10 days."""
)

progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()
#last_rows = np.random.randn(1, 1)


lat = "50.81"
long = "-1.21"

temperature_api = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&past_days=10&hourly=temperature_2m")
print(temperature_api.json()['hourly'])

print(type(temperature_api.json()['hourly']))
print(temperature_api.json()['hourly'].keys())

#chart = st.line_chart(temperature_api.json()['hourly']['time'][:], temperature_api.json()['hourly']['temperature_2m'][:], "Date and Time", "Temperature (°C)")
#chart = st.line_chart(temperature_api.json()['hourly']['temperature_2m'], "Date and Time", "Temperature (°C)")

chart = st.line_chart()

for i in (temperature_api.json()['hourly']['temperature_2m'][:]):
    new_rows = last_rows + i
    chart.add_rows(new_rows)
    last_rows = new_rows

print(chart)
#   progress_bar.progress(i)    


# for i in range(1, 101):
#     new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
#     status_text.text("%i%% Complete" % i)
#     chart.add_rows(new_rows)
#     progress_bar.progress(i)
#     last_rows = new_rows
#     time.sleep(0.05)

chart = st.line_chart()


progress_bar.empty()

# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Re-run")