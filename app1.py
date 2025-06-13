import streamlit as st
import numpy as np
import pickle

# Load the trained model
model = pickle.load(open('model.pkl', 'rb'))

st.title("🛒 Walmart Weekly Sales Prediction")

# --- Input fields ---
store = st.number_input("Store", min_value=1.0)
dept = st.number_input("Department", min_value=1.0)
is_holiday = st.selectbox("Is Holiday?", ["No", "Yes"])
year = st.number_input("Year", value=2012.0)
month = st.number_input("Month", min_value=1.0, max_value=12.0)
week = st.number_input("Week", min_value=1.0, max_value=53.0)
day = st.number_input("Day", min_value=1.0, max_value=31.0)
dayofweek = st.number_input("Day of Week", min_value=0.0, max_value=6.0)
temperature = st.number_input("Temperature (°F)", value=70.0)
fuel_price = st.number_input("Fuel Price", value=3.0)
markdown1 = st.number_input("MarkDown1", value=0.0)
markdown2 = st.number_input("MarkDown2", value=0.0)
markdown3 = st.number_input("MarkDown3", value=0.0)
markdown4 = st.number_input("MarkDown4", value=0.0)
markdown5 = st.number_input("MarkDown5", value=0.0)
cpi = st.number_input("CPI", value=200.0)
unemployment = st.number_input("Unemployment Rate (%)", value=7.0)
size = st.number_input("Store Size", value=150000.0)

# Store Type (A, B, C) - one-hot encoded
store_type = st.selectbox("Store Type", ["A", "B", "C"])
type_a = 1 if store_type == "A" else 0
type_b = 1 if store_type == "B" else 0
type_c = 1 if store_type == "C" else 0

# --- Convert is_holiday to binary ---
is_holiday = 1 if is_holiday == "Yes" else 0

# --- Prediction ---
if st.button("Predict Weekly Sales"):
    features = [[store, dept, is_holiday, year, month, week, day, dayofweek,
                 temperature, fuel_price, markdown1, markdown2, markdown3,
                 markdown4, markdown5, cpi, unemployment, size,
                 type_a, type_b, type_c]]

    prediction = model.predict(features)[0]
    st.success(f"💰 Predicted Weekly Sales: ${prediction:,.2f}")
