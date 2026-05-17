# -----------------------------
# PAGE CONFIG
# -----------------------------

st.set_page_config(
    page_title="DriveValue Nigeria",
    page_icon="🚗",
    layout="centered"
)

# -----------------------------
# LOAD MODEL
# -----------------------------

model = joblib.load("car_price_model.joblib")

# -----------------------------
# APP TITLE
# -----------------------------

st.title("🚗 Car Price Prediction App")
st.markdown(st.write("Predict the estimated price of your car instantly.")

st.divider()

# -----------------------------
# SELECT BOX OPTIONS
# -----------------------------

makes = [
    "Toyota",
    "Honda",
    "Mercedes-Benz",
    "BMW",
    "Lexus",
    "Hyundai",
    "Kia",
    "Ford",
    "Nissan",
    "Volkswagen"
]

models = [
    "Camry",
    "Corolla",
    "Accord",
    "Civic",
    "GLE",
    "C300",
    "E350",
    "RX350",
    "ES350",
    "Tucson",
    "Elantra",
    "Sportage",
    "Explorer",
    "Passat"
]

fuel_types = [
    "Petrol",
    "Diesel",
    "Hybrid",
    "Electric"
]

transmissions = [
    "Automatic",
    "Manual"
]

# -----------------------------
# USER INPUTS
# -----------------------------

make = st.selectbox("Select Car Make", makes)

car_model = st.selectbox("Select Car Model", models)

year = st.number_input(
    "Year of Manufacture",
    min_value=1990,
    max_value=2026,
    value=2018
)

mileage = st.number_input(
    "Mileage (km)",
    min_value=0,
    value=50000
)

engine_size = st.number_input(
    "Engine Size",
    min_value=0.8,
    max_value=10.0,
    value=2.0,
    step=0.1
)

fuel = st.selectbox("Fuel Type", fuel_types)

transmission = st.selectbox("Transmission", transmissions)

# -----------------------------
# PREDICT BUTTON
# -----------------------------

if st.button("Predict Price"):

    input_data = pd.DataFrame({
        'Year of manufacture': [year],
        'Mileage': [mileage],
        'Engine Size': [engine_size]
    })

    # -----------------------------
    # ADD DUMMY COLUMNS
    # -----------------------------

    dummy_columns = [
        'Make_Toyota',
        'Make_Honda',
        'Make_Mercedes-Benz',
        'Make_BMW',
        'Make_Lexus',
        'Make_Hyundai',
        'Make_Kia',
        'Make_Ford',
        'Make_Nissan',
        'Make_Volkswagen',
        'Model_Camry',
        'Model_Corolla',
        'Model_Accord',
        'Model_Civic',
        'Model_GLE',
        'Model_C300',
        'Model_E350',
        'Model_RX350',
        'Model_ES350',
        'Model_Tucson',
        'Model_Elantra',
        'Model_Sportage',
        'Model_Explorer',
        'Model_Passat',
        'Fuel_Petrol',
        'Fuel_Diesel',
        'Fuel_Hybrid',
        'Fuel_Electric',
        'Transmission_Automatic',
        'Transmission_Manual'
    ]

    for col in dummy_columns:
        input_data[col] = 0

    # -----------------------------
    # SET SELECTED VALUES TO 1
    # -----------------------------

    make_col = f"Make_{make}"
    model_col = f"Model_{car_model}"
    fuel_col = f"Fuel_{fuel}"
    trans_col = f"Transmission_{transmission}"

    if make_col in input_data.columns:
        input_data[make_col] = 1

    if model_col in input_data.columns:
        input_data[model_col] = 1

    if fuel_col in input_data.columns:
        input_data[fuel_col] = 1

    if trans_col in input_data.columns:
        input_data[trans_col] = 1

    # -----------------------------
    # PREDICTION
    # -----------------------------

    prediction = model.predict(input_data)[0]

    st.success(f"Estimated Car Price: ₦{prediction:,.0f}")
