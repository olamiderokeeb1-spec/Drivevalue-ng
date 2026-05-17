import streamlit as st
import pandas as pd
import joblib

# Page setup
st.set_page_config(page_title="Car Price Predictor", page_icon="🚗")

# Load files
model = joblib.load("car_price_model.joblib")
scaler = joblib.load("car_price_scaler.joblib")
columns = joblib.load("car_price_columns.joblib")

# Title
st.title("🚗 Car Price Prediction App")
st.write("Predict the estimated price of your car instantly.")

# Inputs
fuel_type = st.selectbox("⛽️ Fuel Type", ["Petrol", "Diesel"])
gear_type = st.selectbox("⚙️ Gear Type", ["Automatic", "Manual"])
make = st.text_input("🏢 Car Make")
model_name = st.text_input("🚘 Car Model")
year = st.number_input("📅 Year", 1990, 2026)
condition = st.selectbox(
    "📌 Condition",
    ["Nigerian Used", "Foreign Used", "Brand New"]
)
mileage = st.number_input("🛣 Mileage")
engine_size = st.number_input("🔧 Engine Size")

# Predict button
if st.button("🚀 Predict Price"):

    input_data = pd.DataFrame([{
        'fuel type': fuel_type,
        'gear type': gear_type,
        'Make': make,
        'Model': model_name,
        'Year of manufacture': year,
        'Condition': condition,
        'Mileage': mileage,
        'Engine Size': engine_size
    }])

    # Convert categorical data
    input_data = pd.get_dummies(input_data)

    # Match columns
    input_data = input_data.reindex(
        columns=columns,
        fill_value=0
    )

    # Scale
    input_scaled = scaler.transform(input_data)

    # Predict
    prediction = model.predict(input_scaled)

    # Output
    st.success(f"💰 Estimated Price: ₦{prediction[0]:,.0f}")
    st.success(f"Estimated Car Price: ₦{prediction:,.0f}")
