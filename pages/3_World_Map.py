import streamlit as st
import pandas as pd
import pydeck as pdk
from data_loader import load_demo_data
import numpy as np

st.title("Global CO₂ Emissions Map")

df = load_demo_data()

# Filter out aggregates (OWID_* codes)
df = df[~df["iso_code"].str.contains("OWID", na=False)]

# Allow user to select year
years = sorted(df["year"].dropna().unique())
default_year = max(years)

year = st.slider("Select year", min_value=min(years), max_value=max(years), value=default_year)

# Filter for selected year
df_year = df[df["year"] == year].dropna(subset=["lat", "lon"])

# Create a color gradient based on CO2 emissions
# Normalize CO2 for color scaling
co2_min = df_year["co2"].min()
co2_max = df_year["co2"].max()
co2_range = co2_max - co2_min if co2_max != co2_min else 1

def co2_to_color(x):
    """
    Map CO2 emission value to RGB color.
    Green (low) → Yellow → Red (high)
    """
    norm = (x - co2_min) / co2_range  # normalize 0-1
    r = int(255 * norm)
    g = int(255 * (1 - norm))
    b = 0
    return [r, g, b]

df_year["color"] = df_year["co2"].fillna(0).apply(co2_to_color)

st.subheader(f"CO₂ Emissions Map — {year}")

# Render map
view_state = pdk.ViewState(
    latitude=20,
    longitude=0,
    zoom=1.2,
    pitch=0,
)

layer = pdk.Layer(
    "ScatterplotLayer",
    df_year,
    get_position=["lon", "lat"],
    get_radius=50000,
    get_fill_color="color",
    pickable=True,
)

tooltip = {
    "html": "<b>{country}</b><br>CO₂: {co2} Mt",
    "style": {"color": "white"}
}

r = pdk.Deck(
    layers=[layer],
    initial_view_state=view_state,
    tooltip=tooltip
)

st.pydeck_chart(r)

# Display a legend
st.markdown("""
**Color Legend:**  
- 🟢 Low emissions  
- 🟡 Medium emissions  
- 🔴 High emissions
""")