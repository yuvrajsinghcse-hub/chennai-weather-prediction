import requests
import pandas as pd

url = "https://archive-api.open-meteo.com/v1/archive"

params = {
    "latitude": 13.0827,
    "longitude": 80.2707,
    "start_date": "2023-01-01",
    "end_date": "2024-12-31",
    "daily": [
        "temperature_2m_max",
        "temperature_2m_min",
        "precipitation_sum",
        "relative_humidity_2m_mean",
        "windspeed_10m_max"
    ],
    "timezone": "Asia/Kolkata"
}

response = requests.get(url, params=params)
data = response.json()

# Convert the daily data into a DataFrame
df = pd.DataFrame(data["daily"])
df["time"] = pd.to_datetime(df["time"])
df.set_index("time", inplace=True)

print(df.head())
df.to_csv("data/chennai_weather_raw.csv")