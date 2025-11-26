import streamlit as st
import pandas as pd
from data_loader import load_demo_data

st.title("Global CO₂ Dashboard")

df = load_demo_data()
countries = df[~df["iso_code"].str.contains("OWID", na=False)]

latest_year = countries['year'].max()
latest = countries[countries['year'] == latest_year]

col1, col2, col3 = st.columns(3)
col1.metric("🌐 Total Global CO₂ (Mt)", f"{latest['co2'].sum():,.0f}")
col2.metric("🔌 Avg CO₂ per capita", f"{latest['co2_per_capita'].mean():.2f}")
col3.metric("📈 Global Population", f"{latest['population'].sum():,.0f}")

st.subheader("Top 10 Emitters")
top10 = latest.sort_values(by="co2", ascending=False).head(10)
st.bar_chart(top10.set_index("country")["co2"])