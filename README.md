# 🌤️ Chennai Weather Trends & Prediction

An interactive data science app that analyzes 2 years of daily Chennai weather data and predicts next-day maximum temperature using a Random Forest model.

**[Live Demo](#)** &nbsp;·&nbsp; Built with Python, pandas, scikit-learn, and Streamlit

![App Screenshot](screenshot.png)
<!-- Replace screenshot.png with an actual screenshot or GIF of your app before publishing -->

---

## 📌 Overview

This project pulls historical daily weather data for Chennai (Jan 2023 – Dec 2024) from the [Open-Meteo Historical Weather API](https://open-meteo.com/en/docs/historical-weather-api), explores seasonal patterns in temperature and rainfall, and trains a regression model to predict tomorrow's maximum temperature from today's conditions. The full pipeline — data collection, EDA, modeling, and an interactive dashboard — is included.

## 🔍 What I found (EDA highlights)

- Chennai's daily max temperature follows a clear seasonal wave, peaking near **40°C in April–June** and cooling to the mid-20s by December–January.
- Rainfall is heavily concentrated in short bursts rather than spread evenly across the year, consistent with Chennai's **Northeast monsoon (Oct–Dec)**. One single-day spike reached **~250mm**, a real extreme weather event rather than a data error.
- The gap between daily max and min temperature narrows during monsoon months, likely due to increased cloud cover reducing day-night temperature swing.

## 🤖 Modeling

A `RandomForestRegressor` was trained to predict next-day maximum temperature using same-day weather features (max/min temp, rainfall, humidity, windspeed) plus a 3-day rolling temperature trend.

| Model | Mean Absolute Error |
|---|---|
| Naive baseline (predict "tomorrow = today") | 0.93°C |
| Random Forest (same-day features only) | 0.92°C |
| Random Forest + 3-day trend feature | **0.88°C** |

**Takeaway:** Chennai's day-to-day temperature is highly autocorrelated, so a naive baseline is already fairly strong. Adding a short-term trend feature gave a modest but real improvement, suggesting temperature momentum carries some predictive signal beyond same-day conditions alone. Further gains would likely require lagged features over a longer window or external variables like monsoon/El Niño indices.

## 🖥️ App features

- **Interactive time series chart** — filter by date range and switch between temperature, rainfall, and humidity
- **Live prediction tool** — enter today's weather conditions and get a predicted max temperature for tomorrow, powered by the trained model

## 🛠️ Tech stack

- **Data source:** Open-Meteo Historical Weather API (no key required)
- **Data handling:** pandas
- **Visualization:** matplotlib, seaborn
- **Modeling:** scikit-learn (RandomForestRegressor)
- **App:** Streamlit

## 📁 Project structure

```
DS project/
├── data/
│   └── chennai_weather_raw.csv
├── notebooks/
│   └── eda.ipynb          # data cleaning, EDA, model training & evaluation
├── app.py                  # Streamlit app
├── model.pkl                # trained model, saved from the notebook
├── fetch_weather.py        # script to pull data from Open-Meteo
├── requirements.txt
└── README.md
```

## ▶️ Running it locally

```bash
# clone the repo
git clone <your-repo-url>
cd "DS project"

# install dependencies
pip install -r requirements.txt

# (optional) re-fetch the latest data
python fetch_weather.py

# launch the app
streamlit run app.py
```

## 🚀 Possible next steps

- Add lagged features over a longer window (e.g., 7-day, 14-day trends)
- Incorporate external variables (monsoon indices, sea surface temperature)
- Extend the app to predict rainfall or humidity, not just temperature
- Deploy permanently on Streamlit Community Cloud

---

*Built as part of my application to GDG on Campus VIT Chennai — Data Science track.*
