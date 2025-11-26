import streamlit as st
from data_loader import load_demo_data

# To run the app type this in terminal "streamlit run main.py"

st.set_page_config(
    page_title="Multipage Streamlit App",
    layout="wide"
)

st.title("🌐 Multi-Page Streamlit App")
st.subheader("A complete demonstration of Streamlit pages, widgets, caching, charts, and ML")

st.title("Global CO₂ Emissions Explorer")
st.write("""
Welcome to the **CO₂ Emissions Analysis App**, powered by the  
**Our World in Data (OWID) CO₂ dataset**.

Use the sidebar to navigate:
- Global dashboard  
- Country-level explorer  
- Interactive world map  
- Forecasting  
- Dataset download  
""")

st.divider()
st.write("### Demo dataset preview")
df = load_demo_data()
st.dataframe(df, use_container_width=True)