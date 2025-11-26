import streamlit as st
import numpy as np
import altair as alt
import pandas as pd
from sklearn.linear_model import LinearRegression
from data_loader import load_demo_data

st.title("CO₂ Forecasting")

df = load_demo_data()
countries = df[~df["iso_code"].str.contains("OWID", na=False)]

country = st.selectbox("Select a country:", sorted(df["country"].unique()))
dfc = df[df["country"] == country][["year", "co2"]].dropna()

model = LinearRegression()
model.fit(dfc[["year"]], dfc["co2"])

future_years = np.arange(2025, 2051).reshape(-1, 1)
forecast = model.predict(future_years)

forecast_df = {
    "year": future_years.flatten(),
    "predicted_co2": forecast
}

chart = alt.Chart(pd.DataFrame(forecast_df)).mark_line(color="red").encode(
    x="year",
    y="predicted_co2"
)

st.altair_chart(chart, use_container_width=True)