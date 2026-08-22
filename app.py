import streamlit as st
import pandas as pd
import pickle
import matplotlib.pyplot as plt

# Page setup
st.set_page_config(page_title="Chennai Weather Dashboard", layout="wide")
st.title("🌤️ Chennai Weather Trends & Prediction")

# Load data
df = pd.read_csv("data/chennai_weather_raw.csv", index_col="time", parse_dates=True)

# Load trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# --- Sidebar controls ---
st.sidebar.header("Filters")
date_range = st.sidebar.date_input(
    "Select date range",
    value=(df.index.min(), df.index.max()),
    min_value=df.index.min(),
    max_value=df.index.max()
)

metric = st.sidebar.selectbox(
    "Select metric to visualize",
    ["temperature_2m_max", "temperature_2m_min", "precipitation_sum", "relative_humidity_2m_mean"]
)

# Filter data based on selected date range
if len(date_range) == 2:
    start, end = date_range
    filtered_df = df.loc[str(start):str(end)]
else:
    filtered_df = df

# --- Main chart ---
st.subheader(f"{metric} over time")
fig, ax = plt.subplots(figsize=(12, 5))
ax.plot(filtered_df.index, filtered_df[metric], color="steelblue")
ax.set_xlabel("Date")
ax.set_ylabel(metric)
st.pyplot(fig)

# --- Prediction section ---
st.subheader("🔮 Predict Tomorrow's Max Temperature")

col1, col2, col3 = st.columns(3)
with col1:
    temp_max = st.number_input("Today's Max Temp (°C)", value=32.0)
    temp_min = st.number_input("Today's Min Temp (°C)", value=25.0)
with col2:
    precip = st.number_input("Today's Rainfall (mm)", value=0.0)
    humidity = st.number_input("Today's Humidity (%)", value=75.0)
with col3:
    windspeed = st.number_input("Today's Windspeed (km/h)", value=15.0)
    trend_3day = st.number_input("3-Day Avg Max Temp (°C)", value=32.0)

if st.button("Predict"):
    input_data = pd.DataFrame([[temp_max, temp_min, precip, humidity, windspeed, trend_3day]],
                                columns=["temperature_2m_max", "temperature_2m_min", "precipitation_sum",
                                         "relative_humidity_2m_mean", "windspeed_10m_max", "temp_trend_3day"])
    prediction = model.predict(input_data)[0]
    st.success(f"Predicted tomorrow's max temperature: **{prediction:.1f}°C**")