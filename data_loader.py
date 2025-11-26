import pandas as pd
import streamlit as st

CO2_URL = "https://raw.githubusercontent.com/owid/co2-data/master/owid-co2-data.csv"
CENTROID_URL = "data/country_centroids.csv"


@st.cache_data
def load_demo_data():
    df = pd.read_csv(CO2_URL)
    centroids = pd.read_csv(CENTROID_URL)

    # Standardize column names
    centroids.rename(columns={
        "iso_code": "iso_code",
        "latitude": "lat",
        "longitude": "lon"
    }, inplace=True)

    # Merge CO2 dataset with coordinates
    merged = df.merge(centroids[["iso_code", "lat", "lon"]], on="iso_code", how="left")

    return merged