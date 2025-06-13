import streamlit as st
import numpy as np
import pandas as pd
import pickle

# Load the trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

st.title("🛒 Walmart Weekly Sales Prediction")

# --- Input fields based on your training features ---
store = st.number_input("Store", min_value=1, step=1)
dept = st.number_input("Department", min_value=1, step=1)
temperature = st.number_input("Temperature (°F)", value=70.0)
fuel_price = st.number_input("Fuel Price", value=3.0)
cpi = st.number_input("CPI (Consumer Price Index)", value=200.0)
unemployment = st.number_input("Unemployment Rate (%)", value=7.0)
holiday = st.selectbox("Is it a Holiday?", ["No", "Yes"])

# Add more if you used encoded features like:
year = st.number_input("Year", value=2012)
month = st.number_input("Month", min_value=1, max_value=12)
week = st.number_input("Week", min_value=1, max_value=53)
day = st.number_input("Day", min_value=1, max_value=31)
day_of_week = st.number_input("Day of Week", min_value=0, max_value=6)

# --- Build input array ---
input_data = np.array([[store, dept, temperature, fuel_price, cpi, unemployment,
                        1 if holiday == "Yes" else 0,
                        year, month, week, day, day_of_week]])

# --- Predict ---
if st.button("Predict Weekly Sales"):
    prediction = model.predict(input_data)[0]
    st.success(f"💰 Predicted Weekly Sales: ${prediction:,.2f}")
