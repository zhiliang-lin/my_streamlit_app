import streamlit as st
import pandas as pd
import numpy as np
import time


# To run the app type this in terminal "streamlit run MoreOption.py"

st.set_page_config(page_title="Streamlit Showcase", layout="wide")

st.title("Streamlit Full Feature Showcase App")

st.markdown("""
This app demonstrates a wide range of **Streamlit** features:
- Text and layout
- Widgets
- Media
- Charts
- Dataframes and tables
- File upload & download
- Progress indicators
- Session state
- Columns, tabs, expanders
- Caching
- Forms
- Chat elements
""")

# --- Text Elements ---
st.header("Text & Layout")
st.subheader("Markdown, Code, and Alerts")
st.markdown("Here is some **bold text**, *italic text*, and `inline code`.")
st.code("print('Hello Streamlit!')")
st.success("Success message example.")
st.warning("Warning example.")
st.error("Error message example.")

# --- Widgets ---
st.header("Widgets Showcase")
name = st.text_input("Your name:")
age = st.number_input("Your age:", 0, 120)
option = st.selectbox("Choose an option:", ["A", "B", "C"])
slider = st.slider("Pick a number", 0, 100)
date = st.date_input("Pick a date")
checkbox = st.checkbox("Enable advanced features")
rating = st.radio("Rate Streamlit:", ["⭐", "⭐⭐", "⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"])

st.write("### Widget Values:")
st.json({"name": name, "age": age, "option": option, "slider": slider, "date": str(date), "rating": rating})

# --- Columns ---
st.header("Columns & Layout")
col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "72 °F", "+2")
col2.metric("Sales", "1,200", "-5%")
col3.metric("Visitors", "5,431", "+12%")

# --- Tabs ---
st.header("Tabs Example")
tab1, tab2, tab3 = st.tabs(["Chart", "Dataframe", "Code"])

with tab1:
    chart_data = pd.DataFrame(np.random.randn(30, 3), columns=list("ABC"))
    st.line_chart(chart_data)

with tab2:
    st.dataframe(chart_data)

with tab3:
    st.code("st.line_chart(chart_data)")

# --- File Upload ---
st.header("File Upload & Download")
uploaded = st.file_uploader("Upload CSV", type=["csv"])
if uploaded:
    df = pd.read_csv(uploaded)
    st.dataframe(df)
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button("Download Processed CSV", csv, "processed.csv")

# --- Media ---
st.header("Images, Videos, Audio")
st.image("https://streamlit.io/images/brand/streamlit-mark-color.png", width=200)
st.audio(bytes(np.random.randint(0, 255, 20000)), format="audio/wav")
st.video("https://www.w3schools.com/html/mov_bbb.mp4")

# --- Progress Bars & Status ---
st.header("Progress & Status Indicators")
progress = st.progress(0)
for i in range(1, 101):
    time.sleep(0.005)
    progress.progress(i)

# --- Expander ---
st.header("Expander Example")
with st.expander("Click to expand more info"):
    st.write("Hidden content revealed.")

# --- Forms ---
st.header("Forms Example")
with st.form("survey_form"):
    q1 = st.selectbox("How satisfied are you?", [1, 2, 3, 4, 5])
    q2 = st.text_input("Any comments?")
    submitted = st.form_submit_button("Submit")

if submitted:
    st.success("Form submitted!")
    st.write({"satisfaction": q1, "comments": q2})

# --- Session State ---
st.header("Session State Example")
if "counter" not in st.session_state:
    st.session_state.counter = 0

if st.button("Increase Counter"):
    st.session_state.counter += 1

st.write("Counter value:", st.session_state.counter)

# --- Caching Example ---
st.header("Caching Example")
@st.cache_data
def slow_function():
    time.sleep(2)
    return "Finished expensive computation!"

if st.button("Run cached function"):
    st.write(slow_function())

# --- Chat Interface ---
st.header("Chat Interface Example")
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

prompt = st.chat_input("Say something…")
if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = f"Echo: {prompt}"
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.chat_message("assistant").write(response)

st.success("All Streamlit features showcased!")
