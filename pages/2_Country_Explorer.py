import streamlit as st
import altair as alt
from data_loader import load_demo_data

st.title("Country CO₂ Explorer")

df = load_demo_data()
countries = df[~df["iso_code"].str.contains("OWID", na=False)]

country = st.selectbox("Select a country:", sorted(countries["country"].unique()))
dfc = countries[countries["country"] == country]

st.subheader(f"CO₂ Emissions Over Time — {country}")

chart = alt.Chart(dfc).mark_line().encode(
    x='year',
    y='co2',
    tooltip=['year', 'co2']
)

st.altair_chart(chart, use_container_width=True)