import streamlit as st
import pickle
import numpy as np

# Load the trained XGBoost model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

st.title("🛒 Walmart Weekly Sales Prediction")
st.markdown("Predict weekly sales using key inputs below.")

# --- User Input Fields ---
store = st.number_input("Store ID", min_value=1, max_value=100, step=1)
dept = st.number_input("Department ID", min_value=1, max_value=100, step=1)
temperature = st.number_input("Temperature (°F)", value=70.0)
cpi = st.number_input("CPI (Consumer Price Index)", value=200.0)
unemployment = st.number_input("Unemployment Rate (%)", value=7.0)
is_holiday = st.selectbox("Is it a Holiday?", options=[0, 1], format_func=lambda x: "Yes" if x == 1 else "No")

# --- Prediction ---
if st.button("Predict Weekly Sales"):
    input_data = np.array([[store, dept, temperature, cpi, unemployment, is_holiday]])
    prediction = model.predict(input_data)[0]
    st.success(f"💰 Predicted Weekly Sales: ${prediction:,.2f}")
