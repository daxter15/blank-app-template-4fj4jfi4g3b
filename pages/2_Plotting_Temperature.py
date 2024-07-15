import streamlit as st
import requests

st.set_page_config(page_title="Temperature 10 day plot", page_icon="📈")

st.markdown("# Temperature 10 day plot")
st.sidebar.header("Temperature 10 day plot")
st.write(
    """This shows a plot of the temperature for the last 10 days."""
)

#progress_bar = st.sidebar.progress(0)
#status_text = st.sidebar.empty()
#last_rows = np.random.randn(1, 1)


lat = "50.81"
long = "-1.21"

temperature_api = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&past_days=10&hourly=temperature_2m")
print(temperature_api.json()['hourly'])

print(type(temperature_api.json()['hourly']))
print(temperature_api.json()['hourly'].keys())

#chart = st.line_chart(temperature_api.json()['hourly']['time'][:], temperature_api.json()['hourly']['temperature_2m'][:], "Date and Time", "Temperature (°C)")
##chart = st.line_chart(temperature_api.json()['hourly']['temperature_2m'], "Date and Time", "Temperature (°C)")

chart_data = ((temperature_api.json()['hourly']['temperature_2m']))
#print(type(chart_data))
#print(chart_data[:])
### chart = st.line_chart(chart_data) ## Removed as updated by chart2 with more details.
chart_data = ((temperature_api.json()['hourly']['temperature_2m']))
chart2 = st.line_chart((temperature_api.json()['hourly']), x='time', y='temperature_2m', x_label='Time', y_label='Temperature')
#chart2 = st.line_chart(chart_data_dict_test, "temperature_2m", "time")

# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Re-run")