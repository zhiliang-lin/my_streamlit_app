import streamlit as st
import pandas as pd

# To run the app type this in terminal "streamlit run Install_and_firstAPP.py"

st.title("Hello Streamlit")
st.write("This is my first Streamlit app!")
number = st.slider("Pick a number", 0, 100)
st.write("You picked:", number)
df = pd.DataFrame({"x": range(number), "y": [i**2 for i in range(number)]})
st.line_chart(df)