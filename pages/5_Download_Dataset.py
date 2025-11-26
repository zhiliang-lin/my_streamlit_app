import streamlit as st
from data_loader import load_demo_data

st.title("Download CO₂ Dataset")

df = load_demo_data()

csv = df.to_csv(index=False).encode('utf-8')
st.download_button("Download CSV", csv, "owid_co2_dataset.csv", "text/csv")