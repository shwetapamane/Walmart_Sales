import streamlit as st
import numpy as np
import pandas as pd
import pickle

# Load the trained XGBoost model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# Load the columns used during training
#with open('columns.pkl', 'rb') as file:
#    feature_columns = pickle.load(file)

st.title("🛒 Walmart Weekly Sales Prediction")
st.markdown("### Predict weekly sales using key inputs below.")

# User inputs
store = st.number_input("Store ID", min_value=1, step=1)
dept = st.number_input("Department ID", min_value=1, step=1)
temperature = st.number_input("Temperature (°F)", value=70.0)
cpi = st.number_input("CPI (Consumer Price Index)", value=200.0)
unemployment = st.number_input("Unemployment Rate (%)", value=7.0)
holiday = st.selectbox("Is it a Holiday?", ["No", "Yes"])

# Create a dictionary for inputs
input_dict = {
    'Store': store,
    'Dept': dept,
    'Temperature': temperature,
    'CPI': cpi,
    'Unemployment': unemployment,
    'IsHoliday': 1 if holiday == "Yes" else 0
}

# Add default 0s for all other features used during training
for col in feature_columns:
    if col not in input_dict:
        input_dict[col] = 0

# Create input DataFrame in the correct column order
input_df = pd.DataFrame([input_dict])
input_df = input_df[feature_columns]

# Prediction
if st.button("Predict Weekly Sales"):
    prediction = model.predict(input_df)[0]
    st.success(f"💰 Predicted Weekly Sales: ${prediction:,.2f}")
