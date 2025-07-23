import streamlit as st
import pandas as pd
import pickle

# Load trained model
from keras.models import load_model
model = load_model("model.keras")  # ✅ no pickle

st.title("🏦 Bank Customer Churn Prediction")
st.write("Enter customer details to check if they are likely to leave the bank.")

# Input form
credit_score = st.number_input("Credit Score", min_value=300, max_value=900, value=650)
age = st.number_input("Age", min_value=18, max_value=100, value=35)
tenure = st.slider("Tenure (years with bank)", 0, 10, 5)
balance = st.number_input("Balance", value=75000.0)
products = st.selectbox("Number of Products", [1, 2, 3, 4])
has_cr_card = st.radio("Has Credit Card?", ["Yes", "No"])
is_active = st.radio("Is Active Member?", ["Yes", "No"])
salary = st.number_input("Estimated Salary", value=50000.0)
gender = st.radio("Gender", ["Male", "Female"])
geography = st.selectbox("Geography", ["France", "Germany", "Spain"])

# Encode categorical fields
male = 1 if gender == "Male" else 0
germany = 1 if geography == "Germany" else 0
spain = 1 if geography == "Spain" else 0

if st.button("Predict"):
    input_data = pd.DataFrame([{
        "CreditScore": credit_score,
        "Age": age,
        "Tenure": tenure,
        "Balance": balance,
        "NumOfProducts": products,
        "HasCrCard": 1 if has_cr_card == "Yes" else 0,
        "IsActiveMember": 1 if is_active == "Yes" else 0,
        "EstimatedSalary": salary,
        "Germany": germany,
        "Spain": spain,
        "Male": male
    }])

    result = model.predict(input_data)[0]

    if result == 1:
        st.error("🔴 Customer is likely to leave the bank.")
    else:
        st.success("🟢 Customer will stay with the bank.")
